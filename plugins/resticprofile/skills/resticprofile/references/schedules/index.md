---
title: Schedules :: resticprofile
source: https://creativeprojects.github.io/resticprofile/schedules/
---

## Schedules

## Scheduler

resticprofile manages scheduled backups using:

- **[launchd](https://creativeprojects.github.io/resticprofile/schedules/launchd/index.html)** on macOS
- **[Task Scheduler](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/index.html)** on Windows
- **[systemd](https://creativeprojects.github.io/resticprofile/schedules/systemd/index.html)** on Linux and other BSDs
- **[crond](https://creativeprojects.github.io/resticprofile/schedules/cron/index.html)** as a fallback (requires `crontab` binary)
- **[crontab](https://creativeprojects.github.io/resticprofile/schedules/cron/index.html)** files (with or without a user column)

On Unix systems (excluding macOS), resticprofile uses **systemd** if available, otherwise it falls back to **crond**.

See [reference / global section](https://creativeprojects.github.io/resticprofile/reference/global/index.html) for scheduler configuration options.

Each profile can be scheduled independently. Within each profile, these sections can be scheduled:

- **backup**
- **check**
- **forget**
- **prune**
- **copy**

## Deprecation

Scheduling the `retention` section directly is **deprecated**. Use the `forget` section instead.

The retention section should be associated with a `backup` section, not scheduled independently.

```toml
[profile.retention]
  # deprecated
  schedule = "daily"

# use the forget target instead
[profile.forget]
  schedule = "daily"
```

```yaml
---
profile:
  retention:
    # deprecated
    schedule: daily

  # use the forget target instead
  forget:
    schedule: daily
```

```hcl
"profile" = {
  "retention" = {
     # deprecated
    schedule = "daily"
  }

  # use the forget target instead
  "forget" = {
    schedule = "daily"
  }
}
```

```json
{
  "profile": {
    "forget": {
      "schedule": "daily"
    }
  }
}
```

## More information

- [Schedule Configuration](https://creativeprojects.github.io/resticprofile/schedules/configuration/index.html)
- [Schedule Commands](https://creativeprojects.github.io/resticprofile/schedules/commands/index.html)
- [Schedule Examples](https://creativeprojects.github.io/resticprofile/schedules/examples/index.html)
- [Systemd](https://creativeprojects.github.io/resticprofile/schedules/systemd/index.html)
- [Launchd on macOS](https://creativeprojects.github.io/resticprofile/schedules/launchd/index.html)
- [Windows Task Scheduler](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/index.html)
- [Cron & compatible](https://creativeprojects.github.io/resticprofile/schedules/cron/index.html)
- [User schedule in container](https://creativeprojects.github.io/resticprofile/schedules/non-root-schedule-in-container/index.html)