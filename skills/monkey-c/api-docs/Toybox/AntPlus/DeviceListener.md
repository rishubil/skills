---
title: Toybox.AntPlus.DeviceListener
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceListener.html
---

## Class: Toybox.AntPlus.DeviceListener

## Overview

## Direct Known Subclasses

[AntPlus.BikeCadenceListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeCadenceListener.html), [AntPlus.BikePowerListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikePowerListener.html), [AntPlus.BikeRadarListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeRadarListener.html), [AntPlus.BikeSpeedCadenceListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeSpeedCadenceListener.html), [AntPlus.BikeSpeedListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeSpeedListener.html), [AntPlus.FitnessEquipmentListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/FitnessEquipmentListener.html), [AntPlus.LightNetworkListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/LightNetworkListener.html), [AntPlus.RunningDynamicsListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamicsListener.html), [AntPlus.ShiftingListener](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ShiftingListener.html)

## Instance Method Summary

- [**onBatteryStatusUpdate**](#onBatteryStatusUpdate-instance_function "onBatteryStatusUpdate (Instance Function)") (data as [AntPlus.BatteryStatus](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BatteryStatus.html)) as **Void**
	Callback when battery status is received.
- [**onDeviceStateUpdate**](#onDeviceStateUpdate-instance_function "onDeviceStateUpdate (Instance Function)") (data as [AntPlus.DeviceState](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceState.html)) as **Void**
	Callback when device state is updated.
- [**onManufacturerInfoUpdate**](#onManufacturerInfoUpdate-instance_function "onManufacturerInfoUpdate (Instance Function)") (data as [AntPlus.ManufacturerInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ManufacturerInfo.html)) as **Void**
	Callback when manufacturer's information is received.
- [**onMessage**](#onMessage-instance_function "onMessage (Instance Function)") (msg as [Ant.Message](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/Message.html)) as **Void**
	Callback when ANT message is received.
- [**onProductInfoUpdate**](#onProductInfoUpdate-instance_function "onProductInfoUpdate (Instance Function)") (data as [AntPlus.ProductInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ProductInfo.html)) as **Void**
	Callback when product information is received.
- [**onSentMessage**](#onSentMessage-instance_function "onSentMessage (Instance Function)") (status as [AntPlus.MessageSendStatus](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html#MessageSendStatus-module), sentMesgData as {:messageType as [AntPlus.MessageType](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html#MessageType-module),:pageNumber as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) }) as **Void**
	After sending a manufacturer message or page request this will be called to indicate message sent status.
