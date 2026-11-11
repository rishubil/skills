#!/usr/bin/env bash
# Regression tests for self-kill-guard-hook.py, driven through its --check mode.
# The test commands are single-quoted on purpose: `$(...)` and backticks must
# reach the hook literally.
# shellcheck disable=SC2016
set -o errexit -o nounset -o pipefail
[[ "${TRACE:-0}" == "1" ]] && set -o xtrace

usage() {
  cat <<'USAGE'
Usage: self-kill-guard-test.sh [-h|--help]

Runs the hook's --check mode against a fixed list of commands, once with the
tree-sitter-bash parser (the default) and once with the shlex fallback
(SELF_KILL_GUARD_PARSER=shlex), and compares the verdict (DENY / ASK / PASS)
with the expected one. It also checks that the parser reported by --check is the
one that was requested, and that the .sh wrapper still denies when uv cannot
install its dependencies (offline, empty cache). Prints one line per case and a
summary; exits 1 if any case fails.

Environment:
  TRACE=1   Enable shell tracing (set -o xtrace).

The reminder sections use temporary CLAUDE_PLUGIN_DATA and file directories.

Note: the verdict also depends on the caller's ancestor processes' command
lines, so do not run this with a command line that itself contains "myworker".
USAGE
}

case "${1:-}" in
  -h | --help)
    usage
    exit 0
    ;;
  "") ;;
  *)
    echo "Unknown argument: $1" >&2
    usage >&2
    exit 2
    ;;
esac

cd "$(dirname "${BASH_SOURCE[0]}")"

hook="../scripts/self-kill-guard-hook.py"
wrapper="../scripts/self-kill-guard-hook.sh"
if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found (needed for the tree-sitter mode)" >&2
  exit 2
fi

# Current mode: "tree-sitter" (default parser) or "shlex" (forced fallback).
mode=""
run_check() {
  if [[ "$mode" == "shlex" ]]; then
    SELF_KILL_GUARD_PARSER=shlex uv run --script "$hook" --check "$1" 2>/dev/null
  else
    env -u SELF_KILL_GUARD_PARSER uv run --script "$hook" --check "$1" 2>/dev/null
  fi
}

pass_count=0
fail_count=0

# expect_split <tree-sitter verdict> <shlex verdict> <command>
expect_split() {
  local want_ts="$1" want_shlex="$2" command="$3"
  local want output first got parser label status
  if [[ "$mode" == "shlex" ]]; then want="$want_shlex"; else want="$want_ts"; fi
  output="$(run_check "$command")" || true
  first="${output%%$'\n'*}"
  got="${first%% *}"
  parser=""
  if [[ "$first" =~ parser=([a-z-]+) ]]; then parser="${BASH_REMATCH[1]}"; fi
  label="${command//$'\n'/\\n}"
  if [[ "$got" == "$want" && "$parser" == "$mode" ]]; then
    status="ok  "
    pass_count=$((pass_count + 1))
  else
    status="FAIL"
    fail_count=$((fail_count + 1))
  fi
  printf '%s want=%-4s got=%-4s parser=%-11s %s\n' "$status" "$want" "$got" "${parser:-?}" "$label"
}

# expect <DENY|ASK|PASS> <command>: same verdict in both modes.
expect() { expect_split "$1" "$1" "$2"; }

