---
title: Toybox.AntPlus.SimulationSettings
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/SimulationSettings.html
---

## Class: Toybox.AntPlus.SimulationSettings

## Overview

Represents the wind and track simulation training mode settings on the fitness equipment. Fields may return `null` so you should `null` check values before using them. Values that have not yet been set will return invalid.

## Instance Member Summary

- [**draftFactor**](#draftFactor-var "draftFactor (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The simulated draft factor setting for simulation mode A draft factor of 0 removes all wind resistance, and 1.0 indicates no drafting effects.
- [**slope**](#slope-var "slope (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The slope (grade) setting of the simulated track.
- [**surfaceResistance**](#surfaceResistance-var "surfaceResistance (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The simulated surface resistance coefficient for simulation mode.
- [**windResistance**](#windResistance-var "windResistance (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The simulated wind resistance coefficient setting for simulation mode Wind Resistance Coefficient \[kg/m\] = Frontal Surface Area \[m2\] x Drag Coefficient x Air Density \[kg/m3\].
- [**windSpeed**](#windSpeed-var "windSpeed (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The simulated wind speed setting for simulation mode.

## Instance Attribute Details

### var draftFactor as Lang.Float or Null

The simulated draft factor setting for simulation mode A draft factor of 0 removes all wind resistance, and 1.0 indicates no drafting effects.

### var slope as Lang.Float or Null

The slope (grade) setting of the simulated track

### var surfaceResistance as Lang.Float or Null

The simulated surface resistance coefficient for simulation mode. Dimensionless factor to quantify rolling resistance based on friction between bicycle tires and the tracker surface. Rolling Resistance \[N\] = (Bicycle Mass + Cyclist Mass) x Coefficient of Rolling Resistance x 9.8 Sample coefficients: Wooden track = 0.001 Smooth Concrete = 0.002 Asphalt Road = 0.004 Rough Road = 0.008

### var windResistance as Lang.Float or Null

The simulated wind resistance coefficient setting for simulation mode Wind Resistance Coefficient \[kg/m\] = Frontal Surface Area \[m2\] x Drag Coefficient x Air Density \[kg/m3\]

### var windSpeed as Lang.Float or Null

The simulated wind speed setting for simulation mode
