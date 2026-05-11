---
title: Toybox.AntPlus.CalculatedCadence
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/CalculatedCadence.html
---

## Class: Toybox.AntPlus.CalculatedCadence

## Overview

The calculated crank cadence.

Fields may return `null` so you should `null` check values before using them.

## Instance Member Summary

- [**cadence**](#cadence-var "cadence (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Average crank cadence calculated from the sensor data in rounds per minute (rpm).
- [**powerSensorType**](#powerSensorType-var "powerSensorType (Var)") as [AntPlus.BikePowerSensorType](../AntPlus.md#BikePowerSensorType-module) or **Null**
	The [BIKE\_POWER\_SENSOR\_TYPE\_\*](../AntPlus.md#BIKE_POWER_SENSOR_TYPE_CNT-const) value of the bike power sensor.

## Instance Attribute Details

### var cadence as Lang.Number or Null

Average crank cadence calculated from the sensor data in rounds per minute (rpm).

### var powerSensorType as AntPlus.BikePowerSensorType or Null

The [BIKE\_POWER\_SENSOR\_TYPE\_\*](../AntPlus.md#BIKE_POWER_SENSOR_TYPE_CNT-const) value of the bike power sensor.
