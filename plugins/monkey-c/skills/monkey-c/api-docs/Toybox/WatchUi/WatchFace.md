---
title: Toybox.WatchUi.WatchFace
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html
---

## Class: Toybox.WatchUi.WatchFace

## Overview

Create a Watch Face that supports exiting/entering low power mode.

A WatchFace is a special View that provides notifications when the device changes power states.

A WatchFace will run in a high power mode for a short period when responding to a gesture (i.e., raising the watch to check the time) or when returning to the watch face from another application. While in high power mode, the watch face will perform full screen updates every second via calls to [onUpdate()](View.md#onUpdate-instance_function), and the application will have access to timers and animations.

After this period in high power mode (typically about ten seconds), the system will call [onEnterSleep()](WatchFace.md#onEnterSleep-instance_function) to notify the application that it is preparing to enter low power mode.

During low power mode the system will call [onUpdate()](View.md#onUpdate-instance_function) at the top of every minute. If partial update support is available, the [onPartialUpdate()](WatchFace.md#onPartialUpdate-instance_function) method will be called for the first 59 seconds of every minute. The application will not have access to timers or animations while in low power mode.

When a gesture occurs while running in low power mode the system will call [onExitSleep()](WatchFace.md#onExitSleep-instance_function) to notify the application that the transition to high power mode has occurred.

The initial view of a watch face application `must` extend [WatchFace](WatchFace.md).

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onEnterSleep**](#onEnterSleep-instance_function "onEnterSleep (Instance Function)") () as **Void**
	The device is entering low power mode.
- [**onExitSleep**](#onExitSleep-instance_function "onExitSleep (Instance Function)") () as **Void**
	The device is exiting low power mode.
- [**onPartialUpdate**](#onPartialUpdate-instance_function "onPartialUpdate (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Update a portion of the screen.

## Instance Method Details

### initialize()

Constructor

### onEnterSleep() as Void

The device is entering low power mode.

Terminate any active timers and prepare for once-per-minute updates.

### onExitSleep() as Void

The device is exiting low power mode.

Timers and animations may be started here in preparation for once-per-second updates.

### onPartialUpdate(dc as Graphics.Dc) as Void

Update a portion of the screen.

Partial updates can be used to update a small part of the screen to allow for Always On Watch Faces.

This method is called each second as long as the device power budget is not exceeded. It is important to update as small of a portion of the display as possible in this method to avoid exceeding the allowed power budget. To do this, the application must set the clipping region for the [Graphics.Dc](../Graphics/Dc.md) object using the [setClip()](../Graphics/Dc.md#setClip-instance_function) method. Calls to [System.println()](../System.md#println-instance_function) and [System.print()](../System.md#print-instance_function) will not execute on devices when this function is being invoked, but can be used in the device simulator.

If the call to this method exceeds the power budget of the device, the partial update will not draw and a call to [onPowerBudgetExceeded()](WatchFaceDelegate.md#onPowerBudgetExceeded-instance_function) is made to report the limits that were exceeded.

Note:

See the Analog sample distributed with the SDK for an example of onPartialUpdate() using clipping regions
