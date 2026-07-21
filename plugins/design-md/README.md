# design-md

A Claude Code plugin for authoring, applying, evolving, and exporting a
`DESIGN.md` — a checked-in file that pins a project's visual identity as
machine-readable design tokens plus human-readable prose, so UI stays
consistent across sessions, agents, and tools.

## What it does

The bundled `design-md` skill teaches Claude the full DESIGN.md lifecycle:
harvesting evidence and interviewing the user to author a new file, reading
and applying an existing file's tokens and prose when building or restyling
UI, evolving a file's tokens without letting the prose drift out of sync, and
exporting the token block to Tailwind (v3/v4) or W3C DTCG `tokens.json` for
downstream tooling. It ships a starter skeleton with pre-tuned design
tokens, the upstream format spec, a philosophy reference, and a lint-clean
worked example.

The plugin also adds a **PostToolUse hook** that automatically runs
`designmd lint` on any `DESIGN.md`-named file after a Write or Edit. On an
error finding (currently only `broken-ref`) it halts the turn and hands the
findings back to Claude — the write itself is not reverted, since the hook
runs after the tool has already completed. Warnings (contrast ratio,
orphaned tokens, section order, etc.) surface as advisory context instead
of failing the call.

## Source

Based on the DESIGN.md format from Google Labs:
<https://github.com/google-labs-code/design.md>, licensed under the
[Apache License 2.0](https://github.com/google-labs-code/design.md/blob/main/LICENSE),
© Google LLC. The skill's `references/` directory caches a snapshot of the
upstream spec, philosophy doc, and worked example — see
[`skills/design-md/NOTICE.md`](./skills/design-md/NOTICE.md) for details.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install design-md@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install design-md@rishubil-skills --scope project
```

## Usage

Mention a project's design system, visual identity, color palette,
typography, spacing, or component styling — or just say "DESIGN.md" or
"design tokens" — and Claude will activate the skill. If a DESIGN.md already
exists in the repo, Claude reads it before any UI work automatically, even if
you never say the word "design".

The hook needs no manual triggering: any time Claude (or you, through
Claude) writes or edits a `DESIGN.md`-named file, it is linted immediately
afterward, and a blocking `broken-ref` error must be fixed before the
session moves on.

## Scripts

| Path | Purpose |
|---|---|
| `scripts/designmd-lint-hook.sh` | Dispatcher: tries `uv`, then `python3`, then `python` (3.x) |
| `scripts/designmd-lint-hook.py` | Hook logic: runs `designmd lint` on the written/edited file, blocks on error findings, surfaces warnings as advisory context |
