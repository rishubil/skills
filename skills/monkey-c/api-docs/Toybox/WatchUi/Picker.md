---
title: Toybox.WatchUi.Picker
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Picker.html
---

## Class: Toybox.WatchUi.Picker

## Overview

A representation of an on-screen generic picker.

A Picker consists of one or more choose-able objects, a title, a next and previous arrow, and a confirmation button. The next and previous arrows and the confirmation button are device specific but can be overridden if desired. A Picker is pushed using [pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function), which provides a [PickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerDelegate.html).

A [PickerFactory](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerFactory.html) is required to indicate what should be displayed for each pick-able value, and is capable of displaying any number of entries from which may be chosen. For example, consider the following:

```
new NumberFactory();
new Ui.Text({:text=>"-"});
new NumberFactory();
```

This Picker will have three entries: a choosable number, a non-choosable "-", and another choosable number.

## See Also:

- [Toybox.WatchUi.PickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerDelegate.html)
- [Toybox.WatchUi.PickerFactory](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerFactory.html)
Note:

See the Picker sample distributed with the SDK for an example of the use of the Picker class

Note:

The look and feel of a Picker is device-specific, though every device will have the same general layout.

## Typedef Summary

- [**Options**](#Options-named_type "Options (Named Type)") as {:title as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:pattern as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or [WatchUi.PickerFactory](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerFactory.html) >,:defaults as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >,:nextArrow as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:previousArrow as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:confirm as [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) }

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as [Picker.Options](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Picker.html#Options-named_type))
	Constructor.
- [**setOptions**](#setOptions-instance_function "setOptions (Instance Function)") (options as [Picker.Options](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Picker.html#Options-named_type)) as **Void**
	Set the options for the Picker.
