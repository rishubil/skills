---
name: resticprofile
description: "TRIGGER whenever 'resticprofile' appears anywhere in the user's query — in any language. resticprofile is a profile-based configuration manager and scheduler for the restic backup tool. Use for: creating or editing resticprofile config files (profiles.toml/yaml/json/hcl), the `show` command for debugging effective config, profile inheritance (`inherit` key), backup/retention/check sections, `after-backup` and forget behavior, run hooks (`run-before`/`run-after`/`run-after-fail`/`run-finally`), monitoring integrations (healthchecks.io pings), scheduling via systemd/launchd/cron/Task Scheduler, Docker or container deployments, and any resticprofile CLI command (schedule, status, profiles, init). SKIP for bare restic scripts (no resticprofile), Borg Backup, plain systemd timers, or other backup tools not involving resticprofile."
---

# resticprofile

resticprofile is a configuration profile manager for [restic](https://restic.net/). It wraps restic commands with profile-based configuration, supports scheduling (cron/systemd/launchd/Windows Task Scheduler), and lets you define all backup parameters in a single config file.

## Reference Documentation

Detailed documentation is bundled in `references/`. Read the relevant files when working on specific topics:

| Topic | Files |
|-------|-------|
| Overview / what resticprofile does | `references/index.md` |
| Installation (Linux, macOS, Windows, Docker, Ansible…) | `references/installation/index.md` and subdirs |
| Configuration basics & getting started | `references/configuration/index.md`, `references/configuration/getting_started.md` |
| Profile inheritance | `references/configuration/inheritance.md` |
| Run hooks (run-before/after/after-fail/finally) | `references/configuration/run_hooks.md` |
| HTTP hooks (send-before/after/after-fail/finally) | `references/configuration/http_hooks.md` |
| Templates & variables in config | `references/configuration/templates.md`, `references/configuration/variables.md` |
| Configuration v2 format | `references/configuration/v2.md` |
| Scheduling overview | `references/schedules/index.md` |
| Schedule configuration options | `references/schedules/configuration.md` |
| systemd scheduling | `references/schedules/systemd.md` |
| launchd scheduling (macOS) | `references/schedules/launchd.md` |
| cron scheduling | `references/schedules/cron.md` |
| Windows Task Scheduler | `references/schedules/task_scheduler.md` |
| Schedule examples | `references/schedules/examples.md` |
| Profile section reference (all flags per command) | `references/reference/profile/index.md` |
| backup command reference | `references/reference/profile/backup.md` |
| forget command reference | `references/reference/profile/forget.md` |
| retention section reference | `references/reference/profile/retention.md` |
| check command reference | `references/reference/profile/check.md` |
| restore command reference | `references/reference/profile/restore.md` |
| init command reference | `references/reference/profile/init.md` |
| prune command reference | `references/reference/profile/prune.md` |
| copy command reference | `references/reference/profile/copy.md` |
| snapshots command reference | `references/reference/profile/snapshots.md` |
| Global section reference | `references/reference/global.md` |
| Groups section reference | `references/reference/groups.md` |
| Schedule config nested section | `references/reference/nested/scheduleconfig.md` |
| Monitoring (status file, Prometheus) | `references/monitoring/index.md` |
| Locks | `references/usage/locks.md` |
| Key file generation | `references/usage/keyfile.md` |
| Memory check | `references/usage/memory.md` |
| Logging | `references/configuration/logs.md` |

Always read the relevant reference file before answering questions about specific config keys, command flags, or scheduler options.

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

**Profile level** (common repository settings):
- `repository` — restic repository path/URL
- `password-file` / `password-command` — repository password
- `initialize` — auto-init repo if missing (bool)
- `inherit` — inherit from another profile name
- `cache-dir` — restic cache directory
- `env` — environment variables passed to restic (subsection)

> **Profile name quoting**: Profile names containing hyphens or dots must be quoted: `["my-profile"]`. Simple alphanumeric names can omit quotes: `[myprofile]`.

**env subsection** — passes environment variables to restic. Values are Go templates, not shell:

```toml
[myprofile.env]
  # Correct: Go template syntax resolves at runtime
  AWS_ACCESS_KEY_ID     = "{{ .Env.AWS_ACCESS_KEY_ID }}"
  AWS_SECRET_ACCESS_KEY = "{{ .Env.AWS_SECRET_ACCESS_KEY }}"
  # Wrong: ${VAR} is shell syntax and will NOT be expanded by resticprofile
```

Other available template variables: `{{ .Profile.Name }}`, `{{ .Hostname }}`, `{{ .ConfigDir }}`, `{{ .Env.HOME | or "/fallback" }}`

**Backup section** (`[profile.backup]`):
- `source` — list of paths to back up
- `exclude` — glob patterns to exclude (must be inside `[profile.backup]`, not `[profile]`)
- `exclude-file` — path to exclude file
- `schedule` — when to run (see Scheduling below)
- `schedule-permission` — `"auto"` | `"user"` | `"system"` | `"user_logged_on"`
- `run-before` / `run-after` / `run-after-fail` / `run-finally` — shell commands
- `check-before` / `check-after` — run check before/after backup

**Retention section** (`[profile.retention]`):
- `keep-last` / `keep-hourly` / `keep-daily` / `keep-weekly` / `keep-monthly` / `keep-yearly`
- `after-backup = true` — run forget immediately after each backup (preferred over a separate scheduled forget)

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

**Flat style** — `schedule` and `schedule-*` keys directly in the command section:

```toml
[myprofile.backup]
  schedule            = "Sun *-*-* 03:00:00"   # Systemd OnCalendar
  schedule-permission = "system"
  schedule-lock-wait  = "30m"
  schedule-log        = "syslog:"
```

**Nested ScheduleConfig block** — alternative with different key names (`at`, `permission`, `lock-wait`, `log`):

```toml
[myprofile.backup]
  # ... other backup settings ...

[myprofile.backup.schedule]
  at         = "Sun *-*-* 03:00:00"
  permission = "system"
  lock-wait  = "30m"
  log        = "/var/log/resticprofile.log"
```

Common schedule expressions:

```toml
schedule = "daily"                    # Every day at midnight
schedule = "weekly"                   # Every week
schedule = "hourly"                   # Every hour
schedule = "*-*-* 02:00:00"          # Daily at 02:00
schedule = "Mon..Fri *-*-* 20:00:00" # Weekdays at 20:00
schedule = "Sun *-*-* 03:00:00"      # Sundays at 03:00
schedule = "0 20 * * 1-5"            # Cron expression
```

For per-scheduler details read the files under `references/schedules/`.

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

### S3/Cloud Backup with Schedule and Monitoring

```toml
["s3-backup"]
  repository    = "s3:s3.amazonaws.com/my-restic-bucket"
  password-file = "/etc/restic/password"
  initialize    = true

  # Use Go template syntax {{ .Env.VAR }} — not shell ${VAR}
  [s3-backup.env]
    AWS_ACCESS_KEY_ID     = "{{ .Env.AWS_ACCESS_KEY_ID }}"
    AWS_SECRET_ACCESS_KEY = "{{ .Env.AWS_SECRET_ACCESS_KEY }}"

  [s3-backup.backup]
    source  = ["/home", "/etc", "/var/www"]
    exclude = ["**/.cache", "**/node_modules", "**/__pycache__"]
    schedule            = "daily"
    schedule-permission = "system"
    # healthchecks.io monitoring: signal start, success, and failure
    run-before     = ["curl -fsS -m 10 --retry 3 'https://hc-ping.com/your-uuid/start'"]
    run-after      = ["curl -fsS -m 10 --retry 3 'https://hc-ping.com/your-uuid'"]
    run-after-fail = ["curl -fsS -m 10 --retry 3 'https://hc-ping.com/your-uuid/fail'"]

  [s3-backup.retention]
    keep-daily   = 7
    keep-weekly  = 8
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
- `run-before`/`run-after`/`run-after-fail`/`run-finally` accept a list of shell commands — useful for healthcheck pings or mounting network shares.
- For systemd scheduling with `schedule-permission = "system"`, run `resticprofile schedule` as root.
- `--dry-run` flag is available for most commands to preview what would happen.
- For all available flags per command, read `references/reference/profile/<command>.md`.
- **`exclude` must go inside `[profile.backup]`**, not at the `[profile]` level — placing it at the wrong level silently ignores it.
- **`after-backup = true`** in `[profile.retention]` is the resticprofile-native way to run forget after each backup. Avoid creating a separate scheduled forget section — it's redundant and harder to maintain.
- Environment variable values in the `env` section use Go template syntax: `{{ .Env.MY_VAR }}`. Shell-style `${MY_VAR}` is not expanded by resticprofile.
