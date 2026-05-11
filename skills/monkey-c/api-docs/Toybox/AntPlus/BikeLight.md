---
title: Toybox.AntPlus.BikeLight
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeLight.html
---

## Class: Toybox.AntPlus.BikeLight

## Overview

A class representing a bike light sensor.

## Instance Member Summary

- [**mode**](#mode-var "mode (Var)") as [AntPlus.LightMode](../AntPlus.md#LightMode-module)
	The [LIGHT\_MODE\_\*](../AntPlus.md#LIGHT_MODE_AUTO-const) mode of the light.
- [**type**](#type-var "type (Var)") as [AntPlus.LightType](../AntPlus.md#LightType-module)
	The [LIGHT\_TYPE\_\*](../AntPlus.md#LIGHT_TYPE_HEADLIGHT-const) type of the light.

## Instance Method Summary

- [**getCapableModes**](#getCapableModes-instance_function "getCapableModes (Instance Function)") () as [Lang.Array](../Lang/Array.md) < [AntPlus.LightMode](../AntPlus.md#LightMode-module) > or **Null**
	Get a list of the standard and custom light modes that a bike light supports.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**setMode**](#setMode-instance_function "setMode (Instance Function)") (mode as [AntPlus.LightMode](../AntPlus.md#LightMode-module)) as **Void**
	Tell this light to enter a new mode.

## Instance Attribute Details

### var mode as AntPlus.LightMode

The [LIGHT\_MODE\_\*](../AntPlus.md#LIGHT_MODE_AUTO-const) mode of the light.

### var type as AntPlus.LightType

The [LIGHT\_TYPE\_\*](../AntPlus.md#LIGHT_TYPE_HEADLIGHT-const) type of the light.

## Instance Method Details

### getCapableModes() as Lang.Array<AntPlus.LightMode> or Null

Get a list of the standard and custom light modes that a bike light supports.

### initialize()

Constructor

### setMode(mode as AntPlus.LightMode) as Void

Tell this light to enter a new mode.

You should check the capable modes before sending light modes as lights will ignore commands to go into modes that they do not support. Lights whose modes are set here will not be controlled by the Light Network Mode until they are restored OR until the user changes the Light Network Mode outside of ConnectIQ.
