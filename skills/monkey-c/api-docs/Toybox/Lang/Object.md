---
title: Toybox.Lang.Object
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html
---

## Class: Toybox.Lang.Object

## Overview

Object is the root object for the Monkey C class hierarchy.

## Instance Method Summary

- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Test if an Object instance is equal to another instance of an Object.
- [**hashCode**](#hashCode-instance_function "hashCode (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get a hash code value for an Object.
- [**method**](#method-instance_function "method (Instance Function)") (methodName as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html)) as [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html)
	Retrieve a callback to a Method.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert an Object to a String.
- [**weak**](#weak-instance_function "weak (Instance Function)") () as [Lang.WeakReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/WeakReference.html)
	Get a WeakReference to an Object.

## Instance Method Details

### equals(other as Lang.Object or Null) as Lang.Boolean

Test if an Object instance is equal to another instance of an Object.

### hashCode() as Lang.Number

Get a hash code value for an Object.

This computes a 32-bit Number that is typically used as an index when placing Objects into a Dictionary. Hash code values have the following characteristics:

- The computed hash code is constant for the lifetime of an Object
- If two Objects are equal, their hash codes will be equal

### method(methodName as Lang.Symbol) as Lang.Method

Retrieve a callback to a Method.

This is typically used when supplying a callback function to another method.

### toString() as Lang.String

Convert an Object to a String.

### weak() as Lang.WeakReference

Get a WeakReference to an Object.

A weak reference is an object that keeps a reference to an object but does not increment the reference count. This means the object reference can be destroyed, so is a case that should be handled.

Note:

Immutable types (Number, Float, Long, Double, Boolean, String) will return their values. Other Object types will return a WeakReference object.
