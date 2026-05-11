---
title: Toybox.WatchUi.ConfirmationDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ConfirmationDelegate.html
---

## Class: Toybox.WatchUi.ConfirmationDelegate

## Overview

ConfirmationDelegate responds to a [Confirmation](Confirmation.md) selection.

## See Also:

- [Toybox.WatchUi.Confirmation](Confirmation.md)

## Instance Method Summary

- [**onResponse**](#onResponse-instance_function "onResponse (Instance Function)") (response as [WatchUi.Confirm](../WatchUi.md#Confirm-module)) as [Lang.Boolean](../Lang/Boolean.md)
	A confirmation selection was made.

## Instance Method Details

### onResponse(response as WatchUi.Confirm) as Lang.Boolean

A confirmation selection was made.

This method is called when a [Confirmation](Confirmation.md) response is selected, and receives the response as an argument. The response is either a [CONFIRM\_NO](../WatchUi.md#CONFIRM_NO-const) or [CONFIRM\_YES](../WatchUi.md#CONFIRM_YES-const) value.
