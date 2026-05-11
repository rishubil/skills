---
title: Toybox.Sensor.SensorData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorData.html
---

## Class: Toybox.Sensor.SensorData

## Overview

A class to encapsulate all high-frequency sensor data that can be retrieved.

## Instance Member Summary

- [**accelerometerData**](#accelerometerData-var "accelerometerData (Var)") as [Sensor.AccelerometerData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/AccelerometerData.html) or **Null**
	An [AccelerometerData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/AccelerometerData.html) object.
- [**gyroscopeData**](#gyroscopeData-var "gyroscopeData (Var)") as [Sensor.GyroscopeData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/GyroscopeData.html) or **Null**
	An [GyroscopeData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/GyroscopeData.html) object.
- [**heartRateData**](#heartRateData-var "heartRateData (Var)") as [Sensor.HeartRateData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/HeartRateData.html) or **Null**
	A [HeartRateData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/HeartRateData.html) object.
- [**magnetometerData**](#magnetometerData-var "magnetometerData (Var)") as [Sensor.MagnetometerData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/MagnetometerData.html) or **Null**
	An [MagnetometerData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/MagnetometerData.html) object.

## Instance Attribute Details

### var accelerometerData as Sensor.AccelerometerData or Null

An [AccelerometerData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/AccelerometerData.html) object.

Can be `null` if accelerometer data was not requested.

### var gyroscopeData as Sensor.GyroscopeData or Null

An [GyroscopeData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/GyroscopeData.html) object.

Can be `null` if gyroscope data was not requested.

### var heartRateData as Sensor.HeartRateData or Null

A [HeartRateData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/HeartRateData.html) object.

Can be `null` if heart rate interval data is not available.

### var magnetometerData as Sensor.MagnetometerData or Null

An [MagnetometerData](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/MagnetometerData.html) object.

Can be `null` if MagnetometerData data was not requested.
