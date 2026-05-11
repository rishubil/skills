---
title: Toybox.Sensor.GyroscopeData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/GyroscopeData.html
---

## Class: Toybox.Sensor.GyroscopeData

## Overview

A class to store gyroscope sample data.

Each field specified is an [Array](../Lang/Array.md) of [Float](../Lang/Float.md) values. The values for the x, y, and z axes are in deg/sec units. This is typically used in a callback method used by [registerSensorDataListener()](../Sensor.md#registerSensorDataListener-instance_function)

## See Also:

- [Toybox.Sensor.SensorData](SensorData.md)

## Instance Member Summary

- [**timestamp**](#timestamp-var "timestamp (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	The [Array](../Lang/Array.md) of timestamp values as [Numbers](../Lang/Number.md) in milliseconds.
- [**x**](#x-var "x (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) >
	The [Array](../Lang/Array.md) of x axis values as [Float](../Lang/Float.md) in deg/sec.
- [**y**](#y-var "y (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) >
	The [Array](../Lang/Array.md) of y axis values as [Float](../Lang/Float.md) in deg/sec.
- [**z**](#z-var "z (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) >
	The [Array](../Lang/Array.md) of z axis values as [Float](../Lang/Float.md) in deg/sec.

## Instance Attribute Details

### var timestamp as Lang.Array<Lang.Number> or Null

The [Array](../Lang/Array.md) of timestamp values as [Numbers](../Lang/Number.md) in milliseconds.

### var x as Lang.Array<Lang.Float>

The [Array](../Lang/Array.md) of x axis values as [Float](../Lang/Float.md) in deg/sec.

### var y as Lang.Array<Lang.Float>

The [Array](../Lang/Array.md) of y axis values as [Float](../Lang/Float.md) in deg/sec.

### var z as Lang.Array<Lang.Float>

The [Array](../Lang/Array.md) of z axis values as [Float](../Lang/Float.md) in deg/sec.
