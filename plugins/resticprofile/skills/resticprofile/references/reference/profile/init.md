---
title: init :: resticprofile
source: https://creativeprojects.github.io/resticprofile/reference/profile/init/
---

## init

#### Section profile.init

This section configures restic command `init`. Information on command and flags is copied from the [restic](https://github.com/restic/restic) manual pages.

The “init” command initializes a new repository.

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

##### Flags passed to the restic command line:

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| **copy-chunker-params** | `true` / `false` | `false` | copy chunker parameters from the secondary repository (useful with the copy command). `restic >= 0.10.0` |
| **from-insecure-no-password** | `true` / `false` | `false` | use an empty password for the source repository (insecure). `restic >= 0.17.0` |
| **from-key-hint** | `string` | `""` | key ID of key to try decrypting the source repository first (default: $RESTIC\_FROM\_KEY\_HINT). `restic >= 0.14.0` |
| **from-password-command** | `string` | `""` | shell command to obtain the source repository password from (default: $RESTIC\_FROM\_PASSWORD\_COMMAND). `restic >= 0.14.0` |
| **from-password-file** | `string` | `""` | file to read the source repository password from (default: $RESTIC\_FROM\_PASSWORD\_FILE). `restic >= 0.14.0` |
| **from-repository** | `string` | `""` | source repository to copy chunker parameters from (default: $RESTIC\_FROM\_REPOSITORY). `restic >= 0.14.0` |
| **from-repository-file** | `string` | `""` | file from which to read the source repository location to copy chunker parameters from (default: $RESTIC\_FROM\_REPOSITORY\_FILE). `restic >= 0.14.0` |
| ~~key-hint2~~ | `string` | `""` | key ID of key to try decrypting the secondary repository first (default: $RESTIC\_KEY\_HINT2). `restic >= 0.10.0 < 0.14.0` |
| ~~password-command2~~ | `string` | `""` | shell command to obtain the secondary repository password from (default: $RESTIC\_PASSWORD\_COMMAND2). `restic >= 0.10.0 < 0.14.0` |
| ~~password-file2~~ | `string` | `""` | file to read the secondary repository password from (default: $RESTIC\_PASSWORD\_FILE2). `restic >= 0.10.0 < 0.14.0` |
| ~~repo2~~ | `string` | `""` | secondary repository to copy chunker parameters from (default: $RESTIC\_REPOSITORY2). `restic >= 0.10.0 < 0.14.0` |
| ~~repository-file2~~ | `string` | `""` | file from which to read the secondary repository location to copy chunker parameters from (default: $RESTIC\_REPOSITORY\_FILE2). `restic >= 0.13.0 < 0.14.0` |
| **repository-version** | `string` | `"stable"` | repository format version to use, allowed values are a format version, ’latest’ and ‘stable’. `restic >= 0.14.0` |

Tip

Flags declared for the **restic** command line in section can be overridden in this section.