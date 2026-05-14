---
title: Toybox.WatchUi.Drawable
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html
---

## Class: Toybox.WatchUi.Drawable

## Overview

## Direct Known Subclasses

[WatchUi.Bitmap](Bitmap.md), [WatchUi.Selectable](Selectable.md), [WatchUi.Text](Text.md), [WatchUi.TextArea](TextArea.md)

## Instance Member Summary

- [**height**](#height-var "height (Var)") as [Lang.Numeric](../Lang.md#Numeric-named_type)
	The clip height of the Drawable object.
- [**identifier**](#identifier-var "identifier (Var)") as [Lang.Object](../Lang/Object.md) or **Null**
	The ID used to identify the Drawable object.
- [**isVisible**](#isVisible-var "isVisible (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The visibility of the Drawable object.
- [**locX**](#locX-var "locX (Var)") as [Lang.Numeric](../Lang.md#Numeric-named_type)
	The absolute, on-screen x-coordinate of the Drawable object.
- [**locY**](#locY-var "locY (Var)") as [Lang.Numeric](../Lang.md#Numeric-named_type)
	The absolute, on-screen y-coordinate of the Drawable object.
- [**width**](#width-var "width (Var)") as [Lang.Numeric](../Lang.md#Numeric-named_type)
	The clip width of the Drawable object.

## Instance Method Summary

- [**draw**](#draw-instance_function "draw (Instance Function)") (dc as [Graphics.Dc](../Graphics/Dc.md)) as **Void**
	Draw an object to the device context ([Dc](../Graphics/Dc.md)).
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:identifier as [Lang.Object](../Lang/Object.md),:locX as [Lang.Numeric](../Lang.md#Numeric-named_type),:locY as [Lang.Numeric](../Lang.md#Numeric-named_type),:width as [Lang.Numeric](../Lang.md#Numeric-named_type),:height as [Lang.Numeric](../Lang.md#Numeric-named_type),:visible as [Lang.Boolean](../Lang/Boolean.md) })
	Constructor.
- [**setLocation**](#setLocation-instance_function "setLocation (Instance Function)") (x as [Lang.Numeric](../Lang.md#Numeric-named_type), y as [Lang.Numeric](../Lang.md#Numeric-named_type)) as **Void**
	Set the on-screen location for a Drawable object.
- [**setSize**](#setSize-instance_function "setSize (Instance Function)") (w as [Lang.Numeric](../Lang.md#Numeric-named_type), h as [Lang.Numeric](../Lang.md#Numeric-named_type)) as **Void**
	Set the size of a Drawable object.
- [**setVisible**](#setVisible-instance_function "setVisible (Instance Function)") (visible as [Lang.Boolean](../Lang/Boolean.md)) as **Void**
	Set the visibility of a Drawable object.

## Instance Attribute Details

### var height as Lang.Numeric

### var identifier as Lang.Object or Null

### var isVisible as Lang.Boolean

### var locX as Lang.Numeric

### var locY as Lang.Numeric

### var width as Lang.Numeric

## Instance Method Details

### draw(dc as Graphics.Dc) as Void

### initialize(options as {:identifier as Lang.Object,:locX as Lang.Numeric,:locY as Lang.Numeric,:width as Lang.Numeric,:height as Lang.Numeric,:visible as Lang.Boolean })

Note:

The option `:visible` is only supported with ConnectIQ 3.3.0 and later.
