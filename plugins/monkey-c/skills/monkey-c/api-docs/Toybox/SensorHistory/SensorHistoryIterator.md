---
title: Toybox.SensorHistory.SensorHistoryIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorHistoryIterator.html
---

## Class: Toybox.SensorHistory.SensorHistoryIterator

## Overview

A class containing sensor data for a given period of time.

The SensorHistoryIterator describes a sequence of [SensorSample](SensorSample.md) objects. The iterator is retrieved using the appropriate "get" methods found in [SensorHistory](../SensorHistory.md) at the module level. This class provides the methods needed to retrieve information from each of the SensorSample objects included in the iterator.

## See Also:

- [SensorHistory.getHeartRateHistory()](../SensorHistory.md#getHeartRateHistory-instance_function)
- [Toybox.SensorHistory.SensorSample](SensorSample.md)
- [Toybox.Lang.Method](../Lang/Method.md)

## Instance Method Summary

- [**getMax**](#getMax-instance_function "getMax (Instance Function)") () as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md) or **Null**
	Get the maximum [SensorSample](SensorSample.md) data value contained in this iterator.
- [**getMin**](#getMin-instance_function "getMin (Instance Function)") () as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md) or **Null**
	Get the minimum [SensorSample](SensorSample.md) data value contained in this iterator.
- [**getNewestSampleTime**](#getNewestSampleTime-instance_function "getNewestSampleTime (Instance Function)") () as [Time.Moment](../Time/Moment.md) or **Null**
	Get the [Moment](../Time/Moment.md) of the newest [SensorSample](SensorSample.md) in this iterator.
- [**getOldestSampleTime**](#getOldestSampleTime-instance_function "getOldestSampleTime (Instance Function)") () as [Time.Moment](../Time/Moment.md) or **Null**
	Get the [Moment](../Time/Moment.md) of the oldest [SensorSample](SensorSample.md) in this iterator.
- [**next**](#next-instance_function "next (Instance Function)") () as [SensorHistory.SensorSample](SensorSample.md) or **Null**
	Get the next [SensorSample](SensorSample.md) entry in the iterator.

## Instance Method Details

### getMax() as Lang.Number or Lang.Float or Null

Get the maximum [SensorSample](SensorSample.md) data value contained in this iterator.

### getMin() as Lang.Number or Lang.Float or Null

Get the minimum [SensorSample](SensorSample.md) data value contained in this iterator.

### getNewestSampleTime() as Time.Moment or Null

Get the [Moment](../Time/Moment.md) of the newest [SensorSample](SensorSample.md) in this iterator.

### getOldestSampleTime() as Time.Moment or Null

Get the [Moment](../Time/Moment.md) of the oldest [SensorSample](SensorSample.md) in this iterator.

### next() as SensorHistory.SensorSample or Null

Get the next [SensorSample](SensorSample.md) entry in the iterator.

This must be called to get the initial data from the iterator.
