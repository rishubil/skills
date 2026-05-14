---
title: File Input - Meta Box Documentation
source: https://docs.metabox.io/fields/file-input/
version: 5.12.0
fetched: 2026-05-11
---

The file input field creates a simple text input for uploading a single file. You can select a file from the Media Library or enter a file URL directly (even a URL for a file hosted on another website). After selecting from the Media Library, the input file URL will be pasted into the input and is saved into the database.

## Screenshots

![The file input field interface](https://imgur.elightup.com/cPVTMNy.png)

The file input field interface

![The file input field settings](https://docs.metabox.io/settings/file-input.png)

The file input field settings

## Settings

This field doesn't have any specific settings. It only uses [common settings](../field-settings.md).

## Data

This field saves the input file URL in the database.

## Template usage

**Displaying file:**

```php
<?php $value = rwmb_meta( 'my_field_id' ) ?>
<p><a href="<?= $value >">Download file</a></p>
```

**Displaying uploaded image:**

```php
<?php $value = rwmb_meta( 'my_field_id' ) ?>
<p><img src="<?= $value >"></p>
```
