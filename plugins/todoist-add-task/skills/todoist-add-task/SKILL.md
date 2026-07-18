---
name: todoist-add-task
description: >
  Capture spoken or typed to-dos and add them to Todoist through the Todoist
  API. Use this whenever the user dictates or asks to jot down a task,
  reminder, or to-do for Todoist — including rambling voice input that needs
  to be distilled into concise task text. Each task defaults to the Inbox with
  a due date of today, and any other field the API supports (date, time,
  priority, project, section, labels, description, deadline, duration) can be
  set when the user mentions it. Trigger even when the user doesn't say
  "Todoist" explicitly but clearly wants to record something to do.
---

# Add tasks to Todoist

This skill turns what the user says — often loose, spoken-aloud phrasing — into
clean Todoist tasks and creates them via the API. It is built for fast voice
capture: the user rambles, you distill the actual task, confirm it, and file it.

## Prerequisites

- A Todoist API token. The script reads it from the `TODOIST_API_TOKEN`
  environment variable when set; otherwise it falls back to the 1Password CLI
  (`op item get "Todoist API token"`, field: password). Either way the bundled
  script resolves the token — you never pass it yourself.
- `curl` and `jq` are available.

If `TODOIST_API_TOKEN` is unset and `op` is not signed in, the script fails with
a clear message; tell the user to export `TODOIST_API_TOKEN` or run `op signin`
(or `eval $(op signin)`) and retry.

## The script

Everything goes through the bundled script:

```
<path-to-this-skill>/scripts/todoist-add.sh
```

Run `<path-to-this-skill>/scripts/todoist-add.sh --help` to see every option.
Key points:

- **Defaults**: with no options, the task lands in the **Inbox** with a due
  date of **today**. This is the common case, so keep invocations minimal.
- **Content is positional**: the first non-option argument is the task text.
- Add options only for the fields the user actually specified.

### Options you will use most

| Need | Option | Notes |
| --- | --- | --- |
| Due date/time (natural language) | `--due-string "tomorrow at 15:00"` | Parsed by Todoist. Default is `"today"`. English by default (`--due-lang`). |
| No due date | `--no-due` | Use when the user says someday / no date. |
| Priority | `--priority 1` | Todoist p-levels: **1 = p1 (highest)** … 4 = lowest. |
| Description / note | `--description "..."` | Extra detail beyond the title. |
| Different project | `--project-id <id>` | Resolve a project name with `--list-projects` first. |
| Section | `--section-id <id>` | List with `--list-sections <project_id>`. |
| Labels | `--label work --label urgent` | Repeatable. Labels must already exist — unknown ones are rejected, not created (see `--list-labels`). |
| Deadline (≠ due date) | `--deadline-date 2026-07-25` | Todoist's separate "deadline" field. |
| Subtask | `--parent-id <id>` | Makes the task a child of another. |
| Duration | `--duration 30 --duration-unit minute` | |

The full list is in `--help`; the script supports every field the create-task
API accepts.

### Dates: prefer natural language

Pass the user's date/time as `--due-string` in plain English ("today",
"tomorrow", "next monday", "friday at 9am", "jul 25"). Todoist parses it in the
user's own timezone, which is more reliable than computing a date yourself. Use
`--due-date` / `--due-datetime` only when you already have an exact
`YYYY-MM-DD` / RFC3339 value.

**Due date is not the same as a deadline.** "do it / schedule it on this date"
→ the due date (`--due-string`). "must be finished by this date" →
`--deadline-date`.

### Labels and projects are never created

The script references projects and sections by **id** (resolve names with
`--list-projects` / `--list-sections`) and never creates them. Labels are
passed by name, but any label that does not already exist is **rejected** rather
than auto-created — run `todoist-add.sh --list-labels` to see the user's
existing labels, and only pass ones that are on that list. If the user asks for
a label that doesn't exist, tell them instead of silently making a new one.

## Workflow

1. **Distill the task.** Strip filler (the spoken "um", "uh", "I need to...")
   and turn the user's speech into a short imperative task title. Keep the title
   in the same language the user spoke. If the user rattled off several things,
   split them into separate tasks.

2. **Map the details.** Default to Inbox + today. Override only what the user
   stated:
   - A time/date they mention → `--due-string`.
   - Urgency cues ("urgent", "important", "ASAP") → `--priority` (1 or 2, use
     judgment).
   - A named project → run `--list-projects`, match the name, pass
     `--project-id`.
   - Description, deadline, duration → the matching options.
   - Labels → only if they already exist; check with `--list-labels` and pass
     `--label <name>`. Don't invent new labels.

3. **Confirm before adding.** Show the user what you are about to create — the
   task title, the due date, and any non-default fields (project, priority,
   etc.) — in a short summary, and get a quick confirmation. Write the summary
   in the user's language. For multiple tasks, list them all. This catches
   misheard content before it lands in Todoist. You can use `--dry-run` to
   preview the exact JSON payload if you want to double-check field mapping, but
   the user-facing confirmation should be plain language, not JSON.

4. **Create it.** Run the script once per task. On success it prints the task
   title and a link. Report back concisely in the user's language (e.g. "Added
   'Buy milk' to your Inbox, due today."), including the link. On failure, relay
   the error (e.g. an auth / `op signin` issue) instead of silently continuing.

## Examples

The user speaks in their own language; the task title stays in that language,
while the command and its options are always the same. The examples below use
English task text for readability.

**Example 1 — plain capture (defaults):**
User: "uh, not tomorrow, today — add buying milk to my to-dos"
→ confirm "I'll add 'Buy milk' to your Inbox for today" →
`todoist-add.sh "Buy milk"` (Inbox + today are the defaults)

**Example 2 — date + priority:**
User: "book a doctor's appointment friday at 3pm, this one's kind of important"
→ confirm →
`todoist-add.sh "Book doctor's appointment" --due-string "friday at 15:00" --priority 2`

**Example 3 — multiple tasks into a project:**
User: "put two things in my Work project: write up the meeting notes and check the deploy script"
→ `--list-projects` to find the "Work" project id → confirm both →
`todoist-add.sh "Write up meeting notes" --project-id <id>` and
`todoist-add.sh "Check the deploy script" --project-id <id>`
