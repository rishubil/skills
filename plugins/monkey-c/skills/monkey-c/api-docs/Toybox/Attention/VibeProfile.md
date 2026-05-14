---
title: Toybox.Attention.VibeProfile
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention/VibeProfile.html
---

## Class: Toybox.Attention.VibeProfile

## Overview

Define a vibration pattern.

Vibrations have two characteristics: duty cycle and length. These characteristics are used to define a single VibeProfile object, which can then be passed with a collection of other VibeProfile objects in an Array to the vibrate() method. The vibrate() method will play through each of the VibeProfile objects within the Array in order.

## Instance Member Summary

- [**dutyCycle**](#dutyCycle-var "dutyCycle (Var)") as [Lang.Number](../Lang/Number.md)
	The strength of the vibration.
- [**length**](#length-var "length (Var)") as [Lang.Number](../Lang/Number.md)
	Length of the vibration in milliseconds (ms).

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (dutyCycleVal as [Lang.Number](../Lang/Number.md), lengthVal as [Lang.Number](../Lang/Number.md))
	Constructor.

## Instance Attribute Details

### var dutyCycle as Lang.Number

The strength of the vibration.

Duty cycle is the felt strength of the vibration, and is analogous in practice to the frequency of the vibration. It is specified as a value from 0 to 100%, 0 indicating no vibration and 100 indicating the strongest vibration.

### var length as Lang.Number

Length of the vibration in milliseconds (ms).

## Instance Method Details

### initialize(dutyCycleVal as Lang.Number, lengthVal as Lang.Number)

Constructor
