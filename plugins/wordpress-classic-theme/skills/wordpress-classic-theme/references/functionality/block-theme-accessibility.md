---
title: Block Theme Accessibility
source: https://developer.wordpress.org/themes/classic-themes/functionality/block-theme-accessibility/
updated: 2026-05-11
---

# Block Theme Accessibility

**Author:** Benachi  
**Last Updated:** August 29, 2023

## Overview

Block themes in WordPress support and simplify accessibility implementation.

## Landmarks

Block themes enable landmarks through Group, Template part, and Query blocks. Developers can create landmarks using block markup with `"tagName":"header"` or via the site editor's Advanced section, which offers options including `<header>`, `<main>`, `<section>`, `<article>`, `<aside>`, and `<footer>`.

**Code example:**
```
<!-- wp:group {"tagName":"header","layout":{"type":"constrained"}} -->
<header class="wp-block-group"><!-- wp:site-title /--></header>
<!-- /wp:group -->
```

## Skip to Content

Selecting the `<main>` landmark on Group, Template part, or Query blocks automatically generates a Skip to Content link, enhancing keyboard navigation for users.

**Code example:**
```
<!-- wp:group {"tagName":"main","layout":{"type":"constrained"}} -->
<main class="wp-block-group"><!-- wp:heading -->
<h2 id="hello-world">Hello World</h2>
<!-- /wp:heading -->
```

## Accessible Navigation Menu

The Navigation block provides built-in accessibility features: responsive view support, keyboard navigation, `<nav>` landmark insertion, and ARIA attributes (`aria-label`, `aria-hidden`).

## Navigation

- **Previous:** [Administration Menus](administration-menus.md)
- **Next:** [Core-Supported Features](core-supported.md)
