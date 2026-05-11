---
title: Toybox.WatchUi.Menu2
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html
---

## Class: Toybox.WatchUi.Menu2

## Overview

## See Also:

- [Toybox.WatchUi.Menu2InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2InputDelegate.html)
- [Toybox.WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html)
- [Toybox.WatchUi.BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html)
- [WatchUi.pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function)
Note:

The look and feel of a Menu2 is device-specific.

## Direct Known Subclasses

[WatchUi.CheckboxMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CheckboxMenu.html), [WatchUi.CustomMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenu.html)

## Constant Summary

### DividerType

Divider type for supported devices

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DIVIDER\_TYPE\_DEFAULT | 0 | API Level 5.0.1 | Default divider type |
| DIVIDER\_TYPE\_ICON | 1 | API Level 5.0.1 | Icon divider type |

## Instance Method Summary

- [**addItem**](#addItem-instance_function "addItem (Instance Function)") (item as [WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html)) as **Void**
	Add a MenuItem to a Menu2.
- [**deleteItem**](#deleteItem-instance_function "deleteItem (Instance Function)") (index as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or **Null**
	Delete a MenuItem from a Menu2.
- [**findItemById**](#findItemById-instance_function "findItemById (Instance Function)") (identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Find a MenuItem by ID in a Menu2.
- [**getIcon**](#getIcon-instance_function "getIcon (Instance Function)") () as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	Get the icon Retrieve the icon for this Menu2.
- [**getItem**](#getItem-instance_function "getItem (Instance Function)") (index as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html) or **Null**
	Get a MenuItem from a Menu2.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:title as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:footer as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:focus as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:theme as [WatchUi.MenuTheme](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#MenuTheme-module) or **Null**,:dividerType as [Menu2.DividerType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html#DividerType-module) or **Null** } or **Null**)
	Constructor.
- [**setDividerType**](#setDividerType-instance_function "setDividerType (Instance Function)") (divider as [Menu2.DividerType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html#DividerType-module) or **Null**) as **Void**
	Set or change the desired divider type.
- [**setFocus**](#setFocus-instance_function "setFocus (Instance Function)") (focus as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**) as **Void**
	Set the focus of a MenuItem in a Menu2.
- [**setFooter**](#setFooter-instance_function "setFooter (Instance Function)") (footer as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**) as **Void**
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**) as **Void**
	Set the icon Set the icon to display in the subscreen area when the focused MenuItem does not have an icon.
- [**setTheme**](#setTheme-instance_function "setTheme (Instance Function)") (theme as [WatchUi.MenuTheme](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#MenuTheme-module) or **Null**) as **Void**
	Set the theme.
- [**setTitle**](#setTitle-instance_function "setTitle (Instance Function)") (title as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**) as **Void**
	Set a Menu2 title.
- [**updateItem**](#updateItem-instance_function "updateItem (Instance Function)") (item as [WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html), index as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Update a MenuItem in a Menu2.
