# NOTICE — agent-browser-obscura skill

`SKILL.md` in this directory was written for this repository, but parts of it
are adapted (paraphrased and reorganized, not copied verbatim) from two
Apache-2.0 upstream projects. The adapted portions remain under the Apache
License 2.0; this repository's MIT License does not relicense them.

## vercel-labs/agent-browser

- **Source:** https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/SKILL.md
  and https://agent-browser.dev/engines/obscura
- **Copyright:** (c) Vercel, Inc. and agent-browser contributors
- **License:** Apache License 2.0 — https://github.com/vercel-labs/agent-browser/blob/main/LICENSE
- **Retrieved:** 2026-11-15 (upstream `skills/` at commit `4720bc3`, 2026-11-13)
- **Adapted:** the skill's trigger description, the instruction to load the
  version-matched guide with `agent-browser skills get core`, the list of
  specialized skills, and the Obscura engine's unsupported-option list.

## h4ckf0r0day/obscura

- **Source:** https://github.com/h4ckf0r0day/obscura/blob/main/skills/obscura/SKILL.md
  and https://github.com/h4ckf0r0day/obscura/tree/main/docs
  (`Environment-variables.md`, `Configure-stealth-and-proxies.md`,
  `Persist-cookies-and-storage.md`, `Markdown-extraction.md`)
- **Copyright:** (c) Obscura contributors
- **License:** Apache License 2.0 — https://github.com/h4ckf0r0day/obscura/blob/main/LICENSE
- **Retrieved:** 2026-11-15 (upstream `skills/` at commit `055453c`, 2026-10-03)
- **Adapted:** the description of stealth mode and its fingerprint, the
  `OBSCURA_*` environment variables, `obscura fetch --dump` usage, and the
  list of rendering and Web API limitations.

The measurements and behavior notes in `SKILL.md` (memory use, bot-wall
results, engine relaunch rules, `--restore` and storage behavior, quirks) are
original observations made for this repository with agent-browser 0.43.0 and
Obscura 0.2.7.
