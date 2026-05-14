---
title: Toybox.Test
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Test.html
---

## Module: Toybox.Test

## Overview

The Test module provides a testing framework for Monkey C.

The test module provides the tools to implement your own unit test and asserts in your source code. Unit tests take a [Logger](Test/Logger.md) object and allow for different levels of output. Unit tests are annotated with `:test` and ignored if testing is not run. Asserts do not require the `:test` annotation and will be compiled out in release versions or you Connect IQ Content. A test RESULTS section is printed to the console with the tests run, test status, and failure rates.

## See Also:

- [Core Topics - Unit Testing](https://developer.garmin.com/connect-iq/core-topics/unit-testing/)

## Classes Under Namespace

**Classes:** [AssertException](Test/AssertException.md), [Logger](Test/Logger.md)

## Instance Method Summary

- [**assert**](#assert-instance_function "assert (Instance Function)") (test as [Lang.Boolean](Lang/Boolean.md)) as **Void**
	Throws an exception if the test is `false`.
- [**assertEqual**](#assertEqual-instance_function "assertEqual (Instance Function)") (value1 as [Lang.Object](Lang/Object.md), value2 as [Lang.Object](Lang/Object.md) or **Null**) as **Void**
	Throws an exception if value1 and value2 are not equal.
- [**assertEqualMessage**](#assertEqualMessage-instance_function "assertEqualMessage (Instance Function)") (value1 as [Lang.Object](Lang/Object.md), value2 as [Lang.Object](Lang/Object.md) or **Null**, message as [Lang.String](Lang/String.md)) as **Void**
	Throws an exception if value1 and value2 are not equal followed by a [String](Lang/String.md) defined by the developer.
- [**assertMessage**](#assertMessage-instance_function "assertMessage (Instance Function)") (test as [Lang.Boolean](Lang/Boolean.md), message as [Lang.String](Lang/String.md)) as **Void**
	Throws an exception if the test is `false` followed by a [String](Lang/String.md) defined by the developer.
- [**assertNotEqual**](#assertNotEqual-instance_function "assertNotEqual (Instance Function)") (value1 as [Lang.Object](Lang/Object.md), value2 as [Lang.Object](Lang/Object.md) or **Null**) as **Void**
	Throws an exception if value1 and value2 are equal.
- [**assertNotEqualMessage**](#assertNotEqualMessage-instance_function "assertNotEqualMessage (Instance Function)") (value1 as [Lang.Object](Lang/Object.md), value2 as [Lang.Object](Lang/Object.md) or **Null**, message as [Lang.String](Lang/String.md)) as **Void**
	Throws an exception if value1 and value2 are equal followed by a [String](Lang/String.md) defined by the developer.

## Instance Method Details

### assert(test as Lang.Boolean) as Void

Throws an exception if the test is `false`.

### assertEqual(value1 as Lang.Object, value2 as Lang.Object or Null) as Void

Throws an exception if value1 and value2 are not equal.

The objects passed to this function must implement the [Object.equals()](Lang/Object.md#equals-instance_function) method which compares both type and value.

### assertEqualMessage(value1 as Lang.Object, value2 as Lang.Object or Null, message as Lang.String) as Void

Throws an exception if value1 and value2 are not equal followed by a [String](Lang/String.md) defined by the developer.

The objects passed to this function must implement the [Object.equals()](Lang/Object.md#equals-instance_function) method which compares both type and value.

### assertMessage(test as Lang.Boolean, message as Lang.String) as Void

Throws an exception if the test is `false` followed by a [String](Lang/String.md) defined by the developer.

### assertNotEqual(value1 as Lang.Object, value2 as Lang.Object or Null) as Void

Throws an exception if value1 and value2 are equal.

The objects passed to this function must implement the [Object.equals()](Lang/Object.md#equals-instance_function) method which compares both type and value.

### assertNotEqualMessage(value1 as Lang.Object, value2 as Lang.Object or Null, message as Lang.String) as Void

Throws an exception if value1 and value2 are equal followed by a [String](Lang/String.md) defined by the developer.

The objects passed to this function must implement the [Object.equals()](Lang/Object.md#equals-instance_function) method which compares both type and value.
