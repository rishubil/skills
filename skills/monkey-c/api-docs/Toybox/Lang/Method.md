---
title: Toybox.Lang.Method
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html
---

## Class: Toybox.Lang.Method

## Overview

Method is a class that represents a callback, or a function that can be used as an argument to another function. You can create one using the [method()](Object.md#method-instance_function) call, and invoke the Method using the [invoke()](Method.md#invoke-instance_function) method.

## See Also:

- [Toybox.Lang.Object](Object.md)
- [Toybox.Timer](../Timer.md)
- [Toybox.SensorHistory](../SensorHistory.md)

## Instance Method Summary

- [**hashCode**](#hashCode-instance_function "hashCode (Instance Function)") () as [Lang.Number](Number.md)
	Get a hash code value for a Method.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (aClass, aMethod as [Lang.Symbol](Symbol.md))
	Method Constructor.
- [**invoke**](#invoke-instance_function "invoke (Instance Function)") (parameters...) [Lang.Object](Object.md)
	Invoke a Method.

## Instance Method Details

### hashCode() as Lang.Number

Get a hash code value for a Method. This computes a 32-bit Number that is typically used as an index when placing Objects into a Dictionary. Hash code values have the following characteristics:

- The computed hash code is constant for the lifetime of an Object
- If two Objects are equal, their hash codes will be equal

### initialize(aClass, aMethod as Lang.Symbol)

Method Constructor.

### invoke(parameters...) Lang.Object

Invoke a Method.
