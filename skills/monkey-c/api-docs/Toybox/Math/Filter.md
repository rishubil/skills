---
title: Toybox.Math.Filter
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/Filter.html
---

## Class: Toybox.Math.Filter

## Overview

## See Also:

- [Filters](https://en.wikipedia.org/wiki/Filter_\(signal_processing\)#Filters_for_removing_noise_from_data)
Note:

An exception will be thrown if the base Filter class version of this method is called.

## Direct Known Subclasses

[Math.FirFilter](https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/FirFilter.html), [Math.IirFilter](https://developer.garmin.com/connect-iq/api-docs/Toybox/Math/IirFilter.html)

## Instance Method Summary

- [**apply**](#apply-instance_function "apply (Instance Function)") (data as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type) >) as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) >
	Apply the Filter to an Array of samples.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (dictionary as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html))
	Constructor.

## Instance Method Details

### apply(data as Lang.Array<Lang.Numeric>) as Lang.Array<Lang.Float>

Note:

An Exception will be thrown if the base Filter class version of this method is called.
