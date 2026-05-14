---
title: Post Formats
source: https://developer.wordpress.org/themes/classic-themes/functionality/post-formats/
updated: 2026-05-11
---

# Post Formats

**Author:** Samuel Sidler  
**Published:** October 23, 2014  
**Last Modified:** October 29, 2022

## Overview

A Post Format is used by a theme for presenting posts in a certain format and style. This feature enables bloggers to change how posts appear by selecting from a standardized list of formats, rather than relying on category-based styling approaches.

## Supported Formats

The following formats are available (if the theme supports them):

- **aside** – Presented without a title, similar to Facebook status updates
- **gallery** – Contains image gallery shortcodes with attachments
- **link** – Points to external content; may use the first anchor tag or URL
- **image** – Features a single image; uses first img tag or URL
- **quote** – Contains quotations, typically in blockquote tags
- **status** – Brief updates resembling Twitter posts
- **video** – Single video via video/object/embed tags or URL
- **audio** – Audio files, suitable for podcasting
- **chat** – Transcript-style formatted conversations

Posts without a specified format default to "Standard."

## Function Reference

**Main Functions:**
- `set_post_format()`
- `get_post_format()`
- `has_post_format()`

**Other Functions:**
- `get_post_format_link()`
- `get_post_format_string()`

## Adding Theme Support

Themes implement post format support via `functions.php`:

```php
<?php
function themename_post_formats_setup() {
	add_theme_support( 'post-formats', array( 'aside', 'gallery' ) );
}
add_action( 'after_setup_theme', 'themename_post_formats_setup' );
```

## Adding Post Type Support

Custom post types can support formats using `add_post_type_support()`:

```php
<?php
function themename_custom_post_formats_setup() {
	add_post_type_support( 'page', 'post-formats' );
	add_post_type_support( 'my_custom_post_type', 'post-formats' );
}
add_action( 'init', 'themename_custom_post_formats_setup' );
```

## Using Formats

Check post format using the conditional tag:

```php
<?php
if ( has_post_format( 'video' ) ) {
	echo 'This is the video format.';
}
```

## Suggested Styling

Apply CSS classes dynamically with `post_class()` to style formats:

```css
.format-status .post-title {
     display: none;
}
```

## Formats in a Child Theme

Child themes inherit parent formats but must be done at a later priority to override:

```php
<?php
add_action( 'after_setup_theme', 'childtheme_formats', 11 );
function childtheme_formats() {
	 add_theme_support( 'post-formats', array( 'aside', 'gallery', 'link' ) );
}
```

Use `remove_theme_support('post-formats')` to disable entirely.

## Navigation

- **Previous:** [Pagination](pagination.md)
- **Next:** [Sidebars](sidebars.md)
