---
title: Toybox.WatchUi.ToggleMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ToggleMenuItem.html
---

## Class: Toybox.WatchUi.ToggleMenuItem

## Overview

## See Also:

- [Toybox.WatchUi.Menu2](Menu2.md)
- [Toybox.WatchUi.MenuItem](MenuItem.md)

## Instance Method Summary

- [**getSubLabel**](#getSubLabel-instance_function "getSubLabel (Instance Function)") () as [Lang.String](../Lang/String.md) or [Lang.Dictionary](../Lang/Dictionary.md) < [Lang.Symbol](../Lang/Symbol.md), [Lang.String](../Lang/String.md) or **Null** > or **Null**
	Get a ToggleMenuItem label substring.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md), subLabel as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or {:enabled as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**,:disabled as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null** } or **Null**, identifier as [Lang.Object](../Lang/Object.md) or **Null**, enabled as [Lang.Boolean](../Lang/Boolean.md), options as {:alignment as [MenuItem.Alignment](MenuItem.md#Alignment-module),:icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.Drawable](Drawable.md) or [Lang.ResourceId](../Lang/ResourceId.md) } or **Null**)
	Constructor.
- [**isEnabled**](#isEnabled-instance_function "isEnabled (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Get a ToggleMenuItem state.
- [**setEnabled**](#setEnabled-instance_function "setEnabled (Instance Function)") (enabled as [Lang.Boolean](../Lang/Boolean.md)) as **Void**
	Set a ToggleMenuItem state.
- [**setSubLabel**](#setSubLabel-instance_function "setSubLabel (Instance Function)") (subLabel as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or {:enabled as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**,:disabled as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null** } or **Null**) as **Void**
	Set a ToggleMenuItem label substring.

## Instance Method Details

### getSubLabel() as Lang.String or Lang.Dictionary<Lang.Symbol, Lang.String or Null> or Null

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or {:enabled as Lang.String or Lang.ResourceId or Null,:disabled as Lang.String or Lang.ResourceId or Null } or Null, identifier as Lang.Object or Null, enabled as Lang.Boolean, options as {:alignment as MenuItem.Alignment,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId } or Null)

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
