---
title: Toybox.AntPlus.RunningDynamics
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamics.html
---

## Class: Toybox.AntPlus.RunningDynamics

Inherits:

Toybox.AntPlus.Device
- [Toybox.Lang.Object](../Lang/Object.md)
- [Toybox.AntPlus.Device](Device.md)
- [Toybox.AntPlus.RunningDynamics](RunningDynamics.md)
[show all](#)

## Overview

Represents a Running Dynamics Device instance.

## Instance Method Summary

- [**getRunningDynamics**](#getRunningDynamics-instance_function "getRunningDynamics (Instance Function)") () as [AntPlus.RunningDynamicsData](RunningDynamicsData.md)
	Use getRunningDynamics() to get the most current running dynamics.
- [**getSensorPosition**](#getSensorPosition-instance_function "getSensorPosition (Instance Function)") () as [AntPlus.SensorPosition](SensorPosition.md)
	Use getSensorPosition() to retrieve the position of the sensor on the body.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (listener as [AntPlus.RunningDynamicsListener](RunningDynamicsListener.md) or **Null**)
	Constructor.

## Instance Method Details

### getRunningDynamics() as AntPlus.RunningDynamicsData

Use getRunningDynamics() to get the most current running dynamics.

### getSensorPosition() as AntPlus.SensorPosition

Use getSensorPosition() to retrieve the position of the sensor on the body

### initialize(listener as AntPlus.RunningDynamicsListener or Null)

Constructor
