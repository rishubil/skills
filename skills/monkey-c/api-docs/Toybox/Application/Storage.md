---
title: Toybox.Application.Storage
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Storage.html
---

## Module: Toybox.Application.Storage

## Overview

## Typedef Summary

- [**KeyType**](#KeyType-named_type "KeyType (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)
- [**ValueType**](#ValueType-named_type "ValueType (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html) or [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) or [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [WatchUi.AnimationResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationResource.html) or [BluetoothLowEnergy.ScanResult](https://developer.garmin.com/connect-iq/api-docs/Toybox/BluetoothLowEnergy/ScanResult.html) or [Complications.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html) or [WatchFaceConfig.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/WatchFaceConfig/Id.html) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Storage.ValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Storage.html#ValueType-named_type) > or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Storage.KeyType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Storage.html#KeyType-named_type), [Storage.ValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Storage.html#ValueType-named_type) > or **Null**

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
