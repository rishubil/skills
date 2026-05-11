---
title: Toybox.Sensor.AccelerometerData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/AccelerometerData.html
---

## Class: Toybox.Sensor.AccelerometerData

## Overview

A class to store accelerometer sample data.

Each field specified is an [Array](../Lang/Array.md) of [Float](../Lang/Float.md) or [Number](../Lang/Number.md) values. The values for the x, y, and z axes are in Milli G units. For reference, 1000 Milli G = 1 G. If not `null`, all fields are of equal size. This is typically used in a callback method used by [registerSensorDataListener()](../Sensor.md#registerSensorDataListener-instance_function)

## See Also:

- [Toybox.Sensor.SensorData](SensorData.md)
- [G-Force Basic Overview](http://www.gforces.net/what-is-g-force-meaning.html)

## Instance Member Summary

- [**pitch**](#pitch-var "pitch (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) > or **Null**
	The [Array](../Lang/Array.md) of pitch values as [Floats](../Lang/Float.md) in degrees.
- [**power**](#power-var "power (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	The [Array](../Lang/Array.md) of vector power values as [Numbers](../Lang/Number.md) in millig-units.
- [**roll**](#roll-var "roll (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) > or **Null**
	The [Array](../Lang/Array.md) of roll values as [Floats](../Lang/Float.md) in degrees.
- [**timestamp**](#timestamp-var "timestamp (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	The [Array](../Lang/Array.md) of timestamp values as [Numbers](../Lang/Number.md) in milliseconds.
- [**x**](#x-var "x (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >
	The [Array](../Lang/Array.md) of x axis values as [Numbers](../Lang/Number.md) in millig-units.
- [**y**](#y-var "y (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >
	The [Array](../Lang/Array.md) of y axis values as [Numbers](../Lang/Number.md) in millig-units.
- [**z**](#z-var "z (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >
	The [Array](../Lang/Array.md) of z axis values as [Numbers](../Lang/Number.md) in millig-units.

## Instance Attribute Details

### var pitch as Lang.Array<Lang.Float> or Null

The [Array](../Lang/Array.md) of pitch values as [Floats](../Lang/Float.md) in degrees. Can be `null`.

Pitch values are calculated with the equation atan2(y, sqrt(x^2 + z^2)).

### var power as Lang.Array<Lang.Number> or Null

The [Array](../Lang/Array.md) of vector power values as [Numbers](../Lang/Number.md) in millig-units. Can be `null`.

### var roll as Lang.Array<Lang.Float> or Null

The [Array](../Lang/Array.md) of roll values as [Floats](../Lang/Float.md) in degrees. Can be `null`.

Roll values are calculated with the equation atan2(-x, z).

### var timestamp as Lang.Array<Lang.Number> or Null

The [Array](../Lang/Array.md) of timestamp values as [Numbers](../Lang/Number.md) in milliseconds. Can be `null`.

### var x as Lang.Array<Lang.Number>

The [Array](../Lang/Array.md) of x axis values as [Numbers](../Lang/Number.md) in millig-units.

### var y as Lang.Array<Lang.Number>

The [Array](../Lang/Array.md) of y axis values as [Numbers](../Lang/Number.md) in millig-units.

### var z as Lang.Array<Lang.Number>

The [Array](../Lang/Array.md) of z axis values as [Numbers](../Lang/Number.md) in millig-units.
