---
name: uv
description: >
  Enforces uv-based Python workflow in projects that use uv. Use when working in any Python project
  managed by uv — ensures all Python execution goes through `uv run` and dependencies are added via
  `uv add` rather than pip install.
---

# uv — Python Package and Script Management

This project uses [`uv`](https://docs.astral.sh/uv/) as the single entry point for all Python
operations. Follow these rules strictly:

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

## Inline Script Dependencies

For standalone scripts, declare dependencies in the script metadata block:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
# ]
# ///
```

Run such scripts with `uv run script.py` — uv handles the environment automatically.

## Running Tools

Use `uvx` (or `uv tool run`) for one-off tool invocations instead of `pipx` or global installs:

```bash
uvx ruff check .
uvx black --check .
```
