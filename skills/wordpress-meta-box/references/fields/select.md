---
title: Select - Meta Box Documentation
source: https://docs.metabox.io/fields/select/
version: 5.12.0
fetched: 2026-05-11
---

The select field creates a simple select dropdown. You can select one or multiple values from the predefined list.

## Screenshots

![The select field interface](https://docs.metabox.io/screenshots/select-1.png)

The select field interface

![The select field settings](https://docs.metabox.io/settings/select.png)

The select field settings

## Settings

Besides the [common settings](../field-settings.md), this field has the following specific settings, the keys are for use with code:

| Name | Key | Description |
| --- | --- | --- |
| Choices | `options` | List of choices, each per line. If you need to set values and labels, use the format "value: Label" for each choice.   When using with code, this setting is an array of `'value' => 'Label'`. |
| Multiple | `multiple` | Whether to allow select multiple values? `true` or `false` (default). |
| Placeholder | `placeholder` | The placeholder text. |
| Display "Toggle All" button | `select_all_none` | Display "Toggle All" button to quickly toggle choices. Applied only when "Multiple" is set. |
| Flatten | `flatten` | Display sub items without indentation. `true` or `false` (default). See below to know how to define sub items. |
| Callback | `_callback` | A callable function that returns an array of choices. The function should return an array of `'value' => 'Label'`. |

This is a sample field settings array when creating this field with code:

```php
[
    'name'            => 'Select',
    'id'              => 'select',
    'type'            => 'select',
    'multiple'        => true,
    'placeholder'     => 'Select an item',
    'select_all_none' => true,
    'options'         => [
        'java'       => 'Java',
        'javascript' => 'JavaScript',
        'php'        => 'PHP',
        'kotlin'     => 'Kotlin',
        'swift'      => 'Swift',
    ],
],
```

Besides the normal list of choices, you can define sub choices as follows:

```php
[
    'name'        => 'Select',
    'id'          => 'select',
    'type'        => 'select',
    'placeholder' => 'Select an Item',
    'flatten'     => false,
    'options' => [
        [
            'value' => 'monkeys',
            'label' => 'Monkeys',
        ],
        [
            'value' => 'king_kong',
            'label' => 'King Kong',
            'parent' => 'monkeys',
        ],
        [
            'value' => 'curious_george',
            'label' => 'Curious George',
            'parent' => 'monkeys',
        ],
        [
            'value' => 'donkeys',
            'label' => 'Donkeys',
        ],
        [
            'value' => 'eeyore',
            'label' => 'Eeyore',
            'parent' => 'donkeys',
        ],
        [
            'value' => 'guss',
            'label' => 'Gus',
            'parent' => 'donkeys',
        ],
    ],
],
```

Here is how it looks:

![select with sub choices](https://docs.metabox.io/assets/images/select-2-07d8bfd81fd9bc4a7dd87c3de6c2b72e.png)

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
