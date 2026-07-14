# wordpress-classic-theme

A Claude Code plugin for developing WordPress classic (PHP-based) themes.

## What it does

Provides specialist knowledge for creating, extending, and debugging classic WordPress themes. Covers:

| Topic | Description |
|---|---|
| **Template hierarchy** | Rules that determine which template file handles each URL |
| **The Loop** | Core pattern for fetching and rendering posts |
| **Template tags** | Output functions like `the_title()`, `the_content()`, `get_template_part()` |
| **Theme functions** | Hooks and features registered in `functions.php` |
| **Conditional tags** | Branching functions like `is_single()`, `is_archive()` |
| **Sidebars & widgets** | Registering widget areas and using the Widget API |
| **Navigation menus** | Registering and rendering menu locations |
| **Customizer API** | Theme options via `WP_Customize_Manager` |

Bundled with a local cache of the official WordPress theme developer documentation.

> **Does not cover block themes (Full Site Editing / FSE).** For block themes, a separate plugin would be needed.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install wordpress-classic-theme@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install wordpress-classic-theme@rishubil-skills --scope project
```

## Usage

Triggers automatically when:

- Working on classic WordPress theme files (`functions.php`, `index.php`, `single.php`, etc.)
- Asking about template hierarchy, The Loop, Customizer, widgets, or theme functions

## License note

The bundled reference documentation is cached from the WordPress developer docs and remains under GPL-2.0-or-later (WordPress contributors). See [`skills/wordpress-classic-theme/NOTICE.md`](./skills/wordpress-classic-theme/NOTICE.md) for details. The MIT License of this repository does **not** apply to those cached files.
