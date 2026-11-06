# fj-readonly

A Claude Code plugin that intercepts direct read-only `fj` ([forgejo-cli](https://codeberg.org/forgejo-contrib/forgejo-cli)) calls and redirects Claude to a safe, allowlist-based wrapper instead.

## What it does

When installed, this plugin adds a **PreToolUse hook** that fires before every Bash command Claude runs. If Claude is about to call `fj` directly for a read-only operation (viewing issues, searching PRs, listing releases, etc.), the hook blocks the call and suggests using the wrapper instead:

```
Hint: `fj issue view` is a read-only command. Use `fj-readonly` instead of `fj` directly.
  Example: fj-readonly issue view 3
```

Write commands (`fj issue create`, `fj pr merge`, etc.) pass through the hook untouched and still require explicit user permission.

The allowlist lives in a single place, `bin/fj-readonly`. The hook does not keep its own copy: it runs the wrapper in dry-run mode (`FJ_READONLY_DRY_RUN=1`, exit 0 if read-only, 1 otherwise, nothing executed or printed) to decide whether a call is read-only.

The allowlist is based on forgejo-cli v0.7.0 and was derived from its help output and source code. Anything not listed below is blocked (fail closed).

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install fj-readonly@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install fj-readonly@rishubil-skills --scope project
```

## Usage

After installation, Claude automatically uses `fj-readonly` instead of `fj` for read-only operations. No extra prompting is needed — the hook fires silently on every Bash call.

To suppress the per-call permission prompt for the wrapper itself, add a rule to your `~/.claude/settings.json` (or a project-level `.claude/settings.json`):

```json
{
  "permissions": {
    "allow": [
      "Bash(fj-readonly *)"
    ]
  }
}
```

Because `bin/fj-readonly` is added to the Bash tool's `PATH` by the plugin, the command is always called simply as `fj-readonly` — no path prefix needed.

This does **not** grant access to arbitrary `fj` write commands — the wrapper enforces the read-only allowlist internally and exits 1 for any write operation.

Global options (`-H/--host`, `-C/--cwd`, `--style`, `-R/--remote`, `-r/--repo`) may appear before or between subcommands, e.g. `fj-readonly -H codeberg.org repo view owner/repo`.

> **Tip**: Run `/fewer-permission-prompts` in your Claude Code session to automatically generate a tailored allowlist based on your recent command history.

## Read-only allowlist

The wrapper allows the following `fj` subcommands:

| Group | Allowed subcommands |
|---|---|
| top-level | `whoami`, `version`, `completion` |
| `auth` | `list` |
| `repo` | `view`, `readme`, `star-status`, `watch-status`, `browse`, `labels view` |
| `issue` | `search`, `view` (incl. `body`, `comment`, `comments`, `assignees`), `templates`, `browse`, `depend list`, `block list` |
| `pr` | `search`, `view` (incl. its subcommands), `status`, `browse`, `depend list`, `block list`, `review [ID] [list]` (not `review request`) |
| `milestone` | `search`, `view` |
| `wiki` | `contents`, `view`, `browse` |
| `actions` | `tasks`, `variables list`, `secrets list` |
| `release` | `list`, `view`, `browse`, `asset download` |
| `tag` | `list`, `view` |
| `user` | `search`, `view`, `browse`, `following`, `followers`, `repos`, `orgs`, `activity`, `key list/view`, `gpg list/view` |
| `org` | `list`, `view`, `activity`, `members`, `visibility` (without `-s`/`--set`), `team list/view`, `team repo list`, `team member list`, `label list`, `repo list` |

Deliberately blocked: everything that writes or changes local state (create, edit, delete, close, comment, assign, merge, checkout, clone, fork, migrate, star, follow, block, upload, login, logout, `gpg verify`, `actions dispatch`, `wiki clone`, `pr review request`, `org visibility --set`, etc.). `repo units` is also blocked because its implementation always issues an edit request, even without `--enable`.

## Scripts

| Path | Purpose |
|---|---|
| `bin/fj-readonly` | Wrapper: runs `fj` only for allowlisted read-only subcommands; the single source of truth for the allowlist. Supports `FJ_READONLY_DRY_RUN=1`. Added to `PATH` automatically while the plugin is enabled. |
| `scripts/fj-hook.sh` | Dispatcher: tries `uv`, then `python3`, then `python` (3.x) |
| `scripts/fj-hook.py` | Hook logic: finds direct `fj` calls in each simple command, asks the wrapper (dry-run) whether they are read-only, outputs hint, exits 2 |

## Runtime requirements

The hook script (`fj-hook.py`) requires one of:

1. [`uv`](https://docs.astral.sh/uv/) (preferred)
2. `python3`
3. `python` at version 3.x

`bin/fj-readonly` requires `bash` and the `fj` CLI (forgejo-cli).
