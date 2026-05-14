---
title: Toybox.Graphics.BufferedBitmap
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html
---

## Class: Toybox.Graphics.BufferedBitmap

## Overview

## See Also:

- [Core Topics - Resources](https://developer.garmin.com/connect-iq/core-topics/resources/)

## Instance Method Summary

- [**getDc**](#getDc-instance_function "getDc (Instance Function)") () as [Graphics.Dc](Dc.md)
	Get the Dc to draw on the buffered bitmap.
- [**getHeight**](#getHeight-instance_function "getHeight (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the height of a bitmap.
- [**getPalette**](#getPalette-instance_function "getPalette (Instance Function)") () as [Lang.Array](../Lang/Array.md) < [Graphics.ColorType](../Graphics.md#ColorType-named_type) >
	`null` if this surface uses the system palette.
- [**getWidth**](#getWidth-instance_function "getWidth (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Get the width of a bitmap.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:width as [Lang.Number](../Lang/Number.md),:height as [Lang.Number](../Lang/Number.md),:palette as [Lang.Array](../Lang/Array.md) < [Graphics.ColorType](../Graphics.md#ColorType-named_type) >,:colorDepth as [Lang.Number](../Lang/Number.md),:bitmapResource as [WatchUi.BitmapResource](../WatchUi/BitmapResource.md),:alphaBlending as [Graphics.AlphaBlending](../Graphics.md#AlphaBlending-module) }) deprecated
	Constructor.
- [**isCached**](#isCached-instance_function "isCached (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Check if the memory for the bitmap is still loaded in the memory User can invoke this method to check if the underlying resource is still available in the memory since last used if `true`, the resource such as [BufferedBitmap](BufferedBitmap.md) has been cached and can be used directly without re-drawing.
- [**setPalette**](#setPalette-instance_function "setPalette (Instance Function)") (palette as [Lang.Array](../Lang/Array.md) < [Graphics.ColorType](../Graphics.md#ColorType-named_type) >) as **Void**

## Instance Method Details

### getDc() as Graphics.Dc

### getHeight() as Lang.Number

### getPalette() as Lang.Array<Graphics.ColorType>

### getWidth() as Lang.Number

### initialize(options as {:width as Lang.Number,:height as Lang.Number,:palette as Lang.Array<Graphics.ColorType>,:colorDepth as Lang.Number,:bitmapResource as WatchUi.BitmapResource,:alphaBlending as Graphics.AlphaBlending })

**This has been deprecated**

Use [Graphics.createBufferedBitmap()](../Graphics.md#createBufferedBitmap-instance_function) after ConnectIQ version 4.0.0.
