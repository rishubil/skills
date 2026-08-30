#!/usr/bin/env bash
#
# discord-hang-alert-hook.sh — Claude Code hook that pings Discord when a
# session is BLOCKED waiting for the user: a permission prompt, a question
# from Claude, a subagent needing input, or an MCP elicitation dialog. This
# is NOT for progress or completion notices (see the discord-notify plugin
# for that).
#
# It serves two hooks. The Notification hook does the sending. A PreToolUse
# hook matching the AskUserQuestion tool runs this script with
# --mark-question, which only drops a marker file so the notification that
# follows can be titled as a question instead of a permission request —
# Claude Code reports both under notification_type "permission_prompt".
#
# The hook is registered with a `*` matcher, so it receives EVERY
# notification type Claude Code emits. Filtering against the allowlist of
# "blocked waiting for the user" types happens inside this script (see
# DISCORD_HANG_ALERT_TYPES below) rather than via the matcher, so a
# non-matching type is never silently dropped by Claude Code — it shows up
# in the log as "ignored (<type>)" instead.
#
# IMPORTANT: the Notification hook's exit code and stderr are IGNORED by
# Claude Code, so this script can never block or break a session no
# matter what happens. Every failure path below logs (to the log file
# described under "State/logging", never to stderr — stderr is discarded
# and unreadable) and then exits 0. The only debugging surfaces are that
# log file and, when explicitly enabled, the raw-payload capture
# described under DISCORD_HANG_ALERT_DEBUG.
#
# The Notification hook's stdin JSON schema is NOT officially documented.
# Observed on Claude Code as of 2026-08 (captured with
# DISCORD_HANG_ALERT_DEBUG=1):
#
#   {"session_id": "...", "transcript_path": "...", "cwd": "/project",
#    "prompt_id": "...", "hook_event_name": "Notification",
#    "message": "Claude needs your permission",
#    "notification_type": "permission_prompt"}
#
# Note there is no permission_mode field, contrary to what the docs imply,
# and there IS a "message" field carrying Claude Code's own notification
# text. Since none of this is contractual, every field is still read
# defensively with jq "// alt // empty" fallbacks, and
# DISCORD_HANG_ALERT_DEBUG=1 re-captures the raw payload whenever a Claude
# Code update makes this stale.
#
# This script never reads the transcript file and never includes tool
# arguments or any other session content in the Discord message — only
# the notification type and the project's cwd.

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

# Only these hosts are accepted as a target for the webhook POST. This
# guards against a misconfigured webhook URL silently leaking a
# notification to an arbitrary host.
readonly WEBHOOK_HOST_REGEX='^https://(discord\.com|discordapp\.com|ptb\.discord\.com|canary\.discord\.com)/api/webhooks/'

# clip($n) must return AT MOST $n characters: the "…" marker counts toward
# Discord's per-field limits, so slicing to $n and then appending it yields
# $n + 1 and gets the whole message rejected with HTTP 400.
readonly JQ_CLIP='def clip($n): if $n <= 0 then "" elif (length > $n) then .[0:$n-1] + "…" else . end;'

