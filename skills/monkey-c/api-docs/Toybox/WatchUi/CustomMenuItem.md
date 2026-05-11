---
title: Toybox.WatchUi.CustomMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenuItem.html
---

## Class: Toybox.WatchUi.CustomMenuItem

## Overview

## See Also:

- [Toybox.WatchUi.CustomMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenu.html)
- [Toybox.WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html)

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Draw method for a CustomMenuItem.
- [**getDividerIcon**](#getDividerIcon-instance_function "getDividerIcon (Instance Function)") () as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	Get the divider icon.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**, options as {:alignment as [MenuItem.Alignment](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html#Alignment-module),:drawable as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:dividerIcon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) })
	Constructor.
- [**isFocused**](#isFocused-instance_function "isFocused (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Get the CustomMenuItem focus state.
- [**isSelected**](#isSelected-instance_function "isSelected (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Get the CustomMenuItem selected state.
- [**setDividerIcon**](#setDividerIcon-instance_function "setDividerIcon (Instance Function)") (icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**) as **Void**
- [**setDrawable**](#setDrawable-instance_function "setDrawable (Instance Function)") (drawable as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**) as **Void**
	Set a CustomMenuItem Drawable.

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

### getDividerIcon() as Graphics.BitmapType or WatchUi.Drawable or Null

### initialize(identifier as Lang.Object or Null, options as {:alignment as MenuItem.Alignment,:drawable as WatchUi.Drawable,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId,:dividerIcon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId })

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
