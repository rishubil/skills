---
title: Toybox.Application.Properties
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Properties.html
---

## Module: Toybox.Application.Properties

## Overview

## Classes Under Namespace

**Classes:** [InvalidKeyException](Properties/InvalidKeyException.md)

## Typedef Summary

- [**ValueType**](#ValueType-named_type "ValueType (Named Type)") as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md) or [Lang.Long](../Lang/Long.md) or [Lang.Double](../Lang/Double.md) or [Lang.String](../Lang/String.md) or [Lang.Boolean](../Lang/Boolean.md) or [Lang.Array](../Lang/Array.md) < [Properties.ValueType](Properties.md#ValueType-named_type) >

## Instance Method Summary

- [**getValue**](#getValue-instance_function "getValue (Instance Function)") (key as [Lang.String](../Lang/String.md)) as [Properties.ValueType](Properties.md#ValueType-named_type)
	Get the data associated with a given key from application settings.
- [**setValue**](#setValue-instance_function "setValue (Instance Function)") (key as [Lang.String](../Lang/String.md), value as [Properties.ValueType](Properties.md#ValueType-named_type)) as **Void**
	Store the given Application Property.

## Typedef Details

### ValueType as Lang.Number or Lang.Float or Lang.Long or Lang.Double or Lang.String or Lang.Boolean or Lang.Array<Properties.ValueType>

## Instance Method Details

### getValue(key as Lang.String) as Properties.ValueType

### setValue(key as Lang.String, value as Properties.ValueType) as Void

Note:

Background processes cannot save Application Properties
