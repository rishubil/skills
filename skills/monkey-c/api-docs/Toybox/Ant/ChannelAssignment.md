---
title: Toybox.Ant.ChannelAssignment
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/ChannelAssignment.html
---

## Class: Toybox.Ant.ChannelAssignment

## Overview

A class to control the assignment of an ANT wireless channel.

## Instance Member Summary

- [**channelType**](#channelType-var "channelType (Var)") as [Ant.ChannelType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#ChannelType-module)
	Defines the type of channel.
- [**network**](#network-var "network (Var)") as [Ant.NetworkType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#NetworkType-module)
	Defines the type of network the channel should operate under.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (c as [Ant.ChannelType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#ChannelType-module), n as [Ant.NetworkType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#NetworkType-module))
	Constructor By default disables background scanning.
- [**isBackgroundScanEnabled**](#isBackgroundScanEnabled-instance_function "isBackgroundScanEnabled (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	See if background scanning is enabled for the channel assignment.
- [**setBackgroundScan**](#setBackgroundScan-instance_function "setBackgroundScan (Instance Function)") (isBackgroundScanEnabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Set background scan to be enabled or disabled.

## Instance Attribute Details

### var channelType as Ant.ChannelType

Defines the type of channel.

The channel can be defined to primarily send data (master) or receive data(slave). The channel type is set via the [CHANNEL\_TYPE\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#CHANNEL_TYPE_TX_NOT_RX-const) constant passed to the [Ant.ChannelAssignment.initialize()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/ChannelAssignment.html#initialize-instance_function) function for the `channelType` parameter.

### var network as Ant.NetworkType

Defines the type of network the channel should operate under.

The network is set via the [NETWORK\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#NETWORK_PUBLIC-const) constant passed to the [Ant.ChannelAssignment.initialize()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/ChannelAssignment.html#initialize-instance_function) function for the `network` parameter.

## Instance Method Details

### initialize(c as Ant.ChannelType, n as Ant.NetworkType)

Constructor By default disables background scanning.

### isBackgroundScanEnabled() as Lang.Boolean

See if background scanning is enabled for the channel assignment.

### setBackgroundScan(isBackgroundScanEnabled as Lang.Boolean) as Lang.Boolean

Set background scan to be enabled or disabled.

Enabling background scan can only be done on Receive Only channels.
