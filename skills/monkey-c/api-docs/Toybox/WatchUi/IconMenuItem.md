---
title: Toybox.WatchUi.IconMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/IconMenuItem.html
---

## Class: Toybox.WatchUi.IconMenuItem

## Overview

A representation of an icon item in a Menu2.

An IconMenuItem is a element of a [Menu2](Menu2.md) View that represents one of the options in the menu. An IconMenuItem has an icon displayed on the left or right of the menu item labels.

An IconMenuItem can be added to a Menu2 using the [addItem()](Menu2.md#addItem-instance_function) method.

## See Also:

- [Toybox.WatchUi.Menu2](Menu2.md)
- [Toybox.WatchUi.MenuItem](MenuItem.md)

## Instance Method Summary

- [**getIcon**](#getIcon-instance_function "getIcon (Instance Function)") () as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md)
	Get IconMenuItem icon.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md), subLabel as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**, identifier as [Lang.Object](../Lang/Object.md) or **Null**, icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md), options as {:alignment as [MenuItem.Alignment](MenuItem.md#Alignment-module) } or **Null**)
	Constructor.
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md)) as **Void**
	Set the IconMenuItem icon.

## Instance Method Details

### getIcon() as Graphics.BitmapType or WatchUi.Drawable

Get IconMenuItem icon.

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or Null, identifier as Lang.Object or Null, icon as Graphics.BitmapType or WatchUi.Drawable, options as {:alignment as MenuItem.Alignment } or Null)

Constructor

### setIcon(icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId) as Void

Set the IconMenuItem icon.
