---
title: Template Files
source: https://developer.wordpress.org/themes/classic-themes/basics/template-files/
updated: 2026-05-11
---

# Template Files

**Published:** January 14, 2015  
**Last Updated:** January 21, 2023

## In this article

* [Template Terminology](#template-terminology)
* [Template files](#template-files)
* [Template partials](#template-partials)
* [Common WordPress template files](#common-wordpress-template-files)
* [Using template files](#using-template-files)

---

Template files serve as the foundational building blocks for WordPress themes.

## Template Terminology

The term "template" carries multiple meanings in WordPress theme development:

* Template files exist within themes to control how your site displays
* Template Hierarchy is the logic WordPress uses to decide which theme template file(s) to use, depending on the content being requested
* Page Templates are designed for pages, posts, and custom post types to modify their presentation

In classic themes, Template Tags are built-in WordPress functions you can use inside a template file to retrieve and display data such as `the_title()` and `the_content()`. Block themes employ blocks instead of template tags.

## Template files

WordPress themes consist of template files that control layout and design:

* Classic themes use PHP files combining HTML, Template Tags, and PHP code
* Block themes use HTML files with markup representing blocks

When visitors access your site, WordPress loads a template based on the request, with content type determined by the associated Post Type. The Template Hierarchy determines which file loads based on request type and theme availability.

The index template is the catch-all template if a more-specific template can not be found. While only index is required, most themes include multiple templates for various content types.

## Template partials

Template parts are reusable template segments included within other templates, such as headers. Common examples include:

* `header.php` or `header.html` for site headers
* `footer.php` or `footer.html` for footers
* `sidebar.php` or `sidebar.html` for sidebars

You can create additional custom template partials for inclusion elsewhere. In block themes, template parts must reside in a dedicated parts folder.

## Common WordPress template files

**index.php (classic) or index.html (block)**
The primary template file, required for all themes.

**style.css**
The main stylesheet, required for all themes and contains theme information.

**rtl.css**
Right-to-left stylesheet, automatically included for RTL languages.

**front-page.php (classic) or front-page.html (block)**
Used for the site front page when present, regardless of Reading settings.

**home.php (classic) or home.html (block)**
Default front page template; displays latest posts if no static front page is set.

**singular.php (classic) or singular.html (block)**
Fallback template for single posts or pages when specific templates don't exist.

**single.php (classic) or single.html (block)**
Used when visitors request a single post.

**single-{post-type}.php (classic) or single-{post-type}.html (block)**
Template for custom post types, such as `single-book.php`.

**archive-{post-type}.php (classic) or archive-{post-type}.html (block)**
Used for custom post type archives, such as `archive-books.php`.

**page.php (classic) or page.html (block)**
Template for individual page requests.

**page-{slug}.php (classic) or page-{slug}.html (block)**
Template for specific pages, such as `page-about.php`.

**category.php (classic) or category.html (block)**
Used when visitors browse posts by category.

**tag.php (classic) or tag.html (block)**
Used for tag-based post browsing.

**taxonomy.php (classic) or taxonomy.html (block)**
Template for custom taxonomy term requests.

**author.php (classic) or author.html (block)**
Displays author archive pages.

**date.php (classic) or date.html (block)**
Used for date-based post archives.

**archive.php (classic) or archive.html (block)**
Fallback archive template, overridden by more specific templates like category.php.

**search.php (classic) or search.html (block)**
Displays search results.

**attachment.php (classic) or attachment.html (block)**
Template for viewing single attachments like images or PDFs.

**image.php (classic) or image.html (block)**
Specialized template for image attachments; falls back to attachment.php.

**404.php (classic) or 404.html (block)**
Displays when requested content cannot be found.

**comments.php**
Comments template for classic themes; block themes use blocks instead.

## Using template files

### Classic themes

Classic themes utilize Template Tags to display dynamic information, include files, and customize sites. Common functions include:

* `get_header()` - includes the header
* `get_sidebar()` - includes the sidebar
* `get_footer()` - includes the footer
* `get_search_form()` - includes the search form
* `get_template_part()` - includes custom theme files

Example usage:

```php
<?php get_sidebar(); ?>
<?php get_template_part( 'featured-content' ); ?>
<?php get_footer(); ?>
```

### Block themes

Block themes use blocks instead of template tags. To include template parts, add block markup with the part's slug name:

```html
<!-- wp:template-part {"slug":"header"} /-->
(your page content)
<!-- wp:template-part {"slug":"footer"} /-->
```

For search functionality, use the search block markup:

```html
<!-- wp:search {"label":"Search","buttonText":"Search"} /-->
```

## Navigation

- **Previous:** [Reworking Theme Files & Organization](reworking-theme-files-organization.md)
- **Next:** [Template Hierarchy](template-hierarchy.md)
