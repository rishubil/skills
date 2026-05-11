---
title: Toybox.Graphics
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html
---

## Module: Toybox.Graphics

## Overview

## Classes Under Namespace

**Classes:** [AffineTransform](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/AffineTransform.html), [BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html), [BitmapTexture](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapTexture.html), [BoundingBox](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BoundingBox.html), [BufferedBitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html), [BufferedBitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmapReference.html), [Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html), [FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html), [InvalidBitmapResourceException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/InvalidBitmapResourceException.html), [InvalidPaletteException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/InvalidPaletteException.html), [OutOfGraphicsMemoryException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/OutOfGraphicsMemoryException.html), [ResourceReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/ResourceReference.html), [VectorFont](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/VectorFont.html)

## Constant Summary

### FontDefinition

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FONT\_XTINY | 0 | API Level 1.0.0 | Extra tiny Connect IQ font |
| FONT\_TINY | 1 | API Level 1.0.0 | Tiny Connect IQ font |
| FONT\_SMALL | 2 | API Level 1.0.0 | Small Connect IQ font |
| FONT\_MEDIUM | 3 | API Level 1.0.0 | Medium Connect IQ font |
| FONT\_LARGE | 4 | API Level 1.0.0 | Large Connect IQ font |
| FONT\_NUMBER\_MILD | 5 | API Level 1.0.0 | Normal size number only Connect IQ font |
| FONT\_NUMBER\_MEDIUM | 6 | API Level 1.0.0 | Medium size number only Connect IQ font |
| FONT\_NUMBER\_HOT | 7 | API Level 1.0.0 | Large size number only Connect IQ font |
| FONT\_NUMBER\_THAI\_HOT | 8 | API Level 1.0.0 | Huge size number only Connect IQ font |
| FONT\_SYSTEM\_XTINY | 9 | API Level 1.3.0 | Extra tiny system font |
| FONT\_SYSTEM\_TINY | 10 | API Level 1.3.0 | Tiny system font |
| FONT\_SYSTEM\_SMALL | 11 | API Level 1.3.0 | Small system font |
| FONT\_SYSTEM\_MEDIUM | 12 | API Level 1.3.0 | Medium system font |
| FONT\_SYSTEM\_LARGE | 13 | API Level 1.3.0 | Large system font |
| FONT\_SYSTEM\_NUMBER\_MILD | 14 | API Level 1.3.0 | Normal size number only system font |
| FONT\_SYSTEM\_NUMBER\_MEDIUM | 15 | API Level 1.3.0 | Medium size number only system font |
| FONT\_SYSTEM\_NUMBER\_HOT | 16 | API Level 1.3.0 | Large size number only system font |
| FONT\_SYSTEM\_NUMBER\_THAI\_HOT | 17 | API Level 1.3.0 | Huge size number only system font |
| FONT\_GLANCE | 18 | API Level 3.1.8 | Glance text font |
| FONT\_GLANCE\_NUMBER | 19 | API Level 3.1.8 | Glance number only font |
| FONT\_AUX1 | 20 | API Level 4.2.2 | Auxiliary Font 1 |
| FONT\_AUX2 | 21 | API Level 4.2.2 | Auxiliary Font 2 |
| FONT\_AUX3 | 22 | API Level 4.2.3 | Auxiliary Font 3 |
| FONT\_AUX4 | 23 | API Level 4.2.3 | Auxiliary Font 4 |
| FONT\_AUX5 | 24 | API Level 4.2.3 | Auxiliary Font 5 |
| FONT\_AUX6 | 25 | API Level 4.2.3 | Auxiliary Font 6 |
| FONT\_AUX7 | 26 | API Level 4.2.3 | Auxiliary Font 7 |
| FONT\_AUX8 | 27 | API Level 4.2.3 | Auxiliary Font 8 |
| FONT\_AUX9 | 28 | API Level 4.2.3 | Auxiliary Font 9 |

