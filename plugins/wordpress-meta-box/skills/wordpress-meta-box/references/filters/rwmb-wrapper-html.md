---
title: rwmb_wrapper_html - Meta Box Documentation
source: https://docs.metabox.io/filters/rwmb-wrapper-html/
version: 5.12.0
fetched: 2026-05-11
---

This filter is used to change the wrapper HTML of a field, e.g. the HTML content **inside the `<div class="rwmb-field..."></div>`**.

When outputting a field, it will have the following HTML:

```html
<!-- Start: field outer HTML -->
{$field['before']}
<div class="rwmb-field rwmb-{$field['type']}-wrapper {$field['class']} required">

    <!-- Start: field wrapper HTML -->

        <!-- Start: field begin HTML -->
        <div class="rwmb-label" id="{$field['id]}-label">
            <label for="{$field['id']}">
                {$field['name']}
                <span class="rwmb-required">*</span>
            </label>
            <p id="{$field['id']}-label-description" class="description">{$field['label_description']}</p>
        </div>
        <div class="rwmb-input">
        <!-- End: field begin HTML -->

            <!-- Field input HTML -->

        <!-- Start: field end HTML -->
            {$add_clone_button}
            <p id="{$field['id']}-description" class="description">{$field['desc']}</p>
        </div>
        <!-- End: field end HTML -->

    <!-- End: field wrapper HTML -->

</div>
{$field['after']}
<!-- End: field outer HTML -->
```

Syntax:

```php
apply_filters( 'rwmb_wrapper_html', $html, $field, $meta );
```

This filter accepts 3 parameters:

| Name | Description |
| --- | --- |
| `$html` | The wrapper HTML of the field |
| `$field` | Field settings |
| `$meta` | Field value |

This filter has variations:

- `rwmb_wrapper_html`: apply to all fields
- `rwmb_{$field_type}_wrapper_html`: apply to fields with a specific type
- `rwmb_{$field_id}_wrapper_html`: apply to a the field with a specific id
