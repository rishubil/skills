---
title: Section Groups :: resticprofile
source: https://creativeprojects.github.io/resticprofile/reference/groups/
---

## Section Groups

### Section groups

Config file format v1 uses a simplified groups section. Every named item below `groups` maps to one or more `profile` names (list of strings).

From file format v2, every named item in the groups section is configuration structure following the format described below (see [Configuration v2](https://creativeprojects.github.io/resticprofile/configuration/v2/) for details):

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| **continue-on-error** | `true` / `false` | `auto` | Continue with the next profile on a failure, overrides “global.group-continue-on-error” |
| **description** | `string` |  | Describe the group |
| **profiles** | one or more `strings` |  | Names of the profiles belonging to this group |
| **schedules** | `key` => nested *[ScheduleConfig](https://creativeprojects.github.io/resticprofile/reference/nested/scheduleconfig)* |  | Allows to run the group on schedule for the specified command name (backup, copy, check, forget, prune) |