---
title: Toybox.System.ClockTime
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System/ClockTime.html
---

## Class: Toybox.System.ClockTime

## Overview

Represents the current local time.

ClockTime is a convenient way to get the current time in an easy-to-use format without the need to perform time zone conversions or time-based arithmetic. Values provided by ClockTime may require formatting for proper display within an app.

## See Also:

- [Toybox.Time](../Time.md)
- [Number.format()](../Lang/Number.md#format-instance_function)

## Instance Member Summary

- [**dst**](#dst-var "dst (Var)") as [Lang.Number](../Lang/Number.md)
	The daylight savings time offset.
- [**hour**](#hour-var "hour (Var)") as [Lang.Number](../Lang/Number.md)
	The hour of the day based on a 24-hour clock.
- [**min**](#min-var "min (Var)") as [Lang.Number](../Lang/Number.md)
	The minute of the current hour.
- [**sec**](#sec-var "sec (Var)") as [Lang.Number](../Lang/Number.md)
	The second of the current minute.
- [**timeZoneOffset**](#timeZoneOffset-var "timeZoneOffset (Var)") as [Lang.Number](../Lang/Number.md)
	The time offset from UTC in seconds.

## Instance Attribute Details

### var dst as Lang.Number

The daylight savings time offset.

### var hour as Lang.Number

The hour of the day based on a 24-hour clock.

### var min as Lang.Number

The minute of the current hour.

### var sec as Lang.Number

The second of the current minute.

### var timeZoneOffset as Lang.Number

The time offset from UTC in seconds.
