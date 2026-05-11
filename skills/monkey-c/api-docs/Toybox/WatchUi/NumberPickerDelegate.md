---
title: Toybox.WatchUi.NumberPickerDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPickerDelegate.html
---

## Class: Toybox.WatchUi.NumberPickerDelegate

## Overview

NumberPickerDelegate responds to a NumberPicker selection.

This class should be extended to handle the specified number.

**This has been deprecated**

This class may be removed after System 3.

## See Also:

- [Toybox.WatchUi.NumberPicker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPicker.html)

## Instance Method Summary

- [**onNumberPicked**](#onNumberPicked-instance_function "onNumberPicked (Instance Function)") (value as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Time.Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A number was entered in a NumberPicker.

## Instance Method Details

### onNumberPicked(value as Lang.Number or Lang.Float or Time.Duration) as Lang.Boolean

A number was entered in a NumberPicker.

This method is called when a number has been specified by a NumberPicker, and receives the numeric value as an argument.
