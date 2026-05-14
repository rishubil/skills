---
title: Select Advanced - Meta Box Documentation
source: https://docs.metabox.io/fields/select-advanced/
version: 5.12.0
fetched: 2026-05-11
---

The select advanced field creates a beautiful select dropdown using the [select2](https://select2.org/) library.

## Screenshots

![The select advanced field interface](https://imgur.elightup.com/65OkGbt.png)

The select advanced field interface

![The select advanced field settings](https://docs.metabox.io/settings/select-advanced.png)

The select advanced field settings

## Settings

Besides the [common settings](../field-settings.md), this field has the following specific settings, the keys are for use with code:

| Name | Key | Description |
| --- | --- | --- |
| Choices | `options` | List of choices, each per line. If you need to set values and labels, use the format "value: Label" for each choice.   When using with code, this setting is an array of `'value' => 'Label'`. |
| Multiple | `multiple` | Whether to allow select multiple values? `true` or `false` (default). |
| Placeholder | `placeholder` | The placeholder text. |
| Display "Toggle All" button | `select_all_none` | Display "Toggle All" button to quickly toggle choices. Applied only when "Multiple" is set. |
| Select2 options | `js_options` | Options for `select2` library. [See here](https://select2.org/configuration). |

By default, Meta Box applies these default options for select2:

Name | Value | Description --- | --- `allowClear` | `true` | Allow users to clear selection. `width` | `resolve` | Set width by element's width. `placeholder` | `$field['placeholder']` | Make `placeholder` works just like `select` field.

This is a sample field settings array when creating this field with code:

```php
[
    'name'            => 'Select Advanced',
    'id'              => 'select_advanced',
    'type'            => 'select_advanced',
    'options'         => [
        'java'       => 'Java',
        'javascript' => 'JavaScript',
        'php'        => 'PHP',
        'kotlin'     => 'Kotlin',
        'swift'      => 'Swift',
    ],
    'placeholder'     => 'Select an Item',
    'js_options'      => [
        'containerCssClass' => 'my-custom-class',
    ],
],
```

## Data

If "Multiple" is not set, this field saves the selected value in the database.

If "Multiple" is set, this field saves multiple values in the database. Each value is stored in a single row in the database with the same key (similar to what `add_post_meta` does with the last parameter `false`).

If the field is cloneable, the value is stored as a serialized array in a single row in the database.

> [!-warning] -warning
> warning
> 
> Note that this field stores the **values**, not labels.

## Template usage

**Displaying the selected value:**

```php
<?php $value = rwmb_meta( 'my_field_id' ); ?>
<p>Selected: <?= $value ?></p>
```

**Displaying the selected label:**

```php
<p>My choice: <?php rwmb_the_value( 'my_field_id' ) ?></p>
```

**Displaying both value and label:**

```php
<?php
$field   = rwmb_get_field_settings( 'my_field_id' );
$options = $field['options'];
$value   = rwmb_meta( 'my_field_id' );
?>

Value: <?= $value ?><br>
Label: <?= $options[ $value ] ?>
```

**Displaying the list of multiple choices (values):**

```php
<?php $values = rwmb_meta( 'my_field_id' ); ?>
<ul>
    <?php foreach ( $values as $value ) : ?>
        <li><?= $value ?></li>
    <?php endforeach ?>
</ul>
```

**Displaying the list of multiple choices (values and labels):**

```php
<?php
$field   = rwmb_get_field_settings( 'my_field_id' );
$options = $field['options'];
$values  = rwmb_meta( 'my_field_id' );
?>
<ul>
    <?php foreach ( $values as $value ) : ?>
        <li>
            Value: <?= $value ?><br>
            Label: <?= $options[ $value ] ?>
        </li>
    <?php endforeach ?>
</ul>
```

**Displaying cloneable values:**

```php
<?php $values = rwmb_meta( 'my_field_id' ); ?>
<ul>
    <?php foreach ( $values as $value ) : ?>
        <li><?= $value ?></li>
    <?php endforeach ?>
</ul>
```
