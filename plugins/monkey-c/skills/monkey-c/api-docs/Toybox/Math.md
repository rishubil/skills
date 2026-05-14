---
title: Toybox.Math
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Math.html
---

## Module: Toybox.Math

## Overview

## Classes Under Namespace

**Classes:** [Filter](Math/Filter.md), [FirFilter](Math/FirFilter.md), [IirFilter](Math/IirFilter.md)

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | E | 2.7182818284590452354 | API Level 1.0.0 | 32-bit floating point representation of E |
| Type | PI | 3.14159265358979323846 | API Level 1.0.0 | 32-bit floating point representation of PI |

## Instance Method Summary

- [**acos**](#acos-instance_function "acos (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get the arc cosine of an angle.
- [**asin**](#asin-instance_function "asin (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get the arc sine of an angle.
- [**atan**](#atan-instance_function "atan (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get the arc tangent of an angle.
- [**atan2**](#atan2-instance_function "atan2 (Instance Function)") (y as [Lang.Numeric](Lang.md#Numeric-named_type), x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get the arc tangent of y/x in radians.
- [**ceil**](#ceil-instance_function "ceil (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Numeric](Lang.md#Numeric-named_type)
	Compute the ceiling of a value.
- [**cos**](#cos-instance_function "cos (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get the cosine of an angle.
- [**floor**](#floor-instance_function "floor (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Numeric](Lang.md#Numeric-named_type)
	Compute the floor of a value.
- [**ln**](#ln-instance_function "ln (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get natural logarithm of a value.
- [**log**](#log-instance_function "log (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type), base as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get logarithm of a value using the specified base.
- [**mean**](#mean-instance_function "mean (Instance Function)") (data as [Lang.Array](Lang/Array.md) < [Lang.Numeric](Lang.md#Numeric-named_type) >) as [Lang.Double](Lang/Double.md)
	Get the arithmetic mean (average) of an array of data.
- [**mode**](#mode-instance_function "mode (Instance Function)") (data as [Lang.Array](Lang/Array.md) < [Lang.Object](Lang/Object.md) >) as [Lang.Object](Lang/Object.md)
	Get the most common value found in an array of data.
- [**pow**](#pow-instance_function "pow (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type), y as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Calculate x to the power of y.
- [**rand**](#rand-instance_function "rand (Instance Function)") () as [Lang.Number](Lang/Number.md)
	Returns a pseudo-random Number.
- [**round**](#round-instance_function "round (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Numeric](Lang.md#Numeric-named_type)
	Round a value.
- [**sin**](#sin-instance_function "sin (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get the sine of an angle.
- [**sqrt**](#sqrt-instance_function "sqrt (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Calculate the square root of a value.
- [**srand**](#srand-instance_function "srand (Instance Function)") (seed as [Lang.Number](Lang/Number.md)) as **Void**
	Seed the random number generator.
- [**stdev**](#stdev-instance_function "stdev (Instance Function)") (data as [Lang.Array](Lang/Array.md) < [Lang.Numeric](Lang.md#Numeric-named_type) >, xbar as [Lang.Double](Lang/Double.md) or **Null**) as [Lang.Double](Lang/Double.md)
	Get the standard deviation of a sample of population data.
- [**tan**](#tan-instance_function "tan (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Get the tangent of an angle.
- [**toDegrees**](#toDegrees-instance_function "toDegrees (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Convert an angle from radians to degrees.
- [**toRadians**](#toRadians-instance_function "toRadians (Instance Function)") (x as [Lang.Numeric](Lang.md#Numeric-named_type)) as [Lang.Decimal](Lang.md#Decimal-named_type)
	Convert an angle from degrees to radians.
- [**variance**](#variance-instance_function "variance (Instance Function)") (data as [Lang.Array](Lang/Array.md) < [Lang.Numeric](Lang.md#Numeric-named_type) >, xbar as [Lang.Numeric](Lang.md#Numeric-named_type) or **Null**) as [Lang.Double](Lang/Double.md)
	Get the sample variance of an array of data.

## Instance Method Details

### acos(x as Lang.Numeric) as Lang.Decimal

### asin(x as Lang.Numeric) as Lang.Decimal

### atan(x as Lang.Numeric) as Lang.Decimal

### atan2(y as Lang.Numeric, x as Lang.Numeric) as Lang.Decimal

### ceil(x as Lang.Numeric) as Lang.Numeric

### cos(x as Lang.Numeric) as Lang.Decimal

### floor(x as Lang.Numeric) as Lang.Numeric

### ln(x as Lang.Numeric) as Lang.Decimal

### log(x as Lang.Numeric, base as Lang.Numeric) as Lang.Decimal

### mean(data as Lang.Array<Lang.Numeric>) as Lang.Double

### mode(data as Lang.Array<Lang.Object>) as Lang.Object

### pow(x as Lang.Numeric, y as Lang.Numeric) as Lang.Decimal

### rand() as Lang.Number

### round(x as Lang.Numeric) as Lang.Numeric

### sin(x as Lang.Numeric) as Lang.Decimal

### sqrt(x as Lang.Numeric) as Lang.Decimal

### srand(seed as Lang.Number) as Void

Note:

srand() does not return any value.
