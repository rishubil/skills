---
title: Toybox.WatchUi.Layer
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html
---

## Class: Toybox.WatchUi.Layer

## Overview

A representation of View Layer that will be drawn (bitblit) by system onto the screen during screen update, which include regular View update (onUpdate/onPartialUpdate) as well as animation playback if supported.

## Direct Known Subclasses

[WatchUi.AnimationLayer](AnimationLayer.md)

## Typedef Summary

- [**Options**](#Options-named_type "Options (Named Type)") as {:locX as [Lang.Numeric](../Lang.md#Numeric-named_type),:locY as [Lang.Numeric](../Lang.md#Numeric-named_type),:width as [Lang.Number](../Lang/Number.md),:height as [Lang.Number](../Lang/Number.md),:colorDepth as [Lang.Number](../Lang/Number.md),:visibility as [Lang.Boolean](../Lang/Boolean.md),:identifier as [Lang.Object](../Lang/Object.md) }

## Instance Method Summary

- [**getDc**](#getDc-instance_function "getDc (Instance Function)") () as [Graphics.Dc](../Graphics/Dc.md) or **Null**
	Get the [Graphics.Dc](../Graphics/Dc.md) to draw on.
- [**getId**](#getId-instance_function "getId (Instance Function)") () as [Lang.Object](../Lang/Object.md) or **Null**
	Layer identifier, can be `null`.
- [**getX**](#getX-instance_function "getX (Instance Function)") () as [Lang.Numeric](../Lang.md#Numeric-named_type)
	Get X-axis absolute draw offset relative to the screen origin.
- [**getY**](#getY-instance_function "getY (Instance Function)") () as [Lang.Numeric](../Lang.md#Numeric-named_type)
	Get Y-axis absolute draw offset relative to the screen origin.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as [Layer.Options](Layer.md#Options-named_type) or **Null**)
	Constructor.
- [**isVisible**](#isVisible-instance_function "isVisible (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
- [**setLocation**](#setLocation-instance_function "setLocation (Instance Function)") (x as [Lang.Numeric](../Lang.md#Numeric-named_type), y as [Lang.Numeric](../Lang.md#Numeric-named_type)) as **Void**
	Set draw offset relative to the screen origin.
- [**setVisible**](#setVisible-instance_function "setVisible (Instance Function)") (visible as [Lang.Boolean](../Lang/Boolean.md)) as **Void**
	Set visibility of the layer, if the layer hasn't been added to a view, or the view isn't on top of view stack, the value will be saved.
- [**setX**](#setX-instance_function "setX (Instance Function)") (x as [Lang.Numeric](../Lang.md#Numeric-named_type)) as **Void**
	Set X-axis absolute draw offset relative to the screen origin.
- [**setY**](#setY-instance_function "setY (Instance Function)") (y as [Lang.Numeric](../Lang.md#Numeric-named_type)) as **Void**
	Set Y-axis absolute draw offset relative to the screen origin.

## Typedef Details

### Options as {:locX as Lang.Numeric,:locY as Lang.Numeric,:width as Lang.Number,:height as Lang.Number,:colorDepth as Lang.Number,:visibility as Lang.Boolean,:identifier as Lang.Object }

## Instance Method Details

### getDc() as Graphics.Dc or Null

Get the [Graphics.Dc](../Graphics/Dc.md) to draw on.

### getId() as Lang.Object or Null

Layer identifier, can be `null`

### getX() as Lang.Numeric

Get X-axis absolute draw offset relative to the screen origin

### getY() as Lang.Numeric

Get Y-axis absolute draw offset relative to the screen origin

### initialize(options as Layer.Options or Null)

Constructor

### isVisible() as Lang.Boolean

### setLocation(x as Lang.Numeric, y as Lang.Numeric) as Void

Set draw offset relative to the screen origin

### setVisible(visible as Lang.Boolean) as Void

Set visibility of the layer, if the layer hasn't been added to a view, or the view isn't on top of view stack, the value will be saved.

### setX(x as Lang.Numeric) as Void

Set X-axis absolute draw offset relative to the screen origin

### setY(y as Lang.Numeric) as Void

Set Y-axis absolute draw offset relative to the screen origin