### ColorValue

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| COLOR\_WHITE | 0xFFFFFF | API Level 1.0.0 | White |
| COLOR\_LT\_GRAY | 0xAAAAAA | API Level 1.0.0 | Light Gray |
| COLOR\_DK\_GRAY | 0x555555 | API Level 1.0.0 | Dark Gray |
| COLOR\_BLACK | 0x000000 | API Level 1.0.0 | Black |
| COLOR\_RED | 0xFF0000 | API Level 1.0.0 | Red |
| COLOR\_DK\_RED | 0xAA0000 | API Level 1.0.0 | Dark Red |
| COLOR\_ORANGE | 0xFF5500 | API Level 1.0.0 | Orange |
| COLOR\_YELLOW | 0xFFAA00 | API Level 1.0.0 | Yellow |
| COLOR\_GREEN | 0x00FF00 | API Level 1.0.0 | Green |
| COLOR\_DK\_GREEN | 0x00AA00 | API Level 1.0.0 | Dark Green |
| COLOR\_BLUE | 0x00AAFF | API Level 1.0.0 | Blue |
| COLOR\_DK\_BLUE | 0x0000FF | API Level 1.0.0 | Dark Blue |
| COLOR\_PURPLE | 0xAA00FF | API Level 1.0.0 | Purple. Not valid on fenix 3 or D2 Bravo. Use 0x5500AA instead. |
| COLOR\_PINK | 0xFF00FF | API Level 1.0.0 | Pink |
| COLOR\_TRANSPARENT | \-1 | API Level 1.0.0 | Transparent |

### TextJustification

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| TEXT\_JUSTIFY\_RIGHT | 0 | API Level 1.0.0 | Right justify the text at the x/y coordinates |
| TEXT\_JUSTIFY\_CENTER | 1 | API Level 1.0.0 | Center justify the text at the x/y coordinates |
| TEXT\_JUSTIFY\_LEFT | 2 | API Level 1.0.0 | Left justify the text at the x/y coordinates |
| TEXT\_JUSTIFY\_VCENTER | 4 | API Level 1.0.0 | Center the text vertically |

### BlendMode

Blend mode

Specifies how colors of a source pixel will be blended with the colors of a destination pixel.

In the below descriptions

```
S is source pixel
D is destination pixel
a is the alpha component
```

| Name | Value | Since | Description | Note |
| --- | --- | --- | --- | --- |
| BLEND\_MODE\_DEFAULT | 0 | API Level 4.0.0 | Alias for `BLEND_MODE_SOURCE_OVER` |  |
| BLEND\_MODE\_NO\_BLEND | 1 | API Level 4.0.0 | Alias for `BLEND_MODE_SOURCE` |  |
| BLEND\_MODE\_SOURCE\_OVER | 0 | API Level 4.2.1 | S + (1 - S.a) \* D |  |
| BLEND\_MODE\_SOURCE | 1 | API Level 4.2.1 | S, i.e. no blending. |  |
| BLEND\_MODE\_MULTIPLY | 2 | API Level 4.2.1 | (S \* (1 - D.a)) + (D \* (1 - S.a)) + (S \* D) | Only supported on devices with GPU |
| BLEND\_MODE\_ADDITIVE | 3 | API Level 4.2.1 | S + D | Only supported on devices with GPU |

### AlphaBlending

Constant representing alpha blending state for buffered bitmaps

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ALPHA\_BLENDING\_FULL | 0 | API Level 4.0.0 | Default surface for buffered bitmap with maximum alpha blending support |
| ALPHA\_BLENDING\_PARTIAL | 1 | API Level 4.0.0 | Surface for buffered bitmap with at least a 1-bit alpha channel. The actual number of bits may vary by device. |

### RadialTextDirection

Orientation for radial text

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| RADIAL\_TEXT\_DIRECTION\_CLOCKWISE | 0 | API Level 4.2.1 | Top of text is further from center. Typically used for upright text along the top of a circle. |
| RADIAL\_TEXT\_DIRECTION\_COUNTER\_CLOCKWISE | 1 | API Level 4.2.1 | Bottom of text is further from center. Typically used for upright text along the bottom of a circle. |

### FilterMode

Filter mode

Specifies how many pixels to sample

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FILTER\_MODE\_POINT | 0 | API Level 4.2.1 | Point filter |
| FILTER\_MODE\_BILINEAR | 1 | API Level 4.2.1 | Bilinear filter |

### ArcDirection

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ARC\_COUNTER\_CLOCKWISE | 0 | API Level 1.2.0 | Counter clockwise draw |
| ARC\_CLOCKWISE | 1 | API Level 1.2.0 | Clockwise draw |

## Typedef Summary

