---
title: Toybox.Application.WatchFaceConfig
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig.html
---

## Module: Toybox.Application.WatchFaceConfig

## Overview

The WatchFaceConfig module facilitates access to persisted watchface configurations. Watchface could have more than one configuration settings, and each setting is represented by a unique identifier.

## Classes Under Namespace

**Classes:** [Color](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Color.html), [ComplicationRef](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/ComplicationRef.html), [Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Id.html), [Settings](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Settings.html)

## Instance Method Summary

- [**getIds**](#getIds-instance_function "getIds (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [WatchFaceConfig.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Id.html) > or **Null**
	Returns ids of all saved watchface config settings.
- [**getSettings**](#getSettings-instance_function "getSettings (Instance Function)") (configId as [WatchFaceConfig.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Id.html) or **Null**) as [WatchFaceConfig.Settings](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Settings.html) or **Null**
	Returns the watchface config settings for the given unique identifier.
- [**setSettings**](#setSettings-instance_function "setSettings (Instance Function)") (configId as [WatchFaceConfig.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Id.html) or **Null**, settings as [WatchFaceConfig.Settings](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Settings.html)) as **Void**
	Set or update watchface config settings with the given unique identifier, `configId`.

## Instance Method Details

### getIds() as Lang.Array<WatchFaceConfig.Id> or Null

Returns ids of all saved watchface config settings.

### getSettings(configId as WatchFaceConfig.Id or Null) as WatchFaceConfig.Settings or Null

Returns the watchface config settings for the given unique identifier.

### setSettings(configId as WatchFaceConfig.Id or Null, settings as WatchFaceConfig.Settings) as Void

Set or update watchface config settings with the given unique identifier, `configId`.
