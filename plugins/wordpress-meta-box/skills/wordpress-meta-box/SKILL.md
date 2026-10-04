---
name: wordpress-meta-box
description: Specialist skill for the WordPress Meta Box plugin. Use when implementing custom fields, meta boxes, or custom post types via code or the UI builder, or when looking up the Meta Box API (field settings, actions, filters, and functions).
---

# WordPress Meta Box Development Guide

> Official documentation: https://docs.metabox.io/

Meta Box is a plugin for creating and managing custom fields and meta boxes in WordPress. It supports both code-based configuration and a GUI builder (MB Builder).

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Meta Box** | A group of custom fields inserted into the WordPress editor screen |
| **Field** | An individual input control such as text, image, or date |
| **Field Group** | A container that groups multiple fields (synonymous with meta box) |
| **MB Builder** | A GUI tool for creating field groups without writing code |
| **MB Views** | An extension for rendering fields using Twig templates |

## Basic Usage Patterns

### Registering a Meta Box in Code

```php
add_filter( 'rwmb_meta_boxes', function( $meta_boxes ) {
    $meta_boxes[] = [
        'title'  => 'Event Details',
        'id'     => 'event-details',
        'post_types' => ['event'],
        'fields' => [
            [
                'name' => 'Start Date',
                'id'   => 'start_date',
                'type' => 'date',
            ],
            [
                'name' => 'Location',
                'id'   => 'location',
                'type' => 'text',
            ],
        ],
    ];
    return $meta_boxes;
} );
```

### Outputting Field Values

```php
// Single value
$value = rwmb_meta( 'field_id' );

// Formatted HTML output
rwmb_the_value( 'field_id' );

// Specify a particular post
$value = rwmb_meta( 'field_id', [], $post_id );
```

## Key Field Types

| Type | Purpose |
|------|---------|
| `text`, `textarea` | Text input |
| `number`, `range` | Numeric input |
| `email`, `url`, `password` | Text with format validation |
| `date`, `datetime`, `time` | Date and time pickers |
| `select`, `radio`, `checkbox` | Selection inputs |
| `select_advanced` | Advanced Select2-based selector |
| `image`, `file`, `video`, `audio` | Media uploads |
| `image_advanced` | Multiple image upload |
| `wysiwyg` | TinyMCE editor |
| `oembed` | Media embed URL |
| `color` | Color picker |
| `map`, `osm` | Map fields |
| `post`, `taxonomy`, `user` | WordPress object relationships |
| `group` | Nested field group |

## Local Documentation (consult first)

The `references/` folder in this skill directory contains the full official documentation as markdown files. When checking the API, field options, or actions/filters/functions, **do not open external URLs — Read the local files for accurate information**.

### references/ Directory Structure

```
references/
├── index.md                        # Home (full overview)
├── installation.md                 # Installation and requirements
├── custom-fields.md                # Custom fields overview
├── custom-post-types.md            # Custom post types
├── creating-fields-with-code.md    # Creating fields in code
├── displaying-fields-with-code.md  # Displaying fields in code
├── cloning-fields.md               # Field cloning (repeatable fields)
├── database.md                     # Data storage
├── edit-meta-boxes.md              # Editing meta boxes
├── abilities.md                    # WordPress Abilities API integration
├── block-bindings.md               # Block bindings (field values in core blocks)
├── extensions/                     # Extension plugins
│   └── *.md
├── integrations/                   # Third-party integrations (index.md overview, Polylang, WPML)
│   └── *.md
├── field-settings.md               # Settings common to all field types
├── fields/                         # Detailed guide per field type
│   └── *.md
├── actions/                        # Action hook reference
│   └── rwmb-*.md
├── filters/                        # Filter hook reference
│   └── rwmb-*.md
└── functions/                      # Function reference
    └── *.md
```

### Commonly Referenced Documents

| Topic | File Path |
|-------|-----------|
| Installation | `references/installation.md` |
| Full field type list | `references/fields/index.md` |
| Common field settings | `references/field-settings.md` |
| Image field | `references/fields/image-advanced.md` |
| Date field | `references/fields/date.md` |
| Group field | `references/extensions/meta-box-group.md` |
| Post relationship field | `references/fields/post.md` |
| rwmb_meta() function | `references/functions/rwmb-meta.md` |
| rwmb_the_value() function | `references/functions/rwmb-the-value.md` |
| After-save action | `references/actions/rwmb-after-save-post.md` |

To find documentation, Read the paths above directly or search with `find /home/user/skills/skills/wordpress-meta-box/references -name "*.md" | grep <keyword>`.
