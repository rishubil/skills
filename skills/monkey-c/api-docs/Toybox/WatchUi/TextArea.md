---
title: Toybox.WatchUi.TextArea
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextArea.html
---

## Class: Toybox.WatchUi.TextArea

## Overview

## See Also:

- [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html)

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Draw Text to the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)).
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:color as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type),:backgroundColor as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type),:font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type) >,:justification as [Graphics.TextJustification](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#TextJustification-module) or [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html),:locX as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:locY as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:visible as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) })
	Constructor.
- [**setBackgroundColor**](#setBackgroundColor-instance_function "setBackgroundColor (Instance Function)") (color as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type)) as **Void**
	Set the background color of a Text object.
- [**setColor**](#setColor-instance_function "setColor (Instance Function)") (color as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type)) as **Void**
	Set the color of a Text object.
- [**setFont**](#setFont-instance_function "setFont (Instance Function)") (font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type) >) as **Void**
	Set the font face of a Text object.
- [**setJustification**](#setJustification-instance_function "setJustification (Instance Function)") (justification as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Set the justification of a Text object.
- [**setText**](#setText-instance_function "setText (Instance Function)") (text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html)) as **Void**
	Set the text string of a Text object.
