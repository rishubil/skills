---
title: Toybox.Sensor.AccelerometerData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/AccelerometerData.html
---

## Class: Toybox.Sensor.AccelerometerData

## Overview

A class to store accelerometer sample data.

Each field specified is an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) values. The values for the x, y, and z axes are in Milli G units. For reference, 1000 Milli G = 1 G. If not `null`, all fields are of equal size. This is typically used in a callback method used by [registerSensorDataListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html#registerSensorDataListener-instance_function)

## See Also:

- [Toybox.Sensor.SensorData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorData.html)
- [G-Force Basic Overview](http://www.gforces.net/what-is-g-force-meaning.html)

## Instance Member Summary

- [**pitch**](#pitch-var "pitch (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) > or **Null**
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of pitch values as [Floats](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in degrees.
- [**power**](#power-var "power (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) > or **Null**
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of vector power values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units.
- [**roll**](#roll-var "roll (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) > or **Null**
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of roll values as [Floats](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in degrees.
- [**timestamp**](#timestamp-var "timestamp (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) > or **Null**
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of timestamp values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliseconds.
- [**x**](#x-var "x (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of x axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units.
- [**y**](#y-var "y (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of y axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units.
- [**z**](#z-var "z (Var)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of z axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units.

## Instance Attribute Details

### var pitch as Lang.Array<Lang.Float> or Null

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of pitch values as [Floats](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in degrees. Can be `null`.

Pitch values are calculated with the equation atan2(y, sqrt(x^2 + z^2)).

### var power as Lang.Array<Lang.Number> or Null

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of vector power values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units. Can be `null`.

### var roll as Lang.Array<Lang.Float> or Null

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of roll values as [Floats](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) in degrees. Can be `null`.

Roll values are calculated with the equation atan2(-x, z).

### var timestamp as Lang.Array<Lang.Number> or Null

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of timestamp values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in milliseconds. Can be `null`.

### var x as Lang.Array<Lang.Number>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of x axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units.

### var y as Lang.Array<Lang.Number>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of y axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units.

### var z as Lang.Array<Lang.Number>

The [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of z axis values as [Numbers](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) in millig-units.
