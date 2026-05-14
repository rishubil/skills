---
title: Linking Theme Files & Directories
source: https://developer.wordpress.org/themes/classic-themes/basics/linking-theme-files-directories/
updated: 2026-05-11
---

# Linking Theme Files & Directories

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last Modified:** January 12, 2017

## Linking to Core Theme Files

WordPress themes utilize multiple template files including `sidebar.php`, `header.php`, and `footer.php`, which are loaded using template tags like `get_header()`, `get_footer()`, and `get_sidebar()`.

Custom versions of these files can be created by naming them with a custom suffix, such as `header-{your_custom_template}.php`. These are then called by passing the custom template name as a parameter:

```php
get_header( 'your_custom_template' );
get_footer( 'your_custom_template' );
get_sidebar( 'your_custom_template' );
```

Additional custom template files can be created and loaded anywhere using `get_template_part()`. For example, a `content.php` file can be extended to `content-product.php` and loaded with:

```php
get_template_part( 'content', 'product' );
```

Templates can be organized into subdirectories within your theme. For instance, grouping content templates in a `content-templates` folder would result in loading them like this:

```php
get_template_part( 'content-templates/content', 'location' );
get_template_part( 'content-templates/content', 'product' );
get_template_part( 'content-templates/content', 'profile' );
```

## Linking to Theme Directories

To reference theme directory files, use the `get_theme_file_uri()` function:

```php
echo get_theme_file_uri( 'images/logo.png' );
```

When working with child themes, this function will return the URI of the file in your child theme if it exists. If the file cannot be found in your child theme, the function will return the URI of the file in the parent theme.

For accessing file paths instead of URIs, use `get_theme_file_path()`, which follows the same child/parent theme hierarchy logic.

In child themes, access parent theme files using:

```php
echo get_parent_theme_file_uri( 'images/logo.png' );
//or
echo get_parent_theme_file_path( 'images/logo.png' );
```

Note: these functions will return the URI or file path whether the file exists or not. If the file is missing, these functions will return a broken link.

These functions (`get_theme_file_uri()`, `get_theme_file_path()`, `get_parent_theme_file_uri()`, `get_parent_theme_file_path()`) were introduced in WordPress 4.7. For earlier versions, use `get_template_directory_uri()`, `get_template_directory()`, `get_stylesheet_directory_uri()`, and `get_stylesheet_directory()`.

## Dynamic Linking in Templates

Create dynamic links to pages or posts using their unique numerical ID:

```php
<a href="<?php echo get_permalink($ID); ?>">This is a link</a>
```

This approach allows page slugs to be changed later without breaking links, since IDs remain constant. However, this may increase database queries.

## Navigation

- **Previous:** [Including CSS & JavaScript (Archived)](including-css-javascript.md)
- **Next:** [Main Stylesheet (style.css)](main-stylesheet-style-css.md)
