---
title: Toybox.Math.IirFilter
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/IirFilter.html
---

## Class: Toybox.Math.IirFilter

Inherits:

Toybox.Math.Filter
- [Toybox.Lang.Object](../Lang/Object.md)
- [Toybox.Math.Filter](Filter.md)
- [Toybox.Math.IirFilter](IirFilter.md)
[show all](#)

## Overview

Infinite Impulse Response (IIR) filter implementation.

## See Also:

- [IirFilters](https://en.wikipedia.org/wiki/Infinite_impulse_response)

## Instance Method Summary

- [**apply**](#apply-instance_function "apply (Instance Function)") (data as [Lang.Array](../Lang/Array.md) < [Lang.Numeric](../Lang.md#Numeric-named_type) >) as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) >
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (dictionary as {:coefficients\_a as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) > or [Lang.ResourceId](../Lang/ResourceId.md),:coefficients\_b as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) > or [Lang.ResourceId](../Lang/ResourceId.md),:gain as [Lang.Float](../Lang/Float.md) })
	Constructor.

## Instance Method Details

### apply(data as Lang.Array<Lang.Numeric>) as Lang.Array<Lang.Float>

### initialize(dictionary as {:coefficients\_a as Lang.Array<Lang.Float> or Lang.ResourceId,:coefficients\_b as Lang.Array<Lang.Float> or Lang.ResourceId,:gain as Lang.Float })

Constructor
