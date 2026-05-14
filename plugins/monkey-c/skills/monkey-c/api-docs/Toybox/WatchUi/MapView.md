---
title: Toybox.WatchUi.MapView
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html
---

## Class: Toybox.WatchUi.MapView

## Overview

A [View](View.md) for rendering a map on the screen.

The map is rendered statically and focused on the bounding box and/or a MapMarker point or MapPolyline drawn on the map. The map can be rendered in [MAP\_MODE\_BROWSE](../WatchUi.md) or [MAP\_MODE\_PREVIEW](../WatchUi.md) mode.

## Direct Known Subclasses

[WatchUi.MapTrackView](MapTrackView.md)

## Instance Method Summary

- [**clear**](#clear-instance_function "clear (Instance Function)") () as **Void**
	Clear all the objects from the map.
- [**getMapMode**](#getMapMode-instance_function "getMapMode (Instance Function)") () as [WatchUi.MapMode](../WatchUi.md#MapMode-module)
	Get the current mode for the map in this MapView.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**setMapMarker**](#setMapMarker-instance_function "setMapMarker (Instance Function)") (markers as [WatchUi.MapMarker](MapMarker.md) or [Lang.Array](../Lang/Array.md) < [WatchUi.MapMarker](MapMarker.md) >) as **Void**
	Add a [MapMarker](MapMarker.md) object or an [Array](../Lang/Array.md) of MapMarker objects to be rendered on the map.
- [**setMapMode**](#setMapMode-instance_function "setMapMode (Instance Function)") (mode as [WatchUi.MapMode](../WatchUi.md#MapMode-module)) as **Void**
	Set the mode for the map in this MapView.
- [**setMapVisibleArea**](#setMapVisibleArea-instance_function "setMapVisibleArea (Instance Function)") (topLeft as [Position.Location](../Position/Location.md), bottomRight as [Position.Location](../Position/Location.md)) as **Void**
	Select the area of the map to render on the screen with a bounding box.
- [**setPolyline**](#setPolyline-instance_function "setPolyline (Instance Function)") (polyline as [WatchUi.MapPolyline](MapPolyline.md)) as **Void**
	Add [MapPolyline](MapPolyline.md) object to be rendered on the map.
- [**setScreenVisibleArea**](#setScreenVisibleArea-instance_function "setScreenVisibleArea (Instance Function)") (topLeftX as [Lang.Number](../Lang/Number.md), topLeftY as [Lang.Number](../Lang/Number.md), bottomRightX as [Lang.Number](../Lang/Number.md), bottomRightY as [Lang.Number](../Lang/Number.md)) as **Void**
	Set the area on the screen to focus the map.

## Instance Method Details

### clear() as Void

Clear all the objects from the map.

Removes all [MapPolyline](MapPolyline.md) and [MapMarker](MapMarker.md) objects.

### getMapMode() as WatchUi.MapMode

Get the current mode for the map in this MapView.

### initialize()

Constructor

### setMapMarker(markers as WatchUi.MapMarker or Lang.Array<WatchUi.MapMarker>) as Void

Add a [MapMarker](MapMarker.md) object or an [Array](../Lang/Array.md) of MapMarker objects to be rendered on the map.

### setMapMode(mode as WatchUi.MapMode) as Void

Set the mode for the map in this MapView.

### setMapVisibleArea(topLeft as Position.Location, bottomRight as Position.Location) as Void

Select the area of the map to render on the screen with a bounding box. A redraw of the current underlying map data will occur, so calling this function inside of onUpdate() is discouraged as it could lead to map flicker.

### setPolyline(polyline as WatchUi.MapPolyline) as Void

Add [MapPolyline](MapPolyline.md) object to be rendered on the map.

### setScreenVisibleArea(topLeftX as Lang.Number, topLeftY as Lang.Number, bottomRightX as Lang.Number, bottomRightY as Lang.Number) as Void

Set the area on the screen to focus the map.
