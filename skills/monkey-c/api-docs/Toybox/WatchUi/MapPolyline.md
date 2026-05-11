---
title: Toybox.WatchUi.MapPolyline
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapPolyline.html
---

## Class: Toybox.WatchUi.MapPolyline

## Overview

An object representing a polyline (polygonal chain) on the map.

This object holds an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) objects to draw a polyline on the map.

## See Also:

- [https://en.wikipedia.org/wiki/Polygonal\_chain](https://en.wikipedia.org/wiki/Polygonal_chain)

## Instance Method Summary

- [**addLocation**](#addLocation-instance_function "addLocation (Instance Function)") (location as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) >) as **Void**
	Add a Location or Locations to the MapPolyline object location [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html).
- [**clear**](#clear-instance_function "clear (Instance Function)") () as **Void**
	Clear all the [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) objects from the MapPolyline object's location [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html).
- [**getLocation**](#getLocation-instance_function "getLocation (Instance Function)") (index as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) or **Null**
	Get the [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) object at a provided index in this MapPolyline object.
- [**numLocations**](#numLocations-instance_function "numLocations (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the number of [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) objects in this MapPolyline object.
- [**setColor**](#setColor-instance_function "setColor (Instance Function)") (color as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type)) as **Void**
	Set the color of the MapPolyline to draw on the map.
- [**setWidth**](#setWidth-instance_function "setWidth (Instance Function)") (width as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Set the width of the MapPolyline to draw on the map.

## Instance Method Details

### addLocation(location as Position.Location or Lang.Array<Position.Location>) as Void

Add a Location or Locations to the MapPolyline object location [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html).

### clear() as Void

Clear all the [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) objects from the MapPolyline object's location [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html).

### getLocation(index as Lang.Number) as Position.Location or Null

Get the [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) object at a provided index in this MapPolyline object.

### numLocations() as Lang.Number

Get the number of [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) objects in this MapPolyline object.

### setColor(color as Graphics.ColorType) as Void

Set the color of the MapPolyline to draw on the map.

### setWidth(width as Lang.Number) as Void

Set the width of the MapPolyline to draw on the map.
