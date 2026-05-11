---
title: JavaScript/Underscore.js-Rendered Custom Controls
source: https://developer.wordpress.org/themes/classic-themes/customize-api/javascriptunderscore-js-rendered-custom-controls/
updated: 2026-05-11
---

# JavaScript/Underscore.js-Rendered Custom Controls

**Author:** Nick Halsey  
**Published:** January 10, 2017  
**Last Modified:** March 15, 2018

## Overview

WordPress 4.1 introduced the capability to render JavaScript-intensive controls entirely through JavaScript, enabling more dynamic behavior for controls added dynamically. The Color and Media controls in core utilize this API.

## Registered Control Types

To support multiple controls sharing the same template, a registration mechanism was introduced:

```php
add_action( 'customize_register', 'prefix_customize_register' );
function prefix_customize_register( $wp_customize ) {
  // Define a custom control class, WP_Customize_Custom_Control.
  // Register the class so that its JS template is available in the Customizer.
  $wp_customize->register_control_type( 'WP_Customize_Custom_Control' );
}
```

Templates for all registered control types are printed via `WP_Customize_Manager::print_control_templates()`.

## Sending PHP Control Data to JavaScript

`WP_Customize_Control` exports these variables by default:

* `type`
* `label`
* `description`
* `active` (boolean state)

Extend default parameters by overriding `WP_Customize_Control::to_json()` in your custom subclass:

```php
public function to_json() {
  parent::to_json();
  $this->json['statuses'] = $this->statuses;
  $this->json['defaultValue'] = $this->setting->default;
}
```

## JS/Underscore Templating

After registering your control class and exporting custom variables, create the rendering template by overriding `WP_Customize_Control::content_template()` to replace `WP_Customize_Control::render_content()`. Override `render_content()` with an empty function in your subclass.

Example from the color control template:

```php
class WP_Customize_Color_Control extends WP_Customize_Control {
  public $type = 'color';

  public function content_template() {
    ?>
    <# var defaultValue = '';
    if ( data.defaultValue ) {
      if ( '#' !== data.defaultValue.substring( 0, 1 ) ) {
        defaultValue = '#' + data.defaultValue;
      } else {
        defaultValue = data.defaultValue;
      }
      defaultValue = ' data-default-color=' + defaultValue;
    } #>
    <label>
      <# if ( data.label ) { #>
        <span class="customize-control-title">{{{ data.label }}}</span>
      <# } #>
      <# if ( data.description ) { #>
        <span class="description customize-control-description">{{{ data.description }}}</span>
      <# } #>
      <div class="customize-control-content">
        <input class="color-picker-hex" type="text" maxlength="7" placeholder="<?php esc_attr_e( 'Hex Value' ); ?>" {{ defaultValue }} />
      </div>
    </label>
    <?php
  }
}
```

The template uses `<# #>` notation for JavaScript statements. All exported control data resides in the `data` object. Double braces `{{}}` print escaped variables; triple braces `{{{ }}}` print unescaped content.

## Putting the pieces together

Implementing the new API in a custom control requires these steps:

1. Make `render_content()` an empty override function.
2. Create `content_template()` containing the old `render_content()` code.
3. Export necessary custom class variables through `to_json()` modifications.
4. Convert PHP from `render_content()` into a JS template using `<# #>` for statements and `{{ }}` for variables.
5. **Register the custom control class.** Execute `$wp_customize->register_control_type( 'YourControlClass' );`

## Navigation

- **Previous:** [The Customizer JavaScript API](the-customizer-javascript-api.md)
- **Next:** [Advanced Usage](advanced-usage.md)
