#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
# ]
# ///
"""
PreToolUse hook: while the uv plugin is enabled, every Python use must go through uv.

The hook reads the Bash command from stdin (JSON) and blocks it (exit 2, hint on
stderr) when any command position inside it runs Python or pip directly:

- `python`, `python3`, `python3.12`, `pythonw`, `pip`, `pip3`, `pip3.12`, and any
  path ending in those (`/usr/bin/python3`, `.venv/bin/python`).
- Command positions are found with a small quote-aware tokenizer: after `&&`, `||`,
  `;`, `|`, `&`, newlines, `(`, `$(`, backticks, `!`, `{`, `then`/`do`/`else`, leading
  `VAR=value` assignments, and wrappers (`sudo`, `env`, `exec`, `time`, `nohup`,
  `nice`, `timeout <dur>`, `xargs`, `command`, ...).
- `bash -c '...'`, `sh -c "..."`, `eval ...`, `$(...)`/backticks inside double quotes
  and heredocs fed to a shell (`bash <<EOF`) are scanned recursively. Other heredoc
  bodies are data and are ignored.
- A python executable that is the argument of `uv run` / `uvx` / `uv tool run` is
  allowed; so is any word that is not in command position (`grep python file`).
- `uv pip install` and `uv run pip install` are blocked with an `uv add` suggestion.

Each command position is judged independently, so `uv run a.py && python3 b.py` is
blocked. If the tokenizer fails, a coarser regex scan of the raw text is used instead.
"""

from __future__ import annotations

import json
import re
import shlex
import sys
from dataclasses import dataclass, field

MAX_DEPTH = 5  # nesting limit for bash -c / eval / $(...) payloads

PYTHON_RE = re.compile(r"python(?:\d+(?:\.\d+)*)?w?")
PIP_RE = re.compile(r"pip(?:\d+(?:\.\d+)*)?")
ASSIGN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\+?=")

SHELLS = {"bash", "sh", "zsh", "dash", "ksh", "ash"}

# Shell reserved words after which a new command starts.
RESERVED = {"!", "{", "if", "then", "elif", "else", "while", "until", "do"}

# Wrapper commands: name -> (options that take a value, number of positionals before the command).
WRAPPERS: dict[str, tuple[set[str], int]] = {
    "sudo": ({"-u", "-g", "-h", "-p", "-C", "-D", "-R", "-T", "-U", "-r", "-t",
              "--user", "--group", "--host", "--prompt", "--chdir", "--chroot",
              "--other-user", "--role", "--type", "--close-from"}, 0),
    "doas": ({"-u", "-C"}, 0),
    "env": ({"-u", "-C", "-S", "--unset", "--chdir", "--split-string"}, 0),
    "exec": ({"-a"}, 0),
    "time": ({"-f", "-o", "--format", "--output"}, 0),
    "nohup": (set(), 0),
    "nice": ({"-n", "--adjustment"}, 0),
    "ionice": ({"-c", "-n", "-t", "--class", "--classdata"}, 0),
    "setsid": (set(), 0),
    "stdbuf": ({"-i", "-o", "-e"}, 0),
    "timeout": ({"-s", "-k", "--signal", "--kill-after"}, 1),
    "xargs": ({"-n", "-I", "-L", "-P", "-s", "-d", "-E", "-a",
               "--max-args", "--max-procs", "--max-lines", "--max-chars",
               "--delimiter", "--arg-file", "--eof"}, 0),
    "command": (set(), 0),  # `command -v/-V` only looks a name up
}

UV_VALUED = {
    "--with", "--with-editable", "--with-requirements", "-w", "--python", "-p",
    "--project", "--directory", "--env-file", "--extra", "--group", "--no-group",
    "--package", "--index", "--default-index", "--index-url", "-i",
    "--extra-index-url", "--find-links", "-f", "--index-strategy",
    "--exclude-newer", "--config-file", "--cache-dir", "--upgrade-package", "-P",
    "--reinstall-package", "--refresh-package", "--color",
}

PIP_VALUED = {
    "-r", "--requirement", "-c", "--constraint", "-e", "--editable", "-i",
    "--index-url", "--extra-index-url", "-f", "--find-links", "-t", "--target",
    "--prefix", "--root", "--python", "-p", "--python-version", "--platform",
    "--index", "--no-binary", "--only-binary", "--cache-dir", "--src",
    "--upgrade-strategy", "--config-settings", "-C", "--proxy", "--trusted-host",
}

