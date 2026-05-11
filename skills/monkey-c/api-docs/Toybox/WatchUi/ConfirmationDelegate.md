---
title: Toybox.WatchUi.ConfirmationDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ConfirmationDelegate.html
---

## Class: Toybox.WatchUi.ConfirmationDelegate

## Overview

ConfirmationDelegate responds to a [Confirmation](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Confirmation.html) selection.

## See Also:

- [Toybox.WatchUi.Confirmation](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Confirmation.html)

## Instance Method Summary

- [**onResponse**](#onResponse-instance_function "onResponse (Instance Function)") (response as [WatchUi.Confirm](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Confirm-module)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A confirmation selection was made.

## Instance Method Details

### onResponse(response as WatchUi.Confirm) as Lang.Boolean

A confirmation selection was made.

This method is called when a [Confirmation](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Confirmation.html) response is selected, and receives the response as an argument. The response is either a [CONFIRM\_NO](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#CONFIRM_NO-const) or [CONFIRM\_YES](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#CONFIRM_YES-const) value.
