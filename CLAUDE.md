# CLAUDE.md

This repository is a personal collection of Agent Skills registered as a Claude Code plugin marketplace (`rishubil-skills`). Follow these rules when working here.

## Repository Structure

- `.claude-plugin/marketplace.json` — Marketplace manifest. Defines plugin entries and the skill paths included in each plugin.
- `skills/<skill-name>/SKILL.md` — Individual skill. Each folder is one skill; `SKILL.md` consists of YAML frontmatter (`name`, `description`) and body instructions.
- Scripts and auxiliary resources can be placed freely under `skills/<skill-name>/`.

## Plugin Principles

- This marketplace follows a **one plugin per skill** principle, so users can install only the skills they need.
- The plugin name (`plugins[].name`) must match the folder name of the skill it contains.
- Add a new plugin entry for each new skill until there is a clear reason to bundle multiple skills together.

## Adding a New Skill

1. Create `skills/<new-skill-name>/SKILL.md`.
   - `name` must match the folder name, using only lowercase letters and hyphens.
   - `description` should convey both "what it does" and "when to use it" in one or two sentences.
2. **You must** add a new plugin entry to the `plugins` array in `.claude-plugin/marketplace.json`.
   - `name` matches the skill folder name.
   - `description` should be concise — roughly one sentence in English.
   - `source` is `"./"`, `strict` is `false`.
   - Add `./skills/<new-skill-name>` to the `skills` array.
   - Omitting this will prevent installation through the marketplace.
3. If needed, add a new row to the "Available Plugins" table in `README.md`.

## Modifying or Deleting a Skill

- If you delete or rename a skill folder, sync the corresponding plugin entry (or its `skills` array) in `marketplace.json`, and update the plugin list in `README.md`.
- The `name` field in `SKILL.md` must match the folder name.

## Third-Party Reference Content

Some skills bundle a local cache of upstream documentation (e.g.
`skills/monkey-c/{overview,references,api-docs}/`,
`skills/wordpress-classic-theme/references/`,
`skills/wordpress-meta-box/references/`). Those files are owned by
their original authors and are not relicensed by this repository.

When adding or refreshing such content:

1. If the skill does not yet have a `NOTICE.md` at its top level
   (`skills/<skill-name>/NOTICE.md`), create one that states the
   source, copyright, license, the affected subdirectories, and that
   the repository's MIT License does not apply to the cached files.
   One NOTICE.md per skill — do not place a separate copy inside
   each subdirectory.
2. Update the root `NOTICE` and the "License" section of `README.md`
   when a new third-party source is introduced.
3. Never overwrite or remove the upstream copyright/license metadata
   without consulting the user.

## Committing and Pushing

- Use the branch specified by the user; do not push directly to `main` without permission.
- Keep commit messages concise — one or two sentences explaining *why* the change was made.

## References

- [Agent Skills spec](https://agentskills.io)
- [Anthropic example skills repository](https://github.com/anthropics/skills)
