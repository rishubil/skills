---
title: Toybox.WatchUi.Menu2
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html
---

## Class: Toybox.WatchUi.Menu2

## Overview

## See Also:

- [Toybox.WatchUi.Menu2InputDelegate](Menu2InputDelegate.md)
- [Toybox.WatchUi.MenuItem](MenuItem.md)
- [Toybox.WatchUi.BehaviorDelegate](BehaviorDelegate.md)
- [WatchUi.pushView()](../WatchUi.md#pushView-instance_function)
Note:

The look and feel of a Menu2 is device-specific.

## Direct Known Subclasses

[WatchUi.CheckboxMenu](CheckboxMenu.md), [WatchUi.CustomMenu](CustomMenu.md)

## Constant Summary

### DividerType

Divider type for supported devices

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DIVIDER\_TYPE\_DEFAULT | 0 | API Level 5.0.1 | Default divider type |
| DIVIDER\_TYPE\_ICON | 1 | API Level 5.0.1 | Icon divider type |

## Instance Method Summary

- [**addItem**](#addItem-instance_function "addItem (Instance Function)") (item as [WatchUi.MenuItem](MenuItem.md)) as **Void**
	Add a MenuItem to a Menu2.
- [**deleteItem**](#deleteItem-instance_function "deleteItem (Instance Function)") (index as [Lang.Number](../Lang/Number.md)) as [Lang.Boolean](../Lang/Boolean.md) or **Null**
	Delete a MenuItem from a Menu2.
- [**findItemById**](#findItemById-instance_function "findItemById (Instance Function)") (identifier as [Lang.Object](../Lang/Object.md)) as [Lang.Number](../Lang/Number.md)
	Find a MenuItem by ID in a Menu2.
- [**getIcon**](#getIcon-instance_function "getIcon (Instance Function)") () as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or **Null**
	Get the icon Retrieve the icon for this Menu2.
- [**getItem**](#getItem-instance_function "getItem (Instance Function)") (index as [Lang.Number](../Lang/Number.md)) as [WatchUi.MenuItem](MenuItem.md) or **Null**
	Get a MenuItem from a Menu2.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:title as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or [WatchUi.Drawable](Drawable.md),:footer as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or [WatchUi.Drawable](Drawable.md),:focus as [Lang.Number](../Lang/Number.md),:icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md),:theme as [WatchUi.MenuTheme](../WatchUi.md#MenuTheme-module) or **Null**,:dividerType as [Menu2.DividerType](Menu2.md#DividerType-module) or **Null** } or **Null**)
	Constructor.
- [**setDividerType**](#setDividerType-instance_function "setDividerType (Instance Function)") (divider as [Menu2.DividerType](Menu2.md#DividerType-module) or **Null**) as **Void**
	Set or change the desired divider type.
- [**setFocus**](#setFocus-instance_function "setFocus (Instance Function)") (focus as [Lang.Number](../Lang/Number.md) or **Null**) as **Void**
	Set the focus of a MenuItem in a Menu2.
- [**setFooter**](#setFooter-instance_function "setFooter (Instance Function)") (footer as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or [WatchUi.Drawable](Drawable.md) or **Null**) as **Void**
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**) as **Void**
	Set the icon Set the icon to display in the subscreen area when the focused MenuItem does not have an icon.
- [**setTheme**](#setTheme-instance_function "setTheme (Instance Function)") (theme as [WatchUi.MenuTheme](../WatchUi.md#MenuTheme-module) or **Null**) as **Void**
	Set the theme.
- [**setTitle**](#setTitle-instance_function "setTitle (Instance Function)") (title as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or [WatchUi.Drawable](Drawable.md) or **Null**) as **Void**
	Set a Menu2 title.
- [**updateItem**](#updateItem-instance_function "updateItem (Instance Function)") (item as [WatchUi.MenuItem](MenuItem.md), index as [Lang.Number](../Lang/Number.md)) as **Void**
	Update a MenuItem in a Menu2.
