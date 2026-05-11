---
title: Toybox.Sensor.HeartRateData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/HeartRateData.html
---

## Class: Toybox.Sensor.HeartRateData

## Overview

A class to store granular heart rate data.

This class provides granular heart rate data like beat-to-beat intervals. This is typically used in a callback method used by [registerSensorDataListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html#registerSensorDataListener-instance_function).

## See Also:

- [Toybox.Sensor.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/Info.html)
- [Toybox.Sensor.SensorData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorData.html)
- [Beat-to-beat interval or "Interbeat interval"](https://en.wikipedia.org/wiki/Interbeat_interval)

## Instance Member Summary

- [**heartBeatIntervals**](#heartBeatIntervals-var "heartBeatIntervals (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	The most recent beat-to-beat interval data as an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of [Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) objects in milliseconds (ms).

## Instance Attribute Details

### var heartBeatIntervals as Lang.Array<Lang.Number>

The most recent beat-to-beat interval data as an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of [Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) objects in milliseconds (ms).
