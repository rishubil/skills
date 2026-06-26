# hypothesis

A Claude Code plugin that writes property-based tests for Python codebases using the [Hypothesis](https://hypothesis.readthedocs.io/) library.

## What it does

When triggered, this skill:

1. **Explores** the target code and identifies a small set of the most valuable properties to test (round-trip, inverse, idempotence, invariants, metamorphic properties, etc.)
2. **Investigates** how the related code is actually used in the codebase before writing tests
3. **Writes** focused Hypothesis tests and adds them to the existing test suite, following the project's testing conventions
4. **Runs** the new tests and reflects on any failures — distinguishing genuine bugs from overly broad test inputs

The skill prioritises clarity and precision over coverage: it writes a few high-quality tests, not a comprehensive suite.

## Prerequisites

Hypothesis must be installed in the project:

```bash
pip install hypothesis
# or, if using uv:
uv add hypothesis
```

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install hypothesis@rishubil-skills
```

## Usage

Trigger phrases include:

- "add Hypothesis tests to this module"
- "write property-based tests for `parser.py`"
- "find properties worth testing in the `encode`/`decode` functions"
- "write Hypothesis tests for the entire codebase"

You can name a specific module, file, or function to narrow the scope; otherwise the skill explores the entire codebase.

## Source

Based on the [`hypothesis.md`](https://github.com/HypothesisWorks/hypothesis/blob/master/.claude/commands/hypothesis.md) Claude command from the [HypothesisWorks/hypothesis](https://github.com/HypothesisWorks/hypothesis) repository (MIT License).
