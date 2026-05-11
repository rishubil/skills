---
title: Creating fields with code - Meta Box Documentation
source: https://docs.metabox.io/creating-fields-with-code/
---

Creating custom fields with code is suitable if you want to keep everything in your themes or plugins. This way, you can re-use them in many websites and put them under a version control like Git.

## Registering custom fields with PHP

To create custom fields, you'll need to use the filter `rwmb_meta_boxes` to register field groups. This filter accepts one parameter - the array of field groups:

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

Each field group has several settings and a list of fields, which we'll cover below.

## Field group settings

Each field group has several settings for the location or appearance. Please see the list below:

| Name | Description |
| --- | --- |
| `id` | ID, must be unique. Optional. If it's absent, it will be generated from the title. |
| `title` | The field group title. Required. |
| `post_types` | Custom post types which the field group is for. It can be a string or an array of slugs. Must be in lowercase (like the slug). Optional. Default: `post`. |
| `context` | Where the field group is displayed. See below for a list of field group contexts. Optional. |
| `style` | Whether to keep the default WordPress field group style (`default`) or remove the wrapper box and display the fields seamlessly (`seamless`). |
| `closed` | Whether to collapse the field group when the page loads? Optional. Default: `false`. |
| `priority` | Priority within the context where the box is displayed (`high` or `low`). Optional. Default: `high`. |
| `default_hidden` | Hide the field group by default (`true` or `false`)? The field group can be toggled using the checkbox option in screen Help (on the top right). Optional. Default `false`. |
| `autosave` | Auto save the custom fields' values (like post content and title)? Optional. Default: `false`. |
| `media_modal` | Add custom fields to media modal when viewing/editing an attachment. Works only when `post_types` is or contains `attachment`. Optional. Default `false`. |
| `class` | Custom CSS class for the field group wrapper. Optional. |

> [!-info] -info
> Media modal limitation
> 
> Only simple fields such as text, select, radio, checkbox work in the media modal. Other fields that require custom JavaScript don't work.

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
> Gutenberg
> 
> Gutenberg editor only supports `normal` and `side` contexts. Other extra contexts are not supported.

## Fields

Fields are added to a field group via the key `fields`. Each field is an array of settings.

Meta Box supports more than 40 field types. They share some common settings but also offer unique settings per field type.

### Field types

When adding a field, you need to know what type it is and how it works. Understanding that helps you choose the right type of field and, therefore, the right type of data that you want to add to your posts.

Below is the list of supported field types in alphabet order with a brief description. The field type key is used for reference in code. For how do they look like and how to use them, please see details in the [Field types](https://docs.metabox.io/fields/) menu.

### Field settings

Each field contains settings to determine where and how data is loaded and saved. All fields share some common settings, but also offer unique settings per field type. There are also settings from extensions which are explained on each extension docs.

Below is the list of settings with a brief description. The keys are for reference in code.

> [!-success] -success
> Field ID prefix
> 
> You can add a prefix to field IDs to prevent from using the same ID with other scripts. If you want to hide the fields in the default WordPress **Custom Fields** meta box, use underscore (`_`) as the prefix.

### Field-specific settings

Besides all common settings, each field type can have its own settings. Please see more details for each field type on the left menu.

> [!-success] -success
> Code examples
> 
> To save time read and write settings for fields, we've already prepared some code examples that you can get from [Meta Box Code Snippet Library](https://github.com/wpmetabox/library/).

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

This video shows you all the field types and field settings:

## FAQ

> [!-info] -info
> Why does not my default value work?
> 
> The mechanism of `std` in Meta Box works only if the **field group has not been saved before**. It means all fields in that field group, not just the specific field that you set the `std` for. So if there's any field that already has value, then `std` won't work for other fields, even new fields you've just added.
> 
> Examples:
> 
> When you create a new post, then no fields have values (of course), then `std` works for all fields.
> 
> When you edit an existing post that has a field group, then some fields might have values. Therefore, `std` doesn't work for all fields. In this case, if you edit the field group and add a new field, `std` still doesn't work for that new field (even it has no value before), because the field group has been saved before.
> 
> [\# Link to this question](#why-does-not-my-default-value-work)

> [!-info] -info
> Why does not my context work?
> 
> There are some situations that the context doesn't work as expected. That is probably because you have dragged and dropped the field groups to reorder them? If you have, then WordPress will save the position/location of them and use the saved position instead of the value in the `context` parameter. The order of field groups is saved in the user meta `meta-box-order_{screen id}` as follows:
> 
> ![meta box order](https://imgur.elightup.com/A7bkxT9.png)
> 
> In this case, deleting this user meta from the database will make the context work again.
> 
> [\# Link to this question](#why-does-not-my-context-work)
