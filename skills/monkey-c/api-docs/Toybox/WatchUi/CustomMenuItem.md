---
title: Toybox.WatchUi.CustomMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenuItem.html
---

## Class: Toybox.WatchUi.CustomMenuItem

## Overview

## See Also:

- [Toybox.WatchUi.CustomMenu](CustomMenu.md)
- [Toybox.WatchUi.MenuItem](MenuItem.md)

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Draw method for a CustomMenuItem.
- [**getDividerIcon**](#getDividerIcon-instance_function "getDividerIcon (Instance Function)") () as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or **Null**
	Get the divider icon.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (identifier as [Lang.Object](../Lang/Object.md) or **Null**, options as {:alignment as [MenuItem.Alignment](MenuItem.md#Alignment-module),:drawable as [WatchUi.Drawable](Drawable.md),:icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md),:dividerIcon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md) })
	Constructor.
- [**isFocused**](#isFocused-instance_function "isFocused (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Get the CustomMenuItem focus state.
- [**isSelected**](#isSelected-instance_function "isSelected (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Get the CustomMenuItem selected state.
- [**setDividerIcon**](#setDividerIcon-instance_function "setDividerIcon (Instance Function)") (icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**) as **Void**
- [**setDrawable**](#setDrawable-instance_function "setDrawable (Instance Function)") (drawable as [WatchUi.Drawable](Drawable.md) or **Null**) as **Void**
	Set a CustomMenuItem Drawable.

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

### getDividerIcon() as Graphics.BitmapType or WatchUi.Drawable or Null

### initialize(identifier as Lang.Object or Null, options as {:alignment as MenuItem.Alignment,:drawable as WatchUi.Drawable,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId,:dividerIcon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId })

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
