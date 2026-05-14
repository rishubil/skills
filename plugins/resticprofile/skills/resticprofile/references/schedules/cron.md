---
title: Cron & compatible :: resticprofile
source: https://creativeprojects.github.io/resticprofile/schedules/cron/
---

## Cron & compatible

On non-Windows OS, use a **crond** -compatible scheduler if specified in `global` / `scheduler`:

Windows No Longer Supported

Crond support on Windows has been removed due to significant issues in previous versions.

```toml
[global]
  scheduler = "crond"
```

```yaml
---
global:
    scheduler: crond
```

```hcl
"global" = {
  "scheduler" = "crond"
}
```

```json
{
  "global": {
    "scheduler": "crond"
  }
}
```

This configuration uses the default `crontab` tool shipped with `crond`.

You can specify the location of the `crontab` tool:

```toml
[global]
  scheduler = "crond:/usr/bin/crontab"
```

```yaml
---
global:
    scheduler: crond:/usr/bin/crontab
```

```hcl
"global" = {
  "scheduler" = "crond:/usr/bin/crontab"
}
```

```json
{
  "global": {
    "scheduler": "crond:/usr/bin/crontab"
  }
}
```

## Crontab

You can use a crontab file directly instead of the `crontab` tool:

- `crontab:*:filepath`: Use a crontab file `filepath` **with a user field** filled in automatically
- `crontab:username:filepath`: Use a crontab file `filepath` **with a user field** always set to `username`
- `crontab:-:filepath`: Use a crontab file `filepath` **without a user field**

### With user field

```toml
[global]
  scheduler = "crontab:*:/etc/cron.d/resticprofile"
```

```yaml
---
global:
    scheduler: "crontab:*:/etc/cron.d/resticprofile"
```

```hcl
"global" = {
  "scheduler" = "crontab:*:/etc/cron.d/resticprofile"
}
```

```json
{
  "global": {
    "scheduler": "crontab:*:/etc/cron.d/resticprofile"
  }
}
```

### Without a user field

```toml
[global]
  scheduler = "crontab:-:/var/spool/cron/crontabs/username"
```

```yaml
---
global:
    scheduler: "crontab:-:/var/spool/cron/crontabs/username"
```

```hcl
"global" = {
  "scheduler" = "crontab:-:/var/spool/cron/crontabs/username"
}
```

```json
{
  "global": {
    "scheduler": "crontab:-:/var/spool/cron/crontabs/username"
  }
}
```