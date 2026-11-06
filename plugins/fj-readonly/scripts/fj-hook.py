#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
# ]
# ///
"""
PreToolUse hook: detects direct `fj` (forgejo-cli) invocations for read-only
commands and suggests using the fj-readonly wrapper instead.

The read-only allowlist lives only in bin/fj-readonly. This hook asks the
wrapper (dry-run mode) whether the arguments are read-only, so there is a
single source of truth.

Write commands (fj issue create, fj pr merge, etc.) are left alone; those
require explicit user permission and should use `fj` directly.
"""

import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

WRAPPER = Path(__file__).resolve().parent.parent / "bin" / "fj-readonly"
OPERATOR_CHARS = set("();<>|&\n")
ENV_ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")


def tokenize(command: str) -> list[str] | None:
    lexer = shlex.shlex(command, posix=True, punctuation_chars="();<>|&\n")
    lexer.whitespace_split = True
    lexer.whitespace = " \t\r"
    try:
        return list(lexer)
    except ValueError:
        return None


def split_segments(tokens: list[str]) -> list[list[str]]:
    segments: list[list[str]] = [[]]
    for token in tokens:
        if set(token) <= OPERATOR_CHARS:
            segments.append([])
        else:
            segments[-1].append(token)
    return [s for s in segments if s]


def is_readonly(args: list[str]) -> bool:
    env = {**os.environ, "FJ_READONLY_DRY_RUN": "1"}
    try:
        result = subprocess.run(
            ["bash", str(WRAPPER), *args],
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def main() -> int:
    try:
        data = json.load(sys.stdin)
        command = data.get("tool_input", {}).get("command", "")
    except (ValueError, AttributeError):
        return 0
    if not isinstance(command, str) or not command or not WRAPPER.is_file():
        return 0

    tokens = tokenize(command)
    if tokens is None:
        return 0

    for segment in split_segments(tokens):
        i = 0
        while i < len(segment) and ENV_ASSIGNMENT.match(segment[i]):
            i += 1
        if i >= len(segment) or os.path.basename(segment[i]) != "fj":
            continue
        args = segment[i + 1 :]
        if not args or not is_readonly(args):
            continue
        shown = " ".join(args[:2])
        print(
            f"Hint: `fj {shown}` is a read-only command. Use"
            f" `fj-readonly` instead of `fj` directly.\n"
            f"  Example: fj-readonly {shlex.join(args)}",
            file=sys.stderr,
        )
        return 2
    return 0


sys.exit(main())
