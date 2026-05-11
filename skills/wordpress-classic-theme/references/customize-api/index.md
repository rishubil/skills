---
title: Theme Options – The Customize API
source: https://developer.wordpress.org/themes/classic-themes/customize-api/
updated: 2026-05-11
---

# Theme Options – The Customize API

**Published:** October 23, 2014  
**Last Updated:** October 1, 2025

## Overview

The Customize API, also known as the Customizer, serves as a framework for live-previewing any change to WordPress. It delivers an integrated platform where users can modify various theme and site elements including colors, layouts, widgets, and menus.

## Key Features

**User Capability Control**: The Customize API enables granular permission settings. While administrators typically access all options by default, other users can be granted access to specific customization features as needed.

**Contextual Display**: The interface intelligently shows relevant options based on the front-end preview context. For instance, widget areas only display when the user is viewing a page that contains them within the preview window.

**Universal Implementation**: Both themes and plugins can contribute options to the Customizer, making it the recommended approach for adding customization features to WordPress themes.

## Documentation Resources

The page recommends developers examine core customizer code (files containing "customize") as the authoritative resource beyond inline documentation within the code itself.

## Sub-pages

- [Customizer Objects](customizer-objects.md)
- [Other Resources](other-resources.md)
- [Tools for Improved User Experience](tools-for-improved-user-experience.md)
- [The Customizer JavaScript API](the-customizer-javascript-api.md)
- [JavaScript/Underscore.js-Rendered Custom Controls](javascriptunderscore-js-rendered-custom-controls.md)
- [Advanced Usage](advanced-usage.md)

## Navigation

- **Previous:** [Sticky Posts](../functionality/sticky-posts.md)
- **Next:** [Customizer Objects](customizer-objects.md)
