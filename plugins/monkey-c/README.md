# monkey-c

A Claude Code plugin for developing Garmin Connect IQ applications in Monkey C.

## What it does

Provides specialist knowledge for writing, debugging, and refactoring Monkey C code on the Garmin Connect IQ platform. Covers all supported app types:

| App type | Description |
|---|---|
| Watch Face | Customize the watch display |
| Device App | Full app with complete access to device resources |
| Widget | Information card in the main carousel |
| Data Field | Custom metric display on the activity screen |
| Audio Content Provider | Integration with third-party audio services |

Bundled with a local cache of the official Garmin Connect IQ reference documentation (overviews, language references, and API docs) so it can answer questions offline.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install monkey-c@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install monkey-c@rishubil-skills --scope project
```

## Usage

Triggers automatically when:

- You mention Garmin, Connect IQ, or Monkey C in your query
- You open or edit `.mc` files
- You ask about Watch Faces, Device Apps, Widgets, or Data Fields for Garmin wearables

## License note

The bundled reference documentation is cached from official Garmin sources and remains under Garmin's copyright. See [`skills/monkey-c/NOTICE.md`](./skills/monkey-c/NOTICE.md) for details. The MIT License of this repository does **not** apply to those cached files.
