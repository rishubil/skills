---
title: Toybox.WatchUi.TextPickerDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPickerDelegate.html
---

## Class: Toybox.WatchUi.TextPickerDelegate

## Overview

TextPickerDelegate responds to a TextPicker selection.

This class should be extended to handle the specified text.

## See Also:

- [Toybox.WatchUi.TextPicker](TextPicker.md)

## Instance Method Summary

- [**onCancel**](#onCancel-instance_function "onCancel (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Text entry has been canceled.
- [**onTextEntered**](#onTextEntered-instance_function "onTextEntered (Instance Function)") (text as [Lang.String](../Lang/String.md), changed as [Lang.Boolean](../Lang/Boolean.md)) as [Lang.Boolean](../Lang/Boolean.md)
	A text string was entered into a TextPicker.

## Instance Method Details

### onCancel() as Lang.Boolean

Text entry has been canceled.

### onTextEntered(text as Lang.String, changed as Lang.Boolean) as Lang.Boolean

A text string was entered into a TextPicker.

This method is called when text has been specified by a TextPicker, and receives the text String as an argument.
