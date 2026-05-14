---
title: Custom Front Page Templates
source: https://developer.wordpress.org/themes/classic-themes/functionality/custom-front-page-templates/
updated: 2026-05-11
---

# Custom Front Page Templates

**Author:** Akira Tachibana  
**Published:** March 18, 2018

## Overview

By default, WordPress displays your most recent posts in reverse chronological order on your site's front page. Many users prefer a static front page or splash page instead. The look and feel of the front page of the site is based upon the choices of the user combined with the features and options of the WordPress Theme.

## Template Hierarchy of Custom Front Page

WordPress will always use the front-page.php template file if it exists. Otherwise, it determines which template to use based on the Reading settings configuration:

**For a static page:** WordPress uses the Static Page template hierarchy:
1. Custom Page Template
2. page-{id}.php
3. page-{slug}.php
4. page.php
5. index.php

**For your latest posts:** WordPress uses the Blog Posts Index hierarchy:
1. home.php
2. index.php

### Custom Site Front Page Template

To create a custom site front page template, include either:
* front-page.php
* A Custom Page Template (e.g., template-featured.php)

### Custom Blog Posts Index Page Template

Include home.php for a custom blog posts index template. Do not use a Custom Page Template because:
1. WordPress won't use a Custom Page Template for the blog posts index when static front page is configured
2. Pagination won't work properly if the Custom Page Template is assigned elsewhere

## Contextual Conditional Tags

### is_front_page

The Conditional Tag is_front_page() checks if the site front page is being displayed.

Returns true when viewing the site front page, regardless of whether the setting displays "Your latest posts" or "A static page".

### is_home

The Conditional Tag is_home() checks if the blog posts index is being displayed.

Returns true when viewing the blog posts index in these scenarios:
* Front page displays latest posts
* Front page displays a static page AND the current page is designated as the Posts Page

When the front page displays latest posts, both is_front_page() and is_home() return true.

## Configuration of front-page.php

If front-page.php exists, it's used regardless of the Reading settings. The theme must account for both options so the front page displays either static content or the blog posts index.

### Conditional display within front-page.php

**Method 1: Including custom content directly**

```php
if ( 'posts' == get_option( 'show_on_front' ) ) {
    include( get_home_template() );
} else {
    // Custom content markup goes here
}
```

**Method 2: Including any page template**

```php
if ( 'posts' == get_option( 'show_on_front' ) ) {
    include( get_home_template() );
} else {
    include( get_page_template() );
}
```

### Filtering frontpage_template

An alternative approach filters frontpage_template by adding this to functions.php:

```php
function themeslug_filter_front_page_template( $template ) {
    return is_home() ? '' : $template;
}
add_filter( 'frontpage_template', 'themeslug_filter_front_page_template' );
```

## Adding custom query loops to front-page.php

The default WordPress Loop applies to the static page content. To display custom content (latest posts, featured items), use secondary WP_Query loops:

```php
$latest_blog_posts = new WP_Query( array( 'posts_per_page' => 3 ) );

if ( $latest_blog_posts->have_posts() ) : while ( $latest_blog_posts->have_posts() ) : $latest_blog_posts->the_post();
    // Loop output goes here
endwhile; endif;
```

## Pagination

Static front pages are not intended to be paged. Previous/Next page link functions don't work with static front pages. Pagination uses the page query variable rather than the paged variable.

## Navigation

- **Previous:** [Custom Backgrounds](custom-backgrounds.md)
- **Next:** [Custom Headers](custom-headers.md)
