---
title: Toybox.AntPlus.Shifting
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/Shifting.html
---

## Class: Toybox.AntPlus.Shifting

Inherits:

Toybox.AntPlus.Device
- [Toybox.Lang.Object](../Lang/Object.md)
- [Toybox.AntPlus.Device](Device.md)
- [Toybox.AntPlus.Shifting](Shifting.md)
[show all](#)

## Overview

Represents a shifting device instance

## Instance Method Summary

- [**getShiftingStatus**](#getShiftingStatus-instance_function "getShiftingStatus (Instance Function)") () as [AntPlus.ShiftingStatus](ShiftingStatus.md)
	Get current shifting system status Will not provide status for Shimano shifting systems.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (listener as [AntPlus.ShiftingListener](ShiftingListener.md) or **Null**)
	Constructor.

## Instance Method Details

### getShiftingStatus() as AntPlus.ShiftingStatus

Get current shifting system status Will not provide status for Shimano shifting systems.

### initialize(listener as AntPlus.ShiftingListener or Null)

Constructor
