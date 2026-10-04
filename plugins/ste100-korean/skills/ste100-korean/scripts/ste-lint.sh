#!/usr/bin/env bash
# Launcher for ste-lint.py. Interpreter order:
#   1. the plugin venv ($STE_LINT_VENV or `--venv DIR` as the first argument),
#      when it can import kiwipiepy
#   2. uv run --script
#   3. python3
#   4. python (3.x only)
# Set STE_LINT_DEBUG=1 to print the chosen interpreter on stderr.

set -o errexit
set -o nounset
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LINT="${DIR}/ste-lint.py"

venv="${STE_LINT_VENV:-}"
if [[ "${1:-}" == "--venv" ]]; then
    venv="${2:?ste-lint.sh: --venv needs a directory}"
    shift 2
fi

debug() {
    if [[ "${STE_LINT_DEBUG:-}" == "1" ]]; then
        echo "ste-lint.sh: $*" >&2
    fi
}

# An unexpanded ${CLAUDE_PLUGIN_DATA} (skill installed outside a plugin) is
# not a real path: skip the venv.
if [[ -n "$venv" && "$venv" != *'${'* && -d "$venv" ]]; then
    for candidate in "${venv}/bin/python" "${venv}/Scripts/python.exe"; do
        if [[ -x "$candidate" ]] && "$candidate" -c 'import kiwipiepy' >/dev/null 2>&1; then
            debug "using venv ${candidate}"
            exec "$candidate" "$LINT" "$@"
        fi
    done
    debug "venv ${venv} unusable; falling back"
fi

if command -v uv >/dev/null 2>&1; then
    debug "using uv run --script"
    exec uv run --script "$LINT" "$@"
fi

if command -v python3 >/dev/null 2>&1; then
    debug "using python3"
    exec python3 "$LINT" "$@"
fi

if command -v python >/dev/null 2>&1 \
    && python -c 'import sys; sys.exit(0 if sys.version_info[0] == 3 else 1)' 2>/dev/null; then
    debug "using python"
    exec python "$LINT" "$@"
fi

echo "ste-lint.sh: none of uv, python3, python (3.x) found in PATH" >&2
exit 127
