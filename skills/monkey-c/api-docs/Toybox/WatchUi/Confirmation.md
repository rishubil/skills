---
title: Toybox.WatchUi.Confirmation
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Confirmation.html
---

## Class: Toybox.WatchUi.Confirmation

## Overview

A representation of a confirmation dialog.

A Confirmation is a special View that presents the user with a yes/no question. After an option is selected, the registered [onResponse()](ConfirmationDelegate.md#onResponse-instance_function) method will be called. A Confirmation is pushed using [pushView()](../WatchUi.md#pushView-instance_function), which provides a [ConfirmationDelegate](ConfirmationDelegate.md) as the input delegate.

## See Also:

- [Toybox.WatchUi.ConfirmationDelegate](ConfirmationDelegate.md)
- [WatchUi.pushView()](../WatchUi.md#pushView-instance_function)
Note:

The look and feel of a confirmation dialog is device-specific.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (message as [Lang.String](../Lang/String.md))
	Constructor.

## Instance Method Details

### initialize(message as Lang.String)

Constructor
