#!/usr/bin/env bash
#
# todoist-add.sh — Add a task to Todoist via the REST API.
#
# Defaults: the task goes to the Inbox with a due date of "today".
# Every other Todoist create-task field is exposed as an option so the
# caller can set whatever the API supports.
#
# Auth: the API token is read from 1Password:
#   op item get "Todoist API token" --fields label=password --reveal
#
# Requires: bash, curl, jq, and the 1Password CLI (op), signed in.

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

API_BASE="https://api.todoist.com/api/v1"

usage() {
    cat <<'EOF'
Usage:
  todoist-add.sh "Task content" [options]
  todoist-add.sh --list-projects
  todoist-add.sh --list-sections <project_id>

Add a task to Todoist. By default the task lands in the Inbox with a due
date of today. Pass options to override any field the Todoist API supports.

Content:
  <content>                 Task text (required unless a --list-* mode is used).
  --description <text>      Longer note / description for the task.

Scheduling (choose at most one "due" form; default is --due-string "today"):
  --due-string <text>       Natural-language due date, e.g. "today",
                            "tomorrow at 15:00", "next monday". Parsed by Todoist.
  --due-date <YYYY-MM-DD>   Fixed all-day due date.
  --due-datetime <RFC3339>  Fixed due date and time, e.g. 2026-07-20T15:00:00Z.
  --due-lang <code>         Language for parsing --due-string (default: en).
  --no-due                  Create the task with no due date at all.

Deadline (distinct from the due date):
  --deadline-date <YYYY-MM-DD>  Deadline date.
  --deadline-lang <code>        Language for the deadline (default: en).

Placement:
  --project-id <id>         Target project (default: Inbox). See --list-projects.
  --section-id <id>         Target section within the project.
  --parent-id <id>          Make this a subtask of the given task id.
  --order <int>             Explicit ordering position.

Attributes:
  --priority <1-4>          Todoist UI priority: 1 = p1 (highest) .. 4 = p4 (lowest).
  --label <name>            Add an EXISTING label by name (repeatable). Unknown
                            labels are rejected, never auto-created. See --list-labels.
  --assignee-id <id>        Assign to a collaborator (shared projects).
  --duration <int>          Amount of time the task will take.
  --duration-unit <unit>    "minute" or "day" (required with --duration).

Modes:
  --list-projects           Print "id<TAB>name" for every project, then exit.
  --list-sections <proj>    Print "id<TAB>name" for the project's sections, then exit.
  --list-labels             Print "id<TAB>name" for every existing label, then exit.
  --dry-run                 Print the JSON payload instead of sending it.
  -h, --help                Show this help.

Environment:
  TRACE=1                   Enable bash xtrace for debugging.
EOF
}

err() { echo "todoist-add: $*" >&2; }
die() { err "$*"; exit 1; }

# ---- argument parsing -------------------------------------------------------
CONTENT=""
DESCRIPTION=""
DUE_STRING=""
DUE_DATE=""
DUE_DATETIME=""
DUE_LANG="en"
NO_DUE=0
DEADLINE_DATE=""
DEADLINE_LANG="en"
PROJECT_ID=""
SECTION_ID=""
PARENT_ID=""
ORDER=""
PRIORITY=""
ASSIGNEE_ID=""
DURATION=""
DURATION_UNIT=""
LABELS=()
MODE="add"
LIST_SECTIONS_PROJECT=""
DRY_RUN=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help|help|-help) usage; exit 0 ;;
        --description)   DESCRIPTION="${2-}"; shift 2 ;;
        --due-string)    DUE_STRING="${2-}"; shift 2 ;;
        --due-date)      DUE_DATE="${2-}"; shift 2 ;;
        --due-datetime)  DUE_DATETIME="${2-}"; shift 2 ;;
        --due-lang)      DUE_LANG="${2-}"; shift 2 ;;
        --no-due)        NO_DUE=1; shift ;;
        --deadline-date) DEADLINE_DATE="${2-}"; shift 2 ;;
        --deadline-lang) DEADLINE_LANG="${2-}"; shift 2 ;;
        --project-id)    PROJECT_ID="${2-}"; shift 2 ;;
        --section-id)    SECTION_ID="${2-}"; shift 2 ;;
        --parent-id)     PARENT_ID="${2-}"; shift 2 ;;
        --order)         ORDER="${2-}"; shift 2 ;;
        --priority)      PRIORITY="${2-}"; shift 2 ;;
        --label)         LABELS+=("${2-}"); shift 2 ;;
        --assignee-id)   ASSIGNEE_ID="${2-}"; shift 2 ;;
        --duration)      DURATION="${2-}"; shift 2 ;;
        --duration-unit) DURATION_UNIT="${2-}"; shift 2 ;;
        --list-projects) MODE="list-projects"; shift ;;
        --list-sections) MODE="list-sections"; LIST_SECTIONS_PROJECT="${2-}"; shift 2 ;;
        --list-labels)   MODE="list-labels"; shift ;;
        --dry-run)       DRY_RUN=1; shift ;;
        --) shift; if [[ -n "${1-}" ]]; then CONTENT="$1"; shift; fi; break ;;
        -*) die "unknown option: $1" ;;
        *)  if [[ -z "$CONTENT" ]]; then CONTENT="$1"; shift; else die "unexpected argument: $1"; fi ;;
    esac
