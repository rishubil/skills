# resticprofile S3 Backup Configuration — Explanation

## File: `profiles.toml`

### Structure Overview

The configuration defines two TOML sections:

- **`[default]`** — A base profile that sets the S3 repository URL and AWS credentials via environment variable references. All other profiles can inherit from this.
- **`[backup-weekly]`** — The active backup profile, which inherits the base settings and adds source paths, hooks, and a systemd-compatible schedule.

---

### Key Design Decisions

#### Repository
```toml
repository = "s3:s3.amazonaws.com/mycompany-backup"
```
Uses the standard restic S3 URI format.

#### AWS Credentials via Environment Variables
```toml
[default.env]
  AWS_ACCESS_KEY_ID     = "{{ .Env.AWS_ACCESS_KEY_ID }}"
  AWS_SECRET_ACCESS_KEY = "{{ .Env.AWS_SECRET_ACCESS_KEY }}"
```
Credentials are not hardcoded. resticprofile reads them from the shell environment at runtime using Go template syntax. You must export these variables before running, or inject them via a systemd `EnvironmentFile=`.

#### Backup Sources
```toml
source = ["/var/www", "/etc"]
```
Both directories are backed up in a single restic invocation.

#### Healthchecks.io Hooks
| Hook | URL called | Purpose |
|------|-----------|---------|
| `run-before` | `…/{uuid}/start` | Signals backup has started |
| `run-after` | `…/{uuid}` | Signals success |
| `run-after-fail` | `…/{uuid}/fail` | Signals failure |

Set the `HC_UUID` environment variable (or replace it in the file) with your healthchecks.io check UUID.

#### Systemd Schedule
```toml
schedule = "Sun *-*-* 03:00:00"
permission = "system"
```
Uses systemd calendar syntax. Running `resticprofile schedule --all` will generate and install a systemd timer + service unit automatically. The `permission = "system"` setting ensures the units are installed as system-level (not user-level) services.

---

### Setup Checklist

1. Install restic and resticprofile on the server.
2. Create `/etc/resticprofile/restic-password` with your restic repository password (mode `600`).
3. Export or inject AWS credentials:
   ```
   AWS_ACCESS_KEY_ID=...
   AWS_SECRET_ACCESS_KEY=...
   ```
   For systemd, add an `EnvironmentFile=` pointing to a secure credentials file.
4. Set `HC_UUID` to your healthchecks.io check UUID (or replace the shell variable in the hooks).
5. Initialize the restic repository once:
   ```
   resticprofile backup-weekly.backup --init
   ```
6. Register the systemd timer:
   ```
   resticprofile schedule --all
   ```
7. Verify the timer:
   ```
   systemctl status resticprofile-backup-weekly@backup.timer
   ```
