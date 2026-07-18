# todoist-add-task

A Claude Code plugin that captures spoken or typed to-dos and adds them to Todoist through the Todoist API.

## What it does

When triggered, this skill:

1. **Distills** the user's (often rambling, spoken-aloud) input into a short, clean task title
2. **Maps** any details the user mentioned — date/time, priority, project, section, labels, description, deadline, duration — onto the matching Todoist API fields
3. **Confirms** the task (and its due date/non-default fields) with the user before creating anything
4. **Creates** the task via the bundled `todoist-add.sh` script, which defaults to the **Inbox** with a due date of **today** unless told otherwise
5. **Reports back** the created task with a link, or relays the error (e.g. a 1Password auth issue) if creation failed

Authentication is handled transparently: the script reads the Todoist API token
from the 1Password CLI (`op`), so no token ever needs to be typed or pasted.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install todoist-add-task@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install todoist-add-task@rishubil-skills --scope project
```

## Usage

Trigger phrases include (spoken or typed, in any language):

- "Add buying milk to my to-do list"
- "Remind me to book a doctor's appointment friday at 3pm on Todoist"
- "Add 'review the PR' to Todoist for tomorrow, high priority"
- "Jot this down as a task for today"

Just say or type the task — including messy, unstructured voice input — and
the skill will distill it, confirm the details, and add it to Todoist.

## Scripts

| Path | Purpose |
|---|---|
| `scripts/todoist-add.sh` | Adds a task to Todoist via `curl` + `jq` against the REST API. Reads the API token from the `TODOIST_API_TOKEN` environment variable if set, otherwise from 1Password (`op item get "Todoist API token" --fields label=password --reveal`) — never accepts the token as an argument. Defaults to the Inbox with a due date of today; every other create-task field (due date/time, deadline, project, section, parent, order, priority, labels, assignee, duration) is available as an option. Supports `--list-projects` / `--list-sections` / `--list-labels` for id/name lookup and `--dry-run` for previewing the JSON payload without contacting the API. Projects and sections are referenced by id and are never created; labels must already exist — unknown labels are rejected, never auto-created. Requires `curl`, `jq`, and either a `TODOIST_API_TOKEN` environment variable or a signed-in 1Password CLI (`op`). |
