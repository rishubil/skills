---
title: Toybox.Ant.Message
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/Message.html
---

## Class: Toybox.Ant.Message

## Overview

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | DATA\_PAYLOAD\_LENGTH | 8 | API Level 1.0.0 |  |

## Instance Member Summary

- [**deviceNumber**](#deviceNumber-var "deviceNumber (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The Unique device number (ANT-id).
- [**deviceType**](#deviceType-var "deviceType (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	A 1-Byte device type identifier.
- [**length**](#length-var "length (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Number of data bytes in the data payload (not including any extended data if applicable).
- [**messageId**](#messageId-var "messageId (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The Data Type Identifier.
- [**rssi**](#rssi-var "rssi (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The Received Signal Strength Indication.
- [**timestamp**](#timestamp-var "timestamp (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The time stamp of received message generated off of a 32.768 kHz clock.
- [**transmissionType**](#transmissionType-var "transmissionType (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The manufacturer-specific transport type and extended device number.

## Instance Method Summary

- [**getPayload**](#getPayload-instance_function "getPayload (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >
	Get the ANT data packet.
- [**setPayload**](#setPayload-instance_function "setPayload (Instance Function)") (data as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >) as **Void**
	Set the ANT data packet.
