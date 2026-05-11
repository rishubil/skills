---
title: Checkbox - Meta Box Documentation
source: https://docs.metabox.io/fields/checkbox/
---

The checkbox field creates a single checkbox.

## Screenshots

![The checkbox field interface](https://docs.metabox.io/screenshots/checkbox.png)

The checkbox field interface

![The checkbox field settings](https://docs.metabox.io/settings/checkbox.png)

The checkbox field settings

## Settings

Besides the [common settings](https://docs.metabox.io/field-settings/), this field has the following specific settings, the keys are for use with code:

| Name | Key | Description |
| --- | --- | --- |
| Checked by default | `std` | Whether the checkbox is checked by default? |

This is a sample field settings array when creating this field with code:

```php
[
    'name' => 'Checkbox',
    'id'   => 'field_id',
    'type' => 'checkbox',
    'std'  => 1, // 0 or 1
],
```

## Data

This field saves the "checked" and "unchecked" values in the database as "1" or "0".

## Template usage

**Conditional check:**

```php
$value = rwmb_meta( 'my_field_id' );
if ( $value ) {
    echo 'Checked';
} else {
    echo 'Unchecked';
}
```

**Displaying "Yes/No":**

```php
rwmb_the_value( 'my_field_id' );
```
