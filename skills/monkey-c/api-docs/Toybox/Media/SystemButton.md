---
title: Toybox.Media.SystemButton
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/SystemButton.html
---

## Class: Toybox.Media.SystemButton

## Overview

Note:

[BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) is only supported in CIQ 4.0.0 and later

## Instance Method Summary

- [**getImage**](#getImage-instance_function "getImage (Instance Function)") (image as [Media.ButtonImage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html#ButtonImage-module), state as [Media.ButtonState](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html#ButtonState-module), highlighted as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type) or [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) or **Null**
	Called by the system to draw the button in the Media Player.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (type as [Media.PlaybackControl](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html#PlaybackControl-module), options as {:disabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) } or **Null**)
	Constructor.

## Instance Method Details

### getImage(image as Media.ButtonImage, state as Media.ButtonState, highlighted as Lang.Boolean) as Graphics.BitmapType or Graphics.ColorType or Null

Note:

[BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) is only supported in CIQ 4.0.0 and later
