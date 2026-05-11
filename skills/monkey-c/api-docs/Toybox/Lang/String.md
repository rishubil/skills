---
title: Toybox.Lang.String
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html
---

## Class: Toybox.Lang.String

## Overview

## Instance Method Summary

- [**compareTo**](#compareTo-instance_function "compareTo (Instance Function)") (other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Lexicographically compare self to some other string.
- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Test if an Object instance is equal to another instance of an Object.
- [**find**](#find-instance_function "find (Instance Function)") (string as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Determine if the specified String exists in a String.
- [**hashCode**](#hashCode-instance_function "hashCode (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get a hash code value for a String.
- [**length**](#length-instance_function "length (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the number of characters in a String.
- [**substring**](#substring-instance_function "substring (Instance Function)") (startIndex as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**, endIndex as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	Create a new String that contains the contents of the current String from a start position to an end position.
- [**toCharArray**](#toCharArray-instance_function "toCharArray (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html) >
	Convert a String to an Array of Char objects.
- [**toDouble**](#toDouble-instance_function "toDouble (Instance Function)") () as [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or **Null**
	Convert a String to a Double.
- [**toFloat**](#toFloat-instance_function "toFloat (Instance Function)") () as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	Convert a String to a Float.
- [**toLong**](#toLong-instance_function "toLong (Instance Function)") () as [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or **Null**
	Convert a String to a Long.
- [**toLongWithBase**](#toLongWithBase-instance_function "toLongWithBase (Instance Function)") (base as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or **Null**
	Convert a String to a Long using a specified base.
- [**toLower**](#toLower-instance_function "toLower (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert a String to lowercase.
- [**toNumber**](#toNumber-instance_function "toNumber (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Convert a String to a Number.
- [**toNumberWithBase**](#toNumberWithBase-instance_function "toNumberWithBase (Instance Function)") (base as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Convert a String to a Number using a specified base.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert a String to a String.
- [**toUpper**](#toUpper-instance_function "toUpper (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert a String to uppercase.
- [**toUtf8Array**](#toUtf8Array-instance_function "toUtf8Array (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	Convert a String to an Array of Number objects.

## Instance Method Details

### compareTo(other as Lang.Object) as Lang.Number

### equals(other as Lang.Object or Null) as Lang.Boolean

### find(string as Lang.String) as Lang.Number or Null

### hashCode() as Lang.Number

### length() as Lang.Number

### substring(startIndex as Lang.Number or Null, endIndex as Lang.Number or Null) as Lang.String or Null

Note:

Starting with 3.3.2, passing null for `startIndex` sets it to the start of the string and passing null for `endIndex` sets it to the end of the string. Passing in a negative number for either `startIndex` or `endIndex` offsets it from the end of the string.
