---
title: Toybox.Graphics.BufferedBitmap
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html
---

## Class: Toybox.Graphics.BufferedBitmap

## Overview

## See Also:

- [Core Topics - Resources](https://developer.garmin.com/connect-iq/core-topics/resources/)

## Instance Method Summary

- [**getDc**](#getDc-instance_function "getDc (Instance Function)") () as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)
	Get the Dc to draw on the buffered bitmap.
- [**getHeight**](#getHeight-instance_function "getHeight (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the height of a bitmap.
- [**getPalette**](#getPalette-instance_function "getPalette (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) >
	`null` if this surface uses the system palette.
- [**getWidth**](#getWidth-instance_function "getWidth (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the width of a bitmap.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:width as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:height as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:palette as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) >,:colorDepth as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:bitmapResource as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html),:alphaBlending as [Graphics.AlphaBlending](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#AlphaBlending-module) }) deprecated
	Constructor.
- [**isCached**](#isCached-instance_function "isCached (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Check if the memory for the bitmap is still loaded in the memory User can invoke this method to check if the underlying resource is still available in the memory since last used if `true`, the resource such as [BufferedBitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html) has been cached and can be used directly without re-drawing.
- [**setPalette**](#setPalette-instance_function "setPalette (Instance Function)") (palette as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) >) as **Void**

## Instance Method Details

### getDc() as Graphics.Dc

### getHeight() as Lang.Number

### getPalette() as Lang.Array<Graphics.ColorType>

### getWidth() as Lang.Number

### initialize(options as {:width as Lang.Number,:height as Lang.Number,:palette as Lang.Array<Graphics.ColorType>,:colorDepth as Lang.Number,:bitmapResource as WatchUi.BitmapResource,:alphaBlending as Graphics.AlphaBlending })

**This has been deprecated**

Use [Graphics.createBufferedBitmap()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#createBufferedBitmap-instance_function) after ConnectIQ version 4.0.0.
