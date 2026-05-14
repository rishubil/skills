# python-lsp-uvx-ty

Configure and use [ty](https://docs.astral.sh/ty/) — Astral's extremely fast Python type checker
and language server — as an LSP server launched via `uvx ty server`.

## What it does

Bundles a `.lsp.json` that wires `uvx ty server` into Claude Code's LSP integration, so Claude
receives real-time diagnostics, hover info, go-to-definition, and completions for Python files as
soon as the plugin is installed — no separate binary installation required.

Also provides a skill with editor-specific LSP setup instructions (VS Code, Neovim, Zed, PyCharm,
Emacs), `ty.toml` / `pyproject.toml` configuration guidance, and `ty check` CLI usage.

## Scripts

| File | Purpose |
| --- | --- |
| `.lsp.json` | Registers `uvx ty server` as the LSP server for `.py` and `.pyi` files |

## Installation

```
/plugin install python-lsp-uvx-ty@rishubil-skills
```

## Usage

After installing the plugin, ask Claude to:

- Set up ty as the LSP server in your editor configuration
- Create or update `ty.toml` / `pyproject.toml` type-checking rules
- Run `uvx ty check` with the right flags for your CI or local workflow
- Explain ty language server initialization and settings options

## Source

- [ty documentation](https://docs.astral.sh/ty/)
- [ty editor setup](https://docs.astral.sh/ty/editors/)
- [ty CLI reference](https://docs.astral.sh/ty/reference/cli/)
- [ty editor settings reference](https://docs.astral.sh/ty/reference/editor-settings/)