NOTE = "The uv plugin is enabled, so all Python must go through uv in every directory."


# --------------------------------------------------------------------------- #
# Result
# --------------------------------------------------------------------------- #


@dataclass
class Violation:
    kind: str  # "python", "pip", "uv pip install", "uv run pip install"
    packages: list[str] | None = None

    def message(self) -> str:
        if self.kind == "python":
            return (
                f"Hint: direct python detected. {NOTE}\n"
                "  Use `uv run python ...` (or `uv run --no-project python ...` for a standalone"
                " script inside a project), or `uvx <tool>` for tools."
            )
        what = {
            "pip": "direct pip",
            "uv pip install": "`uv pip install`",
            "uv run pip install": "`uv run pip install`",
        }[self.kind]
        text = (
            f"Hint: {what} detected. {NOTE}\n"
            "  Inside a uv project use `uv add <pkgs>`; outside one use"
            " `uv run --with <pkgs> ...`, inline script metadata, or `uvx <tool>`."
        )
        if self.packages:
            text += "\n  Suggested command: uv add " + " ".join(shlex.quote(p) for p in self.packages)
        return text


# --------------------------------------------------------------------------- #
# Tokenizer: shell text -> simple commands
# --------------------------------------------------------------------------- #


@dataclass
class Heredoc:
    delim: str = ""
    strip_tabs: bool = False
    body: str = ""  # heredoc body, or the word of a here-string


@dataclass
class Command:
    words: list[str] = field(default_factory=list)
    heredocs: list[Heredoc] = field(default_factory=list)


_META = set(" \t\r\n;&|()<>`")


def _match_paren(text: str, open_idx: int) -> int:
    """Index of the `)` matching the `(` at open_idx (len(text) if unbalanced)."""
    depth = 0
    for k in range(open_idx, len(text)):
        if text[k] == "(":
            depth += 1
        elif text[k] == ")":
            depth -= 1
            if depth == 0:
                return k
    return len(text)


