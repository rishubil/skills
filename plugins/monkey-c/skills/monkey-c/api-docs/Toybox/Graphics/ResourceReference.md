---
title: Toybox.Graphics.ResourceReference
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/ResourceReference.html
---

## Class: Toybox.Graphics.ResourceReference

## Overview

Object represents a reference for the resource allocated from the graphics memory pool rather than from the app's local memory. The underlying resource object could be temporarily purged from the system memory pool when all `strong` references are destroyed. The memory allocation is performed only when [ResourceReference::get()](ResourceReference.md#get-instance_function) method is invoked.

## Direct Known Subclasses

[Graphics.BitmapReference](BitmapReference.md), [Graphics.BufferedBitmapReference](BufferedBitmapReference.md), [Graphics.FontReference](FontReference.md)

## Typedef Summary

- [**Options**](#Options-named_type "Options (Named Type)") as {:resource as [WatchUi.FontResource](../WatchUi/FontResource.md) or [WatchUi.BitmapResource](../WatchUi/BitmapResource.md) or [Graphics.BufferedBitmap](BufferedBitmap.md),:rezId as [Lang.ResourceId](../Lang/ResourceId.md),:bufferedBitmap as {:bitmapResource as [Lang.ResourceId](../Lang/ResourceId.md),:width as [Lang.Number](../Lang/Number.md),:height as [Lang.Number](../Lang/Number.md),:palette as [Lang.Array](../Lang/Array.md) < [Graphics.ColorType](../Graphics.md#ColorType-named_type) >,:colorDepth as [Lang.Number](../Lang/Number.md) } }

## Instance Method Summary

- [**get**](#get-instance_function "get (Instance Function)") () as [WatchUi.BitmapResource](../WatchUi/BitmapResource.md) or [Graphics.BufferedBitmap](BufferedBitmap.md) or [WatchUi.FontResource](../WatchUi/FontResource.md) or **Null**
	Get the underlying resource object referenced by the ResourceReference, this trigger either the allocate from the system memory pool or return the existing resource in the pool.

## Typedef Details

### Options as {:resource as WatchUi.FontResource or WatchUi.BitmapResource or Graphics.BufferedBitmap,:rezId as Lang.ResourceId,:bufferedBitmap as {:bitmapResource as Lang.ResourceId,:width as Lang.Number,:height as Lang.Number,:palette as Lang.Array<Graphics.ColorType>,:colorDepth as Lang.Number } }

## Instance Method Details

### get() as WatchUi.BitmapResource or Graphics.BufferedBitmap or WatchUi.FontResource or Null

Get the underlying resource object referenced by the ResourceReference, this trigger either the allocate from the system memory pool or return the existing resource in the pool.
