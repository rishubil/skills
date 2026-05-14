---
title: Windows Task Scheduler :: resticprofile
source: https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/
---

## Windows Task Scheduler

## Minimum version supported

Windows 10 is the minimum version supported for scheduling.

## Elevated mode

If your schedule profile has the permission set to `system`, resticprofile needs to run in elevated mode to set up the schedules.

Generally, you don’t need to worry about this: resticprofile will restart itself in elevated mode. You’ll see a popup window asking for elevated privileges.

### resticprofile is blocked from restarting in elevated mode

[![Unwanted software](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/unwanted_my_ass.png)](#R-image-d96d4b638fd3a4e4e4d802fbb7e9fae3) ![Unwanted software](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/unwanted_my_ass.png)

I can’t prevent this without buying a developer certificate. If you know any free or cheap certificate for open-source software, please let me know.

#### Solution

You’ll need to start an elevated shell yourself.

- Right-click on `Command Prompt`, `Windows Terminal`, or `Windows Powershell` (choose your favorite)
- Click on `Run as administrator`

[![Start elevated command prompt](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/runas.png)](#R-image-9af96363203c5aa989bd36d6acfecccf) ![Start elevated command prompt](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/runas.png)

It’s easy to spot a terminal window opened with Administrator privileges:

[![Administrator prefix](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/administrator.png)](#R-image-c34e0f43647d9246a05ce3ad263db9f4) ![Administrator prefix](https://creativeprojects.github.io/resticprofile/schedules/task_scheduler/administrator.png)

Important

Running the schedule command might cause Windows to delete *resticprofile.exe*, treating it as a threat.

## Start when available

If your computer might be asleep or off during a scheduled backup time, you can enable `schedule-start-when-available` to run the task as soon as the computer becomes available.

```yaml
profile:
  backup:
    schedule: "03:00"
    schedule-start-when-available: true
```

This sets the “Start the task as soon as possible after a scheduled start is missed” option in Windows Task Scheduler.