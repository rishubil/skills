---
title: Toybox.WatchUi.AnimationResource
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationResource.html
---

## Class: Toybox.WatchUi.AnimationResource

## Overview

A representation of an animation resource.

AnimationResource objects are returned by the [loadResource()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#loadResource-instance_function) method.

## Instance Method Summary

- [**getColorDepth**](#getColorDepth-instance_function "getColorDepth (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the color depth in terms of bit/pixel of the animation resource.
- [**getFrameRate**](#getFrameRate-instance_function "getFrameRate (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the target frame rate of an animation resource.
- [**getHeight**](#getHeight-instance_function "getHeight (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the height of an animation resource.
- [**getNumberOfFrames**](#getNumberOfFrames-instance_function "getNumberOfFrames (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the number of frames of an animation resource.
- [**getWidth**](#getWidth-instance_function "getWidth (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the width of an animation resource.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Get info about an animation resource as a String.

## Instance Method Details

### getColorDepth() as Lang.Number

Get the color depth in terms of bit/pixel of the animation resource.

### getFrameRate() as Lang.Number

Get the target frame rate of an animation resource.

### getHeight() as Lang.Number

Get the height of an animation resource.

### getNumberOfFrames() as Lang.Number

Get the number of frames of an animation resource.

### getWidth() as Lang.Number

Get the width of an animation resource.

### toString() as Lang.String

Get info about an animation resource as a String.

The info String is formatted as "Animation X x Y" where "X" is the width of the animation and "Y" is the height.
