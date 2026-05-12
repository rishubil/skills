# rishubil/skills

A personal collection of Claude [Agent Skills](https://agentskills.io). Can be registered as a Claude Code plugin marketplace for easy installation.

## Repository Structure

```
.
├── .claude-plugin/
│   └── marketplace.json   # Marketplace definition (one plugin per skill)
├── skills/                # Skill collection (each folder is one skill)
│   └── <skill-name>/
│       └── SKILL.md
├── LICENSE
└── README.md
```

A skill only needs a `skills/<skill-name>/SKILL.md` file to work. You can freely add scripts or auxiliary files to the same folder as needed.

This marketplace registers **one skill as one plugin**, so users can pick and install only the skills they need.

> **When adding a new skill, add an entry to the `plugins` array in `.claude-plugin/marketplace.json` and register the `./skills/<skill-name>` path in that entry's `skills` field.**

## Available Plugins

| Plugin | Description |
| --- | --- |
| `shell-script` | Best practices and error handling patterns for writing Bash shell scripts. |
| `fetch-docs` | Download web-based development documentation as clean markdown files, preserving the directory structure. |
| `monkey-c` | Develop Garmin Connect IQ apps in Monkey C (Watch Face, Device App, Widget, Data Field, etc.). |
| `wordpress-meta-box` | WordPress Meta Box plugin — custom fields, meta boxes, CPTs, and the full Meta Box API. |
| `wordpress-classic-theme` | WordPress classic (PHP) themes — template hierarchy, The Loop, widgets, Customizer API, etc. (block themes excluded) |
| `commit` | Write commit messages in Conventional Commits format with a body explaining *why* the change was made. |

## Using in Claude Code

First, add the marketplace:

```
/plugin marketplace add rishubil/skills
```

Then install individual plugins:

```
/plugin install <plugin-name>@rishubil-skills
```

Example:

```
/plugin install shell-script@rishubil-skills
/plugin install commit@rishubil-skills
```

After installation, mention the skill name or description and Claude will automatically use the relevant skill.

## Skills from Other Repositories

In addition to this repository, the following external skills are also used.

| Marketplace | Plugin | Install Command |
|---|---|---|
| `forrestchang/andrej-karpathy-skills` | `andrej-karpathy-skills` | `/plugin marketplace add forrestchang/andrej-karpathy-skills` → `/plugin install andrej-karpathy-skills@karpathy-skills` |

## References

- [Agent Skills official spec](https://agentskills.io)
- [Anthropic's example skills repository](https://github.com/anthropics/skills)
- [Guide to creating custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
