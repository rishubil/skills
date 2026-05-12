---
name: resticprofile
description: "Specialist skill for resticprofile — a configuration profile manager for the restic backup tool. Use this skill whenever the user is configuring resticprofile profiles, writing or editing resticprofile config files (TOML/YAML/JSON/HCL), setting up backup schedules, running resticprofile commands, or troubleshooting restic backups managed by resticprofile. Trigger on any mention of resticprofile, restic profiles, restic config files, or restic backup automation."
---

# resticprofile

resticprofile is a configuration profile manager for [restic](https://restic.net/). It wraps restic commands with profile-based configuration, supports scheduling (cron/systemd/launchd/Windows Task Scheduler), and lets you define all backup parameters in a single config file.

## Reference Documentation

Detailed documentation is bundled in `references/`. Read the relevant files when working on specific topics:

| Topic | File |
|-------|------|
| Configuration reference (all keys) | `references/reference/index.md` and subdirs |
| Command-line usage | `references/usage/index.md` |
| Scheduling | `references/schedules/index.md` |
| Installation | `references/installation.md` |
| Getting started / overview | `references/index.md` |
| How-to guides | `references/how-to/index.md` |

Always read the relevant reference file before answering questions about config keys, commands, or scheduler options.

## Configuration File

resticprofile supports **TOML** (default), YAML, JSON, and HCL. TOML is most common in examples.

Default config file search order: `profiles.toml`, `profiles.yaml`, `profiles.json`, `profiles.hcl`, `~/.config/resticprofile/profiles.toml`.

### Top-level Sections

```toml
[global]          # resticprofile-wide settings (not passed to restic)
  priority = "low"
  ionice = true

[groups]          # Named groups of profiles to run together
  [groups.full-backup]
    profiles = ["documents", "photos"]

["default"]       # Profile named "default" — used when no profile is specified
  repository = "/mnt/backup/default"
  password-file = "key"

["my-profile"]    # A named profile
  inherit = "default"   # Inherit settings from another profile
  ...
```

### Profile Configuration

Within a profile, you configure restic repository settings and sub-sections for each restic command:

```toml
["my-profile"]
  repository = "s3:s3.amazonaws.com/my-bucket"
  password-file = "/etc/restic/password"
  
  [my-profile.env]
    AWS_ACCESS_KEY_ID = "..."
    AWS_SECRET_ACCESS_KEY = "..."

  [my-profile.backup]
    source = ["/home", "/etc"]
    exclude = ["**/.cache", "**/node_modules"]
    schedule = "daily"
    schedule-permission = "system"

  [my-profile.retention]
    keep-daily = 7
    keep-weekly = 4
    keep-monthly = 12
    after-backup = true   # Run forget after every backup

  [my-profile.check]
    schedule = "weekly"
```

### Key Configuration Properties

**Repository settings** (profile level):
- `repository` — restic repository path/URL
- `password-file` / `password-command` — repository password
- `initialize` — auto-init repo if missing (bool)
- `inherit` — inherit from another profile name
- `cache-dir` — restic cache directory

**Backup section** (`[profile.backup]`):
- `source` — list of paths to back up
- `exclude` — glob patterns to exclude
- `exclude-file` — path to exclude file
- `schedule` — when to run (see Scheduling)
- `schedule-permission` — `"user"` or `"system"`
- `run-before` / `run-after` / `run-after-fail` — shell commands

**Retention section** (`[profile.retention]`):
- `keep-last` / `keep-hourly` / `keep-daily` / `keep-weekly` / `keep-monthly` / `keep-yearly`
- `after-backup = true` — run forget immediately after each backup

## Common Commands

```bash
# Run backup for a profile
resticprofile [--name profile-name] backup

# List snapshots
resticprofile [--name profile-name] snapshots

# Initialize repository
resticprofile [--name profile-name] init

# Restore
resticprofile [--name profile-name] restore latest --target /tmp/restore

# Run forget/prune
resticprofile [--name profile-name] forget
resticprofile [--name profile-name] prune

# Check repository
resticprofile [--name profile-name] check

# List profiles in config
resticprofile profiles

# Show effective configuration for a profile
resticprofile show

# Schedule management
resticprofile schedule         # Install scheduled tasks for the profile
resticprofile unschedule       # Remove scheduled tasks
resticprofile status           # Show scheduler status

# Run a group of profiles
resticprofile --name full-backup backup
```

### Global Flags

```bash
resticprofile \
  --config /path/to/profiles.toml \   # Config file path
  --name profile-name \                # Profile to use
  --dry-run \                          # Simulate without changes
  --log /var/log/resticprofile.log \   # Log file
  --no-ansi \                          # Disable color output
  backup
```

## Scheduling

resticprofile integrates with the OS scheduler:

| OS | Scheduler |
|----|-----------|
| Linux (system) | systemd |
| Linux (user) | systemd user |
| macOS | launchd |
| Windows | Task Scheduler |
| Fallback | crond |

Schedule expressions (set on `backup`, `check`, etc.):

```toml
schedule = "daily"             # Every day
schedule = "weekly"            # Every week  
schedule = "hourly"            # Every hour
schedule = "Mon..Fri *-*-* 20:00:00"   # Systemd calendar notation
schedule = "@daily"            # Cron-style
schedule = "0 20 * * 1-5"     # Cron expression
```

## Common Patterns

### Minimal Working Config

```toml
[global]
  priority = "low"

["local"]
  repository = "/mnt/backup/local"
  password-file = "key"
  initialize = true

  [local.backup]
    source = ["/home/user"]
    exclude = ["**/.cache"]

  [local.retention]
    keep-daily = 7
    keep-weekly = 4
    after-backup = true
```

### S3/Cloud Backup with Schedule

```toml
["s3-backup"]
  repository = "s3:s3.amazonaws.com/my-restic-bucket"
  password-file = "/etc/restic/password"

  [s3-backup.env]
    AWS_ACCESS_KEY_ID = "your-key-id"
    AWS_SECRET_ACCESS_KEY = "your-secret"

  [s3-backup.backup]
    source = ["/home", "/etc", "/var/www"]
    exclude = ["**/.cache", "**/node_modules", "**/__pycache__"]
    schedule = "daily"
    schedule-permission = "system"
    run-after-fail = ["curl -fsS -m 10 'https://hc-ping.com/your-uuid/fail'"]

  [s3-backup.retention]
    keep-daily = 7
    keep-weekly = 8
    keep-monthly = 12
    after-backup = true

  [s3-backup.check]
    schedule = "weekly"
```

### Profile Inheritance

```toml
["base"]
  repository = "/mnt/backup"
  password-file = "/etc/restic/password"
  
  [base.retention]
    keep-daily = 7
    keep-weekly = 4
    after-backup = true

["documents"]
  inherit = "base"
  [documents.backup]
    source = ["/home/user/Documents"]

["photos"]
  inherit = "base"
  [photos.backup]
    source = ["/home/user/Pictures"]
    exclude = ["**/*.tmp"]
```

## Tips

- Use `resticprofile show` to see the merged/effective config for a profile — invaluable for debugging inheritance.
- `initialize = true` at the profile level auto-inits the repo if it doesn't exist yet.
- `run-before`/`run-after`/`run-after-fail` accept a list of shell commands — useful for healthcheck pings or mounting network shares.
- For systemd scheduling with `schedule-permission = "system"`, run `resticprofile schedule` as root.
- `--dry-run` flag is available for most commands to preview what would happen.
