---
title: Toybox.ScanCode
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ScanCode.html
---

## Module: Toybox.ScanCode

## Overview

The ScanCode module provides functionality to for generating machine readable code images.

## Constant Summary

### QrCodeEcc

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| QR\_CODE\_ECC\_LOW | 0 | API Level 6.0.0 | Tolerate up to 7% error |
| QR\_CODE\_ECC\_MEDIUM | 1 | API Level 6.0.0 | Tolerate up to 15% error |
| QR\_CODE\_ECC\_QUARTILE | 2 | API Level 6.0.0 | Tolerate up to 25% error |
| QR\_CODE\_ECC\_HIGH | 3 | API Level 6.0.0 | Tolerate up to 30% error |

### QrCodeMask

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| QR\_CODE\_MASK\_AUTO | \-1 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_0 | 0 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_1 | 1 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_2 | 2 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_3 | 3 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_4 | 4 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_5 | 5 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_6 | 6 | API Level 6.0.0 |  |
| QR\_CODE\_MASK\_7 | 7 | API Level 6.0.0 |  |

## Typedef Summary

- [**QrCodeOptions**](#QrCodeOptions-named_type "QrCodeOptions (Named Type)") as {:minVersion as [Lang.Number](Lang/Number.md),:maxVersion as [Lang.Number](Lang/Number.md),:maskValue as [ScanCode.QrCodeMask](ScanCode.md#QrCodeMask-module),:color as [Graphics.ColorType](Graphics.md#ColorType-named_type),:backgroundColor as [Graphics.ColorType](Graphics.md#ColorType-named_type) }
- [**QrCodeValue**](#QrCodeValue-named_type "QrCodeValue (Named Type)") as [Lang.ByteArray](Lang/ByteArray.md) or [Lang.String](Lang/String.md) or [Lang.Array](Lang/Array.md) < [Lang.ByteArray](Lang/ByteArray.md) or [Lang.String](Lang/String.md) >

## Instance Method Summary

- [**createQrCodeImage**](#createQrCodeImage-instance_function "createQrCodeImage (Instance Function)") (value as [ScanCode.QrCodeValue](ScanCode.md#QrCodeValue-named_type), ecc as [ScanCode.QrCodeEcc](ScanCode.md#QrCodeEcc-module), imageSize as [Lang.Number](Lang/Number.md), options as [ScanCode.QrCodeOptions](ScanCode.md#QrCodeOptions-named_type) or **Null**) as [Graphics.BufferedBitmap](Graphics/BufferedBitmap.md)
	Create a Quick Response Code image.

## Typedef Details

### QrCodeOptions as {:minVersion as Lang.Number,:maxVersion as Lang.Number,:maskValue as ScanCode.QrCodeMask,:color as Graphics.ColorType,:backgroundColor as Graphics.ColorType }

### QrCodeValue as Lang.ByteArray or Lang.String or Lang.Array<Lang.ByteArray or Lang.String>

## Instance Method Details

### createQrCodeImage(value as ScanCode.QrCodeValue, ecc as ScanCode.QrCodeEcc, imageSize as Lang.Number, options as ScanCode.QrCodeOptions or Null) as Graphics.BufferedBitmap

Create a Quick Response Code image
