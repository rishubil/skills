---
title: Toybox.Sensor.SensorDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorDelegate.html
---

## Class: Toybox.Sensor.SensorDelegate

## Overview

Delegate for handling native sensor pairing process.

The members of this object get called by the system to delegate scanning and pairing of different sensors.

## Instance Method Summary

- [**onPair**](#onPair-instance_function "onPair (Instance Function)") (sensor as [Sensor.SensorInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Pair the sensor.
- [**onScan**](#onScan-instance_function "onScan (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Start the sensor scan process.
- [**onUnpair**](#onUnpair-instance_function "onUnpair (Instance Function)") (sensor as [Sensor.SensorInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Unpair the sensor.
- [**pairingRequired**](#pairingRequired-instance_function "pairingRequired (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Is sensor pairing required? Is called by the system to check if sensor pairing is required.

## Instance Method Details

### onPair(sensor as Sensor.SensorInfo) as Lang.Boolean

Pair the sensor.

Is called by the system to pair the sensor, during the native sensor pairing process.

### onScan() as Lang.Boolean

Start the sensor scan process.

Is called by the system to start the sensor scan process, during the native sensor pairing process.

### onUnpair(sensor as Sensor.SensorInfo) as Lang.Boolean

Unpair the sensor.

Is called by the system to unpair the sensor, during the native sensor removing process.

### pairingRequired() as Lang.Boolean

Is sensor pairing required?

Is called by the system to check if sensor pairing is required.
