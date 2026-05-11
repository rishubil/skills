---
title: Toybox.WatchUi.Confirmation
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Confirmation.html
---

## Class: Toybox.WatchUi.Confirmation

## Overview

A representation of a confirmation dialog.

A Confirmation is a special View that presents the user with a yes/no question. After an option is selected, the registered [onResponse()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ConfirmationDelegate.html#onResponse-instance_function) method will be called. A Confirmation is pushed using [pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function), which provides a [ConfirmationDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ConfirmationDelegate.html) as the input delegate.

## See Also:

- [Toybox.WatchUi.ConfirmationDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ConfirmationDelegate.html)
- [WatchUi.pushView()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#pushView-instance_function)
Note:

The look and feel of a confirmation dialog is device-specific.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (message as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html))
	Constructor.

## Instance Method Details

### initialize(message as Lang.String)

Constructor
