---
title: The Customizer JavaScript API
source: https://developer.wordpress.org/themes/classic-themes/customize-api/the-customizer-javascript-api/
updated: 2026-05-11
---

# The Customizer JavaScript API

**First published:** January 10, 2017  
**Last updated:** November 1, 2022

## Overview

In WordPress 4.1, expanded JavaScript APIs were introduced for all customizer objects. The entire JavaScript API is located in a single file, wp-admin/js/customize-controls.js, which contains models for all objects, core custom controls, and more.

## Preview JS and Controls JS

The customizer app divides into two distinct areas: the customizer controls pane and the customize preview. The preview runs in an iframe, meaning all JavaScript executes either in the controls pane or in the preview. The postMessage API facilitates communication between preview and controls.

There is one JS file for the controls pane, named `customize-controls.js` and one file for the customize preview, named `customize-preview.js`. All themes and plugins should follow this naming convention for clarity.

### Example: Controls-side JavaScript

```javascript
// Change the previewed URL to the selected page when changing the page_for_posts.
wp.customize(
	'page_for_posts',
	function( setting ) {
		setting.bind( function( pageId ) {
			pageId = parseInt( pageId, 10 );
			if ( pageId > 0 ) {
				api.previewer.previewUrl.set( api.settings.url.home + '?page_id=' + pageId );
			}
		});
	}
);
```

## Models for Controls, Sections, and Panels

Like PHP, each Customizer object type has a corresponding JavaScript object. There are `wp.customize.Control`, `wp.customize.Panel`, and `wp.customize.Section` models, as well as collections. Iterate over panels, sections, and controls via:

```javascript
wp.customize.panel.each( function ( panel ) { /* ... */ } );
wp.customize.section.each( function ( section ) { /* ... */ } );
wp.customize.control.each( function ( control ) { /* ... */ } );
```

## Relating Controls, Sections, and Panels together

In the JavaScript API, retrieve a control's section:

```javascript
id = wp.customize.control( 'blogname' ).section(); // returns title_tagline by default
```

Move a control to another section using the `section` state:

```javascript
wp.customize.control( 'blogname' ).section( 'nav' );
```

Similarly, retrieve a section's panel ID:

```javascript
id = wp.customize.section( 'sidebar-widgets-sidebar-1' ).panel(); // returns widgets by default
```

Obtain children of panels and sections:

```javascript
sections = wp.customize.panel( 'widgets' ).sections();
controls = wp.customize.section( 'title_tagline' ).controls();
```

## Contextual Panels, Sections, and Controls

`Control`, `Panel`, and `Section` instances have an `active` state. Methods `activate()` and `deactivate()` manipulate this `active` state:

```javascript
wp.customize.section( 'nav' ).deactivate(); // slide up
wp.customize.section( 'nav' ).activate({ duration: 1000 }); // slide down slowly
wp.customize.section( 'colors' ).deactivate({ duration: 0 }); // hide immediately
```

## Focusing UI Objects

The `focus()` method expands necessary elements, scrolls the target container into view, and puts browser focus on the first focusable element:

```javascript
wp.customize.control( 'page_on_front' ).focus()
```

The focus functionality implements autofocus via URL parameters:

* `…/wp-admin/customize.php?autofocus[panel]=widgets`
* `…/wp-admin/customize.php?autofocus[section]=colors`
* `…/wp-admin/customize.php?autofocus[control]=blogname`

## Priorities

Retrieve the priority for the widgets panel:

```javascript
priority = wp.customize.panel( 'widgets' ).priority(); // returns 110 by default
```

Dynamically change the priority:

```javascript
wp.customize.panel( 'widgets' ).priority( 1 ); // move Widgets to the top
```

## Navigation

- **Previous:** [Tools for Improved User Experience](tools-for-improved-user-experience.md)
- **Next:** [JavaScript/Underscore.js-Rendered Custom Controls](javascriptunderscore-js-rendered-custom-controls.md)
