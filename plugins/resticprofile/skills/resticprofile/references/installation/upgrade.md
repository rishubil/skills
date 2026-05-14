---
title: Upgrade :: resticprofile
source: https://creativeprojects.github.io/resticprofile/installation/upgrade/
---

## Upgrade

After installation, upgrade resticprofile to the latest release with this command:

```shell
resticprofile self-update
```
Package Managers

The `self-update` command is generally unavailable when installed through a package manager like Homebrew or Scoop. Use the package manager’s upgrade feature instead.

Resticprofile checks for new versions from GitHub releases and prompts you to update. Use the `-q` or `--quiet` flag to update automatically without prompting.

```shell
resticprofile --quiet self-update
```

or

```shell
resticprofile self-update --quiet
```