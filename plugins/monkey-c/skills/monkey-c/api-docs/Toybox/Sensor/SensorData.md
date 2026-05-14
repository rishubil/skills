---
title: Toybox.Sensor.SensorData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorData.html
---

## Class: Toybox.Sensor.SensorData

## Overview

A class to encapsulate all high-frequency sensor data that can be retrieved.

## Instance Member Summary

- [**accelerometerData**](#accelerometerData-var "accelerometerData (Var)") as [Sensor.AccelerometerData](AccelerometerData.md) or **Null**
	An [AccelerometerData](AccelerometerData.md) object.
- [**gyroscopeData**](#gyroscopeData-var "gyroscopeData (Var)") as [Sensor.GyroscopeData](GyroscopeData.md) or **Null**
	An [GyroscopeData](GyroscopeData.md) object.
- [**heartRateData**](#heartRateData-var "heartRateData (Var)") as [Sensor.HeartRateData](HeartRateData.md) or **Null**
	A [HeartRateData](HeartRateData.md) object.
- [**magnetometerData**](#magnetometerData-var "magnetometerData (Var)") as [Sensor.MagnetometerData](MagnetometerData.md) or **Null**
	An [MagnetometerData](MagnetometerData.md) object.

## Instance Attribute Details

### var accelerometerData as Sensor.AccelerometerData or Null

An [AccelerometerData](AccelerometerData.md) object.

Can be `null` if accelerometer data was not requested.

### var gyroscopeData as Sensor.GyroscopeData or Null

An [GyroscopeData](GyroscopeData.md) object.

Can be `null` if gyroscope data was not requested.

### var heartRateData as Sensor.HeartRateData or Null

A [HeartRateData](HeartRateData.md) object.

Can be `null` if heart rate interval data is not available.

### var magnetometerData as Sensor.MagnetometerData or Null

An [MagnetometerData](MagnetometerData.md) object.

Can be `null` if MagnetometerData data was not requested.