cases() {
  # --- DENY: newline is a command separator ---
  expect DENY $'echo a\npkill -f myworker'
  expect DENY $'cd /tmp\npkill -f myworker'
  expect DENY $'echo a # note\npkill -f myworker'
  expect DENY $'echo a;\npkill -f myworker'
  expect DENY $'true &&\npkill -f myworker'

  # --- DENY: shell reserved words before a command ---
  expect DENY 'if true; then pkill -f myworker; fi'
  expect DENY 'for i in 1; do pkill -f myworker; done'
  expect DENY '{ pkill -f myworker; }'
  expect DENY '! pkill -f myworker'
  expect DENY 'if pkill -f myworker; then :; fi'

  # --- DENY: existing behaviour ---
  expect DENY 'pkill -f myworker'
  expect DENY 'cd /tmp; pkill -f myworker'
  expect DENY 'kill $(pgrep -f myworker)'
  expect DENY 'sudo pkill -f myworker'

  # --- PASS ---
  expect PASS $'cd /tmp \\\npkill -f myworker'
  expect PASS '# pkill -f myworker'
  expect PASS 'echo pkill -f myworker'
  expect PASS 'git commit -m "pkill -f myworker"'
  expect PASS $'echo "a\npkill -f myworker"'
  expect PASS 'pgrep -af myworker'
  expect PASS 'kill 123 456'
  expect PASS "pkill -f 'myworke[r]'"
  expect PASS 'pkill -x nod'
  expect PASS 'killall nod'

  # --- Heredocs and stray quotes ---
  expect DENY $'cat <<\'EOF\'\ndon\'t\nEOF\npkill -f myworker'
  expect DENY $'cat <<EOF\ndon\'t\nEOF\npkill -f myworker'
  expect DENY $'cat <<-EOF\ndon\'t\n\tEOF\npkill -f myworker'
  expect DENY $'cat <<EOF\nit\'s\nEOF\necho a\npkill -f myworker'
  expect DENY $'cat <<A <<B\nit\'s\nA\nb\nB\npkill -f myworker'
  expect DENY $'echo don\'t\npkill -f myworker'
  expect PASS "cat <<<'pkill -f myworker'"
  expect PASS $'cat <<\'EOF\'\necho "pkill -f myworker"\nEOF'

  # --- Nested and interpreted code. The shlex fallback cannot see inside
  # quoted strings, so those are known misses there (PASS). ---
  expect DENY $'bash <<\'EOF\'\npkill -f myworker\nEOF'
  expect_split DENY PASS "bash -c 'pkill -f myworker'"
  expect_split DENY PASS 'sh -c "pkill -f myworker"'
  expect_split DENY PASS "eval 'pkill -f myworker'"
  expect DENY 'echo $(pkill -f myworker)'
  expect_split DENY PASS 'echo "$(pkill -f myworker)"'
  expect_split DENY PASS 'echo `pkill -f myworker`'
  expect DENY '( pkill -f myworker )'
  expect DENY 'cat <(pkill -f myworker)'
  expect DENY 'ls **/*(.om[1]) && pkill -f myworker'
  expect DENY 'pgrep -f myworker | xargs kill'
  expect DENY "ps aux | grep myworker | awk '{print \$2}' | xargs kill"
  expect_split DENY PASS "bash <<<'pkill -f myworker'"
  expect DENY $'cat <<EOF | bash\npkill -f myworker\nEOF'
  expect_split DENY PASS "sudo -E /bin/bash -c 'pkill -f myworker'"
  expect DENY 'x=$(pkill -f myworker)'

  # --- Heuristic false positives that the real parser removes ---
  expect_split PASS DENY 'echo then pkill -f myworker'
  expect_split PASS DENY $'cat <<\'EOF\'\npkill -f myworker\nEOF'
  expect PASS "bash -c 'echo pkill -f myworker'"
  expect_split PASS DENY "echo ';' pkill -f myworker"

  # --- Data heredoc that writes kill code: PASS (plus a reminder, checked
  # below) with tree-sitter, still DENY with the fail-closed shlex fallback ---
  expect_split PASS DENY $'cat > /tmp/x.sh <<\'EOF\'\npkill -f myworker\nEOF'
}

for mode in tree-sitter shlex; do
  printf '=== parser: %s ===\n' "$mode"
  cases
  printf '\n'
done

# --- Wrapper fallback: uv cannot install its dependencies (offline, empty
# cache), so the wrapper must replay the same stdin through python3. ---
printf '=== wrapper fallback (UV_OFFLINE=1, empty UV_CACHE_DIR) ===\n'
if command -v python3 >/dev/null 2>&1; then
  empty_cache="$(mktemp -d)"
  trap 'rm -rf "$empty_cache"' EXIT
  payload='{"tool_name":"Bash","tool_input":{"command":"pkill -f myworker"}}'
  wrapper_out="$(SELF_KILL_GUARD_NO_WARMUP=1 UV_OFFLINE=1 UV_CACHE_DIR="$empty_cache" "$wrapper" <<<"$payload" 2>&1)" || true
  decisions="$(grep -c '"permissionDecision": "deny"' <<<"$wrapper_out" || true)"
  if [[ "$decisions" == "1" ]]; then
    printf 'ok   wrapper emitted exactly one deny decision without uv dependencies\n'
    pass_count=$((pass_count + 1))
  else
    printf 'FAIL wrapper output (deny count=%s): %s\n' "$decisions" "$wrapper_out"
    fail_count=$((fail_count + 1))
  fi
  check_out="$(SELF_KILL_GUARD_NO_WARMUP=1 UV_OFFLINE=1 UV_CACHE_DIR="$empty_cache" "$wrapper" --check 'pkill -f myworker' 2>&1)" || true
  if [[ "${check_out%% *}" == "DENY" ]]; then
    printf 'ok   wrapper --check passes through and denies via the fallback\n'
    pass_count=$((pass_count + 1))
  else
    printf 'FAIL wrapper --check output: %s\n' "$check_out"
    fail_count=$((fail_count + 1))
  fi
  rm -rf "$empty_cache"
  trap - EXIT
