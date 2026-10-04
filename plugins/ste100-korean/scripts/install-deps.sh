#!/usr/bin/env bash
# Install requirements.txt into ${CLAUDE_PLUGIN_DATA}/venv (kiwipiepy for the
# Korean morphology rules). Safe to run concurrently and repeatedly: a lock
# directory serializes installs and a stamp file records the installed
# requirements. Output goes to stdout/stderr; the caller redirects it.

set -o errexit
set -o nounset
set -o pipefail

ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
DATA="${CLAUDE_PLUGIN_DATA:?CLAUDE_PLUGIN_DATA is not set}"
REQUIREMENTS="${ROOT}/requirements.txt"
VENV="${DATA}/venv"
STAMP="${DATA}/requirements.installed"
LOCK="${DATA}/.install.lock"
STALE_MINUTES=30

mkdir -p "$DATA"

if cmp -s "$REQUIREMENTS" "$STAMP" 2>/dev/null; then
    echo "install-deps: already installed"
    exit 0
fi

# A lock older than STALE_MINUTES belongs to a dead installer.
if [[ -d "$LOCK" ]] && [[ -n "$(find "$LOCK" -maxdepth 0 -mmin "+${STALE_MINUTES}" 2>/dev/null)" ]]; then
    echo "install-deps: removing stale lock"
    rm -rf "$LOCK"
fi

if ! mkdir "$LOCK" 2>/dev/null; then
    echo "install-deps: another install is running; exiting"
    exit 0
fi
trap 'rm -rf "$LOCK"' EXIT

# Another installer may have finished between the first check and the lock.
if cmp -s "$REQUIREMENTS" "$STAMP" 2>/dev/null; then
    echo "install-deps: already installed"
    exit 0
fi

venv_python() {
    if [[ -x "${VENV}/bin/python" ]]; then
        echo "${VENV}/bin/python"
    elif [[ -x "${VENV}/Scripts/python.exe" ]]; then
        echo "${VENV}/Scripts/python.exe"
    else
        return 1
    fi
}

# errexit is ignored inside `if`, so each step returns explicitly.
install_venv() {
    local py base
    if command -v uv >/dev/null 2>&1; then
        echo "install-deps: using uv"
        uv venv "$VENV" || return 1
        py="$(venv_python)" || return 1
        uv pip install --python "$py" -r "$REQUIREMENTS" || return 1
    else
        if command -v python3 >/dev/null 2>&1; then
            base=python3
        elif command -v python >/dev/null 2>&1; then
            base=python
        else
            echo "install-deps: neither uv nor python3 found" >&2
            return 1
        fi
        echo "install-deps: using ${base} -m venv"
        "$base" -m venv "$VENV" || return 1
        py="$(venv_python)" || return 1
        "$py" -m pip install -r "$REQUIREMENTS" || return 1
    fi
    "$py" -c 'import kiwipiepy' || return 1
}

rm -f "$STAMP"
rm -rf "$VENV"
if install_venv; then
    cp "$REQUIREMENTS" "$STAMP"
    echo "install-deps: done"
else
    rm -f "$STAMP"
    rm -rf "$VENV"
    echo "install-deps: failed" >&2
    exit 1
fi
