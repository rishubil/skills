---
title: Toybox.BluetoothLowEnergy.ScanResult
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html
---

## Class: Toybox.BluetoothLowEnergy.ScanResult

## Overview

## Instance Method Summary

- [**equals**](#equals-instance_function "equals (Instance Function)") (other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Compares the ScanResult to another object for equality.
- [**getAppearance**](#getAppearance-instance_function "getAppearance (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Gets the Advertised Appearance of the sensor.
- [**getDeviceName**](#getDeviceName-instance_function "getDeviceName (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	Gets the advertised device name If no device name is advertised this function will return `null`.
- [**getManufacturerSpecificData**](#getManufacturerSpecificData-instance_function "getManufacturerSpecificData (Instance Function)") (manufacturerId as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Gets Manufacturer Specific Data for a given Manufacturer Manufacturer Specific Data is decoded according to the BLE Core Specification V4.0 Volume 3 Part C Section 18.11.
- [**getManufacturerSpecificDataIterator**](#getManufacturerSpecificDataIterator-instance_function "getManufacturerSpecificDataIterator (Instance Function)") () as [BluetoothLowEnergy.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Iterator.html)
	Gets an iterator over all of the Manufacturer Specific Data AD Entries in the advertising packet Manufacturer Specific Data is decoded according to the BLE Core Specification V4.0 Volume 3 Part C Section 18.11.
- [**getRawData**](#getRawData-instance_function "getRawData (Instance Function)") () as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Gets the Raw Data that was retrieved in the advertising packet.
- [**getRssi**](#getRssi-instance_function "getRssi (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Gets the received signal strength indication (RSSI) value of the received advertisement.
- [**getServiceData**](#getServiceData-instance_function "getServiceData (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)) as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Gets Service Data for a specific UUID Service data is decoded according to the BLE Core Specification V4.0 Volume 3 Part C Section 18.10.
- [**getServiceUuids**](#getServiceUuids-instance_function "getServiceUuids (Instance Function)") () as [BluetoothLowEnergy.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Iterator.html)
	Gets service UUIDs advertised by the device If the advertising data contains any service UUID values.
- [**hasAddress**](#hasAddress-instance_function "hasAddress (Instance Function)") (address as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Check that advertised device BLE address matches.
- [**isSameDevice**](#isSameDevice-instance_function "isSameDevice (Instance Function)") (other as [BluetoothLowEnergy.ScanResult](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Determines if another scan result represents the same device as another.
