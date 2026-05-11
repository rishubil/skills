---
title: Toybox.Graphics.Dc
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html
---

## Class: Toybox.Graphics.Dc

## Overview

Note:

You should never directly instantiate a Dc object, or attempt to render to the screen outside of an onUpdate call.

## Instance Method Summary

- [**clear**](#clear-instance_function "clear (Instance Function)") () as **Void**
	Erase the screen using the background color.
- [**clearClip**](#clearClip-instance_function "clearClip (Instance Function)") () as **Void**
	Reset the drawable area to the full area of the Dc.
- [**drawAngledText**](#drawAngledText-instance_function "drawAngledText (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), font as [Graphics.VectorFont](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/VectorFont.html), text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), justification as [Graphics.TextJustification](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#TextJustification-module) or [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), angle as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw angled text Draw text such that it is oriented perpendicular to a radial line at the given angle.
- [**drawArc**](#drawArc-instance_function "drawArc (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), r as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), attr as [Graphics.ArcDirection](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ArcDirection-module), degreeStart as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), degreeEnd as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw an arc.
- [**drawBitmap**](#drawBitmap-instance_function "drawBitmap (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmap as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type)) as **Void**
	Draw a bitmap to the screen.
- [**drawBitmap2**](#drawBitmap2-instance_function "drawBitmap2 (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmap as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type), options as {:bitmapX as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:bitmapY as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:bitmapWidth as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:bitmapHeight as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:tintColor as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type),:filterMode as [Graphics.FilterMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FilterMode-module),:transform as [Graphics.AffineTransform](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/AffineTransform.html) } or **Null**) as **Void**
	Draw bitmap with the given options.
- [**drawCircle**](#drawCircle-instance_function "drawCircle (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), radius as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw a circle around a point.
- [**drawEllipse**](#drawEllipse-instance_function "drawEllipse (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), a as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), b as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw an ellipse around a point.
- [**drawLine**](#drawLine-instance_function "drawLine (Instance Function)") (x1 as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y1 as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), x2 as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y2 as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw a line between two points.
- [**drawOffsetBitmap**](#drawOffsetBitmap-instance_function "drawOffsetBitmap (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmapX as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmapY as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmapWidth as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmapHeight as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmap as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type)) as **Void**
	Draw a bitmap to the screen with an offset.
- [**drawPoint**](#drawPoint-instance_function "drawPoint (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw a point on the screen.
- [**drawRadialText**](#drawRadialText-instance_function "drawRadialText (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), font as [Graphics.VectorFont](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/VectorFont.html), text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), justification as [Graphics.TextJustification](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#TextJustification-module) or [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), angle as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), radius as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), direction as [Graphics.RadialTextDirection](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#RadialTextDirection-module)) as **Void**
	Draw radial text Draw text oriented along an arc.
- [**drawRectangle**](#drawRectangle-instance_function "drawRectangle (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw a rectangle.
- [**drawRoundedRectangle**](#drawRoundedRectangle-instance_function "drawRoundedRectangle (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), radius as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Draw a rounded rectangle.
- [**drawScaledBitmap**](#drawScaledBitmap-instance_function "drawScaledBitmap (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), bitmap as [Graphics.BitmapType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BitmapType-named_type)) as **Void**
	Draw a scaled bitmap to a surface.
- [**drawText**](#drawText-instance_function "drawText (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type), text as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**, justification as [Graphics.TextJustification](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#TextJustification-module) or [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Draw text at the given location.
- [**fillCircle**](#fillCircle-instance_function "fillCircle (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), radius as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Fill a circle with the foreground color.
- [**fillEllipse**](#fillEllipse-instance_function "fillEllipse (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), a as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), b as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Fill an ellipse with the foreground color.
- [**fillPolygon**](#fillPolygon-instance_function "fillPolygon (Instance Function)") (pts as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.Point2D](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#Point2D-named_type) >) as **Void**
	Fill a polygon with the foreground color.
- [**fillRectangle**](#fillRectangle-instance_function "fillRectangle (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Fill a rectangle with the foreground color.
- [**fillRoundedRectangle**](#fillRoundedRectangle-instance_function "fillRoundedRectangle (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), radius as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Fill a rounded rectangle with the foreground color.
- [**getFontHeight**](#getFontHeight-instance_function "getFontHeight (Instance Function)") (font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the height of a font.
- [**getHeight**](#getHeight-instance_function "getHeight (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the height of the display region that is available to the app.
- [**getTextDimensions**](#getTextDimensions-instance_function "getTextDimensions (Instance Function)") (text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type)) as \[ [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) \]
	Get the width and height of a String.
- [**getTextWidthInPixels**](#getTextWidthInPixels-instance_function "getTextWidthInPixels (Instance Function)") (text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), font as [Graphics.FontType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#FontType-named_type)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the width of a String.
- [**getWidth**](#getWidth-instance_function "getWidth (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the width of the display region that is available to the app.
- [**setAntiAlias**](#setAntiAlias-instance_function "setAntiAlias (Instance Function)") (enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as **Void**
	Enable anti-aliased drawing for primitives This method is not supported for a [BufferedBitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BufferedBitmap.html) that has a palette.
- [**setBlendMode**](#setBlendMode-instance_function "setBlendMode (Instance Function)") (mode as [Graphics.BlendMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#BlendMode-module)) as **Void**
	Set blend mode for drawing.
- [**setClip**](#setClip-instance_function "setClip (Instance Function)") (x as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), y as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), height as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Apply a clipping region to the Dc.
- [**setColor**](#setColor-instance_function "setColor (Instance Function)") (foreground as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type), background as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type)) as **Void**
	Set the current foreground and background colors.
- [**setFill**](#setFill-instance_function "setFill (Instance Function)") (fill as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Graphics.BitmapTexture](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapTexture.html)) as **Void**
	Set fill tool for drawing primitives.
- [**setPenWidth**](#setPenWidth-instance_function "setPenWidth (Instance Function)") (width as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type)) as **Void**
	Set the width of a line.
- [**setStroke**](#setStroke-instance_function "setStroke (Instance Function)") (stroke as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Graphics.BitmapTexture](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapTexture.html)) as **Void**
	Set draw tool for drawing primitives.

## Instance Method Details

### clear() as Void

Note:

Starting form version 3.1.0, COLOR\_TRANSPARENT will also be honored as background color, which will cause the value of pixels in the clip region to be replaced by COLOR\_TRANSPARENT. For example, this can be used to clear the transparent overlay layer so animation background is visible.

### clearClip() as Void

### drawAngledText(x as Lang.Numeric, y as Lang.Numeric, font as Graphics.VectorFont, text as Lang.String, justification as Graphics.TextJustification or Lang.Number, angle as Lang.Numeric) as Void

### drawArc(x as Lang.Numeric, y as Lang.Numeric, r as Lang.Numeric, attr as Graphics.ArcDirection, degreeStart as Lang.Numeric, degreeEnd as Lang.Numeric) as Void

### drawBitmap(x as Lang.Numeric, y as Lang.Numeric, bitmap as Graphics.BitmapType) as Void

Note:

[BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) is only supported in CIQ 4.0.0 and later

### drawBitmap2(x as Lang.Numeric, y as Lang.Numeric, bitmap as Graphics.BitmapType, options as {:bitmapX as Lang.Number,:bitmapY as Lang.Number,:bitmapWidth as Lang.Number,:bitmapHeight as Lang.Number,:tintColor as Graphics.ColorType,:filterMode as Graphics.FilterMode,:transform as Graphics.AffineTransform } or Null) as Void

### drawCircle(x as Lang.Numeric, y as Lang.Numeric, radius as Lang.Numeric) as Void

### drawEllipse(x as Lang.Numeric, y as Lang.Numeric, a as Lang.Numeric, b as Lang.Numeric) as Void

### drawLine(x1 as Lang.Numeric, y1 as Lang.Numeric, x2 as Lang.Numeric, y2 as Lang.Numeric) as Void

### drawOffsetBitmap(x as Lang.Numeric, y as Lang.Numeric, bitmapX as Lang.Numeric, bitmapY as Lang.Numeric, bitmapWidth as Lang.Numeric, bitmapHeight as Lang.Numeric, bitmap as Graphics.BitmapType) as Void

### drawPoint(x as Lang.Numeric, y as Lang.Numeric) as Void

### drawRadialText(x as Lang.Numeric, y as Lang.Numeric, font as Graphics.VectorFont, text as Lang.String, justification as Graphics.TextJustification or Lang.Number, angle as Lang.Numeric, radius as Lang.Numeric, direction as Graphics.RadialTextDirection) as Void

### drawRectangle(x as Lang.Numeric, y as Lang.Numeric, width as Lang.Numeric, height as Lang.Numeric) as Void

### drawRoundedRectangle(x as Lang.Numeric, y as Lang.Numeric, width as Lang.Numeric, height as Lang.Numeric, radius as Lang.Numeric) as Void

### drawScaledBitmap(x as Lang.Numeric, y as Lang.Numeric, width as Lang.Numeric, height as Lang.Numeric, bitmap as Graphics.BitmapType) as Void

### drawText(x as Lang.Numeric, y as Lang.Numeric, font as Graphics.FontType, text as Lang.Object or Null, justification as Graphics.TextJustification or Lang.Number) as Void

Note:

[FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) is only supported in CIQ 4.0.0 and later

### fillCircle(x as Lang.Numeric, y as Lang.Numeric, radius as Lang.Numeric) as Void

### fillEllipse(x as Lang.Numeric, y as Lang.Numeric, a as Lang.Numeric, b as Lang.Numeric) as Void

### fillPolygon(pts as Lang.Array<Graphics.Point2D>) as Void

### fillRectangle(x as Lang.Numeric, y as Lang.Numeric, width as Lang.Numeric, height as Lang.Numeric) as Void

### fillRoundedRectangle(x as Lang.Numeric, y as Lang.Numeric, width as Lang.Numeric, height as Lang.Numeric, radius as Lang.Numeric) as Void

### getFontHeight(font as Graphics.FontType) as Lang.Number

### getHeight() as Lang.Number

### getTextDimensions(text as Lang.String, font as Graphics.FontType) as \[ Lang.Number, Lang.Number \]

### getTextWidthInPixels(text as Lang.String, font as Graphics.FontType) as Lang.Number

### getWidth() as Lang.Number

### setAntiAlias(enabled as Lang.Boolean) as Void

### setBlendMode(mode as Graphics.BlendMode) as Void

Note:

BLEND\_MODE\_NO\_BLEND is only supported while drawing bitmaps

### setClip(x as Lang.Numeric, y as Lang.Numeric, width as Lang.Numeric, height as Lang.Numeric) as Void

### setColor(foreground as Graphics.ColorType, background as Graphics.ColorType) as Void

### setFill(fill as Lang.Number or Graphics.BitmapTexture) as Void

Note:

this function takes precedence over setColor(). If fill tool is not set, the foreground color will be used.

### setPenWidth(width as Lang.Numeric) as Void

### setStroke(stroke as Lang.Number or Graphics.BitmapTexture) as Void

Note:

this function takes precedence over setColor(). If draw tool is not set, the foreground color will be used.
