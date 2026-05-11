---
title: Toybox.Lang.Array
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html
---

## Class: Toybox.Lang.Array

## Overview

Array objects are fixed size (not a linked list), numerically indexed, single dimensional, and take any Objects (including Arrays) as members. Array keys must be Numbers, but Array values may be any type of Object.

## Instance Method Summary

- [**add**](#add-instance_function "add (Instance Function)") (object as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null** >
	Add an Object to the end of an Array.
- [**addAll**](#addAll-instance_function "addAll (Instance Function)") (array as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null** >) as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null** >
	Add an Array of Objects to the end of an Array.
- [**indexOf**](#indexOf-instance_function "indexOf (Instance Function)") (object as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the index of an Object within the Array.
- [**remove**](#remove-instance_function "remove (Instance Function)") (object as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Remove an Object from an Array.
- [**removeAll**](#removeAll-instance_function "removeAll (Instance Function)") (object as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Remove Objects from an Array.
- [**reverse**](#reverse-instance_function "reverse (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null** >
	Return a new Array that contains the elements of a source Array in reverse order.
- [**size**](#size-instance_function "size (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the size of an Array.
- [**slice**](#slice-instance_function "slice (Instance Function)") (startIndex as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**, endIndex as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**) as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null** >
	Get a new Array containing a portion of an existing Array.
- [**sort**](#sort-instance_function "sort (Instance Function)") (comparator as [Lang.Comparator](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Comparator-named_type) or **Null**) as **Void**
	Sort an Array.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert an Array to a String.

## Instance Method Details

### add(object as Lang.Object or Null) as Lang.Array<Lang.Object or Null>

Add an Object to the end of an Array.

When adding an Object, the Array size is increased by one and the new Object is inserted at the new index.

### addAll(array as Lang.Array<Lang.Object or Null>) as Lang.Array<Lang.Object or Null>

Add an Array of Objects to the end of an Array.

When adding an Array of Objects, the Array is expanded by the size of the provided Array, and all of the new elements are inserted starting at the new index.

### indexOf(object as Lang.Object or Null) as Lang.Number

Get the index of an Object within the Array.

### remove(object as Lang.Object or Null) as Lang.Boolean

Remove an Object from an Array.

If the passed Object is found, the Array size is decreased by one and elements beyond it are shifted to the next lower index. If the Array has multiple matches, the matching Object at the lowest index will be removed but the other matching Objects will not be removed.

### removeAll(object as Lang.Object or Null) as Lang.Boolean

Remove Objects from an Array.

For each instance of the Object that is found, the Array size is decreased by one and elements beyond it are shifted to the next lower index.

### reverse() as Lang.Array<Lang.Object or Null>

Return a new Array that contains the elements of a source Array in reverse order.

### size() as Lang.Number

Get the size of an Array.

### slice(startIndex as Lang.Number or Null, endIndex as Lang.Number or Null) as Lang.Array<Lang.Object or Null>

Get a new Array containing a portion of an existing Array.

### sort(comparator as Lang.Comparator or Null) as Void

Sort an Array

### toString() as Lang.String

Convert an Array to a String.

This does not convert the elements of the Array into Strings, but transforms the entire Array into a String.
