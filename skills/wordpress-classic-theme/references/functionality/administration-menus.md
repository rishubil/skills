---
title: Administration Menus
source: https://developer.wordpress.org/themes/classic-themes/functionality/administration-menus/
updated: 2026-05-11
---

# Administration Menus

**Author:** Samuel Sidler  
**Published:** October 23, 2014  
**Last Modified:** October 29, 2022

## Overview

This documentation explains how to create administration menu items in WordPress themes. The Customizer API is the recommended way to give more control and flexibility to your users rather than using administration menus directly.

## Three Essential Steps

To add an administration menu, developers must:

1. Create a function containing the menu-building code
2. Register that function using the `admin_menu` action hook (or `network_admin_menu` for network menus)
3. Create HTML output for the screen displayed when the menu is clicked

You can't simply call the menu code. You need to put it inside a function, and then register this function.

## Function Categories

**Menu Pages:**
- `add_menu_page()`
- `add_object_page()`
- `add_utility_page()`
- `remove_menu_page()`

**Sub-menu Pages:**
- `add_submenu_page()`
- `remove_submenu_page()`

**WordPress Administration Menu Wrappers:**
- `add_dashboard_page()`
- `add_posts_page()`
- `add_media_page()`
- `add_links_page()`
- `add_pages_page()`
- `add_comments_page()`
- `add_theme_page()`
- `add_plugins_page()`
- `add_users_page()`
- `add_management_page()`
- `add_options_page()`

## Code Examples

### Basic Example

A simple example demonstrates adding a sub-level item under Settings:

```php
<?php
add_action( 'admin_menu', 'my_menu' );

function my_menu() {
    add_options_page(
        'My Options',
        'My Menu',
        'manage_options',
        'my-unique-identifier',
        'my_options'
    );
}

function my_options() {
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_die( __( 'You do not have sufficient permissions to access this page.' ) );
    }
    echo 'Here is where I output the HTML for my screen.';
}
```

### Top-Level and Sub-Level Example

```php
<?php
function register_my_theme_settings_menu() {
    add_menu_page(
        "My Theme's Settings",
        'My Theme',
        'manage_options',
        'my-theme-settings-menu'
    );
}

function register_my_theme_more_settings_menu() {
    add_submenu_page(
        'my-theme-settings-menu',
        'More Settings for My Theme',
        'More Settings',
        'manage_options',
        'my-theme-more-settings-menu'
    );
}

add_action( 'admin_menu', 'register_my_theme_settings_menu' );
add_action( 'admin_menu', 'register_my_theme_more_settings_menu' );
```

## Page Hook Suffix

Every menu-adding function returns a **Page Hook Suffix** value. This enables creating page-specific actions using the `load-{page_hook}` hook.

```php
<?php
add_action( 'admin_menu', 'my_menu' );

function my_menu() {
    $hook_suffix = add_options_page( 'My Options', 'My Theme', 'manage_options', 'my-unique-identifier', 'my_options' );
    add_action( 'load-' . $hook_suffix, 'my_load_function' );
}
```

## Key Takeaways

- Menu-adding functions should be hooked to `admin_menu` action, not called directly
- User capability must be checked both when displaying menu items and when processing page content
- It is rare that a theme would require the creation of a new top-level menu
- The Customizer API is now the recommended approach for theme options

## Navigation

- **Previous:** [Accessibility](accessibility.md)
- **Next:** [Block theme accessibility](block-theme-accessibility.md)
