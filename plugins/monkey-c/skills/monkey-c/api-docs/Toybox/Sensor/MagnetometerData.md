---
title: Toybox.Sensor.MagnetometerData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/MagnetometerData.html
---

## Class: Toybox.Sensor.MagnetometerData

## Overview

A class to store magnetometerData sample data.

Each field specified is an [Array](../Lang/Array.md) of [Number](../Lang/Number.md) values. The values for the x, y, and z axes are in milliGauss (mG) This is typically used in a callback method used by [registerSensorDataListener()](../Sensor.md#registerSensorDataListener-instance_function)

## See Also:

- [Toybox.Sensor.SensorData](SensorData.md)

## Instance Member Summary

- [**timestamp**](#timestamp-var "timestamp (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	The [Array](../Lang/Array.md) of timestamp values as [Numbers](../Lang/Number.md) in milliseconds.
- [**x**](#x-var "x (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >
	The [Array](../Lang/Array.md) of x axis values as [Numbers](../Lang/Number.md) in milliGauss.
- [**y**](#y-var "y (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >
	The [Array](../Lang/Array.md) of y axis values as [Numbers](../Lang/Number.md) in milliGauss.
- [**z**](#z-var "z (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) >
	The [Array](../Lang/Array.md) of z axis values as [Numbers](../Lang/Number.md) in milliGauss.

## Instance Attribute Details

### var timestamp as Lang.Array<Lang.Number> or Null

The [Array](../Lang/Array.md) of timestamp values as [Numbers](../Lang/Number.md) in milliseconds.

### var x as Lang.Array<Lang.Number>

The [Array](../Lang/Array.md) of x axis values as [Numbers](../Lang/Number.md) in milliGauss.

### var y as Lang.Array<Lang.Number>

The [Array](../Lang/Array.md) of y axis values as [Numbers](../Lang/Number.md) in milliGauss.

### var z as Lang.Array<Lang.Number>

The [Array](../Lang/Array.md) of z axis values as [Numbers](../Lang/Number.md) in milliGauss.
