---
title: rwmb_html - Meta Box Documentation
source: https://docs.metabox.io/filters/rwmb-html/
---

This filter is used to change the HTML of the **field input**.

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

This filter is used to change the **field input HTML**, e.g. the HTML of the inputs to enter data.

The HTML of a field input is various and depends on the field type. For example, a text field outputs an `input` tag, while a wysiwyg field outputs a complex `div`.

```php
apply_filters( 'rwmb_html', $html, $field, $value );
```

This filter accepts 3 parameters:

| Name | Description |
| --- | --- |
| `$html` | HTML output of a field |
| `$field` | Field settings |
| `$value` | Field value |

This filter has variations:

- `rwmb_html`: apply to all fields
- `rwmb_{$field_type}_html`: apply to fields with a specific type
- `rwmb_{$field_id}_html`: apply to a field with a specific id
