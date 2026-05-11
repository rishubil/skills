---
title: rwmb_the_value - Meta Box Documentation
source: https://docs.metabox.io/filters/rwmb-the-value/
version: 5.12.0
fetched: 2026-05-11
---

This filter is used to change the returned value of the [rwmb\_the\_value()](../functions/rwmb-the-value.md) helper function.

```php
apply_filters( 'rwmb_the_value', $value, $field_id, $args, $object_id );
```

It accepts 4 parameters:

| Name | Description |
| --- | --- |
| `$value` | The value returned by the `rwmb_the_value` function |
| `$field_id` | The field ID |
| `$args` | Arguments passed to the `rwmb_the_value` function |
| `$object_id` | Object ID |

## Examples

Format the value of a date field:

```php
add_filter( 'rwmb_meta', function( $value, $field_id, $args, $object_id ) {
    if ( $field_id === 'event_date' ) {
        $value = date( 'F j, Y', strtotime( $value ) );
    }
    return $value;
}, 10, 4 );
```
