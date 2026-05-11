---
title: Toybox.AntPlus.BatteryStatus
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BatteryStatus.html
---

## Class: Toybox.AntPlus.BatteryStatus

## Overview

A class containing information from the Battery Status ANT+ common page.

Fields may return `null` so you should `null` check values before using them.

## See Also:

- [ANT Downloads & Resources (ANT+ Common Pages)](https://www.thisisant.com/resources/common-data-pages/)

## Instance Member Summary

- [**batteryStatus**](#batteryStatus-var "batteryStatus (Var)") as [AntPlus.BatteryStatusValue](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html#BatteryStatusValue-module) or **Null**
	The [BATT\_STATUS\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html#BATT_STATUS_CNT-const) value of the battery.
- [**batteryVoltage**](#batteryVoltage-var "batteryVoltage (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The voltage, -1 is invalid.
- [**operatingTime**](#operatingTime-var "operatingTime (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The operating time in seconds.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.

## Instance Attribute Details

### var batteryStatus as AntPlus.BatteryStatusValue or Null

The [BATT\_STATUS\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html#BATT_STATUS_CNT-const) value of the battery.

### var batteryVoltage as Lang.Float or Null

The voltage, -1 is invalid

### var operatingTime as Lang.Number or Null

The operating time in seconds.

## Instance Method Details

### initialize()

Constructor
