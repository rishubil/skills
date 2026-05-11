---
title: Toybox.WatchUi.WatchFacePowerInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFacePowerInfo.html
---

## Class: Toybox.WatchUi.WatchFacePowerInfo

## Overview

Power information provided when the power budget is exceeded during a call to [onPartialUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html#onPartialUpdate-instance_function).

This is automatically passed to the [onPowerBudgetExceeded()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFaceDelegate.html#onPowerBudgetExceeded-instance_function) method when it is invoked.

## See Also:

- [Toybox.WatchUi.WatchFaceDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFaceDelegate.html)

## Instance Member Summary

- [**executionTimeAverage**](#executionTimeAverage-var "executionTimeAverage (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)
	The average partial update execution time [onPartialUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html#onPartialUpdate-instance_function) took to complete.
- [**executionTimeLimit**](#executionTimeLimit-var "executionTimeLimit (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)
	The maximum allowable partial update execution time [onPartialUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html#onPartialUpdate-instance_function) is allowed to take.

## Instance Attribute Details

### var executionTimeAverage as Lang.Float

The average partial update execution time [onPartialUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html#onPartialUpdate-instance_function) took to complete.

### var executionTimeLimit as Lang.Float

The maximum allowable partial update execution time [onPartialUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html#onPartialUpdate-instance_function) is allowed to take.
