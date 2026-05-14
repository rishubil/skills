---
title: Toybox.Media.CustomButton
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/CustomButton.html
---

## Class: Toybox.Media.CustomButton

## Overview

## Instance Method Summary

- [**getImage**](#getImage-instance_function "getImage (Instance Function)") (image as [Media.ButtonImage](../Media.md#ButtonImage-module), highlighted as [Lang.Boolean](../Lang/Boolean.md)) as [WatchUi.BitmapResource](../WatchUi/BitmapResource.md) or [Graphics.BitmapReference](../Graphics/BitmapReference.md) or **Null**
	Called by the system to draw the button in the Media Player.
- [**getState**](#getState-instance_function "getState (Instance Function)") () as [Media.ButtonState](../Media.md#ButtonState-module)
	Called by the system to determine if the current state of the button.
- [**getText**](#getText-instance_function "getText (Instance Function)") (state as [Media.ButtonState](../Media.md#ButtonState-module)) as [Lang.String](../Lang/String.md) or **Null**
	Called by the system to draw the name of the button.

## Instance Method Details

### getImage(image as Media.ButtonImage, highlighted as Lang.Boolean) as WatchUi.BitmapResource or Graphics.BitmapReference or Null

Note:

[BitmapReference](../Graphics/BitmapReference.md) is only supported in CIQ 4.0.0 and later.