else
  echo "skip python3 not found; wrapper fallback not tested"
fi

# --- Wrapper warm-up: with an empty uv cache the first call must answer fast
# through the fallback, start a detached background install (stamp file), and
# a later call must use tree-sitter once the install finished. ---
printf '\n=== wrapper warm-up (empty UV_CACHE_DIR, warm-up enabled) ===\n'
if command -v python3 >/dev/null 2>&1; then
  warm_cache="$(mktemp -d)"
  warm_xdg="$(mktemp -d)"
  stamp="${warm_xdg}/self-kill-guard/warmup.stamp"
  # The warm-up is detached, so make sure it is gone before the cache is.
  # shellcheck disable=SC2329 # invoked via trap
  cleanup_warm() {
    local marker="${warm_xdg}/self-kill-guard/warmup.running" warm_pid=""
    if [[ -r "$marker" ]]; then warm_pid="$(<"$marker")"; fi
    if [[ "$warm_pid" =~ ^[0-9]+$ ]]; then
      kill -- "-${warm_pid}" 2>/dev/null || kill "$warm_pid" 2>/dev/null || true
      sleep 0.3
    fi
    rm -rf "$warm_cache" "$warm_xdg"
  }
  trap cleanup_warm EXIT
  payload='{"tool_name":"Bash","tool_input":{"command":"pkill -f myworker"}}'
  t0="${EPOCHREALTIME/[.,]/}"
  warm_out="$(env -u SELF_KILL_GUARD_NO_WARMUP UV_CACHE_DIR="$warm_cache" XDG_CACHE_HOME="$warm_xdg" "$wrapper" <<<"$payload" 2>&1)" || true
  t1="${EPOCHREALTIME/[.,]/}"
  elapsed_ms=$(((t1 - t0) / 1000))
  if [[ "$(grep -c '"permissionDecision": "deny"' <<<"$warm_out" || true)" == "1" && "$elapsed_ms" -lt 3000 ]]; then
    printf 'ok   first call denied via fallback in %d ms\n' "$elapsed_ms"
    pass_count=$((pass_count + 1))
  else
    printf 'FAIL first call (%d ms): %s\n' "$elapsed_ms" "$warm_out"
    fail_count=$((fail_count + 1))
  fi
  if [[ -e "$stamp" ]]; then
    printf 'ok   warm-up stamp file created\n'
    pass_count=$((pass_count + 1))
  else
    printf 'FAIL no warm-up stamp at %s\n' "$stamp"
    fail_count=$((fail_count + 1))
  fi
  ready=0
  for _ in $(seq 1 20); do
    if [[ ! -e "${warm_xdg}/self-kill-guard/warmup.running" ]] \
      && UV_CACHE_DIR="$warm_cache" uv run --offline --script "$hook" --help >/dev/null 2>&1; then
      ready=1
      break
    fi
    sleep 1
  done
  if ((ready == 1)); then
    later_out="$(SELF_KILL_GUARD_NO_WARMUP=1 UV_CACHE_DIR="$warm_cache" "$wrapper" --check 'pkill -f myworker' 2>&1)" || true
    if [[ "${later_out%% *}" == "DENY" && "$later_out" == *"parser=tree-sitter"* ]]; then
      printf 'ok   later call uses tree-sitter after the warm-up finished\n'
      pass_count=$((pass_count + 1))
    else
      printf 'FAIL later call output: %s\n' "${later_out%%$'\n'*}"
      fail_count=$((fail_count + 1))
    fi
  else
    echo "skip warm-up did not finish within 20 s (network unavailable?); tree-sitter handover not tested"
  fi
  cleanup_warm
  trap - EXIT
