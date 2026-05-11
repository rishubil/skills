---
title: Image - Meta Box Documentation
source: https://docs.metabox.io/fields/image/
---

The image field creates a simple image upload with default UI like `<input type="file">`. Unlike other media fields, this field doesn't use Media Library UI to upload images.

This field is very similar to [file](https://docs.metabox.io/fields/file/). The only difference is that the file field allows uploading all file types while this field allows only images.

## Screenshots

![The image field interface](https://imgur.elightup.com/8GFxWKP.png)

The image field interface

![The image field settings](https://docs.metabox.io/settings/image.png)

The image field settings

## Settings

Besides the [common settings](https://docs.metabox.io/field-settings/), this field has the following specific settings, the keys are for use with code:

| Name | Key | Description |
| --- | --- | --- |
| Max number of files | `max_file_uploads` | Max number of uploaded files. Optional. |
| Force delete | `force_delete` | Whether or not delete the files from Media Library when deleting them from post meta. `true` or `false` (default). Optional. Note: it might affect other posts if you use the same file for multiple posts. |
| Custom upload folder | `upload_dir` | Full path to a custom upload folder. |
| Unique filename callback | `unique_filename_callback` | Custom callback to set the uploaded file name. Works only when uploading to a custom folder. |

This is a sample field settings array when creating this field with code:

```php
[
    'name'         => 'Image Upload',
    'id'           => 'field_id',
    'type'         => 'image',
    'force_delete' => false,
],
```

## Data

This field saves multiple attachment IDs in the database. Each value (attachment ID) is stored in a single row in the database with the same meta key (similar to what `add_post_meta` does with the last parameter `false`).

## Custom upload folder

To upload files to a custom folder, set "Custom upload folder" to your folder full path.

If you're using code to create this field, you can use WordPress constants to specify the path easier, such as:

```php
'upload_dir' => ABSPATH . '/invoices/',

// or

'upload_dir' => WP_CONTENT_DIR . '/invoices/',
'unique_filename_callback' => 'my_function',
```

The custom folder should be inside your WordPress website's root folder. So you can store it in `/uploads/`, `/downloads/` folders if you want. The configuration is *per* field, so you can have one field storing files in `/downloads/` and another field in `/invoices/`.

The uploaded file name is normally the original file name and maybe with the suffix "-1", "-2" to prevent duplicated names. In case you want to set custom names for files, pass your custom callback to the setting `unique_filename_callback`.

Unlike the normal case, where files are added to the WordPress Media Library, files uploaded to custom folders are **not available in the Media Library**. Thus, the data saved in the custom fields is **file URL**, not attachment ID.

To get the field data, you can use `get_post_meta()` to get file URL, or use `rwmb_meta()` to get an array of file details which includes: `path`, `url` and `name`.

## Template usage

**Displaying uploaded images:**

```php
<?php $images = rwmb_meta( 'my_field_id', ['size' => 'thumbnail'] ); ?>
<h3>Uploaded images</h3>
<ul>
    <?php foreach ( $images as $image ) : ?>
        <li><img src="<?= $image['url']; ?>"></li>
    <?php endforeach ?>
</ul>
```

or simpler:

```php
<h3>Uploaded files</h3>
<?php rwmb_the_value( 'my_field_id', ['size' => 'thumbnail'] ) ?>
```

`rwmb_the_value()` outputs images in an unordered list, and `rwmb_meta()` returns an array of images, each image has the following information:

```php
[
    'ID'          => 123,
    'name'        => 'logo-150x80.png',
    'path'        => '/var/www/wp-content/uploads/logo-150x80.png',
    'url'         => 'https://example.com/wp-content/uploads/logo-150x80.png',
    'width'       => 150,
    'height'      => 80,
    'full_url'    => 'https://example.com/wp-content/uploads/logo.png',
    'title'       => 'Logo',
    'caption'     => 'Logo caption',
    'description' => 'Used in the header',
    'alt'         => 'Logo ALT text',
    'srcset'      => 'large.jpg 1920w, medium.jpg 960w, small.jpg 480w', // List of responsive image src
    'sizes'       => [], // List of image sizes. See https://developer.wordpress.org/reference/functions/wp_get_attachment_metadata/
    'image_meta'  => [], // List of image meta. See https://developer.wordpress.org/reference/functions/wp_get_attachment_metadata/
];
```

**Display images with links to the full-size versions (for lightbox effects):**

```php
<?php $images = rwmb_meta( 'my_field_id', ['size' => 'thumbnail'] ); ?>
<h3>Uploaded images</h3>
<ul>
    <?php foreach ( $images as $image ) : ?>
        <li><a href="<?= $image['full_url'] ?>"><img src="<?= $image['url']; ?>"></a></li>
    <?php endforeach ?>
</ul>
```

or simpler:

```php
<h3>Uploaded files</h3>
<?php rwmb_the_value( 'my_field_id', ['size' => 'thumbnail', 'link' => true] ) ?>
```

**Displaying only one image:**

```php
<?php $images = rwmb_meta( 'my_field_id', ['limit' => 1] ) ?>
<?php $image = reset( $images ) ?>
<img src="<?= $image['url']; ?>">
```

The 2nd argument for `rwmb_meta()` and `rwmb_the_value()` is an array of extra parameters and accepts the following parameters:

| Name | Description |
| --- | --- |
| `size` | Image size returned. Optional. Default `thumbnail`. |
| `link` | Set to `true` to show a link to the full-size version. Default `false`. |
| `limit` | Limit the number of returned images. |

## Filters

This field has some filters to change the texts displayed on the screen.

| Filter | Default | Description |
| --- | --- | --- |
| `rwmb_file_upload_string` | Upload Files | File upload string |
| `rwmb_file_add_string` | \+ Add new file | Add new file string |
| `rwmb_file_delete_string` | Delete | File delete string |
| `rwmb_file_edit_string` | Edit | File edit string |

All filters above accept 2 parameters:

- `$string`: the string needs to be changed
- `$field`: array of the field settings

The code below changes the "+ Add new file" string:

```php
add_filter( 'rwmb_file_add_string', function () {
    return '+ New File';
} );
```

## Tutorials

[How to display uploaded images as a WordPress image gallery?](https://metabox.io/display-uploaded-images-as-wordpress-image-gallery/)