done

command -v curl >/dev/null || die "curl is required but not installed"
command -v jq   >/dev/null || die "jq is required but not installed"

# ---- token ------------------------------------------------------------------
get_token() {
    # Prefer an explicit environment variable; fall back to 1Password.
    if [[ -n "${TODOIST_API_TOKEN-}" ]]; then
        printf '%s' "$TODOIST_API_TOKEN"
        return 0
    fi
    command -v op >/dev/null \
        || die "no TODOIST_API_TOKEN set, and the 1Password CLI (op) is not installed"
    local token
    token="$(op item get "Todoist API token" --fields label=password --reveal 2>/dev/null)" \
        || die "could not read the Todoist token (set TODOIST_API_TOKEN, or run 'op signin')"
    [[ -n "$token" ]] || die "the Todoist API token from 1Password is empty"
    printf '%s' "$token"
}

# ---- list modes -------------------------------------------------------------
if [[ "$MODE" == "list-projects" ]]; then
    TOKEN="$(get_token)"
    if ! out="$(curl -fsS "$API_BASE/projects" -H "Authorization: Bearer $TOKEN")"; then
        die "failed to fetch projects from Todoist"
    fi
    printf '%s' "$out" | jq -r '(.results // .)[] | "\(.id)\t\(.name)"'
    exit 0
fi

if [[ "$MODE" == "list-sections" ]]; then
    [[ -n "$LIST_SECTIONS_PROJECT" ]] || die "--list-sections requires a project id"
    TOKEN="$(get_token)"
    if ! out="$(curl -fsS "$API_BASE/sections?project_id=$LIST_SECTIONS_PROJECT" -H "Authorization: Bearer $TOKEN")"; then
        die "failed to fetch sections from Todoist"
    fi
    printf '%s' "$out" | jq -r '(.results // .)[] | "\(.id)\t\(.name)"'
    exit 0
fi

if [[ "$MODE" == "list-labels" ]]; then
    TOKEN="$(get_token)"
    if ! out="$(curl -fsS "$API_BASE/labels" -H "Authorization: Bearer $TOKEN")"; then
        die "failed to fetch labels from Todoist"
    fi
    printf '%s' "$out" | jq -r '(.results // .)[] | "\(.id)\t\(.name)"'
    exit 0
fi

# ---- validate add -----------------------------------------------------------
[[ -n "$CONTENT" ]] || die "task content is required (see --help)"

# At most one due specifier.
due_forms=0
[[ -n "$DUE_STRING" ]]   && due_forms=$((due_forms + 1))
[[ -n "$DUE_DATE" ]]     && due_forms=$((due_forms + 1))
[[ -n "$DUE_DATETIME" ]] && due_forms=$((due_forms + 1))
[[ "$due_forms" -le 1 ]] || die "use only one of --due-string / --due-date / --due-datetime"
if [[ "$NO_DUE" -eq 1 && "$due_forms" -gt 0 ]]; then
    die "--no-due cannot be combined with a due date"
fi

