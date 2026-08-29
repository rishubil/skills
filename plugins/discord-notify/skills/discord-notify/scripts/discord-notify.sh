#!/usr/bin/env bash
#
# discord-notify.sh — Send a short notification to Discord via an incoming
# webhook.
#
# By default the message becomes a rich embed; --plain sends a plain
# "content" message instead. Mentions are always suppressed, failed sends
# are never retried, and the webhook URL is validated before use so a
# misconfigured variable can never leak a message to an arbitrary host.
#
# Auth: the webhook URL is resolved in this order:
#   1. -w/--webhook
#   2. DISCORD_WEBHOOK_URL environment variable
#   3. 1Password CLI (op), item "Discord Webhook URL", password field
#
# Requires: bash, curl, jq; the 1Password CLI (op) is optional and only
# used as a fallback when no webhook URL is supplied another way.

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

readonly PROGNAME="${0##*/}"
readonly MAX_DESC=4000
readonly MAX_CONTENT=1900
# Discord rejects a message whose embeds sum to more than 6000 characters
# across title + description + footer. Clipping each field independently is
# not enough (256 + 4000 + 2048 = 6304), so the description is additionally
# shrunk to fit whatever budget the title and footer leave. 5900 keeps a
# margin for the ellipsis characters clip() appends.
readonly MAX_EMBED_TOTAL=5900

# Only these hosts are accepted as a target for the webhook POST. This
# guards against a misconfigured DISCORD_WEBHOOK_URL (or a bad --webhook
# value) silently leaking message content to an arbitrary host.
readonly WEBHOOK_HOST_REGEX='^https://(discord\.com|discordapp\.com|ptb\.discord\.com|canary\.discord\.com)/api/webhooks/'

usage() {
    cat <<'EOF'
Usage:
  discord-notify.sh [options] [message text...]
  echo "message" | discord-notify.sh [options]

Send a short notification to Discord via an incoming webhook. By default
the message body becomes a rich embed; pass --plain to send it as a plain
content message instead.

Options:
  -t, --title <text>       Embed title (ignored with --plain).
  -c, --color <value>      Embed color (ignored with --plain). One of the
                            names green, red, blue, yellow, orange,
                            gray/grey; a "#rrggbb" hex value; or a raw
                            decimal color integer. Default: blue.
  -f, --footer <text>      Embed footer text (ignored with --plain).
  -u, --username <text>    Override the webhook's default username.
  -w, --webhook <url>      Discord webhook URL. Takes priority over
                            DISCORD_WEBHOOK_URL and the 1Password fallback.
  -p, --plain              Send a plain content message instead of an embed.
  -n, --dry-run            Print the JSON payload instead of sending it.
  -h, --help               Show this help.

Message body:
  Positional arguments are joined with spaces to form the message body.
  If none are given and stdin is not a terminal, the body is read from
  stdin instead. Literal "\n" sequences in the body are converted to real
  newlines.

Webhook resolution (first match wins):
  1. -w/--webhook
  2. DISCORD_WEBHOOK_URL environment variable
  3. 1Password CLI ("op"), item named "Discord Webhook URL", password field

  If none of these resolve, either export DISCORD_WEBHOOK_URL or store the
  webhook URL in 1Password as an item named "Discord Webhook URL".

Safety:
  - The resolved webhook URL must point at discord.com, discordapp.com,
    ptb.discord.com, or canary.discord.com; anything else is rejected
    before any request is made.
  - Mentions are always suppressed (allowed_mentions.parse is empty), so
    "@everyone" / "@here" in a message body never actually pings anyone.
  - Failed sends are never retried automatically, to avoid duplicate
    notifications going out.
  - Long values are clipped to Discord's limits (title 256, footer 2048,
    description 4000), and the description is shrunk further when needed so
    the whole embed stays under Discord's 6000-character total.

