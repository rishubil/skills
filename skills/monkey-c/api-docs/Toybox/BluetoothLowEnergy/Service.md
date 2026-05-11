---
title: Toybox.BluetoothLowEnergy.Service
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Service.html
---

## Class: Toybox.BluetoothLowEnergy.Service

## Overview

## Instance Method Summary

- [**getCharacteristic**](#getCharacteristic-instance_function "getCharacteristic (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)) as [BluetoothLowEnergy.Characteristic](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Characteristic.html) or **Null**
	Retrieves the Characteristic with a specified UUID.
- [**getCharacteristics**](#getCharacteristics-instance_function "getCharacteristics (Instance Function)") () as [BluetoothLowEnergy.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Iterator.html)
	Retrieves an Iterator over the Characteristics in a Service This will only provide Characteristics that have been registered using [registerProfile()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy.html#registerProfile-instance_function).
- [**getDevice**](#getDevice-instance_function "getDevice (Instance Function)") () as [BluetoothLowEnergy.Device](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Device.html)
	Retrieves the Service's Device Retrieve the Device that this service belongs to.
- [**getUuid**](#getUuid-instance_function "getUuid (Instance Function)") () as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)
	Returns the UUID of the service.
