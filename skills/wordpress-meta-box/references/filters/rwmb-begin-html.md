---
title: rwmb_begin_html - Meta Box Documentation
source: https://docs.metabox.io/filters/rwmb-begin-html/
---

This filter is used to change the beginning HTML output of a field.

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

The default beginning HTML of a field is:

```html
<div class="rwmb-label" id="{$field['id]}-label">
    <label for="{$field['id']}">
        {$field['name']}
        <span class="rwmb-required">*</span>
    </label>
    <p id="{$field['id']}-label-description" class="description">{$field['label_description']}</p>
</div>
<div class="rwmb-input">
```

Syntax:

```php
apply_filters( 'rwmb_begin_html', $begin, $field, $value );
```

This filter accepts 3 parameters:

| Name | Description |
| --- | --- |
| `$begin` | The beginning HTML output of the field |
| `$field` | Field settings |
| `$value` | Field value |

This filter has variations:

- `rwmb_begin_html`: apply to all fields
- `rwmb_{$field_type}_begin_html`: apply to fields with a specific type
- `rwmb_{$field_id}_begin_html`: apply to a field with a specific id
