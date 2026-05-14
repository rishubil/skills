---
title: MB Custom Post Types & Custom Taxonomies - Meta Box Documentation
source: https://docs.metabox.io/extensions/mb-custom-post-type/
version: 5.12.0
fetched: 2026-05-11
---

This extension helps you create custom post types and custom taxonomies with a user-friendly interface.

## Creating post types

To create a new custom post type, go to **Meta Box » Post Types** and click **New Post Type**:

![create a new custom post type](https://imgur.elightup.com/3GKvMnb.png)

There are several settings divided into tabs. In most cases, you only need to enter the plural name, singular name, and slug in the **General** tab and click the **Publish** button to register the post type.

### Post type settings

If you want to customize the post type such as changing the menu icon or disabling the block editor (Gutenberg) for it, please see the settings below.

> [!-success] -success
> tip
> 
> From our experience, the most important settings are in the **Advanced** tab.

### Getting PHP code

If you're familiar with PHP, you might want to get the PHP code to register the post type. To do that, click the **Get PHP Code** button and copy the generated code. Then can insert it into your theme's `functions.php` file (or your plugin's file). After inserting, you can deactivate the extension to make your site a little bit faster.

## Creating taxonomies

To create a new custom taxonomy, go to **Meta Box » Taxonomies** and click **Add New**:

![create a new taxonomy](https://imgur.elightup.com/zKK4f87.png)

There are several settings divided into tabs. In most cases, you only need to enter the plural name, singular name, and slug in the **General** tab and click the **Publish** button to register the taxonomy.

The settings are similar to creating post types above.

### Taxonomy settings

If you want to customize the taxonomy such as setting the hierarchy or showing it in the post type list table, please see the settings below.

> [!-success] -success
> tip
> 
> From our experience, the most important settings are in the **Advanced** tab.

### Getting PHP code

If you're familiar with PHP, you might want to get the PHP code to register the taxonomy. To do that, click the **Get PHP Code** button and copy the generated code. Then can insert it into your theme's `functions.php` file (or your plugin's file). After inserting, you can deactivate the extension to make your site a little bit faster.

## Video tutorial

The video below shows you the steps and explains the settings for a custom post type (and also custom taxonomy):

## Notes

### Custom capabilities for custom post types

When creating custom post types, you have 3 options to set capabilities: copy from "post", copy from "page" or create custom capabilities. While copying from "post" or "page" is clear (the plugin applies the same capabilities from post or page for this custom post type), creating custom capabilities might be confusing.

When you select "custom" for capabilities, the plugin does the following (assumming we have a post type `book`):

- Set `'capability_type' => array( 'book', 'books' ),`, and
- Set `'map_meta_cap' => true`

These 2 steps will create the following capabilities for the post types:

```php
[edit_post]              => 'edit_book'
[read_post]              => 'read_book'
[delete_post]            => 'delete_book'

// Primitive capabilities used outside of map_meta_cap():

[edit_posts]             => 'edit_books'
[edit_others_posts]      => 'edit_others_books'
[publish_posts]          => 'publish_books'
[read_private_posts]     => 'read_private_books'

// Primitive capabilities used within map_meta_cap():

[read]                   => 'read',
[delete_posts]           => 'delete_books'
[delete_private_posts]   => 'delete_private_books'
[delete_published_posts] => 'delete_published_books'
[delete_others_posts]    => 'delete_others_books'
[edit_private_posts]     => 'edit_private_books'
[edit_published_posts]   => 'edit_published_books'
[create_posts]           => 'edit_books'
```

And thanks to `map_meta_cap`, the admin role can edit the posts types.

### Block templates with MB Blocks

Sometimes you want to load default blocks created by [MB Blocks](mb-blocks.md) when creating a new post. Block templates allow specifying a default initial state for an editor session. Use the argument `template` when registering the post type:

`'template'              => [     ['meta-box/{$block_id}'] ]`

### Reserved terms

There is a complete set of reserved keywords, or terms, in WordPress that should not be used in certain circumstances as they may conflict with core functionality. See more in [the documentation](https://codex.wordpress.org/Reserved_Terms).

## FAQ

> [!-info] -info
> Why do I see 404 errors (not found) for my custom post type?
> 
> The problem is that WordPress hasn't refreshed the rewrite rules for the custom post type. Please go to **Settings » Permalink** and re-save the settings.
> 
> [\# Link to this question](#why-do-i-see-404-errors-not-found-for-my-custom-post-type)

> [!-info] -info
> How do I customize the permalink for custom post types?
> 
> Meta Box only supports changing the rewrite slug for custom post types. If you want more customization for the permalink, you'll need a plugin like [Custom Post Type Permalinks](https://wordpress.org/plugins/custom-post-type-permalinks/) or if you're a developer, you can follow [this guide](https://www.shibashake.com/wp/custom-post-type-permalinks-part-2).
> 
> [\# Link to this question](#how-do-i-customize-the-permalink-for-custom-post-types)

> [!-info] -info
> How do I add custom taxonomies to the permalink of custom post types?
> 
> Similar to the question above, Meta Box only supports changing the rewrite slug for custom post types. If you want to add custom taxonomies to the permalink of custom post types, you'll need a plugin like [Custom Post Type Permalinks](https://wordpress.org/plugins/custom-post-type-permalinks/) or if you're a developer, you can follow [this guide](https://wordpress.stackexchange.com/q/94817/2051).
> 
> [\# Link to this question](#how-do-i-add-custom-taxonomies-to-the-permalink-of-custom-post-types)

> [!-info] -info
> How do I change a post type slug without losing posts?
> 
> After changing your post type slug, you can use the plugin [Post Type Switcher](https://wordpress.org/plugins/post-type-switcher/) to switch the posts from the old post type to the new one.
> 
> [\# Link to this question](#how-do-i-change-a-post-type-slug-without-losing-posts)

> [!-info] -info
> Will my posts be deleted if I remove a post type?
> 
> No, they're still in the database, but not visible. To show them again, create a post type with the old slug.
> 
> [\# Link to this question](#will-my-posts-be-deleted-if-i-remove-a-post-type)

> [!-info] -info
> Can I change the back-end UI for selecting taxonomy to radio buttons?
> 
> The default WordPress UI can't be changed to radio buttons. However, you can remove the default WordPress UI and create a [taxonomy field](../fields/taxonomy.md) with Meta Box, which supports many ways to display and choose terms, including radio buttons. See this video for how to do that:
> 
> [\# Link to this question](#can-i-change-the-back-end-ui-for-selecting-taxonomy-to-radio-buttons)

> [!-info] -info
> Can I use this extension without Meta Box?
> 
> Yes! This extension can work independently without Meta Box. If you only need custom post types and/or custom taxonomies (no custom fields), then you can install the extension for free from [WordPress.org](https://wordpress.org/plugins/mb-custom-post-type/).
> 
> [\# Link to this question](#can-i-use-this-extension-without-meta-box)
