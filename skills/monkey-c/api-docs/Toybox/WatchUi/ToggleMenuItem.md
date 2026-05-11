---
title: Toybox.WatchUi.ToggleMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ToggleMenuItem.html
---

## Class: Toybox.WatchUi.ToggleMenuItem

## Overview

## See Also:

- [Toybox.WatchUi.Menu2](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html)
- [Toybox.WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html)

## Instance Method Summary

- [**getSubLabel**](#getSubLabel-instance_function "getSubLabel (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html), [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null** > or **Null**
	Get a ToggleMenuItem label substring.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), subLabel as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or {:enabled as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**,:disabled as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null** } or **Null**, identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**, enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html), options as {:alignment as [MenuItem.Alignment](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html#Alignment-module),:icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) } or **Null**)
	Constructor.
- [**isEnabled**](#isEnabled-instance_function "isEnabled (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Get a ToggleMenuItem state.
- [**setEnabled**](#setEnabled-instance_function "setEnabled (Instance Function)") (enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as **Void**
	Set a ToggleMenuItem state.
- [**setSubLabel**](#setSubLabel-instance_function "setSubLabel (Instance Function)") (subLabel as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or {:enabled as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**,:disabled as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null** } or **Null**) as **Void**
	Set a ToggleMenuItem label substring.

## Instance Method Details

### getSubLabel() as Lang.String or Lang.Dictionary<Lang.Symbol, Lang.String or Null> or Null

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or {:enabled as Lang.String or Lang.ResourceId or Null,:disabled as Lang.String or Lang.ResourceId or Null } or Null, identifier as Lang.Object or Null, enabled as Lang.Boolean, options as {:alignment as MenuItem.Alignment,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId } or Null)

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
