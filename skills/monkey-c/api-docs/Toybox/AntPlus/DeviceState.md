---
title: Toybox.AntPlus.DeviceState
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceState.html
---

## Class: Toybox.AntPlus.DeviceState

## Overview

The DeviceState object represents the state of the device.

Fields may return `null` so you should `null` check values before using them.

## Instance Member Summary

- [**deviceNumber**](#deviceNumber-var "deviceNumber (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The current Device ID being tracked/searched for.
- [**state**](#state-var "state (Var)") as [AntPlus.DeviceCurrentState](../AntPlus.md#DeviceCurrentState-module) or **Null**
	The state of the device as an [DEVICE\_STATE\_\*](../AntPlus.md#DEVICE_STATE_CLOSED-const) value.

## Instance Attribute Details

### var deviceNumber as Lang.Number or Null

The current Device ID being tracked/searched for.

### var state as AntPlus.DeviceCurrentState or Null

The state of the device as an [DEVICE\_STATE\_\*](../AntPlus.md#DEVICE_STATE_CLOSED-const) value.
