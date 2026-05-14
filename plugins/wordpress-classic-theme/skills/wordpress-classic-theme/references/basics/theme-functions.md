---
title: Theme Functions
source: https://developer.wordpress.org/themes/classic-themes/basics/theme-functions/
updated: 2026-05-11
---

# Theme Functions

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last Modified:** March 17, 2023

## Overview

The `functions.php` file serves as a mechanism for adding unique features to WordPress themes. It behaves like a WordPress plugin, adding features and functionality to a WordPress site.

## What is functions.php?

The file functions similarly to a plugin but applies only to the active theme. Notable distinctions include:

- **WordPress Plugin:** Requires header text, stored in wp-content/plugins, applies to all themes
- **functions.php:** No header text needed, stored in theme directory, applies only to active theme

The code in the active theme's functions.php is actually run, and child themes can have their own functions file for risk-free modifications.

## Primary Uses

Developers can:

- Use WordPress hooks to modify functionality
- Enable features via `add_theme_support()`
- Define reusable functions for template files

## Theme Setup Examples

The documentation provides a complete setup function template (`myfirsttheme_setup()`) demonstrating:

- **Automatic Feed Links:** Enable RSS feeds
- **Navigation Menus:** Support custom menu registration
- **Text Domain Loading:** Enable theme translation
- **Post Thumbnails:** Allow featured images
- **Post Formats:** Support varied content presentation

## Content Width

For classic themes, a content width variable limits maximum content dimensions:

```php
if ( ! isset ( $content_width) ) {
    $content_width = 800;
}
```

## Naming Conventions

The guide emphasizes prefixing functions with unique identifiers to avoid conflicts, recommending theme name abbreviations.

## Navigation

- **Previous:** [The Loop](the-loop.md)
- **Next:** [Tools & Resources](tools-resources.md)
