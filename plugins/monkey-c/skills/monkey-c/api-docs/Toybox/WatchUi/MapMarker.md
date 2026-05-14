---
title: Toybox.WatchUi.MapMarker
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html
---

## Class: Toybox.WatchUi.MapMarker

## Overview

The base class for the MapMarker object.

The MapMarker is used to hold a [BitmapResource](BitmapResource.md), or a [MAP\_MARKER\_ICON\_\*](../WatchUi.md) enum value, and the corresponding `x, y` value to note the "hotspot" for the image to be used as an icon for a marker within a [MapView](MapView.md). This class also contains the [Location](../Position/Location.md) at which the MapMarker should be displayed on the map.

## Instance Method Summary

- [**getLocation**](#getLocation-instance_function "getLocation (Instance Function)") () as [Position.Location](../Position/Location.md)
	Get the location for the MapMarker.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (location as [Position.Location](../Position/Location.md))
	Constructor.
- [**setIcon**](#setIcon-instance_function "setIcon (Instance Function)") (icon as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [WatchUi.MapMarkerIcon](../WatchUi.md#MapMarkerIcon-module) or [Lang.Number](../Lang/Number.md), x as [Lang.Number](../Lang/Number.md), y as [Lang.Number](../Lang/Number.md)) as **Void**
	Set a bitmap icon to use for the MapMarker object on a [MapView](MapView.md).
- [**setLabel**](#setLabel-instance_function "setLabel (Instance Function)") (label as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md)) as **Void**

## Instance Method Details

### getLocation() as Position.Location

Get the location for the MapMarker.

### initialize(location as Position.Location)

Constructor

### setIcon(icon as Graphics.BitmapType or WatchUi.MapMarkerIcon or Lang.Number, x as Lang.Number, y as Lang.Number) as Void

Set a bitmap icon to use for the MapMarker object on a [MapView](MapView.md).
