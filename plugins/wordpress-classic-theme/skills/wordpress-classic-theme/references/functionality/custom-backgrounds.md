---
title: Custom Backgrounds
source: https://developer.wordpress.org/themes/classic-themes/functionality/custom-backgrounds/
updated: 2026-05-11
---

# Custom Backgrounds

**First published:** March 5, 2017  
**Last updated:** November 17, 2022

## Enable Custom Backgrounds

Custom Backgrounds represents a theme feature that provides for customization of the background color and image. Theme developers need two implementation steps:

1. Enable Custom Background using `add_theme_support()`
2. Display Custom Background via `wp_head()` and `body_class()`

To activate this feature, add the following to your `functions.php` file:

```php
add_theme_support( 'custom-background' );
```

Optional default parameters can be specified:

```php
$args = array(
    'default-color' => '0000ff',
    'default-image' => get_template_directory_uri() . '/images/wapuu.jpg',
);
add_theme_support( 'custom-background', $args );
```

This displays 'Background Image' menu and 'Background Color' section in Colors menu within the Customizer.

## Display Custom Backgrounds

Include both `wp_head()` and `body_class()` in your `header.php`:

```php
<!DOCTYPE html>
<html>
<head>
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
```

The `wp_head()` function generates an extra style sheet in-line with the HTML headers that overrides theme stylesheet background values.

## Another default example

Additional customization options are available:

```php
$another_args = array(
    'default-color'      => '0000ff',
    'default-image'      => get_template_directory_uri() . '/images/wapuu.jpg',
    'default-position-x' => 'right',
    'default-position-y' => 'top',
    'default-repeat'     => 'no-repeat',
);
add_theme_support( 'custom-background', $another_args );
```

Note: When a default image is specified, it becomes the active background immediately. Default color settings only appear in the Customizer menu and require administrator action to take effect.

## Navigation

- **Previous:** [Core-Supported Features](core-supported.md)
- **Next:** [Custom Front Page Templates](custom-front-page-templates.md)
