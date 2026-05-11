---
title: Toybox.Graphics.BoundingBox
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BoundingBox.html
---

## Class: Toybox.Graphics.BoundingBox

## Overview

## Instance Member Summary

- [**height**](#height-var "height (Var)") as [Lang.Number](../Lang/Number.md)
	Represents the height of the bounding box.
- [**width**](#width-var "width (Var)") as [Lang.Number](../Lang/Number.md)
	Represents the width of the bounding box.
- [**x**](#x-var "x (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Represents the x coordinate for the origin of the bounding box.
- [**y**](#y-var "y (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Represents the y coordinate for the origin of the bounding box.

## Instance Method Summary

- [**addBoundingBox**](#addBoundingBox-instance_function "addBoundingBox (Instance Function)") (box as [Graphics.BoundingBox](BoundingBox.md)) as **Void**
	Expand self to include a bounding box Update `self` to include the full bounding box specified.
- [**addCircle**](#addCircle-instance_function "addCircle (Instance Function)") (x as [Lang.Number](../Lang/Number.md), y as [Lang.Number](../Lang/Number.md), radius as [Lang.Number](../Lang/Number.md)) as **Void**
	Expand self to include a circle Update `self` to include the circle specified.
- [**addEllipse**](#addEllipse-instance_function "addEllipse (Instance Function)") (x as [Lang.Number](../Lang/Number.md), y as [Lang.Number](../Lang/Number.md), a as [Lang.Number](../Lang/Number.md), b as [Lang.Number](../Lang/Number.md)) as **Void**
	Expand self to include an ellipse Update `self` to include the ellipse specified.
- [**addPoint**](#addPoint-instance_function "addPoint (Instance Function)") (x as [Lang.Number](../Lang/Number.md), y as [Lang.Number](../Lang/Number.md)) as **Void**
	Add a point to the bounding box Update `self` to include the point specified.
- [**addPoints**](#addPoints-instance_function "addPoints (Instance Function)") (points as [Lang.Array](../Lang/Array.md) <\[ [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md) \]>) as **Void**
	Add one or more points to a bounding box Update `self` to include all of the points specified.
- [**addRectangle**](#addRectangle-instance_function "addRectangle (Instance Function)") (x as [Lang.Number](../Lang/Number.md), y as [Lang.Number](../Lang/Number.md), width as [Lang.Number](../Lang/Number.md), height as [Lang.Number](../Lang/Number.md)) as **Void**
	Expand self to include a rectangle Update `self` to include the rectangle specified.
- [**expand**](#expand-instance_function "expand (Instance Function)") (dx as [Lang.Number](../Lang/Number.md), dy as [Lang.Number](../Lang/Number.md)) as **Void**
	Expand self by the given offsets Expand `self` by the x and y offsets specified.
- [**includesPoint**](#includesPoint-instance_function "includesPoint (Instance Function)") (x as [Lang.Number](../Lang/Number.md), y as [Lang.Number](../Lang/Number.md)) as [Lang.Boolean](../Lang/Boolean.md)
	Determine if self includes a point Points on the edge of a box are considered to be included since the box would not expand if such a point were added to the box.
- [**normalize**](#normalize-instance_function "normalize (Instance Function)") () as **Void**
	Update self to ensure non-negative width and height values Repair `self` to so that `width` and `height` are non-negative, updating the `x` and `y` coordinates as appropriate.
- [**reset**](#reset-instance_function "reset (Instance Function)") () as **Void**
	Reset self to an invalid state.
- [**valid**](#valid-instance_function "valid (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Check box is valid.
