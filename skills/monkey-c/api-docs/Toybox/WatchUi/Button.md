---
title: Toybox.WatchUi.Button
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Button.html
---

## Class: Toybox.WatchUi.Button

## Overview

A representation of a Selectable button.

Button objects are mappable to a BehaviorDelegate method on selection.

## See Also:

- [Toybox.WatchUi.Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html)
Note:

See the Selectable sample distributed with the SDK for an example of the use of the Button class

## Instance Member Summary

- [**background**](#background-var "background (Var)") as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html) or **Null**
	The Button background A [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), [Graphics.COLOR\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#COLOR_WHITE-const) value, or 24-bit integer of the form 0xRRGGBB to be drawn before the current Selectable state is drawn.
- [**behavior**](#behavior-var "behavior (Var)") as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html) or **Null**
	A Symbol describing the behavior method executed when button is selected.

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Draw the Button to the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)).
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:behavior as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html),:background as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:locX as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:locY as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:stateDefault as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:stateHighlighted as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:stateSelected as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:stateDisabled as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or [WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html),:identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html),:visible as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) })
	Constructor Initializes a Button object's foreground, background, and behavior.

## Instance Attribute Details

### var background as Graphics.ColorType or WatchUi.Drawable or Null

The Button background

A [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), [Graphics.COLOR\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#COLOR_WHITE-const) value, or 24-bit integer of the form 0xRRGGBB to be drawn before the current Selectable state is drawn.

### var behavior as Lang.Symbol or Null

A Symbol describing the behavior method executed when button is selected.

This Symbol must be a member of the active View object's registered BehaviorDelegate, such as:onBack, but may also be a Symbol from an extended class. If the value is `null`, then a [SelectableEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SelectableEvent.html) will be issued.

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

Draw the Button to the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)).

This method assumes that the device context has already been configured to the proper options.

### initialize(options as {:behavior as Lang.Symbol,:background as Graphics.ColorType or WatchUi.Drawable,:locX as Lang.Numeric,:locY as Lang.Numeric,:width as Lang.Numeric,:height as Lang.Numeric,:stateDefault as Graphics.ColorType or WatchUi.Drawable,:stateHighlighted as Graphics.ColorType or WatchUi.Drawable,:stateSelected as Graphics.ColorType or WatchUi.Drawable,:stateDisabled as Graphics.ColorType or WatchUi.Drawable,:identifier as Lang.Object,:visible as Lang.Boolean })

Constructor Initializes a Button object's foreground, background, and behavior. The Button must be registered during [setLayout()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#setLayout-instance_function) in order to be usable.
