# resticprofile

A Claude Code plugin for working with [resticprofile](https://creativeprojects.github.io/resticprofile/) — a configuration profile manager and scheduler for the [restic](https://restic.net/) backup tool.

## What it does

Provides specialist knowledge for:

- Creating and editing resticprofile config files (`profiles.toml` / `.yaml` / `.json` / `.hcl`)
- Profile inheritance (`inherit` key)
- Backup, retention, and check sections
- Run hooks (`run-before` / `run-after` / `run-after-fail` / `run-finally`)
- Monitoring integrations (e.g. healthchecks.io pings)
- Scheduling via systemd, launchd, cron, or Windows Task Scheduler
- Docker and container deployments
- Any resticprofile CLI command (`schedule`, `status`, `profiles`, `init`, etc.)

Bundled with a local cache of the official resticprofile documentation.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install resticprofile@rishubil-skills
```

## Usage

Triggers automatically whenever **"resticprofile"** appears anywhere in your query (in any language). Does **not** trigger for:

- Bare `restic` scripts with no resticprofile involvement
- Borg Backup, plain systemd timers, or other backup tools

## License note

The bundled reference documentation is cached from the official resticprofile docs and remains under the MIT License of the resticprofile contributors. See [`skills/resticprofile/NOTICE.md`](./skills/resticprofile/NOTICE.md) for details.
