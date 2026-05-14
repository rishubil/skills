---
name: python-lsp-uvx-ty
description: >
  Specialist skill for configuring and using the ty Python type checker as an LSP server via uvx.
  Use when setting up ty as an LSP in an editor (VS Code, Neovim, Zed, PyCharm, Emacs, etc.),
  writing ty.toml / pyproject.toml configuration, or diagnosing type errors with ty check.
---

# python-lsp-uvx-ty — ty Language Server via uvx

[ty](https://docs.astral.sh/ty/) is an extremely fast Python type checker and language server
written in Rust by Astral (the team behind uv and Ruff). Launch it with `uvx` so no installation
is required.

## Starting the Language Server

```json
{
  "ty": {
    "command": "uvx",
    "args": ["ty", "server"],
    "extensionToLanguage": {
      ".py": "python",
      ".pyi": "python"
    }
  }
}
```

The LSP server is started with `uvx ty server`. No arguments are needed beyond `server`.

## Editor Configuration

### VS Code

Install the official **ty** extension from the VS Code marketplace. It starts the server
automatically and respects the settings below in `settings.json`:

```json
{
  "ty.diagnosticMode": "workspace",
  "ty.inlayHints.variableTypes": true,
  "ty.inlayHints.callArgumentNames": true,
  "ty.completions.autoImport": true
}
```

To use `uvx` instead of a local binary, set:

```json
{
  "ty.importStrategy": "fromEnvironment"
}
```

### Neovim

**nvim-lspconfig** (0.11+):

```lua
vim.lsp.enable('ty')
```

Earlier versions:

```lua
require('lspconfig').ty.setup({})
```

To override the command and use `uvx`:

```lua
require('lspconfig').ty.setup({
  cmd = { "uvx", "ty", "server" },
})
```

### Zed

In `settings.json`:

```json
{
  "languages": {
    "Python": {
      "language_servers": ["ty", "!pyright"]
    }
  }
}
```

### Emacs (Eglot)

```elisp
(add-to-list 'eglot-server-programs
             '(python-mode . ("uvx" "ty" "server")))
```

### PyCharm

Available from version 2025.3 via **Settings → Python → Tools → ty**.
Choose execution mode (Interpreter or Path).

### Generic LSP Client

Point any LSP client at `uvx ty server`. No additional arguments are required.

## Project Configuration

### ty.toml

```toml
[rules]
# "error" | "warn" | "info" | "ignore"
division-by-zero = "error"
index-out-of-bounds = "error"

[environment]
python-version = "3.12"
```

### pyproject.toml

```toml
[tool.ty.rules]
division-by-zero = "error"
index-out-of-bounds = "error"

[tool.ty.environment]
python-version = "3.12"
```

### Precedence (highest → lowest)

1. CLI flags
2. Project-level `ty.toml` or `pyproject.toml [tool.ty]`
3. User-level `~/.config/ty/ty.toml`

## Running the Type Checker

```bash
# Check the current project
uvx ty check

# Watch mode — recheck on file changes
uvx ty check --watch

# Target a specific Python version
uvx ty check --python-version 3.12

# Output formats: full | concise | github | gitlab | junit
uvx ty check --output-format github

# Adjust rule severity inline
uvx ty check --error division-by-zero --ignore index-out-of-bounds

# Auto-fix issues where possible
uvx ty check --fix
```

## Language Server Initialization Options

These options can be passed as `initializationOptions` in the LSP handshake:

| Option | Type | Default | Description |
|---|---|---|---|
| `logLevel` | string | `"info"` | `"trace"` / `"debug"` / `"info"` / `"warn"` / `"error"` |
| `logFile` | string | null | Path for server log output |
| `configuration` | object | null | Inline settings that override config files |
| `configurationFile` | string | null | Path to a `ty.toml` file |

## Language Server Settings

| Setting | Type | Default | Description |
|---|---|---|---|
| `disableLanguageServices` | boolean | `false` | Turn off completion, hover, go-to-definition |
| `diagnosticMode` | string | `"openFilesOnly"` | `"off"` / `"openFilesOnly"` / `"workspace"` |
| `showSyntaxErrors` | boolean | `true` | Show syntax error diagnostics |
| `inlayHints.variableTypes` | boolean | `true` | Inline variable type hints |
| `inlayHints.callArgumentNames` | boolean | `true` | Inline argument name hints |
| `completions.autoImport` | boolean | `true` | Include unimported symbols in completions |
