---
title: Custom Logo
source: https://developer.wordpress.org/themes/classic-themes/functionality/custom-logo/
updated: 2026-05-11
---

# Custom Logo

## Overview

Using a custom logo allows site owners to upload an image for their website, which can be placed at the top of their site. This feature is optional and requires theme support.

## Adding Theme Support

To enable custom logo support, add the following to your theme's `functions.php`:

```php
add_theme_support( 'custom-logo' );
```

You can also specify additional parameters:

```php
function themename_custom_logo_setup() {
    $defaults = array(
        'height'      => 100,
        'width'       => 400,
        'flex-height' => true,
        'flex-width'  => true,
        'header-text' => array( 'site-title', 'site-description' ),
    );
    add_theme_support( 'custom-logo', $defaults );
}
add_action( 'after_setup_theme', 'themename_custom_logo_setup' );
```

## Displaying the Logo

Use the `the_custom_logo()` function to display the custom logo:

```php
<?php the_custom_logo(); ?>
```

Or use `get_custom_logo()` to retrieve it as a value:

```php
$custom_logo_id = get_theme_mod( 'custom_logo' );
$logo = wp_get_attachment_image_src( $custom_logo_id , 'full' );
if ( has_custom_logo() ) {
    echo '<img src="' . esc_url( $logo[0] ) . '" alt="' . get_bloginfo( 'name' ) . '">';
} else {
    echo '<h1>' . get_bloginfo( 'name' ) . '</h1>';
}
```

## Function Reference

- `the_custom_logo()` – Displays the custom logo
- `get_custom_logo()` – Returns the custom logo HTML
- `has_custom_logo()` – Checks if a custom logo has been set

## Navigation

- **Previous:** [Custom Headers](custom-headers.md)
- **Next:** [Featured Images & Post Thumbnails](featured-images-post-thumbnails.md)
