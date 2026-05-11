---
title: Customizer Objects
source: https://developer.wordpress.org/themes/classic-themes/customize-api/customizer-objects/
updated: 2026-05-11
---

# Customizer Objects

**First published:** January 10, 2017  
**Last updated:** July 14, 2018

## Overview

The Customize API employs an object-oriented architecture with four primary component types: Panels, Sections, Settings, and Controls. Settings associate UI elements (controls) with settings that are saved in the database. Sections serve as organizational containers for controls, while panels group multiple sections together. All objects are managed through the `WP_Customize_Manager` class.

## Accessing the Customizer Manager

To modify Customizer objects, developers use the `customize_register` hook:

```php
function themeslug_customize_register( $wp_customize ) {
  // Do stuff with $wp_customize, the WP_Customize_Manager object.
}
add_action( 'customize_register', 'themeslug_customize_register' );
```

The manager provides `add_`, `get_`, and `remove_` methods for each object type, all functioning with unique IDs.

## Settings

Settings handle live-previewing, saving, and sanitization. When adding a setting, developers specify parameters including type, capability, default values, transport method, and sanitization callbacks.

Two primary setting types exist: options (stored in wp_options table, site-wide) and theme modifications (theme-specific). Themes should rarely if ever add settings of the option type.

**Important restriction:** Setting IDs matching patterns like `widget_*`, `sidebars_widgets[*]`, `nav_menu[*]`, or `nav_menu_item[*]` are reserved and should not be used.

Example theme setting:

```php
$wp_customize->add_setting( 'accent_color', array(
  'default' => '#f72525',
  'sanitize_callback' => 'sanitize_hex_color',
) );
```

Retrieve setting values using `get_theme_mod()` or `get_option()` functions.

## Controls

Controls create the primary user interface elements. Each control must associate with a setting. Core provides multiple built-in types:

- Input elements (text, email, number, range, date, etc.)
- Checkbox
- Textarea
- Radio buttons
- Select dropdowns
- Dropdown pages

Controls must be added to sections before display. Example textarea control:

```php
$wp_customize->add_control( 'custom_theme_css', array(
  'label' => __( 'Custom Theme CSS' ),
  'type' => 'textarea',
  'section' => 'custom_css',
) );
```

### Core Custom Controls

**Color Control:**
```php
$wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'color_control', array(
  'label' => __( 'Accent Color', 'theme_textdomain' ),
  'section' => 'media',
) ) );
```

**Media Control:** Implements WordPress media manager with mime type filtering for images or audio.

**Cropped Image Control:** Introduced in WordPress 4.3, provides image cropping interface for specific aspect ratios.

## Sections

Sections organize controls within the customizer interface. Use the `add_section()` method:

```php
$wp_customize->add_section( 'custom_css', array(
  'title' => __( 'Custom CSS' ),
  'description' => __( 'Add custom CSS here' ),
  'priority' => 160,
) );
```

Core sections and their priorities:

| Title | ID | Priority |
|-------|----|---------:|
| Site Title & Tagline | title_tagline | 20 |
| Colors | colors | 40 |
| Header Image | header_image | 60 |
| Background Image | background_image | 80 |
| Menus (Panel) | nav_menus | 100 |
| Widgets (Panel) | widgets | 110 |
| Static Front Page | static_front_page | 120 |
| Additional CSS | custom_css | 200 |

## Panels

Introduced in WordPress 4.0, panels create hierarchical groupings beyond sections. Themes should not register their own panels in most cases. Panels are designed for distinct feature contexts like Widgets or Menus.

Panels must contain at least one section, which must contain at least one control, to display.

```php
$wp_customize->add_panel( 'menus', array(
  'title' => __( 'Menus' ),
  'priority' => 160,
) );
$wp_customize->add_section( $section_id , array(
  'title' => $menu->name,
  'panel' => 'menus',
) );
```

## Custom Controls, Sections, and Panels

Developers create custom objects by subclassing base classes: `WP_Customize_Control`, `WP_Customize_Section`, and `WP_Customize_Panel`.

Example custom control:

```php
class WP_New_Menu_Customize_Control extends WP_Customize_Control {
  public $type = 'new_menu';
  
  public function render_content() {
  ?>
    <button class="button button-primary" id="create-new-menu-submit" tabindex="0"><?php _e( 'Create Menu' ); ?></button>
  <?php
  }
}
```

## Navigation

- **Previous:** [Theme Options – The Customize API](index.md)
- **Next:** [Other Resources](other-resources.md)
