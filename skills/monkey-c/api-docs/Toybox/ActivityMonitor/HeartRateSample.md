---
title: Toybox.ActivityMonitor.HeartRateSample
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/HeartRateSample.html
---

## Class: Toybox.ActivityMonitor.HeartRateSample

## Overview

A class containing heart rate data at a given time.

## Instance Member Summary

- [**heartRate**](#heartRate-var "heartRate (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Heart rate in beats per minute (bpm).
- [**when**](#when-var "when (Var)") as [Time.Moment](../Time/Moment.md) or **Null**
	The time of the heart rate sample.

## Instance Attribute Details

### var heartRate as Lang.Number or Null

Heart rate in beats per minute (bpm).

Before using heart rate information, check for [INVALID\_HR\_SAMPLE](../ActivityMonitor.md#INVALID_HR_SAMPLE-const) to be sure data is available.

### var when as Time.Moment or Null

The time of the heart rate sample
