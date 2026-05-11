---
title: Toybox.Application.Storage
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Storage.html
---

## Module: Toybox.Application.Storage

## Overview

## Typedef Summary

- [**KeyType**](#KeyType-named_type "KeyType (Named Type)") as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md) or [Lang.Long](../Lang/Long.md) or [Lang.Double](../Lang/Double.md) or [Lang.String](../Lang/String.md) or [Lang.Boolean](../Lang/Boolean.md) or [Lang.Char](../Lang/Char.md)
- [**ValueType**](#ValueType-named_type "ValueType (Named Type)") as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md) or [Lang.Long](../Lang/Long.md) or [Lang.Double](../Lang/Double.md) or [Lang.String](../Lang/String.md) or [Lang.Boolean](../Lang/Boolean.md) or [Lang.Char](../Lang/Char.md) or [Lang.ByteArray](../Lang/ByteArray.md) or [Graphics.BitmapReference](../Graphics/BitmapReference.md) or [WatchUi.BitmapResource](../WatchUi/BitmapResource.md) or [WatchUi.AnimationResource](../WatchUi/AnimationResource.md) or [BluetoothLowEnergy.ScanResult](../BluetoothLowEnergy/ScanResult.md) or [Complications.Id](../Complications/Id.md) or [WatchFaceConfig.Id](WatchFaceConfig/Id.md) or [Lang.Array](../Lang/Array.md) < [Storage.ValueType](Storage.md#ValueType-named_type) > or [Lang.Dictionary](../Lang/Dictionary.md) < [Storage.KeyType](Storage.md#KeyType-named_type), [Storage.ValueType](Storage.md#ValueType-named_type) > or **Null**

## Instance Method Summary

## Typedef Details

### KeyType as Lang.Number or Lang.Float or Lang.Long or Lang.Double or Lang.String or Lang.Boolean or Lang.Char

### ValueType as Lang.Number or Lang.Float or Lang.Long or Lang.Double or Lang.String or Lang.Boolean or Lang.Char or Lang.ByteArray or Graphics.BitmapReference or WatchUi.BitmapResource or WatchUi.AnimationResource or BluetoothLowEnergy.ScanResult or Complications.Id or WatchFaceConfig.Id or Lang.Array<Storage.ValueType> or Lang.Dictionary<Storage.KeyType, Storage.ValueType> or Null

## Instance Method Details

### clearValues() as Void

### deleteValue(key as Storage.KeyType) as Void

### getValue(key as Storage.KeyType) as Storage.ValueType

Note:

Symbols can change from build to build and are not to be used for for Keys or Values

### setValue(key as Storage.KeyType, value as Storage.ValueType) as Void

Note:

Symbols can change from build to build and are not to be used for for Keys or Values
