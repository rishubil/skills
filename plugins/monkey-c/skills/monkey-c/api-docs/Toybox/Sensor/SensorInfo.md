---
title: Toybox.Sensor.SensorInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html
---

## Class: Toybox.Sensor.SensorInfo

## Overview

A class describing a Sensor

The SensorInfo provides access to the attributes of a Sensor.

## Instance Member Summary

- [**data**](#data-var "data (Var)") as [Lang.Dictionary](../Lang/Dictionary.md) or **Null**
	The Sensor-specific data A dictionary of sensor-specific attributes.
- [**enabled**](#enabled-var "enabled (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The Sensor enabled flag.
- [**manufacturerId**](#manufacturerId-var "manufacturerId (Var)") as [Lang.Number](../Lang/Number.md)
	The Sensor manufacturer.
- [**name**](#name-var "name (Var)") as [Lang.String](../Lang/String.md)
	The Sensor name.
- [**partNumber**](#partNumber-var "partNumber (Var)") as [Lang.Number](../Lang/Number.md)
	The Sensor part number.
- [**softwareVersion**](#softwareVersion-var "softwareVersion (Var)") as [Lang.Number](../Lang/Number.md)
	The Sensor software version.
- [**technology**](#technology-var "technology (Var)") as [Sensor.SensorTechnology](../Sensor.md#SensorTechnology-module)
	The Sensor technology The technology used to communicate with this sensor.
- [**type**](#type-var "type (Var)") as [Sensor.SensorType](../Sensor.md#SensorType-named_type)
	The Sensor type.

## Instance Attribute Details

### var data as Lang.Dictionary or Null

The Sensor-specific data

A dictionary of sensor-specific attributes. Currently supported attributes include:

- `:bleAddress` - The mac address of the BLE sensor (e.g., 01:02:03:04:05:06) as a [ByteArray](../Lang/ByteArray.md), if available.
- `:antSerialNumber` - The 20-bit ANT sensor serial number as a [Number](../Lang/Number.md)
- `:bleScanResult` - The scanresult of a discovered BLE device as a [ScanResult](../BluetoothLowEnergy/ScanResult.md).
- `:antMessage` - The ANT message of a discovered ANT device as a [Message](../Ant/Message.md)

### var enabled as Lang.Boolean

The Sensor enabled flag.

An indicator of whether or not the sensor is enabled for pairing.

### var manufacturerId as Lang.Number

The Sensor manufacturer.

The manufacturer id of the sensor. May be `null`.

### var name as Lang.String

The Sensor name.

The name of the sensor.

### var partNumber as Lang.Number

The Sensor part number.

The part number the sensor. May be `null`.

### var softwareVersion as Lang.Number

The Sensor software version.

The software version of the sensor. May be `null`.

### var technology as Sensor.SensorTechnology

The Sensor technology

The technology used to communicate with this sensor.

### var type as Sensor.SensorType

The Sensor type.

The type of the sensor.
