---
title: Your First Theme
source: https://developer.wordpress.org/themes/classic-themes/your-first-theme/
updated: 2026-05-11
---

# Your First Theme

**Author:** Samuel Sidler  
**Published:** July 31, 2014  
**Last Modified:** December 14, 2023

## Table of Contents

- [Block Theme](#block-theme)
  - [Required Files](#required-files)
  - [Step 1 – Create a theme folder](#step-1--create-a-theme-folder)
  - [Step 2 – Create a style.css file](#step-2--create-a-stylecss-file)
  - [Step 3 – Create a theme.json file](#step-3--create-a-themejson-file)
  - [Step 4 – Add index.html inside the templates folder](#step-4--add-indexhtml-inside-the-templates-folder)
  - [Step 5 – Install and activate your theme](#step-5--install-and-activate-your-theme)
- [Classic Theme](#classic-theme)
  - [Required Files](#required-files-1)
  - [Step 1 – Create a theme folder](#step-1--create-a-theme-folder-1)
  - [Step 2 – Create a style.css file](#step-2--create-a-stylecss-file-1)
  - [Step 3 – Create an index.php file](#step-3--create-an-indexphp-file)
  - [Step 4 – Install Your Theme](#step-4--install-your-theme)
  - [Step 5 – Activate Your Theme](#step-5--activate-your-theme)
  - [Using Your First Theme](#using-your-first-theme)
- [What have we learned?](#what-have-we-learned)
- [Up Next](#up-next)

---

## Block Theme

This section covers creating a block theme in WordPress.

### Required Files

A block theme requires only three essential files:

- **index.html** - The main template displaying your post list, placed inside a `templates` folder
- **style.css** - File for styling content
- **theme.json** - Structured file for setting style properties

For advanced development, you may also add:

**Templates directory** with files such as:
- index.html
- archive.html
- single.html
- page.html

**Parts directory** with template parts like:
- header.html
- footer.html
- sidebar.html

### Step 1 – Create a theme folder

Start by creating a new folder named **my-first-theme** where all theme files will reside.

### Step 2 – Create a style.css file

Use a basic text editor (Notepad on Windows, TextEdit on Mac) to create a `style.css` file. Add this code:

```css
/*
 Theme Name: My First WordPress Theme */
```

### Step 3 – Create a theme.json file

Create `theme.json` in the root folder with this content:

```json
{
 "version": 2,
 "settings": {
   "layout": {
     "contentSize": "840px",
     "wideSize": "1100px"
   }
 }
}
```

### Step 4 – Add index.html inside the templates folder

Create a `templates` folder in your theme directory, then add an `index.html` file inside it.

Your theme structure should now look like:

```
my-first-theme/
├── templates/
│   └── index.html
├── style.css
└── theme.json
```

### Step 5 – Install and activate your theme

Create a ZIP file of your theme directory (e.g., `my-first-theme.zip`). In WordPress admin, navigate to **Appearance > Themes > Add New > Upload**. Upload the ZIP file, then install and activate.

**Congratulations – you've created your first WordPress block theme!**

For more information, download the default Twenty Twenty-Three theme as a reference.

---

## Classic Theme

### Required Files

As noted in the "What is a Theme" section, only two files are essential for a WordPress theme to function:

- An `index.php` file to display your post list
- A `style.css` file to style the content

As themes grow more complex, developers typically separate code into multiple template files, commonly including:

- `header.php`
- `index.php`
- `sidebar.php`
- `footer.php`

This guide focuses on launching your basic theme first; advanced file structures will be covered later in the handbook.

### Step 1 – Create a theme folder

Create a new folder named **my-first-theme**. This folder will contain all theme files.

### Step 2 – Create a style.css file

Using a basic text editor, create a `style.css` file and add this code:

```css
/*
Theme Name: My First WordPress Theme
*/

body {
background: #21759b;
}
```

### Step 3 – Create an index.php file

Create an `index.php` file in your theme folder with this code:

```php
<!DOCTYPE html>
<html>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<title><?php wp_title( '|', true, 'right' ); ?></title>
<link rel="stylesheet" href="<?php echo esc_url( get_stylesheet_uri() ); ?>" type="text/css" />
<?php wp_head(); ?>
</head>
<body>
<h1><?php bloginfo( 'name' ); ?></h1>
<h2><?php bloginfo( 'description' ); ?></h2>

<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>

<h3><?php the_title(); ?></h3>

<?php the_content(); ?>
<?php wp_link_pages(); ?>
<?php edit_post_link(); ?>

<?php endwhile; ?>

<?php
if ( get_next_posts_link() ) {
next_posts_link();
}
?>
<?php
if ( get_previous_posts_link() ) {
previous_posts_link();
}
?>

<?php else: ?>

<p>No posts found. :(</p>

<?php endif; ?>
<?php wp_footer(); ?>
</body>
</html>
```

### Step 4 – Install Your Theme

Copy your theme folder to the `wp-content/themes` directory in your development environment for testing.

### Step 5 – Activate Your Theme

Navigate to **Admin > Appearance > Themes** and activate your theme.

### Using Your First Theme

**Congratulations – you've just made your first WordPress theme!**

When activated, your theme displays basic styling with your site title and posts. While functional, this theme lacks the design refinement of production themes—but it's an excellent foundation.

---

## What have we learned?

Though this basic theme is missing advanced functionality, it demonstrates the core principles of WordPress theme development that remain consistent over time.

The key here is not to get caught up in how all those other things are done now, but to understand the guiding principles that ensure longevity.

All websites share common structural elements: headers, content areas, menus, sidebars, and footers. Creating WordPress themes is fundamentally about organizing these components effectively.

---

## Up Next

[Chapter 2: Theme Basics](https://developer.wordpress.org/themes/basics/) explores deeper theme concepts including:

- Template Tags
- The Loop
- Theme Functions
- Conditional Tags
- And more

---

**← Previous:** [Classic themes](index.md)

**Next →** [Theme Basics](basics/index.md)