else
  echo "skip python3 not found; wrapper warm-up not tested"
fi

# --- Reminders: heredoc data in a Bash command (PreToolUse) and file writes
# (PostToolUse). Both only add non-blocking additionalContext. ---
rtmp="$(mktemp -d)"
trap 'rm -rf "$rtmp"' EXIT
readme="$(cd .. && pwd)/README.md"
write_hook="../scripts/write-reminder-hook.sh"
export CLAUDE_PLUGIN_DATA="${rtmp}/data"
unset CLAUDE_PLUGIN_ROOT

# record <description> <ok|bad> [detail]
record() {
  if [[ "$2" == "ok" ]]; then
    printf 'ok   %s\n' "$1"
    pass_count=$((pass_count + 1))
  else
    printf 'FAIL %s %s\n' "$1" "${3:-}"
    fail_count=$((fail_count + 1))
  fi
}

# mk_payload <session> <tool> [key value]...: hook payload JSON on stdout.
mk_payload() {
  uv run --no-project python -c '
import json, sys
a = sys.argv[1:]
print(json.dumps({"session_id": a[0], "tool_name": a[1], "tool_input": dict(zip(a[2::2], a[3::2]))}))
' "$@"
}

# validate_ctx <event> <needle>...: stdin must be one JSON object with
# hookSpecificOutput.additionalContext containing every needle, the right
# hookEventName and NO permissionDecision key.
validate_ctx() {
  uv run --no-project python -c '
import json, sys
d = json.load(sys.stdin)
assert list(d) == ["hookSpecificOutput"], list(d)
h = d["hookSpecificOutput"]
assert h["hookEventName"] == sys.argv[1], h["hookEventName"]
assert "permissionDecision" not in h and "permissionDecisionReason" not in h
assert set(h) == {"hookEventName", "additionalContext"}, set(h)
assert len(h["additionalContext"]) <= 10000
for needle in sys.argv[2:]:
    assert needle in h["additionalContext"], needle
' "$@"
}

printf '=== heredoc reminder (Bash, PreToolUse) ===\n'
heredoc_cmd=$'cat > /tmp/x.sh <<\'EOF\'\necho start\npkill -f myworker\nEOF'
out="$(env -u SELF_KILL_GUARD_PARSER uv run --script "$hook" --check "$heredoc_cmd" 2>/dev/null)" || true
first="${out%%$'\n'*}"
if [[ "${first%% *}" == "PASS" && "$first" == *"parser=tree-sitter"* && "$out" == *"--- REMIND ---"* && "$out" == *"pkill -f myworker"* && "$out" == *"$readme"* ]]; then
  record "--check: data heredoc is PASS with a REMIND section and the README path" ok
else
  record "--check: data heredoc is PASS with a REMIND section and the README path" bad "$out"
fi
out="$(env -u SELF_KILL_GUARD_PARSER uv run --script "$hook" --check 'cat <<<"pkill -f myworker"' 2>/dev/null)" || true
if [[ "${out%% *}" == "PASS" && "$out" == *"--- REMIND ---"* ]]; then
  record "--check: here-string into a non-shell gets a reminder" ok
else
  record "--check: here-string into a non-shell gets a reminder" bad "$out"
fi
out="$(env -u SELF_KILL_GUARD_PARSER uv run --script "$hook" --check 'pkill -f myworker' 2>/dev/null)" || true
if [[ "${out%% *}" == "DENY" && "$out" != *"REMIND"* ]]; then
  record "--check: plain pkill -f is DENY with no reminder" ok
else
  record "--check: plain pkill -f is DENY with no reminder" bad "$out"
fi
out="$(env -u SELF_KILL_GUARD_PARSER uv run --script "$hook" --check $'cat > /tmp/x.sh <<\'EOF\'\necho hello\nEOF' 2>/dev/null)" || true
if [[ "${out%% *}" == "PASS" && "$out" != *"REMIND"* ]]; then
  record "--check: harmless heredoc stays silent" ok
else
  record "--check: harmless heredoc stays silent" bad "$out"
