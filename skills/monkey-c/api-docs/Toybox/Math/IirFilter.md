---
title: Toybox.Math.IirFilter
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/IirFilter.html
---

## Class: Toybox.Math.IirFilter

Inherits:

Toybox.Math.Filter
- [Toybox.Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)
- [Toybox.Math.Filter](https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/Filter.html)
- [Toybox.Math.IirFilter](https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/IirFilter.html)
[show all](#)

## Overview

Infinite Impulse Response (IIR) filter implementation.

## See Also:

- [IirFilters](https://en.wikipedia.org/wiki/Infinite_impulse_response)

## Instance Method Summary

- [**apply**](#apply-instance_function "apply (Instance Function)") (data as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type) >) as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) >
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (dictionary as {:coefficients\_a as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) > or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:coefficients\_b as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) > or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:gain as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) })
	Constructor.

## Instance Method Details

### apply(data as Lang.Array<Lang.Numeric>) as Lang.Array<Lang.Float>

### initialize(dictionary as {:coefficients\_a as Lang.Array<Lang.Float> or Lang.ResourceId,:coefficients\_b as Lang.Array<Lang.Float> or Lang.ResourceId,:gain as Lang.Float })

Constructor
