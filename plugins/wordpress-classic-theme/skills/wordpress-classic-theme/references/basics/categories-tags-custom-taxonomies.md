---
title: Categories, Tags, & Custom Taxonomies
source: https://developer.wordpress.org/themes/classic-themes/basics/categories-tags-custom-taxonomies/
updated: 2026-05-11
---

# Categories, Tags, & Custom Taxonomies

## Overview

This WordPress documentation article explains how taxonomies organize content. The piece uses a recipe website as an example to illustrate the distinction between categories, tags, and custom taxonomies.

## Key Concepts

**Categories vs. Tags vs. Taxonomies**

Categories provide broad groupings—like "Breakfast" or "Desserts" on a recipe site. Tags offer more specific descriptors, such as "chocolate" or "ginger." Taxonomies are the method of classifying content and data in WordPress. Categories and tags are actually default taxonomy types.

**Default Taxonomies in WordPress**

The platform includes three default taxonomy types:
- Categories (hierarchical)
- Tags (non-hierarchical)
- Post formats

**Terms Explained**

Terms are individual items within a taxonomy. For instance, "dogs," "cats," and "sheep" would be terms within an "Animal" taxonomy. These can be created through the WordPress admin or via the `wp_insert_term()` function.

**Database Storage**

Taxonomies use three database tables: `wp_terms`, `wp_term_taxonomy`, and `wp_term_relationships`.

**Custom Taxonomies**

Users can create custom taxonomies for specialized organization needs. The documentation recommends putting this functionality in a plugin to preserve content during theme changes.

## Navigation

- **Previous:** [Theme Basics](index.md)
- **Next:** [Conditional Tags](conditional-tags.md)
