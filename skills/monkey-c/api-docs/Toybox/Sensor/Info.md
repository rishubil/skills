---
title: Toybox.Sensor.Info
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/Info.html
---

## Class: Toybox.Sensor.Info

## Overview

The Sensor.Info class contains all of the information provided by enabled sensors.

[Sensor.Info](Info.md) can be retrieved on every call of [onUpdate()](../WatchUi/View.md#onUpdate-instance_function) or it can be obtained on demand. Fields in this class may return `null` so should be checked for `null` values prior to use.

## Instance Member Summary

- [**accel**](#accel-var "accel (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	The accelerometer reading of the x, y, and z axes as an Array of [Number](../Lang/Number.md) values in millig-units.
- [**altitude**](#altitude-var "altitude (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The altitude above mean sea level in meters (m).
- [**cadence**](#cadence-var "cadence (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The cadence in revolutions per minute (rpm).
- [**heading**](#heading-var "heading (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The true north referenced heading in radians.
- [**heartRate**](#heartRate-var "heartRate (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The heart rate in beats per minute (bpm).
- [**mag**](#mag-var "mag (Var)") as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	The magnetometer reading of the x, y, and z axes as an Array of [Number](../Lang/Number.md) values in milliGauss (mG).
- [**oxygenSaturation**](#oxygenSaturation-var "oxygenSaturation (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The current oxygen saturation in percent (%).
- [**power**](#power-var "power (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The power in Watts (W).
- [**pressure**](#pressure-var "pressure (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The barometric pressure in Pascals (Pa).
- [**speed**](#speed-var "speed (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The speed in meters per second (m/s).
- [**temperature**](#temperature-var "temperature (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The temperature in degrees Celsius (C).

## Instance Attribute Details

### var accel as Lang.Array<Lang.Number> or Null

The accelerometer reading of the x, y, and z axes as an Array of [Number](../Lang/Number.md) values in millig-units.

### var altitude as Lang.Float or Null

The altitude above mean sea level in meters (m).

Elevation is derived from the most accurate source: Barometer or GPS in order of descending accuracy. If no GPS is present, then barometer readings will be used.

### var cadence as Lang.Number or Null

The cadence in revolutions per minute (rpm).

Cadence is derived from (in order of priority):

1. Bike sensors (cadence or speed must be enabled)
2. Advanced running dynamics sensors (e.g. heart strap with running dynamics enabled)
3. Foot pod
4. Watch-based cadence calculations

### var heading as Lang.Float or Null

The true north referenced heading in radians.

This provides compass orientation if it is supported by the device.

### var heartRate as Lang.Number or Null

The heart rate in beats per minute (bpm).

### var mag as Lang.Array<Lang.Number> or Null

The magnetometer reading of the x, y, and z axes as an Array of [Number](../Lang/Number.md) values in milliGauss (mG).

### var oxygenSaturation as Lang.Number or Null

The current oxygen saturation in percent (%)

### var power as Lang.Number or Null

The power in Watts (W).

### var pressure as Lang.Float or Null

The barometric pressure in Pascals (Pa).

This returns barometric pressure calibrated to sea level. Since pressure varies dues to several factors, a GPS-based altitude must first be obtained, then the ambient (local) pressure is measured by the pressure sensor before conversion to a calibrated barometric pressure value.

### var speed as Lang.Float or Null

The speed in meters per second (m/s).

### var temperature as Lang.Float or Null

The temperature in degrees Celsius (C).
