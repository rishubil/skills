---
title: Toybox.BluetoothLowEnergy.Characteristic
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Characteristic.html
---

## Class: Toybox.BluetoothLowEnergy.Characteristic

## Overview

Encapsulates a characteristic on a service

## Instance Method Summary

- [**getDescriptor**](#getDescriptor-instance_function "getDescriptor (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](Uuid.md)) as [BluetoothLowEnergy.Descriptor](Descriptor.md) or **Null**
	Retrieves the Descriptor with a specified UUID.
- [**getDescriptors**](#getDescriptors-instance_function "getDescriptors (Instance Function)") () as [BluetoothLowEnergy.Iterator](Iterator.md)
	Retrieves an Iterator over the [Descriptors](Descriptor.md) discovered in the Characteristic This will only provide descriptors that have been registered using [registerProfile()](../BluetoothLowEnergy.md#registerProfile-instance_function).
- [**getService**](#getService-instance_function "getService (Instance Function)") () as [BluetoothLowEnergy.Service](Service.md)
	Retrieves the Characteristic's Service Retrieve the Service that this characteristic belongs to.
- [**getUuid**](#getUuid-instance_function "getUuid (Instance Function)") () as [BluetoothLowEnergy.Uuid](Uuid.md)
	Return the UUID of the Characteristic.
- [**requestRead**](#requestRead-instance_function "requestRead (Instance Function)") () as **Void**
	Requests a read operation on the characteristic Once the operation is completed, [onCharacteristicRead()](BleDelegate.md#onCharacteristicRead-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation Support for long reads is not implemented.
- [**requestWrite**](#requestWrite-instance_function "requestWrite (Instance Function)") (value as [Lang.ByteArray](../Lang/ByteArray.md), options as {:writeType as [BluetoothLowEnergy.WriteType](../BluetoothLowEnergy.md#WriteType-module) }) as **Void**
	Requests a write operation Once the operation is completed, [onCharacteristicWrite()](BleDelegate.md#onCharacteristicWrite-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation Support for long writes is not implemented.

## Instance Method Details

### getDescriptor(uuid as BluetoothLowEnergy.Uuid) as BluetoothLowEnergy.Descriptor or Null

Retrieves the Descriptor with a specified UUID

### getDescriptors() as BluetoothLowEnergy.Iterator

Retrieves an Iterator over the [Descriptors](Descriptor.md) discovered in the Characteristic

This will only provide descriptors that have been registered using [registerProfile()](../BluetoothLowEnergy.md#registerProfile-instance_function)

### getService() as BluetoothLowEnergy.Service

Retrieves the Characteristic's Service

Retrieve the Service that this characteristic belongs to

### getUuid() as BluetoothLowEnergy.Uuid

Return the UUID of the Characteristic

### requestRead() as Void

Requests a read operation on the characteristic

Once the operation is completed, [onCharacteristicRead()](BleDelegate.md#onCharacteristicRead-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation

Support for long reads is not implemented.

### requestWrite(value as Lang.ByteArray, options as {:writeType as BluetoothLowEnergy.WriteType }) as Void

Requests a write operation

Once the operation is completed, [onCharacteristicWrite()](BleDelegate.md#onCharacteristicWrite-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation

Support for long writes is not implemented. Requesting a write on a characteristic longer than 20 bytes will cause an [InvalidRequestException](InvalidRequestException.md)
