---
title: Toybox.Sensor
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html
---

## Module: Toybox.Sensor

## Overview

## Classes Under Namespace

**Classes:** [AccelerometerData](Sensor/AccelerometerData.md), [GyroscopeData](Sensor/GyroscopeData.md), [HeartRateData](Sensor/HeartRateData.md), [Info](Sensor/Info.md), [MagnetometerData](Sensor/MagnetometerData.md), [SensorData](Sensor/SensorData.md), [SensorDelegate](Sensor/SensorDelegate.md), [SensorInfo](Sensor/SensorInfo.md), [SensorInfoIterator](Sensor/SensorInfoIterator.md), [TooManySensorDataListenersException](Sensor/TooManySensorDataListenersException.md)

## Constant Summary

### RemoteSensorType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SENSOR\_BIKESPEED | 0 | API Level 1.0.0 |  |
| SENSOR\_BIKECADENCE | 1 | API Level 1.0.0 |  |
| SENSOR\_BIKEPOWER | 2 | API Level 1.0.0 |  |
| SENSOR\_FOOTPOD | 3 | API Level 1.0.0 |  |
| SENSOR\_HEARTRATE | 4 | API Level 1.0.0 |  |
| SENSOR\_TEMPERATURE | 5 | API Level 1.0.0 |  |
| SENSOR\_GENERIC | 9 | API Level 5.1.0 |  |

### OnboardSensorType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SENSOR\_PULSE\_OXIMETRY | 6 | API Level 3.2.0 |  |
| SENSOR\_ONBOARD\_PULSE\_OXIMETRY | 7 | API Level 3.2.0 |  |
| SENSOR\_ONBOARD\_HEARTRATE | 8 | API Level 3.2.0 |  |

### SensorTechnology

The sensor technology

Describes the technology used to communicate with the sensor.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SENSOR\_TECHNOLOGY\_ANT | 0 | API Level 3.2.0 | ANT Sensor |
| SENSOR\_TECHNOLOGY\_BLE | 1 | API Level 3.2.0 | Bluetooth Low Energy Sensor |
| SENSOR\_TECHNOLOGY\_ONBOARD | 2 | API Level 3.2.0 | Onboard Sensor |

## Typedef Summary

## Instance Method Summary

