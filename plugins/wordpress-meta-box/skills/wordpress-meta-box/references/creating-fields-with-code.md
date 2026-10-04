---
title: Creating fields with code - Meta Box Documentation
source: https://docs.metabox.io/creating-fields-with-code/
version: 5.15.1
fetched: 2026-10-04
---

Use code to create custom fields if you want to keep everything in your themes or plugins. This lets you reuse them across websites and put them under version control like Git.

## Registering custom fields with PHP

To create custom fields, use the `rwmb_meta_boxes` filter to register field groups. This filter accepts one parameter - the array of field groups:

```php
add_filter( 'rwmb_meta_boxes', function ( $meta_boxes ) {
    $meta_boxes[] = [
        'title'      => 'Event details',
        'post_types' => 'event',
        'fields'     => [
            [
                'name' => 'Date and time',
                'id'   => 'datetime',
                'type' => 'datetime',
            ],
            [
                'name' => 'Location',
                'id'   => 'location',
                'type' => 'text',
            ],
            [
                'name'          => 'Map',
                'id'            => 'map',
                'type'          => 'osm',
                'address_field' => 'location',
            ],
        ],
    ];

    // Add more field groups if you want
    // $meta_boxes[] = ...

    return $meta_boxes;
} );
```

Each field group has settings and a list of fields, covered below.

## Field group settings

Each field group has settings for location or appearance:

| Name | Description |
| --- | --- |
| `id` | ID, must be unique. Optional. If it is absent, it will be generated from the title. We recommend specifying the ID explicitly to avoid issues when the title contains non-ASCII characters (e.g. Chinese, Japanese, Korean, or Vietnamese). |
| `title` | The field group title. Required. |
| `post_types` | Custom post types for the field group. Can be a string or an array of slugs. Must be in lowercase (like the slug). Optional. Default: `post`. |
| `context` | Where the field group is displayed. See below for a list of field group contexts. Optional. |
| `style` | Keep the default WordPress field group style (`default`) or remove the wrapper box and display fields without styling (`seamless`). |
| `closed` | Whether to collapse the field group when the page loads? Optional. Default: `false`. |
| `priority` | Priority within the context where the box is displayed (`high` or `low`). Optional. Default: `high`. |
| `default_hidden` | Hide the field group by default (`true` or `false`)? Toggle this with the checkbox in screen Help (top right). Optional. Default `false`. |
| `autosave` | Auto save the custom fields' values (like post content and title)? Optional. Default: `false`. |
| `media_modal` | Add custom fields to media modal when viewing/editing an attachment. Works only when `post_types` is or contains `attachment`. Optional. Default `false`. |
| `class` | Custom CSS class for the field group wrapper. Optional. |

> [!-info] -info
> Media modal limitation
> 
> Only simple fields such as text, select, radio, and checkbox work in the media modal. Fields that require custom JavaScript do not work.

### Contexts

The plugin supports the following contexts (locations) where a field group can appear:

| Name | Description |
| --- | --- |
| `normal` | Below the post editor. This is the default value. |
| `advanced` | Below the `normal` section. |
| `side` | On the right sidebar. |
| `form_top` | Top of the post form, before the post title |
| `after_title` | After post title |
| `after_editor` | After the post content editor, but before `normal` section |
| `before_permalink` | Before permalink |

> [!-warning] -warning
> Block editor
> 
> The block editor editor supports only `normal` and `side` contexts. Other contexts do not work.

## Fields

Add fields to a field group via the `fields` key. Each field is an array of settings.

Meta Box supports more than 40 field types. They share some common settings but also offer unique settings per field type.

### Field types

Know the field type and how it works before adding a field. This helps you choose the right type for your data.

The list below shows all supported field types in alphabetical order with a brief description. The field type key is used for code reference. See the [Field types](fields/index.md) menu for details on how they look and how to use them.

### Field settings

Each field has settings for where and how data is loaded and saved. All fields share common settings. Each field type also has unique settings. Extension settings are explained in each extension docs.

Below is the list of settings with a brief description. The keys are for reference in code.

> [!-success] -success
> Field ID prefix
> 
> You can add a prefix to field IDs to prevent using the same ID with other scripts. If you want to hide the fields in the default WordPress **Custom Fields** meta box, use underscore (`_`) as the prefix.

### Field-specific settings

In addition to common settings, each field type has its own settings. See the left menu for details on each field type.

> [!-success] -success
> Code examples
> 
> To save time, we have prepared code examples in the [Meta Box Code Snippet Library](https://github.com/wpmetabox/library/).

### Shorthand syntax

For **text** field type, you can omit the `type` settings, like this:

```php
add_filter( 'rwmb_meta_boxes', function ( $meta_boxes ) {
    $meta_boxes[] = [
        'title'      => 'Event details',
        'post_types' => 'event',
        'fields'     => [
            [
                'name' => 'Date and time',
                'id'   => 'datetime',
                'type' => 'datetime',
            ],
            [
                'name' => 'Location',
                'id'   => 'location',
            ],
            [
                'name'          => 'Map',
                'id'            => 'map',
                'type'          => 'osm',
                'address_field' => 'location',
            ],
        ],
    ];

    return $meta_boxes;
} );
```

And if the `id` of the field can be auto-generated from the field name, you can omit it and **define the field as a simple string**:

```php
add_filter( 'rwmb_meta_boxes', function ( $meta_boxes ) {
    $meta_boxes[] = [
        'title'      => 'Event details',
        'post_types' => 'event',
        'fields'     => [
            [
                'name' => 'Date and time',
                'id'   => 'datetime',
                'type' => 'datetime',
            ],
            'Location',
            [
                'name'          => 'Map',
                'id'            => 'map',
                'type'          => 'osm',
                'address_field' => 'location',
            ],
        ],
    ];

    return $meta_boxes;
} );
```

## Video tutorial

This video shows all field types and field settings:

## FAQ

> [!-info] -info
> Why does not my default value work?
> 
> The `std` value works only if the field group has not been saved before. This applies to all fields in the group, not just the field with `std`. If any field has a value, `std` does not work for other fields, even new ones you add.
> 
> Examples:
> 
> When you create a new post, no fields have values. `std` works for all fields.
> 
> When you edit an existing post with a field group, some fields may have values. Then `std` does not work for all fields. If you add a new field to the field group, `std` does not work for that field, even if it has no value. The field group was saved before.
> 
> [\# Link to this question](#why-does-not-my-default-value-work)

> [!-info] -info
> Why does not my context work?
> 
> The context may not work if you dragged and dropped field groups to reorder them. WordPress saves the position and uses it instead of the `context` value. The order is saved in user meta `meta-box-order_{screen id}`:
> 
> ![meta box order](https://imgur.elightup.com/A7bkxT9.png)
> 
> To fix this, delete the user meta from the database. The context will work again.
> 
> [\# Link to this question](#why-does-not-my-context-work)
