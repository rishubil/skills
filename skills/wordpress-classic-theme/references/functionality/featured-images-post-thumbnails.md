---
title: Featured Images & Post Thumbnails
source: https://developer.wordpress.org/themes/classic-themes/functionality/featured-images-post-thumbnails/
updated: 2026-05-11
---

# Featured Images & Post Thumbnails

**First published:** October 23, 2014  
**Last updated:** October 27, 2022

## Enabling Support for Featured Image

Featured images (also sometimes called Post Thumbnails) are images that represent an individual Post, Page, or Custom Post Type. To enable this functionality in your theme, declare support by adding this code to your theme's `functions.php` file:

```php
add_theme_support( 'post-thumbnails' );
```

## Setting a Featured Image

After enabling featured image support, the Featured Image meta box will be visible on the appropriate content item's Edit screens.

## Function Reference

* `add_image_size()` – Register a new image size
* `set_post_thumbnail_size()` – Register an image size for the post thumbnail
* `has_post_thumbnail()` – Check if a post has an image attached
* `the_post_thumbnail()` – Display post thumbnail
* `get_the_post_thumbnail()` – Retrieve post thumbnail
* `get_post_thumbnail_id()` – Retrieve post thumbnail ID

## Image Sizes

WordPress provides default image sizes: "Thumbnail", "Medium", "Large" and "Full Size" (original uploaded image). These can be configured in the WordPress Administration Media panel under **Settings > Media**. You can also define custom image dimensions:

```php
the_post_thumbnail(); // Without parameter -> Thumbnail
the_post_thumbnail( 'thumbnail' ); // Thumbnail (default 150px x 150px max)
the_post_thumbnail( 'medium' ); // Medium resolution (default 300px x 300px max)
the_post_thumbnail( 'medium_large' ); // Medium-large resolution (default 768px x no height limit max)
the_post_thumbnail( 'large' ); // Large resolution (default 1024px x 1024px max)
the_post_thumbnail( 'full' ); // Original image resolution (unmodified)
the_post_thumbnail( array( 100, 100 ) ); // Other resolutions (height, width)
```

## Add Custom Featured Image Sizes

```php
if ( function_exists( 'add_theme_support' ) ) {
    add_theme_support( 'post-thumbnails' );
    set_post_thumbnail_size( 150, 150, true ); // default Featured Image dimensions (cropped)

    // additional image sizes
    add_image_size( 'category-thumb', 300, 9999 ); // 300 pixels wide (and unlimited height)
}
```

## Set the Featured Image Output Size

Resize the image proportionally without distortion:

```php
set_post_thumbnail_size( 50, 50 ); // 50 pixels wide by 50 pixels tall, resize mode
```

Crop the image from sides, top, or bottom:

```php
set_post_thumbnail_size( 50, 50, true ); // 50 pixels wide by 50 pixels tall, crop mode
```

## Styling Featured Images

Featured Images are given a class 'wp-post-image'. They also get a class depending on the size of the thumbnail being displayed.

```css
img.wp-post-image
img.attachment-thumbnail
img.attachment-medium
img.attachment-large
img.attachment-full
```

Assign custom classes via the attribute parameter in `the_post_thumbnail()`:

```php
the_post_thumbnail( 'thumbnail', array( 'class' => 'alignleft' ) );
```

## Examples

### Default Usage

```php
// check if the post or page has a Featured Image assigned to it.
if ( has_post_thumbnail() ) {
    the_post_thumbnail();
}
```

### Linking to Post Permalink

```php
<?php if ( has_post_thumbnail()) : ?>
    <a href="<?php the_permalink(); ?>" alt="<?php the_title_attribute(); ?>">
        <?php the_post_thumbnail(); ?>
    </a>
<?php endif; ?>
```

### Link All Post Thumbnails Globally

Add to `functions.php`:

```php
add_filter( 'post_thumbnail_html', 'my_post_image_html', 10, 3 );
function my_post_image_html( $html, $post_id, $post_image_id ) {
  $html = '<a href="' . get_permalink( $post_id ) . '">' . $html . '</a>';
  return $html;
}
```

## Navigation

- **Previous:** [Custom Logo](custom-logo.md)
- **Next:** [Internationalization](internationalization.md)
