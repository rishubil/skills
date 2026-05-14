---
title: Toybox.WatchUi.TextArea
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextArea.html
---

## Class: Toybox.WatchUi.TextArea

## Overview

## See Also:

- [Drawable](Drawable.md)

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Draw Text to the device context ([Dc](../Graphics/Dc.md)).
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:text as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md),:color as [Graphics.ColorType](../Graphics.md#ColorType-named_type),:backgroundColor as [Graphics.ColorType](../Graphics.md#ColorType-named_type),:font as [Graphics.FontType](../Graphics.md#FontType-named_type) or [Lang.Array](../Lang/Array.md) < [Graphics.FontType](../Graphics.md#FontType-named_type) >,:justification as [Graphics.TextJustification](../Graphics.md#TextJustification-module) or [Lang.Number](../Lang/Number.md),:identifier as [Lang.Object](../Lang/Object.md),:locX as [Lang.Numeric](../Lang.md#Numeric-named_type),:locY as [Lang.Numeric](../Lang.md#Numeric-named_type),:width as [Lang.Numeric](../Lang.md#Numeric-named_type),:height as [Lang.Numeric](../Lang.md#Numeric-named_type),:visible as [Lang.Boolean](../Lang/Boolean.md) })
	Constructor.
- [**setBackgroundColor**](#setBackgroundColor-instance_function "setBackgroundColor (Instance Function)") (color as [Graphics.ColorType](../Graphics.md#ColorType-named_type)) as **Void**
	Set the background color of a Text object.
- [**setColor**](#setColor-instance_function "setColor (Instance Function)") (color as [Graphics.ColorType](../Graphics.md#ColorType-named_type)) as **Void**
	Set the color of a Text object.
- [**setFont**](#setFont-instance_function "setFont (Instance Function)") (font as [Graphics.FontType](../Graphics.md#FontType-named_type) or [Lang.Array](../Lang/Array.md) < [Graphics.FontType](../Graphics.md#FontType-named_type) >) as **Void**
	Set the font face of a Text object.
- [**setJustification**](#setJustification-instance_function "setJustification (Instance Function)") (justification as [Lang.Number](../Lang/Number.md)) as **Void**
	Set the justification of a Text object.
- [**setText**](#setText-instance_function "setText (Instance Function)") (text as [Lang.String](../Lang/String.md) or [Lang.ResourceId](../Lang/ResourceId.md)) as **Void**
	Set the text string of a Text object.
