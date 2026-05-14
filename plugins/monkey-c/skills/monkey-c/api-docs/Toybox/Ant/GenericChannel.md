---
title: Toybox.Ant.GenericChannel
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/GenericChannel.html
---

## Class: Toybox.Ant.GenericChannel

## Overview

## Instance Method Summary

- [**close**](#close-instance_function "close (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Close a generic ANT Channel.
- [**disableEncryption**](#disableEncryption-instance_function "disableEncryption (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Disable encryption on this channel.
- [**enableEncryption**](#enableEncryption-instance_function "enableEncryption (Instance Function)") (configuration as [Ant.CryptoConfig](CryptoConfig.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Set the encryption configuration and enable encryption on this channel.
- [**getDeviceConfig**](#getDeviceConfig-instance_function "getDeviceConfig (Instance Function)") () as [Ant.DeviceConfig](DeviceConfig.md)
	Get the current ANT channel configuration.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (listener as [Lang.Method](../Lang/Method.md) (msg as [Ant.Message](Message.md)) as **Void**, channelAssignment as [Ant.ChannelAssignment](ChannelAssignment.md))
	Constructor.
- [**open**](#open-instance_function "open (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Open a generic ANT Channel.
- [**release**](#release-instance_function "release (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Release the generic ANT Channel back to the system.
- [**sendAcknowledge**](#sendAcknowledge-instance_function "sendAcknowledge (Instance Function)") (data as [Ant.Message](Message.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Send an acknowledge message.
- [**sendBroadcast**](#sendBroadcast-instance_function "sendBroadcast (Instance Function)") (data as [Ant.Message](Message.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Send a broadcast message.
- [**sendBurst**](#sendBurst-instance_function "sendBurst (Instance Function)") (burstData as [Ant.BurstPayload](BurstPayload.md)) as **Void**
	Send an [Array](../Lang/Array.md) of [Messages](Message.md) as a burst across the ANT channel.
- [**setBurstListener**](#setBurstListener-instance_function "setBurstListener (Instance Function)") (listener as [Ant.BurstListener](BurstListener.md)) as **Void**
	Set the [BurstListener](BurstListener.md) for burst events.
- [**setDeviceConfig**](#setDeviceConfig-instance_function "setDeviceConfig (Instance Function)") (configuration as [Ant.DeviceConfig](DeviceConfig.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Set the current ANT channel configuration.

## Instance Method Details

### close() as Lang.Boolean

### disableEncryption() as Lang.Boolean

### enableEncryption(configuration as Ant.CryptoConfig) as Lang.Boolean

### getDeviceConfig() as Ant.DeviceConfig

### initialize(listener as Lang.Method(msg as Ant.Message) as Void, channelAssignment as Ant.ChannelAssignment)

### open() as Lang.Boolean

Note:

Multitasking: Ant channel connection can not be changed while in inacitve mode and ant channels opened during active mode will be closed when app becomes inactive, and re-opened automatically when is active again. These state changes are denoted by calls to AppBase.onActive() and AppBase.onInactive().
