---
title: Toybox.WatchUi.CheckboxMenuItem
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CheckboxMenuItem.html
---

## Class: Toybox.WatchUi.CheckboxMenuItem

## Overview

## See Also:

- [Toybox.WatchUi.CheckboxMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CheckboxMenu.html)
- [Toybox.WatchUi.MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html)

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (label as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), subLabel as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**, identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**, checked as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html), options as {:alignment as [MenuItem.Alignment](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html#Alignment-module),:icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) } or **Null**)
	Constructor.
- [**isChecked**](#isChecked-instance_function "isChecked (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Get a CheckboxMenuItem state.
- [**setChecked**](#setChecked-instance_function "setChecked (Instance Function)") (checked as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as **Void**
	Set a CheckboxMenuItem state.

## Instance Method Details

### initialize(label as Lang.String or Lang.ResourceId, subLabel as Lang.String or Lang.ResourceId or Null, identifier as Lang.Object or Null, checked as Lang.Boolean, options as {:alignment as MenuItem.Alignment,:icon as Graphics.BitmapType or WatchUi.Drawable or Lang.ResourceId } or Null)

Note:

The `:icon` option is only used on ConnectIQ 3.4.0 devices with subscreen support.
