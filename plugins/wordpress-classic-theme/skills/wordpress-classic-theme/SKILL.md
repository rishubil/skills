---
name: wordpress-classic-theme
description: Specialist skill for developing WordPress classic (PHP-based) themes. Use when creating a classic theme from scratch or when implementing or debugging classic-theme-specific features such as template hierarchy, The Loop, theme functions, sidebars, widgets, or the Customizer API. Does not cover block themes (FSE).
---

# WordPress Classic Theme Development Guide

> Official documentation: https://developer.wordpress.org/themes/classic-themes/

A WordPress classic theme is a PHP-based theme that requires `index.php` and `style.css` as mandatory files. It works directly with WordPress-specific mechanisms such as template hierarchy, The Loop, theme functions, and the Customizer API.

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Template Hierarchy** | The rules that determine which template file to use based on the requested URL |
| **The Loop** | The core WordPress pattern for fetching posts from the database and iterating over them |
| **Template Tags** | Output functions used inside templates, such as `the_title()` and `the_content()` |
| **Theme Functions** | Hooks and features registered in `functions.php` |
| **Conditional Tags** | Conditional branching functions such as `is_single()` and `is_archive()` |
| **Customizer API** | The theme options UI with live preview support |

## Basic File Structure

```
my-theme/
├── style.css          # Required: theme metadata + styles
├── index.php          # Required: default template
├── functions.php      # Hook and feature registration
├── header.php
├── footer.php
├── sidebar.php
├── single.php         # Single post
├── page.php           # Page
├── archive.php        # Archive
├── search.php
└── 404.php
```

## Common Patterns

### style.css Theme Header

```css
/*
Theme Name: My Theme
Theme URI: https://example.com
Author: Your Name
Description: A classic WordPress theme.
Version: 1.0.0
License: GNU General Public License v2 or later
Text Domain: my-theme
*/
```

### functions.php Skeleton

```php
function my_theme_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    add_theme_support( 'menus' );
    register_nav_menus( [ 'primary' => __( 'Primary Menu', 'my-theme' ) ] );
}
add_action( 'after_setup_theme', 'my_theme_setup' );

function my_theme_scripts() {
    wp_enqueue_style( 'my-theme-style', get_stylesheet_uri() );
    wp_enqueue_script( 'my-theme-script', get_template_directory_uri() . '/js/main.js', [], '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'my_theme_scripts' );
```

### The Loop

```php
<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
    <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
    <?php the_excerpt(); ?>
<?php endwhile; else : ?>
    <p><?php esc_html_e( 'No posts found.', 'my-theme' ); ?></p>
<?php endif; ?>
```

## Local Documentation (consult first)

The `references/` folder in this skill directory contains the full official documentation as markdown files. When checking template files, hooks, functions, or the Customizer API, **do not open external URLs — Read the local files for accurate information**.

### references/ Directory Structure

```
references/
├── index.md                              # Classic theme overview
├── your-first-theme.md                   # Creating your first theme
├── basics/
│   ├── index.md                          # Basics overview
│   ├── template-files.md                 # Template files
│   ├── template-hierarchy.md             # Template hierarchy
│   ├── template-tags.md                  # Template tags
│   ├── the-loop.md                       # The Loop
│   ├── theme-functions.md                # functions.php
│   ├── post-types.md                     # Post types
│   ├── conditional-tags.md               # Conditional tags
│   ├── categories-tags-custom-taxonomies.md  # Taxonomies
│   ├── main-stylesheet-style-css.md      # style.css
│   ├── organizing-theme-files.md         # File structure
│   ├── including-css-javascript.md       # Loading CSS/JS
│   ├── linking-theme-files-directories.md # File paths
│   ├── reworking-theme-files-organization.md
│   └── tools-resources.md
├── templates/
│   ├── index.md                          # Template files overview
│   ├── post-template-files.md            # Post templates
│   ├── page-template-files.md            # Page template files
│   ├── page-templates.md                 # Page templates (custom)
│   ├── attachment-template-files.md      # Attachment templates
│   ├── custom-post-type-template-files.md # CPT templates
│   ├── taxonomy-templates.md             # Taxonomy templates
│   └── partial-and-miscellaneous-template-files/
│       ├── index.md                      # Partial templates
│       └── comment-template.md           # Comment template
├── functionality/
│   ├── index.md                          # Functionality overview
│   ├── custom-headers.md                 # Custom headers
│   ├── custom-backgrounds.md             # Custom backgrounds
│   ├── custom-logo.md                    # Custom logo
│   ├── custom-front-page-templates.md    # Front page
│   ├── featured-images-post-thumbnails.md # Featured images
│   ├── navigation-menus.md               # Navigation menus
│   ├── sidebars.md                       # Sidebars
│   ├── widgets.md                        # Widgets
│   ├── pagination.md                     # Pagination
│   ├── post-formats.md                   # Post formats
│   ├── sticky-posts.md                   # Sticky posts
│   ├── 404-pages.md                      # 404 pages
│   ├── media/
│   │   ├── index.md
│   │   ├── images.md
│   │   ├── video.md
│   │   ├── audio.md
│   │   └── galleries.md
│   ├── internationalization.md           # Internationalization (i18n)
│   ├── localization.md                   # Localization (l10n)
│   ├── accessibility.md                  # Accessibility
│   ├── administration-menus.md           # Admin menus
│   ├── core-supported.md                 # Core-supported features
│   └── block-theme-accessibility.md
├── customize-api/
│   ├── index.md                          # Customizer API overview
│   ├── customizer-objects.md             # Panel, Section, Setting, Control
│   ├── the-customizer-javascript-api.md  # JS API
│   ├── javascriptunderscore-js-rendered-custom-controls.md
│   ├── tools-for-improved-user-experience.md # Selective Refresh, etc.
│   ├── advanced-usage.md                 # Advanced usage
│   └── other-resources.md
└── references/
    ├── index.md                          # Reference list
    ├── list-of-template-tags.md          # Full template tag list
    └── list-of-conditional-tags.md       # Full conditional tag list
```

### Commonly Referenced Documents

| Topic | File Path |
|-------|-----------|
| Creating your first theme | `references/your-first-theme.md` |
| Template hierarchy | `references/basics/template-hierarchy.md` |
| The Loop | `references/basics/the-loop.md` |
| Template tag list | `references/references/list-of-template-tags.md` |
| Conditional tag list | `references/references/list-of-conditional-tags.md` |
| functions.php | `references/basics/theme-functions.md` |
| Loading CSS/JS | `references/basics/including-css-javascript.md` |
| Navigation menus | `references/functionality/navigation-menus.md` |
| Sidebars and widgets | `references/functionality/sidebars.md` |
| Custom logo | `references/functionality/custom-logo.md` |
| Featured images | `references/functionality/featured-images-post-thumbnails.md` |
| Customizer basics | `references/customize-api/index.md` |
| Customizer objects | `references/customize-api/customizer-objects.md` |
| Page templates | `references/templates/page-templates.md` |
| Taxonomy templates | `references/templates/taxonomy-templates.md` |

To find documentation, Read the paths above directly or search with `find <skill-path>/references -name "*.md" | grep <keyword>`.
