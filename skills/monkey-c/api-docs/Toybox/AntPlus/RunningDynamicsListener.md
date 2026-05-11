---
title: Toybox.AntPlus.RunningDynamicsListener
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamicsListener.html
---

## Class: Toybox.AntPlus.RunningDynamicsListener

Inherits:

Toybox.AntPlus.DeviceListener
- [Toybox.Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)
- [Toybox.AntPlus.DeviceListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceListener.html)
- [Toybox.AntPlus.RunningDynamicsListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamicsListener.html)
[show all](#)

## Overview

Listener class for Running Dynamics.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onRunningDynamicsUpdate**](#onRunningDynamicsUpdate-instance_function "onRunningDynamicsUpdate (Instance Function)") (data as [AntPlus.RunningDynamicsData](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamicsData.html)) as **Void**
	Callback when running dynamics are updated (max freq 1Hz).
- [**onSensorPositionUpdate**](#onSensorPositionUpdate-instance_function "onSensorPositionUpdate (Instance Function)") (data as [AntPlus.SensorPosition](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/SensorPosition.html)) as **Void**
	Callback when sensor position is updated (max freq 1Hz).

## Instance Method Details

### initialize()

Constructor

### onRunningDynamicsUpdate(data as AntPlus.RunningDynamicsData) as Void

Callback when running dynamics are updated (max freq 1Hz)

### onSensorPositionUpdate(data as AntPlus.SensorPosition) as Void

Callback when sensor position is updated (max freq 1Hz)
