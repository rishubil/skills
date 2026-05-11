---
title: Toybox.Application
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html
---

## Module: Toybox.Application

## Overview

## See Also:

- [Core Topics - Persisting Data](https://developer.garmin.com/connect-iq/core-topics/persisting-data/)

## Modules Under Namespace

**Modules:** [Application.Properties](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Properties.html), [Application.Storage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Storage.html), [Application.WatchFaceConfig](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig.html)

## Classes Under Namespace

**Classes:** [AppBase](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/AppBase.html), [AudioContentProviderApp](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/AudioContentProviderApp.html), [ObjectStoreAccessException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/ObjectStoreAccessException.html)

## Constant Summary

### GoalType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| GOAL\_TYPE\_STEPS | 0 | API Level 1.3.0 |  |
| GOAL\_TYPE\_FLOORS\_CLIMBED | 1 | API Level 1.3.0 |  |
| GOAL\_TYPE\_ACTIVE\_MINUTES | 2 | API Level 1.3.0 |  |

## Typedef Summary

- [**PersistableType**](#PersistableType-named_type "PersistableType (Named Type)") as [Application.PropertyValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#PropertyValueType-named_type)
- [**PropertyKeyType**](#PropertyKeyType-named_type "PropertyKeyType (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)
- [**PropertyValueType**](#PropertyValueType-named_type "PropertyValueType (Named Type)") as [Application.PropertyKeyType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#PropertyKeyType-named_type) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Application.PropertyValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#PropertyValueType-named_type) > or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Application.PropertyKeyType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#PropertyKeyType-named_type), [Application.PropertyValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#PropertyValueType-named_type) > or [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [BluetoothLowEnergy.ScanResult](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html) or [Complications.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html) or [WatchFaceConfig.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Id.html) or **Null**
- [**ResourceReferenceType**](#ResourceReferenceType-named_type "ResourceReferenceType (Named Type)") as [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) or [Graphics.FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html)
- [**ResourceType**](#ResourceType-named_type "ResourceType (Named Type)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [WatchUi.AnimationResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationResource.html) or [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [WatchUi.FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html)

## Instance Method Summary

- [**getApp**](#getApp-instance_function "getApp (Instance Function)") () as [Application.AppBase](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/AppBase.html)
	Retrieve the AppBase [Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) that is currently running.
- [**loadResource**](#loadResource-instance_function "loadResource (Instance Function)") (resource as [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html)) as [Application.ResourceType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#ResourceType-named_type) or [Application.ResourceReferenceType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#ResourceReferenceType-named_type)
	Load a resource from the executable.

## Typedef Details

### PersistableType as Application.PropertyValueType

### PropertyKeyType as Lang.Number or Lang.Float or Lang.Long or Lang.Double or Lang.String or Lang.Boolean or Lang.Char

### PropertyValueType as Application.PropertyKeyType or Lang.Array<Application.PropertyValueType> or Lang.Dictionary<Application.PropertyKeyType, Application.PropertyValueType> or WatchUi.BitmapResource or BluetoothLowEnergy.ScanResult or Complications.Id or WatchFaceConfig.Id or Null

### ResourceReferenceType as Graphics.BitmapReference or Graphics.FontReference

### ResourceType as Lang.Array or Lang.Dictionary or Lang.String or WatchUi.AnimationResource or WatchUi.BitmapResource or WatchUi.FontResource

## Instance Method Details

### getApp() as Application.AppBase

### loadResource(resource as Lang.ResourceId) as Application.ResourceType or Application.ResourceReferenceType

Note:

[Toybox::Graphics::BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) and [Toybox::Graphics::FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) are returned for [Toybox::WatchUi::BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) and [Toybox::WatchUi::FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html) in CIQ 4.0.0 and later.
