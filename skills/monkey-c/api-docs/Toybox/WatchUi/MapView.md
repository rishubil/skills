---
title: Toybox.WatchUi.MapView
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html
---

## Class: Toybox.WatchUi.MapView

## Overview

A [View](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html) for rendering a map on the screen.

The map is rendered statically and focused on the bounding box and/or a MapMarker point or MapPolyline drawn on the map. The map can be rendered in [MAP\_MODE\_BROWSE](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html) or [MAP\_MODE\_PREVIEW](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html) mode.

## Direct Known Subclasses

[WatchUi.MapTrackView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapTrackView.html)

## Instance Method Summary

- [**clear**](#clear-instance_function "clear (Instance Function)") () as **Void**
	Clear all the objects from the map.
- [**getMapMode**](#getMapMode-instance_function "getMapMode (Instance Function)") () as [WatchUi.MapMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#MapMode-module)
	Get the current mode for the map in this MapView.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**setMapMarker**](#setMapMarker-instance_function "setMapMarker (Instance Function)") (markers as [WatchUi.MapMarker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [WatchUi.MapMarker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html) >) as **Void**
	Add a [MapMarker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html) object or an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of MapMarker objects to be rendered on the map.
- [**setMapMode**](#setMapMode-instance_function "setMapMode (Instance Function)") (mode as [WatchUi.MapMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#MapMode-module)) as **Void**
	Set the mode for the map in this MapView.
- [**setMapVisibleArea**](#setMapVisibleArea-instance_function "setMapVisibleArea (Instance Function)") (topLeft as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html), bottomRight as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html)) as **Void**
	Select the area of the map to render on the screen with a bounding box.
- [**setPolyline**](#setPolyline-instance_function "setPolyline (Instance Function)") (polyline as [WatchUi.MapPolyline](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapPolyline.html)) as **Void**
	Add [MapPolyline](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapPolyline.html) object to be rendered on the map.
- [**setScreenVisibleArea**](#setScreenVisibleArea-instance_function "setScreenVisibleArea (Instance Function)") (topLeftX as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), topLeftY as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), bottomRightX as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), bottomRightY as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Set the area on the screen to focus the map.

## Instance Method Details

### clear() as Void

Clear all the objects from the map.

Removes all [MapPolyline](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapPolyline.html) and [MapMarker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html) objects.

### getMapMode() as WatchUi.MapMode

Get the current mode for the map in this MapView.

### initialize()

Constructor

### setMapMarker(markers as WatchUi.MapMarker or Lang.Array<WatchUi.MapMarker>) as Void

Add a [MapMarker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html) object or an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of MapMarker objects to be rendered on the map.

### setMapMode(mode as WatchUi.MapMode) as Void

Set the mode for the map in this MapView.

### setMapVisibleArea(topLeft as Position.Location, bottomRight as Position.Location) as Void

Select the area of the map to render on the screen with a bounding box. A redraw of the current underlying map data will occur, so calling this function inside of onUpdate() is discouraged as it could lead to map flicker.

### setPolyline(polyline as WatchUi.MapPolyline) as Void

Add [MapPolyline](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapPolyline.html) object to be rendered on the map.

### setScreenVisibleArea(topLeftX as Lang.Number, topLeftY as Lang.Number, bottomRightX as Lang.Number, bottomRightY as Lang.Number) as Void

Set the area on the screen to focus the map.
