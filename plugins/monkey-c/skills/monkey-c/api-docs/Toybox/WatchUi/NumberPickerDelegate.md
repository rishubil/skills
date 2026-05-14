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

- [Toybox.WatchUi.NumberPicker](NumberPicker.md)

## Instance Method Summary

- [**onNumberPicked**](#onNumberPicked-instance_function "onNumberPicked (Instance Function)") (value as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md) or [Time.Duration](../Time/Duration.md)) as [Lang.Boolean](../Lang/Boolean.md)
	A number was entered in a NumberPicker.

## Instance Method Details

### onNumberPicked(value as Lang.Number or Lang.Float or Time.Duration) as Lang.Boolean

A number was entered in a NumberPicker.

This method is called when a number has been specified by a NumberPicker, and receives the numeric value as an argument.
