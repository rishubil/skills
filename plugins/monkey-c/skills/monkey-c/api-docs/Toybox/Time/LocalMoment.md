---
title: Toybox.Time.LocalMoment
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/LocalMoment.html
---

## Class: Toybox.Time.LocalMoment

## Overview

A LocalMoment is an immutable moment in time.

LocalMoment represents a single point in time at a specific location. It differs from Moment in that it also keeps time zone information in addition to the time.

## Instance Method Summary

- [**add**](#add-instance_function "add (Instance Function)") (addend as [Time.Duration](Duration.md)) as [Time.LocalMoment](LocalMoment.md)
	Add a [Duration](Duration.md) to a LocalMoment.
- [**compare**](#compare-instance_function "compare (Instance Function)") (moment as [Time.LocalMoment](LocalMoment.md)) as [Lang.Number](../Lang/Number.md)
	Determine if a LocalMoment is before or after another LocalMoment This computes a Number representing the difference between the two LocalMoment objects in seconds.
- [**getDaylightSavingsTimeOffset**](#getDaylightSavingsTimeOffset-instance_function "getDaylightSavingsTimeOffset (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the daylight saving time offset from UTC time in seconds.
- [**getOffset**](#getOffset-instance_function "getOffset (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the total time offset from UTC time in seconds.
- [**getTimeZoneOffset**](#getTimeZoneOffset-instance_function "getTimeZoneOffset (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the time zone offset from UTC time in seconds.
- [**greaterThan**](#greaterThan-instance_function "greaterThan (Instance Function)") (moment as [Time.LocalMoment](LocalMoment.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determine if a LocalMoment is greater than another LocalMoment.
- [**isDaylightSavingsTime**](#isDaylightSavingsTime-instance_function "isDaylightSavingsTime (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Get whether the daylight saving time offset is in effect.
- [**lessThan**](#lessThan-instance_function "lessThan (Instance Function)") (moment as [Time.LocalMoment](LocalMoment.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determine if a LocalMoment is less than another LocalMoment.
- [**subtract**](#subtract-instance_function "subtract (Instance Function)") (subtrahend as [Time.Duration](Duration.md) or [Time.LocalMoment](LocalMoment.md)) as [Time.Duration](Duration.md) or [Time.LocalMoment](LocalMoment.md)
	Subtract a [Duration](Duration.md) or [LocalMoment](LocalMoment.md) from a LocalMoment.
- [**toMoment**](#toMoment-instance_function "toMoment (Instance Function)") () as [Time.Moment](Moment.md)
	Get a Moment for this.
- [**value**](#value-instance_function "value (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the UTC value of a LocalMoment.

## Instance Method Details

### add(addend as Time.Duration) as Time.LocalMoment

Add a [Duration](Duration.md) to a LocalMoment.

### compare(moment as Time.LocalMoment) as Lang.Number

Determine if a LocalMoment is before or after another LocalMoment

This computes a Number representing the difference between the two LocalMoment objects in seconds. The [subtract()](LocalMoment.md#subtract-instance_function) method can also be used to get the absolute Duration between two LocalMoment objects.

### getDaylightSavingsTimeOffset() as Lang.Number

Get the daylight saving time offset from UTC time in seconds.

### getOffset() as Lang.Number

Get the total time offset from UTC time in seconds

### getTimeZoneOffset() as Lang.Number

Get the time zone offset from UTC time in seconds.

This is the time zone offset without the daylight saving time offset.

### greaterThan(moment as Time.LocalMoment) as Lang.Boolean

Determine if a LocalMoment is greater than another LocalMoment.

### isDaylightSavingsTime() as Lang.Boolean

Get whether the daylight saving time offset is in effect

### lessThan(moment as Time.LocalMoment) as Lang.Boolean

Determine if a LocalMoment is less than another LocalMoment.

### subtract(subtrahend as Time.Duration or Time.LocalMoment) as Time.Duration or Time.LocalMoment

Subtract a [Duration](Duration.md) or [LocalMoment](LocalMoment.md) from a LocalMoment.

### toMoment() as Time.Moment

Get a Moment for this.

### value() as Lang.Number

Get the UTC value of a LocalMoment.
