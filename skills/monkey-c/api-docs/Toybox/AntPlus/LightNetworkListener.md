---
title: Toybox.AntPlus.LightNetworkListener
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/LightNetworkListener.html
---

## Class: Toybox.AntPlus.LightNetworkListener

Inherits:

Toybox.AntPlus.DeviceListener
- [Toybox.Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)
- [Toybox.AntPlus.DeviceListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceListener.html)
- [Toybox.AntPlus.LightNetworkListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/LightNetworkListener.html)
[show all](#)

## Overview

Listener class for use with LightNetwork.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onBikeLightUpdate**](#onBikeLightUpdate-instance_function "onBikeLightUpdate (Instance Function)") (data as [AntPlus.BikeLight](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeLight.html)) as **Void**
	Callback when a bike light's data is updated (max freq.
- [**onLightNetworkStateUpdate**](#onLightNetworkStateUpdate-instance_function "onLightNetworkStateUpdate (Instance Function)") (data as [AntPlus.LightNetworkState](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html#LightNetworkState-module)) as **Void**
	Callback when the light network state changes.

## Instance Method Details

### initialize()

Constructor

### onBikeLightUpdate(data as AntPlus.BikeLight) as Void

Callback when a bike light's data is updated (max freq. 1Hz)

### onLightNetworkStateUpdate(data as AntPlus.LightNetworkState) as Void

Callback when the light network state changes
