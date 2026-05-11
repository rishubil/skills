---
title: rwmb_end_html - Meta Box Documentation
source: https://docs.metabox.io/filters/rwmb-end-html/
---

This filter is similar to [rwmb\_begin\_html](https://docs.metabox.io/filters/rwmb-begin-html/) and is used to change the ending HTML output of a field.

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

The ending HTML for a field looks like this:

```html
{$add_clone_button}
    <p id="{$field['id']}-description" class="description">{$field['desc']}</p>
</div><!-- .rwmb-input -->
```

Syntax:

```php
apply_filters( 'rwmb_end_html', $end, $field, $value );
```

This filter accepts 3 parameters:

| Name | Description |
| --- | --- |
| `$end` | The ending HTML output of the field |
| `$field` | Field settings |
| `$value` | Field value |

This filter has variations:

- `rwmb_end_html`: apply to all fields
- `rwmb_{$field_type}_end_html`: apply to fields with a specific type
- `rwmb_{$field_id}_end_html`: apply to a field with a specific id
