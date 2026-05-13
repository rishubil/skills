---
title: Logs :: resticprofile
source: https://creativeprojects.github.io/resticprofile/configuration/logs/
---

## Logs

By default **resticprofile** will display all logs (from itself and **restic**) to the console.

You can redirect the logs to a local file, a temporary file or a syslog server.

## Destination

The log destination syntax is a such:

- `-` redirects all the logs to the console / stdout (is the default log destination)
- `filename` redirects all the logs to the local file called **filename**
- `temp:filename` redirects all the logs to a temporary file available during the whole session, and deleted afterwards.
- `syslog:`, `syslog://syslog_server[:514]` or `syslog-tcp://syslog_server[:514]` redirects all the logs to a local or remote **syslog** server. Alternative configurations for remote servers are: `udp://syslog_server:514` & `tcp://syslog_server:514`.
Note

Logging to syslog is not available on Windows.

Tip

If the location cannot be opened, **resticprofile** will default to send the logs to the console.

## Default

You can adjust the default log destination in the `global` section:

```toml
version = "1"

[global]
log = "resticprofile.log"
[global.schedule-defaults]
log = "scheduled-resticprofile.log"
```

```yaml
version: "1"

global:
  log: "resticprofile.log"
  schedule-defaults:
    log: "scheduled-resticprofile.log"
```

```hcl
"global" {
  "log" = "resticprofile.log"
  "schedule-defaults" {
    "log" = "scheduled-resticprofile.log"
  }
}
```

```json
{
  "version": "1",
  "global": {
    "log": "resticprofile.log",
    "schedule-defaults": {
      "log": "scheduled-resticprofile.log"
    }
  }
}
```

## Command line

You can redirect the logs on the command line with the `--log` flag:

```shell
resticprofile --log backup.log backup
```

## On a schedule

You can keep the logs displayed on the console when you run **resticprofile** commands manually, but send the logs somewhere else when **resticprofile** is started from a schedule.

```toml
version = "1"

[profile]
  [profile.backup]
    schedule = "*:00,30"
    schedule-priority = "background"
    schedule-log = "profile-backup.log"
```

```yaml
version: "1"

profile:
  backup:
    schedule: '*:00,30'
    schedule-priority: background
    schedule-log: profile-backup.log
```

```hcl
"profile" "backup" {
  "schedule" = "*:00,30"
  "schedule-priority" = "background"
  "schedule-log" = "profile-backup.log"
}
```

```json
{
  "version": "1",
  "profile": {
    "backup": {
      "schedule": "*:00,30",
      "schedule-priority": "background",
      "schedule-log": "profile-backup.log"
    }
  }
}
```

## Priority on the log targets

If specified in different places, here’s the priority order for the log destination:

1. `--log` flag on the command line
2. `schedule-log` in the `profile` section
3. `log` in the `global` section
4. default to the console

## Send logs to a temporary file

This can be done by using the [template](https://creativeprojects.github.io/resticprofile/configuration/templates/index.html) function `tempFile`.

This is to cover a special case when you want to upload the logs one by one to a remote location in a `run-finally` or a `run-after-fail` target.

```toml
version = "1"

[backup_current]
  [backup_current.backup]
    verbose = true
    no-error-on-warning = true
    source = "{{ .CurrentDir }}"
    schedule = "*:44"
    schedule-log = '{{ tempFile "backup.log" }}'
    run-finally = 'cp {{ tempFile "backup.log" }} /logs/backup{{ .Now.Format "2006-01-02T15-04-05" }}.log'
```

```yaml
version: "1"

backup_current:
  backup:
    verbose: true
    no-error-on-warning: true
    source: "{{ .CurrentDir }}"
    schedule:
      - "*:44"
    schedule-log: '{{ tempFile "backup.log" }}'
    run-finally: 'cp {{ tempFile "backup.log" }} /logs/backup{{ .Now.Format "2006-01-02T15-04-05" }}.log'
```

```hcl
"profile" "backup" {
  "verbose" = true
  "no-error-on-warning" = true
  "source" = "{{ .CurrentDir }}"
  "schedule" = "*:44"
  "schedule-log" = "{{ tempFile "backup.log" }}"
  "run-finally" = "cp {{ tempFile "backup.log" }} /logs/backup{{ .Now.Format "2006-01-02T15-04-05" }}.log"
}
```

```json
{
  "version": "1",
  "profile": {
    "backup": {
      "verbose": true,
      "no-error-on-warning": true,
      "source": "{{ .CurrentDir }}",
      "schedule": "*:44",
      "schedule-log": "{{ tempFile "backup.log" }}",
      "run-finally": "cp {{ tempFile "backup.log" }} /logs/backup{{ .Now.Format "2006-01-02T15-04-05" }}.log"
    }
  }
}
```