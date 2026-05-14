---
title: Tools for Improved User Experience
source: https://developer.wordpress.org/themes/classic-themes/customize-api/tools-for-improved-user-experience/
updated: 2026-05-11
---

# Tools for Improved User Experience

**First published:** January 10, 2017  
**Last updated:** January 20, 2018

## Contextual Controls, Sections, and Panels

WordPress 4.0 and 4.1 introduced functionality allowing Customizer UI elements to display conditionally based on the previewed page. For example, if your theme only shows the header image on the front page, you can use the Customizer Manager's get_ methods to make those controls context-aware:

```php
// Hide core sections/controls when they aren't used on the current page.
$wp_customize->get_section( 'header_image' )->active_callback = 'is_front_page';
$wp_customize->get_control( 'blogdescription' )->active_callback = 'is_front_page';
```

The `active_callback` parameter accepts a callback function name. You can set this when registering new objects:

```php
$wp_customize->add_section( 'featured_content', array(
  'title'       => __( 'Featured Content', 'twentyfourteen' ),
  'description' => '...',
  'priority'        => 130,
  'active_callback' => 'is_front_page',
) );
```

For complex conditional logic, custom functions work well. If you don't require PHP 5.2 compatibility, use inline functions:

```php
'active_callback' => function () { return is_page(); }
```

For PHP 5.2 support, create a named function:

```php
'active_callback' => 'prefix_return_is_page';

function prefix_return_is_page() {
  return is_page();
}
```

The `active_callback` API operates identically for Controls, Sections, and Panels. Sections automatically hide when all contained controls are contextually hidden.

---

## Selective Refresh: Fast, Accurate Updates

WordPress 4.5 introduced Selective Refresh, which updates only preview areas with changed associated settings. Key advantages include:

* DRY (Don't Repeat Yourself) logic
* Accurate preview updates
* Association between preview elements and their corresponding settings/controls, with visible edit shortcuts

Unlike pure-JavaScript `postMessage` updates that require duplicating logic, Selective Refresh eliminates JavaScript and PHP duplication through Ajax requests that retrieve fresh markup for the preview.

### Registering Partials

```php
function foo_theme_customize_register( WP_Customize_Manager $wp_customize ) {
    $wp_customize->selective_refresh->add_partial( 'blogdescription', array(
        'selector' => '.site-description',
        'container_inclusive' => false,
        'render_callback' => function() {
            bloginfo( 'description' );
        },
    ) );
}
add_action( 'customize_register', 'foo_theme_customize_register' );
```

Key partial arguments:

| **Variable** | **Type** | **Description** |
|---|---|---|
| `settings` | array | Setting IDs associated with the partial. |
| `selector` | string | Targets page markup elements for refresh. |
| `container_inclusive` | boolean | Replaces entire container if true; otherwise replaces children only. Defaults to false. |
| `render_callback` | function | Produces markup rendered on refresh. |
| `fallback_refresh` | bool | Whether full-page refresh occurs if partial not found. |

### Selective Refresh JavaScript Events

Events that fire on `wp.customize.selectiveRefresh`:

* `partial-content-rendered`: Triggers when placement renders.
* `render-partials-response`: Fires when data returns from partial rendering requests.
* `partial-content-moved`: Occurs when widgets move between sidebars.
* `widget-updated`: Triggers when `WidgetPartial` refreshes.
* `sidebar-updated`: Fires when sidebars have refreshed/updated widgets.

### Widgets: Opting-In To Selective Refresh

#### Theme Support In Sidebars

```php
add_theme_support( 'customize-selective-refresh-widgets' );
```

**Important:** Selective refresh requires themes to include a `before_widget`/`after_widget` wrapper containing the widget's ID:

```php
function example_widgets_init() {
	register_sidebar(
		array(
			'name'          => esc_html__( 'Sidebar', 'example' ),
			'id'            => 'sidebar-1',
			'description'   => esc_html__( 'Add widgets here.', 'example' ),
			'before_widget' => '<section id="%1$s" class="widget %2$s">',
			'after_widget'  => '</section>',
			'before_title'  => '<h2 class="widget-title">',
			'after_title'   => '</h2>',
		)
	);
}
add_action( 'widgets_init', 'example_widgets_init' );
```

#### Widget Support

Widgets must individually opt-in:

```php
class Foo_Widget extends WP_Widget {
    public function __construct() {
        parent::__construct(
            'foo',
            __( 'Example', 'bar-plugin' ),
            array(
                'description' => __( 'An example widget', 'bar-plugin' ),
                'customize_selective_refresh' => true,
            )
        );
    }
```

---

## Using PostMessage For Improved Setting Previewing

The Customizer offers a JavaScript API for managing changes directly, enabling truly-live previewing through `postMessage` transport.

To implement postMessage, set the transport parameter when adding settings:

```php
$wp_customize->get_setting( 'blogname' )->transport        = 'postMessage';
$wp_customize->get_setting( 'blogdescription' )->transport = 'postMessage';
```

After setting transport to postMessage, create and enqueue JavaScript to update settings:

```php
function my_preview_js() {
  wp_enqueue_script( 'custom_css_preview', 'path/to/file.js', array( 'customize-preview', 'jquery' ) );
}
add_action( 'customize_preview_init', 'my_preview_js' );
```

JavaScript implementation:

```javascript
( function( $ ) {
  wp.customize( 'setting_id', function( value ) {
    value.bind( function( to ) {
      $( '#custom-theme-css' ).html( to );
    } );
  } );
} )( jQuery );
```

---

## Setting Validation

WordPress 4.6 introduced validation APIs for Customizer setting values.

### Validating Settings in PHP

Supply a `validate_callback` when registering settings:

```php
$wp_customize->add_setting( 'established_year', array(
    'sanitize_callback' => 'absint',
    'validate_callback' => 'validate_established_year'
) );
function validate_established_year( $validity, $value ) {
    $value = intval( $value );
    if ( empty( $value ) || ! is_numeric( $value ) ) {
        $validity->add( 'required', __( 'You must supply a valid year.' ) );
    } elseif ( $value < 1900 ) {
        $validity->add( 'year_too_small', __( 'Year is too old.' ) );
    } elseif ( $value > gmdate( 'Y' ) ) {
        $validity->add( 'year_too_big', __( 'Year is too new.' ) );
    }
    return $validity;
}
```

### Client-side Validation

```javascript
wp.customize( 'established_year', function ( setting ) {
	setting.validate = function ( value ) {
		var code, notification;
		var year = parseInt( value, 10 );

		code = 'required';
		if ( isNaN( year ) ) {
			notification = new wp.customize.Notification( code, {message: myPlugin.l10n.yearRequired} );
			setting.notifications.add( code, notification );
		} else {
			setting.notifications.remove( code );
		}
		return value;
	};
} );
```

---

## Notifications

Notifications provide user feedback based on control setting values. Error notifications add to a setting's `notifications` collection when validation returns a `WP_Error`.

Add JavaScript-based notifications:

```javascript
wp.customize( 'blogname', function( setting ) {
    setting.bind( function( value ) {
        var code = 'long_title';
        if ( value.length > 20 ) {
            setting.notifications.add( code, new wp.customize.Notification(
                code,
                {
                    type: 'warning',
                    message: 'This theme prefers title with max 20 chars.'
                }
            ) );
        } else {
            setting.notifications.remove( code );
        }
    } );
} );
```

## Navigation

- **Previous:** [Other Resources](other-resources.md)
- **Next:** [The Customizer JavaScript API](the-customizer-javascript-api.md)
