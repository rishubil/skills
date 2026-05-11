---
title: Toybox.BluetoothLowEnergy.Uuid
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html
---

## Class: Toybox.BluetoothLowEnergy.Uuid

## Overview

Encapsulates a Bluetooth UUID and provides various helper methods for interacting with UUID within the Bluetooth Low Energy Subsystem

## Instance Method Summary

- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Compares the Uuid to another object for equality.
- [**hashCode**](#hashCode-instance_function "hashCode (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Retrieve a hash code of the UUID Optimized for BLE standard.
- [**toByteArray**](#toByteArray-instance_function "toByteArray (Instance Function)") () as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Convert UUID to a Little Endian Byte Array.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert a UUID to a String.

## Instance Method Details

### equals(other as Lang.Object or Null) as Lang.Boolean

Compares the Uuid to another object for equality

### hashCode() as Lang.Number

Retrieve a hash code of the UUID

Optimized for BLE standard

### toByteArray() as Lang.ByteArray

Convert UUID to a Little Endian Byte Array

### toString() as Lang.String

Convert a UUID to a String
