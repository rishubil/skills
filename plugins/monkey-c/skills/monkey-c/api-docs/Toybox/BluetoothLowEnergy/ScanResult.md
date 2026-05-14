---
title: Toybox.BluetoothLowEnergy.ScanResult
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html
---

## Class: Toybox.BluetoothLowEnergy.ScanResult

## Overview

## Instance Method Summary

- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](../Lang/Object.md) or **Null**) as [Lang.Boolean](../Lang/Boolean.md)
	Compares the ScanResult to another object for equality.
- [**getAppearance**](#getAppearance-instance_function "getAppearance (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Gets the Advertised Appearance of the sensor.
- [**getDeviceName**](#getDeviceName-instance_function "getDeviceName (Instance Function)") () as [Lang.String](../Lang/String.md) or **Null**
	Gets the advertised device name If no device name is advertised this function will return `null`.
- [**getManufacturerSpecificData**](#getManufacturerSpecificData-instance_function "getManufacturerSpecificData (Instance Function)") (manufacturerId as [Lang.Number](../Lang/Number.md)) as [Lang.ByteArray](../Lang/ByteArray.md)
	Gets Manufacturer Specific Data for a given Manufacturer Manufacturer Specific Data is decoded according to the BLE Core Specification V4.0 Volume 3 Part C Section 18.11.
- [**getManufacturerSpecificDataIterator**](#getManufacturerSpecificDataIterator-instance_function "getManufacturerSpecificDataIterator (Instance Function)") () as [BluetoothLowEnergy.Iterator](Iterator.md)
	Gets an iterator over all of the Manufacturer Specific Data AD Entries in the advertising packet Manufacturer Specific Data is decoded according to the BLE Core Specification V4.0 Volume 3 Part C Section 18.11.
- [**getRawData**](#getRawData-instance_function "getRawData (Instance Function)") () as [Lang.ByteArray](../Lang/ByteArray.md)
	Gets the Raw Data that was retrieved in the advertising packet.
- [**getRssi**](#getRssi-instance_function "getRssi (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Gets the received signal strength indication (RSSI) value of the received advertisement.
- [**getServiceData**](#getServiceData-instance_function "getServiceData (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](Uuid.md)) as [Lang.ByteArray](../Lang/ByteArray.md)
	Gets Service Data for a specific UUID Service data is decoded according to the BLE Core Specification V4.0 Volume 3 Part C Section 18.10.
- [**getServiceUuids**](#getServiceUuids-instance_function "getServiceUuids (Instance Function)") () as [BluetoothLowEnergy.Iterator](Iterator.md)
	Gets service UUIDs advertised by the device If the advertising data contains any service UUID values.
- [**hasAddress**](#hasAddress-instance_function "hasAddress (Instance Function)") (address as [Lang.ByteArray](../Lang/ByteArray.md) or [Lang.String](../Lang/String.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Check that advertised device BLE address matches.
- [**isSameDevice**](#isSameDevice-instance_function "isSameDevice (Instance Function)") (other as [BluetoothLowEnergy.ScanResult](ScanResult.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determines if another scan result represents the same device as another.
