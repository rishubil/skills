---
title: Post Types
source: https://developer.wordpress.org/themes/classic-themes/basics/post-types/
updated: 2026-05-11
---

# Post Types

**Author:** Samuel Sidler  
**Published:** October 22, 2014  
**Last modified:** February 13, 2023

## Overview

WordPress organizes content into different categories called Post Types. All of the Post Types are stored in the same place — in the wp_posts database table — but are differentiated by a database column called post_type.

Post Types serve to categorize what type of content you are dealing with, and different Post Types typically connect to specific template files for display purposes.

## Default Post Types

WordPress includes several built-in Post Types:

- **Post** (Post Type: 'post')
- **Page** (Post Type: 'page')
- **Attachment** (Post Type: 'attachment')
- **Revision** (Post Type: 'revision')
- **Navigation menu** (Post Type: 'nav_menu_item')
- **Block templates** (Post Type: 'wp_template')
- **Template parts** (Post Type: 'wp_template_part')

### Post

Posts function in blog contexts with these characteristics:
- Displayed in reverse chronological order
- Include date and time stamps
- Support categories and tags
- Generate feed content

Template files include: `single`, `single-post`, `category`, `tag`, `taxonomy`, `archive`, `author`, `date`, `search`, `home`, and `index`.

### Page

Pages represent static content outside the blog stream:
- Without timestamps
- Exclude category/tag organization
- Support hierarchical parent-child relationships

Template files include: `page`, `front-page`, `search`, and `index`.

### Attachment

Attachments display media and files:
- Store uploaded file information
- Include metadata for images (size, thumbnails, location)

Template files include: `MIME_type`, `attachment`, `single-attachment`, `single`, and `index`.

## Custom Post Types

Developers can create custom post types, though this type of functionality should be placed/created in a plugin rather than themes. This preserves content portability when themes change.

Custom Post Type templates use these patterns:
- `single-{post-type}`
- `archive-{post-type}`
- `search`
- `index`

## Navigation

- **Previous:** [Organizing Theme Files](organizing-theme-files.md)
- **Next:** [Reworking Theme Files & Organization](reworking-theme-files-organization.md)
