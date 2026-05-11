---
title: Toybox.Graphics.AffineTransform
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/AffineTransform.html
---

## Class: Toybox.Graphics.AffineTransform

## Overview

A 2D affine transformation matrix

This is a 2D transform, typically used for converting coordinates from one 2D coordinate system to another. These transformations can represent a sequence of rotations, scales, shears, and translations.

```
| m00  m01  m02 |
| m10  m11  m12 |
|   0    0    1 |
```

## Instance Method Summary

- [**concatenate**](#concatenate-instance_function "concatenate (Instance Function)") (xform as [Graphics.AffineTransform](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/AffineTransform.html)) as **Void**
	Apply the given transform Assign self to the result of the following matrix-matrix product: | m00 m01 m02 | | x00 x01 x02 | | m10 m11 m12 | x | x10 x11 x12 | | 0 0 1 | | 0 0 1 |.
- [**getDeterminant**](#getDeterminant-instance_function "getDeterminant (Instance Function)") () as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)
	Get the transform determinant.
- [**getMatrix**](#getMatrix-instance_function "getMatrix (Instance Function)") () as \[ [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) \]
	Get the transform values Get the underlying values of this transform as an Array | m00 m01 m02 | | m10 m11 m12 | => \[ m00, m01, m02, m10, m11, m12 \] | 0 0 1 |.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	initialize self to the identity transform | 1 0 0 | | 0 1 0 | | 0 0 1 |.
- [**invert**](#invert-instance_function "invert (Instance Function)") () as **Void**
	Invert self.
- [**preConcatenate**](#preConcatenate-instance_function "preConcatenate (Instance Function)") (xform as [Graphics.AffineTransform](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/AffineTransform.html)) as **Void**
	Apply the given transform Assign self to the result of the following matrix-matrix product: | x00 x01 x02 | | m00 m01 m02 | | x10 x11 x12 | x | m10 m11 m12 | | 0 0 1 | | 0 0 1 |.
- [**rotate**](#rotate-instance_function "rotate (Instance Function)") (theta as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Apply a rotation Assign self to the result of the following matrix-matrix product: | m00 m01 m02 | | cos -sin 0 | | m10 m11 m12 | x | sin cos 0 | | 0 0 1 | | 0 0 1 | Equivalent to var xform = new AffineTransform(); xform.setToRotation(theta); self.concatenate(xform);.
- [**scale**](#scale-instance_function "scale (Instance Function)") (sx as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), sy as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Apply a scale Assign self to the result of the following matrix-matrix product: | m00 m01 m02 | | sx 0 0 | | m10 m11 m12 | x | 0 sy 0 | | 0 0 1 | | 0 0 1 | Equivalent to var xform = new AffineTransform(); xform.setToScale(sx, sy); self.concatenate(xform);.
- [**setMatrix**](#setMatrix-instance_function "setMatrix (Instance Function)") (m as \[ [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) \]) as **Void**
	Set the transform values | m00 m01 m02 | \[ m00, m01, m02, m10, m11, m12 \] => | m10 m11 m12 | | 0 0 1 |.
- [**setToRotation**](#setToRotation-instance_function "setToRotation (Instance Function)") (theta as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Set self to a rotation transform | cos -sin 0 | | sin cos 0 | | 0 0 1 |.
- [**setToScale**](#setToScale-instance_function "setToScale (Instance Function)") (sx as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), sy as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Set self to a scale transform | sx 0 0 | | 0 sy 0 | | 0 0 1 |.
- [**setToShear**](#setToShear-instance_function "setToShear (Instance Function)") (shx as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), shy as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Set self to a shear transform | 1 shx 0 | | shy 1 0 | | 0 0 1 |.
- [**setToTranslation**](#setToTranslation-instance_function "setToTranslation (Instance Function)") (tx as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), ty as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Set self to a translation transform | 1 0 tx | | 0 1 ty | | 0 0 1 |.
- [**shear**](#shear-instance_function "shear (Instance Function)") (shx as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), shy as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Apply a shear Assign self to the result of the following matrix-matrix product: | m00 m01 m02 | | 1 shx 0 | | m10 m11 m12 | x | shy 1 0 | | 0 0 1 | | 0 0 1 | Equivalent to var xform = new AffineTransform(); xform.setToShear(shx, shy); self.concatenate(xform);.
- [**transformPoint**](#transformPoint-instance_function "transformPoint (Instance Function)") (pt as [Graphics.Point2D](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#Point2D-named_type)) as [Graphics.Point2D](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#Point2D-named_type)
	Apply transform to a 2D coordinate Transform a single point as if by generating the following matrix-vector product: | m00 m01 m02 | | ptx | | m10 m11 m12 | x | pty | | 0 0 1 | | 1 |.
- [**transformPoints**](#transformPoints-instance_function "transformPoints (Instance Function)") (pts as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.Point2D](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#Point2D-named_type) >) as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Graphics.Point2D](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#Point2D-named_type) >
	Apply transform to an Array of 2D coordinates Transform an array of coordinates.
- [**translate**](#translate-instance_function "translate (Instance Function)") (tx as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), ty as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Apply translation Assign self to the result of the following matrix-matrix product: | m00 m01 m02 | | 1 0 tx | | m10 m11 m12 | x | 0 1 ty | | 0 0 1 | | 0 0 1 | Equivalent to var xform = new AffineTransform(); xform.setToTranslation(tx, ty); self.concatenate(xform);.

## Instance Method Details

### concatenate(xform as Graphics.AffineTransform) as Void

Apply the given transform

Assign self to the result of the following matrix-matrix product:

```
| m00  m01  m02 |   | x00  x01  x02 |
| m10  m11  m12 | x | x10  x11  x12 |
|   0    0    1 |   |   0    0    1 |
```

### getDeterminant() as Lang.Float

### getMatrix() as \[ Lang.Float, Lang.Float, Lang.Float, Lang.Float, Lang.Float, Lang.Float \]

Get the transform values

Get the underlying values of this transform as an Array

```
| m00  m01  m02 |
| m10  m11  m12 | => [ m00, m01, m02, m10, m11, m12 ]
|   0    0    1 |
```

### initialize()

initialize self to the identity transform

```
|   1    0    0 |
|   0    1    0 |
|   0    0    1 |
```

### invert() as Void

### preConcatenate(xform as Graphics.AffineTransform) as Void

Apply the given transform

Assign self to the result of the following matrix-matrix product:

```
| x00  x01  x02 |   | m00  m01  m02 |
| x10  x11  x12 | x | m10  m11  m12 |
|   0    0    1 |   |   0    0    1 |
```

### rotate(theta as Lang.Float) as Void

Apply a rotation

Assign self to the result of the following matrix-matrix product:

```
| m00  m01  m02 |   | cos -sin    0 |
| m10  m11  m12 | x | sin  cos    0 |
|   0    0    1 |   |   0    0    1 |
```

Equivalent to

```
var xform = new AffineTransform();
xform.setToRotation(theta);
self.concatenate(xform);
```

### scale(sx as Lang.Float, sy as Lang.Float) as Void

Apply a scale

Assign self to the result of the following matrix-matrix product:

```
| m00  m01  m02 |   |  sx    0    0 |
| m10  m11  m12 | x |   0   sy    0 |
|   0    0    1 |   |   0    0    1 |
```

Equivalent to

```
var xform = new AffineTransform();
xform.setToScale(sx, sy);
self.concatenate(xform);
```

### setMatrix(m as \[ Lang.Float, Lang.Float, Lang.Float, Lang.Float, Lang.Float, Lang.Float \]) as Void

Set the transform values

```
| m00  m01  m02 |
```

m00, m01, m02, m10, m11, m12

- \=> | m10 m11 m12 |
	```
	|   0    0    1 |
	```

### setToRotation(theta as Lang.Float) as Void

Set self to a rotation transform

```
| cos -sin    0 |
| sin  cos    0 |
|   0    0    1 |
```

### setToScale(sx as Lang.Float, sy as Lang.Float) as Void

Set self to a scale transform

```
|  sx    0    0 |
|   0   sy    0 |
|   0    0    1 |
```

### setToShear(shx as Lang.Float, shy as Lang.Float) as Void

Set self to a shear transform

```
|   1  shx    0 |
| shy    1    0 |
|   0    0    1 |
```

### setToTranslation(tx as Lang.Float, ty as Lang.Float) as Void

Set self to a translation transform

```
|   1    0   tx |
|   0    1   ty |
|   0    0    1 |
```

### shear(shx as Lang.Float, shy as Lang.Float) as Void

Apply a shear

Assign self to the result of the following matrix-matrix product:

```
| m00  m01  m02 |   |   1  shx    0 |
| m10  m11  m12 | x | shy    1    0 |
|   0    0    1 |   |   0    0    1 |
```

Equivalent to

```
var xform = new AffineTransform();
xform.setToShear(shx, shy);
self.concatenate(xform);
```

### transformPoint(pt as Graphics.Point2D) as Graphics.Point2D

Apply transform to a 2D coordinate

Transform a single point as if by generating the following matrix-vector product:

```
| m00  m01  m02 |   | ptx |
| m10  m11  m12 | x | pty |
|   0    0    1 |   |   1 |
```

### transformPoints(pts as Lang.Array<Graphics.Point2D>) as Lang.Array<Graphics.Point2D>

### translate(tx as Lang.Float, ty as Lang.Float) as Void

Apply translation

Assign self to the result of the following matrix-matrix product:

```
| m00  m01  m02 |   |   1    0   tx |
| m10  m11  m12 | x |   0    1   ty |
|   0    0    1 |   |   0    0    1 |
```

Equivalent to

```
var xform = new AffineTransform();
xform.setToTranslation(tx, ty);
self.concatenate(xform);
```
