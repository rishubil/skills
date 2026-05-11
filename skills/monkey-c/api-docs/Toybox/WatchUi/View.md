---
title: Toybox.WatchUi.View
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html
---

## Class: Toybox.WatchUi.View

## Overview

## See Also:

- [Toybox.WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html)

## Direct Known Subclasses

[WatchUi.DataField](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html), [WatchUi.DataFieldAlert](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataFieldAlert.html), [WatchUi.GlanceView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/GlanceView.html), [WatchUi.MapView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html), [WatchUi.Menu2](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html), [WatchUi.Picker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Picker.html), [WatchUi.WatchFace](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html)

## Typedef Summary

- [**ActionMenuIndicatorOptions**](#ActionMenuIndicatorOptions-named_type "ActionMenuIndicatorOptions (Named Type)") as {:enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) }
- [**ControlBarOptions**](#ControlBarOptions-named_type "ControlBarOptions (Named Type)") as {:leftButton as [WatchUi.ControlBarLeftButton](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#ControlBarLeftButton-module),:title as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html),:rightButton as [WatchUi.ControlBarRightButton](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#ControlBarRightButton-module) }

## Instance Method Summary

- [**addLayer**](#addLayer-instance_function "addLayer (Instance Function)") (layer as [WatchUi.Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html)) as **Void**
	Add a [WatchUi.Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html) on the top of view's layer stack.
- [**clearLayers**](#clearLayers-instance_function "clearLayers (Instance Function)") () as **Void**
	Clear all layers that are added to the view.
- [**findDrawableById**](#findDrawableById-instance_function "findDrawableById (Instance Function)") (identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	Find a Drawable by its ID.
- [**getLayerIndex**](#getLayerIndex-instance_function "getLayerIndex (Instance Function)") (layer as [WatchUi.Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Return the index of the layer from the bottom of the view layer stack.
- [**getLayers**](#getLayers-instance_function "getLayers (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [WatchUi.Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html) > or **Null**
	Get a copy of the layer stack currently added to the view, sorted by the drawing order, i.e.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**insertLayer**](#insertLayer-instance_function "insertLayer (Instance Function)") (layer as [WatchUi.Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html), idx as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Insert the layer at the given index in the layer stack, this will stop animation playback.
- [**onHide**](#onHide-instance_function "onHide (Instance Function)") () as **Void**
	Hide the View.
- [**onLayout**](#onLayout-instance_function "onLayout (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	The entry point for the View.
- [**onShow**](#onShow-instance_function "onShow (Instance Function)") () as **Void**
	Show the View.
- [**onUpdate**](#onUpdate-instance_function "onUpdate (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Update the View.
- [**removeLayer**](#removeLayer-instance_function "removeLayer (Instance Function)") (layer as [WatchUi.Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Remove a layer from the view layer stack, this will stop animation playback.
- [**setActionMenuIndicator**](#setActionMenuIndicator-instance_function "setActionMenuIndicator (Instance Function)") (options as [View.ActionMenuIndicatorOptions](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#ActionMenuIndicatorOptions-named_type) or **Null**) as **Void**
- [**setClockHandPosition**](#setClockHandPosition-instance_function "setClockHandPosition (Instance Function)") (options as {:clockState as [WatchUi.AnalogClockState](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#AnalogClockState-module),:hour as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**,:minute as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null** }) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Set the clock hands position.
- [**setControlBar**](#setControlBar-instance_function "setControlBar (Instance Function)") (options as [View.ControlBarOptions](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#ControlBarOptions-named_type) or **Null**) as **Void**
	Set control bar options for this view.
- [**setKeyToSelectableInteraction**](#setKeyToSelectableInteraction-instance_function "setKeyToSelectableInteraction (Instance Function)") (enable as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as **Void**
	Enter Selectable interaction mode.
- [**setLayout**](#setLayout-instance_function "setLayout (Instance Function)") (layout as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) > or **Null**) as **Void**
	Set the layout for the View.

## Typedef Details

### ActionMenuIndicatorOptions as {:enabled as Lang.Boolean }

### ControlBarOptions as {:leftButton as WatchUi.ControlBarLeftButton,:title as Lang.String,:rightButton as WatchUi.ControlBarRightButton }

## Instance Method Details

### addLayer(layer as WatchUi.Layer) as Void

### clearLayers() as Void

### findDrawableById(identifier as Lang.Object) as WatchUi.Drawable or Null

### getLayerIndex(layer as WatchUi.Layer) as Lang.Number

### getLayers() as Lang.Array<WatchUi.Layer> or Null

### initialize()

### insertLayer(layer as WatchUi.Layer, idx as Lang.Number) as Void

### onHide() as Void

### onLayout(dc as Graphics.Dc) as Void

### onShow() as Void

### onUpdate(dc as Graphics.Dc) as Void

### removeLayer(layer as WatchUi.Layer) as Lang.Boolean

### setActionMenuIndicator(options as View.ActionMenuIndicatorOptions or Null) as Void

### setClockHandPosition(options as {:clockState as WatchUi.AnalogClockState,:hour as Lang.Number or Null,:minute as Lang.Number or Null }) as Lang.Boolean

### setControlBar(options as View.ControlBarOptions or Null) as Void

Note:

Control bar visibility changes made from [onLayout](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onLayout-instance_function) or [onUpdate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onUpdate-instance_function) will result in an exception.
