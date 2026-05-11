---
title: Toybox.WatchUi.TextPickerDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPickerDelegate.html
---

## Class: Toybox.WatchUi.TextPickerDelegate

## Overview

TextPickerDelegate responds to a TextPicker selection.

This class should be extended to handle the specified text.

## See Also:

- [Toybox.WatchUi.TextPicker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPicker.html)

## Instance Method Summary

- [**onCancel**](#onCancel-instance_function "onCancel (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Text entry has been canceled.
- [**onTextEntered**](#onTextEntered-instance_function "onTextEntered (Instance Function)") (text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), changed as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A text string was entered into a TextPicker.

## Instance Method Details

### onCancel() as Lang.Boolean

Text entry has been canceled.

### onTextEntered(text as Lang.String, changed as Lang.Boolean) as Lang.Boolean

A text string was entered into a TextPicker.

This method is called when text has been specified by a TextPicker, and receives the text String as an argument.
