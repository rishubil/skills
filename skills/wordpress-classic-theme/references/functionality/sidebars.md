---
title: Sidebars
source: https://developer.wordpress.org/themes/classic-themes/functionality/sidebars/
updated: 2026-05-11
---

# Sidebars

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last Modified:** October 29, 2022

## What are Sidebars

A sidebar is any widgetized area of your theme. Widget areas are places in your theme where users can add their own widgets. Users don't need sidebars included, but they enable content addition through the Customizer or Widgets Admin Panel.

Widgets can be employed for a variety of purposes, ranging from listing recent posts to conducting live chats.

The term "sidebars" originated when widget areas were normally created in a long strip to the lefthand or righthand side of a blog. Currently, sidebars have evolved beyond their original name. They can be included anywhere on your website.

## Registering a Sidebar

Sidebars must be registered in `functions.php`. The `register_sidebar()` function includes these key parameters:

- **name** – The sidebar's display name in the Widgets panel
- **id** – Must be lowercase; used with the `dynamic_sidebar` function
- **description** – Shown in the admin Widgets panel
- **class** – CSS class name for the widget's HTML
- **before_widget** – HTML placed before each widget
- **after_widget** – HTML placed after each widget; closes `before_widget` tags
- **before_title** – HTML placed before widget titles (e.g., header tags)
- **after_title** – HTML placed after titles; closes `before_title` tags

```php
<?php
function themename_widgets_init() {
	register_sidebar( array(
		'name'          => __( 'Primary Sidebar', 'theme_name' ),
		'id'            => 'sidebar-1',
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h3 class="widget-title">',
		'after_title'   => '</h3>',
	) );
	register_sidebar( array(
		'name'          => __( 'Secondary Sidebar', 'theme_name' ),
		'id'            => 'sidebar-2',
		'before_widget' => '<ul><li id="%1$s" class="widget %2$s">',
		'after_widget'  => '</li></ul>',
		'before_title'  => '<h3 class="widget-title">',
		'after_title'   => '</h3>',
	) );
}
```

Two functions are available:
- `register_sidebar()` – registers one sidebar
- `register_sidebars()` – registers multiple sidebars

It's recommended to register sidebars individually for unique, descriptive naming.

## Displaying Sidebars in your Theme

### Create a Sidebar Template File

WordPress recognizes `sidebar.php` and `sidebar-{name}.php` template files.

Example `sidebar-primary.php`:

```php
<div id="sidebar-primary" class="sidebar">
	<?php dynamic_sidebar( 'primary' ); ?>
</div>
```

### Load your Sidebar

```php
<?php get_sidebar(); ?>
```

Display the Primary sidebar by passing the `$name` parameter:

```php
<?php get_sidebar( 'primary' ); ?>
```

## Customizing your Sidebar

### Display Default Sidebar Content

```php
<div id="sidebar-primary" class="sidebar">
	<?php if ( is_active_sidebar( 'primary' ) ) : ?>
		<?php dynamic_sidebar( 'primary' ); ?>
	<?php else : ?>
		<!-- Time to add some widgets! -->
	<?php endif; ?>
</div>
```

### Display Default Widgets

Pre-populate sidebars with default widgets:

```php
<div id="primary" class="sidebar">
	<?php if ( ! dynamic_sidebar( 'sidebar-primary' ) ) : ?>
		<aside id="search" class="widget widget_search">
			<?php get_search_form(); ?>
		</aside><!-- #search -->

		<aside id="archives" class="widget">
			<h3 class="widget-title"><?php _e( 'Archives', 'shape' ); ?></h3>
			<ul>
				<?php wp_get_archives( array( 'type' => 'monthly' ) ); ?>
			</ul>
		</aside><!-- #archives -->
	<?php endif; ?>
</div><!-- #primary -->
```

## Navigation

- **Previous:** [Post Formats](post-formats.md)
- **Next:** [Widgets](widgets.md)
