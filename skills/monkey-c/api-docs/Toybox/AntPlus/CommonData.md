---
title: Toybox.AntPlus.CommonData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/CommonData.html
---

## Class: Toybox.AntPlus.CommonData

## Overview

The CommonData object represents the information shared across all common data types.

Fields may return `null` so you should `null` check values before using them.

## Direct Known Subclasses

[AntPlus.BatteryStatus](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BatteryStatus.html), [AntPlus.BikeLight](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/BikeLight.html), [AntPlus.ManufacturerInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ManufacturerInfo.html), [AntPlus.ProductInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/ProductInfo.html)

## Instance Member Summary

- [**identifier**](#identifier-var "identifier (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The Component Identifier.
- [**numComponents**](#numComponents-var "numComponents (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Number of components in the system.

## Instance Attribute Details

### var identifier as Lang.Number or Null

The Component Identifier.

Component IDs are defined on a by-ANT+-profile basis.

### var numComponents as Lang.Number or Null

Number of components in the system.
