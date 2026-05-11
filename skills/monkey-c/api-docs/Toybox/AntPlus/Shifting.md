---
title: Toybox.AntPlus.Shifting
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/Shifting.html
---

## Class: Toybox.AntPlus.Shifting

Inherits:

Toybox.AntPlus.Device
- [Toybox.Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)
- [Toybox.AntPlus.Device](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/Device.html)
- [Toybox.AntPlus.Shifting](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/Shifting.html)
[show all](#)

## Overview

Represents a shifting device instance

## Instance Method Summary

- [**getShiftingStatus**](#getShiftingStatus-instance_function "getShiftingStatus (Instance Function)") () as [AntPlus.ShiftingStatus](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ShiftingStatus.html)
	Get current shifting system status Will not provide status for Shimano shifting systems.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (listener as [AntPlus.ShiftingListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ShiftingListener.html) or **Null**)
	Constructor.

## Instance Method Details

### getShiftingStatus() as AntPlus.ShiftingStatus

Get current shifting system status Will not provide status for Shimano shifting systems.

### initialize(listener as AntPlus.ShiftingListener or Null)

Constructor
