---
title: Conditional Tags
source: https://developer.wordpress.org/themes/classic-themes/basics/conditional-tags/
updated: 2026-05-11
---

# Conditional Tags

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last Modified:** April 4, 2024

## Overview

Conditional Tags enable template file modifications based on page context. They work with PHP if/else statements to display different content depending on conditions the current page matches.

Basic example:
```php
if ( is_user_logged_in() ) :
	echo 'Welcome, registered user!';
else :
	echo 'Welcome, visitor!';
endif;
```

## Where to Use Conditional Tags

Database queries must complete before conditional tags function. The `functions.php` file loads before query execution, so conditional tags won't work there directly.

Two implementation methods:
- Place in template files
- Create functions in `functions.php` that hook into actions/filters triggering later

## The Conditions For

### The Main Page
**is_home()** - Returns true displaying the main blog page in reverse chronological order, or the designated "Posts page" if homepage is static.

### The Front Page
**is_front_page()** - Returns true when displaying the site's front page, whether showing posts or a static page.

### The Administration Panels
**is_admin()** - Returns true when Dashboard or administration panels display.

### A Single Post Page
**is_single()** - Returns true for any single post, attachment, or custom post type (false for pages).

Parameters:
```php
is_single( '17' );                    // Post ID 17
is_single( 'Irish Stew' );            // Post title
is_single( 'beef-stew' );             // Post slug
is_single( array( 17, 'beef-stew', 'Irish Stew' ) );
is_single( array( 17, 19, 1, 11 ) );  // Multiple IDs
```

### A Single Post, Page, or Attachment
**is_singular()** - Returns true for any single post, page, or attachment; allows post type testing.

### A Sticky Post
**is_sticky()** - Returns true if "Stick this post to the front page" is enabled.

### A Post Type
**get_post_type()** - Returns the registered post type of current post (not a true conditional tag).

```php
if ( 'book' == get_post_type() ) { ... }
```

**post_type_exists()** - Returns true if a given post type is registered.

### A "PAGE" Page
**is_page()** - When any WordPress page (post_type 'page') displays.

Parameters:
```php
is_page( '42' );                      // Page ID 42
is_page( 'About Me And Joe' );        // Page title
is_page( 'about-me' );                // Page slug
is_page( array( 42, 'about-me', 'About Me And Joe' ) );
```

### A Category Page
**is_category()** - When a category archive page displays.

**in_category()** - Returns true if current post is in specified category.

### A Tag Page
**is_tag()** - When any tag archive page displays.

**has_tag()** - When current post has a tag (use inside the Loop).

### A Taxonomy Page
**is_tax()** - When any taxonomy archive page displays.

**has_term()** - Check if current post has given terms.

### An Author Page
**is_author()** - When any author archive page displays.

### A Date Page
**is_date()** - When any date-based archive displays.

**is_year()** - When a yearly archive displays.

**is_month()** - When a monthly archive displays.

**is_day()** - When a daily archive displays.

### Any Archive Page
**is_archive()** - When any archive page displays.

### A Search Result Page
**is_search()** - When a search result archive displays.

### A 404 Not Found Page
**is_404()** - When a 404 error page displays.

### An Attachment
**is_attachment()** - When displaying an attachment.

### Has An Excerpt
**has_excerpt()** - When current post has an excerpt.

### Is Sidebar Active
**is_active_sidebar()** - Check if a sidebar is active/in use.

### A Child Theme
**is_child_theme()** - Checks whether a child theme is in use.

### Theme supports a feature
**current_theme_supports()** - Checks if various theme features exist.

## Working Examples

### Single Post

```php
<?php
if ( is_single() ) {
	echo 'This is just one of many fabulous entries in the ' . 
	     single_cat_title() . ' category!';
}
```

### Check for Multiple Conditionals

```php
<?php
if ( is_single() || is_page() ) {
	// If single post or single page
}

if ( is_archive() && ! is_category( 'nachos' ) ) {
	// If archive page EXCEPT nachos category
}
```

### Variable Sidebar Content

```php
<div id="sidebar">
<?php
if ( is_home() ) {
	wp_list_categories( 'optionall=0&sort_column=name&list=1&children=0' );
} elseif ( is_category() ) {
	wp_list_categories( 'optionall=1&sort_column=name&list=1&children=1&hierarchical=1' );
} elseif ( is_single() ) {
	// Hide sidebar for single posts
} elseif ( is_page() ) {
	if ( is_page( 'About' ) ) {
		echo 'This is my about page!';
	} elseif ( is_page( 'Colophon' ) ) {
		echo 'This is my colophon page, running on WordPress ' . 
		     bloginfo( 'version' ) . '';
	} else {
		echo 'Vote for Pedro!';
	}
} else {
	echo 'Pedro offers you his protection.';
}
?>
</div><!-- #sidebar -->
```

## Conditional Tags Index

[List of Conditional Tags](https://developer.wordpress.org/themes/references/list-of-conditional-tags/)

## Navigation

- **Previous:** [Categories, Tags, & Custom Taxonomies](categories-tags-custom-taxonomies.md)
- **Next:** [Including CSS & JavaScript (Archived)](including-css-javascript.md)