Exit codes:
  0  sent successfully (or --dry-run printed the payload)
  1  usage error: bad arguments, missing/invalid webhook, unknown color,
     non-Discord webhook host, missing jq/curl, or an empty message
  3  rate limited by Discord (HTTP 429) — do not retry
  4  Discord rejected the request (other 4xx)
  5  could not reach Discord (5xx response, or a network failure)

Environment:
  DISCORD_WEBHOOK_URL       Discord webhook URL (see Webhook resolution).
  TRACE=1                   Enable bash xtrace for debugging.

Examples:
  discord-notify.sh -t "Build done" -c green "all 42 tests passed"
  discord-notify.sh -p "hello @everyone"
  echo "deploy finished" | discord-notify.sh -t Deploy -f "prod / us-east-1"
  discord-notify.sh -n -t "Preview" "check the payload before sending"
EOF
}

die() {
    echo "$PROGNAME: $*" >&2
    exit 1
}

# Like die(), but with a caller-chosen exit code (used for the Discord
# HTTP-status outcomes documented under "Exit codes" above).
die_code() {
    local code="$1"
    shift
    echo "$PROGNAME: $*" >&2
    exit "$code"
}

resolve_color() {
    local input="$1"
    case "${input,,}" in
        green)    echo 5763719  ;;
        red)      echo 15548997 ;;
        blue)     echo 3447003  ;;
        yellow)   echo 16776960 ;;
        orange)   echo 16744448 ;;
        gray|grey) echo 9807270 ;;
        '#'*)     echo $((16#${input#\#})) ;;
        *[!0-9]*) die "unknown color: $input" ;;
        *)        echo "$input" ;;
    esac
}

# Convert literal backslash-n sequences into real newlines.
normalize() { printf '%s' "${1//$'\\n'/$'\n'}"; }

# clip($n) must return AT MOST $n characters: the "…" marker counts toward
# Discord's per-field limits, so slicing to $n and then appending it yields
# $n + 1 and gets the whole message rejected with HTTP 400.
readonly JQ_CLIP='def clip($n): if $n <= 0 then "" elif (length > $n) then .[0:$n-1] + "…" else . end;'

# Resolve the webhook URL: explicit argument, then env var, then 1Password.
resolve_webhook() {
    local explicit="$1"
    if [[ -n "$explicit" ]]; then
        printf '%s' "$explicit"
        return 0
    fi
    if [[ -n "${DISCORD_WEBHOOK_URL-}" ]]; then
        printf '%s' "$DISCORD_WEBHOOK_URL"
        return 0
    fi
    command -v op >/dev/null \
        || die "no webhook URL available: set DISCORD_WEBHOOK_URL, pass --webhook, or store it in 1Password as \"Discord Webhook URL\" (1Password CLI 'op' not found)"
    local url
    url="$(op item get "Discord Webhook URL" --fields label=password --reveal 2>/dev/null)" \
        || die "could not read the webhook URL from 1Password (set DISCORD_WEBHOOK_URL, pass --webhook, or run 'op signin')"
    [[ -n "$url" ]] || die "the Discord webhook URL from 1Password is empty"
    printf '%s' "$url"
}

# Reject anything that isn't a Discord webhook host. Never print the full
# URL here (it's a secret) — only the host, for diagnosis.
validate_webhook() {
    local url="$1"
    if [[ ! "$url" =~ $WEBHOOK_HOST_REGEX ]]; then
        local host="${url#*://}"
        host="${host%%/*}"
        die "refusing to POST to a non-Discord webhook URL: ${host:-<empty>}"
    fi
}

