---
title: Accessibility
source: https://developer.wordpress.org/themes/classic-themes/functionality/accessibility/
updated: 2026-05-11
---

# Accessibility

**Changelog:**
- Rewritten and published: February 16, 2023
- First published: October 23, 2014

## Overview

A WordPress theme should generate pages that everyone can use, including those who cannot see or use a mouse.

To create an accessible theme, you need knowledge of web standards for HTML, CSS, and JavaScript, along with awareness of best practices and familiarity with the Web Content Accessibility Guidelines (WCAG).

Accessibility should be considered from the project's beginning as part of your specifications. Making the right decisions from the beginning, you can avoid making last-minute adjustments that can be costly, time-consuming, and of low quality.

## The four principles of web accessibility

### Perceivable

Content must be available to all. It should not depend on a specific device or browser or require a specific physical sense, such as sight or sound.

### Operable

Users must be able to move around and operate the final site effectively, whether they're using a keyboard, a mouse, or assistive technology.

### Understandable

The content should be presented in a manner that supports understanding, including supporting the construction of a mental model of the site for screen reader users.

### Robust

Content must be equally available across a wide range of user agents. Disabled users employ various assistive technologies including screen readers, voice recognition software, braille readers, and switches.

## Perceivable and understandable

### Color and color contrast

High color contrast between backgrounds and foregrounds improves readability. Theme authors must ensure that all background/foreground color contrasts for plain content text are within the level AA contrast ratio (4.5:1).

Requirements include:
* Color alone cannot be the sole identifier for controls, links, or error messages
* Linked text without decoration needs 3:1 contrast ratio versus surrounding text, plus other contrast requirements

### Resizable text

Users must access all content and functionality when text resizes up to 200% of original size. Text resizing must not trigger multi-dimensional scrolling or cause overlaps.

Recommendations include:
* Use relative units for font sizes and line heights
* Test themes across browsers and screen widths

### Images

**Non-decorative images** should include an `alt` attribute.

**Decorative images** should use CSS when possible. Images with `img` elements should have empty `alt=""` attributes.

**Featured images:** Alt attributes are defined in the media library. Unlinked featured images should describe the image; linked ones should reference the post title.

## Operable

### Controls

All controls must be usable with the keyboard on all screen sizes, including but not limited to buttons for opening and closing menus, submenus, any type of dialog, modal, and popup.

### Headings

Headings break content into logical sections and indicate importance. Screen reader users can scan the contents of a page by reading the headings, and navigating to a section via its heading. Headings must be used logically, not for styling purposes.

### Links

**Link text:** Link text should describe the resource it navigates to, remaining meaningful out of context. Bare URLs should never be used as links.

**Link underlining:** Links outside navigation menus should typically be underlined. The default browser style for the focus state should not be removed unless replaced with a more visible focus style.

**Skip Links:** These enable users to navigate directly to content or navigation. Common examples include:
* Skip to main navigation
* Skip to content
* Skip to footer

### Forms

Requirements include:
* Provide sufficient information to complete forms
* All input fields must have labels (placeholders don't replace labels)
* Include visible focus styles on inputs
* Group related controls using `fieldset` and `legend`
* Maintain tab order matching visual field order

## Robust

Use semantic HTML elements appropriately: buttons for actions, links for navigation. Content should remain available if users disable JavaScript and CSS.

## Resources

Make WordPress Accessible is the official WordPress Accessibility Team blog.

## Navigation

- **Previous:** [404 Pages](404-pages.md)
- **Next:** [Administration Menus](administration-menus.md)
