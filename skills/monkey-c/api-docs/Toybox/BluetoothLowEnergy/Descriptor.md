---
title: Toybox.BluetoothLowEnergy.Descriptor
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Descriptor.html
---

## Class: Toybox.BluetoothLowEnergy.Descriptor

## Overview

Encapsulates a Descriptor from on a Characteristic

## Instance Method Summary

- [**getCharacteristic**](#getCharacteristic-instance_function "getCharacteristic (Instance Function)") () as [BluetoothLowEnergy.Characteristic](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Characteristic.html)
	Retrieves the Descriptors Characteristic Retrieve the Characteristic that this descriptor belongs to.
- [**getUuid**](#getUuid-instance_function "getUuid (Instance Function)") () as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)
	Returns the UUID of the Descriptor.
- [**requestRead**](#requestRead-instance_function "requestRead (Instance Function)") () as **Void**
	Requests a read operation on the descriptor Once the operation is completed, [onDescriptorRead()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onDescriptorRead-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) with the status of the operation.
- [**requestWrite**](#requestWrite-instance_function "requestWrite (Instance Function)") (value as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)) as **Void**
	Requests a write operation Writes the locally stored value to the remote descriptor.

## Instance Method Details

### getCharacteristic() as BluetoothLowEnergy.Characteristic

Retrieves the Descriptors Characteristic

Retrieve the Characteristic that this descriptor belongs to

### getUuid() as BluetoothLowEnergy.Uuid

Returns the UUID of the Descriptor

### requestRead() as Void

Requests a read operation on the descriptor

Once the operation is completed, [onDescriptorRead()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onDescriptorRead-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) with the status of the operation

### requestWrite(value as Lang.ByteArray) as Void

Requests a write operation

Writes the locally stored value to the remote descriptor.

Once the operation is completed, [onDescriptorWrite()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onDescriptorWrite-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) with the status of the operation

Support for long writes is not implemented. Requesting a write on a characteristic longer than 20 bytes will cause an [InvalidRequestException](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/InvalidRequestException.html)
