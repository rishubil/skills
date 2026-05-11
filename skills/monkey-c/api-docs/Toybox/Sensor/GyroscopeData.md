---
title: Toybox.Sensor.GyroscopeData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/GyroscopeData.html
---

## Class: Toybox.Sensor.GyroscopeData

## Overview

A class to store gyroscope sample data.

Each field specified is an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) values. The values for the x, y, and z axes are in deg/sec units. This is typically used in a callback method used by [registerSensorDataListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html#registerSensorDataListener-instance_function)

## See Also:

- [Toybox.Sensor.SensorData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorData.html)

## Instance Member Summary

- [**timestamp**](#timestamp-var "timestamp (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) > or **Null**
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of timestamp values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliseconds.
- [**x**](#x-var "x (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of x axis values as [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in deg/sec.
- [**y**](#y-var "y (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of y axis values as [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in deg/sec.
- [**z**](#z-var "z (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of z axis values as [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in deg/sec.

## Instance Attribute Details

### var timestamp as Lang.Array<Lang.Number> or Null

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of timestamp values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliseconds.

### var x as Lang.Array<Lang.Float>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of x axis values as [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in deg/sec.

### var y as Lang.Array<Lang.Float>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of y axis values as [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in deg/sec.

### var z as Lang.Array<Lang.Float>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of z axis values as [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in deg/sec.