fi
out="$(SELF_KILL_GUARD_PARSER=shlex uv run --script "$hook" --check "$heredoc_cmd" 2>/dev/null)" || true
if [[ "${out%% *}" == "DENY" && "$out" != *"REMIND"* ]]; then
  record "--check: shlex mode stays DENY without a reminder" ok
else
  record "--check: shlex mode stays DENY without a reminder" bad "$out"
fi

hd_payload="$(mk_payload h1 Bash command "$heredoc_cmd")"
out="$(SELF_KILL_GUARD_NO_WARMUP=1 "$wrapper" <<<"$hd_payload" 2>/dev/null)" || true
if [[ -n "$out" ]] && validate_ctx PreToolUse "pkill -f myworker" "$readme" <<<"$out" 2>/dev/null; then
  record "hook mode: PreToolUse additionalContext, no permissionDecision" ok
else
  record "hook mode: PreToolUse additionalContext, no permissionDecision" bad "$out"
fi
out="$(SELF_KILL_GUARD_NO_WARMUP=1 "$wrapper" <<<"$hd_payload" 2>/dev/null)" || true
if [[ -z "$out" ]]; then
  record "hook mode: same heredoc line in the same session is not repeated" ok
else
  record "hook mode: same heredoc line in the same session is not repeated" bad "$out"
fi
hd_payload2="$(mk_payload h2 Bash command "$heredoc_cmd")"
out="$(SELF_KILL_GUARD_NO_WARMUP=1 "$wrapper" <<<"$hd_payload2" 2>/dev/null)" || true
if [[ -n "$out" ]] && validate_ctx PreToolUse "pkill -f myworker" <<<"$out" 2>/dev/null; then
  record "hook mode: a different session is reminded again" ok
else
  record "hook mode: a different session is reminded again" bad "$out"
fi
out="$(SELF_KILL_GUARD_NO_WARMUP=1 "$wrapper" <<<"$(mk_payload h3 Bash command 'pkill -f myworker')" 2>/dev/null)" || true
if [[ "$out" == *'"permissionDecision": "deny"'* && "$out" != *additionalContext* ]]; then
  record "hook mode: plain pkill -f is still a deny, no reminder" ok
else
  record "hook mode: plain pkill -f is still a deny, no reminder" bad "$out"
fi

printf '\n=== write reminder (PostToolUse: Write / Edit / NotebookEdit) ===\n'
wr_content=$'#!/bin/sh\necho start\npkill -f myworker\necho done\n'
wr_payload="$(mk_payload w1 Write file_path "${rtmp}/a.sh" content "$wr_content")"
out="$("$write_hook" <<<"$wr_payload")" || true
if [[ -n "$out" ]] && validate_ctx PostToolUse "${rtmp}/a.sh" "line 3: pkill -f myworker" "$readme" "not an error" <<<"$out" 2>/dev/null; then
  record "Write: kill code on line 3 gives valid additionalContext (no permissionDecision)" ok
else
  record "Write: kill code on line 3 gives valid additionalContext (no permissionDecision)" bad "$out"
fi
out="$("$write_hook" <<<"$wr_payload")" || true
if [[ -z "$out" ]]; then
  record "Write: same file and line again in the same session is silent" ok
else
  record "Write: same file and line again in the same session is silent" bad "$out"
fi
out="$("$write_hook" <<<"$(mk_payload w2 Write file_path "${rtmp}/a.sh" content "$wr_content")")" || true
if [[ -n "$out" ]]; then
  record "Write: a different session is reminded again" ok
else
  record "Write: a different session is reminded again" bad
fi
out="$("$write_hook" <<<"$(mk_payload w3 Write file_path "${rtmp}/b.sh" content $'echo a\necho b\n')")" || true
if [[ -z "$out" ]]; then
  record "Write: no kill words gives no output" ok
else
  record "Write: no kill words gives no output" bad "$out"
fi
out="$("$write_hook" <<<"$(mk_payload w3 Write file_path "${rtmp}/notes.md" content $'# Notes\n\nDo not run pkill here.\n')")" || true
if [[ -n "$out" ]] && validate_ctx PostToolUse "notes.md" "line 3" <<<"$out" 2>/dev/null; then
  record "Write: a .md file is scanned too (all file types)" ok
else
  record "Write: a .md file is scanned too (all file types)" bad "$out"
