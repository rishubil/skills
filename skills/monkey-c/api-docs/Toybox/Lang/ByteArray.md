---
title: Toybox.Lang.ByteArray
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html
---

## Class: Toybox.Lang.ByteArray

## Overview

## Instance Method Summary

- [**add**](#add-instance_function "add (Instance Function)") (byte as [Lang.Number](Number.md) or [Lang.Char](Char.md)) as [Lang.ByteArray](ByteArray.md)
	Add a byte to the end of a ByteArray.
- [**addAll**](#addAll-instance_function "addAll (Instance Function)") (array as [Lang.Array](Array.md) or [Lang.ByteArray](ByteArray.md)) as [Lang.ByteArray](ByteArray.md)
	Add a ByteArray or an [Array](Array.md) of bytes to the end of a ByteArray.
- [**decodeNumber**](#decodeNumber-instance_function "decodeNumber (Instance Function)") (format as [Lang.NumberFormat](../Lang.md#NumberFormat-module), options as {:offset as [Lang.Number](Number.md),:endianness as [Lang.Endian](../Lang.md#Endian-module) }) as [Lang.Numeric](../Lang.md#Numeric-named_type)
	Decodes a portion of the array to a number based on a specified format.
- [**encodeNumber**](#encodeNumber-instance_function "encodeNumber (Instance Function)") (value as [Lang.Numeric](../Lang.md#Numeric-named_type), format as [Lang.NumberFormat](../Lang.md#NumberFormat-module), options as {:offset as [Lang.Number](Number.md),:endianness as [Lang.Endian](../Lang.md#Endian-module) }) as [Lang.ByteArray](ByteArray.md)
	Encodes a number into the byte array.
- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](Object.md) or **Null**) as [Lang.Boolean](Boolean.md)
	Test if an Object instance is equal to another instance of an Object.
- [**hashCode**](#hashCode-instance_function "hashCode (Instance Function)") () as [Lang.Number](Number.md)
	Get a hash code value for a ByteArray.
- [**indexOf**](#indexOf-instance_function "indexOf (Instance Function)") (byte as [Lang.Number](Number.md) or [Lang.Char](Char.md)) as [Lang.Number](Number.md)
	Get the index of a byte within the ByteArray.
- [**remove**](#remove-instance_function "remove (Instance Function)") (byte as [Lang.Number](Number.md) or [Lang.Char](Char.md)) as [Lang.Boolean](Boolean.md)
	Remove a byte from a ByteArray.
- [**removeAll**](#removeAll-instance_function "removeAll (Instance Function)") (byte as [Lang.Number](Number.md) or [Lang.Char](Char.md)) as [Lang.Boolean](Boolean.md)
	Remove bytes from a ByteArray.
- [**reverse**](#reverse-instance_function "reverse (Instance Function)") () as [Lang.ByteArray](ByteArray.md)
	Return a new ByteArray that contains the elements of a source ByteArray in reverse order.
- [**size**](#size-instance_function "size (Instance Function)") () as [Lang.Number](Number.md)
	Get the size of a ByteArray.
- [**slice**](#slice-instance_function "slice (Instance Function)") (startIndex as [Lang.Number](Number.md) or **Null**, endIndex as [Lang.Number](Number.md) or **Null**) as [Lang.ByteArray](ByteArray.md)
	Get a new ByteArray containing a portion of an existing ByteArray.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](String.md)
	Convert a ByteArray to a String.