def tokenize(text: str) -> tuple[list[Command], list[str]]:
    """Split shell text into simple commands.

    Returns (commands, nested), where nested holds `$(...)` / backtick payloads found
    inside double quotes. Redirections are dropped, heredoc bodies are attached to the
    command that owns them. Never raises on unbalanced quotes; it just consumes to the end.
    """
    cmds: list[Command] = []
    nested: list[str] = []
    cur = Command()
    pending: list[Heredoc] = []
    buf: list[str] = []
    in_word = False
    n = len(text)
    i = 0

    def flush() -> None:
        nonlocal in_word
        if in_word:
            cur.words.append("".join(buf))
            buf.clear()
            in_word = False

    def end() -> None:
        nonlocal cur
        flush()
        if cur.words or cur.heredocs:
            cmds.append(cur)
            cur = Command()

    def scan_single(i: int) -> tuple[str, int]:
        j = text.find("'", i + 1)
        return (text[i + 1:], n) if j == -1 else (text[i + 1:j], j + 1)

    def scan_double(i: int) -> tuple[str, int]:
        out: list[str] = []
        j = i + 1
        while j < n:
            c = text[j]
            if c == '"':
                return "".join(out), j + 1
            if c == "\\" and j + 1 < n:
                nxt = text[j + 1]
                if nxt != "\n":
                    out.append(nxt if nxt in '"\\$`' else c + nxt)
                j += 2
            elif c == "$" and text.startswith("$(", j):
                close = _match_paren(text, j + 1)
                nested.append(text[j + 2:close])
                j = close + 1
            elif c == "`":
                close = text.find("`", j + 1)
                close = n if close == -1 else close
                nested.append(text[j + 1:close])
                j = close + 1
            else:
                out.append(c)
                j += 1
        return "".join(out), n

    def read_word(i: int) -> tuple[str, int]:
        """Read one (possibly quoted) word, e.g. a redirect target or heredoc delimiter."""
        while i < n and text[i] in " \t":
            i += 1
        out: list[str] = []
        while i < n and text[i] not in _META:
            c = text[i]
            if c == "'":
                s, i = scan_single(i)
                out.append(s)
            elif c == '"':
                s, i = scan_double(i)
                out.append(s)
            elif c == "\\" and i + 1 < n:
                if text[i + 1] != "\n":
                    out.append(text[i + 1])
                i += 2
            else:
                out.append(c)
                i += 1
        return "".join(out), i

    def read_heredoc_bodies(i: int) -> int:
        """i points just past a newline; consume the bodies of all pending heredocs."""
        for hd in pending:
            lines: list[str] = []
            while i < n:
                k = text.find("\n", i)
                k = n if k == -1 else k
                line = text[i:k].rstrip("\r")
                i = min(k + 1, n)
                if (line.lstrip("\t") if hd.strip_tabs else line) == hd.delim:
                    break
                lines.append(line)
            hd.body = "\n".join(lines)
        pending.clear()
        return i

    while i < n:
        c = text[i]
        if c == "\\":
            if text.startswith("\\\n", i):
                i += 2
            elif i + 1 < n:
                buf.append(text[i + 1])
                in_word = True
                i += 2
            else:
                i += 1
        elif c == "'":
            s, i = scan_single(i)
            buf.append(s)
            in_word = True
        elif c == '"':
            s, i = scan_double(i)
            buf.append(s)
            in_word = True
        elif c == "#" and not in_word:
            j = text.find("\n", i)
            i = n if j == -1 else j
        elif c == "$" and text.startswith("$(", i):
            end()
            i += 2
        elif c == "`":
            end()
            i += 1
        elif c in " \t\r":
            flush()
            i += 1
        elif c == "\n":
            end()
            i = read_heredoc_bodies(i + 1)
        elif c in ";()|" or (c == "&" and not text.startswith("&>", i)):
            end()
            i += 1
        elif c in "<>&":
            if in_word and "".join(buf).isdigit():  # fd number such as the 2 in 2>&1
                buf.clear()
                in_word = False
            else:
                flush()
            if text.startswith("<<<", i):
                word, i = read_word(i + 3)
                cur.heredocs.append(Heredoc(body=word))
            elif text.startswith("<<", i):
                i += 2
                strip = text.startswith("-", i)
                i += strip
                delim, i = read_word(i)
                hd = Heredoc(delim=delim, strip_tabs=strip)
                cur.heredocs.append(hd)
                pending.append(hd)
            else:
                while i < n and text[i] in "<>&|":
                    i += 1
                if text.startswith("(", i):  # process substitution <(...) / >(...)
                    end()
                    i += 1
                else:
                    _, i = read_word(i)
        else:
            buf.append(c)
            in_word = True
            i += 1

    end()
    return cmds, nested


# --------------------------------------------------------------------------- #
# Analysis
# --------------------------------------------------------------------------- #


def _base(word: str) -> str:
    return word.rsplit("/", 1)[-1]


def find_exec(words: list[str]) -> int | None:
    """Index of the real executable after assignments, reserved words and wrappers."""
    i, n = 0, len(words)
    while i < n:
        word = words[i]
        if ASSIGN_RE.match(word) or word in RESERVED:
            i += 1
            continue
        name = _base(word)
        spec = WRAPPERS.get(name)
        if spec is None:
            return i
        valued, positionals = spec
        i += 1
        while i < n and words[i].startswith("-"):
            opt = words[i]
            if name == "command" and opt in ("-v", "-V"):
                return None
            if opt == "--":
                i += 1
                break
            i += 2 if opt in valued else 1
        i += positionals
    return None


def _first_positional(args: list[str], valued: set[str]) -> int | None:
    """Index of the first argument that is not an option or an option's value."""
    i = 0
    while i < len(args):
        if args[i].startswith("-") and args[i] != "-":
            i += 2 if args[i] in valued else 1
        else:
            return i
    return None


def _install_packages(args: list[str]) -> list[str] | None:
    """If args (after the pip program) is an `install` call, return its package list."""
    start = _first_positional(args, PIP_VALUED)
    if start is None or args[start] != "install":
        return None
    packages: list[str] = []
    rest = args[start + 1:]
    i = 0
    while i < len(rest):
        word = rest[i]
        if word in ("-r", "--requirement") and i + 1 < len(rest):
            packages += ["-r", rest[i + 1]]
            i += 2
        elif word.startswith("-") and word != "-":
            i += 2 if word in PIP_VALUED else 1
        else:
            packages.append(word)
            i += 1
    return packages


