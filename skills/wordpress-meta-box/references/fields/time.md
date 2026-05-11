---
title: Time - Meta Box Documentation
source: https://docs.metabox.io/fields/time/
version: 5.12.0
fetched: 2026-05-11
---

The time field allows you to select a time via a friendly UI. This field uses jQuery UI time picker libraries.

## Screenshots

![The time field interface](https://imgur.elightup.com/xwV5FN5.png)

The time field interface

![The time field with select dropdowns](https://imgur.elightup.com/S83Wpau.png)

The time field with select dropdowns

![The time field settings](https://docs.metabox.io/settings/time.png)

The time field settings

## Settings

Besides the [common settings](../field-settings.md), this field has the following specific settings, the keys are for use with code:

| Name | Key | Description |
| --- | --- | --- |
| Size of the input box | `size` | Size of the input box. Optional. Default 10. Without this setting, the input box is full-width. |
| Inline | `inline` | Whether to display the time picker inline with the input and don't require to click to show the time picker? `true` or `false` (default). |
| Time picker options | `js_options` | Time picker options. [See here](http://trentrichardson.com/examples/timepicker/). |

This is a sample field settings array when creating this field with code:

```php
[
    'name'       => 'Time picker',
    'id'         => 'field_id',
    'type'       => 'time',
    'js_options' => [
        'stepMinute'      => 15,
        'controlType'     => 'select',
        'showButtonPanel' => false,
        'oneLine'         => true,
    ],
],
```

## Data

This field saves ther entered time in the database.

If the field is cloneable, then the value is stored as a serialized array in a single row in the database.

## Template usage

**Displaying entered time:**

```php
<?php $value = rwmb_meta( 'my_field_id' ) ?>
<p>Entered: <?= $value ?>
```

or simpler:

```php
<p>Entered: <?= rwmb_the_value( 'my_field_id' ) ?>
```
