---
title: Toybox.ActivityMonitor
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor.html
---

## Module: Toybox.ActivityMonitor

## Overview

## Classes Under Namespace

**Classes:** [ActiveMinutes](ActivityMonitor/ActiveMinutes.md), [HeartRateIterator](ActivityMonitor/HeartRateIterator.md), [HeartRateSample](ActivityMonitor/HeartRateSample.md), [History](ActivityMonitor/History.md), [Info](ActivityMonitor/Info.md)

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | INVALID\_HR\_SAMPLE | 255 | API Level 1.2.2 | Indicates that the given heart rate sample is invalid. |
| Type | MOVE\_BAR\_LEVEL\_MAX | 5 | API Level 1.0.0 | The maximum level of the move bar |
| Type | MOVE\_BAR\_LEVEL\_MIN | 0 | API Level 1.0.0 | The minimum level of the move bar |

## Instance Method Summary

- [**getHeartRateHistory**](#getHeartRateHistory-instance_function "getHeartRateHistory (Instance Function)") (period as [Time.Duration](Time/Duration.md) or [Lang.Number](Lang/Number.md) or **Null**, newestFirst as [Lang.Boolean](Lang/Boolean.md)) as [ActivityMonitor.HeartRateIterator](ActivityMonitor/HeartRateIterator.md)
	Get the heart rate history for the given period, up to the last power cycle.
- [**getHistory**](#getHistory-instance_function "getHistory (Instance Function)") () as [Lang.Array](Lang/Array.md) < [ActivityMonitor.History](ActivityMonitor/History.md) >
	Get an Array of ActivityMonitor.History objects.
- [**getInfo**](#getInfo-instance_function "getInfo (Instance Function)") () as [ActivityMonitor.Info](ActivityMonitor/Info.md)
	Get the current [ActivityMonitor.Info](ActivityMonitor/Info.md).
