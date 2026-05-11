---
title: Toybox.Time.Moment
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html
---

## Class: Toybox.Time.Moment

## Overview

## See Also:

- [UTC Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)
- [UNIX Time](https://en.wikipedia.org/wiki/Unix_time)

## Instance Method Summary

- [**add**](#add-instance_function "add (Instance Function)") (duration as [Time.Duration](Duration.md)) as [Time.Moment](Moment.md)
	Add a [Duration](Duration.md) to a Moment.
- [**compare**](#compare-instance_function "compare (Instance Function)") (moment as [Time.Moment](Moment.md)) as [Lang.Number](../Lang/Number.md)
	Determine if a Moment is before or after another Moment.
- [**greaterThan**](#greaterThan-instance_function "greaterThan (Instance Function)") (moment as [Time.Moment](Moment.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determine if a Moment is greater than another Moment.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (seconds as [Lang.Number](../Lang/Number.md)) [Time.Moment](Moment.md)
	Constructor.
- [**lessThan**](#lessThan-instance_function "lessThan (Instance Function)") (moment as [Time.Moment](Moment.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determine if a Moment is less than another Moment.
- [**subtract**](#subtract-instance_function "subtract (Instance Function)") (subtrahend as [Time.Moment](Moment.md) or [Time.Duration](Duration.md)) as [Time.Moment](Moment.md) or [Time.Duration](Duration.md)
	Subtract a [Duration](Duration.md) or [Moment](Moment.md) from a Moment.
- [**value**](#value-instance_function "value (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the UTC value of a Moment.

## Instance Method Details

### add(duration as Time.Duration) as Time.Moment

### compare(moment as Time.Moment) as Lang.Number

### greaterThan(moment as Time.Moment) as Lang.Boolean

### initialize(seconds as Lang.Number) Time.Moment

### lessThan(moment as Time.Moment) as Lang.Boolean

### subtract(subtrahend as Time.Moment or Time.Duration) as Time.Moment or Time.Duration

Note:

Subtracting a Duration from a Moment was not supported until ConnectIQ 3.0.0. If backward compatibility is a concern, it may be best to add a negative Duration instead.
