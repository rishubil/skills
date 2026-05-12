---
title: Priority :: resticprofile
source: https://creativeprojects.github.io/resticprofile/configuration/priority/
---

## Priority

By default, restic is running with the default priority. It means it will get equal share of the resources with other processes.

You can lower the priority of restic to avoid slowing down other processes. This is especially useful when you run restic on a production server.

## Nice

You can use these values for the `priority` parameter, string or numeric values are both valid:

| String value | “nice” equivalent on unixes | Notes |
| --- | --- | --- |
| Idle | 19 |  |
| Background [^1] | 15 | **This mode is NOT recommended on Windows 11** |
| Low | 10 |  |
| Normal | 0 | Default priority when unspecified |
| High | \-10 |  |
| Highest | \-20 |  |

## IO Nice

This setting is only available on Linux. It allows you to set the disks IO priority of restic.

Info

This setting is only affecting access to local disks. It has no effect on any network access.

More information about ionice “class” and “level” can be found [here](https://linux.die.net/man/1/ionice).

## Examples

```toml
version = "1"

[global]
  # priority is using priority class on windows, and "nice" on unixes
  priority = "low"
  # ionice is available on Linux only
  ionice = true
  ionice-class = 2
  ionice-level = 6
```

```yaml
version: "1"

global:
  # priority is using priority class on windows, and "nice" on unixes
  priority: low
  # ionice is available on Linux only
  ionice: true
  ionice-class: 2
  ionice-level: 6
```

```hcl
global {
    # priority is using priority class on windows, and "nice" on unixes
    priority = "low"
    # ionice is available on Linux only
    ionice = true
    ionice-class = 2
    ionice-level = 6
}
```

## Warnings

In some cases (mostly before version `v0.27.0`), resticprofile won’t be able to set the priority of restic.

A warning message like this will be displayed:

```html
cannot set process group priority, restic will run with the default priority: operation not permitted
```

This either means:

- resticprofile is running inside docker
- you are using a tight security linux distribution which is launching every process inside a new container
- resticprofile is running in WSL
- you’re running an older version of resticprofile (< `v0.27.0`)

[^1]: It seems that the implementation of the background mode is broken in Windows 11. Even though undocumented, it is widely reported that the process has a limit of 32MB of memory. Please use `Idle` or `Low` on Windows 11.