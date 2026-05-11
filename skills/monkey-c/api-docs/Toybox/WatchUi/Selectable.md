---
title: Toybox.WatchUi.Selectable
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html
---

## Class: Toybox.WatchUi.Selectable

## Overview

A representation of an on-screen selectable object with defined states depending on selection mode.

## See Also:

- [Toybox.WatchUi.Drawable](Drawable.md)
Note:

See the Selectable sample distributed with the SDK for an example of the use of the Selectable class

## Direct Known Subclasses

[WatchUi.Button](Button.md)

## Instance Member Summary

- [**stateDefault**](#stateDefault-var "stateDefault (Var)") as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md) or **Null**
	The default state of a Selectable object.
- [**stateDisabled**](#stateDisabled-var "stateDisabled (Var)") as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md) or **Null**
	The disabled state of a Selectable object.
- [**stateHighlighted**](#stateHighlighted-var "stateHighlighted (Var)") as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md) or **Null**
	The highlighted state of a Selectable object.
- [**stateSelected**](#stateSelected-var "stateSelected (Var)") as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md) or **Null**
	The selected state of a Selectable object.

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Draw the Selectable to the device context ([Dc](../Graphics/Dc.md)).
- [**getState**](#getState-instance_function "getState (Instance Function)") () as [Lang.Symbol](../Lang/Symbol.md)
	Get the current state of a Selectable object.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:locX as [Lang.Numeric](../Lang.md#Numeric-named_type),:locY as [Lang.Numeric](../Lang.md#Numeric-named_type),:width as [Lang.Numeric](../Lang.md#Numeric-named_type),:height as [Lang.Numeric](../Lang.md#Numeric-named_type),:stateDefault as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md),:stateHighlighted as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md),:stateSelected as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md),:stateDisabled as [Graphics.ColorType](../Graphics.md#ColorType-named_type) or [WatchUi.Drawable](Drawable.md),:identifier as [Lang.Object](../Lang/Object.md),:visible as [Lang.Boolean](../Lang/Boolean.md) })
	Constructor.
- [**setState**](#setState-instance_function "setState (Instance Function)") (state as [Lang.Symbol](../Lang/Symbol.md)) as **Void**
	Set the current state of a Selectable object.

## Instance Attribute Details

### var stateDefault as Graphics.ColorType or WatchUi.Drawable or Null

The default state of a Selectable object.

A [Drawable](Drawable.md), [Graphics.COLOR\_\*](../Graphics.md#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the default state of the Selectable

### var stateDisabled as Graphics.ColorType or WatchUi.Drawable or Null

The disabled state of a Selectable object.

A [Drawable](Drawable.md), [Graphics.COLOR\_\*](../Graphics.md#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the disabled state of the Selectable

### var stateHighlighted as Graphics.ColorType or WatchUi.Drawable or Null

The highlighted state of a Selectable object.

A [Drawable](Drawable.md), [Graphics.COLOR\_\*](../Graphics.md#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the highlighted state of the Selectable

### var stateSelected as Graphics.ColorType or WatchUi.Drawable or Null

The selected state of a Selectable object.

A [Drawable](Drawable.md), [Graphics.COLOR\_\*](../Graphics.md#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the selected state of the Selectable

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

Draw the Selectable to the device context ([Dc](../Graphics/Dc.md)).

This method assumes that the device context has already been configured to the proper options.

### getState() as Lang.Symbol

Get the current state of a Selectable object.

### initialize(options as {:locX as Lang.Numeric,:locY as Lang.Numeric,:width as Lang.Numeric,:height as Lang.Numeric,:stateDefault as Graphics.ColorType or WatchUi.Drawable,:stateHighlighted as Graphics.ColorType or WatchUi.Drawable,:stateSelected as Graphics.ColorType or WatchUi.Drawable,:stateDisabled as Graphics.ColorType or WatchUi.Drawable,:identifier as Lang.Object,:visible as Lang.Boolean })

Constructor

### setState(state as Lang.Symbol) as Void

Set the current state of a Selectable object.
