---
title: Toybox.Media.SystemButton
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/SystemButton.html
---

## Class: Toybox.Media.SystemButton

## Overview

Note:

[BitmapReference](../Graphics/BitmapReference.md) is only supported in CIQ 4.0.0 and later

## Instance Method Summary

- [**getImage**](#getImage-instance_function "getImage (Instance Function)") (image as [Media.ButtonImage](../Media.md#ButtonImage-module), state as [Media.ButtonState](../Media.md#ButtonState-module), highlighted as [Lang.Boolean](../Lang/Boolean.md)) as [Graphics.BitmapType](../Graphics.md#BitmapType-named_type) or [Graphics.ColorType](../Graphics.md#ColorType-named_type) or **Null**
	Called by the system to draw the button in the Media Player.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (type as [Media.PlaybackControl](../Media.md#PlaybackControl-module), options as {:disabled as [Lang.Boolean](../Lang/Boolean.md) } or **Null**)
	Constructor.

## Instance Method Details

### getImage(image as Media.ButtonImage, state as Media.ButtonState, highlighted as Lang.Boolean) as Graphics.BitmapType or Graphics.ColorType or Null

Note:

[BitmapReference](../Graphics/BitmapReference.md) is only supported in CIQ 4.0.0 and later
