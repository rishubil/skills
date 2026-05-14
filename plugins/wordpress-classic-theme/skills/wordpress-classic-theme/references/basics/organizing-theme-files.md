---
title: Organizing Theme Files
source: https://developer.wordpress.org/themes/classic-themes/basics/organizing-theme-files/
updated: 2026-05-11
---

# Organizing Theme Files

**Author:** Samuel Sidler  
**Published:** August 2, 2014  
**Last Modified:** October 25, 2022

## Theme folder and file structure

While WordPress themes technically only require two files (`index.php` in classic themes and `index.html` in block themes, and `style.css`), they usually comprise many files that can quickly become disorganized.

The Twenty Seventeen Theme demonstrates recommended organization practices. Here's its typical structure:

```
.
├── assets (dir)/
│   ├── css (dir)
│   ├── images (dir)
│   └── js (dir)
├── inc (dir)
├── template-parts (dir)/
│   ├── footer (dir)
│   ├── header (dir)
│   ├── navigation (dir)
│   ├── page (dir)
│   └── post (dir)
├── 404.php
├── archive.php
├── comments.php
├── footer.php
├── front-page.php
├── functions.php
├── header.php
├── index.php
├── page.php
├── README.txt
├── rtl.css
├── screenshot.png
├── search.php
├── searchform.php
├── sidebar.php
├── single.php
└── style.css
```

This organization places main template files in the root directory, JavaScript and CSS assets in the assets folder, template parts in the template-parts subdirectory, and core functionality functions in the inc directory.

**Important notes:**
- No folders are required in classic themes
- Block themes must place templates in a **templates** folder and parts in a **parts** folder
- `style.css` should reside in the root directory of your theme not within the CSS directory

## Languages folder

Best practice involves internationalizing your theme for translation. The `languages` folder typically contains a .pot file and translated .mo files. While this is the default folder name, it's customizable—just update the `load_theme_textdomain()` function accordingly.

## Navigation

- **Previous:** [Main Stylesheet (style.css)](main-stylesheet-style-css.md)
- **Next:** [Post Types](post-types.md)
