---
title: Toybox.FitContributor.Field
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html
---

## Class: Toybox.FitContributor.Field

## Overview

A Field records custom FIT data from an Application or Data Field to a FIT file on the device's file system.

Once a Field is created with the [createField()](../ActivityRecording/Session.md#createField-instance_function) method, you can submit the next Field value with [setData()](Field.md#setData-instance_function), which will get written to the FIT file at the next opportunity. Depending on the device, writes to the FIT file may occur once per second or when new data is available (Smart Recording). Best practice is to only call [setData()](Field.md#setData-instance_function) when values have changed to accommodate Smart Recording.

If [setData()](Field.md#setData-instance_function) is called before the previous data is written out, the previous value will be lost and replaced by the current data. For this reason, we do not recommend using this feature for time-sensitive data requiring sub-second granularity.

## See Also:

- [Session.createField()](../ActivityRecording/Session.md#createField-instance_function)
- [Smart Recording vs. Every Second Recording](https://support.garmin.com/?faq=s4w6kZmbmK0P6l20SgpW28)
- [Learn more about the FIT format](http://www.thisisant.com/resources/fit)

## Instance Method Summary

- [**setData**](#setData-instance_function "setData (Instance Function)") (input as [Lang.Object](../Lang/Object.md)) as **Void**
	Set the value to write to this Field.

## Instance Method Details

### setData(input as Lang.Object) as Void

Set the value to write to this Field.
