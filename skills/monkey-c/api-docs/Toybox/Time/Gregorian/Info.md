---
title: Toybox.Time.Gregorian.Info
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian/Info.html
---

## Class: Toybox.Time.Gregorian.Info

## Overview

The Gregorian.Info class contains all of the necessary information to represent a Gregorian date.

The types of some returned values depend on the Time.FORMAT\_\* value specified when calling [info()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian.html#info-instance_function) or [utcInfo()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian.html#utcInfo-instance_function).

## Instance Member Summary

- [**day**](#day-var "day (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The date, indicating the day of the month.
- [**day\_of\_week**](#day_of_week-var "day_of_week (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	The day of the week (e.g.
- [**hour**](#hour-var "hour (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The hour of the day based on a 24-hour clock.
- [**min**](#min-var "min (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The minutes within an hour.
- [**month**](#month-var "month (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	The month of the year (e.g.
- [**sec**](#sec-var "sec (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The seconds within a minute.
- [**year**](#year-var "year (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The year.

## Instance Attribute Details

### var day as Lang.Number

The date, indicating the day of the month.

### var day\_of\_week as Lang.Number or Lang.String

The day of the week (e.g. Monday, Tuesday, Wednesday, etc,).

### var hour as Lang.Number

The hour of the day based on a 24-hour clock.

### var min as Lang.Number

The minutes within an hour.

### var month as Lang.Number or Lang.String

The month of the year (e.g. January, February, March, etc.).

### var sec as Lang.Number

The seconds within a minute.

### var year as Lang.Number

The year.
