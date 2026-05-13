---
title: Warnings :: resticprofile
source: https://creativeprojects.github.io/resticprofile/configuration/warnings/
---

## Warnings

## Warnings from restic

Until version 0.13.0, resticprofile was always considering a restic warning as an error. This will remain the **default**. But the version 0.13.0 introduced a parameter to avoid this behaviour and consider that the backup was successful instead.

A restic warning occurs when it cannot read some files, but a snapshot was successfully created.

### no-error-on-warning

```toml
version = "1"

[profile]

  [profile.backup]
    no-error-on-warning = true
```

```yaml
version: "1"

profile:
    backup:
        no-error-on-warning: true
```

```hcl
"profile" = {

  "backup" = {
    "no-error-on-warning" = true
  }
}
```

```json
{
  "version": "1",
  "profile": {
    "backup": {
      "no-error-on-warning": true
    }
  }
}
```