---
title: Toybox.AntPlus.LightNetwork
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/LightNetwork.html
---

## Class: Toybox.AntPlus.LightNetwork

## Overview

A class representing a network of bike lights

## Instance Method Summary

- [**getBikeLights**](#getBikeLights-instance_function "getBikeLights (Instance Function)") () as [Lang.Array](../Lang/Array.md) < [AntPlus.LightNetworkState](../AntPlus.md#LightNetworkState-module) > or **Null**
	Get a list of lights in the network.
- [**getNetworkMode**](#getNetworkMode-instance_function "getNetworkMode (Instance Function)") () as [AntPlus.LightNetworkMode](../AntPlus.md#LightNetworkMode-module)
	Get the light network mode.
- [**getNetworkState**](#getNetworkState-instance_function "getNetworkState (Instance Function)") () as [AntPlus.LightNetworkState](../AntPlus.md#LightNetworkState-module)
	Get the light network state.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (listener as [AntPlus.LightNetworkListener](LightNetworkListener.md) or **Null**)
	Constructor.
- [**restoreHeadlightsNetworkModeControl**](#restoreHeadlightsNetworkModeControl-instance_function "restoreHeadlightsNetworkModeControl (Instance Function)") () as **Void**
	Bring all headlights under the control of whichever light network mode has been chosen by the user.
- [**restoreTaillightsNetworkModeControl**](#restoreTaillightsNetworkModeControl-instance_function "restoreTaillightsNetworkModeControl (Instance Function)") () as **Void**
	Bring all taillights under the control of whichever light network mode has been chosen by the user.
- [**setHeadlightsMode**](#setHeadlightsMode-instance_function "setHeadlightsMode (Instance Function)") (mode as [AntPlus.LightMode](../AntPlus.md#LightMode-module)) as **Void**
	Tell all headlights to enter the same mode.
- [**setTaillightsMode**](#setTaillightsMode-instance_function "setTaillightsMode (Instance Function)") (mode as [AntPlus.LightMode](../AntPlus.md#LightMode-module)) as **Void**
	Tell all taillights to enter the same mode.
- [**toggleSignalLight**](#toggleSignalLight-instance_function "toggleSignalLight (Instance Function)") (left as [Lang.Boolean](../Lang/Boolean.md)) as **Void**
	A signal switch for right and left signals.

## Instance Method Details

### getBikeLights() as Lang.Array<AntPlus.LightNetworkState> or Null

Get a list of lights in the network.

### getNetworkMode() as AntPlus.LightNetworkMode

Get the light network mode.

### getNetworkState() as AntPlus.LightNetworkState

Get the light network state.

### initialize(listener as AntPlus.LightNetworkListener or Null)

Constructor

### restoreHeadlightsNetworkModeControl() as Void

Bring all headlights under the control of whichever light network mode has been chosen by the user.

### restoreTaillightsNetworkModeControl() as Void

Bring all taillights under the control of whichever light network mode has been chosen by the user.

### setHeadlightsMode(mode as AntPlus.LightMode) as Void

Tell all headlights to enter the same mode.

You should check the capable modes of each headlight in the network before sending light modes, as lights will ignore commands to go into modes that they do not support. Lights whose modes are set here will not be controlled by the Light Network Mode until they are restored OR until the user changes the Light Network Mode outside of ConnectIQ.

### setTaillightsMode(mode as AntPlus.LightMode) as Void

Tell all taillights to enter the same mode.

You should check the capable modes of each taillight in the network before sending light modes, as lights will ignore commands to go into modes that they do not support. Lights whose modes are set here will not be controlled by the Light Network Mode until they are restored OR until the user changes the Light Network Mode outside of ConnectIQ.

### toggleSignalLight(left as Lang.Boolean) as Void

A signal switch for right and left signals.

- If signal light is engaged, disengage it.
- If signal light is disengaged, engage it.

\*This will automatically disengage the opposite signal if it is currently engaged.
