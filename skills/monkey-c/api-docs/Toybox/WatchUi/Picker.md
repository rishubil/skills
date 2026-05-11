---
title: Toybox.WatchUi.Picker
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Picker.html
---

## Class: Toybox.WatchUi.Picker

## Overview

A representation of an on-screen generic picker.

A Picker consists of one or more choose-able objects, a title, a next and previous arrow, and a confirmation button. The next and previous arrows and the confirmation button are device specific but can be overridden if desired. A Picker is pushed using [pushView()](../WatchUi.md#pushView-instance_function), which provides a [PickerDelegate](PickerDelegate.md).

A [PickerFactory](PickerFactory.md) is required to indicate what should be displayed for each pick-able value, and is capable of displaying any number of entries from which may be chosen. For example, consider the following:

```
new NumberFactory();
new Ui.Text({:text=>"-"});
new NumberFactory();
```

This Picker will have three entries: a choosable number, a non-choosable "-", and another choosable number.

## See Also:

- [Toybox.WatchUi.PickerDelegate](PickerDelegate.md)
- [Toybox.WatchUi.PickerFactory](PickerFactory.md)
Note:

See the Picker sample distributed with the SDK for an example of the use of the Picker class

Note:

The look and feel of a Picker is device-specific, though every device will have the same general layout.

## Typedef Summary

- [**Options**](#Options-named_type "Options (Named Type)") as {:title as [WatchUi.Drawable](Drawable.md),:pattern as [Lang.Array](../Lang/Array.md) < [WatchUi.Drawable](Drawable.md) or [WatchUi.PickerFactory](PickerFactory.md) >,:defaults as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >,:nextArrow as [WatchUi.Drawable](Drawable.md),:previousArrow as [WatchUi.Drawable](Drawable.md),:confirm as [WatchUi.Drawable](Drawable.md) }

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as [Picker.Options](Picker.md#Options-named_type))
	Constructor.
- [**setOptions**](#setOptions-instance_function "setOptions (Instance Function)") (options as [Picker.Options](Picker.md#Options-named_type)) as **Void**
	Set the options for the Picker.
