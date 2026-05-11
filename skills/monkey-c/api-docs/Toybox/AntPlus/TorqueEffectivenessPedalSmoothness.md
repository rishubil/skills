---
title: Toybox.AntPlus.TorqueEffectivenessPedalSmoothness
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/TorqueEffectivenessPedalSmoothness.html
---

## Class: Toybox.AntPlus.TorqueEffectivenessPedalSmoothness

## Overview

The TorqueEffectivenessPedalSmoothness object represents the instantaneous torque effectiveness and pedal smoothness.

Fields may return `null` so you should `null` check values before using them.

## Instance Member Summary

- [**leftOrCombinedPedalSmoothness**](#leftOrCombinedPedalSmoothness-var "leftOrCombinedPedalSmoothness (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	Left pedal smoothness if separate is supported, else it is the combined smoothness (%).
- [**leftTorqueEffectiveness**](#leftTorqueEffectiveness-var "leftTorqueEffectiveness (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	Left torque effectiveness.
- [**rightPedalSmoothness**](#rightPedalSmoothness-var "rightPedalSmoothness (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	Right pedal smoothness (%).
- [**rightTorqueEffectiveness**](#rightTorqueEffectiveness-var "rightTorqueEffectiveness (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	Right torque effectiveness.
- [**separatePedalSmoothnessSupport**](#separatePedalSmoothnessSupport-var "separatePedalSmoothnessSupport (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or **Null**
	Define if pedal smoothness is separate.

## Instance Attribute Details

### var leftOrCombinedPedalSmoothness as Lang.Float or Null

Left pedal smoothness if separate is supported, else it is the combined smoothness (%).

### var leftTorqueEffectiveness as Lang.Float or Null

Left torque effectiveness.

0xFF: Invalid or negative values (%).

### var rightPedalSmoothness as Lang.Float or Null

Right pedal smoothness (%).

### var rightTorqueEffectiveness as Lang.Float or Null

Right torque effectiveness.

0xFF: Invalid or negative values (%).

### var separatePedalSmoothnessSupport as Lang.Boolean or Null

Define if pedal smoothness is separate.
