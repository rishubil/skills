---
title: Toybox.WatchUi.PickerDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerDelegate.html
---

## Class: Toybox.WatchUi.PickerDelegate

## Overview

## See Also:

- [Toybox.WatchUi.Picker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Picker.html)
Note:

[popView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#popView-instance_function) is not automatically called once a Picker selection is made

Note:

See the Picker sample distributed with the SDK for an example of the use of the PickerDelegate class

## Instance Method Summary

- [**onAccept**](#onAccept-instance_function "onAccept (Instance Function)") (values as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Handle a confirm event from a Picker.
- [**onActionMenu**](#onActionMenu-instance_function "onActionMenu (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
- [**onCancel**](#onCancel-instance_function "onCancel (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Handle a cancel event from a Picker.

## Instance Method Details

### onAccept(values as Lang.Array) as Lang.Boolean

Note:

A `null` value will be returned for any [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) entries
