---
title: repair-packs :: resticprofile
source: https://creativeprojects.github.io/resticprofile/reference/profile/repair-packs/
---

## repair-packs

#### Section profile.repair-packs

This section configures restic command `repair-packs` available since `0.16.1`. Information on command and flags is copied from the [restic](https://github.com/restic/restic) manual pages.

WARNING: The CLI for this command is experimental and will likely change in the future!

The “repair packs” command extracts intact blobs from the specified pack files, rebuilds the index to remove the damaged pack files and removes the pack files from the repository.

##### Flags used by resticprofile only:

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| **run-after** | one or more `strings` |  | Run shell command(s) after a successful restic command |
| **run-after-fail** | one or more `strings` |  | Run shell command(s) after failed restic or shell commands |
| **run-before** | one or more `strings` |  | Run shell command(s) before a restic command |
| **run-finally** | one or more `strings` |  | Run shell command(s) always, after all other commands |
| **send-after** | one or more nested *[SendMonitoringSection](https://creativeprojects.github.io/resticprofile/reference/nested/sendmonitoringsection/index.html)* |  | Send HTTP request(s) after a successful restic command |
| **send-after-fail** | one or more nested *[SendMonitoringSection](https://creativeprojects.github.io/resticprofile/reference/nested/sendmonitoringsection/index.html)* |  | Send HTTP request(s) after failed restic or shell commands |
| **send-before** | one or more nested *[SendMonitoringSection](https://creativeprojects.github.io/resticprofile/reference/nested/sendmonitoringsection/index.html)* |  | Send HTTP request(s) before a restic command |
| **send-finally** | one or more nested *[SendMonitoringSection](https://creativeprojects.github.io/resticprofile/reference/nested/sendmonitoringsection/index.html)* |  | Send HTTP request(s) always, after all other commands |

Tip

Flags declared for the **restic** command line in section can be overridden in this section.