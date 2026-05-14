---
title: Toybox.Math.FirFilter
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/FirFilter.html
---

## Class: Toybox.Math.FirFilter

Inherits:

Toybox.Math.Filter
- [Toybox.Lang.Object](../Lang/Object.md)
- [Toybox.Math.Filter](Filter.md)
- [Toybox.Math.FirFilter](FirFilter.md)
[show all](#)

## Overview

Finite Impulse Response (FIR) filter implementation.

## See Also:

- [FirFilters](https://en.wikipedia.org/wiki/Finite_impulse_response)

## Instance Method Summary

- [**apply**](#apply-instance_function "apply (Instance Function)") (data as [Lang.Array](../Lang/Array.md) < [Lang.Numeric](../Lang.md#Numeric-named_type) >) as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) >
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (dictionary as {:coefficients as [Lang.Array](../Lang/Array.md) < [Lang.Float](../Lang/Float.md) > or [Lang.ResourceId](../Lang/ResourceId.md),:gain as [Lang.Float](../Lang/Float.md) })
	Constructor.

## Instance Method Details

### apply(data as Lang.Array<Lang.Numeric>) as Lang.Array<Lang.Float>

### initialize(dictionary as {:coefficients as Lang.Array<Lang.Float> or Lang.ResourceId,:gain as Lang.Float })

Constructor
