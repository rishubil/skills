---
title: Toybox.WatchUi.Selectable
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html
---

## Class: Toybox.WatchUi.Selectable

## Overview

A representation of an on-screen selectable object with defined states depending on selection mode.

## See Also:

- [Toybox.WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html)
Note:

See the Selectable sample distributed with the SDK for an example of the use of the Selectable class

## Direct Known Subclasses

[WatchUi.Button](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Button.html)

## Instance Member Summary

- [**stateDefault**](#stateDefault-var "stateDefault (Var)") as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	The default state of a Selectable object.
- [**stateDisabled**](#stateDisabled-var "stateDisabled (Var)") as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	The disabled state of a Selectable object.
- [**stateHighlighted**](#stateHighlighted-var "stateHighlighted (Var)") as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	The highlighted state of a Selectable object.
- [**stateSelected**](#stateSelected-var "stateSelected (Var)") as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	The selected state of a Selectable object.

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Draw the Selectable to the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)).
- [**getState**](#getState-instance_function "getState (Instance Function)") () as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html)
	Get the current state of a Selectable object.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:locX as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:locY as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:stateDefault as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:stateHighlighted as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:stateSelected as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:stateDisabled as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html),:visible as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) })
	Constructor.
- [**setState**](#setState-instance_function "setState (Instance Function)") (state as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html)) as **Void**
	Set the current state of a Selectable object.

## Instance Attribute Details

### var stateDefault as Graphics.ColorType or WatchUi.Drawable or Null

The default state of a Selectable object.

A [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), [Graphics.COLOR\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the default state of the Selectable

### var stateDisabled as Graphics.ColorType or WatchUi.Drawable or Null

The disabled state of a Selectable object.

A [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), [Graphics.COLOR\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the disabled state of the Selectable

### var stateHighlighted as Graphics.ColorType or WatchUi.Drawable or Null

The highlighted state of a Selectable object.

A [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), [Graphics.COLOR\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the highlighted state of the Selectable

### var stateSelected as Graphics.ColorType or WatchUi.Drawable or Null

The selected state of a Selectable object.

A [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), [Graphics.COLOR\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#COLOR_WHITE-const) constant, or 24-bit integer of the form 0xRRGGBB representing the selected state of the Selectable

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

Draw the Selectable to the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)).

This method assumes that the device context has already been configured to the proper options.

### getState() as Lang.Symbol

Get the current state of a Selectable object.

### initialize(options as {:locX as Lang.Numeric,:locY as Lang.Numeric,:width as Lang.Numeric,:height as Lang.Numeric,:stateDefault as Graphics.ColorType or WatchUi.Drawable,:stateHighlighted as Graphics.ColorType or WatchUi.Drawable,:stateSelected as Graphics.ColorType or WatchUi.Drawable,:stateDisabled as Graphics.ColorType or WatchUi.Drawable,:identifier as Lang.Object,:visible as Lang.Boolean })

Constructor

### setState(state as Lang.Symbol) as Void

Set the current state of a Selectable object.
