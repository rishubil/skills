---
title: Toybox.WatchUi.MenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html
---

## Class: Toybox.WatchUi.MenuItem

## Overview

## See Also:

- [Toybox.WatchUi.Menu2](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html)

## Direct Known Subclasses

[WatchUi.CheckboxMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CheckboxMenuItem.html), [WatchUi.CustomMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenuItem.html), [WatchUi.IconMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/IconMenuItem.html), [WatchUi.ToggleMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ToggleMenuItem.html)

## Constant Summary

### Alignment

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MENU\_ITEM\_LABEL\_ALIGN\_RIGHT | 0 | API Level 3.0.0 | Right align a MenuItem label |
| MENU\_ITEM\_LABEL\_ALIGN\_LEFT | 1 | API Level 3.0.0 | Left align a MenuItem label |

## Instance Method Summary

- [**getIcon**](#getIcon-instance_function "getIcon (Instance Function)") () as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	Get the icon Retrieve the icon for this MenuItem.
- [**getId**](#getId-instance_function "getId (Instance Function)") () as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**
	Get a MenuItem identifier.
- [**getLabel**](#getLabel-instance_function "getLabel (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Get a MenuItem label.
- [**getSubLabel**](#getSubLabel-instance_function "getSubLabel (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html), [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null** > or **Null**
	Get a MenuItem substring label.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), subLabel as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**, identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**, options as {:alignment as [MenuItem.Alignment](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html#Alignment-module),:icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) } or **Null**)
	Constructor.
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**) as **Void**
	Set the icon Set the icon displayed in the subscreen area when this MenuItem has the focus.
- [**setLabel**](#setLabel-instance_function "setLabel (Instance Function)") (label as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html)) as **Void**
	Set a MenuItem label.
- [**setSubLabel**](#setSubLabel-instance_function "setSubLabel (Instance Function)") (subLabel as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**) as **Void**
	Set a MenuItem substring label.

## Instance Method Details

### getIcon() as Graphics.BitmapType or WatchUi.Drawable or Null

### getId() as Lang.Object or Null

### getLabel() as Lang.String

### getSubLabel() as Lang.String or Lang.Dictionary<Lang.Symbol, Lang.String or Null> or Null

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or Null, identifier as Lang.Object or Null, options as {:alignment as MenuItem.Alignment,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId } or Null)

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
