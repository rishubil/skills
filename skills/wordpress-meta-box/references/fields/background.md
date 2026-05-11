---
title: Background - Meta Box Documentation
source: https://docs.metabox.io/fields/background/
version: 5.12.0
fetched: 2026-05-11
---

The background field allows you to set background properties for a post. You can set the background color, select an image, and set other background settings.

## Screenshots

![The background field interface](https://docs.metabox.io/screenshots/background.png)

The background field interface

![The background field settings](https://docs.metabox.io/settings/background.png)

The background field settings

## Settings

This field doesn't have any specific settings. It only uses [common settings](../field-settings.md).

This is a sample field settings array when creating this field with code:

```php
[
    'id'   => 'background',
    'name' => 'Section background',
    'type' => 'background',
],
```

## Data

This field stores background properties in a serialized array in the post meta.

## Template usage

**Getting the background properties:**

```php
$background = rwmb_meta( 'my_field_id' );
echo $background['color'];
echo $background['image'];
```

This helper function returns an array of background properties:

```php
[
    'color'      => '#111222',
    'image'      => 'https://domain.com/wp-uploads/2017/12/bg.png',
    'position'   => 'top left',
    'attachment' => 'fixed',
    'size'       => 'cover',
    'repeat'     => 'no-repeat',
];
```

**Outputting the CSS for the background:**

```php
<div style="<?php rwmb_the_value( 'my_field_id' ) ?>">
    <h2>My section title</h2>
    <p>My section content</p>
</div>
```
