---
title: Toybox.ActivityMonitor
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor.html
---

## Module: Toybox.ActivityMonitor

## Overview

## Classes Under Namespace

**Classes:** [ActiveMinutes](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/ActiveMinutes.html), [HeartRateIterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/HeartRateIterator.html), [HeartRateSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/HeartRateSample.html), [History](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/History.html), [Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/Info.html)

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | INVALID\_HR\_SAMPLE | 255 | API Level 1.2.2 | Indicates that the given heart rate sample is invalid. |
| Type | MOVE\_BAR\_LEVEL\_MAX | 5 | API Level 1.0.0 | The maximum level of the move bar |
| Type | MOVE\_BAR\_LEVEL\_MIN | 0 | API Level 1.0.0 | The minimum level of the move bar |

## Instance Method Summary

- [**getHeartRateHistory**](#getHeartRateHistory-instance_function "getHeartRateHistory (Instance Function)") (period as [Time.Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html) or [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**, newestFirst as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as [ActivityMonitor.HeartRateIterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/HeartRateIterator.html)
	Get the heart rate history for the given period, up to the last power cycle.
- [**getHistory**](#getHistory-instance_function "getHistory (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [ActivityMonitor.History](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/History.html) >
	Get an Array of ActivityMonitor.History objects.
- [**getInfo**](#getInfo-instance_function "getInfo (Instance Function)") () as [ActivityMonitor.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/Info.html)
	Get the current [ActivityMonitor.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/Info.html).
