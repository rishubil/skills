---
title: Template Hierarchy
source: https://developer.wordpress.org/themes/classic-themes/basics/template-hierarchy/
updated: 2026-05-11
---

# Template Hierarchy

## Overview

The WordPress template hierarchy is a system that determines which template files render specific pages on your site. WordPress uses the query string to decide which template or set of templates should be used to display the page.

## How It Works

WordPress follows a three-step process:

1. Matches the query string to identify the page type (search, category, etc.)
2. Selects templates based on hierarchy order
3. Looks for matching template files and uses the first matching template file as specified by the hierarchy

If no matching template exists, WordPress falls back to `index.php`.

## Key Template Types

**Home & Front Page:**
- `front-page.php` takes precedence
- `home.php` for blog post index
- Falls back to `index.php`

**Single Posts & Pages:**
- Single posts check: `single-{post-type}-{slug}.php` → `single-{post-type}.php` → `single.php`
- Pages check: `page-{slug}.php` → `page-{id}.php` → `page.php`

**Archives:**
- Categories: `category-{slug}.php` → `category-{id}.php` → `category.php`
- Tags: `tag-{slug}.php` → `tag-{id}.php` → `tag.php`
- Custom post types: `archive-{post_type}.php`

**Special Pages:**
- Search: `search.php`
- 404 errors: `404.php`
- Author archives: `author-{nicename}.php` → `author-{id}.php`

## Child Theme Behavior

Child theme templates override parent theme templates at the same specificity level. More specific child templates take precedence over general parent templates.

## Filter Hierarchy

Developers can manipulate template selection using filters like `{$type}_template` (e.g., `author_template`, `page_template`) to customize hierarchy behavior programmatically.

## Navigation

- **Previous:** [Template Files](template-files.md)
- **Next:** [Template Tags](template-tags.md)
