---
title: Toybox.Lang.Dictionary
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html
---

## Class: Toybox.Lang.Dictionary

## Overview

A Dictionary is a hash table or associative array used to map keys to values.

Both the keys and values can be any Object type, though they do not all need to be of the same type. Objects used as a keys should override the [hashCode()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html#hashCode-instance_function) method. Due to the nature of hash tables, the order of Dictionary elements are not guaranteed to match the insertion order.

## See Also:

- [Hash Table](https://en.wikipedia.org/wiki/Hash_table)

## Instance Method Summary

- [**get**](#get-instance_function "get (Instance Function)") (key as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**
	Retrieve a value from a Dictionary for a given key.
- [**hasKey**](#hasKey-instance_function "hasKey (Instance Function)") (key as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Determine whether a key exists within a Dictionary.
- [**isEmpty**](#isEmpty-instance_function "isEmpty (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Determine whether a Dictionary is empty.
- [**keys**](#keys-instance_function "keys (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) >
	Retrieve the keys in the Dictionary.
- [**put**](#put-instance_function "put (Instance Function)") (key as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html), value as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as **Void**
	Place a value in the Dictionary with a given key.
- [**remove**](#remove-instance_function "remove (Instance Function)") (key as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as **Void**
	Delete an item from a Dictionary.
- [**size**](#size-instance_function "size (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Retrieve the number of elements in a Dictionary.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert a Dictionary to a String.
- [**values**](#values-instance_function "values (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null** >
	Retrieve the values in the Dictionary.

## Instance Method Details

### get(key as Lang.Object) as Lang.Object or Null

Retrieve a value from a Dictionary for a given key.

### hasKey(key as Lang.Object) as Lang.Boolean

Determine whether a key exists within a Dictionary.

### isEmpty() as Lang.Boolean

Determine whether a Dictionary is empty.

### keys() as Lang.Array<Lang.Object>

Retrieve the keys in the Dictionary.

### put(key as Lang.Object, value as Lang.Object or Null) as Void

Place a value in the Dictionary with a given key.

### remove(key as Lang.Object) as Void

Delete an item from a Dictionary.

### size() as Lang.Number

Retrieve the number of elements in a Dictionary.

### toString() as Lang.String

Convert a Dictionary to a String.

Due to the nature of hash tables, the order of Dictionary elements are not guaranteed to match the insertion order when converting to a String.

### values() as Lang.Array<Lang.Object or Null>

Retrieve the values in the Dictionary.
