---
title: Toybox.System.Stats
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Stats.html
---

## Class: Toybox.System.Stats

## Overview

Represents various statistics available on a device, such as the battery charge and memory use.

## See Also:

- [System.getSystemStats()](../System.md#getSystemStats-instance_function)

## Instance Member Summary

- [**battery**](#battery-var "battery (Var)") as [Lang.Float](../Lang/Float.md)
	The remaining battery life as a percentage.
- [**batteryInDays**](#batteryInDays-var "batteryInDays (Var)") as [Lang.Float](../Lang/Float.md)
	The remaining battery life in days.
- [**charging**](#charging-var "charging (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	Battery charging indicator.
- [**freeMemory**](#freeMemory-var "freeMemory (Var)") as [Lang.Number](../Lang/Number.md)
	The current free memory in bytes.
- [**solarIntensity**](#solarIntensity-var "solarIntensity (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	A [Toybox::Lang::Number](../Lang/Number.md) value from 0-100 that describes the solar sensor's charge efficiency, if available.
- [**totalMemory**](#totalMemory-var "totalMemory (Var)") as [Lang.Number](../Lang/Number.md)
	The total available memory in bytes.
- [**usedMemory**](#usedMemory-var "usedMemory (Var)") as [Lang.Number](../Lang/Number.md)
	The memory used by the application in bytes.

## Instance Attribute Details

### var battery as Lang.Float

The remaining battery life as a percentage.

### var batteryInDays as Lang.Float

The remaining battery life in days.

### var charging as Lang.Boolean

Battery charging indicator. This will be set to `true` if the device is connected to the charging cradle or cable whether or not the device is fully charged.

### var freeMemory as Lang.Number

The current free memory in bytes.

### var solarIntensity as Lang.Number or Null

A [Toybox::Lang::Number](../Lang/Number.md) value from 0-100 that describes the solar sensor's charge efficiency, if available. Will be set to `null` if the device doesn't support solar or a `negative` number when the device is not currently charging.

### var totalMemory as Lang.Number

The total available memory in bytes.

### var usedMemory as Lang.Number

The memory used by the application in bytes.
