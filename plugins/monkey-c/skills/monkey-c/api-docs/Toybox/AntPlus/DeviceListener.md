---
title: Toybox.AntPlus.DeviceListener
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DeviceListener.html
---

## Class: Toybox.AntPlus.DeviceListener

## Overview

## Direct Known Subclasses

[AntPlus.BikeCadenceListener](BikeCadenceListener.md), [AntPlus.BikePowerListener](BikePowerListener.md), [AntPlus.BikeRadarListener](BikeRadarListener.md), [AntPlus.BikeSpeedCadenceListener](BikeSpeedCadenceListener.md), [AntPlus.BikeSpeedListener](BikeSpeedListener.md), [AntPlus.FitnessEquipmentListener](FitnessEquipmentListener.md), [AntPlus.LightNetworkListener](LightNetworkListener.md), [AntPlus.RunningDynamicsListener](RunningDynamicsListener.md), [AntPlus.ShiftingListener](ShiftingListener.md)

## Instance Method Summary

- [**onBatteryStatusUpdate**](#onBatteryStatusUpdate-instance_function "onBatteryStatusUpdate (Instance Function)") (data as [AntPlus.BatteryStatus](BatteryStatus.md)) as **Void**
	Callback when battery status is received.
- [**onDeviceStateUpdate**](#onDeviceStateUpdate-instance_function "onDeviceStateUpdate (Instance Function)") (data as [AntPlus.DeviceState](DeviceState.md)) as **Void**
	Callback when device state is updated.
- [**onManufacturerInfoUpdate**](#onManufacturerInfoUpdate-instance_function "onManufacturerInfoUpdate (Instance Function)") (data as [AntPlus.ManufacturerInfo](ManufacturerInfo.md)) as **Void**
	Callback when manufacturer's information is received.
- [**onMessage**](#onMessage-instance_function "onMessage (Instance Function)") (msg as [Ant.Message](../Ant/Message.md)) as **Void**
	Callback when ANT message is received.
- [**onProductInfoUpdate**](#onProductInfoUpdate-instance_function "onProductInfoUpdate (Instance Function)") (data as [AntPlus.ProductInfo](ProductInfo.md)) as **Void**
	Callback when product information is received.
- [**onSentMessage**](#onSentMessage-instance_function "onSentMessage (Instance Function)") (status as [AntPlus.MessageSendStatus](../AntPlus.md#MessageSendStatus-module), sentMesgData as {:messageType as [AntPlus.MessageType](../AntPlus.md#MessageType-module),:pageNumber as [Lang.Number](../Lang/Number.md) }) as **Void**
	After sending a manufacturer message or page request this will be called to indicate message sent status.