def _check_uv(args: list[str]) -> Violation | None:
    sub = _first_positional(args, UV_VALUED)
    if sub is None:
        return None
    rest = args[sub + 1:]
    if args[sub] == "pip":
        packages = _install_packages(rest)
        if packages is not None:
            return Violation("uv pip install", packages)
    elif args[sub] == "run":
        target = _first_positional(rest, UV_VALUED)
        if target is not None and PIP_RE.fullmatch(_base(rest[target])):
            packages = _install_packages(rest[target + 1:])
            if packages is not None:
                return Violation("uv run pip install", packages)
    return None


def _shell_payload(args: list[str]) -> str | None:
    """The script text of `sh -c '...'` (also -lc, -ec, ...)."""
    for idx, arg in enumerate(args):
        if arg.startswith("-") and not arg.startswith("--") and "c" in arg[1:]:
            return args[idx + 1] if idx + 1 < len(args) else None
    return None


def _check_command(cmd: Command, depth: int) -> Violation | None:
    idx = find_exec(cmd.words)
    if idx is None:
        return None
    exe, args = cmd.words[idx], cmd.words[idx + 1:]
    name = _base(exe)

    if name == "uv":
        return _check_uv(args)
    if name in SHELLS:
        payload = _shell_payload(args)
        if payload is not None:
            return analyze(payload, depth + 1)
        script_file = _first_positional(args, set()) is not None
        if cmd.heredocs and (not script_file or "-s" in args):
            for hd in cmd.heredocs:
                found = analyze(hd.body, depth + 1)
                if found:
                    return found
        return None
    if name == "eval":
        return analyze(" ".join(args), depth + 1)
    if PYTHON_RE.fullmatch(name):
        # `python -m pip install ...` is pip in disguise
        for k, arg in enumerate(args[:-1]):
            if arg == "-m" and PIP_RE.fullmatch(args[k + 1]):
                return Violation("pip", _install_packages(args[k + 2:]))
        return Violation("python")
    if PIP_RE.fullmatch(name):
        return Violation("pip", _install_packages(args))
    return None


def analyze(text: str, depth: int = 0) -> Violation | None:
    if depth > MAX_DEPTH:
        return None
    cmds, nested = tokenize(text)
    for cmd in cmds:
        found = _check_command(cmd, depth)
        if found:
            return found
    for payload in nested:
        found = analyze(payload, depth + 1)
        if found:
            return found
    return None


# --------------------------------------------------------------------------- #
# Fallback: coarse regex scan, used only if the tokenizer raises
# --------------------------------------------------------------------------- #

_VERSION = r"\d+(?:\.\d+)*"
_FALLBACK_RE = re.compile(
    r"(?:^|[;&|(){}`\n!]|\$\(|\b(?:then|do|else|sudo|env|exec|time|nohup|nice|timeout|xargs|command)\b)"
    r"\s*(?:(?:-\S*|[A-Za-z_]\w*=\S*|\d+[smhd]?)\s+)*"
    r"(?:[^\s;&|()`]*/)?"
    rf"(?:(?P<py>python(?:{_VERSION})?w?)|(?P<pip>pip(?:{_VERSION})?))(?![\w.\-/])"
)
_FALLBACK_UV_PIP_RE = re.compile(r"\buv\s+(?:run\s+)?pip3?\s+install\b")


def fallback_scan(command: str) -> Violation | None:
    m = _FALLBACK_UV_PIP_RE.search(command)
    if m:
        return Violation("uv run pip install" if " run " in m.group(0) else "uv pip install")
    m = _FALLBACK_RE.search(command)
    if m:
        return Violation("python" if m.group("py") else "pip")
    return None


# --------------------------------------------------------------------------- #


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    tool_input = data.get("tool_input") if isinstance(data, dict) else None
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str) or not command:
        return 0

    try:
        violation = analyze(command)
    except Exception:  # noqa: BLE001 - never crash; degrade to the coarse scan
        violation = fallback_scan(command)

    if violation is None:
        return 0
    print(violation.message(), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
