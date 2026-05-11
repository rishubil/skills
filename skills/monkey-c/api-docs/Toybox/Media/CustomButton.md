---
title: Toybox.Media.CustomButton
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/CustomButton.html
---

## Class: Toybox.Media.CustomButton

## Overview

## Instance Method Summary

- [**getImage**](#getImage-instance_function "getImage (Instance Function)") (image as [Media.ButtonImage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html#ButtonImage-module), highlighted as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) or **Null**
	Called by the system to draw the button in the Media Player.
- [**getState**](#getState-instance_function "getState (Instance Function)") () as [Media.ButtonState](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html#ButtonState-module)
	Called by the system to determine if the current state of the button.
- [**getText**](#getText-instance_function "getText (Instance Function)") (state as [Media.ButtonState](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html#ButtonState-module)) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	Called by the system to draw the name of the button.

## Instance Method Details

### getImage(image as Media.ButtonImage, highlighted as Lang.Boolean) as WatchUi.BitmapResource or Graphics.BitmapReference or Null

Note:

[BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) is only supported in CIQ 4.0.0 and later.
