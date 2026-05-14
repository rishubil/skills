---
title: Internationalization
source: https://developer.wordpress.org/themes/classic-themes/functionality/internationalization/
updated: 2026-05-11
---

# Internationalization

**First published:** October 23, 2014  
**Last updated:** November 17, 2022

## What is internationalization?

Internationalization refers to the process of developing your theme, so it can easily be translated into other languages. The term is frequently abbreviated as `i18n` because there are 18 letters between the first and last characters.

## Why is internationalization important?

WordPress has a global user base spanning countries where English isn't the primary language. The strings in the WordPress plugins need to be coded in a special way so that can be easily translated into other languages. Developers can leverage translator contributions without requiring modifications to the underlying code.

## How to internationalize your theme?

Strings should be passed through WordPress localization functions rather than hardcoded into theme files.

**Non-translatable approach:**
```php
<h1>Settings Page</h1>
```

**Translatable approach:**
```php
<h1><?php _e( 'Settings Page' ); ?></h1>
```

WordPress implements gettext libraries for translation functionality, though developers should use WordPress-specific localization functions rather than native PHP alternatives.

## Text Domain

The text domain serves as a unique identifier, allowing WordPress to distinguish between all of the loaded translations. It's required for themes and plugins.

For WordPress.org-hosted themes, the text domain must correspond to the theme's URL slug. Text domain names must use dashes (not underscores) and be lowercase.

Text domains appear in three locations:

1. The `style.css` theme header
2. Localization function arguments
3. `load_theme_textdomain()` or `load_child_theme_textdomain()` function calls

### style.css theme header

```php
/*
* Theme Name: My Theme
* Author: Theme Author
* Text Domain: my-theme
*/
```

### Domain Path

The domain path specifies where translation files are stored:

```php
/*
* Theme Name: My Theme
* Author: Theme Author
* Text Domain: my-theme
* Domain Path: /languages
*/
```

### Add text domain to strings

All localization functions require the text domain argument:

```php
__( 'Post', 'my-theme' )
_e( 'Post', 'my-theme' )
_n( '%s post', '%s posts', $count, 'my-theme' )
```

Text domains should be passed as strings, not variables, to enable proper parsing by translation tools.

### Loading Translations

```php
function my_theme_load_theme_textdomain() {
    load_theme_textdomain( 'my-theme', get_template_directory() . '/languages' );
}
add_action( 'after_setup_theme', 'my_theme_load_theme_textdomain' );
```

This function should be placed in the theme's `functions.php` file.

## Navigation

- **Previous:** [Featured Images & Post Thumbnails](featured-images-post-thumbnails.md)
- **Next:** [Localization](localization.md)
