---
title: Toybox.WatchUi.TextPicker
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPicker.html
---

## Class: Toybox.WatchUi.TextPicker

## Overview

A representation of an on-screen text picker.

A TextPicker is a special View that provides a way to specify textual input in an app. A TextPicker is pushed using [pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function), and provides a [TextPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPickerDelegate.html) as the input delegate. A default value can be provided and is displayed as editable text with the cursor placed at the end.

## See Also:

- [Toybox.WatchUi.TextPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPickerDelegate.html)
Note:

The look and feel of a text picker is device-specific.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (initialText as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html))
	Constructor.

## Instance Method Details

### initialize(initialText as Lang.String)

Constructor