# POST the payload and translate the HTTP outcome into stdout/stderr output
# and an exit code, per the "Exit codes" section of usage(). No retries:
# resending on failure risks duplicate notifications.
send_payload() {
    local payload="$1" webhook="$2" title="$3"
    local response http_code body

    response="$(curl --silent --show-error --max-time 10 --request POST \
        --header "Content-Type: application/json" \
        --data "$payload" \
        --write-out $'\n%{http_code}' \
        "$webhook")" || true

    http_code="${response##*$'\n'}"
    body="${response%$'\n'*}"
    [[ "$http_code" =~ ^[0-9]+$ ]] || http_code=""

    if [[ "$http_code" == "200" || "$http_code" == "204" ]]; then
        if [[ -n "$title" ]]; then
            printf 'Sent to Discord. (%s)\n' "$title"
        else
            printf 'Sent to Discord.\n'
        fi
        return 0
    elif [[ "$http_code" == "429" ]]; then
        die_code 3 "rate limited by Discord (429) — do not retry, you are sending too often"
    elif [[ "$http_code" =~ ^4[0-9][0-9]$ ]]; then
        die_code 4 "Discord rejected the request (HTTP $http_code): ${body:0:500}"
    else
        die_code 5 "could not reach Discord (HTTP ${http_code})"
    fi
}

main() {
    local title="" color="" footer="" username="" webhook=""
    local plain=0 dry_run=0
    local -a words=()

    while (( $# > 0 )); do
        case "$1" in
            -t|--title)    title="${2-}";    shift 2 ;;
            -c|--color)    color="${2-}";    shift 2 ;;
            -f|--footer)   footer="${2-}";   shift 2 ;;
            -u|--username) username="${2-}"; shift 2 ;;
            -w|--webhook)  webhook="${2-}";  shift 2 ;;
            -p|--plain)    plain=1;   shift ;;
            -n|--dry-run)  dry_run=1; shift ;;
            -h|--help)     usage; exit 0 ;;
            --)            shift; words+=("$@"); break ;;
            -)             shift ;;
            -*)            die "unknown option: $1 (see --help)" ;;
            *)             words+=("$1"); shift ;;
        esac
    done

    command -v jq   >/dev/null || die "jq is required but not installed"
    command -v curl >/dev/null || die "curl is required but not installed"

    webhook="$(resolve_webhook "$webhook")"
    validate_webhook "$webhook"

    local body
    if (( ${#words[@]} > 0 )); then
        body="${words[*]}"
    elif [[ ! -t 0 ]]; then
        body="$(cat)"
    else
        body=""
    fi

    [[ -n "$body" || -n "$title" ]] || die "nothing to send (see --help)"

    # Resolved as a standalone assignment (not inline inside the jq call
    # below) so an unknown color dies cleanly here, with die()'s message
    # and exit code 1 — instead of feeding an empty --argjson to jq and
    # failing later with a confusing jq parse error.
    local color_value
    color_value="$(resolve_color "${color:-blue}")"

    local payload
    if (( plain )); then
        payload="$(jq -n \
            --arg content "$(normalize "$body")" \
            --arg username "$username" \
            --argjson max "$MAX_CONTENT" \
            "$JQ_CLIP"'
             {content: ($content | clip($max)),
              allowed_mentions: {parse: []}}
             + (if $username != "" then {username: $username} else {} end)')"
    else
        payload="$(jq -n \
            --arg title "$title" \
            --arg desc "$(normalize "$body")" \
            --arg footer "$footer" \
            --arg username "$username" \
            --argjson color "$color_value" \
            --argjson max "$MAX_DESC" \
            --argjson total "$MAX_EMBED_TOTAL" \
            "$JQ_CLIP"'
             ($title  | clip(256))  as $t
           | ($footer | clip(2048)) as $f
           | ([$max, ($total - ($t | length) - ($f | length))] | min) as $raw
           | (if $raw < 0 then 0 else $raw end) as $dmax
           | ($desc | clip($dmax)) as $d
           | {embeds: [ {color: $color}
                + (if $t != "" then {title: $t} else {} end)
                + (if $d != "" then {description: $d} else {} end)
                + (if $f != "" then {footer: {text: $f}} else {} end) ],
              allowed_mentions: {parse: []}}
             + (if $username != "" then {username: $username} else {} end)')"
    fi

    if (( dry_run )); then
        printf '%s\n' "$payload"
        return 0
    fi

    send_payload "$payload" "$webhook" "$title"
}

main "$@"
