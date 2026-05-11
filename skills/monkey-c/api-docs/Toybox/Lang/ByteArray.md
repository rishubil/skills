---
title: Toybox.Lang.ByteArray
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html
---

## Class: Toybox.Lang.ByteArray

## Overview

## Instance Method Summary

- [**add**](#add-instance_function "add (Instance Function)") (byte as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)) as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Add a byte to the end of a ByteArray.
- [**addAll**](#addAll-instance_function "addAll (Instance Function)") (array as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) or [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)) as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Add a ByteArray or an [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) of bytes to the end of a ByteArray.
- [**decodeNumber**](#decodeNumber-instance_function "decodeNumber (Instance Function)") (format as [Lang.NumberFormat](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#NumberFormat-module), options as {:offset as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:endianness as [Lang.Endian](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Endian-module) }) as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)
	Decodes a portion of the array to a number based on a specified format.
- [**encodeNumber**](#encodeNumber-instance_function "encodeNumber (Instance Function)") (value as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), format as [Lang.NumberFormat](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#NumberFormat-module), options as {:offset as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:endianness as [Lang.Endian](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Endian-module) }) as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Encodes a number into the byte array.
- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Test if an Object instance is equal to another instance of an Object.
- [**hashCode**](#hashCode-instance_function "hashCode (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get a hash code value for a ByteArray.
- [**indexOf**](#indexOf-instance_function "indexOf (Instance Function)") (byte as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the index of a byte within the ByteArray.
- [**remove**](#remove-instance_function "remove (Instance Function)") (byte as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Remove a byte from a ByteArray.
- [**removeAll**](#removeAll-instance_function "removeAll (Instance Function)") (byte as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Remove bytes from a ByteArray.
- [**reverse**](#reverse-instance_function "reverse (Instance Function)") () as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Return a new ByteArray that contains the elements of a source ByteArray in reverse order.
- [**size**](#size-instance_function "size (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the size of a ByteArray.
- [**slice**](#slice-instance_function "slice (Instance Function)") (startIndex as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**, endIndex as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**) as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Get a new ByteArray containing a portion of an existing ByteArray.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert a ByteArray to a String.