usage() {
    cat <<'EOF'
Usage:
  discord-hang-alert-hook.sh              Read a Notification hook payload
                                           from stdin and, if it looks like
                                           the session is blocked waiting on
                                           the user, send a Discord alert.
  discord-hang-alert-hook.sh --self-test   Send a synthetic test notification
                                           (bypasses the cooldown, does not
                                           write cooldown state, and prints
                                           diagnostics). Use this to verify
                                           your setup.
  discord-hang-alert-hook.sh --mark-question
                                           PreToolUse companion mode. Reads a
                                           PreToolUse payload from stdin and
                                           only records that an
                                           AskUserQuestion call is starting,
                                           so the next notification for that
                                           session is titled as a question
                                           rather than a permission request.
                                           Never contacts the network and
                                           never writes to stdout.
  discord-hang-alert-hook.sh --help        Show this help.

Purpose:
  This is a Claude Code Notification hook. It fires when a session is
  BLOCKED waiting for the user to respond — a permission prompt, a
  question from Claude, a subagent needing input, or an MCP elicitation
  dialog — and sends a short Discord webhook message so you notice even
  when you're away from the terminal. It is NOT for progress or
  completion notices.

  IMPORTANT: the Notification hook's exit code and stderr are ignored by
  Claude Code. This script can NEVER block or break a Claude Code
  session, no matter what happens (missing config, network failure,
  malformed input, etc.) — every failure path logs and exits 0.

  The hook itself is registered with a `*` matcher, so Claude Code hands
  it every notification type it emits; this script then filters against
  DISCORD_HANG_ALERT_TYPES below. A type that isn't in the allowlist is
  never silently dropped by Claude Code — it shows up in the log as
  "ignored (<type>)".

Webhook URL resolution (first match wins):
  1. DISCORD_HANG_ALERT_WEBHOOK_URL environment variable
  2. DISCORD_WEBHOOK_URL environment variable
  3. first line of "${CLAUDE_PLUGIN_DATA}/webhook"
     (only consulted when CLAUDE_PLUGIN_DATA is set and the file exists)
  4. first line of "${XDG_CONFIG_HOME:-$HOME/.config}/discord-hang-alert/webhook"

  If none of these resolve, the plugin is inert (this is a normal,
  expected state, not an error): it logs "no webhook configured" and
  exits 0.

Environment variables:
  DISCORD_HANG_ALERT_WEBHOOK_URL   Discord webhook URL (highest priority).
  DISCORD_WEBHOOK_URL              Discord webhook URL (shared with the
                                    discord-notify plugin).
  DISCORD_HANG_ALERT_DISABLE       Set to 1 to disable this hook entirely.
                                    No-ops and exits 0 immediately, without
                                    logging anything at all.
  DISCORD_HANG_ALERT_COOLDOWN      Minimum seconds between notifications
                                    for the same session id. Must be a
                                    non-negative integer; any other value
                                    falls back to the default silently.
                                    Kept short because every alert means
                                    work is already stopped: suppressing
                                    one costs you the wait, and the events
                                    are naturally sparse. Default: 60.
  DISCORD_HANG_ALERT_USERNAME      Webhook display username.
                                    Default: "Claude Code".
  DISCORD_HANG_ALERT_DEBUG         Set to 1 to additionally write the raw,
                                    unmodified stdin payload to
                                    "<state dir>/last-payload.json". This
                                    is the only sanctioned way to inspect
                                    the real (undocumented) hook payload
                                    shape.
  DISCORD_HANG_ALERT_TYPES         Allowlist of notification_type values
                                    that trigger an alert. Entries are
                                    separated by commas and/or whitespace
                                    (e.g. "a,b", "a b", "a, b" are all
                                    equivalent). The special value "all"
                                    (case-insensitive) disables filtering
                                    entirely, letting every notification
                                    type through — combine this with
                                    DISCORD_HANG_ALERT_DEBUG=1 to discover
                                    which notification types a given
                                    Claude Code version actually emits
                                    (e.g. whether the AskUserQuestion tool
                                    produces any notification at all).
                                    Default:
                                    permission_prompt,agent_needs_input,elicitation_dialog,elicitation_url_dialog

Config files (used only when the corresponding env var is unset):
  ${CLAUDE_PLUGIN_DATA}/webhook
  ${XDG_CONFIG_HOME:-$HOME/.config}/discord-hang-alert/webhook

State/logging:
  State directory:
    ${CLAUDE_PLUGIN_DATA:-${XDG_STATE_HOME:-$HOME/.local/state}/discord-hang-alert}
  Files inside it:
    question-<id>.marker  set by the PreToolUse companion hook when an
                            AskUserQuestion call is about to run; consumed
                            by the next notification for that session
    session-<id>.last     unix timestamp of the last successful send for
                            that session (used for the cooldown check;
                            pruned automatically after 7 days)
    hang-alert.log         one line per invocation; this is the ONLY
                            debugging surface, since the Notification
                            hook's stderr is discarded and unreadable
    last-payload.json      raw stdin payload, only written when
                            DISCORD_HANG_ALERT_DEBUG=1

Requires: bash, curl, jq.
EOF
}

