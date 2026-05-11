---
title: Toybox.BluetoothLowEnergy.Descriptor
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Descriptor.html
---

## Class: Toybox.BluetoothLowEnergy.Descriptor

## Overview

Encapsulates a Descriptor from on a Characteristic

## Instance Method Summary

- [**getCharacteristic**](#getCharacteristic-instance_function "getCharacteristic (Instance Function)") () as [BluetoothLowEnergy.Characteristic](Characteristic.md)
	Retrieves the Descriptors Characteristic Retrieve the Characteristic that this descriptor belongs to.
- [**getUuid**](#getUuid-instance_function "getUuid (Instance Function)") () as [BluetoothLowEnergy.Uuid](Uuid.md)
	Returns the UUID of the Descriptor.
- [**requestRead**](#requestRead-instance_function "requestRead (Instance Function)") () as **Void**
	Requests a read operation on the descriptor Once the operation is completed, [onDescriptorRead()](BleDelegate.md#onDescriptorRead-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation.
- [**requestWrite**](#requestWrite-instance_function "requestWrite (Instance Function)") (value as [Lang.ByteArray](../Lang/ByteArray.md)) as **Void**
	Requests a write operation Writes the locally stored value to the remote descriptor.

## Instance Method Details

### getCharacteristic() as BluetoothLowEnergy.Characteristic

Retrieves the Descriptors Characteristic

Retrieve the Characteristic that this descriptor belongs to

### getUuid() as BluetoothLowEnergy.Uuid

Returns the UUID of the Descriptor

### requestRead() as Void

Requests a read operation on the descriptor

Once the operation is completed, [onDescriptorRead()](BleDelegate.md#onDescriptorRead-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation

### requestWrite(value as Lang.ByteArray) as Void

Requests a write operation

Writes the locally stored value to the remote descriptor.

Once the operation is completed, [onDescriptorWrite()](BleDelegate.md#onDescriptorWrite-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation

Support for long writes is not implemented. Requesting a write on a characteristic longer than 20 bytes will cause an [InvalidRequestException](InvalidRequestException.md)
