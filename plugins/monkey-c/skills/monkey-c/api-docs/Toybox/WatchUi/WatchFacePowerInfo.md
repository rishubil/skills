---
title: Toybox.WatchUi.WatchFacePowerInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFacePowerInfo.html
---

## Class: Toybox.WatchUi.WatchFacePowerInfo

## Overview

Power information provided when the power budget is exceeded during a call to [onPartialUpdate()](WatchFace.md#onPartialUpdate-instance_function).

This is automatically passed to the [onPowerBudgetExceeded()](WatchFaceDelegate.md#onPowerBudgetExceeded-instance_function) method when it is invoked.

## See Also:

- [Toybox.WatchUi.WatchFaceDelegate](WatchFaceDelegate.md)

## Instance Member Summary

- [**executionTimeAverage**](#executionTimeAverage-var "executionTimeAverage (Var)") as [Lang.Float](../Lang/Float.md)
	The average partial update execution time [onPartialUpdate()](WatchFace.md#onPartialUpdate-instance_function) took to complete.
- [**executionTimeLimit**](#executionTimeLimit-var "executionTimeLimit (Var)") as [Lang.Float](../Lang/Float.md)
	The maximum allowable partial update execution time [onPartialUpdate()](WatchFace.md#onPartialUpdate-instance_function) is allowed to take.

## Instance Attribute Details

### var executionTimeAverage as Lang.Float

The average partial update execution time [onPartialUpdate()](WatchFace.md#onPartialUpdate-instance_function) took to complete.

### var executionTimeLimit as Lang.Float

The maximum allowable partial update execution time [onPartialUpdate()](WatchFace.md#onPartialUpdate-instance_function) is allowed to take.
