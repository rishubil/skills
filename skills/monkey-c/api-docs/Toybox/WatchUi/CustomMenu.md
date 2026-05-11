---
title: Toybox.WatchUi.CustomMenu
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenu.html
---

## Class: Toybox.WatchUi.CustomMenu

## Overview

## See Also:

- [Toybox.WatchUi.Menu2](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html)
- [Toybox.WatchUi.CustomMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenuItem.html)
- [Toybox.WatchUi.Menu2InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2InputDelegate.html)
- [Toybox.WatchUi.BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html)
- [WatchUi.pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function)

## Instance Method Summary

- [**addItem**](#addItem-instance_function "addItem (Instance Function)") (item as [WatchUi.CustomMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenuItem.html)) as **Void**
	Add a CustomMenuItem to a CustomMenu.
- [**drawFooter**](#drawFooter-instance_function "drawFooter (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
- [**drawForeground**](#drawForeground-instance_function "drawForeground (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Draw the CustomMenu foreground.
- [**drawTitle**](#drawTitle-instance_function "drawTitle (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Draw the CustomMenu title.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (itemHeight as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), backgroundColor as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type), options as {:focus as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:focusItemHeight as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**,:title as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:footer as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:foreground as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:titleItemHeight as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**,:footerItemHeight as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**,:theme as [WatchUi.MenuTheme](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#MenuTheme-module) or **Null**,:dividerType as [Menu2.DividerType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html#DividerType-module) or **Null** } or **Null**)
	Constructor.
- [**setBackgroundColor**](#setBackgroundColor-instance_function "setBackgroundColor (Instance Function)") (color as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type)) as **Void**
	Set the background color.
- [**setDividerType**](#setDividerType-instance_function "setDividerType (Instance Function)") (divider as [Menu2.DividerType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html#DividerType-module) or **Null**) as **Void**
	Set or change the desired divider type.
- [**setFooter**](#setFooter-instance_function "setFooter (Instance Function)") (drawable as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**) as **Void**
- [**setForeground**](#setForeground-instance_function "setForeground (Instance Function)") (drawable as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**) as **Void**
	Set the foreground drawable.
- [**setTitle**](#setTitle-instance_function "setTitle (Instance Function)") (drawable as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**) as **Void**
	Set the title drawable.
