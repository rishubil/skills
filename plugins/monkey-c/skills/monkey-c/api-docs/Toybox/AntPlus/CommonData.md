---
title: Toybox.AntPlus.CommonData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/CommonData.html
---

## Class: Toybox.AntPlus.CommonData

## Overview

The CommonData object represents the information shared across all common data types.

Fields may return `null` so you should `null` check values before using them.

## Direct Known Subclasses

[AntPlus.BatteryStatus](BatteryStatus.md), [AntPlus.BikeLight](BikeLight.md), [AntPlus.ManufacturerInfo](ManufacturerInfo.md), [AntPlus.ProductInfo](ProductInfo.md)

## Instance Member Summary

- [**identifier**](#identifier-var "identifier (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The Component Identifier.
- [**numComponents**](#numComponents-var "numComponents (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Number of components in the system.

## Instance Attribute Details

### var identifier as Lang.Number or Null

The Component Identifier.

Component IDs are defined on a by-ANT+-profile basis.

### var numComponents as Lang.Number or Null

Number of components in the system.
