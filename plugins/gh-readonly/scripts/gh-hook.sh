#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="${SCRIPT_DIR}/gh-hook.py"

if command -v uv >/dev/null 2>&1; then
    exec uv run --script "$PY_SCRIPT"
elif command -v python3 >/dev/null 2>&1; then
    exec python3 "$PY_SCRIPT"
elif command -v python >/dev/null 2>&1; then
    py_major="$(python -c 'import sys; print(sys.version_info[0])' 2>/dev/null || echo 0)"
    if [[ "$py_major" == "3" ]]; then
        exec python "$PY_SCRIPT"
    fi
    echo "gh-hook: 'python' found but is not Python 3.x (major=$py_major)" >&2
    exit 1
else
    echo "gh-hook: none of 'uv', 'python3', 'python' (3.x) found in PATH" >&2
    exit 1
fi