log_line() {
    # Append one timestamped line to the log file. Best-effort: if the
    # state dir or log file can't be written, there is nowhere to log to,
    # so this silently does nothing (the caller still exits 0).
    local state_dir="$1" message="$2"
    local log_file="${state_dir}/hang-alert.log"
    local timestamp
    # %:z is GNU-only; the portable spelling yields +0900 instead of +09:00.
    timestamp="$(date +%Y-%m-%dT%H:%M:%S%z)"

    # Keep the log from growing unbounded: if it's gotten large, truncate
    # it to its last 200 lines before appending.
    if [[ -f "$log_file" ]]; then
        local size
        size="$(wc -c <"$log_file" 2>/dev/null || echo 0)"
        if (( size > 1048576 )); then
            local tmp_file
            tmp_file="${log_file}.tmp.$$"
            if tail -n 200 "$log_file" >"$tmp_file" 2>/dev/null; then
                mv -- "$tmp_file" "$log_file" 2>/dev/null || rm -f -- "$tmp_file"
            fi
        fi
    fi

    printf '%s %s\n' "$timestamp" "$message" >>"$log_file" 2>/dev/null || true
}

# Extract just the host from a URL, for safe logging (never log the full
# URL — it's a secret).
url_host() {
    local url="$1" host
    host="${url#*://}"
    host="${host%%/*}"
    printf '%s' "${host:-<empty>}"
}

resolve_webhook() {
    # Prints "<source>\t<url>" on stdout ("<source>\t" with empty url if
    # none resolved). Sources: env:DISCORD_HANG_ALERT_WEBHOOK_URL,
    # env:DISCORD_WEBHOOK_URL, "plugin data file", "config file", "none".
    if [[ -n "${DISCORD_HANG_ALERT_WEBHOOK_URL-}" ]]; then
        printf 'DISCORD_HANG_ALERT_WEBHOOK_URL\t%s\n' "$DISCORD_HANG_ALERT_WEBHOOK_URL"
        return 0
    fi
    if [[ -n "${DISCORD_WEBHOOK_URL-}" ]]; then
        printf 'DISCORD_WEBHOOK_URL\t%s\n' "$DISCORD_WEBHOOK_URL"
        return 0
    fi
    if [[ -n "${CLAUDE_PLUGIN_DATA-}" && -f "${CLAUDE_PLUGIN_DATA}/webhook" ]]; then
        local url
        url="$(head -n 1 -- "${CLAUDE_PLUGIN_DATA}/webhook" 2>/dev/null || true)"
        if [[ -n "$url" ]]; then
            printf 'plugin data file\t%s\n' "$url"
            return 0
        fi
    fi
    local config_file="${XDG_CONFIG_HOME:-$HOME/.config}/discord-hang-alert/webhook"
    if [[ -f "$config_file" ]]; then
        local url
        url="$(head -n 1 -- "$config_file" 2>/dev/null || true)"
        if [[ -n "$url" ]]; then
            printf 'config file\t%s\n' "$url"
            return 0
        fi
    fi
    printf 'none\t\n'
}

# Notification types that mean "the session is blocked waiting for the
# user". Overridable with DISCORD_HANG_ALERT_TYPES.
readonly DEFAULT_TYPES='permission_prompt,agent_needs_input,elicitation_dialog,elicitation_url_dialog'

# How long an AskUserQuestion marker dropped by the PreToolUse hook stays
# valid. PreToolUse is awaited before the tool runs and the notification
# follows within the same instant, so this only needs to cover that gap;
# keeping it short stops a stale marker from mislabelling a genuine
# permission prompt that happens to arrive soon after.
readonly QUESTION_MARKER_TTL=15

# Exact-match test of a notification type against the allowlist. Entries in
# the allowlist may be separated by commas and/or whitespace. The whole
# value "all" (case-insensitive) disables filtering. An empty type never
# matches, so a payload whose notification_type field is missing or renamed
# is reported as ignored rather than silently alerting on everything.
type_allowed() {
    local needle="$1"
    local raw="${DISCORD_HANG_ALERT_TYPES:-$DEFAULT_TYPES}"

    if [[ "${raw,,}" == "all" ]]; then
        return 0
    fi
    if [[ -z "$needle" ]]; then
        return 1
    fi

    local item found=1
    local old_ifs="$IFS"
    IFS=$', \t\n'
    # Deliberately unquoted: IFS word-splitting is the point here. Empty
    # fields from repeated separators can never match a non-empty needle.
    # shellcheck disable=SC2086
    for item in $raw; do
        if [[ "$item" == "$needle" ]]; then
            found=0
            break
        fi
    done
    IFS="$old_ifs"
    return "$found"
}

