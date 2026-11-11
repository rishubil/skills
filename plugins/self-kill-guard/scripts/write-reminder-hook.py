#!/usr/bin/env python3
"""
PostToolUse hook for Write / Edit / NotebookEdit: when the text just written
mentions kill-by-pattern code (`pkill`, `pgrep`, `killall`, `pidof`, a
`ps | grep | kill` chain), add a non-blocking reminder to the model's context
asking it to re-check that code. Whether the code is dangerous depends on how
the file is later executed, so nothing is blocked and nothing is decided here.

Output is either nothing or exactly one JSON object:
  {"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "..."}}
Stdlib only, no subprocesses. Fails open: any error exits 0 without output.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PATH_KEYS = {"file_path", "notebook_path", "path"}
SKIP_KEYS = PATH_KEYS | {"old_string"}


def scan_edit(tool_input: dict) -> tuple[str, str, list, str]:
    """Edit: report absolute line numbers when new_string is found exactly once
    in the file as it is on disk now."""
    import kill_reminder as kr

    new = tool_input.get("new_string")
    path = tool_input.get("file_path", "")
    if not isinstance(new, str) or not new:
        return path, "", [], ""
    hits = kr.find_kill_lines(new)
    if not hits:
        return path, "", [], ""
    note = ""
    offset = None
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            content = fh.read()
        if content.count(new) == 1:
            offset = content[: content.index(new)].count("\n")
    except Exception:
        pass
    if offset is None:
        note = "(Line numbers are relative to the edited fragment; the new text could not be located uniquely in the file.)"
    else:
        hits = [(n + offset, text) for n, text in hits]
    return path, "", hits, note


def collect(data: dict) -> tuple[str, list, str]:
    """Returns (path, [(line, text)], note)."""
    import kill_reminder as kr

    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input")
    if not isinstance(tool_input, dict):
        return "", [], ""

    if tool == "Write":
        content = tool_input.get("content")
        path = tool_input.get("file_path", "")
        if not isinstance(content, str):
            return path, [], ""
        return path, kr.find_kill_lines(content), ""

    if tool == "Edit":
        path, _unused, hits, note = scan_edit(tool_input)
        return path, hits, note

    # NotebookEdit (content field name is undocumented): scan every string
    # value except paths and old_string; line numbers are per value.
    path = tool_input.get("notebook_path") or tool_input.get("file_path") or ""
    hits = []
    for key, value in tool_input.items():
        if key in SKIP_KEYS or not isinstance(value, str):
            continue
        hits.extend(kr.find_kill_lines(value))
    note = "(Line numbers are relative to the edited cell or fragment.)" if hits else ""
    return path, hits, note


def main() -> None:
    import kill_reminder as kr

    if os.environ.get("SELF_KILL_GUARD_DISABLE") == "1":
        return
    data = json.load(sys.stdin)
    if not isinstance(data, dict):
        return
    path, hits, note = collect(data)
    if not hits:
        return
    session_id = str(data.get("session_id", ""))
    key = path or "<unknown-file>"
    fresh = kr.filter_new(session_id, key, hits)
    if not fresh:
        return
    shown = fresh[: kr.MAX_LISTED]
    message = kr.build_message(
        f"You just modified {key}, which contains process-kill code:",
        fresh,
        "line",
        note,
    )
    print(kr.context_json("PostToolUse", message))
    kr.mark_reported(session_id, key, shown)


if __name__ == "__main__":
    try:
        main()
    except BaseException:  # fail open, silently
        pass
    sys.exit(0)
