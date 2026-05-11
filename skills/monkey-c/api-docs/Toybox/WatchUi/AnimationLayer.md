---
title: Toybox.WatchUi.AnimationLayer
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationLayer.html
---

## Class: Toybox.WatchUi.AnimationLayer

## Overview

## Instance Method Summary

- [**getDc**](#getDc-instance_function "getDc (Instance Function)") () as [Graphics.Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html) or **Null**
	getDc will always return `null`, as the dc buffer of animations can not be updated by user.
- [**getResource**](#getResource-instance_function "getResource (Instance Function)") () as [WatchUi.AnimationResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationResource.html)
	Get the animation resource.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (rez as [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) or [WatchUi.AnimationResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationResource.html), options as {:locX as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:locY as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:identifier as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html),:visibility as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) } or **Null**)
	Constructor.
- [**play**](#play-instance_function "play (Instance Function)") (options as {:delegate as [WatchUi.AnimationDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationDelegate.html) } or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
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
