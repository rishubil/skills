#!/usr/bin/env bash
# Dispatcher for write-reminder-hook.py (PostToolUse reminder).
#
# The Python script is stdlib only, so plain Python 3 is enough and starts
# faster than `uv run`; uv is only a last resort when no python3 exists. Any
# problem fails open: no output, exit 0 (a reminder must never break a tool
# call, and anything else printed on stdout would break the JSON parsing).

set -o nounset
set -o pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="${SCRIPT_DIR}/write-reminder-hook.py"

if command -v python3 >/dev/null 2>&1; then
    python3 "$PY_SCRIPT" 2>/dev/null || true
elif command -v python >/dev/null 2>&1 \
    && [[ "$(python -c 'import sys; print(sys.version_info[0])' 2>/dev/null)" == "3" ]]; then
    python "$PY_SCRIPT" 2>/dev/null || true
elif command -v uv >/dev/null 2>&1; then
    uv run --offline --no-project --script "$PY_SCRIPT" 2>/dev/null || true
fi
exit 0
