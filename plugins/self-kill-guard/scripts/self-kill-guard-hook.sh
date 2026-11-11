#!/usr/bin/env bash
# Dispatcher for self-kill-guard-hook.py.
#
# Hot path: `uv run --offline --script` — only ever uses the already cached
# environment (tree-sitter packages), so latency never depends on the network.
# If that fails (dependencies not cached yet, uv missing, any uv error) a
# throttled, detached background warm-up installs the dependencies for the
# next calls, and THIS call is answered by a plain Python 3, where the script
# falls back to its stdlib-only shlex heuristic.

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="${SCRIPT_DIR}/self-kill-guard-hook.py"

# Seconds the cached-environment uv attempt may take (hooks.json allows 10s).
UV_TIMEOUT="${SELF_KILL_GUARD_UV_TIMEOUT:-7}"
# Minutes between background warm-up attempts.
WARMUP_THROTTLE_MIN=10
# A running warm-up holds uv's cache lock, so `uv run --offline` would block on
# it. A marker file (valid for 5 min, the warm-up's own timeout) tells the hot
# path to skip uv and use the fallback straight away.
WARMUP_DIR="${XDG_CACHE_HOME:-${HOME:-/tmp}/.cache}/self-kill-guard"
WARMUP_STAMP="${WARMUP_DIR}/warmup.stamp"
WARMUP_RUNNING="${WARMUP_DIR}/warmup.running"

# True if file $1 exists and was modified within the last $2 minutes.
fresh_file() {
    [[ -e "$1" && -n "$(find "$1" -mmin "-$2" 2>/dev/null)" ]]
}

# Print the first usable Python 3 interpreter, or nothing.
find_python3() {
    local py_major
    if command -v python3 >/dev/null 2>&1; then
        echo python3
    elif command -v python >/dev/null 2>&1; then
        py_major="$(python -c 'import sys; print(sys.version_info[0])' 2>/dev/null || echo 0)"
        if [[ "$py_major" == "3" ]]; then
            echo python
        fi
    fi
}

# Install the pinned dependencies in the background so a later call can use
# them. Never waits, never inherits the hook's stdout/stderr (Claude Code would
# wait for the pipe to close), throttled by a stamp file, and never fails.
warm_up() {
    if [[ "${SELF_KILL_GUARD_NO_WARMUP:-0}" == "1" ]]; then
        return 0
    fi
    mkdir -p "$WARMUP_DIR" 2>/dev/null || return 0
    if fresh_file "$WARMUP_STAMP" "$WARMUP_THROTTLE_MIN"; then
        return 0
    fi
    touch "$WARMUP_STAMP" "$WARMUP_RUNNING" 2>/dev/null || return 0

    local -a cmd=(uv run --script "$PY_SCRIPT" --help)
    if command -v timeout >/dev/null 2>&1; then
        cmd=(timeout 300 "${cmd[@]}")
    fi
    if command -v setsid >/dev/null 2>&1; then
        cmd=(setsid "${cmd[@]}")
    elif command -v nohup >/dev/null 2>&1; then
        cmd=(nohup "${cmd[@]}")
    fi
    # The subshell must not inherit the hook's stdout/stderr either.
    # The marker records the warm-up's PID (also useful for cleanup).
    (
        "${cmd[@]}" &
        warm_pid=$!
        echo "$warm_pid" >"$WARMUP_RUNNING" 2>/dev/null || true
        wait "$warm_pid" || true
        rm -f "$WARMUP_RUNNING"
    ) </dev/null >/dev/null 2>&1 &
    disown 2>/dev/null || true
    return 0
}

PYTHON="$(find_python3)"

# The PreToolUse JSON arrives on stdin and can only be read once; buffer it so
# both attempts see it. With arguments (--check, --help) stdin is not used.
payload=""
if (($# == 0)); then
    payload="$(cat)"
fi

if command -v uv >/dev/null 2>&1 && ! fresh_file "$WARMUP_RUNNING" 5; then
    uv_cmd=(uv run --offline --script "$PY_SCRIPT" "$@")
    if command -v timeout >/dev/null 2>&1; then
        uv_cmd=(timeout "$UV_TIMEOUT" "${uv_cmd[@]}")
    fi
    # Output is captured so that a failed attempt can never leave partial
    # output behind and a successful one is emitted exactly once.
    uv_status=0
    if [[ -n "$PYTHON" ]]; then
        uv_out="$("${uv_cmd[@]}" <<<"$payload" 2>/dev/null)" || uv_status=$?
    else
        uv_out="$("${uv_cmd[@]}" <<<"$payload")" || uv_status=$?
    fi
    if ((uv_status == 0)); then
        if [[ -n "$uv_out" ]]; then
            printf '%s\n' "$uv_out"
        fi
        exit 0
    fi
    warm_up || true
fi

if [[ -n "$PYTHON" ]]; then
    exec "$PYTHON" "$PY_SCRIPT" "$@" <<<"$payload"
fi

# A guard that cannot run must not break every Bash call — fail open
# (silently, aside from the stderr note) rather than exiting nonzero on
# every single command in the session.
echo "self-kill-guard: no working 'uv' and no Python 3.x ('python3', 'python') found in PATH; guard is disabled for this call" >&2
exit 0
