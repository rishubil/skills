"""
Shared, stdlib-only helpers for the self-kill-guard "review your kill code"
reminders. Used by write-reminder-hook.py (PostToolUse on Write / Edit /
NotebookEdit) and by self-kill-guard-hook.py (PreToolUse on Bash, for heredoc
bodies that are data).

Nothing here judges whether the code is dangerous: that depends on how the
text is later executed, which cannot be known statically. The helpers only find
lines that mention kill-by-pattern tools, de-duplicate reminders per session,
and build the model-facing `additionalContext` message.

Every function is written to fail open: callers wrap them in try/except and a
problem here must never break a tool call.
"""

import hashlib
import json
import os
import re
import time

MAX_LISTED = 10          # matching lines listed in one message
MAX_LINE_CHARS = 160     # per listed line
MAX_CONTEXT_CHARS = 9000  # Claude Code caps additionalContext at 10,000
STATE_MAX_AGE_SECONDS = 7 * 24 * 3600

KILL_WORD_RE = re.compile(r"\b(?:pkill|pgrep|killall|pidof)\b")
# `ps ... | ... grep ... | ... kill` on one line.
PS_CHAIN_RE = re.compile(r"\bps\b.*\|.*\bgrep\b.*\|.*\bkill\b")
# `kill ... $(pgrep|pidof ...)` / backticks are covered by KILL_WORD_RE; this
# is kept separate only so the intent is explicit and testable.
SUBST_RE = re.compile(r"\bkill\b.*(?:\$\(|`)\s*(?:pgrep|pidof)\b")


def line_matches(line: str) -> bool:
    return bool(KILL_WORD_RE.search(line) or PS_CHAIN_RE.search(line) or SUBST_RE.search(line))


def find_kill_lines(text: str) -> list[tuple[int, str]]:
    """(1-based line number, stripped line) for every line that matches."""
    hits: list[tuple[int, str]] = []
    for n, line in enumerate(text.split("\n"), start=1):
        line = line.rstrip("\r")
        if line_matches(line):
            hits.append((n, line.strip()))
    return hits


# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------


def plugin_root() -> str:
    root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
    if root:
        return root
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def readme_path() -> str:
    return os.path.join(plugin_root(), "README.md")


def state_dir() -> str:
    data = os.environ.get("CLAUDE_PLUGIN_DATA", "")
    if data:
        return data
    cache = os.environ.get("XDG_CACHE_HOME", "") or os.path.join(os.path.expanduser("~"), ".cache")
    return os.path.join(cache, "self-kill-guard")


# --------------------------------------------------------------------------
# Per-session de-duplication
# --------------------------------------------------------------------------

STATE_PREFIX = "reminded-"


def _prune(directory: str) -> None:
    cutoff = time.time() - STATE_MAX_AGE_SECONDS
    try:
        for name in os.listdir(directory):
            if not (name.startswith(STATE_PREFIX) and name.endswith(".json")):
                continue
            path = os.path.join(directory, name)
            try:
                if os.path.getmtime(path) < cutoff:
                    os.remove(path)
            except OSError:
                pass
    except OSError:
        pass


def _state_file(directory: str, session_id: str) -> str:
    digest = hashlib.sha256((session_id or "no-session").encode("utf-8", "replace")).hexdigest()[:24]
    return os.path.join(directory, f"{STATE_PREFIX}{digest}.json")


def filter_new(session_id: str, key: str, entries: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Drop entries whose (key, stripped line) was already reported in this
    session. State problems never raise: on any error every entry counts as
    new."""
    try:
        directory = state_dir()
        with open(_state_file(directory, session_id), encoding="utf-8") as fh:
            seen = set(json.load(fh).get(key, []))
    except Exception:
        return entries
    return [(n, line) for n, line in entries if line not in seen]


def mark_reported(session_id: str, key: str, entries: list[tuple[int, str]]) -> None:
    """Remember the lines that were actually shown. Never raises."""
    try:
        directory = state_dir()
        os.makedirs(directory, exist_ok=True)
        _prune(directory)
        path = _state_file(directory, session_id)
        try:
            with open(path, encoding="utf-8") as fh:
                state = json.load(fh)
            if not isinstance(state, dict):
                state = {}
        except Exception:
            state = {}
        known = state.get(key, [])
        for _n, line in entries:
            if line not in known:
                known.append(line)
        state[key] = known
        tmp = f"{path}.{os.getpid()}.tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(state, fh)
        os.replace(tmp, path)
    except Exception:
        pass


# --------------------------------------------------------------------------
# Message
# --------------------------------------------------------------------------

CHECKLIST = """\
Review the kill code against this checklist. If it is already safe, no change is needed.
- `pkill -f`, `pgrep -f` and `ps | grep` patterns match FULL command lines. Make sure the pattern cannot match the shell or command line that will run this file (including its arguments and the Bash tool command that invokes it), nor Claude Code or its ancestor processes.
- Prefer `pgrep -af PATTERN` first, check the output, then kill the literal PIDs it printed.
- The bracket trick (`myservic[e]` instead of `myservice`) hides a pattern from its own text.
- In tests and cleanup code, record PIDs (`$!`, pid files) and kill by PID or process group instead of by pattern.
- `killall NAME`, `pkill NAME` and `pidof NAME` match process names; `node`, `bash`, `sh`, `zsh`, `python` and `claude` are dangerous targets.
- Patternless kills (`kill -1`, `kill 0`, `pkill -u $USER`) are never safe."""


def _shorten(line: str) -> str:
    if len(line) > MAX_LINE_CHARS:
        return line[: MAX_LINE_CHARS - 3] + "..."
    return line


def build_message(header: str, entries: list[tuple[int, str]], line_label: str, note: str = "") -> str:
    """`header` names where the code is; `entries` are (line, text) pairs, at
    most MAX_LISTED of which are listed; `line_label` is e.g. "line"."""
    listed = entries[:MAX_LISTED]
    rest = len(entries) - len(listed)
    parts = [header]
    if note:
        parts.append(note)
    parts.extend(f"  {line_label} {n}: {_shorten(text)}" for n, text in listed)
    if rest > 0:
        parts.append(f"  ... and {rest} more")
    parts.append("")
    parts.append(CHECKLIST)
    parts.append("")
    parts.append(
        "This is a reminder, not an error: it cannot be judged without knowing how the code is run. "
        f"Details: {readme_path()}"
    )
    message = "\n".join(parts)
    if len(message) > MAX_CONTEXT_CHARS:
        message = message[:MAX_CONTEXT_CHARS]
    return message


def context_json(event: str, message: str) -> str:
    """The only stdout a reminder hook may print. No permissionDecision."""
    return json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": message}})
