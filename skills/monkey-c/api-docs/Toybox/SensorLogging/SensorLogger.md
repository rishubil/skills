---
title: Toybox.SensorLogging.SensorLogger
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorLogging/SensorLogger.html
---

## Class: Toybox.SensorLogging.SensorLogger

## Overview

## Instance Method Summary

- [**getStats**](#getStats-instance_function "getStats (Instance Function)") () as [SensorLogging.SensorLoggingStats](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorLogging/SensorLoggingStats.html) or **Null**
	Get statistics for the data gathered in the current session.
- [**getStats2**](#getStats2-instance_function "getStats2 (Instance Function)") (sensor as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html) or **Null**) as [SensorLogging.SensorLoggingStats](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorLogging/SensorLoggingStats.html) or {:accelerometer as [SensorLogging.SensorLoggingStats](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorLogging/SensorLoggingStats.html),:gyroscope as [SensorLogging.SensorLoggingStats](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorLogging/SensorLoggingStats.html),:magnetometer as [SensorLogging.SensorLoggingStats](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorLogging/SensorLoggingStats.html) }
	Get statistics for the sensor data gathered in the current session.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:accelerometer as {:enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) },:gyroscope as {:enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) },:magnetometer as {:enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) },:synchronous as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) })
	Constructor.

## Instance Method Details

### getStats() as SensorLogging.SensorLoggingStats or Null

### getStats2(sensor as Lang.Symbol or Null) as SensorLogging.SensorLoggingStats or {:accelerometer as SensorLogging.SensorLoggingStats,:gyroscope as SensorLogging.SensorLoggingStats,:magnetometer as SensorLogging.SensorLoggingStats }

### initialize(options as {:accelerometer as {:enabled as Lang.Boolean },:gyroscope as {:enabled as Lang.Boolean },:magnetometer as {:enabled as Lang.Boolean },:synchronous as Lang.Boolean })

Note:

A SensorLogger may be initialized with the same dictionary of options provided to [registerSensorDataListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html#registerSensorDataListener-instance_function), but only the options documented below will be used.

Note:

Magnetometer data is not supported in synchronous data request.
