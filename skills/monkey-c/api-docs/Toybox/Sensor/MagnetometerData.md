---
title: Toybox.Sensor.MagnetometerData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/MagnetometerData.html
---

## Class: Toybox.Sensor.MagnetometerData

## Overview

A class to store magnetometerData sample data.

Each field specified is an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of [Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) values. The values for the x, y, and z axes are in milliGauss (mG) This is typically used in a callback method used by [registerSensorDataListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html#registerSensorDataListener-instance_function)

## See Also:

- [Toybox.Sensor.SensorData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorData.html)

## Instance Member Summary

- [**timestamp**](#timestamp-var "timestamp (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) > or **Null**
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of timestamp values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliseconds.
- [**x**](#x-var "x (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of x axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliGauss.
- [**y**](#y-var "y (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of y axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliGauss.
- [**z**](#z-var "z (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of z axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliGauss.

## Instance Attribute Details

### var timestamp as Lang.Array<Lang.Number> or Null

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of timestamp values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliseconds.

### var x as Lang.Array<Lang.Number>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of x axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliGauss.

### var y as Lang.Array<Lang.Number>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of y axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliGauss.

### var z as Lang.Array<Lang.Number>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of z axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliGauss.
