# uv

A Claude Code plugin that enforces uv for all Python use: direct `python`, `pip`, and `uv pip install` invocations are blocked before they run.

## What it does

While installed, this plugin adds a **PreToolUse hook** that fires before every Bash command Claude runs. It applies in **every directory**, not only in uv-managed projects: all Python must go through uv. The hook blocks the command and prints the uv equivalent.

**Direct python:**
```
Hint: direct python detected. The uv plugin is enabled, so all Python must go through uv in every directory.
  Use `uv run python ...` (or `uv run --no-project python ...` for a standalone script inside a project), or `uvx <tool>` for tools.
```

**Direct pip (including `python -m pip`):**
```
Hint: direct pip detected. The uv plugin is enabled, so all Python must go through uv in every directory.
  Inside a uv project use `uv add <pkgs>`; outside one use `uv run --with <pkgs> ...`, inline script metadata, or `uvx <tool>`.
  Suggested command: uv add requests
```

**`uv run pip install` or `uv pip install`:**
```
Hint: `uv pip install` detected. The uv plugin is enabled, so all Python must go through uv in every directory.
  Inside a uv project use `uv add <pkgs>`; outside one use `uv run --with <pkgs> ...`, inline script metadata, or `uvx <tool>`.
  Suggested command: uv add requests
```

Python that is the argument of `uv run`, `uvx`, or `uv tool run` passes through.

### What is detected

Every command position in the Bash command is judged independently, so `uv run a.py && python3 b.py` is still blocked. Detected:

- **Names and paths:** `python`, `python3`, `python3.12`, `pythonw`, `pip`, `pip3`, `pip3.12`, and any path ending in those (`/usr/bin/python3`, `.venv/bin/python`).
- **Compound commands:** after `&&`, `||`, `;`, `|`, newlines, `(`, `$(`, backticks, `!`, `{`, and `then`/`do`/`else`.
- **Prefixes and wrappers:** `VAR=value`, `sudo`, `env`, `exec`, `time`, `nohup`, `nice`, `timeout <dur>`, `xargs`, `command`.
- **Nested shells:** `bash -c '...'`, `sh -c "..."`, `eval`, and heredocs fed to a shell (`bash <<EOF`).

Not matched: words that merely mention Python (`grep python file`, `brew info python`, `cat scripts/python3-notes.txt`), `pipx`, `pipenv`, and heredoc bodies that are plain data (`git commit -F - <<EOF`).

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install uv@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install uv@rishubil-skills --scope project
```

## Usage

After installation, Claude automatically avoids direct `python`/`pip` calls and uses `uv run` / `uv add` / `uv run --with` / `uvx` instead. No extra prompting is needed — the hook fires silently on every Bash call.

The plugin also activates the **uv skill**, which provides Claude with guidance on the correct uv workflow for script execution, dependency management, and tool invocation.

### Limitations

The hook inspects only the Bash command text. A script run through its own shebang (`./tool.py` with `#!/usr/bin/env python3`) or Python launched indirectly by another program is not caught.

## Scripts

| Path | Purpose |
|---|---|
| `scripts/uv-hook.sh` | Dispatcher: tries `uv`, then `python3`, then `python` (3.x) |
| `scripts/uv-hook.py` | Hook logic: tokenizes the command, detects direct Python/pip, outputs hint, exits 2 |

## Runtime requirements

The hook script (`uv-hook.py`) requires one of:

1. [`uv`](https://docs.astral.sh/uv/) (preferred)
2. `python3`
3. `python` at version 3.x

## Source

Hook logic based on [mitsuhiko/agent-stuff](https://github.com/mitsuhiko/agent-stuff/tree/main/skills/uv).
