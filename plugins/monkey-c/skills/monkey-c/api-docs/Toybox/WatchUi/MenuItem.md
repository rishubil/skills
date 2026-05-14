---
title: Toybox.WatchUi.MenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html
---

## Class: Toybox.WatchUi.MenuItem

## Overview

## See Also:

- [Toybox.WatchUi.Menu2](Menu2.md)

## Direct Known Subclasses

[WatchUi.CheckboxMenuItem](CheckboxMenuItem.md), [WatchUi.CustomMenuItem](CustomMenuItem.md), [WatchUi.IconMenuItem](IconMenuItem.md), [WatchUi.ToggleMenuItem](ToggleMenuItem.md)

## Constant Summary

### Alignment

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MENU\_ITEM\_LABEL\_ALIGN\_RIGHT | 0 | API Level 3.0.0 | Right align a MenuItem label |
| MENU\_ITEM\_LABEL\_ALIGN\_LEFT | 1 | API Level 3.0.0 | Left align a MenuItem label |

## Instance Method Summary

- [**getIcon**](#getIcon-instance_function "getIcon (Instance Function)") () as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or **Null**
	Get the icon Retrieve the icon for this MenuItem.
- [**getId**](#getId-instance_function "getId (Instance Function)") () as [Lang.Object](../Lang/Object.md) or **Null**
	Get a MenuItem identifier.
- [**getLabel**](#getLabel-instance_function "getLabel (Instance Function)") () as [Lang.String](../Lang/String.md)
	Get a MenuItem label.
- [**getSubLabel**](#getSubLabel-instance_function "getSubLabel (Instance Function)") () as [Lang.String](../Lang/String.md) or [Lang.Dictionary](../Lang/Dictionary.md) < [Lang.Symbol](../Lang/Symbol.md), [Lang.String](../Lang/String.md) or **Null** > or **Null**
	Get a MenuItem substring label.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md), subLabel as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**, identifier as [Lang.Object](../Lang/Object.md) or **Null**, options as {:alignment as [MenuItem.Alignment](MenuItem.md#Alignment-module),:icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md) } or **Null**)
	Constructor.
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**) as **Void**
	Set the icon Set the icon displayed in the subscreen area when this MenuItem has the focus.
- [**setLabel**](#setLabel-instance_function "setLabel (Instance Function)") (label as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md)) as **Void**
	Set a MenuItem label.
- [**setSubLabel**](#setSubLabel-instance_function "setSubLabel (Instance Function)") (subLabel as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**) as **Void**
	Set a MenuItem substring label.

## Instance Method Details

### getIcon() as Graphics.BitmapType or WatchUi.Drawable or Null

### getId() as Lang.Object or Null

### getLabel() as Lang.String

### getSubLabel() as Lang.String or Lang.Dictionary<Lang.Symbol, Lang.String or Null> or Null

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or Null, identifier as Lang.Object or Null, options as {:alignment as MenuItem.Alignment,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId } or Null)

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
