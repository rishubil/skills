---
title: The Loop
source: https://developer.wordpress.org/themes/classic-themes/basics/the-loop/
updated: 2026-05-11
---

# The Loop

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last Modified:** November 17, 2022

## Overview

The Loop is the default mechanism WordPress uses for outputting posts through a theme's template files. The number of posts displayed depends on the Reading settings configuration. WordPress retrieves each post from the database and formats it according to theme instructions, processing any HTML or PHP code in The Loop for each post.

## Core Functionality

The basic loop structure follows this pattern:

```php
<?php
if ( have_posts() ) :
    while ( have_posts() ) : the_post();
        // Display post content
    endwhile;
endif;
?>
```

The `have_posts()` function checks for available posts, while the `while` loop continues executing as long as posts exist.

## Placement Guidelines

The Loop should be placed in `index.php` and other post-display templates, always after calling `get_header()` to avoid duplicating headers. It must begin with matching `if` and `while` statements and end with corresponding `endwhile` and `endif` statements.

A basic `index.php` example:

```php
<?php
get_header();

if ( have_posts() ) :
    while ( have_posts() ) : the_post();
        the_content();
    endwhile;
else :
    _e( 'Sorry, no posts matched your criteria.', 'textdomain' );
endif;

get_sidebar();
get_footer();
?>
```

## Common Template Tags

The Loop can display various post elements using template tags:

- `the_title()` – post or page title
- `the_content()` – main post or page content
- `the_excerpt()` – first 55 words followed by ellipsis or read more link
- `the_author()` – post author
- `the_category()` – associated categories
- `the_tags()` – associated tags
- `the_ID()` – post or page ID
- `the_time()` – post date/time (customizable with PHP formatting)
- `the_meta()` – custom fields
- `the_shortlink()` – shortened URL link
- `next_post_link()` – chronologically following post
- `previous_post_link()` – chronologically preceding post

## Conditional Tags

Template logic can incorporate conditional tags:

- `is_home()` – checks if current page is homepage
- `is_single()` – checks if displaying single post
- `is_page()` – checks if displaying single page
- `is_category()` – checks for specific category
- `is_tag()` – checks for specific tag
- `is_search()` – checks if search results page
- `is_404()` – checks if page doesn't exist
- `is_author()` – checks if author archive page
- `has_excerpt()` – checks if post has excerpt

## Basic Examples

### Blog Archive

```php
<?php
if ( have_posts() ) :
    while ( have_posts() ) : the_post();
        the_title( '<h2>', '</h2>' );
        the_post_thumbnail();
        the_excerpt();
    endwhile;
else:
    _e( 'Sorry, no posts matched your criteria.', 'textdomain' );
endif;
?>
```

### Individual Post

```php
<?php
if ( have_posts() ) :
    while ( have_posts() ) : the_post();
        the_title( '<h1>', '</h1>' );
        the_content();
    endwhile;
else:
    _e( 'Sorry, no pages matched your criteria.', 'textdomain' );
endif;
?>
```

## Intermediate Example: Conditional Styling

```php
<?php
// Start the Loop.
if ( have_posts() ) :
    while ( have_posts() ) : the_post();
        if ( in_category( 3 ) ) : ?>
        <div class="post-category-three">
        <?php else : ?>
        <div class="post">
        <?php endif; 

            the_title( '<h2>', '</h2>' ); 

            printf( __( 'Posted by %s', 'textdomain' ), get_the_author_posts_link() );

            ?>
            <div class="entry">
                <?php the_content() ?>
            </div>

            <?php
            _e( 'Posted in ', 'textdomain' ); the_category( ', ' ); 
        ?>
        </div>

    <?php
    endwhile; 

else :
    _e( 'Sorry, no posts matched your criteria.', 'textdomain' );

endif;
?>
```

## Multiple Loops

### Using rewind_posts()

To loop through the same query twice:

```php
<?php
// Start the main loop
if ( have_posts() ) :
    while ( have_posts() ) : the_post();
        the_title();
    endwhile;
endif;

// Use rewind_posts() to use the query a second time.
rewind_posts();

// Start a new loop
while ( have_posts() ) : the_post();
    the_content();
endwhile;
?>
```

### Creating Secondary Queries

```php
<?php
// The main query.
if ( have_posts() ) :
    while ( have_posts() ) : the_post();
        the_title();
        the_content();
    endwhile;
else :
    _e( 'Sorry, no posts matched your criteria.' );
endif;
wp_reset_postdata();

// The secondary query.
$secondary_query = new WP_Query( 'category_name=example-category' );

// The second loop.
if ( $secondary_query->have_posts() )
    echo '<ul>';
    while ( $secondary_query->have_posts() ) : $secondary_query->the_post();
        the_title( '<li>', '</li>' );
    endwhile;
    echo '</ul>';
endif;
wp_reset_postdata();
?>
```

## Resetting Multiple Loops

Three primary reset functions exist depending on query type:

### wp_reset_postdata()

Use with custom or multiple loops employing `WP_Query`. This function restores the global `$post` variable to the current post in the main query.

```php
<?php
$args = array( 'posts_per_page' => 3 ); 

$the_query = new WP_Query( $args ); 

if ( $the_query->have_posts() ) :
    while ( $the_query->have_posts() ) : $the_query->the_post();
        the_title();
        the_excerpt();
    endwhile;
else:
    _e( 'Sorry, no posts matched your criteria.', 'textdomain' );
endif; 

wp_reset_postdata();
?>
```

### wp_reset_query()

Use this function only after using `query_posts()`. This restores both the WP_Query and global `$post` data to the original main query. Note: `query_posts()` is not considered best practice and should be avoided.

```php
<?php wp_reset_query(); ?>
```

### rewind_posts()

Allows looping through the same query a second time without creating a new query object.

## Navigation

- **Previous:** [Template Tags](template-tags.md)
- **Next:** [Theme Functions](theme-functions.md)
