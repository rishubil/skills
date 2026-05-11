---
title: Toybox.AntPlus.Device
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/Device.html
---

## Class: Toybox.AntPlus.Device

## Overview

The Device object represents an ANT+ Device instance.

## Direct Known Subclasses

[AntPlus.BikeCadence](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeCadence.html), [AntPlus.BikePower](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikePower.html), [AntPlus.BikeRadar](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeRadar.html), [AntPlus.BikeSpeed](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeSpeed.html), [AntPlus.BikeSpeedCadence](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeSpeedCadence.html), [AntPlus.FitnessEquipment](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/FitnessEquipment.html), [AntPlus.LightNetwork](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/LightNetwork.html), [AntPlus.RunningDynamics](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamics.html), [AntPlus.Shifting](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/Shifting.html)

## Instance Method Summary

- [**getBatteryStatus**](#getBatteryStatus-instance_function "getBatteryStatus (Instance Function)") (identifier as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [AntPlus.BatteryStatus](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BatteryStatus.html) or **Null**
	Retrieve battery status for provided component identifier.
- [**getComponentIdentifiers**](#getComponentIdentifiers-instance_function "getComponentIdentifiers (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) > or **Null**
	Retrieve a list of known component identifiers for this Device.
- [**getDeviceState**](#getDeviceState-instance_function "getDeviceState (Instance Function)") () as [AntPlus.DeviceState](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceState.html)
	Retrieve the state of the device.
- [**getManufacturerInfo**](#getManufacturerInfo-instance_function "getManufacturerInfo (Instance Function)") (identifier as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [AntPlus.ManufacturerInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ManufacturerInfo.html) or **Null**
	Retrieve manufacturer information for provided component identifier.
- [**getProductInfo**](#getProductInfo-instance_function "getProductInfo (Instance Function)") (identifier as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [AntPlus.ProductInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ProductInfo.html) or **Null**
	Retrieve product information for provided component identifier.
- [**sendManufacturerMessage**](#sendManufacturerMessage-instance_function "sendManufacturerMessage (Instance Function)") (message as [Ant.Message](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/Message.html)) as **Void**
	Send Manufacturer Message.
- [**sendPageRequest**](#sendPageRequest-instance_function "sendPageRequest (Instance Function)") (pageNumber as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Send Page request Request 2 broadcast pages from connected sensor.

## Instance Method Details

### getBatteryStatus(identifier as Lang.Number) as AntPlus.BatteryStatus or Null

Retrieve battery status for provided component identifier.

### getComponentIdentifiers() as Lang.Array<Lang.Number> or Null

Retrieve a list of known component identifiers for this Device.

This list may update over time as ANT+ devices with >1 component periodically send information about each of their components. The device reports its total number of components in [CommonData.numComponents](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/CommonData.html#numComponents-var). The returned Array will only contain entries for components that the ANT+ device has provided a component identifier for.

### getDeviceState() as AntPlus.DeviceState

Retrieve the state of the device.

### getManufacturerInfo(identifier as Lang.Number) as AntPlus.ManufacturerInfo or Null

Retrieve manufacturer information for provided component identifier.

### getProductInfo(identifier as Lang.Number) as AntPlus.ProductInfo or Null

Retrieve product information for provided component identifier.

### sendManufacturerMessage(message as Ant.Message) as Void

Send Manufacturer Message

### sendPageRequest(pageNumber as Lang.Number) as Void

Send Page request Request 2 broadcast pages from connected sensor. Use [onMessage()](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceListener.html#onMessage-instance_function) to process requested page broadcasts from the sensor.
