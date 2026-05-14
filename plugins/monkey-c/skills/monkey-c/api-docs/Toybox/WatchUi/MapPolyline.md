---
title: Toybox.WatchUi.MapPolyline
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapPolyline.html
---

## Class: Toybox.WatchUi.MapPolyline

## Overview

An object representing a polyline (polygonal chain) on the map.

This object holds an [Array](../Lang/Array.md) of [Location](../Position/Location.md) objects to draw a polyline on the map.

## See Also:

- [https://en.wikipedia.org/wiki/Polygonal\_chain](https://en.wikipedia.org/wiki/Polygonal_chain)

## Instance Method Summary

- [**addLocation**](#addLocation-instance_function "addLocation (Instance Function)") (location as [Position.Location](../Position/Location.md) or [Lang.Array](../Lang/Array.md) < [Position.Location](../Position/Location.md) >) as **Void**
	Add a Location or Locations to the MapPolyline object location [Array](../Lang/Array.md).
- [**clear**](#clear-instance_function "clear (Instance Function)") () as **Void**
	Clear all the [Location](../Position/Location.md) objects from the MapPolyline object's location [Array](../Lang/Array.md).
- [**getLocation**](#getLocation-instance_function "getLocation (Instance Function)") (index as [Lang.Number](../Lang/Number.md)) as [Position.Location](../Position/Location.md) or **Null**
	Get the [Location](../Position/Location.md) object at a provided index in this MapPolyline object.
- [**numLocations**](#numLocations-instance_function "numLocations (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the number of [Location](../Position/Location.md) objects in this MapPolyline object.
- [**setColor**](#setColor-instance_function "setColor (Instance Function)") (color as [Graphics.ColorType](../Graphics.md#ColorType-named_type)) as **Void**
	Set the color of the MapPolyline to draw on the map.
- [**setWidth**](#setWidth-instance_function "setWidth (Instance Function)") (width as [Lang.Number](../Lang/Number.md)) as **Void**
	Set the width of the MapPolyline to draw on the map.

## Instance Method Details

### addLocation(location as Position.Location or Lang.Array<Position.Location>) as Void

Add a Location or Locations to the MapPolyline object location [Array](../Lang/Array.md).

### clear() as Void

Clear all the [Location](../Position/Location.md) objects from the MapPolyline object's location [Array](../Lang/Array.md).

### getLocation(index as Lang.Number) as Position.Location or Null

Get the [Location](../Position/Location.md) object at a provided index in this MapPolyline object.

### numLocations() as Lang.Number

Get the number of [Location](../Position/Location.md) objects in this MapPolyline object.

### setColor(color as Graphics.ColorType) as Void

Set the color of the MapPolyline to draw on the map.

### setWidth(width as Lang.Number) as Void

Set the width of the MapPolyline to draw on the map.
