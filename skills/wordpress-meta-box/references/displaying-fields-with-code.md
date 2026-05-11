---
title: Displaying fields with code - Meta Box Documentation
source: https://docs.metabox.io/displaying-fields-with-code/
version: 5.12.0
fetched: 2026-05-11
---

If you're a developer and familiar with changing template file with PHP code, you can use Meta Box helper functions to display fields:

- [`rwmb_get_value()`](functions/rwmb-get-value.md): to get a field value as a variable
- [`rwmb_the_value()`](functions/rwmb-the-value.md): to display a field

In addition, we also provide [`rwmb_meta()`](functions/rwmb-meta.md) function, which is a wrapper of the 2 functions above which:

- Returns the HTML output for rich-content fields: `map`, `osm`, and `oembed`, same as `rwmb_the_value()`,
- Returns the same value as `rwmb_get_value()` for other field types.

Now open your template file for the single event content. Usually, it's `template-parts/content.php`, `single-event.php` or `single.php` file, depending on your theme structure. Then add the following code below the content area:

```php
<?php
/**
 * Template part for displaying single post content
 */
?>

<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
        <header class="entry-header">
                <?php the_title( '<h1 class="entry-title">', '</h1>' ); ?>
        </header>

        <div class="entry-content">
                <?php the_content(); ?>

                <p>
                    <strong>Date and time:</strong> <?php rwmb_the_value( 'datetime' ) ?>
                </p>
                <p>
                    <strong>Location:</strong> <?php rwmb_the_value( 'location' ) ?>
                </p>
                <p>
                    <strong>Map:</strong>
                </p>
                <?php rwmb_the_value( 'map' ) ?>
        </div>
</article>
```

> [!-warning] -warning
> Block themes
> 
> For block themes, everything is blocks and there's no PHP template files. In that case, please use the [MB Views](extensions/mb-views.md) extension.

All functions accept the following parameters:

| Name | Description |
| --- | --- |
| `$field_id` | The field ID. Required. |
| `$args` | Extra arguments for some field types (image, file, etc.). Can be array or a string in format `param1=value1&param2=value2`. See more details in field types. Optional. |
| `$object_id` | Object ID that custom fields are got from. Optional. If not present, the current post ID is used. |
| `$echo` | Echo the HTML output (`true` - default) or return it (`false`). Applied only for `rwmb_the_value()` function. |

## FAQ

> [!-info] -info
> Why does my site crash when I deactivate Meta Box?
> 
> If you're using our helper functions in your theme, then they become unavailable when Meta Box is deactivated. You can fix that by going to the admin area » Plugins and re-activate Meta Box.
> 
> Alternatively, you can add the following code into your theme's `functions.php` file to make the error go away, however, the custom fields won't display, either.
> 
> ```php
> if ( ! function_exists( 'rwmb_the_value' ) ) {
>     function rwmb_the_value( $key, $args = [], $post_id = null ) {
>         return null;
>     }
> }
> if ( ! function_exists( 'rwmb_get_value' ) ) {
>     function rwmb_get_value( $key, $args = [], $post_id = null ) {
>         return null;
>     }
> }
> if ( ! function_exists( 'rwmb_meta' ) ) {
>     function rwmb_meta( $key, $args = [], $post_id = null ) {
>         return null;
>     }
> }
> ```
> [\# Link to this question](#why-does-my-site-crash-when-i-deactivate-meta-box)

> [!-info] -info
> Can I use WordPress's get\_post\_meta() function to get custom field value?
> 
> Absolutely. Our helper function is just a wrapper of WordPress's `get_post_meta` function.
> 
> [\# Link to this question](#can-i-use-wordpresss-get_post_meta-function-to-get-custom-field-value)

> [!-info] -info
> Why don't I see values of custom fields?
> 
> There are some cases where you register custom fields conditionally or only for the back end like you wrap the code under `is_admin()`. In that case, make sure you remove the condition and register custom fields for both the back end and front end.
> 
> [\# Link to this question](#why-dont-i-see-values-of-custom-fields)

> [!-info] -info
> Can I use a page builder to show Meta Box fields?
> 
> Absolutely. We have official support for Beaver Builder and Elementor. Some page builders already have built-in support for Meta Box like Oxygen Builder, Bricks, and Brizy. See the [list of compatible plugins](compatibility.md) and refer to their docs for how to use them with Meta Box.
> 
> [\# Link to this question](#can-i-use-a-page-builder-to-show-meta-box-fields)
