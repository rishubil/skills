---
title: Meta Box AIO - Meta Box Documentation
source: https://docs.metabox.io/extensions/meta-box-aio/
version: 5.12.0
fetched: 2026-05-11
---

Meta Box AIO is a special plugin that contains all the extensions. It allows you to install only one plugin and have everything, so you can have the plugin list short and clean.

Meta Box AIO includes the Meta Box framework, so you don't have to install it separately.

## Settings page

The plugin has a settings page under *Meta Box → Extensions*, where you can enable/disable the extensions you need/don't need.

![meta box aio settings page](https://docs.metabox.io/assets/images/all-extensions-90a56f98bf37cdc62745f6e00b423d99.png)

Check/uncheck the checkbox to enable/disable the corresponding extensions. Then click **Save Changes**.

## Filters

While the settings page and the notification to install free extensions are great for users, developers might want to hide them from normal users. To do that, Meta Box AIO provides some filters:

### mb\_aio\_show\_settings

This filter is used to show/hide the settings page. The callback function should return `true` to show the settings page, or `false` to hide it.

To hide the settings page, use the following code:

```php
add_filter( 'mb_aio_show_settings', '__return_false' );
```

### mb\_aio\_extensions

This filter allows you to change the list of enabled premium extensions. Thus, enable/disable modules by just coding.

This filter takes a list of enabled extensions (their slugs), and returns the filtered list.

For example, the code below enables only the [MB Builder](meta-box-builder.md) extension:

```php
add_filter( 'mb_aio_extensions', function( $extensions ) {
    $extensions = ['meta-box-builder'];

    // You can also do
    // $extensions[] = 'meta-box-builder';

    return $extensions;
} );
```

## Tools

These are the Meta Box tools for managing custom fields and custom post types. They help you clean up and optimize your WordPress database.

This set of tools is only available in **Meta Box AIO**. To use it, go to **Meta Box** > **Tools**:

![Interface of Meta Box tools](https://docs.metabox.io/assets/images/tools-0c3520fe505d6ebd3d3bf6dcb4b99d38.png)

> [!-warning] -warning
> Important
> 
> Please back up your database before using any of these tools. This can't be reversed.

### Remove orphan fields

This tool removes all custom fields that are not attached to a valid post, term, or user.

Just click on the **Remove** button, then Meta Box will notify you of the number of custom fields that have been deleted for each object.

![Successfully remove orphan fields](https://docs.metabox.io/assets/images/remove-orphan-field-2604d9a93e99594893f426bc418bb8c6.png)

### Remove custom fields

Use this tool to remove the specific fields via their field ID.

Simply enter the meta key and choose the object type (post, term, user or all of them).

![Remove custom fields](https://docs.metabox.io/assets/images/remove-custom-field-4c46c6f537c8d78412864ea506e94d78.png)

### Change custom field key

This is useful when you want to change the custom field key without losing existing data. Meta Box allows you to select the meta key from the suggestion list.

![Change custom field key](https://docs.metabox.io/assets/images/change-meta-key-ddd55e66907250866283c6446e5a7406.png)

After that, you can check the update meta key in the database.

![Change ID in database](https://docs.metabox.io/assets/images/field-id-change-database-16a6de28e6d2d9eaa3fd7c9b2326d0d9.png)

### Change post type

This tool is to change the slug of a post type, page, or media. For the post type, its posts will be converted to the new one.

![Change post type](https://docs.metabox.io/assets/images/change-post-type-734132bb3f80e7d2ed8bb0c5fb9fb44e.png)

## Notes

When an extension is enabled in Meta Box AIO and is activated as an individual plugin, the individual plugin will has higher priority and will be used. The version bundled inside Meta Box AIO will not be used.

This behavior is expected and has a good benefit: whenever we release a new version for individual extensions, you can try them first on your website to ensure compatibility before updating the whole Meta Box AIO package.
