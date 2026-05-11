---
title: Toybox.AntPlus.FitnessEquipmentData
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/FitnessEquipmentData.html
---

## Class: Toybox.AntPlus.FitnessEquipmentData

## Overview

Represents general fitness equipment transmitted data. Fields may return `null` so you should `null` check values before using them.

## Instance Member Summary

- [**feDistance**](#feDistance-var "feDistance (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The elapsed distance calculated by the trainer since reset Range is always greater than or equal to 0m.
- [**feHeartRate**](#feHeartRate-var "feHeartRate (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The heart rate calculated by the trainer.
- [**feSpeed**](#feSpeed-var "feSpeed (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The speed calculated by the trainer.

## Instance Attribute Details

### var feDistance as Lang.Float or Null

The elapsed distance calculated by the trainer since reset Range is always greater than or equal to 0m

### var feHeartRate as Lang.Float or Null

The heart rate calculated by the trainer. This may come from hand sensors, or an HRM if connected to the equipment

### var feSpeed as Lang.Float or Null

The speed calculated by the trainer
