---
title: Navigation Menus
source: https://developer.wordpress.org/themes/classic-themes/functionality/navigation-menus/
updated: 2026-05-11
---

# Navigation Menus

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last Modified:** March 17, 2017

## Register Menus

Navigation Menus are customizable menus in your theme that allow users to add Pages, Posts, Categories, and URLs to the menu. To implement them, you must first register menus in your theme's functions.php file using the `register_nav_menus()` function. This step makes menu names visible in **Appearance -> Menus**.

Example registration:

```php
function register_my_menus() {
  register_nav_menus(
    array(
      'header-menu' => __( 'Header Menu' ),
      'extra-menu' => __( 'Extra Menu' )
     )
   );
 }
 add_action( 'init', 'register_my_menus' );
```

## Display Menus

After registering menus, use `wp_nav_menu()` to display them in your theme. Add this code to your header.php file:

```php
wp_nav_menu( array( 'theme_location' => 'header-menu' ) );
```

You can also add container classes for CSS styling:

```php
wp_nav_menu(
  array(
    'theme_location' => 'extra-menu',
    'container_class' => 'my_extra_menu_class'
  )
);
```

## Display Additional Contents

Add span elements or text around menu items using `link_before`, `link_after`, `before`, and `after` parameters:

```php
wp_nav_menu(
  array(
    'menu' => 'primary',
    'link_before' => '<span class="screen-reader-text">',
    'link_after' => '</span>',
  )
);
```

## Define Callback

Prevent default fallback behavior using the `fallback_cb` parameter:

```php
wp_nav_menu(
  array(
    'menu' => 'primary',
    'theme_location' => '__no_such_location',
    'fallback_cb' => false
  )
);
```

## Navigation

- **Previous:** [Video](media/video.md)
- **Next:** [Pagination](pagination.md)
