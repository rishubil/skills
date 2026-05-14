---
title: Toybox.WatchUi.View
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html
---

## Class: Toybox.WatchUi.View

## Overview

## See Also:

- [Toybox.WatchUi.Drawable](Drawable.md)

## Direct Known Subclasses

[WatchUi.DataField](DataField.md), [WatchUi.DataFieldAlert](DataFieldAlert.md), [WatchUi.GlanceView](GlanceView.md), [WatchUi.MapView](MapView.md), [WatchUi.Menu2](Menu2.md), [WatchUi.Picker](Picker.md), [WatchUi.WatchFace](WatchFace.md)

## Typedef Summary

- [**ActionMenuIndicatorOptions**](#ActionMenuIndicatorOptions-named_type "ActionMenuIndicatorOptions (Named Type)") as {:enabled as [Lang.Boolean](../Lang/Boolean.md) }
- [**ControlBarOptions**](#ControlBarOptions-named_type "ControlBarOptions (Named Type)") as {:leftButton as [WatchUi.ControlBarLeftButton](../WatchUi.md#ControlBarLeftButton-module),:title as [Lang.String](../Lang/String.md),:rightButton as [WatchUi.ControlBarRightButton](../WatchUi.md#ControlBarRightButton-module) }

## Instance Method Summary

- [**addLayer**](#addLayer-instance_function "addLayer (Instance Function)") (layer as [WatchUi.Layer](Layer.md)) as **Void**
	Add a [WatchUi.Layer](Layer.md) on the top of view's layer stack.
- [**clearLayers**](#clearLayers-instance_function "clearLayers (Instance Function)") () as **Void**
	Clear all layers that are added to the view.
- [**findDrawableById**](#findDrawableById-instance_function "findDrawableById (Instance Function)") (identifier as [Lang.Object](../Lang/Object.md)) as [WatchUi.Drawable](Drawable.md) or **Null**
	Find a Drawable by its ID.
- [**getLayerIndex**](#getLayerIndex-instance_function "getLayerIndex (Instance Function)") (layer as [WatchUi.Layer](Layer.md)) as [Lang.Number](../Lang/Number.md)
	Return the index of the layer from the bottom of the view layer stack.
- [**getLayers**](#getLayers-instance_function "getLayers (Instance Function)") () as [Lang.Array](../Lang/Array.md) < [WatchUi.Layer](Layer.md) > or **Null**
	Get a copy of the layer stack currently added to the view, sorted by the drawing order, i.e.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**insertLayer**](#insertLayer-instance_function "insertLayer (Instance Function)") (layer as [WatchUi.Layer](Layer.md), idx as [Lang.Number](../Lang/Number.md)) as **Void**
	Insert the layer at the given index in the layer stack, this will stop animation playback.
- [**onHide**](#onHide-instance_function "onHide (Instance Function)") () as **Void**
	Hide the View.
- [**onLayout**](#onLayout-instance_function "onLayout (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	The entry point for the View.
- [**onShow**](#onShow-instance_function "onShow (Instance Function)") () as **Void**
	Show the View.
- [**onUpdate**](#onUpdate-instance_function "onUpdate (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Update the View.
- [**removeLayer**](#removeLayer-instance_function "removeLayer (Instance Function)") (layer as [WatchUi.Layer](Layer.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Remove a layer from the view layer stack, this will stop animation playback.
- [**setActionMenuIndicator**](#setActionMenuIndicator-instance_function "setActionMenuIndicator (Instance Function)") (options as [View.ActionMenuIndicatorOptions](View.md#ActionMenuIndicatorOptions-named_type) or **Null**) as **Void**
- [**setClockHandPosition**](#setClockHandPosition-instance_function "setClockHandPosition (Instance Function)") (options as {:clockState as [WatchUi.AnalogClockState](../WatchUi.md#AnalogClockState-module),:hour as [Lang.Number](../Lang/Number.md) or **Null**,:minute as [Lang.Number](../Lang/Number.md) or **Null** }) as [Lang.Boolean](../Lang/Boolean.md)
	Set the clock hands position.
- [**setControlBar**](#setControlBar-instance_function "setControlBar (Instance Function)") (options as [View.ControlBarOptions](View.md#ControlBarOptions-named_type) or **Null**) as **Void**
	Set control bar options for this view.
- [**setKeyToSelectableInteraction**](#setKeyToSelectableInteraction-instance_function "setKeyToSelectableInteraction (Instance Function)") (enable as [Lang.Boolean](../Lang/Boolean.md)) as **Void**
	Enter Selectable interaction mode.
- [**setLayout**](#setLayout-instance_function "setLayout (Instance Function)") (layout as [Lang.Array](../Lang/Array.md) < [WatchUi.Drawable](Drawable.md) > or **Null**) as **Void**
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

Control bar visibility changes made from [onLayout](View.md#onLayout-instance_function) or [onUpdate](View.md#onUpdate-instance_function) will result in an exception.
