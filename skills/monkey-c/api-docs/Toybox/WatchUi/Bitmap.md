---
title: Toybox.WatchUi.Bitmap
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Bitmap.html
---

## Class: Toybox.WatchUi.Bitmap

## Overview

## See Also:

- [Toybox.WatchUi.Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html)

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)) as **Void**
	Draw a Bitmap to the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)).
- [**getDimensions**](#getDimensions-instance_function "getDimensions (Instance Function)") () as \[ [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type) \]
	Get the dimensions of a Bitmap.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:rezId as [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:bitmap as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type),:identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html),:locX as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:locY as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:visible as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) })
	Constructor.
- [**setBitmap**](#setBitmap-instance_function "setBitmap (Instance Function)") (bitmap as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or **Null**) as **Void**
	Set the resource associated with the Bitmap.

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

### getDimensions() as \[ Lang.Numeric, Lang.Numeric \]

### initialize(options as {:rezId as Lang.ResourceId,:bitmap as Graphics.BitmapType,:identifier as Lang.Object,:locX as Lang.Numeric,:locY as Lang.Numeric,:width as Lang.Numeric,:height as Lang.Numeric,:visible as Lang.Boolean })

### setBitmap(bitmap as Graphics.BitmapType or Lang.ResourceId or Null) as Void

Note:

A `null` value passed for the bitmap parameter is only supported with ConnectIQ 5.0.0 and later.
