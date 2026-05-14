---
title: resticprofile
source: https://creativeprojects.github.io/resticprofile/
---

**resticprofile** bridges the gap between a configuration file and restic backup. Although creating a configuration file for restic has been [discussed](https://github.com/restic/restic/issues/16), it remains a low priority.

With resticprofile:

- No need to remember command parameters and environment variables
- Create multiple profiles in one configuration file
- Profiles can inherit options from other profiles
- Run the forget command before or after a backup (in a section called *retention*)
- Check a repository before or after a backup
- Create groups of profiles to run sequentially
- Run [shell commands](https://creativeprojects.github.io/resticprofile/configuration/run_hooks/index.html) before or after running a profile, useful for mounting and unmounting backup disks
- Run a [shell command](https://creativeprojects.github.io/resticprofile/configuration/run_hooks/index.html) if an error occurs
- Send a backup stream via *stdin*
- Start restic at different [priorities](https://creativeprojects.github.io/resticprofile/configuration/priority/index.html) (Priority Class in Windows, *nice* in Unix, and/or *ionice* in Linux)
- Check for [enough memory](https://creativeprojects.github.io/resticprofile/usage/memory/index.html) before starting a backup
- Generate cryptographically secure random keys for a restic [key file](https://creativeprojects.github.io/resticprofile/usage/keyfile/index.html)
- Easily [schedule](https://creativeprojects.github.io/resticprofile/schedules/index.html) backups, retentions, and checks (supports *systemd*, *crond*, *launchd*, and *Windows Task Scheduler*)
- Generate a simple [status file](https://creativeprojects.github.io/resticprofile/monitoring/status/index.html) for monitoring software to ensure backups are running smoothly
- Use [template syntax](https://creativeprojects.github.io/resticprofile/configuration/templates/index.html) in your configuration file
- Automatically clear [stale locks](https://creativeprojects.github.io/resticprofile/usage/locks/index.html)
- Export a [prometheus](https://creativeprojects.github.io/resticprofile/monitoring/prometheus/index.html) file after a backup or send the report to a push gateway
- Run shell commands in the background when non-fatal errors are detected
- Send messages to [HTTP hooks](https://creativeprojects.github.io/resticprofile/configuration/http_hooks/index.html) before, after a successful or failed job (backup, forget, check, prune, copy)
- Automatically [initialize the secondary repository](https://creativeprojects.github.io/resticprofile/configuration/copy/index.html) using the `copy-chunker-params` flag
- Send resticprofile [logs](https://creativeprojects.github.io/resticprofile/configuration/logs/index.html) to a syslog server
- Prevent the system from [idle sleeping](https://creativeprojects.github.io/resticprofile/configuration/sleep/index.html)
- View help for both restic and resticprofile via the `help` command or `-h` flag
- Avoid scheduling a job when the system is on battery
- **\[new for v0.29.0\]** Schedule a group of profiles (configuration `v2` only)

The configuration file supports various formats:

- [TOML](https://github.com/toml-lang/toml): files with extensions *.toml* and *.conf* (for compatibility with versions before 0.6.0)
- [JSON](https://en.wikipedia.org/wiki/JSON): files with extension *.json*
- [YAML](https://en.wikipedia.org/wiki/YAML): files with extension *.yaml*
- [HCL](https://github.com/hashicorp/hcl): files with extension *.hcl*