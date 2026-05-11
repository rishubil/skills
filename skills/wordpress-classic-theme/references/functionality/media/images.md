---
title: Images
source: https://developer.wordpress.org/themes/classic-themes/functionality/media/images/
updated: 2026-05-11
---

# Images

**First published:** January 13, 2017  
**Last updated:** November 1, 2022

## Images

This section describes the handling of images in the Media Library. If you want to display the image file located within your theme directory, just specify the location with the img tag, and style it with CSS.

### Getting img code

To display the image in the Media Library, use the `wp_get_attachment_image()` function.

```php
echo wp_get_attachment_image( $attachment->ID, 'thumbnail' );
```

You will get HTML output with the selected thumbnail size. You can specify other sizes such as 'full' for the original image or 'medium' and 'large', or any pair of width and height as an array:

```php
echo wp_get_attachment_image( $attachment->ID, array(640, 480) );
```

### Getting URL of image

If you want to get the URL of the image, use `wp_get_attachment_image_src()`. It returns an array (URL, width, height, is_intermediate), or `false`, if no image is available.

```php
<?php 
$image_attributes = wp_get_attachment_image_src( $attachment->ID );
if ( $image_attributes ) : ?>
    <img src="<?php echo $image_attributes[0]; ?>" width="<?php echo $image_attributes[1]; ?>" height="<?php echo $image_attributes[2]; ?>" />
<?php endif; ?>
```

### Alignments

When adding the image in your site, you can specify the image alignment as right, left, center or none. WordPress core automatically adds CSS classes to align the image:

* alignright
* alignleft
* aligncenter
* alignnone

In order to take advantage of these CSS classes for alignment and text wrapping, your theme must include the styles in a stylesheet.

### Caption

If a Caption was specified to an image in the Media Library, the HTML `img` element is enclosed by the shortcode `[caption]` and `[/caption]`.

Similar to alignments, your theme must include following styles:

* `wp-caption`
* `wp-caption-text`

## WebP support and default MIME type of sub size image output

WordPress 5.8 introduces support for WebP image format which provides improved lossless and lossy compression for images on the web. WebP images are approximately 30% smaller on average than their JPEG or PNG equivalents.

When images are uploaded, WordPress generates smaller sub sizes as defined using `add_image_size()`. By default, WordPress will generate these sub sizes in the same format as the original.

The `image_editor_output_format` filter hook can be used to change the file format used for image sub sizes:

```php
<?php
function wporg_image_editor_output_format( $formats ) {
    $formats['image/jpg'] = 'image/webp';

    return $formats;
}
add_filter( 'image_editor_output_format', 'wporg_image_editor_output_format' );
```

## Navigation

- **Previous:** [Galleries](galleries.md)
- **Next:** [Video](video.md)
