#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "tree-sitter==0.26.1",
#     "tree-sitter-bash==0.25.1",
# ]
# ///
"""
PreToolUse hook: blocks Bash commands that would kill the shell running
them, or Claude Code itself.

Claude Code runs every Bash tool call as a fresh
`/bin/zsh -c '<preamble> && <the entire command text>'` process, so the
command's own text is present in that shell's `/proc/<pid>/cmdline`. Anything
that matches by *full command line* (`pkill -f`, `pgrep -f` piped to `kill`,
`ps aux | grep ... | kill`) can therefore match the very shell running it and
kill it before the intended target is ever reached, silently, because the
process that would have reported the result is the one that died.

This hook is deliberately NOT a blacklist of `pkill -f` / `killall` / etc. It
extracts the pattern operand each command would actually search with, and
tests whether that pattern would really match something at risk (the command
text itself, an ancestor process's command line, the shell wrapper's fixed
strings, or a process name in the Claude Code / shell family). A pattern that
provably does not match anything at risk is let through untouched — including
the classic `pkill -f 'uvicor[n]'` bracket trick, which hides the literal
substring from the very text it appears in.

Modes:
  (no args)              Read the PreToolUse JSON payload from stdin.
  --check "<command>"    Evaluate a command string and print a verdict. For
                          testing; never denies anything for real, exits 0.
  -h / --help            Usage text.

Kill switch: set SELF_KILL_GUARD_DISABLE=1 to exit immediately, no output.

Parsing: which words are real command invocations is decided by a real shell
parser (tree-sitter-bash, imported lazily). If it is not importable (e.g. run
with a plain python3) or SELF_KILL_GUARD_PARSER=shlex is set, the older shlex
heuristic is used instead. `--check` reports which one was used.
"""

import json
import os
import re
import shlex
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import kill_reminder
except Exception:  # the reminder is optional; the guard must keep working
    kill_reminder = None

HELP_TEXT = """\
self-kill-guard-hook.py - block Bash commands that would kill their own
shell or Claude Code itself.

Usage:
  self-kill-guard-hook.py                 Read a PreToolUse payload from stdin
                                           (tool_input.command) and, if the
                                           command is dangerous, print a
                                           hookSpecificOutput JSON decision.
  self-kill-guard-hook.py --check CMD      Evaluate CMD directly and print a
                                           human-readable verdict plus the
                                           JSON that would be emitted. Always
                                           exits 0. For testing.
  self-kill-guard-hook.py -h|--help        Show this text.

Environment:
  SELF_KILL_GUARD_DISABLE=1   Disable the guard entirely (exit 0, no output).
  SELF_KILL_GUARD_PARSER=shlex
                              Force the shlex heuristic instead of
                              tree-sitter-bash (for tests / debugging).

A data heredoc / here-string that contains kill words (e.g. a script being
written with `cat > x.sh <<'EOF'`) passes, but adds a non-blocking
PreToolUse additionalContext reminder (never a permissionDecision).
"""

# --------------------------------------------------------------------------
# Tokenizing
# --------------------------------------------------------------------------

PUNCT_RE = re.compile(r"^[|&;()<>\n]+$")


HEREDOC_DELIM_END = " \t\n;&|()<>"


def _read_heredoc_delim(command: str, i: int) -> tuple[str, int] | None:
    """Parse the delimiter word starting at `i` (after `<<` / `<<-`). Returns
    (delimiter with quotes removed, index after it) or None if absent."""
    n = len(command)
    while i < n and command[i] in " \t":
        i += 1
    delim: list[str] = []
    start = i
    while i < n:
        ch = command[i]
        if ch in "'\"":
            end = command.find(ch, i + 1)
            if end == -1:
                return None
            delim.append(command[i + 1:end])
            i = end + 1
        elif ch in HEREDOC_DELIM_END:
            break
        else:
            delim.append(ch)
            i += 1
    if i == start:
        return None
    return "".join(delim), i


def _normalize_once(command: str) -> tuple[str, int | None]:
    """One pass of normalize_shell_text. Returns (text, pos) where `pos` is
    the index of a quote character that was never closed, or None."""
    out: list[str] = []
    quote = ""  # "", "'" or '"'
    quote_pos = -1
    word_start = True
    pending: list[tuple[str, bool]] = []  # heredocs awaiting their body
    i = 0
    n = len(command)
    while i < n:
        ch = command[i]
        if quote == "'":
            out.append(ch)
            if ch == "'":
                quote = ""
            i += 1
            continue
        if ch == "\\":
            if i + 1 < n and command[i + 1] == "\n":
                i += 2  # line continuation: joins the lines
                continue
            out.append(ch)
            if i + 1 < n:
                out.append(command[i + 1])
            word_start = False
            i += 2
            continue
        if quote == '"':
            out.append(ch)
            if ch == '"':
                quote = ""
            i += 1
            continue
        if ch in "'\"":
            quote = ch
            quote_pos = i
            out.append(ch)
            word_start = False
        elif ch == "\n":
            out.append(" ; ")
            word_start = True
            i += 1
            # Heredoc bodies: quotes are neutralised so an apostrophe in
            # prose cannot open a quote, but lines are still tokenized
            # (fail closed: a body line starting with `pkill` still counts).
            for delim, strip_tabs in pending:
                while i < n:
                    end = command.find("\n", i)
                    line = command[i:] if end == -1 else command[i:end]
                    i = n if end == -1 else end + 1
                    check = line.lstrip("\t") if strip_tabs else line
                    if check == delim:
                        break
                    for c in line:
                        out.append(" " if c in "'\"`\\" else c)
                    out.append(" ; ")
            pending = []
            continue
        elif ch == "#" and word_start:
            while i < n and command[i] != "\n":
                i += 1
            continue
        elif ch == "<" and command.startswith("<<<", i):
            out.append("<<<")  # here-string, not a heredoc
            word_start = True
            i += 3
            continue
        elif ch == "<" and command.startswith("<<", i):
            out.append("<<")
            i += 2
            strip_tabs = i < n and command[i] == "-"
            if strip_tabs:
                out.append("-")
                i += 1
            parsed = _read_heredoc_delim(command, i)
            if parsed is not None:
                pending.append((parsed[0], strip_tabs))
            word_start = True
            continue
        else:
            out.append(ch)
            word_start = ch in " \t;&|()<>"
        i += 1
    return "".join(out), (quote_pos if quote else None)


