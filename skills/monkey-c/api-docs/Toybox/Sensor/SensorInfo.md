---
title: Toybox.Sensor.SensorInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html
---

## Class: Toybox.Sensor.SensorInfo

## Overview

A class describing a Sensor

The SensorInfo provides access to the attributes of a Sensor.

## Instance Member Summary

- [**data**](#data-var "data (Var)") as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or **Null**
	The Sensor-specific data A dictionary of sensor-specific attributes.
- [**enabled**](#enabled-var "enabled (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The Sensor enabled flag.
- [**manufacturerId**](#manufacturerId-var "manufacturerId (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The Sensor manufacturer.
- [**name**](#name-var "name (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	The Sensor name.
- [**partNumber**](#partNumber-var "partNumber (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The Sensor part number.
- [**softwareVersion**](#softwareVersion-var "softwareVersion (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The Sensor software version.
- [**technology**](#technology-var "technology (Var)") as [Sensor.SensorTechnology](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html#SensorTechnology-module)
	The Sensor technology The technology used to communicate with this sensor.
- [**type**](#type-var "type (Var)") as [Sensor.SensorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html#SensorType-named_type)
	The Sensor type.

## Instance Attribute Details

### var data as Lang.Dictionary or Null

The Sensor-specific data

A dictionary of sensor-specific attributes. Currently supported attributes include:

- `:bleAddress` - The mac address of the BLE sensor (e.g., 01:02:03:04:05:06) as a [ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html), if available.
- `:antSerialNumber` - The 20-bit ANT sensor serial number as a [Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
- `:bleScanResult` - The scanresult of a discovered BLE device as a [ScanResult](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html).
- `:antMessage` - The ANT message of a discovered ANT device as a [Message](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/Message.html)

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