- [**disableSensorType**](#disableSensorType-instance_function "disableSensorType (Instance Function)") (sensorType as [Sensor.SensorType](Sensor.md#SensorType-named_type)) as [Lang.Boolean](Lang/Boolean.md)
	Disable the given sensor type for use.
- [**enableSensorEvents**](#enableSensorEvents-instance_function "enableSensorEvents (Instance Function)") (listener as **Null** or [Lang.Method](Lang/Method.md) (info as [Sensor.Info](Sensor/Info.md)) as **Void**) as **Void**
	Request sensor events from enabled sensors.
- [**enableSensorType**](#enableSensorType-instance_function "enableSensorType (Instance Function)") (sensorType as [Sensor.SensorType](Sensor.md#SensorType-named_type)) as [Lang.Boolean](Lang/Boolean.md)
	Enable the given sensor type for use.
- [**getInfo**](#getInfo-instance_function "getInfo (Instance Function)") () as [Sensor.Info](Sensor/Info.md)
	Get the current Sensor [Sensor.Info](Sensor/Info.md).
- [**getMaxSampleRate**](#getMaxSampleRate-instance_function "getMaxSampleRate (Instance Function)") () as [Lang.Number](Lang/Number.md)
	Get the maximum sample rate supported by the system.
- [**getMaxSampleRateForSensorType**](#getMaxSampleRateForSensorType-instance_function "getMaxSampleRateForSensorType (Instance Function)") (sensorDataType as [Lang.Symbol](Lang/Symbol.md)) as [Lang.Number](Lang/Number.md)
	Get the maximum sample rate supported for given sensor data type.
- [**getRegisteredSensors**](#getRegisteredSensors-instance_function "getRegisteredSensors (Instance Function)") (sensorType as [Sensor.SensorType](Sensor.md#SensorType-named_type) or **Null**) as [Sensor.SensorInfoIterator](Sensor/SensorInfoIterator.md)
	Retrieve the sensors that are currently registered.
- [**notifyError**](#notifyError-instance_function "notifyError (Instance Function)") (string as [Lang.String](Lang/String.md) or **Null**) as **Void**
	Let the system know the app has encountered an error.
- [**notifyNewSensor**](#notifyNewSensor-instance_function "notifyNewSensor (Instance Function)") (sensor as [Sensor.SensorInfo](Sensor/SensorInfo.md), configurationRequired as [Lang.Boolean](Lang/Boolean.md)) as **Void**
	Let the system know the app has discovered a new sensor.
- [**notifyPairComplete**](#notifyPairComplete-instance_function "notifyPairComplete (Instance Function)") (sensor as [Sensor.SensorInfo](Sensor/SensorInfo.md)) as **Void**
	Let the system know the app has finished pairing a sensor.
- [**notifyScanComplete**](#notifyScanComplete-instance_function "notifyScanComplete (Instance Function)") () as **Void**
	Let the system know the app has finished scanning for sensors.
- [**notifyUnpairComplete**](#notifyUnpairComplete-instance_function "notifyUnpairComplete (Instance Function)") (sensor as [Sensor.SensorInfo](Sensor/SensorInfo.md)) as **Void**
	Let the system know the app has finished unpairing a sensor.
- [**registerSensorDataListener**](#registerSensorDataListener-instance_function "registerSensorDataListener (Instance Function)") (listener as [Lang.Method](Lang/Method.md) (data as [Sensor.SensorData](Sensor/SensorData.md)) as **Void**, options as {:period as [Lang.Number](Lang/Number.md),:accelerometer as {:enabled as [Lang.Boolean](Lang/Boolean.md),:sampleRate as [Lang.Number](Lang/Number.md),:includePower as [Lang.Boolean](Lang/Boolean.md),:includePitch as [Lang.Boolean](Lang/Boolean.md),:includeRoll as [Lang.Boolean](Lang/Boolean.md),:includeTimestamps as [Lang.Boolean](Lang/Boolean.md) },:gyroscope as {:enabled as [Lang.Boolean](Lang/Boolean.md),:sampleRate as [Lang.Number](Lang/Number.md),:includeTimestamps as [Lang.Boolean](Lang/Boolean.md) },:magnetometer as {:enabled as [Lang.Boolean](Lang/Boolean.md),:sampleRate as [Lang.Number](Lang/Number.md),:includeTimestamps as [Lang.Boolean](Lang/Boolean.md) },:heartBeatIntervals as {:enabled as [Lang.Boolean](Lang/Boolean.md) },:synchronous as [Lang.Boolean](Lang/Boolean.md) }) as **Void**
	Register a callback to fetch high-frequency data from various sensors.
- [**setEnabledSensors**](#setEnabledSensors-instance_function "setEnabledSensors (Instance Function)") (sensors as [Lang.Array](Lang/Array.md) < [Sensor.SensorType](Sensor.md#SensorType-named_type) >) as [Lang.Array](Lang/Array.md) < [Sensor.SensorType](Sensor.md#SensorType-named_type) >
	Enable sensors for use.
- [**unregisterSensorDataListener**](#unregisterSensorDataListener-instance_function "unregisterSensorDataListener (Instance Function)") () as **Void**
	Unregister a previously registered data listener.

## Typedef Details

### SensorType as Sensor.RemoteSensorType or Sensor.OnboardSensorType

## Instance Method Details

### disableSensorType(sensorType as Sensor.SensorType) as Lang.Boolean

Note:

Will cause an app crash if called from a data field app

### enableSensorEvents(listener as Null or Lang.Method(info as Sensor.Info) as Void) as Void

Note:

Will cause an app crash if called from a data field app

### enableSensorType(sensorType as Sensor.SensorType) as Lang.Boolean

Note:

Will cause an app crash if called from a data field app

Note:

Multitasking: Sensor states can not be changed while in inacitve mode and sensor enabled during active mode will be disabled when app becomes inactive, and re-enabled automatically when is active again. These state changes are denoted by calls to AppBase.onActive() and AppBase.onInactive().

### getInfo() as Sensor.Info

Note:

Will cause an app crash if called from a data field app

### getMaxSampleRate() as Lang.Number

Note:

Will cause an app crash if called from a data field app

Note:

This function can produce different results after the app transitions to the active state after being inactive. These state changes are denoted by calls to AppBase.onActive() and AppBase.onInactive().

### getMaxSampleRateForSensorType(sensorDataType as Lang.Symbol) as Lang.Number

Note:

Will cause an app crash if called from a data field app

Note:

This function can produce different results after the app transitions to the active state after being inactive. These state changes are denoted by calls to AppBase.onActive() and AppBase.onInactive().

### getRegisteredSensors(sensorType as Sensor.SensorType or Null) as Sensor.SensorInfoIterator

### notifyError(string as Lang.String or Null) as Void

### notifyNewSensor(sensor as Sensor.SensorInfo, configurationRequired as Lang.Boolean) as Void

### notifyPairComplete(sensor as Sensor.SensorInfo) as Void

### notifyScanComplete() as Void

### notifyUnpairComplete(sensor as Sensor.SensorInfo) as Void

### registerSensorDataListener(listener as Lang.Method(data as Sensor.SensorData) as Void, options as {:period as Lang.Number,:accelerometer as {:enabled as Lang.Boolean,:sampleRate as Lang.Number,:includePower as Lang.Boolean,:includePitch as Lang.Boolean,:includeRoll as Lang.Boolean,:includeTimestamps as Lang.Boolean },:gyroscope as {:enabled as Lang.Boolean,:sampleRate as Lang.Number,:includeTimestamps as Lang.Boolean },:magnetometer as {:enabled as Lang.Boolean,:sampleRate as Lang.Number,:includeTimestamps as Lang.Boolean },:heartBeatIntervals as {:enabled as Lang.Boolean },:synchronous as Lang.Boolean }) as Void

Note:

Only one data request is allowed to be registered at a time. Subsequent calls to this function for the same sensor type will override previously registered requests.

Note:

Magnetometer data is not supported in synchronous data request.

Note:

Will cause an app crash if called from a data field app

### setEnabledSensors(sensors as Lang.Array<Sensor.SensorType>) as Lang.Array<Sensor.SensorType>

Note:

Will cause an app crash if called from a data field app

Note:

Multitasking: Sensor states can not be changed while in inacitve mode and sensor enabled during active mode will be disabled when app becomes inactive, and re-enabled automatically when is active again. These state changes are denoted by calls to AppBase.onActive() and AppBase.onInactive().

### unregisterSensorDataListener() as Void

Note:

Will cause an app crash if called from a data field app
