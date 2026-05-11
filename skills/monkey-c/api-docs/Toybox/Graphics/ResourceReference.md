---
title: Toybox.Graphics.ResourceReference
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/ResourceReference.html
---

## Class: Toybox.Graphics.ResourceReference

## Overview

Object represents a reference for the resource allocated from the graphics memory pool rather than from the app's local memory. The underlying resource object could be temporarily purged from the system memory pool when all `strong` references are destroyed. The memory allocation is performed only when [ResourceReference::get()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/ResourceReference.html#get-instance_function) method is invoked.

## Direct Known Subclasses

[Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html), [Graphics.BufferedBitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmapReference.html), [Graphics.FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html)

## Typedef Summary

- [**Options**](#Options-named_type "Options (Named Type)") as {:resource as [WatchUi.FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html) or [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BufferedBitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html),:rezId as [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:bufferedBitmap as {:bitmapResource as [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:width as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:height as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:palette as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) >,:colorDepth as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) } }

## Instance Method Summary

- [**get**](#get-instance_function "get (Instance Function)") () as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BufferedBitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html) or [WatchUi.FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html) or **Null**
	Get the underlying resource object referenced by the ResourceReference, this trigger either the allocate from the system memory pool or return the existing resource in the pool.

## Typedef Details

### Options as {:resource as WatchUi.FontResource or WatchUi.BitmapResource or Graphics.BufferedBitmap,:rezId as Lang.ResourceId,:bufferedBitmap as {:bitmapResource as Lang.ResourceId,:width as Lang.Number,:height as Lang.Number,:palette as Lang.Array<Graphics.ColorType>,:colorDepth as Lang.Number } }

## Instance Method Details

### get() as WatchUi.BitmapResource or Graphics.BufferedBitmap or WatchUi.FontResource or Null

Get the underlying resource object referenced by the ResourceReference, this trigger either the allocate from the system memory pool or return the existing resource in the pool.
