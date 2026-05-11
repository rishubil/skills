---
title: Toybox.AntPlus.CalculatedPower
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/CalculatedPower.html
---

## Class: Toybox.AntPlus.CalculatedPower

## Overview

Represents the calculated power.

Fields may return `null` so you should `null` check values before using them.

## Instance Member Summary

- [**power**](#power-var "power (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The average power calculated from the sensor data in watts (W).
- [**powerSensorType**](#powerSensorType-var "powerSensorType (Var)") as [AntPlus.BikePowerSensorType](../AntPlus.md#BikePowerSensorType-module) or **Null**
	The [BIKE\_POWER\_SENSOR\_TYPE\_\*](../AntPlus.md#BIKE_POWER_SENSOR_TYPE_CNT-const) value of the bike power sensor.

## Instance Attribute Details

### var power as Lang.Float or Null

The average power calculated from the sensor data in watts (W).

### var powerSensorType as AntPlus.BikePowerSensorType or Null

The [BIKE\_POWER\_SENSOR\_TYPE\_\*](../AntPlus.md#BIKE_POWER_SENSOR_TYPE_CNT-const) value of the bike power sensor.