# Human-readable title for a known notification type, or empty for one we
# have no wording for (the caller then falls back to the payload's own
# "message" field).
#
# Claude Code reports the AskUserQuestion tool as permission_prompt with the
# message "Claude needs your permission", so this type alone cannot tell a
# tool awaiting approval from a question awaiting an answer. The companion
# PreToolUse hook resolves that: it drops a marker file, and the caller
# overrides the title when a fresh one is present.
title_for_type() {
    case "$1" in
        permission_prompt)      echo "Waiting for your permission" ;;
        agent_needs_input)      echo "A subagent needs your input" ;;
        elicitation_dialog)     echo "An MCP server is asking for input" ;;
        elicitation_url_dialog) echo "An MCP server is asking you to open a URL" ;;
        *)                      echo "" ;;
    esac
}

build_payload() {
    local notification_type="$1" cwd="$2" session_id="$3" username="$4"
    local message="${5-}" question_pending="${6-0}"
    local title project_name footer_session

    if [[ "$notification_type" == "permission_prompt" && "$question_pending" == "1" ]]; then
        # The PreToolUse hook saw an AskUserQuestion call moments ago, so
        # this permission_prompt is Claude asking something, not a tool
        # waiting for approval.
        title="Claude has a question for you"
    else
        title="$(title_for_type "$notification_type")"
        # Unknown type: prefer Claude Code's own notification text over a
        # generic string, so a type added in a future release still says
        # something useful.
        if [[ -z "$title" ]]; then
            title="${message:-Claude Code needs your attention}"
        fi
    fi
    project_name="$(basename -- "$cwd")"
    footer_session=""
    if [[ -n "$session_id" ]]; then
        footer_session="${session_id:0:8}"
    fi

    jq -n \
        --arg title "$title" \
        --arg project "$project_name" \
        --arg cwd "$cwd" \
        --arg session "$footer_session" \
        --arg username "$username" \
        --argjson color 16776960 \
        "$JQ_CLIP"'
         ($title | clip(256)) as $t
       | ("Claude Code is blocked and cannot continue until you respond.\nProject: `" + $project + "`") as $desc_raw
       | ($desc_raw | clip(4000)) as $d
       | ($cwd + (if $session != "" then " · " + $session else "" end)) as $footer_raw
       | ($footer_raw | clip(2048)) as $f
       | {embeds: [ {title: $t, description: $d, color: $color, footer: {text: $f}} ],
          allowed_mentions: {parse: []}}
         + (if $username != "" then {username: $username} else {} end)'
}

send_payload() {
    # Prints "<http_code>\t<body>" on stdout. Never raises on network
    # failure (curl's own exit status is deliberately ignored via
    # `|| true`, matching this script's must-never-hang / must-never-fail
    # contract), so the caller always gets a status line to inspect.
    local payload="$1" webhook="$2"
    local response http_code body

    response="$(curl --silent --show-error --max-time 5 --request POST \
        --header "Content-Type: application/json" \
        --data "$payload" \
        --write-out $'\n%{http_code}' \
        "$webhook" 2>/dev/null)" || true

    http_code="${response##*$'\n'}"
    body="${response%$'\n'*}"
    [[ "$http_code" =~ ^[0-9]+$ ]] || http_code=""

    printf '%s\t%s\n' "$http_code" "$body"
}

