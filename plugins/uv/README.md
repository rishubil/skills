# uv

A Claude Code plugin that enforces uv-based Python workflow by intercepting direct `python`, `pip`, and `uv pip install` invocations before they run.

## What it does

When installed, this plugin adds a **PreToolUse hook** that fires before every Bash command Claude runs. It blocks two common anti-patterns and suggests the correct uv equivalent:

**Direct python/pip calls:**
```
Hint: direct python/pip detected. Use `uv run python`, `uv run pip`, etc. instead —
  this project requires all Python commands to go through uv.
```

**`uv run pip install` or `uv pip install`:**
```
Hint: `uv run pip install` detected. Use `uv add` instead —
  this project manages dependencies through uv, not pip.
  Suggested command: uv add requests
```

Commands already using `uv run` pass through the hook untouched.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install uv@rishubil-skills
```

## Usage

After installation, Claude automatically avoids direct `python`/`pip` calls and uses `uv run` / `uv add` instead. No extra prompting is needed — the hook fires silently on every Bash call.

The plugin also activates the **uv skill**, which provides Claude with guidance on the correct uv workflow for script execution, dependency management, and tool invocation.

## Scripts

| Path | Purpose |
|---|---|
| `scripts/uv-hook.sh` | Dispatcher: tries `uv`, then `python3`, then `python` (3.x) |
| `scripts/uv-hook.py` | Hook logic: detects anti-patterns, outputs hint, exits 2 |

## Runtime requirements

The hook script (`uv-hook.py`) requires one of:

1. [`uv`](https://docs.astral.sh/uv/) (preferred)
2. `python3`
3. `python` at version 3.x

## Source

Hook logic based on [mitsuhiko/agent-stuff](https://github.com/mitsuhiko/agent-stuff/tree/main/skills/uv).
