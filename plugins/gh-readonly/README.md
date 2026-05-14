# gh-readonly

A Claude Code plugin that intercepts direct read-only `gh` CLI calls and
redirects Claude to a safe, allowlist-based wrapper script instead.

## What it does

When installed, this plugin adds a **PreToolUse hook** that fires before
every Bash command Claude runs. If Claude is about to call `gh` directly
for a read-only operation (listing issues, viewing PRs, checking CI, etc.),
the hook blocks the call and suggests using the wrapper instead:

```
Hint: `gh issue` is a read-only command. Use `/path/to/gh-readonly.sh` instead of `gh` directly.
  Example: /path/to/gh-readonly.sh issue list
```

Write commands (`gh issue create`, `gh pr merge`, etc.) pass through the
hook untouched and still require explicit user permission.

## Scripts

| Script | Purpose |
|---|---|
| `scripts/gh-hook.sh` | Dispatcher: tries `uv`, then `python3`, then `python` (3.x) |
| `scripts/gh-hook.py` | Hook logic: detects read-only `gh` calls, outputs hint, exits 2 |
| `scripts/gh-readonly.sh` | Wrapper: runs `gh` only for allowlisted read-only subcommands |

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install gh-readonly@rishubil-skills
```

## Recommended: allow `gh-readonly.sh` in settings.json

After installation, Claude will still be prompted for permission each time
it calls `gh-readonly.sh`. To pre-approve the wrapper and suppress these
prompts, add a permission rule to your `~/.claude/settings.json` (or a
project-level `.claude/settings.json`):

```json
{
  "permissions": {
    "allow": [
      "Bash(*/gh-readonly.sh*)"
    ]
  }
}
```

The glob `*/gh-readonly.sh*` matches the wrapper at its installed path
(e.g. `~/.claude/plugins/gh-readonly@rishubil-skills/scripts/gh-readonly.sh`)
followed by any arguments. This does **not** grant access to arbitrary `gh`
write commands — the wrapper enforces the read-only allowlist internally and
exits 1 for any write operation.

> **Tip**: Run `/fewer-permission-prompts` in your Claude Code session to
> automatically generate a tailored allowlist based on your recent command
> history.

## Read-only allowlist

The wrapper allows the following `gh` subcommands:

| Group | Allowed subcommands |
|---|---|
| `issue` | `list`, `status`, `view` |
| `pr` | `list`, `status`, `checks`, `diff`, `view` |
| `run` | `list`, `view`, `watch`, `download` |
| `workflow` | `list`, `view` |
| `repo` | `list`, `view`, `gitignore list/view`, `license list/view`, `deploy-key list` |
| `release` | `list`, `view`, `download` |
| `search` | `code`, `commits`, `issues`, `prs`, `repos` |
| `api` | GET requests only (no `-X POST/PUT/PATCH/DELETE`) |
| `auth` | `status`, `token` |
| `gist` | `list`, `view` |
| `project` | `list`, `view`, `field-list`, `item-list` |
| `cache` | `list` |
| `label` | `list` |
| `secret` | `list` |
| `variable` | `get`, `list` |
| `ruleset` | `check`, `list`, `view` |
| `extension` | `list`, `search` |
| top-level | `status`, `completion`, `browse` |

## Runtime requirements

The hook script (`gh-hook.py`) requires one of:

1. [`uv`](https://docs.astral.sh/uv/) (preferred)
2. `python3`
3. `python` at version 3.x

`gh-readonly.sh` requires `bash` and the `gh` CLI.
