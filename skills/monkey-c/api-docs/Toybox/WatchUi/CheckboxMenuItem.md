---
title: Toybox.WatchUi.CheckboxMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CheckboxMenuItem.html
---

## Class: Toybox.WatchUi.CheckboxMenuItem

## Overview

## See Also:

- [Toybox.WatchUi.CheckboxMenu](CheckboxMenu.md)
- [Toybox.WatchUi.MenuItem](MenuItem.md)

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md), subLabel as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**, identifier as [Lang.Object](../Lang/Object.md) or **Null**, checked as [Lang.Boolean](../Lang/Boolean.md), options as {:alignment as [MenuItem.Alignment](MenuItem.md#Alignment-module),:icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md) } or **Null**)
	Constructor.
- [**isChecked**](#isChecked-instance_function "isChecked (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Get a CheckboxMenuItem state.
- [**setChecked**](#setChecked-instance_function "setChecked (Instance Function)") (checked as [Lang.Boolean](../Lang/Boolean.md)) as **Void**
	Set a CheckboxMenuItem state.

## Instance Method Details

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or Null, identifier as Lang.Object or Null, checked as Lang.Boolean, options as {:alignment as MenuItem.Alignment,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId } or Null)

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
