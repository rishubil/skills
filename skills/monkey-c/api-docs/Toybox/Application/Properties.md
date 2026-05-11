---
title: Toybox.Application.Properties
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Properties.html
---

## Module: Toybox.Application.Properties

## Overview

## Classes Under Namespace

**Classes:** [InvalidKeyException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Properties/InvalidKeyException.html)

## Typedef Summary

- [**ValueType**](#ValueType-named_type "ValueType (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Properties.ValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Properties.html#ValueType-named_type) >

## Instance Method Summary

- [**getValue**](#getValue-instance_function "getValue (Instance Function)") (key as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as [Properties.ValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Properties.html#ValueType-named_type)
	Get the data associated with a given key from application settings.
- [**setValue**](#setValue-instance_function "setValue (Instance Function)") (key as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), value as [Properties.ValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/Properties.html#ValueType-named_type)) as **Void**
	Store the given Application Property.

## Typedef Details

### ValueType as Lang.Number or Lang.Float or Lang.Long or Lang.Double or Lang.String or Lang.Boolean or Lang.Array<Properties.ValueType>

## Instance Method Details

### getValue(key as Lang.String) as Properties.ValueType

### setValue(key as Lang.String, value as Properties.ValueType) as Void

Note:

Background processes cannot save Application Properties