# Default: due today, unless the caller asked for no due date or set one.
if [[ "$NO_DUE" -eq 0 && "$due_forms" -eq 0 ]]; then
    DUE_STRING="today"
fi

# Priority: accept Todoist UI levels p1..p4 (1 = highest) and map to the API
# scale where 4 = highest.
API_PRIORITY=""
if [[ -n "$PRIORITY" ]]; then
    [[ "$PRIORITY" =~ ^[1-4]$ ]] || die "--priority must be 1-4 (1 = p1, highest)"
    API_PRIORITY=$((5 - PRIORITY))
fi

if [[ -n "$DURATION" && -z "$DURATION_UNIT" ]]; then
    die "--duration requires --duration-unit (minute or day)"
fi

# ---- build payload ----------------------------------------------------------
jq_args=(--arg content "$CONTENT")
filter='{content:$content}'

add_str()  { jq_args+=(--arg "$1" "$2"); filter+=" + {$1:\$$1}"; }
add_json() { jq_args+=(--argjson "$1" "$2"); filter+=" + {$1:\$$1}"; }

[[ -n "$DESCRIPTION" ]]   && add_str  description "$DESCRIPTION"
if [[ -n "$DUE_STRING" ]]; then add_str due_string "$DUE_STRING"; add_str due_lang "$DUE_LANG"; fi
[[ -n "$DUE_DATE" ]]      && add_str  due_date "$DUE_DATE"
[[ -n "$DUE_DATETIME" ]]  && add_str  due_datetime "$DUE_DATETIME"
if [[ -n "$DEADLINE_DATE" ]]; then add_str deadline_date "$DEADLINE_DATE"; add_str deadline_lang "$DEADLINE_LANG"; fi
[[ -n "$PROJECT_ID" ]]    && add_str  project_id "$PROJECT_ID"
[[ -n "$SECTION_ID" ]]    && add_str  section_id "$SECTION_ID"
[[ -n "$PARENT_ID" ]]     && add_str  parent_id "$PARENT_ID"
[[ -n "$ORDER" ]]         && add_json order "$ORDER"
[[ -n "$API_PRIORITY" ]]  && add_json priority "$API_PRIORITY"
[[ -n "$ASSIGNEE_ID" ]]   && add_str  assignee_id "$ASSIGNEE_ID"
if [[ -n "$DURATION" ]]; then add_json duration "$DURATION"; add_str duration_unit "$DURATION_UNIT"; fi

if [[ "${#LABELS[@]}" -gt 0 ]]; then
    labels_json="$(printf '%s\n' "${LABELS[@]}" | jq -R . | jq -s .)"
    add_json labels "$labels_json"
fi

payload="$(jq -n "${jq_args[@]}" "$filter")"

if [[ "$DRY_RUN" -eq 1 ]]; then
    printf '%s\n' "$payload"
    exit 0
fi

# ---- send -------------------------------------------------------------------
TOKEN="$(get_token)"

# Refuse to auto-create labels: every requested label must already exist.
if [[ "${#LABELS[@]}" -gt 0 ]]; then
    if ! existing_labels="$(curl -fsS "$API_BASE/labels" -H "Authorization: Bearer $TOKEN")"; then
        die "failed to fetch labels from Todoist for validation"
    fi
    for label in "${LABELS[@]}"; do
        if ! printf '%s' "$existing_labels" | jq -e --arg n "$label" '[(.results // .)[].name] | index($n)' >/dev/null; then
            die "label '$label' does not exist in your Todoist; refusing to auto-create it (run with --list-labels to see existing labels)"
        fi
    done
fi

if ! response="$(curl -sS -w $'\n%{http_code}' -X POST "$API_BASE/tasks" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    --data "$payload")"; then
    die "failed to reach the Todoist API"
fi

http_code="${response##*$'\n'}"
body="${response%$'\n'*}"

if [[ "$http_code" == 2* ]]; then
    task_id="$(printf '%s' "$body" | jq -r '.id // empty')"
    printf 'Added: %s\n' "$CONTENT"
    [[ -n "$task_id" ]] && printf '  https://app.todoist.com/app/task/%s\n' "$task_id"
    exit 0
fi

err "Todoist API returned HTTP $http_code"
printf '%s\n' "$body" >&2
exit 1
