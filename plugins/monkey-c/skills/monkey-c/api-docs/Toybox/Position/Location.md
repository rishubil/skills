---
title: Toybox.Position.Location
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html
---

## Class: Toybox.Position.Location

## Overview

The Location object represents a specific position.

Location objects provide methods for retrieving position coordinates in various formats.

## Instance Method Summary

- [**getProjectedLocation**](#getProjectedLocation-instance_function "getProjectedLocation (Instance Function)") (angle as [Lang.Numeric](../Lang.md#Numeric-named_type), distance as [Lang.Numeric](../Lang.md#Numeric-named_type)) as [Position.Location](Location.md)
	Get a [Location](Location.md) object that is offset from the current position by a given distance and angle.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:latitude as [Lang.Numeric](../Lang.md#Numeric-named_type),:longitude as [Lang.Numeric](../Lang.md#Numeric-named_type),:format as [Lang.Symbol](../Lang/Symbol.md) })
	Constructor Create a Location based on a set of coordinates.
- [**toDegrees**](#toDegrees-instance_function "toDegrees (Instance Function)") () as \[ [Lang.Double](../Lang/Double.md), [Lang.Double](../Lang/Double.md) \]
	Get a Location object's coordinates in degrees.
- [**toGeoString**](#toGeoString-instance_function "toGeoString (Instance Function)") (format as [Position.CoordinateFormat](../Position.md#CoordinateFormat-module)) as [Lang.String](../Lang/String.md)
	Get a String representation a Location object's coordinates.
- [**toRadians**](#toRadians-instance_function "toRadians (Instance Function)") () as \[ [Lang.Double](../Lang/Double.md), [Lang.Double](../Lang/Double.md) \]
	Get a location object's coordinates in radians.

## Instance Method Details

### getProjectedLocation(angle as Lang.Numeric, distance as Lang.Numeric) as Position.Location

Get a [Location](Location.md) object that is offset from the current position by a given distance and angle.

### initialize(options as {:latitude as Lang.Numeric,:longitude as Lang.Numeric,:format as Lang.Symbol })

Constructor Create a Location based on a set of coordinates.

### toDegrees() as \[ Lang.Double, Lang.Double \]

Get a Location object's coordinates in degrees.

### toGeoString(format as Position.CoordinateFormat) as Lang.String

Get a String representation a Location object's coordinates.

### toRadians() as \[ Lang.Double, Lang.Double \]

Get a location object's coordinates in radians.
