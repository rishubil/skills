---
title: Toybox.WatchUi.Bitmap
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Bitmap.html
---

## Class: Toybox.WatchUi.Bitmap

## Overview

## See Also:

- [Toybox.WatchUi.Drawable](Drawable.md)

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Draw a Bitmap to the device context ([Dc](../Graphics/Dc.md)).
- [**getDimensions**](#getDimensions-instance_function "getDimensions (Instance Function)") () as \[ [Lang.Numeric](../Lang.md#Numeric-named_type), [Lang.Numeric](../Lang.md#Numeric-named_type) \]
	Get the dimensions of a Bitmap.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:rezId as [Lang.ResourceId](../Lang/ResourceId.md),:bitmap as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type),:identifier as [Lang.Object](../Lang/Object.md),:locX as [Lang.Numeric](../Lang.md#Numeric-named_type),:locY as [Lang.Numeric](../Lang.md#Numeric-named_type),:width as [Lang.Numeric](../Lang.md#Numeric-named_type),:height as [Lang.Numeric](../Lang.md#Numeric-named_type),:visible as [Lang.Boolean](../Lang/Boolean.md) })
	Constructor.
- [**setBitmap**](#setBitmap-instance_function "setBitmap (Instance Function)") (bitmap as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [Lang.ResourceId](../Lang/ResourceId.md) or **Null**) as **Void**
	Set the resource associated with the Bitmap.

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

### getDimensions() as \[ Lang.Numeric, Lang.Numeric \]

### initialize(options as {:rezId as Lang.ResourceId,:bitmap as Graphics.BitmapType,:identifier as Lang.Object,:locX as Lang.Numeric,:locY as Lang.Numeric,:width as Lang.Numeric,:height as Lang.Numeric,:visible as Lang.Boolean })

### setBitmap(bitmap as Graphics.BitmapType or Lang.ResourceId or Null) as Void

Note:

A `null` value passed for the bitmap parameter is only supported with ConnectIQ 5.0.0 and later.
