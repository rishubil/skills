---
title: 404 Pages
source: https://developer.wordpress.org/themes/classic-themes/functionality/404-pages/
updated: 2026-05-11
---

# 404 Pages

**First published:** October 23, 2014  
**Last updated:** October 17, 2015  
**Author:** Samuel Sidler

## Overview

A 404 error page serves an essential purpose in WordPress themes. When visitors land on non-existent URLs, a 404 page is important to add into your theme in case a user stumbles upon a page that doesn't exist. Beyond simply notifying users of the error, the page should give your visitors a way to arrive at the right place.

## Creating the 404.php file

Begin by generating a new file named `404.php` in your WordPress theme directory. Using your existing `index.php` as a reference point can provide a solid foundation for development.

## Add a file header

Include a descriptive comment at the top of `404.php` and reference your theme's header file:

```php
/**
 * The template for displaying 404 pages (Not Found)
 */
get_header();
```

## Adding the body to your 404 Page

Structure the main content area with markup, messaging, and a search feature:

```php
<div id="primary" class="content-area">
		<div id="content" class="site-content" role="main">

			<header class="page-header">
				<h1 class="page-title"><?php _e( 'Not Found', 'twentythirteen' ); ?></h1>
			</header>

			<div class="page-wrapper">
				<div class="page-content">
					<h2><?php _e( 'This is somewhat embarrassing, isn\'t it?', 'twentythirteen' ); ?></h2>
					<p><?php _e( 'It looks like nothing was found at this location. Maybe try a search?', 'twentythirteen' ); ?></p>

					<?php get_search_form(); ?>
				</div><!-- .page-content -->
			</div><!-- .page-wrapper -->

		</div><!-- #content -->
	</div><!-- #primary -->
```

## Adding the footer and sidebar

Complete the template by including footer and optional sidebar components:

```php
get_sidebar();
get_footer();
```

## Testing Your 404 Page

After uploading `404.php`, verify functionality by visiting a non-existent URL on your domain (for example, `http://example.com/fred.php`). This should trigger the error page you've created.

## Navigation

- **Previous:** [Theme Functionality](index.md)
- **Next:** [Accessibility](accessibility.md)
