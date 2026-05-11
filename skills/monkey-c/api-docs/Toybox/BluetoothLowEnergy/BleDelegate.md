---
title: Toybox.BluetoothLowEnergy.BleDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html
---

## Class: Toybox.BluetoothLowEnergy.BleDelegate

## Overview

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onCharacteristicChanged**](#onCharacteristicChanged-instance_function "onCharacteristicChanged (Instance Function)") (characteristic as [BluetoothLowEnergy.Characteristic](Characteristic.md), value as [Lang.ByteArray](../Lang/ByteArray.md)) as **Void**
	After enabling notifications or indications on a characteristic by enabling the appropriate bit of the CCCD of the characteristic this function will be called after every change to the characteristic.
- [**onCharacteristicRead**](#onCharacteristicRead-instance_function "onCharacteristicRead (Instance Function)") (characteristic as [BluetoothLowEnergy.Characteristic](Characteristic.md), status as [BluetoothLowEnergy.Status](../BluetoothLowEnergy.md#Status-module), value as [Lang.ByteArray](../Lang/ByteArray.md)) as **Void**
	After requesting a read operation on a Characteristic with [requestRead()](Characteristic.md#requestRead-instance_function), this function will be called when the operation is completed.
- [**onCharacteristicWrite**](#onCharacteristicWrite-instance_function "onCharacteristicWrite (Instance Function)") (characteristic as [BluetoothLowEnergy.Characteristic](Characteristic.md), status as [BluetoothLowEnergy.Status](../BluetoothLowEnergy.md#Status-module)) as **Void**
	After requesting a write operation on a Characteristic with [requestWrite()](Characteristic.md#requestWrite-instance_function), this function will be called when the operation is completed.
- [**onConnectedStateChanged**](#onConnectedStateChanged-instance_function "onConnectedStateChanged (Instance Function)") (device as [BluetoothLowEnergy.Device](Device.md), state as [BluetoothLowEnergy.ConnectionState](../BluetoothLowEnergy.md#ConnectionState-module)) as **Void**
	After pairing a device this will be called after the connection is made.
- [**onDescriptorRead**](#onDescriptorRead-instance_function "onDescriptorRead (Instance Function)") (descriptor as [BluetoothLowEnergy.Descriptor](Descriptor.md), status as [BluetoothLowEnergy.Status](../BluetoothLowEnergy.md#Status-module), value as [Lang.ByteArray](../Lang/ByteArray.md)) as **Void**
	After requesting a read operation on a Descriptor with [requestRead()](Descriptor.md#requestRead-instance_function) this function will be called when the operation is completed.
- [**onDescriptorWrite**](#onDescriptorWrite-instance_function "onDescriptorWrite (Instance Function)") (descriptor as [BluetoothLowEnergy.Descriptor](Descriptor.md), status as [BluetoothLowEnergy.Status](../BluetoothLowEnergy.md#Status-module)) as **Void**
	After requesting a write operation on a Descriptor with [requestWrite()](Descriptor.md#requestWrite-instance_function) this function will be called when the operation is completed.
- [**onEncryptionStatus**](#onEncryptionStatus-instance_function "onEncryptionStatus (Instance Function)") (device as [BluetoothLowEnergy.Device](Device.md), status as [BluetoothLowEnergy.Status](../BluetoothLowEnergy.md#Status-module)) as **Void**
	After requesting a new bond or reconnecting to a device with a previously established bond, this function will be called with the current encryption status.
- [**onProfileRegister**](#onProfileRegister-instance_function "onProfileRegister (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](Uuid.md), status as [BluetoothLowEnergy.Status](../BluetoothLowEnergy.md#Status-module)) as **Void**
	After Registering a UUID this callback will notify of the result of the registration request.
- [**onScanResults**](#onScanResults-instance_function "onScanResults (Instance Function)") (scanResults as [BluetoothLowEnergy.Iterator](Iterator.md)) as **Void**
	If a scan is running this will be called when new ScanResults are received.
- [**onScanStateChange**](#onScanStateChange-instance_function "onScanStateChange (Instance Function)") (scanState as [BluetoothLowEnergy.ScanState](../BluetoothLowEnergy.md#ScanState-module), status as [BluetoothLowEnergy.Status](../BluetoothLowEnergy.md#Status-module)) as **Void**
	When the state of scanning is modified the system will call this function with the new state and a status indicating the result of the last call to [setScanState()](../BluetoothLowEnergy.md#setScanState-instance_function).
