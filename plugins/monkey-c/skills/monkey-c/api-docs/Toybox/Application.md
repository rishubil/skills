---
title: Toybox.Application
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html
---

## Module: Toybox.Application

## Overview

## See Also:

- [Core Topics - Persisting Data](https://developer.garmin.com/connect-iq/core-topics/persisting-data/)

## Modules Under Namespace

**Modules:** [Application.Properties](Application/Properties.md), [Application.Storage](Application/Storage.md), [Application.WatchFaceConfig](Application/WatchFaceConfig.md)

## Classes Under Namespace

**Classes:** [AppBase](Application/AppBase.md), [AudioContentProviderApp](Application/AudioContentProviderApp.md), [ObjectStoreAccessException](Application/ObjectStoreAccessException.md)

## Constant Summary

### GoalType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| GOAL\_TYPE\_STEPS | 0 | API Level 1.3.0 |  |
| GOAL\_TYPE\_FLOORS\_CLIMBED | 1 | API Level 1.3.0 |  |
| GOAL\_TYPE\_ACTIVE\_MINUTES | 2 | API Level 1.3.0 |  |

## Typedef Summary

- [**PersistableType**](#PersistableType-named_type "PersistableType (Named Type)") as [Application.PropertyValueType](Application.md#PropertyValueType-named_type)
- [**PropertyKeyType**](#PropertyKeyType-named_type "PropertyKeyType (Named Type)") as [Lang.Number](Lang/Number.md) or [Lang.Float](Lang/Float.md) or [Lang.Long](Lang/Long.md) or [Lang.Double](Lang/Double.md) or [Lang.String](Lang/String.md) or [Lang.Boolean](Lang/Boolean.md) or [Lang.Char](Lang/Char.md)
- [**PropertyValueType**](#PropertyValueType-named_type "PropertyValueType (Named Type)") as [Application.PropertyKeyType](Application.md#PropertyKeyType-named_type) or [Lang.Array](Lang/Array.md) < [Application.PropertyValueType](Application.md#PropertyValueType-named_type) > or [Lang.Dictionary](Lang/Dictionary.md) < [Application.PropertyKeyType](Application.md#PropertyKeyType-named_type), [Application.PropertyValueType](Application.md#PropertyValueType-named_type) > or [WatchUi.BitmapResource](WatchUi/BitmapResource.md) or [BluetoothLowEnergy.ScanResult](BluetoothLowEnergy/ScanResult.md) or [Complications.Id](Complications/Id.md) or [WatchFaceConfig.Id](Application/WatchFaceConfig/Id.md) or **Null**
- [**ResourceReferenceType**](#ResourceReferenceType-named_type "ResourceReferenceType (Named Type)") as [Graphics.BitmapReference](Graphics/BitmapReference.md) or [Graphics.FontReference](Graphics/FontReference.md)
- [**ResourceType**](#ResourceType-named_type "ResourceType (Named Type)") as [Lang.Array](Lang/Array.md) or [Lang.Dictionary](Lang/Dictionary.md) or [Lang.String](Lang/String.md) or [WatchUi.AnimationResource](WatchUi/AnimationResource.md) or [WatchUi.BitmapResource](WatchUi/BitmapResource.md) or [WatchUi.FontResource](WatchUi/FontResource.md)

## Instance Method Summary

- [**getApp**](#getApp-instance_function "getApp (Instance Function)") () as [Application.AppBase](Application/AppBase.md)
	Retrieve the AppBase [Object](Lang/Object.md) that is currently running.
- [**loadResource**](#loadResource-instance_function "loadResource (Instance Function)") (resource as [Lang.ResourceId](Lang/ResourceId.md)) as [Application.ResourceType](Application.md#ResourceType-named_type) or [Application.ResourceReferenceType](Application.md#ResourceReferenceType-named_type)
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

[Toybox::Graphics::BitmapReference](Graphics/BitmapReference.md) and [Toybox::Graphics::FontReference](Graphics/FontReference.md) are returned for [Toybox::WatchUi::BitmapResource](WatchUi/BitmapResource.md) and [Toybox::WatchUi::FontResource](WatchUi/FontResource.md) in CIQ 4.0.0 and later.
