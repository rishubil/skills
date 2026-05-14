---
title: Toybox.AntPlus.RunningDynamicsData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/RunningDynamicsData.html
---

## Class: Toybox.AntPlus.RunningDynamicsData

## Overview

All running dynamics information. Fields may return `null` so you should `null` check values before using them.

## Instance Member Summary

- [**cadence**](#cadence-var "cadence (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Filtered instantaneous cadence (0 - 255 strides/min).
- [**groundContactBalance**](#groundContactBalance-var "groundContactBalance (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Filtered instantaneous ground contact balance (0 - 100%, 0.03125% precision).
- [**groundContactTime**](#groundContactTime-var "groundContactTime (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Filtered instantaneous ground contact time (0 - 2047 ms).
- [**stanceTime**](#stanceTime-var "stanceTime (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Filtered instantaneous stance time percentage (0 - 100%, 0.25% precision).
- [**stepCount**](#stepCount-var "stepCount (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Step count (rolls over!) (0 - 127 steps).
- [**stepLength**](#stepLength-var "stepLength (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Step Length (0 - 8191 mm).
- [**verticalOscillation**](#verticalOscillation-var "verticalOscillation (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Filtered instantaneous vertical oscillation (0 - 2047 mm, 0.25mm precision).
- [**verticalRatio**](#verticalRatio-var "verticalRatio (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Vertical ratio (0 - 100%, 0.03125% precision).
- [**walkingFlag**](#walkingFlag-var "walkingFlag (Var)") as [Lang.Boolean](../Lang/Boolean.md) or **Null**
	`true` if walking, `false` if running.

## Instance Attribute Details

### var cadence as Lang.Number or Null

Filtered instantaneous cadence (0 - 255 strides/min)

### var groundContactBalance as Lang.Float or Null

Filtered instantaneous ground contact balance (0 - 100%, 0.03125% precision)

### var groundContactTime as Lang.Number or Null

Filtered instantaneous ground contact time (0 - 2047 ms)

### var stanceTime as Lang.Float or Null

Filtered instantaneous stance time percentage (0 - 100%, 0.25% precision)

### var stepCount as Lang.Number or Null

Step count (rolls over!) (0 - 127 steps)

### var stepLength as Lang.Number or Null

Step Length (0 - 8191 mm)

### var verticalOscillation as Lang.Float or Null

Filtered instantaneous vertical oscillation (0 - 2047 mm, 0.25mm precision)

### var verticalRatio as Lang.Float or Null

Vertical ratio (0 - 100%, 0.03125% precision)

### var walkingFlag as Lang.Boolean or Null

`true` if walking, `false` if running
