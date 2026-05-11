---
title: Toybox.Lang.Object
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html
---

## Class: Toybox.Lang.Object

## Overview

Object is the root object for the Monkey C class hierarchy.

## Instance Method Summary

- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](Object.md) or **Null**) as [Lang.Boolean](Boolean.md)
	Test if an Object instance is equal to another instance of an Object.
- [**hashCode**](#hashCode-instance_function "hashCode (Instance Function)") () as [Lang.Number](Number.md)
	Get a hash code value for an Object.
- [**method**](#method-instance_function "method (Instance Function)") (methodName as [Lang.Symbol](Symbol.md)) as [Lang.Method](Method.md)
	Retrieve a callback to a Method.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](String.md)
	Convert an Object to a String.
- [**weak**](#weak-instance_function "weak (Instance Function)") () as [Lang.WeakReference](WeakReference.md)
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
