---
title: MB Term Meta - Meta Box Documentation
source: https://docs.metabox.io/extensions/mb-term-meta/
version: 5.12.0
fetched: 2026-05-11
---

MB Term Meta helps you to add custom fields to taxonomies.

![category custom fields](https://imgur.elightup.com/bSykYdo.png)

## Settings

Creating custom meta boxes for taxonomies is similar to posts. The only difference is you need to specify `taxonomies` settings which the meta box will be added to:

```php
add_filter( 'rwmb_meta_boxes', function ( $meta_boxes ) {
    $meta_boxes[] = [
        'title'      => 'Standard Fields',
        'taxonomies' => 'category', // List of taxonomies. Array or comma-separated string.

        'fields' => [
            [
                'name' => 'Featured?',
                'id'   => 'featured',
                'type' => 'checkbox',
            ],
            [
                'name' => 'Featured Content',
                'id'   => 'featured_content',
                'type' => 'wysiwyg',
            ],
            [
                'name' => 'Featured Image',
                'id'   => 'image_advanced',
                'type' => 'image_advanced',
            ],
            [
                'name' => 'Color',
                'id'   => 'color',
                'type' => 'color',
            ],
        ],
    ];
    return $meta_boxes;
} );
```

## Data

WordPress provides an identical way to store values in the meta tables for post / term / user. This extension utilizes that API and stores field value in the term meta exactly like post meta.

## Getting field value

You're able to use helper function [rwmb\_meta()](../functions/rwmb-meta.md) to get field value for terms.

```php
$term_id = get_queried_object_id();
$value = rwmb_meta( $field_id, ['object_type' => 'term'], $term_id );
echo $value;
```

> [!-info] -info
> info
> 
> - In the 2nd parameter, you need to pass `'object_type' => 'term'`, and
> - The last parameter is the term ID. To get the ID of the the current category/term page, please use the function `get_queried_object_id()`.

Other parameters are the same as for post. Please see [this documentation](../displaying-fields-with-code.md) for details.

> [!-warning] -warning
> warning
> 
> It requires the extension version 1.1+ to use the helper function. If you're using an older version, please [update now](../updates.md).

## FAQ

> [!-info] -info
> How to output term meta in MB Views?
> 
> Please use this code to output term meta in a view
> 
> `{% set custom_field = mb.rwmb_meta( 'field_id', { object_type: 'term' }, term_id ) %} {{ custom_field }}`
> 
> [\# Link to this question](#how-to-output-term-meta-in-mb-views)
