---
title: Toybox.BluetoothLowEnergy.Service
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Service.html
---

## Class: Toybox.BluetoothLowEnergy.Service

## Overview

## Instance Method Summary

- [**getCharacteristic**](#getCharacteristic-instance_function "getCharacteristic (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](Uuid.md)) as [BluetoothLowEnergy.Characteristic](Characteristic.md) or **Null**
	Retrieves the Characteristic with a specified UUID.
- [**getCharacteristics**](#getCharacteristics-instance_function "getCharacteristics (Instance Function)") () as [BluetoothLowEnergy.Iterator](Iterator.md)
	Retrieves an Iterator over the Characteristics in a Service This will only provide Characteristics that have been registered using [registerProfile()](../BluetoothLowEnergy.md#registerProfile-instance_function).
- [**getDevice**](#getDevice-instance_function "getDevice (Instance Function)") () as [BluetoothLowEnergy.Device](Device.md)
	Retrieves the Service's Device Retrieve the Device that this service belongs to.
- [**getUuid**](#getUuid-instance_function "getUuid (Instance Function)") () as [BluetoothLowEnergy.Uuid](Uuid.md)
	Returns the UUID of the service.
