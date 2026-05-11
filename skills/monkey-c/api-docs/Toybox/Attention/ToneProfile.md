---
title: Toybox.Attention.ToneProfile
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention/ToneProfile.html
---

## Class: Toybox.Attention.ToneProfile

## Overview

Define a tone pattern.

Tones have two characteristics: frequency and duration. These characteristics are used to define a single ToneProfile object, which can then be passed with a collection of other ToneProfile objects in an Array to the playTone() method. The playTone() method will play through each of the ToneProfile objects within the Array in order.

## Instance Member Summary

- [**duration**](#duration-var "duration (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The duration of the tone in milliseconds (ms).
- [**frequency**](#frequency-var "frequency (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The frequency of the tone in hertz (hz).

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (aFrequency as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), aDuration as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html))
	Constructor.

## Instance Attribute Details

### var duration as Lang.Number

The duration of the tone in milliseconds (ms).

### var frequency as Lang.Number

The frequency of the tone in hertz (hz).

## Instance Method Details

### initialize(aFrequency as Lang.Number, aDuration as Lang.Number)

Constructor
