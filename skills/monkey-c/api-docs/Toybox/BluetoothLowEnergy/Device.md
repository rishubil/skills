---
title: Toybox.BluetoothLowEnergy.Device
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Device.html
---

## Class: Toybox.BluetoothLowEnergy.Device

## Overview

Represents a Bluetooth Low Energy Device that has been paired with the system.

This class cannot be instantiated, access to paired system devices is done through the use of [getPairedDevices()](../BluetoothLowEnergy.md#getPairedDevices-instance_function) or by calling [pairDevice()](../BluetoothLowEnergy.md#pairDevice-instance_function) after receiving a [ScanResult](ScanResult.md) for a device

## Instance Method Summary

- [**getName**](#getName-instance_function "getName (Instance Function)") () as [Lang.String](../Lang/String.md) or **Null**
	Retrieves the Name of the sensor according to the device name that is available in the GAP Service.
- [**getService**](#getService-instance_function "getService (Instance Function)") (uuid as [BluetoothLowEnergy.Uuid](Uuid.md)) as [BluetoothLowEnergy.Service](Service.md) or **Null**
	Retrieves the service with a specified UUID If access to a specific service is required, use this function to directly access the service based on a UUID.
- [**getServices**](#getServices-instance_function "getServices (Instance Function)") () as [BluetoothLowEnergy.Iterator](Iterator.md)
	Retrieves an Iterator over the services provided by the device.
- [**isBonded**](#isBonded-instance_function "isBonded (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Gets the Bonded State of the Device.
- [**isConnected**](#isConnected-instance_function "isConnected (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Gets the connected status of the device.
- [**requestBond**](#requestBond-instance_function "requestBond (Instance Function)") () as **Void**
	Requests that a bond is formed with the Device If the device is not currently bonded this will initiate the bonding procedure.

## Instance Method Details

### getName() as Lang.String or Null

Retrieves the Name of the sensor according to the device name that is available in the GAP Service

### getService(uuid as BluetoothLowEnergy.Uuid) as BluetoothLowEnergy.Service or Null

Retrieves the service with a specified UUID

If access to a specific service is required, use this function to directly access the service based on a UUID.

### getServices() as BluetoothLowEnergy.Iterator

Retrieves an Iterator over the services provided by the device.

This will only provide Services that have been registered using [registerProfile()](../BluetoothLowEnergy.md#registerProfile-instance_function)

### isBonded() as Lang.Boolean

Gets the Bonded State of the Device

### isConnected() as Lang.Boolean

Gets the connected status of the device

### requestBond() as Void

Requests that a bond is formed with the Device

If the device is not currently bonded this will initiate the bonding procedure.

Once the operation is completed, [onEncryptionStatus()](BleDelegate.md#onEncryptionStatus-instance_function) will be called on the registered [BleDelegate](BleDelegate.md) with the status of the operation
