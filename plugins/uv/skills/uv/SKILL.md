---
name: uv
description: >
  Enforces a uv-only Python workflow in every directory, not just uv projects. Use whenever Python is
  about to be run, a Python package installed, or a Python tool invoked — all of it goes through
  `uv run`, `uv add`, `uv run --with`, or `uvx` instead of `python`, `pip`, or `pipx`.
---

# uv — Python Package and Script Management

While this plugin is enabled, [`uv`](https://docs.astral.sh/uv/) is the single entry point for all
Python operations in every directory, whether or not the directory is a uv project. Follow these
rules strictly:

## Running Python

Always use `uv run` instead of calling `python` or `python3` directly:

```bash
# correct
uv run python script.py
uv run pytest
uv run mypy src/

# wrong — never do this
python script.py
python3 script.py
```

## Installing Dependencies

Use `uv add` to add packages. Never use `pip install`, even through `uv run pip install`:

```bash
# correct
uv add requests
uv add --dev pytest

# wrong
pip install requests
uv run pip install requests
uv pip install requests
```

`uv add` only works inside a uv project (one with a `pyproject.toml`). Outside one, use
`uv run --with <pkg> ...`, inline script metadata (see below), or `uvx <tool>`:

```bash
uv run --with requests script.py
uvx ruff check .
```

## Running Scripts

```bash
uv run script.py                   # Run a script
uv run script.py arg1 arg2         # With arguments
uv run --python 3.10 script.py     # Specific Python version
echo 'print("hi")' | uv run -      # From stdin
```

In a project directory, skip installing the project when running a standalone script:

```bash
uv run --no-project script.py
```

### Syntax Verification (No `__pycache__`)

Use the AST parser instead of `python -m py_compile`:

```bash
uv run python -m ast script.py >/dev/null
```

### Ad-hoc Dependencies

```bash
uv run --with requests script.py
uv run --with 'requests>2,<3' script.py
uv run --with requests --with rich script.py
```

## Inline Script Metadata (Recommended)

Declare dependencies directly in the script:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich import print
```

Then just: `uv run script.py`

### Managing Script Dependencies

```bash
uv init --script example.py --python 3.12   # Create script with metadata
uv add --script example.py requests rich    # Add dependencies
```

### Locking Script Dependencies

```bash
uv lock --script example.py  # Creates example.py.lock
```

### Pinning Resolution Date

```python
# /// script
# dependencies = ["requests"]
# [tool.uv]
# exclude-newer = "2023-10-16T00:00:00Z"
# ///
```

### Executable Scripts (Shebang)

```python
#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["httpx"]
# ///

import httpx
print(httpx.get("https://example.com"))
```

```bash
chmod +x myscript
./myscript
```

## Running Tools

Use `uvx` (or `uv tool run`) for one-off tool invocations instead of `pipx` or global installs:

```bash
uvx ruff check .
uvx black --check .
```
