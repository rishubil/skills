---
title: Toybox.BluetoothLowEnergy.Characteristic
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Characteristic.html
---

## Class: Toybox.BluetoothLowEnergy.Characteristic

## Overview

Encapsulates a characteristic on a service

## Instance Method Summary

- [**getDescriptor**](#getDescriptor-instance_function "getDescriptor (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)) as [BluetoothLowEnergy.Descriptor](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Descriptor.html) or **Null**
	Retrieves the Descriptor with a specified UUID.
- [**getDescriptors**](#getDescriptors-instance_function "getDescriptors (Instance Function)") () as [BluetoothLowEnergy.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Iterator.html)
	Retrieves an Iterator over the [Descriptors](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Descriptor.html) discovered in the Characteristic This will only provide descriptors that have been registered using [registerProfile()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy.html#registerProfile-instance_function).
- [**getService**](#getService-instance_function "getService (Instance Function)") () as [BluetoothLowEnergy.Service](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Service.html)
	Retrieves the Characteristic's Service Retrieve the Service that this characteristic belongs to.
- [**getUuid**](#getUuid-instance_function "getUuid (Instance Function)") () as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)
	Return the UUID of the Characteristic.
- [**requestRead**](#requestRead-instance_function "requestRead (Instance Function)") () as **Void**
	Requests a read operation on the characteristic Once the operation is completed, [onCharacteristicRead()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onCharacteristicRead-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) with the status of the operation Support for long reads is not implemented.
- [**requestWrite**](#requestWrite-instance_function "requestWrite (Instance Function)") (value as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html), options as {:writeType as [BluetoothLowEnergy.WriteType](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy.html#WriteType-module) }) as **Void**
	Requests a write operation Once the operation is completed, [onCharacteristicWrite()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onCharacteristicWrite-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) with the status of the operation Support for long writes is not implemented.

## Instance Method Details

### getDescriptor(uuid as BluetoothLowEnergy.Uuid) as BluetoothLowEnergy.Descriptor or Null

Retrieves the Descriptor with a specified UUID

### getDescriptors() as BluetoothLowEnergy.Iterator

Retrieves an Iterator over the [Descriptors](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Descriptor.html) discovered in the Characteristic

This will only provide descriptors that have been registered using [registerProfile()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy.html#registerProfile-instance_function)

### getService() as BluetoothLowEnergy.Service

Retrieves the Characteristic's Service

Retrieve the Service that this characteristic belongs to

### getUuid() as BluetoothLowEnergy.Uuid

Return the UUID of the Characteristic

### requestRead() as Void

Requests a read operation on the characteristic

Once the operation is completed, [onCharacteristicRead()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onCharacteristicRead-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) with the status of the operation

Support for long reads is not implemented.

### requestWrite(value as Lang.ByteArray, options as {:writeType as BluetoothLowEnergy.WriteType }) as Void

Requests a write operation

Once the operation is completed, [onCharacteristicWrite()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onCharacteristicWrite-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) with the status of the operation

Support for long writes is not implemented. Requesting a write on a characteristic longer than 20 bytes will cause an [InvalidRequestException](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/InvalidRequestException.html)
