# python-lsp-uvx-ty

A Claude Code LSP plugin that registers [ty](https://docs.astral.sh/ty/) as a Python language server via `uvx ty server`.

## What it does

When installed, this plugin provides real-time code intelligence for `.py` and `.pyi` files by wiring `uvx ty server` into Claude Code's LSP integration:

- **Instant diagnostics**: type errors and warnings appear immediately after each edit
- **Code navigation**: go to definition, find references, hover documentation
- **Completions**: auto-import and symbol suggestions

No separate binary installation is required — `uvx` fetches and runs `ty` on demand.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install python-lsp-uvx-ty@rishubil-skills
```

## Usage

After installation, Claude Code automatically starts `uvx ty server` when you open a Python file. No extra configuration is needed.

## Scripts

| Path | Purpose |
|---|---|
| `.lsp.json` | Registers `uvx ty server` as the LSP server for `.py` and `.pyi` files |

## Runtime requirements

- [`uv`](https://docs.astral.sh/uv/) must be installed and available in `PATH`
