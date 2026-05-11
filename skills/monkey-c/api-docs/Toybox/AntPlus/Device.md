---
title: Toybox.AntPlus.Device
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/Device.html
---

## Class: Toybox.AntPlus.Device

## Overview

The Device object represents an ANT+ Device instance.

## Direct Known Subclasses

[AntPlus.BikeCadence](BikeCadence.md), [AntPlus.BikePower](BikePower.md), [AntPlus.BikeRadar](BikeRadar.md), [AntPlus.BikeSpeed](BikeSpeed.md), [AntPlus.BikeSpeedCadence](BikeSpeedCadence.md), [AntPlus.FitnessEquipment](FitnessEquipment.md), [AntPlus.LightNetwork](LightNetwork.md), [AntPlus.RunningDynamics](RunningDynamics.md), [AntPlus.Shifting](Shifting.md)

## Instance Method Summary

- [**getBatteryStatus**](#getBatteryStatus-instance_function "getBatteryStatus (Instance Function)") (identifier as [Lang.Number](../Lang/Number.md)) as [AntPlus.BatteryStatus](BatteryStatus.md) or **Null**
	Retrieve battery status for provided component identifier.
- [**getComponentIdentifiers**](#getComponentIdentifiers-instance_function "getComponentIdentifiers (Instance Function)") () as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	Retrieve a list of known component identifiers for this Device.
- [**getDeviceState**](#getDeviceState-instance_function "getDeviceState (Instance Function)") () as [AntPlus.DeviceState](DeviceState.md)
	Retrieve the state of the device.
- [**getManufacturerInfo**](#getManufacturerInfo-instance_function "getManufacturerInfo (Instance Function)") (identifier as [Lang.Number](../Lang/Number.md)) as [AntPlus.ManufacturerInfo](ManufacturerInfo.md) or **Null**
	Retrieve manufacturer information for provided component identifier.
- [**getProductInfo**](#getProductInfo-instance_function "getProductInfo (Instance Function)") (identifier as [Lang.Number](../Lang/Number.md)) as [AntPlus.ProductInfo](ProductInfo.md) or **Null**
	Retrieve product information for provided component identifier.
- [**sendManufacturerMessage**](#sendManufacturerMessage-instance_function "sendManufacturerMessage (Instance Function)") (message as [Ant.Message](../Ant/Message.md)) as **Void**
	Send Manufacturer Message.
- [**sendPageRequest**](#sendPageRequest-instance_function "sendPageRequest (Instance Function)") (pageNumber as [Lang.Number](../Lang/Number.md)) as **Void**
	Send Page request Request 2 broadcast pages from connected sensor.

## Instance Method Details

### getBatteryStatus(identifier as Lang.Number) as AntPlus.BatteryStatus or Null

Retrieve battery status for provided component identifier.

### getComponentIdentifiers() as Lang.Array<Lang.Number> or Null

Retrieve a list of known component identifiers for this Device.

This list may update over time as ANT+ devices with >1 component periodically send information about each of their components. The device reports its total number of components in [CommonData.numComponents](CommonData.md#numComponents-var). The returned Array will only contain entries for components that the ANT+ device has provided a component identifier for.

### getDeviceState() as AntPlus.DeviceState

Retrieve the state of the device.

### getManufacturerInfo(identifier as Lang.Number) as AntPlus.ManufacturerInfo or Null

Retrieve manufacturer information for provided component identifier.

### getProductInfo(identifier as Lang.Number) as AntPlus.ProductInfo or Null

Retrieve product information for provided component identifier.

### sendManufacturerMessage(message as Ant.Message) as Void

Send Manufacturer Message

### sendPageRequest(pageNumber as Lang.Number) as Void

Send Page request Request 2 broadcast pages from connected sensor. Use [onMessage()](DeviceListener.md#onMessage-instance_function) to process requested page broadcasts from the sensor.
