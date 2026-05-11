---
title: Toybox.Ant.DeviceConfig
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/DeviceConfig.html
---

## Class: Toybox.Ant.DeviceConfig

## Overview

## See Also:

- [ANT Downloads & Resources - ANT Message Protocol](https://www.thisisant.com/developer/resources/downloads/)
- [Toybox.AntPlus](../AntPlus.md)

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | DEFAULT\_DEVICE\_NUMBER | 123 | API Level 1.0.0 | The default values for a device configuration |
| Type | DEFAULT\_DEVICE\_TYPE | 1 | API Level 1.0.0 |  |
| Type | DEFAULT\_MESSAGE\_PERIOD | 8192 | API Level 1.0.0 |  |
| Type | DEFAULT\_NETWORK\_KEY | 0 | API Level 1.2.0 |  |
| Type | DEFAULT\_RADIO\_FREQUENCY | 10 | API Level 1.0.0 |  |
| Type | DEFAULT\_THRESHOLD | 0 | API Level 1.0.0 |  |
| Type | DEFAULT\_TRANSMISSION\_TYPE | 0 | API Level 1.0.0 |  |
| Type | NETWORK\_KEY\_LENGTH\_128BIT | 16 | API Level 1.2.0 |  |
| Type | NETWORK\_KEY\_LENGTH\_64BIT | 8 | API Level 1.2.0 | Network key lengths |

## Typedef Summary

- [**NetworkKey128Bit**](#NetworkKey128Bit-named_type "NetworkKey128Bit (Named Type)") as \[ [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md) \]
- [**NetworkKey64Bit**](#NetworkKey64Bit-named_type "NetworkKey64Bit (Named Type)") as \[ [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md) \]

## Instance Member Summary

- [**deviceNumber**](#deviceNumber-var "deviceNumber (Var)") as [Lang.Number](../Lang/Number.md)
	The unique device number (ANT-id).
- [**deviceType**](#deviceType-var "deviceType (Var)") as [Lang.Number](../Lang/Number.md)
	A 1-Byte device type identifier.
- [**messagePeriod**](#messagePeriod-var "messagePeriod (Var)") as [Lang.Number](../Lang/Number.md)
	The Message period that the sensor uses.
- [**networkKey128Bit**](#networkKey128Bit-var "networkKey128Bit (Var)") as [DeviceConfig.NetworkKey128Bit](DeviceConfig.md#NetworkKey128Bit-named_type) or **Null**
	A 128 bit network key.
- [**networkKey64Bit**](#networkKey64Bit-var "networkKey64Bit (Var)") as [DeviceConfig.NetworkKey64Bit](DeviceConfig.md#NetworkKey64Bit-named_type) or **Null**
	A 64 bit network key.
- [**radioFrequency**](#radioFrequency-var "radioFrequency (Var)") as [Lang.Number](../Lang/Number.md)
	The radio frequency that the sensor operates on.
- [**searchThreshold**](#searchThreshold-var "searchThreshold (Var)") as [Lang.Number](../Lang/Number.md)
	The proximity threshold bin.
- [**searchTimeoutHighPriority**](#searchTimeoutHighPriority-var "searchTimeoutHighPriority (Var)") as [Lang.Number](../Lang/Number.md)
	High Priority search timeout that a receiving channel will wait for in order to start tracking a master \* Measured in 2.5s increments \* Limited to a maximum of 5 seconds (Range of 0 to 2).
- [**searchTimeoutLowPriority**](#searchTimeoutLowPriority-var "searchTimeoutLowPriority (Var)") as [Lang.Number](../Lang/Number.md)
	The low Priority search timeout that a receiving channel will wait for in order to start tracking a master \* Measured in 2.5s increments \* Limited to a maximum of 30 seconds (Range of 0 to 12).
- [**transmissionType**](#transmissionType-var "transmissionType (Var)") as [Lang.Number](../Lang/Number.md)
	The manufacturer-specific transport type and extended device number.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:deviceNumber as [Lang.Number](../Lang/Number.md),:deviceType as [Lang.Number](../Lang/Number.md),:transmissionType as [Lang.Number](../Lang/Number.md),:messagePeriod as [Lang.Number](../Lang/Number.md),:radioFrequency as [Lang.Number](../Lang/Number.md),:searchTimeoutLowPriority as [Lang.Number](../Lang/Number.md),:searchTimeoutHighPriority as [Lang.Number](../Lang/Number.md),:searchThreshold as [Lang.Number](../Lang/Number.md),:networkKey64Bit as [DeviceConfig.NetworkKey64Bit](DeviceConfig.md#NetworkKey64Bit-named_type),:networkKey128Bit as [DeviceConfig.NetworkKey128Bit](DeviceConfig.md#NetworkKey128Bit-named_type) })
	Constructor.
