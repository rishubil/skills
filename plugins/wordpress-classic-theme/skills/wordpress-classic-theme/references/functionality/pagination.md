---
title: Pagination
source: https://developer.wordpress.org/themes/classic-themes/functionality/pagination/
updated: 2026-05-11
---

# Pagination

**Author:** Samuel Sidler  
**Published:** October 23, 2014  
**Last Modified:** October 25, 2022

## Using Pagination to Navigate Post Lists

Pagination allows your user to page back and forth through multiple pages of content. WordPress implements pagination in two primary scenarios:

* When viewing post lists where the number of posts exceeds what fits on a single page
* When breaking up longer posts manually using the `<!--nextpage-->` tag

The most common implementation breaks up extensive post lists into separate pages. By default, WordPress displays 10 posts per page, though site administrators can adjust this setting via **Admin > Settings > Reading**.

## Examples

### Loop with Pagination

```php
<?php if ( have_posts() ) : ?>

    <!-- Start the pagination functions before the loop. -->
    <div class="nav-previous alignleft"><?php next_posts_link( 'Older posts' ); ?></div>
    <div class="nav-next alignright"><?php previous_posts_link( 'Newer posts' ); ?></div>
    <!-- End the pagination functions before the loop. -->

	<!-- Start of the main loop. -->
	<?php while ( have_posts() ) : the_post();  ?>

	<!-- the rest of your theme's main loop -->

    <?php endwhile; ?>
    <!-- End of the main loop -->

    <!-- Start the pagination functions after the loop. -->
    <div class="nav-previous alignleft"><?php next_posts_link( 'Older posts' ); ?></div>
    <div class="nav-next alignright"><?php previous_posts_link( 'Newer posts' ); ?></div>
    <!-- End the pagination functions after the loop. -->

<?php else : ?>

	<?php _e( 'Sorry, no posts matched your criteria.' ); ?>

<?php endif; ?>
```

### Methods for displaying pagination links

When using pagination functions outside the template file containing the loop, you must reference the global `$wp_query` variable:

```php
function your_themes_pagination() {
	global $wp_query;
	echo paginate_links();
}
```

#### Simple Pagination

**posts_nav_link**

The `posts_nav_link()` function represents one of the simplest approaches. Place it after your loop to generate links to both the next and previous post pages:

```php
posts_nav_link();
```

**next_posts_link & previous_posts_link**

```php
next_posts_link();
previous_posts_link();
```

#### Numerical Pagination

**For WordPress 4.1+**

```php
the_posts_pagination();
```

**For WordPress prior to 4.1**

```php
echo paginate_links();
```

#### Pagination Between Single Posts

For individual blog posts, use on single.php template below the loop:

```php
previous_post_link();
next_post_link();
```

### Pagination within a post

To enable pagination within individual posts, insert the `<!--nextpage-->` tag in post content. Your single.php template must include the `wp_link_pages()` function within the loop:

```php
<?php if ( have_posts() ) : ?>
	<?php while ( have_posts() ) : the_post(); ?>
		<?php the_content(); ?>
		<?php wp_link_pages(); ?>
	<?php endwhile; ?>
<?php endif; ?>
```

## Navigation

- **Previous:** [Navigation Menus](navigation-menus.md)
- **Next:** [Post Formats](post-formats.md)
