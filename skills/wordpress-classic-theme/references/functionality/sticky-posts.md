---
title: Sticky Posts
source: https://developer.wordpress.org/themes/classic-themes/functionality/sticky-posts/
updated: 2026-05-11
---

# Sticky Posts

**First published:** January 12, 2017  
**Last updated:** October 29, 2022

## Overview

A sticky post gets positioned at the top of the front page. This functionality applies only to the default "post" type and cannot be used with custom post types.

## How to Stick a Post

1. Navigate to **Administration Screen > Posts > Add New** or **Edit**
2. In the right sidebar menu, select the Edit link for the Visibility option within the Publish group
3. Check the "Stick this post to the front page" option

## Display Sticky Posts

### Show Sticky Posts

**Display the first sticky post only:**
```php
<?php
$sticky = get_option( 'sticky_posts' );
$query  = new WP_Query( 'p=' . $sticky[0] );
```

**Display first sticky post, or fall back to the most recent post:**
```php
<?php
$args  = array(
	'posts_per_page'      => 1,
	'post__in'            => get_option( 'sticky_posts' ),
	'ignore_sticky_posts' => 1,
);
$query = new WP_Query( $args );
```

### Don't Show Sticky Posts

**Exclude all sticky posts:**
```php
<?php
$args  = array( 'post__not_in' => get_option( 'sticky_posts' ) );
$query = new WP_Query( $args );
```

**Exclude sticky posts from a category while maintaining natural ordering:**
```php
<?php
$args  = array(
	'ignore_sticky_posts' => 1,
	'posts_per_page'      => 3,
	'cat'                 => 6,
);
$query = new WP_Query( $args );
```

**Display top 5 sticky posts:**
```php
<?php
/* Get all Sticky Posts */
$sticky = get_option( 'sticky_posts' );

/* Sort Sticky Posts, newest at the top */
rsort( $sticky );

/* Get top 5 Sticky Posts */
$sticky = array_slice( $sticky, 0, 5 );

/* Query Sticky Posts */
$query = new WP_Query( array(
	'post__in'            => $sticky,
	'ignore_sticky_posts' => 1,
) );
```

## Style Sticky Posts

The `post_class()` function automatically adds styling classes to post divs, including the "sticky" class for sticky posts:

```php
<div id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
```

Apply CSS styling to target sticky posts:
```css
.sticky { color: red; }
```

**Important note:** The sticky class only appears on the homepage's first page.

## Navigation

- **Previous:** [Widgets](widgets.md)
- **Next:** [Theme Options – The Customize API](../customize-api/index.md)
