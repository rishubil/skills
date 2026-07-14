# wordpress-meta-box

A Claude Code plugin for developing with the [Meta Box](https://metabox.io/) WordPress plugin — custom fields, meta boxes, and custom post types.

## What it does

Provides specialist knowledge for:

- Creating custom fields and meta boxes via code or the GUI builder (MB Builder)
- Custom post types (CPTs) and taxonomies
- The full Meta Box API — field settings, actions, filters, and functions
- MB Views (Twig-based template rendering for fields)
- Extensions: MB Settings Page, MB Blocks, MB Relationships, and more

Bundled with a local cache of the official Meta Box documentation.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install wordpress-meta-box@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install wordpress-meta-box@rishubil-skills --scope project
```

## Usage

Triggers automatically when:

- Working with Meta Box code (`rwmb_*` functions, field group arrays, `add_filter('rwmb_meta_boxes', ...)`)
- Asking about custom fields, meta boxes, or the Meta Box API in a WordPress context

## License note

The bundled reference documentation is cached from the official Meta Box docs and remains under the copyright of MetaBox.io / eLightUp. See [`skills/wordpress-meta-box/NOTICE.md`](./skills/wordpress-meta-box/NOTICE.md) for details. The MIT License of this repository does **not** apply to those cached files.
