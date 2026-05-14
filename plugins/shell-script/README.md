# shell-script

A Claude Code plugin that applies best practices and error handling patterns when writing Bash shell scripts.

## What it does

When triggered, this skill writes or reviews shell scripts following opinionated best practices:

- Always uses `bash` with `#!/usr/bin/env bash`
- Sets `set -o errexit` (exit on error) and `set -o nounset` (exit on unset variables)
- Uses `set -o pipefail` so pipeline errors are not silently swallowed
- Quotes all variable expansions
- Uses `local` for function-scoped variables
- Prefers `[[ ]]` over `[ ]` for conditionals
- Uses `$(...)` over backticks

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install shell-script@rishubil-skills
```

## Usage

Triggers automatically when:

- Writing new bash scripts (`.sh` / `.bash` files)
- Improving or reviewing existing scripts
- Adding error handling to a script
- Editing files in a `scripts/` folder
