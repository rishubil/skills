---
title: Toybox.WatchUi.CustomMenu
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenu.html
---

## Class: Toybox.WatchUi.CustomMenu

## Overview

## See Also:

- [Toybox.WatchUi.Menu2](Menu2.md)
- [Toybox.WatchUi.CustomMenuItem](CustomMenuItem.md)
- [Toybox.WatchUi.Menu2InputDelegate](Menu2InputDelegate.md)
- [Toybox.WatchUi.BehaviorDelegate](BehaviorDelegate.md)
- [WatchUi.pushView()](../WatchUi.md#pushView-instance_function)

## Instance Method Summary

- [**addItem**](#addItem-instance_function "addItem (Instance Function)") (item as [WatchUi.CustomMenuItem](CustomMenuItem.md)) as **Void**
	Add a CustomMenuItem to a CustomMenu.
- [**drawFooter**](#drawFooter-instance_function "drawFooter (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
- [**drawForeground**](#drawForeground-instance_function "drawForeground (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Draw the CustomMenu foreground.
- [**drawTitle**](#drawTitle-instance_function "drawTitle (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Draw the CustomMenu title.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (itemHeight as [Lang.Number](../Lang/Number.md), backgroundColor as [Graphics.ColorType](../Graphics.md#ColorType-named_type), options as {:focus as [Lang.Number](../Lang/Number.md),:focusItemHeight as [Lang.Number](../Lang/Number.md) or **Null**,:title as [WatchUi.Drawable](Drawable.md),:footer as [WatchUi.Drawable](Drawable.md),:foreground as [WatchUi.Drawable](Drawable.md),:icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md),:titleItemHeight as [Lang.Number](../Lang/Number.md) or **Null**,:footerItemHeight as [Lang.Number](../Lang/Number.md) or **Null**,:theme as [WatchUi.MenuTheme](../WatchUi.md#MenuTheme-module) or **Null**,:dividerType as [Menu2.DividerType](Menu2.md#DividerType-module) or **Null** } or **Null**)
	Constructor.
- [**setBackgroundColor**](#setBackgroundColor-instance_function "setBackgroundColor (Instance Function)") (color as [Graphics.ColorType](../Graphics.md#ColorType-named_type)) as **Void**
	Set the background color.
- [**setDividerType**](#setDividerType-instance_function "setDividerType (Instance Function)") (divider as [Menu2.DividerType](Menu2.md#DividerType-module) or **Null**) as **Void**
	Set or change the desired divider type.
- [**setFooter**](#setFooter-instance_function "setFooter (Instance Function)") (drawable as [WatchUi.Drawable](Drawable.md) or **Null**) as **Void**
- [**setForeground**](#setForeground-instance_function "setForeground (Instance Function)") (drawable as [WatchUi.Drawable](Drawable.md) or **Null**) as **Void**
	Set the foreground drawable.
- [**setTitle**](#setTitle-instance_function "setTitle (Instance Function)") (drawable as [WatchUi.Drawable](Drawable.md) or **Null**) as **Void**
	Set the title drawable.