def normalize_shell_text(command: str) -> str:
    """Make line structure visible to shlex, which treats a newline as plain
    whitespace and `#` as a comment that swallows the newline too.

    Walks the text with minimal quote awareness and:
      * deletes backslash-newline (line continuation) outside single quotes,
        so `cd /x \\` + newline + `pkill ...` stays ONE command;
      * replaces an unquoted newline with ` ; ` so it acts as a command
        separator, while newlines inside quotes stay part of the quoted word;
      * drops an unquoted `#` comment (up to, not including, the newline), so
        a comment line never runs and never hides the next line's separator;
      * for `<<DELIM` / `<<-DELIM` heredocs, neutralises quote characters in
        the body lines (they are still tokenized, one `;` per line);
      * if a quote is never closed, treats that quote character as a literal
        (replaces it with a space) and re-processes, so a stray quote cannot
        swallow the rest of the command.
    """
    for _ in range(len(command) + 1):
        text, open_pos = _normalize_once(command)
        if open_pos is None:
            return text
        command = command[:open_pos] + " " + command[open_pos + 1:]
    return text


def tokenize(command: str) -> list[str]:
    command = normalize_shell_text(command)
    try:
        lex = shlex.shlex(command, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        lex.commenters = ""  # comments were already removed above
        return list(lex)
    except ValueError:
        # Newlines are already `;` tokens courtesy of normalize_shell_text.
        return command.split()


def invocation_argv(tokens: list[str], start: int) -> list[str]:
    """Collect argv for an invocation starting at `start`, stopping at a
    punctuation-only token (|, ||, &&, ;, &, (, ), <, >) or end of tokens."""
    argv = [tokens[start]]
    i = start + 1
    while i < len(tokens):
        if PUNCT_RE.match(tokens[i]):
            break
        argv.append(tokens[i])
        i += 1
    return argv


# Commands that commonly precede the real command without themselves being
# it: `sudo pkill ...`, `xargs pkill ...`, `timeout 10 pkill ...`, etc. A
# token in this set (or a flag, or a VAR=value env assignment) is skipped
# when walking backward to decide whether the next token is in command
# position.
PREFIX_COMMANDS = {
    "sudo", "doas", "env", "xargs", "time", "nohup", "command", "exec",
    "nice", "ionice", "timeout", "stdbuf", "setsid",
}

ENV_ASSIGN_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")

# Shell reserved words after which a command starts: `if true; then CMD`,
# `do CMD`, `{ CMD; }`, `! CMD`, ... They confirm command position. This also
# accepts `echo then pkill x` as a command (fail closed, rare).
RESERVED_WORDS = {"if", "then", "else", "elif", "do", "while", "until", "{", "!"}


def is_command_position(tokens: list[str], i: int, structural: bool = False) -> bool:
    """True if tokens[i] is in command position — i.e. it is the command
    being invoked, not an argument (a string like "foo" in `echo pkill foo`
    or `git commit -m "... pkill ..."` must never be mistaken for a real
    `pkill` invocation).

    Walks backward from i-1, skipping flags, prefix commands (`sudo`,
    `xargs`, ...), and env assignments (`FOO=bar`), until it either hits the
    start of the token list or a punctuation-only boundary token (|, ;, &&,
    ...) — both of which confirm command position — or hits anything else,
    which disqualifies it.

    `structural` is set for the tree-sitter token list, where the shell
    grammar has already removed reserved words (`then`, `do`, `{`, `!`, ...)
    and every segment starts at a real command: a literal `then` there is an
    argument (`echo then pkill x`), so it must not confirm command position.
    """
    j = i - 1
    while j >= 0:
        tok = tokens[j]
        if PUNCT_RE.match(tok):
            return True
        if tok.startswith("-"):
            j -= 1
            continue
        if tok in RESERVED_WORDS and not structural:
            return True
        if tok in PREFIX_COMMANDS:
            j -= 1
            continue
        if ENV_ASSIGN_RE.match(tok):
            j -= 1
            continue
        return False
    return True


def find_invocation_tokens(tokens: list[str], name: str, structural: bool = False) -> list[int]:
    """Indices of tokens that invoke `name` (bare, or as .../name) IN
    COMMAND POSITION — the word `pkill` sitting inside an echo argument or a
    commit message must not be treated as a real invocation."""
    hits = []
    for i, tok in enumerate(tokens):
        if (tok == name or tok.endswith("/" + name)) and is_command_position(tokens, i, structural):
            hits.append(i)
    return hits


# --------------------------------------------------------------------------
# tree-sitter-bash front end
#
# The shlex path above is a heuristic: it cannot tell `echo then pkill x`
# from `if c; then pkill x`, and it sees heredoc DATA as commands. This
# section parses the command with tree-sitter-bash instead and renders the
# AST into the same flat token list the rest of the module consumes: one
# simple command per `;`-separated segment, `|` between pipeline stages, every
# word already unquoted. Expansions (`$VAR`, `$(...)`) stay textual so the
# "cannot resolve -> ask" logic still fires.
# --------------------------------------------------------------------------

PARSER_ENV = "SELF_KILL_GUARD_PARSER"

MAX_SCRIPT_DEPTH = 5

SHELL_NAMES = {"bash", "sh", "zsh", "dash", "ksh"}
SHELL_C_FLAG_RE = re.compile(r"^-[A-Za-z]*c[A-Za-z]*$")
DURATION_RE = re.compile(r"^\d+(\.\d+)?[smhd]?$")
SUBSTITUTION_TYPES = {"command_substitution", "process_substitution"}
REDIRECT_TYPES = {"file_redirect", "heredoc_redirect", "herestring_redirect"}


def load_ts_parser():
    """Return a tree-sitter-bash Parser, or None (forced off via
    SELF_KILL_GUARD_PARSER=shlex, or the packages are not importable, e.g.
    when run with a plain python3 instead of `uv run --script`)."""
    if os.environ.get(PARSER_ENV, "").strip().lower() == "shlex":
        return None
    try:
        import tree_sitter_bash
        from tree_sitter import Language, Parser

        return Parser(Language(tree_sitter_bash.language()))
    except Exception:
        return None


def _safe_token(word: str) -> str:
    # A word that is only punctuation (`echo ';'`) must not be mistaken for a
    # command boundary by PUNCT_RE.
    return "\x00" + word if PUNCT_RE.match(word) else word


def shell_invocation(argv: list[str]) -> tuple[str, str | None] | None:
    """Does this argv run a shell interpreter (or eval)?

    Returns ("script", text) when the script text is a literal argument
    (`bash -c TEXT`, `eval ARGS...`), ("stdin", None) when a shell reads its
    script from stdin (so a heredoc / here-string feeds it code), or None.
    The interpreter may sit behind prefixes (`sudo -u x env A=1 bash ...`) and
    be given by path (`/bin/bash`).
    """
    idx = None
    prev_flag = False
    for j, tok in enumerate(argv):
        base = tok.rsplit("/", 1)[-1]
        if base in SHELL_NAMES or base == "eval":
            idx = j
            break
        skippable = (
            tok in PREFIX_COMMANDS
            or tok.startswith("-")
            or bool(ENV_ASSIGN_RE.match(tok))
            or bool(DURATION_RE.match(tok))
            or prev_flag  # probably the value of the preceding flag
        )
        if not skippable:
            return None
        prev_flag = tok.startswith("-")
    if idx is None:
        return None

    args = argv[idx + 1:]
    if argv[idx].rsplit("/", 1)[-1] == "eval":
        return ("script", " ".join(args)) if args else None

    stdin = False
    k = 0
    while k < len(args):
        a = args[k]
        if SHELL_C_FLAG_RE.match(a):
            return ("script", args[k + 1] if k + 1 < len(args) else None)
        if a == "-s":
            stdin = True
        if a in ("-o", "+o", "-O", "+O"):
            k += 2
            continue
        if a.startswith(("-", "+")):
            k += 1
            continue
        break
    else:
        stdin = True  # only flags: reads the script from stdin
    return ("stdin", None) if stdin else None


class AstCollector:
    """Walks a tree-sitter-bash AST and flattens it into the token list that
    collect_invocations() works on."""

    def __init__(self, parser) -> None:
        self.parser = parser
        self.depth = 0
        self.shell_seen = False  # a stdin-reading shell was met (see below)
        # Texts that are DATA (heredoc bodies / here-strings not fed to a
        # shell): never matched as commands, but scanned for the reminder.
        self.data_texts: list[str] = []

    # -- helpers ----------------------------------------------------------

    @staticmethod
    def sep(buf: list[str]) -> None:
        if buf and buf[-1] != ";":
            buf.append(";")

    @staticmethod
    def text(node) -> str:
        return node.text.decode("utf-8", "replace")

    def fallback(self, text: str, buf: list[str]) -> None:
        """Fail closed: tokenize raw text with the shlex heuristic. Reserved
        words become `;` because the structural command-position test of the
        AST path no longer looks at them."""
        self.sep(buf)
        buf.extend(";" if t in RESERVED_WORDS else t for t in tokenize(text))
        self.sep(buf)

    def parse_into(self, text: str, buf: list[str]) -> None:
        if self.depth > MAX_SCRIPT_DEPTH:
            self.fallback(text, buf)
            return
        self.depth += 1
        try:
            tree = self.parser.parse(text.encode("utf-8"))
            self.sep(buf)
            self.walk(tree.root_node, buf)
        finally:
            self.depth -= 1

    def value(self, node) -> str:
        """The word's value after quote removal; expansions stay textual."""
        t = node.type
        text = self.text(node)
        if t in ("string", "translated_string"):
            start = 2 if t == "translated_string" else 1
            inner = text[start:-1] if text.endswith('"') and len(text) > start else text[start:]
            return re.sub(r'\\([\\"$`])', r"\1", inner)
        if t == "raw_string":
            return text[1:-1] if len(text) >= 2 else text
        if t == "ansi_c_string":
            return text[2:-1] if len(text) >= 3 else text
        if t == "concatenation":
            return "".join(self.value(c) for c in node.children)
        if t == "command_name" and node.named_children:
            return self.value(node.named_children[0])
        if t == "word":
            return re.sub(r"\\(.)", r"\1", text.replace("\\\n", ""), flags=re.S)
        return text.replace("\n", " ")

    def substs(self, node, buf: list[str]) -> None:
        """Walk every $(...) / `...` / <(...) below `node` (top-most ones;
        walk() handles nesting) as commands of their own."""
        if node.type in SUBSTITUTION_TYPES:
            self.sep(buf)
            self.walk(node, buf)
            return
        for c in node.children:
            self.substs(c, buf)

    # -- AST walk ---------------------------------------------------------

    def walk(self, node, buf: list[str]) -> None:
        t = node.type
        if t == "ERROR":
            # Syntax tree-sitter could not parse (zsh-only syntax, broken
            # quoting): hand just this text to the shlex heuristic.
            self.fallback(self.text(node), buf)
        elif t == "command":
            self.command(node, buf)
        elif t == "pipeline":
            self.pipeline(node, buf)
        elif t == "redirected_statement":
            self.redirected(node, buf)
        elif node.child_count:
            for c in node.named_children:
                if c.type == "comment":
                    continue
                self.sep(buf)
                self.walk(c, buf)

    def pipeline(self, node, buf: list[str]) -> None:
        stages: list[list[str]] = []
        for c in node.named_children:
            if c.type == "comment":
                continue
            sub: list[str] = []
            self.walk(c, sub)
            stages.append(sub)
        self.sep(buf)
        for n, sub in enumerate(stages):
            if n:
                buf.append("|")
            buf.extend(sub)

    def command(self, node, buf: list[str]) -> None:
        pre: list[str] = []  # commands nested in this command's words
        argv: list[str] = []
        redirects = []
        for c in node.named_children:
            t = c.type
            if t == "comment":
                continue
            if t in REDIRECT_TYPES:
                redirects.append(c)
                continue
            if t == "ERROR":
                self.sep(pre)
                self.walk(c, pre)
                continue
            self.substs(c, pre)
            argv.append(self.text(c).replace("\n", " ") if t == "variable_assignment" else self.value(c))

        self.sep(buf)
        if pre:
            buf.extend(pre)
            self.sep(buf)
        buf.extend(_safe_token(a) for a in argv)

        stdin_shell = False
        info = shell_invocation(argv)
        if info is not None:
            kind, script = info
            if kind == "stdin":
                stdin_shell = True
                self.shell_seen = True
            elif script is not None:
                self.parse_into(script, buf)
        for r in redirects:
            self.redirect(r, buf, stdin_shell)

    def redirect(self, node, buf: list[str], stdin_shell: bool) -> None:
        if node.type == "heredoc_redirect":
            self.heredoc(node, buf, stdin_shell)
            return
        if node.type == "herestring_redirect":
            for c in node.named_children:
                if stdin_shell:
                    self.parse_into(self.value(c), buf)
                else:
                    self.data_texts.append(self.value(c))
        self.substs(node, buf)

    def redirected(self, node, buf: list[str]) -> None:
        # `shell_seen` tells the heredoc whether the command (or pipeline
        # stage) it feeds is a shell reading stdin; fail closed for compound
        # bodies and pipelines by accepting any such shell inside.
        saved = self.shell_seen
        self.shell_seen = False
        redirects = []
        for c in node.named_children:
            if c.type in REDIRECT_TYPES:
                redirects.append(c)
            elif c.type != "comment":
                self.sep(buf)
                self.walk(c, buf)
        for r in redirects:
            self.redirect(r, buf, self.shell_seen)
        self.shell_seen = saved

    def heredoc(self, node, buf: list[str], stdin_shell: bool) -> None:
        body = None
        for c in node.named_children:
            if c.type in ("heredoc_start", "heredoc_end"):
                continue
            if c.type == "heredoc_body":
                body = c
                continue
            # `cat <<EOF | bash`: the pipeline hangs inside the redirect.
            self.sep(buf)
            self.walk(c, buf)
        if body is None:
            return
        if stdin_shell or self.shell_seen:
            self.parse_into(self.text(body), buf)  # the body is a script
        else:
            self.data_texts.append(self.text(body))
            self.substs(body, buf)  # data, but `$(...)` in it still runs


def ast_parse(parser, command: str) -> tuple[list[str], list[str]]:
    """(tokens, data texts): the flattened commands plus the heredoc bodies /
    here-strings that are only data."""
    buf: list[str] = []
    collector = AstCollector(parser)
    collector.parse_into(command, buf)
    return buf, collector.data_texts


def canonical_text(tokens: list[str]) -> str:
    """Single-line command string rebuilt from the AST tokens, for the
    regex gates in collect_invocations()."""
    return " ".join(t if t in (";", "|") else shlex.quote(t) for t in tokens)


# --------------------------------------------------------------------------
# Ancestor process discovery (best-effort; degrades to empty on any failure)
# --------------------------------------------------------------------------


def get_ancestors(max_levels: int = 12) -> list[dict]:
    """Walk up the process tree from this hook's PARENT pid using `ps`.

    Starting at the parent (not os.getpid()) skips this hook's own
    transient python/dispatcher process, which is not worth protecting and
    would be mislabeled if it were.

    The hook runs as a child of the `claude` node process, not of the zsh
    shell running the Bash command, so this walk is what lets us catch
    `pkill node` / `pkill -f claude` / `killall node` — it will never find
    the command's own shell (that's covered separately via the command text
    and the static wrapper strings).
    """
    ancestors: list[dict] = []
    try:
        pid = os.getppid()
        for _ in range(max_levels):
            result = subprocess.run(
                ["ps", "-o", "ppid=,comm=,args=", "-p", str(pid)],
                capture_output=True,
                text=True,
                timeout=2,
            )
            if result.returncode != 0:
                break
            line = result.stdout.strip("\n")
            if not line.strip():
                break
            parts = line.strip().split(None, 2)
            if len(parts) < 2:
                break
            ppid_str = parts[0]
            comm = parts[1]
            args = parts[2] if len(parts) > 2 else comm
            ancestors.append({"pid": pid, "comm": comm, "args": args})
            if ppid_str in ("1", "0", ""):
                break
            try:
                next_pid = int(ppid_str)
            except ValueError:
                break
            if next_pid == pid:
                break
            pid = next_pid
    except Exception:
        return []
    return ancestors


# --------------------------------------------------------------------------
# Protected target sets
# --------------------------------------------------------------------------

STATIC_CMDLINE_STRINGS = [
    "shell-snapshots",
    "snapshot-zsh",
    "snapshot-bash",
    "NO_EXTENDED_GLOB",
    "NO_BARE_GLOB_QUAL",
    "pwd -P",
    "/tmp/claude-",
]

STATIC_NAMES = {
    "zsh": "the shell running this command",
    "bash": "the shell running this command",
    "sh": "the shell running this command",
    "dash": "the shell running this command",
    "node": "Claude Code itself (its node runtime)",
    "claude": "Claude Code itself",
}


def ancestor_label(anc: dict) -> str:
    """Honest per-ancestor label. Not every ancestor IS Claude Code — the
    chain typically runs claude -> claude-desktop -> systemd, and calling
    `systemd` "Claude Code itself" in a deny message would simply be false.
    Only the process(es) that plausibly ARE Claude Code's own runtime get
    that label; everything else is described generically.
    """
    comm = anc["comm"]
    if "claude" in comm.lower() or comm == "node":
        return f"Claude Code itself (pid {anc['pid']}, {comm})"
    return f"an ancestor process of this session (pid {anc['pid']}, {comm})"


def build_protected_cmdlines(command: str, ancestors: list[dict]) -> list[tuple[str, str]]:
    """Returns (text, human-readable label) pairs matched by full cmdline."""
    protected: list[tuple[str, str]] = [(command, "the command you are about to run")]

    for anc in ancestors:
        protected.append((anc["args"], ancestor_label(anc)))

    shell = os.environ.get("SHELL", "")
    wrapper_label = "the shell wrapper Claude Code runs commands in"
    if shell:
        protected.append((shell, wrapper_label))
    for s in STATIC_CMDLINE_STRINGS:
        protected.append((s, wrapper_label))

    return protected


def build_protected_names(ancestors: list[dict]) -> list[tuple[str, str]]:
    """Returns (process name, human-readable label) pairs matched by name."""
    protected: list[tuple[str, str]] = []

    for anc in ancestors:
        protected.append((anc["comm"], ancestor_label(anc)))

    for name, label in STATIC_NAMES.items():
        protected.append((name, label))

    shell = os.environ.get("SHELL", "")
    if shell:
        protected.append((os.path.basename(shell), "the shell running this command"))

    return protected


# --------------------------------------------------------------------------
# Pattern matching
# --------------------------------------------------------------------------


def pattern_hits(pattern: str, target: str, exact: bool = False) -> bool:
    # pgrep/pkill use ERE; Python `re` is close enough for our purposes. If
    # the pattern is not a valid Python regex, fall back to a plain
    # substring test so we still catch the obvious case rather than
    # silently letting it through.
    try:
        rx = re.compile(pattern)
    except re.error:
        return pattern in target
    return bool(rx.fullmatch(target)) if exact else bool(rx.search(target))


def is_unresolved(pattern: str) -> bool:
    # shlex leaves $VAR / ${VAR} / `cmd` literal, it does not expand them,
    # so we cannot know what these actually become at runtime.
    return "$" in pattern or "`" in pattern


# --------------------------------------------------------------------------
# Flag tables and operand extraction
# --------------------------------------------------------------------------

# pkill/pgrep flags that consume the following token as a value.
PKG_VALUE_FLAGS = {
    "-d", "--delimiter",
    "-u", "--euid",
    "-U", "--uid",
    "-g", "--pgroup",
    "-G", "--group",
    "-P", "--parent",
    "-s", "--session",
    "-t", "--terminal",
    "-F", "--pidfile",
    "-L", "--logpidfile",
    "--ns", "--nslist",
    "--signal",
    "-O", "--older",
    "-r", "--runstates",
}

# grep flags that consume the following token as a value.
GREP_VALUE_FLAGS = {
    "-e", "--regexp",
    "-f", "--file",
    "-m", "--max-count",
    "-A", "-B", "-C",
    "-d", "--directories",
    "--color", "--colour",
    "--exclude", "--include",
    "-D",
}

# killall flags that consume the following token as a value. killall has no
# -f/--full on either psmisc or BSD (it never matches full command lines,
# only the process name) — do not add one here.
KILLALL_VALUE_FLAGS = {
    "-u", "--user",
    "-s", "--signal",
    "-y", "--younger-than",
    "-o", "--older-than",
    "-n", "--ns",
    "-Z", "--context",
}

BOOLEAN_SIGNAL_RE = re.compile(r"^-(\d+|[A-Z]+)$")


def extract_operand(argv: list[str], value_flags: set[str], prefer_e_flag: bool = False) -> str | None:
    """Return the pattern operand for an argv (argv[0] is the command name).

    Walks left to right, skipping flags and the values they consume. The
    pattern is the FIRST bare operand encountered, unless `prefer_e_flag`
    is set (grep) and an -e/--regexp value was given, which wins regardless
    of position.
    """
    i = 1
    after_terminator = False
    first_bare: str | None = None
    e_value: str | None = None

    while i < len(argv):
        tok = argv[i]

        if after_terminator:
            if first_bare is None:
                first_bare = tok
            i += 1
            continue

        if tok == "--":
            after_terminator = True
            i += 1
            continue

        if tok.startswith("-") and tok != "-":
            # --opt=value is self-contained, never consumes the next token.
            if tok.startswith("--") and "=" in tok:
                name, _, val = tok.partition("=")
                if prefer_e_flag and name in ("-e", "--regexp"):
                    e_value = val
                i += 1
                continue

            # Value-taking flags checked BEFORE the boolean-signal regex:
            # -F/-U/-G/etc. are uppercase-letter flags that would otherwise
            # be mistaken for a boolean signal name like -TERM.
            if tok in value_flags:
                val = argv[i + 1] if i + 1 < len(argv) else None
                if prefer_e_flag and tok in ("-e", "--regexp") and val is not None:
                    e_value = val
                i += 2
                continue

            # Signal flags (-9, -TERM, -SIGKILL, ...) are boolean.
            if BOOLEAN_SIGNAL_RE.match(tok):
                i += 1
                continue

            # Any other flag (long or a short cluster like -af, -v, -x) is
            # treated as boolean and skipped; we never invent a value for it.
            i += 1
            continue

        if first_bare is None:
            first_bare = tok
        i += 1

    if prefer_e_flag and e_value is not None:
        return e_value
    return first_bare


def has_full_flag(argv: list[str]) -> bool:
    for tok in argv[1:]:
        if tok == "--full":
            return True
        if tok.startswith("-") and not tok.startswith("--") and re.match(r"^-[a-z]*f[a-z]*$", tok):
            return True
    return False


def has_exact_flag(argv: list[str]) -> bool:
    for tok in argv[1:]:
        if tok == "--exact":
            return True
        if tok.startswith("-") and not tok.startswith("--") and re.match(r"^-[a-z]*x[a-z]*$", tok):
            return True
    return False


def has_invert_flag(argv: list[str]) -> bool:
    return "-v" in argv[1:] or "--invert-match" in argv[1:]


def has_regexp_flag(argv: list[str]) -> bool:
    """killall's -r/--regexp: without it, killall matches the process name
    EXACTLY (psmisc and BSD both); with it, the pattern becomes a regex
    search. This is the opposite default from pkill/pgrep."""
    for tok in argv[1:]:
        if tok == "--regexp":
            return True
        if tok.startswith("-") and not tok.startswith("--") and re.match(r"^-[a-z]*r[a-z]*$", tok):
            return True
    return False


# --------------------------------------------------------------------------
# Invocation shapes
# --------------------------------------------------------------------------


class Invocation:
    def __init__(self, shape: str, kind: str, pattern: str, exact: bool, source: str):
        self.shape = shape      # "pkill" | "pgrep" | "ps-grep" | "killall"
        self.kind = kind        # "cmdline" | "name"
        self.pattern = pattern
        self.exact = exact
        self.source = source    # human-readable description for the message


# A newline ends a command like `;` does, so these stop at it too; a pipe may
# still be followed by a newline (`pgrep x |` newline `xargs kill`).
PGREP_PIPE_KILL_RE = re.compile(r"\bpgrep\b[^;\n]*\|\s*[^;\n]*\bkill\b")
PIDOF_PIPE_KILL_RE = re.compile(r"\bpidof\b[^;\n]*\|\s*[^;\n]*\bkill\b")
SUBST_KILL_RE = re.compile(
    r"\bkill\b[^;\n]*(?:\$\(\s*(?:pgrep|pidof)\b[^)]*\)|`\s*(?:pgrep|pidof)\b[^`]*`)"
)
# re.S so a pipeline wrapped across multiple lines (heredocs, wrapped long
# commands) still matches — `.` must cross newlines here.
PS_GREP_KILL_RE = re.compile(r"\bps\b.*?\|.*?\bgrep\b.*?\|.*?\bkill\b", re.S)


def collect_invocations(command: str, tokens: list[str], structural: bool = False) -> list[Invocation]:
    invocations: list[Invocation] = []

    # --- Shape A: pkill — always dangerous, it actually kills. ---
    for idx in find_invocation_tokens(tokens, "pkill", structural):
        argv = invocation_argv(tokens, idx)
        kind = "cmdline" if has_full_flag(argv) else "name"
        pattern = extract_operand(argv, PKG_VALUE_FLAGS)
        if pattern is None:
            continue
        # pkill(1): "-x, --exact: Only match processes whose names (or
        # command lines if -f is specified) exactly match the pattern."
        # Without -x it's a partial ERE search — `pkill nod` really does
        # kill `node`. This applies identically to cmdline- and name-kind.
        invocations.append(
            Invocation("pkill", kind, pattern, has_exact_flag(argv), f"`{' '.join(argv)}`")
        )

    # --- Shape B: pgrep/pidof whose output feeds a kill. A bare
    # `pgrep -af foo` is safe and is the recommended alternative — only
    # flag it when the raw command text shows it is piped into `kill`, or
    # substituted directly as `kill`'s argument. ---
    pgrep_feeds_kill = bool(PGREP_PIPE_KILL_RE.search(command)) or bool(SUBST_KILL_RE.search(command))
    if pgrep_feeds_kill:
        for idx in find_invocation_tokens(tokens, "pgrep", structural):
            argv = invocation_argv(tokens, idx)
            kind = "cmdline" if has_full_flag(argv) else "name"
            pattern = extract_operand(argv, PKG_VALUE_FLAGS)
            if pattern is None:
                continue
            # Same -x/--exact rule as pkill (pgrep shares the man page).
            invocations.append(
                Invocation("pgrep", kind, pattern, has_exact_flag(argv), f"`{' '.join(argv)}` (feeds a kill)")
            )

    pidof_feeds_kill = bool(PIDOF_PIPE_KILL_RE.search(command)) or bool(SUBST_KILL_RE.search(command))
    if pidof_feeds_kill:
        for idx in find_invocation_tokens(tokens, "pidof", structural):
            argv = invocation_argv(tokens, idx)
            # pidof has no -f/--full and no partial-match mode: it takes a
            # literal program name and matches it exactly.
            pattern = extract_operand(argv, set())
            if pattern is None:
                continue
            invocations.append(
                Invocation("pidof", "name", pattern, True, f"`{' '.join(argv)}` (feeds a kill)")
            )

    # --- Shape C: ps | grep | ... | kill. Extract the pattern from each
    # grep in the pipeline, skipping any `grep -v ...` (the `grep -v grep`
    # idiom, not the real pattern). ---
    if PS_GREP_KILL_RE.search(command):
        for idx in find_invocation_tokens(tokens, "grep", structural):
            argv = invocation_argv(tokens, idx)
            if has_invert_flag(argv):
                continue
            pattern = extract_operand(argv, GREP_VALUE_FLAGS, prefer_e_flag=True)
            if pattern is None:
                continue
            invocations.append(
                Invocation("ps-grep", "cmdline", pattern, False, f"`ps | grep` pipeline (`{' '.join(argv)}`)")
            )

    # --- Shape D: killall — always by process name; killall has no -f. ---
    for idx in find_invocation_tokens(tokens, "killall", structural):
        argv = invocation_argv(tokens, idx)
        pattern = extract_operand(argv, KILLALL_VALUE_FLAGS)
        if pattern is None:
            continue
        # killall(1) (psmisc and BSD both): matches the process name EXACTLY
        # by default. Only -r/--regexp turns the pattern into a regex
        # search. This is the OPPOSITE default from pkill/pgrep — do not
        # "fix" this back to match them.
        exact = not has_regexp_flag(argv)
        invocations.append(Invocation("killall", "name", pattern, exact, f"`{' '.join(argv)}`"))

    return invocations


# --------------------------------------------------------------------------
# Judging
# --------------------------------------------------------------------------


def judge(
    inv: Invocation,
    protected_cmdlines: list[tuple[str, str]],
    protected_names: list[tuple[str, str]],
) -> tuple[str, str | None]:
    """Returns (verdict, label) where verdict is 'match', 'unresolved', or 'safe'.

    `inv.exact` was already set correctly per shape at construction time in
    collect_invocations() (pkill/pgrep default to a partial search, exact
    only with -x; killall defaults to exact, search only with -r; pidof is
    always exact) — this function just applies it uniformly and must NOT
    override it, for either kind.
    """
    if is_unresolved(inv.pattern):
        return "unresolved", None

    targets = protected_cmdlines if inv.kind == "cmdline" else protected_names
    for text, label in targets:
        if pattern_hits(inv.pattern, text, exact=inv.exact):
            return "match", label
    return "safe", None


def bracket_trick(pattern: str) -> str | None:
    if re.fullmatch(r"[A-Za-z0-9_]{2,}", pattern):
        return f"{pattern[:-1]}[{pattern[-1]}]"
    return None


def build_deny_reason(inv: Invocation, label: str) -> str:
    trick = bracket_trick(inv.pattern)
    trick_line = ""
    if trick:
        trick_line = (
            "\nIf you really want one step, hide the pattern from itself:\n"
            f"    pkill -f '{trick}'\n"
        )

    if inv.shape == "pkill" and inv.kind == "cmdline":
        body = (
            f"`pkill -f {inv.pattern}` would kill the shell running this very command.\n\n"
            "Claude Code runs each Bash call as `/bin/zsh -c '<the whole command text>'`, "
            f"so the pattern `{inv.pattern}` appears in that shell's own command line. "
            "pkill matches full command lines, so it terminates its own shell first and the "
            "tool call dies before reaching the process you meant. Nothing is reported, "
            "because the reporter is dead.\n\n"
            f"Matched: {label}.\n\n"
            "Do it in two steps instead — a numeric PID cannot match a pattern:\n"
            f"    pgrep -af '{inv.pattern}'      # see what is actually there\n"
            "    kill 12345 12346         # then kill those literal PIDs\n"
            f"{trick_line}"
        )
    elif inv.kind == "name":
        body = (
            f"`{inv.source}` matches by process name, not by pattern — it would kill "
            "something this session depends on.\n\n"
            f"Matched: {label}.\n\n"
            "Do it in two steps instead — a numeric PID cannot match a name:\n"
            f"    pgrep -a '{inv.pattern}'      # see what is actually there\n"
            "    kill 12345 12346        # then kill those literal PIDs\n"
        )
    elif inv.shape == "ps-grep":
        body = (
            f"`{inv.source}` would kill the shell running this very command.\n\n"
            "`ps` lists this command's own process too, so the `grep` in this pipeline "
            f"matches its own invocation (pattern `{inv.pattern}`), and the `kill` at the "
            "end takes the PID of the shell running the pipeline itself.\n\n"
            f"Matched: {label}.\n\n"
            "Do it in two steps instead:\n"
            f"    pgrep -af '{inv.pattern}'      # see what is actually there\n"
            "    kill 12345 12346         # then kill those literal PIDs\n"
        )
    else:  # pgrep/pidof feeding a kill, cmdline or name kind
        body = (
            f"`{inv.source}` would kill the shell running this very command.\n\n"
            f"The pattern `{inv.pattern}` appears in that shell's own command line, so the "
            "pgrep/pidof lookup returns this shell's own PID before it ever reaches the "
            "process you meant, and the kill that follows takes the shell down.\n\n"
            f"Matched: {label}.\n\n"
            "Do it in two steps instead, and look at the result before killing anything:\n"
            f"    pgrep -af '{inv.pattern}'      # see what is actually there\n"
            "    kill 12345 12346         # then kill those literal PIDs\n"
            f"{trick_line}"
        )

    return body + "\nSet SELF_KILL_GUARD_DISABLE=1 to turn this guard off."


def build_ask_reason(inv: Invocation) -> str:
    return (
        f"`{inv.source}` uses a pattern that comes from a variable or command substitution "
        f"(`{inv.pattern}`), so it cannot be checked ahead of time — shlex leaves `$VAR` and "
        "`` `cmd` `` literal, it does not expand them.\n\n"
        "If it expands to anything that appears in this command's own text (or in an "
        "ancestor process, or the shell wrapper), the shell running this command dies before "
        "reaching the intended target.\n\n"
        "Safer form, and it also tells you what you're about to kill:\n"
        f"    pgrep -af \"{inv.pattern}\"      # see what is actually there\n"
        "    kill 12345 12346          # then kill those literal PIDs\n\n"
        "Set SELF_KILL_GUARD_DISABLE=1 to turn this guard off."
    )


# --------------------------------------------------------------------------
# Analysis entry point
# --------------------------------------------------------------------------


def analyze(command: str) -> tuple[str | None, str | None, Invocation | None, str, list[str]]:
    """Returns (decision, reason, invocation, parser, data_texts) where
    decision is 'deny', 'ask', or None (silent pass), parser is 'tree-sitter'
    or 'shlex' (which front end decided what is a real invocation) and
    data_texts are heredoc bodies / here-strings that are only data (empty with
    shlex, which treats heredoc bodies as commands)."""
    ancestors = get_ancestors()
    # The self-match target is always the ORIGINAL text: that is what sits in
    # the running shell's cmdline, whatever the parser made of it.
    protected_cmdlines = build_protected_cmdlines(command, ancestors)
    protected_names = build_protected_names(ancestors)

    invocations: list[Invocation] | None = None
    parser_used = "shlex"
    data_texts: list[str] = []
    ts_parser = load_ts_parser()
    if ts_parser is not None:
        try:
            tokens, data_texts = ast_parse(ts_parser, command)
            invocations = collect_invocations(canonical_text(tokens), tokens, structural=True)
            parser_used = "tree-sitter"
        except Exception:
            invocations = None  # fail closed onto the shlex heuristic
            data_texts = []
    if invocations is None:
        invocations = collect_invocations(command, tokenize(command))

    ask_hit: tuple[Invocation, str] | None = None
    for inv in invocations:
        verdict, label = judge(inv, protected_cmdlines, protected_names)
        if verdict == "match":
            return "deny", build_deny_reason(inv, label), inv, parser_used, data_texts
        if verdict == "unresolved" and ask_hit is None:
            ask_hit = (inv, "")

    if ask_hit is not None:
        inv, _ = ask_hit
        return "ask", build_ask_reason(inv), inv, parser_used, data_texts

    return None, None, None, parser_used, data_texts


def emit_decision(decision: str, reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": decision,
                    "permissionDecisionReason": reason,
                }
            }
        )
    )


