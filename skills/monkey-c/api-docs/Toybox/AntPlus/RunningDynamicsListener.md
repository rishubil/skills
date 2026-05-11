---
title: Toybox.AntPlus.RunningDynamicsListener
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamicsListener.html
---

## Class: Toybox.AntPlus.RunningDynamicsListener

Inherits:

Toybox.AntPlus.DeviceListener
- [Toybox.Lang.Object](../Lang/Object.md)
- [Toybox.AntPlus.DeviceListener](DeviceListener.md)
- [Toybox.AntPlus.RunningDynamicsListener](RunningDynamicsListener.md)
[show all](#)

## Overview

Listener class for Running Dynamics.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onRunningDynamicsUpdate**](#onRunningDynamicsUpdate-instance_function "onRunningDynamicsUpdate (Instance Function)") (data as [AntPlus.RunningDynamicsData](RunningDynamicsData.md)) as **Void**
	Callback when running dynamics are updated (max freq 1Hz).
- [**onSensorPositionUpdate**](#onSensorPositionUpdate-instance_function "onSensorPositionUpdate (Instance Function)") (data as [AntPlus.SensorPosition](SensorPosition.md)) as **Void**
	Callback when sensor position is updated (max freq 1Hz).

## Instance Method Details

### initialize()

Constructor

### onRunningDynamicsUpdate(data as AntPlus.RunningDynamicsData) as Void

Callback when running dynamics are updated (max freq 1Hz)

### onSensorPositionUpdate(data as AntPlus.SensorPosition) as Void

Callback when sensor position is updated (max freq 1Hz)
