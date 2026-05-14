---
title: Reworking Theme Files & Organization
source: https://developer.wordpress.org/themes/classic-themes/basics/reworking-theme-files-organization/
updated: 2026-05-11
---

# Reworking Theme Files & Organization

**Author:** lizkaraffa  
**Published:** December 9, 2014  
**Last Modified:** June 14, 2019

## Theme folder and file structure

While WordPress themes technically need only two foundational files (`index.php` and `style.css`), most themes contain numerous files that can quickly become disorganized.

The previous section covered creating `header.php`, `footer.php`, `page.php`, `home.php`, and `single.php` files. The Twenty Twelve theme serves as a good structural example.

The theme includes many files with descriptive names. Each file typically addresses a specific WordPress feature—for instance, `comments.php` manages comment display, while `image.php` handles image presentation. You only need to create files that your theme actually requires.

The primary template files reside in the theme's root directory, whereas JavaScript, language files, CSS, and page templates are organized into separate folders.

**Important note:** At this time there are **no required folders within a WordPress theme**. However, WordPress automatically recognizes certain conventional folders.

### Page templates folder

The `page-templates` folder (available since version 3.4.0) facilitates organizing custom page template files. WordPress automatically recognizes template files placed in this designated folder.

### Language folder

A `languages` folder can store translation files if you plan to make your theme usable across different languages through internationalization.

## Navigation

- **Previous:** [Post Types](post-types.md)
- **Next:** [Template Files](template-files.md)
