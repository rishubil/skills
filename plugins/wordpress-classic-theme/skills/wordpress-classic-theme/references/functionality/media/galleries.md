---
title: Galleries
source: https://developer.wordpress.org/themes/classic-themes/functionality/media/galleries/
updated: 2026-05-11
---

# Galleries

**First published:** January 13, 2017  
**Last updated:** November 1, 2022

## Galleries

Image galleries showcase pictures on WordPress sites effectively. WordPress includes a built-in **Create Gallery** feature in the media uploader for simple gallery creation.

**Note:** Images must exist in your media library before creating a gallery.

### Gallery shortcode

The **Gallery** feature enables adding image galleries to posts and pages using a shortcode.

Basic shortcode syntax:

```php
[gallery]
```

When using `[gallery]` without the `ids` argument, only images attached to that post or page display.

For multiple specific images:

```php
[gallery ids="10, 205, 552, 607"]
```

To use shortcodes in template files, employ the `do_shortcode()` function:

```php
<?php echo do_shortcode( '[gallery]' ); ?>
```

With IDs:

```php
<?php echo do_shortcode( '[gallery ids="10, 205, 552, 607"]' ); ?>
```

### Supported Options

#### Orderby

'orderby' specifies thumbnail display order. Default is 'menu_order'.

* menu_order
* title
* post_date
* rand
* ID

#### Order

Specifies sort order: ASC or DESC.

```php
[gallery order="DESC" orderby="ID"]
```

#### columns

Specifies gallery column count. Default is 3.

```php
[gallery columns="4"]
```

#### IDs

Loads images with specific post IDs.

#### Size

Determines the image size: "thumbnail", "medium", "large", "full" and custom sizes. Default is "thumbnail".

#### itemtag

The HTML tag enclosing each gallery item. Default is "dl".

#### icontag

The HTML tag enclosing each thumbnail icon. Default is "dt".

#### captiontag

The HTML tag enclosing each caption. Default is "dd".

#### Link

Specify image link destination:

```php
[gallery link="file"]
```

Options: file (link to image file), none (no link).

#### Include

Include specifies comma-separated attachment IDs to display only those images:

```php
[gallery include="23,39,45"]
```

#### Exclude

```php
[gallery exclude="21,32,43"]
```

Note: include and exclude cannot be used together.

## Navigation

- **Previous:** [Audio](audio.md)
- **Next:** [Images](images.md)
