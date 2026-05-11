---
title: Toybox.WatchUi.MapMarker
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html
---

## Class: Toybox.WatchUi.MapMarker

## Overview

The base class for the MapMarker object.

The MapMarker is used to hold a [BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html), or a [MAP\_MARKER\_ICON\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html) enum value, and the corresponding `x, y` value to note the "hotspot" for the image to be used as an icon for a marker within a [MapView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html). This class also contains the [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) at which the MapMarker should be displayed on the map.

## Instance Method Summary

- [**getLocation**](#getLocation-instance_function "getLocation (Instance Function)") () as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html)
	Get the location for the MapMarker.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (location as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html))
	Constructor.
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [WatchUi.MapMarkerIcon](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#MapMarkerIcon-module) or [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), x as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), y as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Set a bitmap icon to use for the MapMarker object on a [MapView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html).
- [**setLabel**](#setLabel-instance_function "setLabel (Instance Function)") (label as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html)) as **Void**

## Instance Method Details

### getLocation() as Position.Location

Get the location for the MapMarker.

### initialize(location as Position.Location)

Constructor

### setIcon(icon as Graphics.BitmapType or WatchUi.MapMarkerIcon or Lang.Number, x as Lang.Number, y as Lang.Number) as Void

Set a bitmap icon to use for the MapMarker object on a [MapView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html).