fi
many=""
for i in $(seq 1 12); do many+="pkill -f myworker${i}"$'\n'; done
out="$("$write_hook" <<<"$(mk_payload w4 Write file_path "${rtmp}/many.sh" content "$many")")" || true
if [[ -n "$out" ]] && validate_ctx PostToolUse "line 10:" "and 2 more" <<<"$out" 2>/dev/null && [[ "$out" != *"line 11:"* ]]; then
  record "Write: at most 10 lines are listed, then 'and N more'" ok
else
  record "Write: at most 10 lines are listed, then 'and N more'" bad "$out"
fi

# Edit: the file on disk already holds the edit; report absolute line numbers.
printf '%s\n' 'echo one' 'echo two' 'echo three' 'pgrep -f myworker | xargs kill' 'echo five' >"${rtmp}/e.sh"
out="$("$write_hook" <<<"$(mk_payload e1 Edit file_path "${rtmp}/e.sh" old_string 'echo four' new_string 'pgrep -f myworker | xargs kill' replace_all false)")" || true
if [[ -n "$out" ]] && validate_ctx PostToolUse "line 4: pgrep -f myworker | xargs kill" <<<"$out" 2>/dev/null; then
  record "Edit: absolute line number of new_string is reported" ok
else
  record "Edit: absolute line number of new_string is reported" bad "$out"
fi
printf '%s\n' 'killall myworker' 'echo x' 'killall myworker' >"${rtmp}/dup.sh"
out="$("$write_hook" <<<"$(mk_payload e2 Edit file_path "${rtmp}/dup.sh" old_string 'a' new_string 'killall myworker')")" || true
if [[ -n "$out" ]] && validate_ctx PostToolUse "line 1: killall myworker" "relative to the edited fragment" <<<"$out" 2>/dev/null; then
  record "Edit: a non-unique new_string falls back to fragment-relative lines and says so" ok
else
  record "Edit: a non-unique new_string falls back to fragment-relative lines and says so" bad "$out"
fi
out="$("$write_hook" <<<"$(mk_payload e3 Edit file_path "${rtmp}/e.sh" old_string 'pkill -f myworker' new_string 'echo removed')")" || true
if [[ -z "$out" ]]; then
  record "Edit: kill words only in old_string give no output" ok
else
  record "Edit: kill words only in old_string give no output" bad "$out"
fi

out="$("$write_hook" <<<"$(mk_payload n1 NotebookEdit notebook_path "${rtmp}/n.ipynb" new_source 'killall myworker' cell_type code)")" || true
if [[ -n "$out" ]] && validate_ctx PostToolUse "n.ipynb" "killall myworker" <<<"$out" 2>/dev/null; then
  record "NotebookEdit: kill code in new_source gives a reminder" ok
else
  record "NotebookEdit: kill code in new_source gives a reminder" bad "$out"
fi

rc=0
out="$("$write_hook" <<<'{"tool_name": "Write", "tool_input": {broken')" || rc=$?
if [[ "$rc" == "0" && -z "$out" ]]; then
  record "malformed JSON: exit 0, no output" ok
else
  record "malformed JSON: exit 0, no output" bad "rc=$rc out=$out"
fi
rc=0
out="$(CLAUDE_PLUGIN_DATA=/proc/nonexistent/state "$write_hook" <<<"$(mk_payload s1 Write file_path "${rtmp}/z.sh" content 'pkill -f myworker')")" || rc=$?
if [[ "$rc" == "0" && -n "$out" ]] && validate_ctx PostToolUse "line 1" <<<"$out" 2>/dev/null; then
  record "unwritable state dir never breaks the hook" ok
else
  record "unwritable state dir never breaks the hook" bad "rc=$rc out=$out"
fi

# State files older than 7 days are pruned the next time state is written.
old_state="${CLAUDE_PLUGIN_DATA}/reminded-old.json"
echo '{}' >"$old_state"
touch -d '10 days ago' "$old_state"
"$write_hook" <<<"$(mk_payload p1 Write file_path "${rtmp}/p.sh" content 'pidof myworker')" >/dev/null || true
if [[ ! -e "$old_state" ]]; then
  record "state files older than 7 days are pruned" ok
else
  record "state files older than 7 days are pruned" bad
fi

rm -rf "$rtmp"
trap - EXIT

printf '\n%d passed, %d failed\n' "$pass_count" "$fail_count"
if ((fail_count > 0)); then
  exit 1
fi
