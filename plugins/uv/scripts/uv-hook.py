#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
# ]
# ///
"""
PreToolUse hook: enforces uv-based Python workflow.

Checks for two anti-patterns:
1. Direct python/python3/pip/pip3 invocations — suggests uv run instead.
2. `uv run pip install` or `uv pip install` — suggests uv add instead.
"""

import json
import re
import sys

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

# Check 1: uv run pip install / uv pip install → suggest uv add
if re.search(r"\buv\s+(?:run\s+)?pip3?\s+install\b", command):
    packages = re.sub(r".*\buv\s+(?:run\s+)?pip3?\s+install\b\s*", "", command).strip()
    packages = re.sub(r"\s*-[a-zA-Z-]+(?:\s+\S+)?", "", packages).strip()

    hint = "Hint: `uv run pip install` detected. Use `uv add` instead —"
    hint += " this project manages dependencies through uv, not pip."
    if packages:
        hint += f"\n  Suggested command: uv add {packages}"

    print(hint, file=sys.stderr)
    sys.exit(2)

# Check 2: direct python/python3/pip/pip3 (not via uv run) → suggest uv run
if re.match(r"\buv\s+run\b", command):
    sys.exit(0)

if re.search(r"(?:^|&&|\|\||;|\|)\s*(?:python3?|pip3?)\b", command):
    print(
        "Hint: direct python/pip detected. Use `uv run python` instead —"
        " this project requires all Python commands to go through uv.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
