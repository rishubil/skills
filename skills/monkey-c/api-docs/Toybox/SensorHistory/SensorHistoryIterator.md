---
title: Toybox.SensorHistory.SensorHistoryIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorHistoryIterator.html
---

## Class: Toybox.SensorHistory.SensorHistoryIterator

## Overview

A class containing sensor data for a given period of time.

The SensorHistoryIterator describes a sequence of [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) objects. The iterator is retrieved using the appropriate "get" methods found in [SensorHistory](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory.html) at the module level. This class provides the methods needed to retrieve information from each of the SensorSample objects included in the iterator.

## See Also:

- [SensorHistory.getHeartRateHistory()](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory.html#getHeartRateHistory-instance_function)
- [Toybox.SensorHistory.SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html)
- [Toybox.Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html)

## Instance Method Summary

- [**getMax**](#getMax-instance_function "getMax (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	Get the maximum [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) data value contained in this iterator.
- [**getMin**](#getMin-instance_function "getMin (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	Get the minimum [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) data value contained in this iterator.
- [**getNewestSampleTime**](#getNewestSampleTime-instance_function "getNewestSampleTime (Instance Function)") () as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) or **Null**
	Get the [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) of the newest [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) in this iterator.
- [**getOldestSampleTime**](#getOldestSampleTime-instance_function "getOldestSampleTime (Instance Function)") () as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) or **Null**
	Get the [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) of the oldest [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) in this iterator.
- [**next**](#next-instance_function "next (Instance Function)") () as [SensorHistory.SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) or **Null**
	Get the next [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) entry in the iterator.

## Instance Method Details

### getMax() as Lang.Number or Lang.Float or Null

Get the maximum [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) data value contained in this iterator.

### getMin() as Lang.Number or Lang.Float or Null

Get the minimum [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) data value contained in this iterator.

### getNewestSampleTime() as Time.Moment or Null

Get the [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) of the newest [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) in this iterator.

### getOldestSampleTime() as Time.Moment or Null

Get the [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) of the oldest [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) in this iterator.

### next() as SensorHistory.SensorSample or Null

Get the next [SensorSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory/SensorSample.html) entry in the iterator.

This must be called to get the initial data from the iterator.
