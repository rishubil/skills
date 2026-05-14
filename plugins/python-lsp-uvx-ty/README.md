# python-lsp-uvx-ty

Configure and use [ty](https://docs.astral.sh/ty/) — Astral's extremely fast Python type checker
and language server — as an LSP server launched via `uvx ty server`.

## What it does

Provides editor-specific LSP setup instructions, `ty.toml` / `pyproject.toml` configuration
guidance, and `ty check` CLI usage for projects that run ty through `uvx` (no local installation
required).

Supported editors: VS Code, Neovim, Zed, PyCharm, Emacs (Eglot), and any generic LSP client.

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
