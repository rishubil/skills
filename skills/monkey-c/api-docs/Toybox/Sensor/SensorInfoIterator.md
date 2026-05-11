---
title: Toybox.Sensor.SensorInfoIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfoIterator.html
---

## Class: Toybox.Sensor.SensorInfoIterator

## Overview

A class encapsulating a collection of Sensors

The SensorIterator describes a collection of [SensorInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html) objects that describe actual sensors. Such an iterator is retrieved using the appropriate "get\*Sensors' methods found in [Sensor](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor.html) at the module level.

## Instance Method Summary

- [**next**](#next-instance_function "next (Instance Function)") () as [Sensor.SensorInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html) or **Null**
	Get the current [SensorInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html) and advance.

## Instance Method Details

### next() as Sensor.SensorInfo or Null

Get the current [SensorInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html) and advance.

Get the current [SensorInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Sensor/SensorInfo.html) and advance self to refer to the next.
