---
title: Toybox.Application.WatchFaceConfig
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig.html
---

## Module: Toybox.Application.WatchFaceConfig

## Overview

The WatchFaceConfig module facilitates access to persisted watchface configurations. Watchface could have more than one configuration settings, and each setting is represented by a unique identifier.

## Classes Under Namespace

**Classes:** [Color](WatchFaceConfig/Color.md), [ComplicationRef](WatchFaceConfig/ComplicationRef.md), [Id](WatchFaceConfig/Id.md), [Settings](WatchFaceConfig/Settings.md)

## Instance Method Summary

- [**getIds**](#getIds-instance_function "getIds (Instance Function)") () as [Lang.Array](../Lang/Array.md) < [WatchFaceConfig.Id](WatchFaceConfig/Id.md) > or **Null**
	Returns ids of all saved watchface config settings.
- [**getSettings**](#getSettings-instance_function "getSettings (Instance Function)") (configId as [WatchFaceConfig.Id](WatchFaceConfig/Id.md) or **Null**) as [WatchFaceConfig.Settings](WatchFaceConfig/Settings.md) or **Null**
	Returns the watchface config settings for the given unique identifier.
- [**setSettings**](#setSettings-instance_function "setSettings (Instance Function)") (configId as [WatchFaceConfig.Id](WatchFaceConfig/Id.md) or **Null**, settings as [WatchFaceConfig.Settings](WatchFaceConfig/Settings.md)) as **Void**
	Set or update watchface config settings with the given unique identifier, `configId`.

## Instance Method Details

### getIds() as Lang.Array<WatchFaceConfig.Id> or Null

Returns ids of all saved watchface config settings.

### getSettings(configId as WatchFaceConfig.Id or Null) as WatchFaceConfig.Settings or Null

Returns the watchface config settings for the given unique identifier.

### setSettings(configId as WatchFaceConfig.Id or Null, settings as WatchFaceConfig.Settings) as Void

Set or update watchface config settings with the given unique identifier, `configId`.
