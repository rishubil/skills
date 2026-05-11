---
title: Toybox.WatchUi.IconMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/IconMenuItem.html
---

## Class: Toybox.WatchUi.IconMenuItem

## Overview

A representation of an icon item in a Menu2.

An IconMenuItem is a element of a [Menu2](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html) View that represents one of the options in the menu. An IconMenuItem has an icon displayed on the left or right of the menu item labels.

An IconMenuItem can be added to a Menu2 using the [addItem()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html#addItem-instance_function) method.

## See Also:

- [Toybox.WatchUi.Menu2](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html)
- [Toybox.WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html)

## Instance Method Summary

- [**getIcon**](#getIcon-instance_function "getIcon (Instance Function)") () as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html)
	Get IconMenuItem icon.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), subLabel as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**, identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**, icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), options as {:alignment as [MenuItem.Alignment](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html#Alignment-module) } or **Null**)
	Constructor.
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html)) as **Void**
	Set the IconMenuItem icon.

## Instance Method Details

### getIcon() as Graphics.BitmapType or WatchUi.Drawable

Get IconMenuItem icon.

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or Null, identifier as Lang.Object or Null, icon as Graphics.BitmapType or WatchUi.Drawable, options as {:alignment as MenuItem.Alignment } or Null)

Constructor

### setIcon(icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId) as Void

Set the IconMenuItem icon.
