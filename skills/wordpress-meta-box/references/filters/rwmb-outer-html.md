---
title: rwmb_outer_html - Meta Box Documentation
source: https://docs.metabox.io/filters/rwmb-outer-html/
version: 5.12.0
fetched: 2026-05-11
---

This filter is used to change the outer HTML output of a field. Outer HTML is the surrounding div (the most outside) of the field.

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

This filter is used to change the **field outer HTML**, e.g. the wrapper div of everything for the field.

```php
apply_filters( 'rwmb_outer_html', $html, $field, $value );
```

This filter accepts 3 parameters:

| Name | Description |
| --- | --- |
| `$html` | The outer HTML output of a field |
| `$field` | Field settings |
| `$value` | Field value |

This filter has variations:

- `rwmb_outer_html`: apply to all fields
- `rwmb_{$field_type}_outer_html`: apply to fields with a specific type
- `rwmb_{$field_id}_outer_html`: apply to a the field with a specific id