- [**BitmapType**](#BitmapType-named_type "BitmapType (Named Type)") as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BufferedBitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) or [Graphics.BufferedBitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmapReference.html)
- [**ColorType**](#ColorType-named_type "ColorType (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Graphics.ColorValue](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorValue-module)
- [**FontType**](#FontType-named_type "FontType (Named Type)") as [WatchUi.FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html) or [Graphics.FontDefinition](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontDefinition-module) or [Graphics.FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) or [Graphics.VectorFont](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/VectorFont.html)
- [**Point2D**](#Point2D-named_type "Point2D (Named Type)") as \[ [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type) \]
	Type alias for an Array of length 2.
- [**VectorFontOptions**](#VectorFontOptions-named_type "VectorFontOptions (Named Type)") as {:face as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) >,:size as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type),:font as [Graphics.FontDefinition](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontDefinition-module) or [Graphics.VectorFont](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/VectorFont.html),:scale as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) }

## Instance Method Summary

- [**createBufferedBitmap**](#createBufferedBitmap-instance_function "createBufferedBitmap (Instance Function)") (options as {:width as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:height as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:palette as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) >,:colorDepth as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:bitmapResource as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html),:alphaBlending as [Graphics.AlphaBlending](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#AlphaBlending-module) }) as [Graphics.BufferedBitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmapReference.html)
	Create a buffered bitmap object.
- [**createColor**](#createColor-instance_function "createColor (Instance Function)") (alpha as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), red as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), green as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), blue as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Create a color with the individual channel values passed in.
- [**fitTextToArea**](#fitTextToArea-instance_function "fitTextToArea (Instance Function)") (text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type), width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), truncate as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	Get a text string to fit in a specified area.
- [**getFontAscent**](#getFontAscent-instance_function "getFontAscent (Instance Function)") (font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the recommended distance above the baseline for single spaced text.
- [**getFontDescent**](#getFontDescent-instance_function "getFontDescent (Instance Function)") (font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the recommended distance below the baseline for single spaced text.
- [**getFontHeight**](#getFontHeight-instance_function "getFontHeight (Instance Function)") (font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the height (ascent plus descent) of the given font.
- [**getVectorFont**](#getVectorFont-instance_function "getVectorFont (Instance Function)") (options as [Graphics.VectorFontOptions](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#VectorFontOptions-named_type)) as [Graphics.VectorFont](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/VectorFont.html) or **Null**
	Get a font for this device.

## Typedef Details

### BitmapType as WatchUi.BitmapResource or Graphics.BufferedBitmap or Graphics.BitmapReference or Graphics.BufferedBitmapReference

### ColorType as Lang.Number or Graphics.ColorValue

### FontType as WatchUi.FontResource or Graphics.FontDefinition or Graphics.FontReference or Graphics.VectorFont

### Point2D as \[ Lang.Numeric, Lang.Numeric \]

### VectorFontOptions as {:face as Lang.String or Lang.Array<Lang.String>,:size as Lang.Numeric,:font as Graphics.FontDefinition or Graphics.VectorFont,:scale as Lang.Float }

## Instance Method Details

### createBufferedBitmap(options as {:width as Lang.Number,:height as Lang.Number,:palette as Lang.Array<Graphics.ColorType>,:colorDepth as Lang.Number,:bitmapResource as WatchUi.BitmapResource or Graphics.BitmapReference,:alphaBlending as Graphics.AlphaBlending }) as Graphics.BufferedBitmapReference

Note:

The result of a draw/fill operation to a [BufferedBitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html) created with [ALPHA\_BLENDING\_PARTIAL](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#AlphaBlending-module) may produce inconsistent results between devices and the ConnectIQ simulator if the drawn pixels are not fully opaque or fully transparent.

### createColor(alpha as Lang.Number, red as Lang.Number, green as Lang.Number, blue as Lang.Number) as Lang.Number

### fitTextToArea(text as Lang.String, font as Graphics.FontType, width as Lang.Numeric, height as Lang.Numeric, truncate as Lang.Boolean) as Lang.String or Null

Note:

[FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) is only supported in CIQ 4.0.0 and later

### getFontAscent(font as Graphics.FontType) as Lang.Number

Note:

[FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) is only supported in CIQ 4.0.0 and later

### getFontDescent(font as Graphics.FontType) as Lang.Number

Note:

[FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) is only supported in CIQ 4.0.0 and later

### getFontHeight(font as Graphics.FontType) as Lang.Number

Note:

[FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) is only supported in CIQ 4.0.0 and later

### getVectorFont(options as Graphics.VectorFontOptions) as Graphics.VectorFont or Null

Note:

The:font and:scale options are only supported in CIQ 5.1.0 and later.
