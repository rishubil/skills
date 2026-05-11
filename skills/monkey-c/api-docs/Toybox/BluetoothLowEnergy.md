---
title: Toybox.BluetoothLowEnergy
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy.html
---

## Module: Toybox.BluetoothLowEnergy

## Overview

## Classes Under Namespace

**Classes:** [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html), [Characteristic](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Characteristic.html), [Descriptor](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Descriptor.html), [Device](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Device.html), [DevicePairException](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/DevicePairException.html), [InvalidRequestException](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/InvalidRequestException.html), [Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Iterator.html), [ProfileRegistrationException](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ProfileRegistrationException.html), [ScanResult](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html), [Service](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Service.html), [Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html), [UuidFormatException](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/UuidFormatException.html)

## Constant Summary

### Status

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| STATUS\_SUCCESS | 0 | API Level 3.1.0 | Operation Successful |
| STATUS\_NOT\_ENOUGH\_RESOURCES | 1 | API Level 3.1.0 | Operation failed due to lack of resources |
| STATUS\_READ\_FAIL | 12 | API Level 3.1.0 | Read Request Failed |
| STATUS\_WRITE\_FAIL | 14 | API Level 3.1.0 | Write Request Failed |
| STATUS\_GATT\_INSUFFICIENT\_AUTHENTICATION\_FAIL | 18 | API Level 4.2.5 | GATT operation failed due to insufficent authentication |
| STATUS\_GATT\_INSUFFICIENT\_ENCRYPTION\_FAIL | 19 | API Level 4.2.5 | GATT operation failed due to insufficent encryption |
| STATUS\_ENCRYPTION\_BOND\_FAIL | 100 | API Level 4.2.5 | Initial Bond Procedure Failed |
| STATUS\_ENCRYPTION\_PEER\_KEYS\_LOST | 101 | API Level 4.2.5 | Peer reports that its keys have been lost. |
| STATUS\_ENCRYPTION\_SECURITY\_INSUFFICIENT | 102 | API Level 4.2.5 | Peer Attempted to Reduce Key Security Level from a previous bond |

### ScanState

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SCAN\_STATE\_OFF | 0 | API Level 3.1.0 | BLE scanning disabled |
| SCAN\_STATE\_SCANNING | 1 | API Level 3.1.0 | BLE scanning active |

### ConnectionState

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONNECTION\_STATE\_DISCONNECTED | 0 | API Level 3.1.0 | Device is Disconnected |
| CONNECTION\_STATE\_CONNECTED | 1 | API Level 3.1.0 | Device is Connected |
| CONNECTION\_STATE\_REJECTED | 2 | API Level 5.1.0 | Device connection is rejected by the user because of insufficient security |

### WriteType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| WRITE\_TYPE\_WITH\_RESPONSE | 0 | API Level 3.1.0 | Write with response |
| WRITE\_TYPE\_DEFAULT | 1 | API Level 3.1.0 | Write without response (Default write type) |

### ConnectionStrategy

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONNECTION\_STRATEGY\_DEFAULT | 0 | API Level 5.1.0 | Pair the device, bonding may be requested later. |
| CONNECTION\_STRATEGY\_SECURE\_PAIR\_BOND | 1 | API Level 5.1.0 | Pair the device and establish secure bonding. Device may be bonded as part of the pairing process. |

## Instance Method Summary

- [**cccdUuid**](#cccdUuid-instance_function "cccdUuid (Instance Function)") () as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)
	Retrieves the CCCD Uuid.
- [**getAvailableConnectionCount**](#getAvailableConnectionCount-instance_function "getAvailableConnectionCount (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Accessor for determining the number of available connections.
- [**getBondedDevices**](#getBondedDevices-instance_function "getBondedDevices (Instance Function)") () as [BluetoothLowEnergy.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Iterator.html)
	Retrieve an Iterator of devices that the Application has bonded with that the system has saved bond information for.
- [**getPairedDevices**](#getPairedDevices-instance_function "getPairedDevices (Instance Function)") () as [BluetoothLowEnergy.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Iterator.html)
	Retrieve an Iterator of all currently paired devices accessible to the Application.
- [**longToUuid**](#longToUuid-instance_function "longToUuid (Instance Function)") (mostSigBits as [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html), leastSigBits as [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html)) as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)
	Converts long representation of a UUID to a Uuid object.
- [**pairDevice**](#pairDevice-instance_function "pairDevice (Instance Function)") (scanResult as [BluetoothLowEnergy.ScanResult](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html)) as [BluetoothLowEnergy.Device](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Device.html) or **Null**
	Pairs a peripheral device seen in scanning with the system.
- [**registerProfile**](#registerProfile-instance_function "registerProfile (Instance Function)") (profile as {:uuid as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html),:characteristics as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) <{:uuid as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html),:descriptors as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html) > }> }) as **Void**
	Registers a Bluetooth Profile Definition Call this function to define all of the Profiles that will be used in the application.
- [**setConnectionStrategy**](#setConnectionStrategy-instance_function "setConnectionStrategy (Instance Function)") (connectionStrategy as [BluetoothLowEnergy.ConnectionStrategy](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy.html#ConnectionStrategy-module)) as **Void**
	Set the connection type used to connect to the BLE device.
- [**setDelegate**](#setDelegate-instance_function "setDelegate (Instance Function)") (delegate as [BluetoothLowEnergy.BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html)) as **Void**
	Sets the Delegate Handler for Bluetooth Asynchronous Callbacks An application can only have 1 registered delegate.
- [**setScanState**](#setScanState-instance_function "setScanState (Instance Function)") (scanState as [BluetoothLowEnergy.ScanState](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy.html#ScanState-module)) as **Void**
	Starts the BLE Scanning Operations Once scanning is started [onScanResults()](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html#onScanResults-instance_function) will be called on the registered [BleDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/BleDelegate.html) as Advertising data is received.
- [**stringToUuid**](#stringToUuid-instance_function "stringToUuid (Instance Function)") (str as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as [BluetoothLowEnergy.Uuid](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Uuid.html)
	Converts the String Representation of a UUID into a Uuid Object.
- [**unpairDevice**](#unpairDevice-instance_function "unpairDevice (Instance Function)") (device as [BluetoothLowEnergy.Device](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/Device.html)) as **Void**
	Unpairs a peripheral device from the system If the device is connected the BLE Subsystem will disconnect from the device and will not attempt to reconnect.

## Instance Method Details

### cccdUuid() as BluetoothLowEnergy.Uuid

### getAvailableConnectionCount() as Lang.Number

### getBondedDevices() as BluetoothLowEnergy.Iterator

### getPairedDevices() as BluetoothLowEnergy.Iterator

### longToUuid(mostSigBits as Lang.Long, leastSigBits as Lang.Long) as BluetoothLowEnergy.Uuid

### pairDevice(scanResult as BluetoothLowEnergy.ScanResult) as BluetoothLowEnergy.Device or Null

### registerProfile(profile as {:uuid as BluetoothLowEnergy.Uuid,:characteristics as Lang.Array<{:uuid as BluetoothLowEnergy.Uuid,:descriptors as Lang.Array<BluetoothLowEnergy.Uuid> }> }) as Void

### setConnectionStrategy(connectionStrategy as BluetoothLowEnergy.ConnectionStrategy) as Void

Note:

The default value is CONNECTION\_TYPE\_DEFAULT. Using the value of CONNECTION\_TYPE\_SECURE\_PAIR\_BOND will pair and bond the device as part of the pairing process.
