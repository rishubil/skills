---
title: Toybox.Sensor.HeartRateData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/HeartRateData.html
---

## Class: Toybox.Sensor.HeartRateData

## Overview

A class to store granular heart rate data.

This class provides granular heart rate data like beat-to-beat intervals. This is typically used in a callback method used by [registerSensorDataListener()](../Sensor.md#registerSensorDataListener-instance_function).

## See Also:

- [Toybox.Sensor.Info](Info.md)
- [Toybox.Sensor.SensorData](SensorData.md)
- [Beat-to-beat interval or "Interbeat interval"](https://en.wikipedia.org/wiki/Interbeat_interval)

## Instance Member Summary

- [**heartBeatIntervals**](#heartBeatIntervals-var "heartBeatIntervals (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >
	The most recent beat-to-beat interval data as an [Array](../Lang/Array.md) of [Number](../Lang/Number.md) objects in milliseconds (ms).

## Instance Attribute Details

### var heartBeatIntervals as Lang.Array<Lang.Number>

The most recent beat-to-beat interval data as an [Array](../Lang/Array.md) of [Number](../Lang/Number.md) objects in milliseconds (ms).