main() {
    local mode="${1---run}"

    if [[ "$mode" == "--help" || "$mode" == "-h" ]]; then
        usage
        exit 0
    fi

    # DISCORD_HANG_ALERT_DISABLE=1 is a hard no-op: no logging at all.
    if [[ "${DISCORD_HANG_ALERT_DISABLE-}" == "1" ]]; then
        exit 0
    fi

    local self_test=0
    if [[ "$mode" == "--self-test" ]]; then
        self_test=1
    fi

    # Required tools. If either is missing there is no way to notify or
    # (for jq) even to build the log line safely with structured data, so
    # just fall back to a plain-text log line and exit.
    local state_dir
    state_dir="${CLAUDE_PLUGIN_DATA:-${XDG_STATE_HOME:-$HOME/.local/state}/discord-hang-alert}"

    if ! command -v curl >/dev/null 2>&1; then
        mkdir -p -- "$state_dir" 2>/dev/null && log_line "$state_dir" "curl not found, cannot send"
        exit 0
    fi
    if ! command -v jq >/dev/null 2>&1; then
        mkdir -p -- "$state_dir" 2>/dev/null && log_line "$state_dir" "jq not found, cannot send"
        exit 0
    fi

    if ! mkdir -p -- "$state_dir" 2>/dev/null; then
        # Nowhere to log to either; nothing more we can do.
        exit 0
    fi

    # Prune stale state (older than 7 days) on every run.
    find "$state_dir" \( -name 'session-*.last' -o -name 'question-*.marker' \) \
        -mtime +7 -delete 2>/dev/null || true

    # --mark-question: the PreToolUse companion hook. It only records that
    # an AskUserQuestion call is about to run, so the Notification handler
    # can tell a question apart from a tool permission request. It never
    # touches the network and never writes to stdout, because PreToolUse is
    # awaited synchronously before the tool runs and stdout there is a
    # decision channel that could block the call.
    if [[ "$mode" == "--mark-question" ]]; then
        local q_payload q_session q_sanitized
        q_payload="$(cat)" || q_payload=""
        q_session="$(jq -r '.session_id // .sessionId // empty' <<<"$q_payload" 2>/dev/null || true)"
        q_sanitized="$(tr -cd 'A-Za-z0-9_-' <<<"$q_session")"
        [[ -n "$q_sanitized" ]] || q_sanitized="unknown"
        printf '%s' "$(date +%s)" >"${state_dir}/question-${q_sanitized}.marker" 2>/dev/null || true
        log_line "$state_dir" "question pending session=${q_session:0:8}"
        exit 0
    fi

    # Resolve cooldown (validated, defaults to 300 on anything invalid).
    local cooldown="${DISCORD_HANG_ALERT_COOLDOWN:-60}"
    if [[ ! "$cooldown" =~ ^[0-9]+$ ]]; then
        cooldown=60
    fi

    local username="${DISCORD_HANG_ALERT_USERNAME:-Claude Code}"

    local webhook_source webhook_url
    IFS=$'\t' read -r webhook_source webhook_url < <(resolve_webhook)

    if (( self_test )); then
        echo "State directory: ${state_dir}"
        echo "Cooldown: ${cooldown}s"
        echo "Webhook source: ${webhook_source}"
        if [[ -z "$webhook_url" ]]; then
            echo "Webhook host: <none configured>"
            log_line "$state_dir" "no webhook configured (self-test)"
            exit 0
        fi
        echo "Webhook host: $(url_host "$webhook_url")"

        if [[ ! "$webhook_url" =~ $WEBHOOK_HOST_REGEX ]]; then
            echo "Result: refusing to send, non-Discord webhook host: $(url_host "$webhook_url")"
            log_line "$state_dir" "refused non-Discord webhook host: $(url_host "$webhook_url") (self-test)"
            exit 0
        fi

        local payload http_code body
        payload="$(build_payload "permission_prompt" "${PWD}" "selftest0000" "$username")"
        IFS=$'\t' read -r http_code body < <(send_payload "$payload" "$webhook_url")

        if [[ "$http_code" == "200" || "$http_code" == "204" ]]; then
            echo "Result: sent (HTTP ${http_code})"
            log_line "$state_dir" "sent (self-test)"
        else
            echo "Result: failed (HTTP ${http_code:-<none>}): ${body:0:500}"
            log_line "$state_dir" "send failed: HTTP ${http_code:-<none>} ${body:0:500} (self-test)"
        fi
        exit 0
    fi

    if [[ -z "$webhook_url" ]]; then
        log_line "$state_dir" "no webhook configured"
        exit 0
    fi

    if [[ ! "$webhook_url" =~ $WEBHOOK_HOST_REGEX ]]; then
        log_line "$state_dir" "refused non-Discord webhook host: $(url_host "$webhook_url")"
        exit 0
    fi

    # Read stdin payload.
    local raw_payload
    raw_payload="$(cat)" || raw_payload=""

    if [[ "${DISCORD_HANG_ALERT_DEBUG-}" == "1" ]]; then
        printf '%s' "$raw_payload" >"${state_dir}/last-payload.json" 2>/dev/null || true
    fi

    if ! jq -e . >/dev/null 2>&1 <<<"$raw_payload"; then
        log_line "$state_dir" "unparseable payload"
        exit 0
    fi

    local notification_type session_id cwd message
    notification_type="$(jq -r '.notification_type // .notificationType // empty' <<<"$raw_payload" 2>/dev/null || true)"
    session_id="$(jq -r '.session_id // .sessionId // empty' <<<"$raw_payload" 2>/dev/null || true)"
    cwd="$(jq -r '.cwd // empty' <<<"$raw_payload" 2>/dev/null || true)"
    # Claude Code's own notification text. Used only as the title for a
    # notification type we have no wording of our own for.
    message="$(jq -r '.message // empty' <<<"$raw_payload" 2>/dev/null || true)"
    [[ -n "$cwd" ]] || cwd="$PWD"

    # Filter here rather than in the hook matcher. The hook is registered
    # with "*" so every notification type reaches this script, which means
    # a type we skip still leaves an "ignored (<type>)" line in the log.
    # With the matcher doing the filtering there was no trace at all, so
    # "no alert arrived" and "no such notification is emitted" looked
    # identical and could not be told apart.
    #
    # This runs BEFORE the cooldown check on purpose: an ignored type must
    # never consume the cooldown budget and hide a later real alert.
    if ! type_allowed "$notification_type"; then
        log_line "$state_dir" "ignored (${notification_type:-<none>})"
        exit 0
    fi

    # Sanitize the session id for use in a filename.
    local sanitized_id
    sanitized_id="$(tr -cd 'A-Za-z0-9_-' <<<"$session_id")"
    [[ -n "$sanitized_id" ]] || sanitized_id="unknown"

    local state_file="${state_dir}/session-${sanitized_id}.last"
    local now
    now="$(date +%s)"

    # Consume any AskUserQuestion marker left by the PreToolUse hook. This
    # happens before the cooldown check on purpose: the marker describes
    # THIS event, so it must be cleared even when the alert is suppressed,
    # or it would go on to mislabel a later permission prompt.
    local question_pending=0
    local marker_file="${state_dir}/question-${sanitized_id}.marker"
    if [[ -f "$marker_file" ]]; then
        local marked
        marked="$(cat -- "$marker_file" 2>/dev/null || echo 0)"
        [[ "$marked" =~ ^[0-9]+$ ]] || marked=0
        if (( now - marked <= QUESTION_MARKER_TTL )); then
            question_pending=1
        fi
        rm -f -- "$marker_file" 2>/dev/null || true
    fi

    if [[ -f "$state_file" ]]; then
        local last remaining
        last="$(cat -- "$state_file" 2>/dev/null || echo 0)"
        [[ "$last" =~ ^[0-9]+$ ]] || last=0
        if (( now - last < cooldown )); then
            remaining=$(( cooldown - (now - last) ))
            log_line "$state_dir" "suppressed (cooldown, ${remaining}s remaining)"
            exit 0
        fi
    fi

    local payload http_code body
    payload="$(build_payload "$notification_type" "$cwd" "$session_id" "$username" "$message" "$question_pending")"
    IFS=$'\t' read -r http_code body < <(send_payload "$payload" "$webhook_url")

    # An `x && y` statement would abort here under `set -o errexit` when the
    # test fails, skipping the result logging entirely for a payload with no
    # session id.
    local session_log=""
    if [[ -n "$session_id" ]]; then
        session_log=" session=${session_id:0:8}"
    fi

    local type_log="${notification_type:-unknown}"
    if (( question_pending )); then
        type_log="${type_log}/question"
    fi

    if [[ "$http_code" == "200" || "$http_code" == "204" ]]; then
        printf '%s' "$now" >"$state_file" 2>/dev/null || true
        log_line "$state_dir" "sent (${type_log})${session_log}"
    else
        log_line "$state_dir" "send failed: HTTP ${http_code:-<none>} ${body:0:500}${session_log}"
    fi

    exit 0
}

main "${1-}"
