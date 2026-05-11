---
title: Toybox.WatchUi.WatchFaceDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFaceDelegate.html
---

## Class: Toybox.WatchUi.WatchFaceDelegate

## Overview

Receive events on a Watch Face.

## See Also:

- [Toybox.WatchUi.WatchFace](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html)

## Instance Method Summary

- [**getComplicationDrawable**](#getComplicationDrawable-instance_function "getComplicationDrawable (Instance Function)") (complication as [WatchFaceConfig.ComplicationRef](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/ComplicationRef.html)) as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [WatchUi.ComplicationDrawableRef](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ComplicationDrawableRef.html) or **Null**
	Get a Drawable for highlighting purposes.
- [**onPowerBudgetExceeded**](#onPowerBudgetExceeded-instance_function "onPowerBudgetExceeded (Instance Function)") (powerInfo as [WatchUi.WatchFacePowerInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFacePowerInfo.html)) as **Void**
	Handle a partial update exceeding the power budget.
- [**onPress**](#onPress-instance_function "onPress (Instance Function)") (clickEvent as [WatchUi.ClickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ClickEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Called when user does a touch and hold.
- [**onTap**](#onTap-instance_function "onTap (Instance Function)") (clickEvent as [WatchUi.ClickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ClickEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A screen tap event has occurred.
- [**onWatchFaceConfigEdited**](#onWatchFaceConfigEdited-instance_function "onWatchFaceConfigEdited (Instance Function)") (options as {:configId as [WatchFaceConfig.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Id.html),:type as [WatchUi.WatchFaceConfigType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#WatchFaceConfigType-module) or **Null**,:committed as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) }) as **Void**
	A watchface config change has occurred.
- [**setSelectedComplication**](#setSelectedComplication-instance_function "setSelectedComplication (Instance Function)") (complicationIdentifier as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Set the selected complication field.

## Instance Method Details

### getComplicationDrawable(complication as WatchFaceConfig.ComplicationRef) as WatchUi.Drawable or WatchUi.ComplicationDrawableRef or Null

Get a Drawable for highlighting purposes.

Called by system to get a Drawable for the given complication field for highlighting purposes. Only available in WatchFace config mode. Animation will be easing around the center of the Drawable. The Dc object passed to the Drawable.draw function shares the same origin as screen, e.g. at \[0, 0\], so it's aligned with the drawable coordinates for convenience.

### onPowerBudgetExceeded(powerInfo as WatchUi.WatchFacePowerInfo) as Void

Handle a partial update exceeding the power budget.

If the [onPartialUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html#onPartialUpdate-instance_function) callback of the associated [WatchFace](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html) exceeds the power budget of the device, this method will be called with information about the limits that were exceeded.

### onPress(clickEvent as WatchUi.ClickEvent) as Lang.Boolean

Called when user does a touch and hold

### onTap(clickEvent as WatchUi.ClickEvent) as Lang.Boolean

A screen tap event has occurred.

Only available in WatchFace config mode. Can be overridden by application to change the selected `complication`, using [WatchFaceDelegate.setSelectedComplication()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFaceDelegate.html#setSelectedComplication-instance_function)

### onWatchFaceConfigEdited(options as {:configId as WatchFaceConfig.Id,:type as WatchUi.WatchFaceConfigType or Null,:committed as Lang.Boolean }) as Void

A watchface config change has occurred.

Only available in WatchFace config mode, application can call [WatchFaceConfig.getSettings()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig.html#getSettings-instance_function) to retrieve the current settings.

### setSelectedComplication(complicationIdentifier as Lang.Number) as Void

Set the selected complication field.

Can be called by application when handling `onTap` event, to change the selected (highlighted) complication. Only effective during WatchFace config mode.
