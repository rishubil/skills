---
title: Toybox.Ant.DeviceConfig
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/DeviceConfig.html
---

## Class: Toybox.Ant.DeviceConfig

## Overview

## See Also:

- [ANT Downloads & Resources - ANT Message Protocol](https://www.thisisant.com/developer/resources/downloads/)
- [Toybox.AntPlus](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html)

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

- [**NetworkKey128Bit**](#NetworkKey128Bit-named_type "NetworkKey128Bit (Named Type)") as \[ [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) \]
- [**NetworkKey64Bit**](#NetworkKey64Bit-named_type "NetworkKey64Bit (Named Type)") as \[ [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) \]

## Instance Member Summary

- [**deviceNumber**](#deviceNumber-var "deviceNumber (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The unique device number (ANT-id).
- [**deviceType**](#deviceType-var "deviceType (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	A 1-Byte device type identifier.
- [**messagePeriod**](#messagePeriod-var "messagePeriod (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The Message period that the sensor uses.
- [**networkKey128Bit**](#networkKey128Bit-var "networkKey128Bit (Var)") as [DeviceConfig.NetworkKey128Bit](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/DeviceConfig.html#NetworkKey128Bit-named_type) or **Null**
	A 128 bit network key.
- [**networkKey64Bit**](#networkKey64Bit-var "networkKey64Bit (Var)") as [DeviceConfig.NetworkKey64Bit](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/DeviceConfig.html#NetworkKey64Bit-named_type) or **Null**
	A 64 bit network key.
- [**radioFrequency**](#radioFrequency-var "radioFrequency (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The radio frequency that the sensor operates on.
- [**searchThreshold**](#searchThreshold-var "searchThreshold (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The proximity threshold bin.
- [**searchTimeoutHighPriority**](#searchTimeoutHighPriority-var "searchTimeoutHighPriority (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	High Priority search timeout that a receiving channel will wait for in order to start tracking a master \* Measured in 2.5s increments \* Limited to a maximum of 5 seconds (Range of 0 to 2).
- [**searchTimeoutLowPriority**](#searchTimeoutLowPriority-var "searchTimeoutLowPriority (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The low Priority search timeout that a receiving channel will wait for in order to start tracking a master \* Measured in 2.5s increments \* Limited to a maximum of 30 seconds (Range of 0 to 12).
- [**transmissionType**](#transmissionType-var "transmissionType (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The manufacturer-specific transport type and extended device number.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:deviceNumber as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:deviceType as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:transmissionType as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:messagePeriod as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:radioFrequency as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:searchTimeoutLowPriority as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:searchTimeoutHighPriority as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:searchThreshold as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:networkKey64Bit as [DeviceConfig.NetworkKey64Bit](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/DeviceConfig.html#NetworkKey64Bit-named_type),:networkKey128Bit as [DeviceConfig.NetworkKey128Bit](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/DeviceConfig.html#NetworkKey128Bit-named_type) })
	Constructor.
