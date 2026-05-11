---
title: Toybox.WatchUi.NumberPicker
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPicker.html
---

## Class: Toybox.WatchUi.NumberPicker

## Overview

A representation of an on-screen number picker.

A NumberPicker is a special View that provides a way to specify numeric values within an app. A NumberPicker is pushed using [pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function) and provides a [NumberPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPickerDelegate.html) as the input delegate.

The NumberPicker class is limited to the eight specific modes described by the [WatchUi.NUMBER\_PICKER\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#NUMBER_PICKER_DISTANCE-const) types enum. There are set minimum and maximum values enforced by the product for each mode, and the initial value of the NumberPicker will be adjusted to fall within these bounds.

**This has been deprecated**

This class may be removed after System 3.

## See Also:

- [Toybox.WatchUi.NumberPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPickerDelegate.html)
Note:

The look and feel of a number picker is device-specific.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (mode as [WatchUi.NumberPickerMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#NumberPickerMode-module), initialValue as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Time.Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html))
	Constructor.

## Instance Method Details

### initialize(mode as WatchUi.NumberPickerMode, initialValue as Lang.Number or Lang.Float or Time.Duration)

Constructor
