---
title: Toybox.SensorHistory
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory.html
---

## Module: Toybox.SensorHistory

## Overview

## Classes Under Namespace

**Classes:** [SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md), [SensorSample](SensorHistory/SensorSample.md)

## Constant Summary

### Order

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ORDER\_NEWEST\_FIRST | 0 | API Level 2.1.0 | Request iterator with newest data first |
| ORDER\_OLDEST\_FIRST | 1 | API Level 2.1.0 | Request iterator with oldest data first |

## Instance Method Summary

- [**getBodyBatteryHistory**](#getBodyBatteryHistory-instance_function "getBodyBatteryHistory (Instance Function)") (options as {:period as [Lang.Number](Lang/Number.md) or [Time.Duration](Time/Duration.md) or **Null**,:order as [SensorHistory.Order](SensorHistory.md#Order-module) } or **Null**) as [SensorHistory.SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md)
	Get the body battery history for the given period.
- [**getElevationHistory**](#getElevationHistory-instance_function "getElevationHistory (Instance Function)") (options as {:period as [Lang.Number](Lang/Number.md) or [Time.Duration](Time/Duration.md) or **Null**,:order as [SensorHistory.Order](SensorHistory.md#Order-module) } or **Null**) as [SensorHistory.SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md)
	Get the elevation history for the given period, up to the last power cycle.
- [**getHeartRateHistory**](#getHeartRateHistory-instance_function "getHeartRateHistory (Instance Function)") (options as {:period as [Lang.Number](Lang/Number.md) or [Time.Duration](Time/Duration.md),:order as [SensorHistory.Order](SensorHistory.md#Order-module) or **Null** } or **Null**) as [SensorHistory.SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md)
	Get the heart rate history for the given period, up to the last power cycle.
- [**getOxygenSaturationHistory**](#getOxygenSaturationHistory-instance_function "getOxygenSaturationHistory (Instance Function)") (options as {:period as [Lang.Number](Lang/Number.md) or [Time.Duration](Time/Duration.md) or **Null**,:order as [SensorHistory.Order](SensorHistory.md#Order-module) } or **Null**) as [SensorHistory.SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md)
	Get the oxygen saturation history for the given period This function always returns the most recent sensor history samples.
- [**getPressureHistory**](#getPressureHistory-instance_function "getPressureHistory (Instance Function)") (options as {:period as [Lang.Number](Lang/Number.md) or [Time.Duration](Time/Duration.md) or **Null**,:order as [SensorHistory.Order](SensorHistory.md#Order-module) } or **Null**) as [SensorHistory.SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md)
	Get the pressure history for the given period, up to the last power cycle.
- [**getStressHistory**](#getStressHistory-instance_function "getStressHistory (Instance Function)") (options as {:period as [Lang.Number](Lang/Number.md) or [Time.Duration](Time/Duration.md) or **Null**,:order as [SensorHistory.Order](SensorHistory.md#Order-module) } or **Null**) as [SensorHistory.SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md)
	Get stress history data for the given period This function always returns the most recent sensor history samples.
- [**getTemperatureHistory**](#getTemperatureHistory-instance_function "getTemperatureHistory (Instance Function)") (options as {:period as [Lang.Number](Lang/Number.md) or [Time.Duration](Time/Duration.md) or **Null**,:order as [SensorHistory.Order](SensorHistory.md#Order-module) } or **Null**) as [SensorHistory.SensorHistoryIterator](SensorHistory/SensorHistoryIterator.md)
	Get the temperature history for the given period, up to the last power cycle.
