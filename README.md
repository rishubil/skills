# rishubil/skills

A personal collection of Claude [Agent Skills](https://agentskills.io). Can be registered as a Claude Code plugin marketplace for easy installation.

## Repository Structure

```
.
├── .claude-plugin/
│   └── marketplace.json        # Marketplace definition (one plugin per skill)
├── plugins/                    # Plugin collection (each folder is one plugin root)
│   └── <plugin-name>/
│       ├── skills/
│       │   └── <skill-name>/
│       │       └── SKILL.md
│       ├── hooks/              # (optional) plugin-scoped hooks
│       │   └── hooks.json
│       └── scripts/            # (optional) plugin scripts
├── LICENSE
├── NOTICE
└── README.md
```

Each plugin lives in its own directory under `plugins/`, so hooks and other components are scoped to that plugin only.

This marketplace registers **one skill as one plugin**, so users can pick and install only the skills they need.

> **When adding a new skill, create `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` and add an entry to `.claude-plugin/marketplace.json` with `source: "./plugins/<plugin-name>"`.**

## Available Plugins

| Plugin | Description |
| --- | --- |
| `shell-script` | Best practices and error handling patterns for writing Bash shell scripts. |
| `fetch-docs` | Download web-based development documentation as clean markdown files, preserving the directory structure. |
| `monkey-c` | Develop Garmin Connect IQ apps in Monkey C (Watch Face, Device App, Widget, Data Field, etc.). |
| `wordpress-meta-box` | WordPress Meta Box plugin — custom fields, meta boxes, CPTs, and the full Meta Box API. |
| `wordpress-classic-theme` | WordPress classic (PHP) themes — template hierarchy, The Loop, widgets, Customizer API, etc. (block themes excluded) |
| `commit` | Write commit messages in Conventional Commits format with a body explaining *why* the change was made. |
| `plan-review` | Structured, opinionated review of an implementation plan — architecture, code quality, tests, performance, and debuggability. |
| `resticprofile` | resticprofile configuration profile manager for restic — profile config files (TOML/YAML/JSON/HCL), commands, and scheduling. |
| `gh-readonly` | PreToolUse hook that blocks direct read-only `gh` calls and redirects them to an allowlist-based wrapper. |
| `skill-eval-hook` | UserPromptSubmit hook that forces mandatory skill evaluation before every task — Claude must assess each available skill and activate relevant ones before implementation. |
| `uv` | PreToolUse hook that blocks direct `python`/`pip` invocations and `pip install` via uv, enforcing `uv run` and `uv add` in uv-managed Python projects. |
| `python-lsp-uvx-ty` | LSP plugin that registers `uvx ty server` as a Python language server in Claude Code — real-time diagnostics and code intelligence for `.py` / `.pyi` files. |
| `landing-protocol-creator` | Analyze the current project's tech stack and generate a project-specific `landing-protocol` skill at `.claude/skills/landing-protocol/SKILL.md`. |
| `check-bullshit` | Analyze a URL or block of text for bullshit using the 13-technique BullshitBench diagnostic framework. |

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
/plugin install gh-readonly@rishubil-skills
```

After installation, mention the skill name or description and Claude will automatically use the relevant skill.

### Auto-install via `.claude/settings.json`

To prompt every team member (or yourself, across projects) to install this marketplace automatically when the project folder is trusted, add it to `.claude/settings.json`. See [Require marketplaces for your team](https://code.claude.com/docs/en/plugin-marketplaces#require-marketplaces-for-your-team) for details.

```json
{
  "extraKnownMarketplaces": {
    "rishubil-skills": {
      "source": {
        "source": "github",
        "repo": "rishubil/skills"
      }
    }
  }
}
```

You can also enable specific plugins by default with `enabledPlugins`:

```json
{
  "extraKnownMarketplaces": {
    "rishubil-skills": {
      "source": {
        "source": "github",
        "repo": "rishubil/skills"
      }
    }
  },
  "enabledPlugins": {
    "shell-script@rishubil-skills": true,
    "commit@rishubil-skills": true
  }
}
```

## Skills from Other Repositories

In addition to this repository, the following external skills are also used.

| Marketplace | Plugin | Install Command |
|---|---|---|
| `forrestchang/andrej-karpathy-skills` | `andrej-karpathy-skills` | `/plugin marketplace add forrestchang/andrej-karpathy-skills` → `/plugin install andrej-karpathy-skills@karpathy-skills` |

## License

The original work in this repository — each skill's `SKILL.md`, the
scripts under `plugins/*/scripts/`, the marketplace manifest, and the
top-level documentation — is released under the
[MIT License](./LICENSE).

Some skills additionally cache reference documentation that was
fetched from third-party sources. **Those cached files are NOT covered
by the MIT License above**; they remain under the copyright and
license of their original authors. See [`NOTICE`](./NOTICE) for the
full list, and the `NOTICE.md` at each affected skill's top level for
per-skill details.

In short:

| Path | License |
| --- | --- |
| Everything else | MIT (this repository) |
| `plugins/wordpress-classic-theme/skills/wordpress-classic-theme/references/**` | GPL-2.0-or-later (WordPress contributors) |
| `plugins/monkey-c/skills/monkey-c/{overview,references,api-docs}/**` | All rights reserved — (c) Garmin Ltd. (local reference cache only) |
| `plugins/wordpress-meta-box/skills/wordpress-meta-box/references/**` | All rights reserved — (c) MetaBox.io / eLightUp (local reference cache only) |
| `plugins/resticprofile/skills/resticprofile/references/**` | MIT License — (c) resticprofile contributors (local reference cache) |

If you are a rights holder for any of the cached third-party content
and wish it removed, please open an issue.

## CLAUDE.md Template

[`CLAUDE.md.template`](./CLAUDE.md.template) is a starting point for your project's `CLAUDE.md`. It includes recommended agent instructions such as:

- Keeping responses honest and direct
- Red-Green TDD workflow (find tests → red → green → verify)
- Always reading documentation before exploring code

Copy it to your project root and rename it to `CLAUDE.md`, then adjust to fit your project's needs.

## References

- [Agent Skills official spec](https://agentskills.io)
- [Anthropic's example skills repository](https://github.com/anthropics/skills)
- [Guide to creating custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
