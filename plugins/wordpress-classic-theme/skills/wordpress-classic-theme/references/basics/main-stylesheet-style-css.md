---
title: Main Stylesheet (style.css)
source: https://developer.wordpress.org/themes/classic-themes/basics/main-stylesheet-style-css/
updated: 2026-05-11
---

# Main Stylesheet (style.css)

**Published:** December 22, 2016  
**Last updated:** March 1, 2021

## Overview

The style.css is a stylesheet (CSS) file required for every WordPress theme. It controls the presentation (visual design and layout) of the website pages.

## Location

For WordPress to identify theme files as valid, the style.css file needs to be located in the root directory of your theme, not a subdirectory.

## Basic Structure

WordPress reads the header comment section of style.css to show theme details in the Appearance dashboard.

### Example

```css
/*
Theme Name: Twenty Twenty
Theme URI: https://wordpress.org/themes/twentytwenty/
Author: the WordPress team
Author URI: https://wordpress.org/
Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor. Organizations and businesses have the ability to create dynamic landing pages with endless layouts using the group and column blocks. The centered content column and fine-tuned typography also makes it perfect for traditional blogs. Complete editor styles give you a good idea of what your content will look like, even before you publish. You can give your site a personal touch by changing the background colors and the accent color in the Customizer. The colors of all elements on your site are automatically calculated based on the colors you pick, ensuring a high, accessible color contrast for your visitors.
Tags: blog, one-column, custom-background, custom-colors, custom-logo, custom-menu, editor-style, featured-images, footer-widgets, full-width-template, rtl-language-support, sticky-post, theme-options, threaded-comments, translation-ready, block-styles, wide-blocks, accessibility-ready
Version: 1.3
Requires at least: 5.0
Tested up to: 5.4
Requires PHP: 7.0
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Text Domain: twentytwenty
This theme, like WordPress, is licensed under the GPL.
Use it to make something cool, have fun, and share what you've learned with others.
*/
```

WordPress Theme Repository uses the number after "Version" in this file to determine if the theme has a new version available.

### Explanations

Items marked with (*) are required for WordPress Theme Repository submission.

- **Theme Name** (*): The theme's name
- **Theme URI**: Web page with theme information
- **Author** (*): Developer's name or organization
- **Author URI**: Developer's website URL
- **Description** (*): Brief theme overview
- **Version** (*): Theme version in X.X or X.X.X format
- **Requires at least** (*): Minimum WordPress version (X.X format)
- **Tested up to** (*): Latest tested WordPress version
- **Requires PHP** (*): Minimum PHP version
- **License** (*): Theme license type
- **License URI** (*): License document URL
- **Text Domain** (*): Translation identifier string
- **Tags**: Keywords for filtering and discovery
- **Domain Path**: Translation file location (defaults to `/languages`)

After the required header section, style.css can contain anything a regular CSS file has.

## Style.css for a Child Theme

Child themes require a **Template** field in the style.css header:

```css
/*
Theme Name: My Child Theme
Template: twentytwenty
*/
```

## Navigation

- **Previous:** [Linking Theme Files & Directories](linking-theme-files-directories.md)
- **Next:** [Organizing Theme Files](organizing-theme-files.md)
