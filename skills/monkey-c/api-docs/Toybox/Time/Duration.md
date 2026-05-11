---
title: Toybox.Time.Duration
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html
---

## Class: Toybox.Time.Duration

## Overview

A Duration is an immutable period of time.

Duration objects are closely related to [Moment](Moment.md) objects, and are frequently used together for time calculations. While a [Moment](Moment.md) represents a single point in time, a Duration represents a span of time such as seven days.

Duration objects are stored as a the number of seconds that compose the span of time the Duration represents.

## Instance Method Summary

- [**add**](#add-instance_function "add (Instance Function)") (time as [Time.Moment](Moment.md) or [Time.Duration](Duration.md)) as [Time.Moment](Moment.md) or [Time.Duration](Duration.md)
	Add a [Moment](Moment.md) or another Duration to a Duration.
- [**compare**](#compare-instance_function "compare (Instance Function)") (duration as [Time.Duration](Duration.md)) as [Lang.Number](../Lang/Number.md)
	Determine if a Duration is shorter or longer than another Duration.
- [**divide**](#divide-instance_function "divide (Instance Function)") (value as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md)) as [Time.Duration](Duration.md)
	Divide a Duration by a value.
- [**greaterThan**](#greaterThan-instance_function "greaterThan (Instance Function)") (duration as [Time.Duration](Duration.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determine if a Duration is longer than another Duration.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (value as [Lang.Number](../Lang/Number.md)) [Time.Duration](Duration.md)
	Constructor.
- [**lessThan**](#lessThan-instance_function "lessThan (Instance Function)") (duration as [Time.Duration](Duration.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determine if a Duration is shorter than another Duration.
- [**multiply**](#multiply-instance_function "multiply (Instance Function)") (value as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md)) as [Time.Duration](Duration.md)
	Multiply a Duration by a value.
- [**subtract**](#subtract-instance_function "subtract (Instance Function)") (duration as [Time.Duration](Duration.md)) as [Time.Duration](Duration.md)
	Get the absolute difference between two Duration objects.
- [**value**](#value-instance_function "value (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the value of a Duration.

## Instance Method Details

### add(time as Time.Moment or Time.Duration) as Time.Moment or Time.Duration

Add a [Moment](Moment.md) or another Duration to a Duration.

When adding a Moment to a Duration, this method functions the same as the [Moment.add()](Moment.md#add-instance_function) method.

### compare(duration as Time.Duration) as Lang.Number

Determine if a Duration is shorter or longer than another Duration.

This computes a Number representing the difference between the two Duration objects in seconds. The [subtract()](Duration.md#subtract-instance_function) method can also be used to get the absolute difference between two Duration objects.

### divide(value as Lang.Number or Lang.Float) as Time.Duration

Divide a Duration by a value.

### greaterThan(duration as Time.Duration) as Lang.Boolean

Determine if a Duration is longer than another Duration.

### initialize(value as Lang.Number) Time.Duration

Constructor

### lessThan(duration as Time.Duration) as Lang.Boolean

Determine if a Duration is shorter than another Duration.

### multiply(value as Lang.Number or Lang.Float) as Time.Duration

Multiply a Duration by a value.

### subtract(duration as Time.Duration) as Time.Duration

Get the absolute difference between two Duration objects.

The computed Duration is always a positive value. The [compare()](Duration.md#compare-instance_function) method can also be used to get the difference between two Duration objects.

### value() as Lang.Number

Get the value of a Duration.
