---
title: Custom Headers
source: https://developer.wordpress.org/themes/classic-themes/functionality/custom-headers/
updated: 2026-05-11
---

# Custom Headers

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last Modified:** October 29, 2022

## Overview

Custom headers enable site owners to upload their own 'title' image to their site, which can be placed at the top of certain pages. Users can customize and crop headers through the Customizer in **Appearance > Header**. These headers are optional theme features implemented via `get_custom_header()` after registering support in `functions.php`.

## Basic Setup

To establish a custom header with text support, add this code to your theme:

```php
<?php
function themename_custom_header_setup() {
	$args = array(
		'default-image'      => get_template_directory_uri() . 'img/default-image.jpg',
		'default-text-color' => '000',
		'width'              => 1000,
		'height'             => 250,
		'flex-width'         => true,
		'flex-height'        => true,
	);
	add_theme_support( 'custom-header', $args );
}
add_action( 'after_setup_theme', 'themename_custom_header_setup' );
```

## Configuration Options

Enable basic support with: `add_theme_support( 'custom-header' );`

Available parameters include:

- `default-image`: Initial header image URL
- `header-text`: Toggle text display (default: enabled)
- `default-text-color`: Text color default
- `width` / `height`: Dimensions in pixels
- `random-default`: Enable random rotation
- `uploads`: Allow admin uploads
- `wp-head-callback`: Theme head function
- `admin-head-callback`: Admin preview function
- `admin-preview-callback`: Admin markup function

## Flexible Headers

When `flex-height` or `flex-width` are omitted, dimensions are fixed. When included, the specified dimensions serve as suggestions rather than requirements.

## Header Text Control

By default, the user will have the option of whether or not to display header text. Set `'header-text' => false` to remove this option entirely.

## Implementation Examples

### Setting Default Images

```php
<?php
$header_info = array(
	'width'         => 980,
	'height'        => 60,
	'default-image' => get_template_directory_uri() . '/images/sunset.jpg',
);
add_theme_support( 'custom-header', $header_info );

$header_images = array(
	'sunset' => array(
		'url'           => get_template_directory_uri() . '/images/sunset.jpg',
		'thumbnail_url' => get_template_directory_uri() . '/images/sunset_thumbnail.jpg',
		'description'   => 'Sunset',
	),
	'flower' => array(
		'url'           => get_template_directory_uri() . '/images/flower.jpg',
		'thumbnail_url' => get_template_directory_uri() . '/images/flower_thumbnail.jpg',
		'description'   => 'Flower',
	),
);
register_default_headers( $header_images );
```

### Flexible Header Setup

```php
<?php
$args = array(
	'flex-width'    => true,
	'width'         => 980,
	'flex-height'   => true,
	'height'        => 200,
	'default-image' => get_template_directory_uri() . '/images/header.jpg',
);
add_theme_support( 'custom-header', $args );
```

Update `header.php`:

```php
<img alt="" src="<?php header_image(); ?>" width="<?php echo absint( get_custom_header()->width ); ?>" height="<?php echo absint( get_custom_header()->height ); ?>">
```

### Displaying Custom Headers

```php
<?php if ( get_header_image() ) : ?>
	<div id="site-header">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home">
			<img src="<?php header_image(); ?>" width="<?php echo absint( get_custom_header()->width ); ?>" height="<?php echo absint( get_custom_header()->height ); ?>" alt="<?php echo esc_attr( get_bloginfo( 'name', 'display' ) ); ?>">
		</a>
	</div>
<?php endif; ?>
```

## Function Reference

- `header_image()` – Display header image URL
- `get_header_image()` – Retrieve header image
- `get_custom_header()` – Get header image data
- `get_random_header_image()` – Retrieve random header
- `add_theme_support()` – Register feature support
- `register_default_headers()` – Register default header selections

## Navigation

- **Previous:** [Custom Front Page Templates](custom-front-page-templates.md)
- **Next:** [Custom Logo](custom-logo.md)
