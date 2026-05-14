---
title: Template Tags
source: https://developer.wordpress.org/themes/classic-themes/basics/template-tags/
updated: 2026-05-11
---

# Template Tags

**Published:** October 22, 2014  
**Last Updated:** November 17, 2022

## Overview

Template tags are fundamental WordPress functions that retrieve content from your database. They enable theme developers to pull dynamic content—from blog titles to complete sidebars—into theme files.

## What is a Template Tag?

A template tag consists of three components: a PHP code tag, a WordPress function, and optional parameters. Examples include:

- `get_header()` - retrieves the header.php file
- `get_footer()` - retrieves the footer.php file
- `the_title()` - fetches the page or post title
- `bloginfo('name')` - retrieves the blog title

Parameters allow developers to ask for specific pieces of information and format the information in a certain way.

## Why Use Template Tags

Template tags offer several advantages:

1. **Maintainability**: Creating a single header.php file referenced across multiple templates (single.php, page.php, etc.) means updates automatically propagate everywhere.

2. **Dynamic Content**: Instead of hardcoding static values like `<title>My Personal Website</title>`, the `bloginfo('name')` tag automatically pulls the current site title from the database.

3. **Code Organization**: Encapsulating content chunks makes themes more manageable and understandable.

## How to Use Template Tags

Basic usage is straightforward—simply call the function in your template file:

```php
get_header();
```

### Parameters

Different template tags accept different parameters. For example:

```php
bloginfo( 'name' );      // Returns blog name
bloginfo( 'version' );   // Returns WordPress version
```

Consult the code reference for specific parameter options.

### Using Template Tags Within the Loop

Many template tags require the WordPress Loop—the PHP structure that generates pages. These tags must appear within the loop structure:

```php
if ( have_posts() ) :
    while ( have_posts() ) :
        the_post();
        // Template tags go here
    endwhile;
else :
    _e( 'Sorry, no posts matched your criteria.', 'devhub' );
endif;
```

Tags requiring the loop include:
- `the_content()`
- `the_excerpt()`
- `next_post()`
- `previous_post()`

Tags that don't require the loop (like `wp_list_cats()` and `wp_list_pages()`) can be placed in sidebars, headers, or footers.

## See Also

- [Conditional Tags](https://developer.wordpress.org/themes/basics/conditional-tags/)
- [Complete list of Template Tags](https://developer.wordpress.org/themes/references/list-of-template-tags/)

## Navigation

- **Previous:** [Template Hierarchy](template-hierarchy.md)
- **Next:** [The Loop](the-loop.md)
