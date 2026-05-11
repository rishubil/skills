---
title: Toybox.WatchUi.ProgressBar
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ProgressBar.html
---

## Class: Toybox.WatchUi.ProgressBar

## Overview

A representation of an on-screen progress bar.

A ProgressBar is a special View that presents the user with a progress indicator. These can display a string and either an incremental progress bar from 0-100% or a "busy" indicator. A ProgressBar is pushed using [pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function), which provides either `null` or a [BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html). If a BehaviorDelegate is provided, the [onBack()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html#onBack-instance_function) method will be called if Back button is pressed while the ProgressBar is displayed.

Note:

The look and feel of a progress bar is device-specific.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (displayString as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), startValue as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**)
	Constructor.
- [**setDisplayString**](#setDisplayString-instance_function "setDisplayString (Instance Function)") (displayString as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as **Void**
	Set the string to display on the ProgressBar.
- [**setProgress**](#setProgress-instance_function "setProgress (Instance Function)") (progressValue as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**) as **Void**
	Set the value of the ProgressBar.

## Instance Method Details

### initialize(displayString as Lang.String, startValue as Lang.Float or Null)

Constructor

### setDisplayString(displayString as Lang.String) as Void

Set the string to display on the ProgressBar.

### setProgress(progressValue as Lang.Float or Null) as Void

Set the value of the ProgressBar.
