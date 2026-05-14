---
title: File Advanced - Meta Box Documentation
source: https://docs.metabox.io/fields/file-advanced/
version: 5.12.0
fetched: 2026-05-11
---

The file advanced field uses the WordPress media popup for selecting / uploading files. You can also reorder files if you want.

## Screenshots

![The file advanced field interface](https://imgur.elightup.com/mqR9Tue.png)

The file advanced field interface

![The file advanced field settings](https://docs.metabox.io/settings/file-advanced.png)

The file advanced field settings

## Settings

Besides the [common settings](../field-settings.md), this field has the following specific settings, the keys are for use with code:

| Name | Key | Description |
| --- | --- | --- |
| Max number of files | `max_file_uploads` | Max number of uploaded files. Optional. |
| Force delete | `force_delete` | Whether or not delete the files from Media Library when deleting them from post meta. `true` or `false` (default). Optional. Note: it might affect other posts if you use the same file for multiple posts. |
| MIME types | `mime_type` | The MIME type of files which you want to show in the Media Library. Note: this is a filter for items in the media popup, it doesn't restrict file types when uploading. See [common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types). |
| Show status | `max_status` | Display how many files uploaded/remaining. Applied only when "Max number of files" is defined. `true` (default) or `false`. Optional. |

This is a sample field settings array when creating this field with code:

```php
[
    'id'               => 'file',
    'name'             => 'File Advanced',
    'type'             => 'file_advanced',
    'force_delete'     => false,
    'max_file_uploads' => 2,
    'mime_type'        => 'application/pdf',
    'max_status'       => false,
],
```

## Data

This field saves multiple attachment IDs in the database. Each value (attachment ID) is stored in a single row in the database with the same meta key (similar to what `add_post_meta` does with the last parameter `false`).

## Template usage

**Displaying uploaded files with links:**

```php
<?php $files = rwmb_meta( 'my_field_id' ); ?>
<h3>Uploaded files</h3>
<ul>
    <?php foreach ( $files as $file ) : ?>
        <li><a href="<?= $file['url']; ?>"><?= $file['name']; ?></a></li>
    <?php endforeach ?>
</ul>
```

or simpler:

```php
<h3>Uploaded files</h3>
<?php rwmb_the_value( 'my_field_id' ) ?>
```

`rwmb_the_value()` outputs files in an unordered list, while `rwmb_meta()` returns an array of files, each file has the following information:

```php
[
    'ID'    => 123,
    'name'  => 'intro.txt',
    'path'  => '/var/www/wp-content/uploads/intro.txt',
    'url'   => 'https://example.com/wp-content/uploads/intro.txt',
    'title' => 'Introduction',
];
```

**Displaying only one file:**

```php
<?php $files = rwmb_meta( 'my_field_id', ['limit' => 1] ) ?>
<?php $file = reset( $files ) ?>
<a class="button" href="<?= $file['url'] ?>">Download file</a>
```

## Filters

This field has some filters to change the texts displayed on the screen..

| Filter | Default | Description |
| --- | --- | --- |
| `rwmb_media_add_string` | \+ Add Media | Add new file string |
| `rwmb_media_single_files_string` | file | Singular "file" string |
| `rwmb_media_multiple_files_string` | files | Plural "files" string |
| `rwmb_media_remove_string` | Remove | File remove string |
| `rwmb_media_edit_string` | Edit | File edit string |
| `rwmb_media_view_string` | View | File view string |

The code below changes the "+ Add Media" string:

```php
add_filter( 'rwmb_media_add_string', function () {
    return '+ New File';
} );
```
