---
title: Toybox.WatchUi.AnimationLayer
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationLayer.html
---

## Class: Toybox.WatchUi.AnimationLayer

## Overview

## Instance Method Summary

- [**getDc**](#getDc-instance_function "getDc (Instance Function)") () as [Graphics.Dc](../Graphics/Dc.md) or **Null**
	getDc will always return `null`, as the dc buffer of animations can not be updated by user.
- [**getResource**](#getResource-instance_function "getResource (Instance Function)") () as [WatchUi.AnimationResource](AnimationResource.md)
	Get the animation resource.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (rez as [Lang.ResourceId](../Lang/ResourceId.md) or [WatchUi.AnimationResource](AnimationResource.md), options as {:locX as [Lang.Numeric](../Lang.md#Numeric-named_type),:locY as [Lang.Numeric](../Lang.md#Numeric-named_type),:identifier as [Lang.Object](../Lang/Object.md),:visibility as [Lang.Boolean](../Lang/Boolean.md) } or **Null**)
	Constructor.
- [**play**](#play-instance_function "play (Instance Function)") (options as {:delegate as [WatchUi.AnimationDelegate](AnimationDelegate.md) } or **Null**) as [Lang.Boolean](../Lang/Boolean.md)
	Play animation, animation must be added to and not abandoned by the view before it can be played.
- [**stop**](#stop-instance_function "stop (Instance Function)") () as **Void**
	Stop a playing animation.

## Instance Method Details

### getDc() as Graphics.Dc or Null

### getResource() as WatchUi.AnimationResource

### initialize(rez as Lang.ResourceId or WatchUi.AnimationResource, options as {:locX as Lang.Numeric,:locY as Lang.Numeric,:identifier as Lang.Object,:visibility as Lang.Boolean } or Null)

### play(options as {:delegate as WatchUi.AnimationDelegate } or Null) as Lang.Boolean

### stop() as Void

Stop a playing animation.

```
The last frame of the animation will be persisted in the frame buffer.
```