# --------------------------------------------------------------------------
# Heredoc reminder (non-blocking)
# --------------------------------------------------------------------------

HEREDOC_KEY = "<bash-heredoc>"


def heredoc_entries(data_texts: list[str]) -> list[tuple[int, str]]:
    """Kill-code lines in data heredoc bodies / here-strings. Line numbers are
    only unique per body, so they are renumbered across all bodies."""
    if kill_reminder is None:
        return []
    entries: list[tuple[int, str]] = []
    n = 0
    for text in data_texts:
        for _line_no, line in kill_reminder.find_kill_lines(text):
            n += 1
            entries.append((n, line))
    return entries


def heredoc_message(entries: list[tuple[int, str]]) -> str:
    return kill_reminder.build_message(
        "This Bash command writes text that contains process-kill code (a heredoc or here-string "
        "that is data and is not executed by this command). Matching lines, numbered in order "
        "of appearance:",
        entries,
        "match",
    )


def emit_context(message: str) -> None:
    print(kill_reminder.context_json("PreToolUse", message))


def maybe_remind(payload: dict, data_texts: list[str]) -> None:
    """Hook mode: print the reminder (never a permissionDecision) unless every
    matching line was already reported in this session. Never raises."""
    try:
        entries = heredoc_entries(data_texts)
        if not entries:
            return
        session_id = str(payload.get("session_id", ""))
        fresh = kill_reminder.filter_new(session_id, HEREDOC_KEY, entries)
        if not fresh:
            return
        emit_context(heredoc_message(fresh))
        kill_reminder.mark_reported(session_id, HEREDOC_KEY, fresh[: kill_reminder.MAX_LISTED])
    except Exception:
        pass


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main() -> None:
    argv = sys.argv[1:]

    if argv and argv[0] in ("-h", "--help"):
        print(HELP_TEXT)
        sys.exit(0)

    if os.environ.get("SELF_KILL_GUARD_DISABLE") == "1":
        sys.exit(0)

    try:
        if argv and argv[0] == "--check":
            if len(argv) < 2:
                print("self-kill-guard-hook.py --check requires a command argument", file=sys.stderr)
                sys.exit(0)
            command = argv[1]
            decision, reason, inv, parser_used, data_texts = analyze(command)
            if decision is None:
                entries = heredoc_entries(data_texts)
                if entries:
                    print(f"PASS parser={parser_used} (reminder only, no permission decision) - kill code inside heredoc/here-string data.")
                    print("--- REMIND ---")
                    message = heredoc_message(entries)
                    print(message)
                    print("---")
                    emit_context(message)
                else:
                    print(f"PASS parser={parser_used} (silent) - nothing to output for this command.")
                    print(json.dumps({}))
            else:
                print(f"{decision.upper()} parser={parser_used} - shape={inv.shape} kind={inv.kind} pattern={inv.pattern!r}")
                print("---")
                print(reason)
                print("---")
                emit_decision(decision, reason)
            sys.exit(0)

        data = json.load(sys.stdin)
        command = data.get("tool_input", {}).get("command", "")
        if not command:
            sys.exit(0)

        decision, reason, _inv, _parser, data_texts = analyze(command)
        if decision is not None:
            emit_decision(decision, reason)
        else:
            maybe_remind(data, data_texts)
        sys.exit(0)
    except Exception:
        # A buggy guard must never block every Bash call in the session.
        sys.exit(0)


if __name__ == "__main__":
    main()
