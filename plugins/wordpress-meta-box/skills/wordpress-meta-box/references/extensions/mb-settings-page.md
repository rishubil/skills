---
title: MB Settings Page - Meta Box Documentation
source: https://docs.metabox.io/extensions/mb-settings-page/
version: 5.12.0
fetched: 2026-05-11
---

MB Settings Page helps you create settings pages for your website. You can use it to create a theme options page, or a settings page for your plugin, or a custom settings page for clients' websites.

The plugins provide several styles for settings pages where you can have tabs or meta boxes. We try to keep the styles similar to the default WordPress UI as much as possible.

![Settings page with WordPress-native tabs](https://imgur.elightup.com/yb9Admk.png)

Settings page with WordPress-native tabs

![Settings page with left tabs](https://imgur.elightup.com/QoaD4la.png)

Settings page with left tabs

![Settings page with meta boxes](https://i0.wp.com/metabox.io/wp-content/uploads/2015/12/settings-page.jpg)

Settings page with meta boxes

> [!-success] -success
> success
> 
> You can also combine styles, for example using tabs with meta boxes.

## Creating settings pages

To create a settings page, go to **Meta Box » Settings Pages** and click **Add New**.

![Creating settings pages](https://docs.metabox.io/assets/images/create-settings-page-d7627f2416f120db6f4fa9c68031deb0.png)

On the new screen, you'll see all details for the settings page.

> [!-info] -info
> info
> 
> The instruction above uses [MB Builder](meta-box-builder.md), an extension providing the UI to create fields, and is already bundled in [Meta Box Lite](https://metabox.io/lite/) and [Meta Box AIO](meta-box-aio.md). If you prefer to use code, please see below.

### Settings

There are several settings for a settings page. All of them are self-explained. We also add some tooltips next to the setting title to give you more information if needed. Here is the list of the settings with the explanation:

| Name | Description |
| --- | --- |
| Menu type | Whether to show the settings page as a top-level menu or a submenu of an existing menu. Depending on the menu type, several settings below will appear. |
| Show menu after | Select the position of the menu. Available only when menu type is Top-level menu. |
| Default first submenu title | If you create a top-level settings page with some sub-settings pages, you can set the default first submenu title here. |
| Icon type | What type of menu icon. Available only when menu type is Top-level menu. Supports Dashicons, Font Awesome, SVG, and custom URL. |
| Icon | The icon for the menu. Available only when the icon type is Dashicons or Font Awesome. |
| Icon SVG | The custom SVG icon for the menu. Available only when the icon type is SVG. |
| Icon URL | The URL for the custom icon. Available only when the icon type is Custom URL. |
| Parent menu | If you select menu type "Submenu", then you can select the parent menu for this sub-menu here. |
| Required capability | The required capability to access the settings page. |
| Custom CSS class | Custom CSS for the wrapper div in the settings page, so you can add your styling. |
| Style | How do you want to style the settings page? Supports "Boxes" which has same the style as normal WordPress meta boxes (like in the edit post screen with the classic editor) and "No boxes" which has the same style as WordPress settings pages. |
| Columns | The number of columns in the meta boxes. Can be 1 (the same as WordPress settings pages) or 2 (the same as the edit post screen). |
| Tabs | Array of tabs (key => label) for the settings page. |
| Tab style | Specify the tab style, which can be "Top" (WordPress-native style) or "Left". |
| Custom submit button | The custom text for submit button. |
| Custom message | The custom message is displayed when saving options. |
| Help content | The content displayed when clicking on the "Help" button on the top right (near the "Screen Options" button) and is organized in tabs. Each tab has its own title and content. |
| Customizer | Whether to show the settings page in the Customizer as a panel. See the "Creating Customizer settings" section for details. |
| Customizer only | Whether to show only as a Customizer panel, no admin settings page. |
| Network | Make the settings page network-wide (in a multisite environment). |

Each settings page also has its own ID and option that specifies which option in the database to store data into. By default, the plugin set the option name the same as the ID. You can change it if you want on the **Settings Page** on the top of the settings page:

![Changing settings page ID and option name](https://docs.metabox.io/assets/images/setting-page-id-95958a89d7410340c842a16b1a9ac4d2.png)

> [!-info] -info
> ID vs. option name
> 
> ID is for internal use for Meta Box, like the settings page URL or reference in the field group definition. The option name is for storing and getting data from the database. They can be the same (works in most cases) or different.

> [!-success] -success
> success
> 
> If you want to use make the data of the settings page compatible with Customizer settings for the current theme, e.g. using theme mods to store the data, then set the option name to `theme_mods_$themeslug`.

You can create as many settings pages as you want. You can also create a top-level settings page and several sub-settings pages.

## Using code

If you're a developer and prefer using code to create settings pages, use the filter `mb_settings_pages`. This is a sample code to create a theme options page under the Appearance menu:

```php
add_filter( 'mb_settings_pages', function ( $settings_pages ) {
    $settings_pages[] = [
        'id'          => 'theme-slug',
        'option_name' => 'theme_slug',
        'menu_title'  => 'Theme Options',
        'parent'      => 'themes.php',
    ];
    return $settings_pages;
} );
```

The `mb_settings_pages` filter takes an array of settings pages as the argument. The callback function must return an array of settings pages.

Each settings page is defined by an array of the following options, which is similar to the UI in the **MB Builder** extension above:

| Name | Description |
| --- | --- |
| `id` | Settings page ID. Required. |
| `option_name` | Option name where settings data is saved to. Optional. Takes `id` if missed. If you want to use theme mods, then set this to `theme_mods_$themeslug`. |
| `class` | Custom CSS for the wrapper div. |
| `menu_title` | Menu title. Optional. Takes `page_title` if missed. |
| `page_title` | Page title. Optional. Takes `menu_title` if missed. Note: either `menu_title` or `page_title` (or both) must have value. |
| `capability` | Required capability to access the settings page. Optional. Default `edit_theme_options`. |
| `icon_url` | The icon for the menu. Supports [Dashicons](https://developer.wordpress.org/resource/dashicons/) (`dashicons-icon-name`), [FontAwesome free](https://fontawesome.com/search?o=r&m=free) (`fa fa-home`), SVG (`data:image/svg+xml;base64...`) and custom URL. |
| `position` | Menu position (number). See below for the list of default WordPress menu positions. |
| `parent` | The ID of the parent page, if you want the settings page to be a submenu. Optional. Can be a WordPress menu or custom settings page menu. See below for the list of WordPress page IDs. |
| `submenu_title` | Set this to the default submenu title (first submenu) if the settings page is a top-level menu. Optional. |
| `help_tabs` | The content is displayed when clicking on the Help button on the top right (near the Screen Options button). See below for details. |
| `style` | How do you want to style the settings page? Supports `boxes` which has same the style as normal WordPress meta boxes (like in the edit post screen) and `no-boxes` which has the same style as WordPress settings pages. In `no-boxes` style, each meta box is a section of the settings page. |
| `columns` | The number of columns in the meta boxes. Can be 1 (the same as WordPress settings pages) or 2 (the same as the edit post screen). |
| `tabs` | Array of tabs for the settings page. See the "Tabs" section for more details. |
| `tab_style` | Specify the tab style, which can be `default` (WordPress-native style) or `left` (tabs are put on the left of the settings page). See the "Tabs" section below for details. |
| `submit_button` | The custom text for submit button. Optional. |
| `message` | The custom message displayed when saving options. Optional. |
| `customizer` | Whether to show the settings page in the Customizer as a panel. `true` or `false` (default). Optional. See below for details. |
| `customizer_only` | Whether to show only as a Customizer panel, no admin settings page. `true` or `false` (default). Optional. |
| `network` | Make the settings page network-wide (in a multisite environment). `true` or `false` (default). Optional. |

### WordPress menus

This is the list of default WordPress menus with their ID (used for the `parent` parameter) and position (used for the `position` parameter):

| Menu | ID | Position |
| --- | --- | --- |
| Dashboard | `index.php` | 2 |
| Posts | `edit.php` | 5 |
| Media | `upload.php` | 10 |
| Links | `link-manager.php` | 15 |
| Pages | `edit.php?post_type=page` | 20 |
| Comments | `edit-comments.php` | 25 |
| Appearance | `themes.php` | 60 |
| Plugins | `plugins.php` | 65 |
| Uses | `users.php` | 70 |
| Tools | `tools.php` | 75 |
| Settings | `options-general.php` | 80 |

### Tabs

The list of tabs is defined in the `tabs` parameter. A tab can have or doesn't have an icon and can be set like this:

```php
'tabs'        => [
    'general' => 'General Settings',         // No icon
    'design'  => [                           // With icon
        'label' => 'Design Customization',
        'icon'  => 'dashicons-admin-customizer',
    ],
],
```

The `icon` parameter can be a [Dashicons](https://developer.wordpress.org/resource/dashicons/) icon or the URL of your custom icon. You can also use another icon library like FontAwesome by specifying its class (e.g. `fa fa-home`), but in that case, you have to enqueue the font yourself.

This screenshot shows the left tab navigation with icons:

![left tab navigation](https://imgur.elightup.com/QoaD4la.png)

### Help tabs

WordPress has a nice feature that allows us to define instructions, and guidelines in the "Help" section of each admin screen. To see the help content, click the "Help" button on the top right, near the "Screen Options" button.

![Help tabs in the Posts screen](https://imgur.elightup.com/B7YRruB.png)

The content is organized into tabs and you can set it in the MB Builder's UI or with code.

If you use code, set the help tabs as follows:

```php
'help_tabs' => [
    [
        'title'   => 'General',
        'content' => '<p>This tab displays the general information about the theme.</p>',
    ],
    [
        'title'   => 'Homepage',
        'callback' => 'my_custom_function',
        'priority' => 10,
    ],
],
```

Each tab has the following parameters:

| Parameter | Description |
| --- | --- |
| `title` | The tab title. |
| `content` | The tab content. |
| `callback` | Custom callback to render the tab content. Optional. |
| `priority` | The priority of the tab, used for ordering. Optional. Default 10. |

## Settings fields

After creating a settings page, you need to create settings fields for it. Creating settings fields for settings pages is [similar as for posts](../custom-fields.md#how-to-create-custom-fields). You can do it [with UI using MB Builder](meta-box-builder.md#creating-custom-fields) or [with code](../creating-fields-with-code.md).

If you use MB Builder to create fields, make sure to select the correct settings page in the Location settings:

![select settings page in MB Builder](data:image/png;base64,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)

If you use code, then you need to hook to `rwmb_meta_boxes` and set a param `settings_pages` to the settings page(s) you want to add to, like this:

```php
add_filter( 'rwmb_meta_boxes', function ( $meta_boxes ) {
    $meta_boxes[] = [
        'id'             => 'general',
        'title'          => 'General',
        'context'        => 'normal',
        'settings_pages' => 'theme-slug',
        'tab'            => 'general',
        'fields'         => [
            [
                'name' => 'Logo',
                'id'   => 'logo',
                'type' => 'file_input',
            ],
        ],
    ];
    return $meta_boxes;
} );
```

> [!-warning] -warning
> warning
> 
> When using tabs, you must define the `tab` parameter for all meta boxes to make them appear in corresponding tabs. Missing the `tab` parameter makes the meta boxes hidden.

Note:

- If you want to add the meta box to 2 or more settings pages, set it to an array of settings pages' IDs.
- If you set the settings page to have 2 columns, then the value for `context` accepts `normal` for the main content area and `side` for the right sidebar.

## Customizer

**MB Settings Pages** allows you to create settings panels & sections for the Customizer. Using Customizer gives users a better experience because they can preview the settings in real time.

### Panels & sections

When creating Customizer settings, it's important to understand that:

- A settings page is mapped to a Customizer panel
- Each meta box in the settings page is mapped to a Customizer section

To bring a settings page to the Customizer, turn on the **Customizer** settings when you create the settings page as follows:

![Set a settings page as a Customizer panels](https://docs.metabox.io/assets/images/customizer-in-settings-page-b5c36befef34621f4902db8bb4e8d998.png)

Then go to the **Appearance » Customize** and you'll see the settings page is available as follows:

![A new panel in the Customizer](https://imgur.elightup.com/D78hKyG.png)

A new panel in the Customizer

![Meta boxes become Customize sections](https://imgur.elightup.com/AfaWiGK.png)

Meta boxes become Customize sections

By default, the settings page is available in the both Customizer as well as in the admin area. If you don't want it in the admin area, choose the **Customizer only**.

If you use code, use the following code:

```php
add_filter( 'mb_settings_pages', function ( $settings_pages ) {
    $settings_pages[] = [
        'id'          => 'rubik',
        'option_name' => 'theme_mods_justread',
        'menu_title'  => 'Theme Options',
        'parent'      => 'themes.php',
        'customizer'  => true,
        'customizer_only'  => true,
    ];

    return $settings_pages;
} );
```

This is a quick video that demonstrates how to use MB Settings Page to create custom panels, sections, and fields in the Customizer with code:

### Top-level sections

Sometimes you don't want the top-level panel that creates too much hierarchy (panel → sections → fields). You just want top-level sections (sections → fields). That will help users to navigate to your settings in the Customizer faster and easier.

> [!-warning] -warning
> warning
> 
> This can be done with code only.

In that case, you need to do 2 steps:

**Step 1:** Remove the code that registers settings pages as you don't need settings pages anymore. If you use MB Builder, delete the settings page entry.

**Step 2:** In each meta box, replace the parameter `'settings_pages' => 'rubik'` with `'panel' => ''`, like this:

```php
add_filter( 'rwmb_meta_boxes', function ( $meta_boxes ) {
    $meta_boxes[] = [
        'id'             => 'general',
        'title'          => 'General',
        'panel'          => '',
        'fields'         => [
            [
                'name' => 'Logo',
                'id'   => 'logo',
                'type' => 'file_input',
            ],
        ],
    ];
    return $meta_boxes;
} );
```

And you'll see the section on the Customizer like this:

![Sections now appear as top-level in the Customizer](https://imgur.elightup.com/xICe0u3.png)

What if you want the *section to be inside another panel*? Like inside another plugin's panel? Set the `panel` parameter to ID of the target panel: `'panel' => 'panel_id'`.

### Compatibility

At the moment, all Meta Box fields are supported in the Customizer, except [file](../fields/file.md) and [image](../fields/image.md) field types. These field types will be converted to the [file\_advanced](../fields/file-advanced.md) and [image\_advanced](../fields/image-advanced.md) automatically to avoid any problems. Other upload field types such as [file\_advanced](../fields/file-advanced.md), [file\_upload](../fields/file-upload.md), [image\_advanced](../fields/image-advanced.md), [image\_upload](../fields/image-upload.md), [single\_image](../fields/single-image.md) still work well.

The good news is all the extensions such as [MB Conditional Logic](meta-box-conditional-logic.md), [MB Tabs](meta-box-tabs.md) are supported. That will help you create much better experiences for your users.

> [!-warning] -warning
> postMessage transport
> 
> The `postMessage` transport for the Customizer is not supported yet, which means changes are updated by refreshing the whole page instead of updating only the needed part of the page.

## Network settings pages

A network settings page is a settings page that provides settings for all the websites in the network (multisite environment). For example, you might want to enter a Google Maps API key for all the websites or set the contact phone number for all of them.

![Sample network settings page](https://imgur.elightup.com/pjZzrKf.png)

Using *MB Settings Page*, you’re now able to do that easily. If you use MB Builder to create the settings page, simply switch on the **Network** option.

![Set as a network settings page](https://docs.metabox.io/assets/images/network-setting-d61d8ccef7f21589864d6585a9276f9e.png)

If you use code, add `'network' => true` to the settings pages args, like this:

```php
add_filter( 'mb_settings_pages', function ( $settings_pages ) {
    $settings_pages[] = [
        'id'          => 'custom-options',
        'option_name' => 'custom_options',
        'menu_title'  => 'Custom Options',
        'icon_url'    => 'dashicons-welcome-widgets-menus',
        'network'     => true,
    ];

    return $settings_pages;
} );
```

Don't forget to *network activate* Meta Box and MB Settings Pages. And now, when you go to the network admin area, you'll see a settings page like the screenshot above.

## Backup & restore settings

Backup is a **special field type** added by the plugin that allows you to back up and restore the settings.

If you use MB Builder to create fields, please add a normal textarea field, go to tab Advanced of the field settings, and add a custom settings with the key "type" and value "backup" as follows:

![create a backup field in MB Builder](https://docs.metabox.io/assets/images/custom-settings-8435bf968cb7b9651406c8ff31c8586a.png)

If you use code, you need to create a special field with `'type' => 'backup'`, like this:

```php
$meta_boxes[] = [
    'id'             => 'colors',
    'title'          => 'Colors',
    'settings_pages' => 'theme-slug',
    'fields'         => [
        [
            'name' => 'Text Color',
            'id'   => 'text-color',
            'type' => 'color',
        ],
        [
            'name' => 'Backup',
            'type' => 'backup',
        ],
    ],
];
```

It will show a textarea field in your settings page like this:

![backup and restore settings](https://imgur.elightup.com/n6d6v1n.png)

When you add it to your settings page, it will show all of your settings in JSON. And you can just copy it and save it to a file to back up the settings. To restore the settings, just paste the JSON again and click the Save Settings button.

The backup field inherits from [`textarea`](../fields/textarea.md) so you can customize it the way you want: change the field name, description, input size, etc. This field doesn't require an `ID`. And of course, you should have only one backup field on your settings page.

> [!-warning] -warning
> warning
> 
> The backup field only works if it is a top field. It does not work if it is a subfield in a group.

## Hooks

**`mb_settings_page_load` action**

This action fires when a settings page is loaded. It's used internally to:

- Register meta boxes and custom fields in the settings page, and
- Save the submitted data.

These actions use the default priority `10`. So you can hook to this action to do something *after* the data is saved with a higher priority (like `20`):

```php
add_action( 'mb_settings_page_load', function ( $args ) {
    if ( $args['id'] === 'YOUR SETTINGS PAGE ID' ) {
        // Do something
    }
}, 20 );
```

**`mb_settings_page_after_title` action**

This action fires after outputting the page title. You can use it to output anything like instructions to users.

**`mb_settings_page_submit_buttons` action**

This action fires after the submit button is rendered, which allows you to add more custom buttons next to the submit button.

## Data

By using Settings API, all the fields' values will be saved as an array in a single option in the WordPress options table with the option name is `option_name` in the settings page configuration. Each field is an element of the array with the corresponding key (field ID). It's the recommended way by WordPress that doesn't make your options table bloat.

## Getting field value

You're able to use helper function [rwmb\_meta()](../functions/rwmb-meta.md) to get field value as follows:

```php
$value = rwmb_meta( $field_id, ['object_type' => 'setting'], $option_name );
echo $value;
```

For network settings, please use the following code:

```php
$value = rwmb_meta( $field_id, ['object_type' => 'network_setting'], $option_name );
echo $value;
```

Notes:

- In the 2nd parameter, you need to pass `'object_type' => 'setting'` or `'object_type' => 'network_setting'`
- In the last parameter, you need to pass the option name for the settings page

Other parameters are the same as for posts. Please see [this documentation](../displaying-fields-with-code.md) for details.

> [!-warning] -warning
> warning
> 
> It requires the extension version 1.2+ to use the helper function. If you're using an older version, please [update now](../updates.md).
