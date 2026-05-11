---
title: Including CSS & JavaScript (Archived)
source: https://developer.wordpress.org/themes/classic-themes/basics/including-css-javascript/
updated: 2026-05-11
---

# Including CSS & JavaScript (Archived)

## Overview

This page documents how to properly add stylesheets and JavaScript files to WordPress themes. The content is archived, with newer documentation available in the "Including Assets" section of Core Concepts.

## Key Concept

When you're creating your theme, you may want to create additional stylesheets or JavaScript files. However, remember that a WordPress website will not just have your theme active, it will also be using many different plugins.

The standard WordPress approach ensures compatibility and prevents conflicts between themes and plugins.

## Enqueuing Scripts and Styles

Files should be loaded via `functions.php` using WordPress functions rather than directly in template files. The `style.css` file is mandatory for all themes.

## Stylesheets

Load CSS using `wp_enqueue_style()` with parameters:
- `$handle` - stylesheet name
- `$src` - file location
- `$deps` - dependencies
- `$ver` - version number
- `$media` - media type (all, screen, print, handheld)

Example:
```php
wp_enqueue_style( 'slider', get_template_directory_uri() . '/css/slider.css', false, '1.1', 'all');
```

## Block Styles

Use `wp_enqueue_block_style()` for WordPress 5.9+ to load CSS only when blocks appear on pages, improving performance.

## Scripts

Load JavaScript using `wp_enqueue_script()` with similar syntax to styles. Parameters include dependencies (like jQuery) and loading strategy options.

## Script Loading Strategies

WordPress 6.3+ supports:
- **defer** - executes after DOM loads, maintains order
- **async** - executes immediately, no guaranteed order

## Comment Reply Script

Include conditionally for classic themes:

```php
if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
    wp_enqueue_script( 'comment-reply' );
}
```

## Best Practice

It is best to combine all enqueued scripts and styles into a single function, and then call them using the `wp_enqueue_scripts` action.

## Navigation

- **Previous:** [Conditional Tags](conditional-tags.md)
- **Next:** [Linking Theme Files & Directories](linking-theme-files-directories.md)
