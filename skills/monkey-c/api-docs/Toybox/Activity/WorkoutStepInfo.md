---
title: Toybox.Activity.WorkoutStepInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/WorkoutStepInfo.html
---

## Class: Toybox.Activity.WorkoutStepInfo

## Overview

The WorkoutStepInfo class contains information about the current workout.

This information can be retrieved with the [getCurrentWorkoutStep()](../Activity.md#getCurrentWorkoutStep-instance_function) or [getNextWorkoutStep()](../Activity.md#getNextWorkoutStep-instance_function) methods.

## Instance Member Summary

- [**intensity**](#intensity-var "intensity (Var)") as [Activity.WorkoutIntensity](../Activity.md#WorkoutIntensity-module)
	The intensity of the step.
- [**name**](#name-var "name (Var)") as [Lang.String](../Lang/String.md)
	The name of the current step.
- [**notes**](#notes-var "notes (Var)") as [Lang.String](../Lang/String.md)
	The notes for the current step.
- [**sport**](#sport-var "sport (Var)") as [Activity.Sport](../Activity.md#Sport-module)
	The sport for the workout step.
- [**step**](#step-var "step (Var)") as [Activity.WorkoutStep](WorkoutStep.md) or [Activity.WorkoutIntervalStep](WorkoutIntervalStep.md)
	Duration and target information about the step.
- [**subSport**](#subSport-var "subSport (Var)") as [Activity.SubSport](../Activity.md#SubSport-module) or **Null**
	The subsport for the workout step.

## Instance Attribute Details

### var intensity as Activity.WorkoutIntensity

The intensity of the step

### var name as Lang.String

The name of the current step

### var notes as Lang.String

The notes for the current step

### var sport as Activity.Sport

The sport for the workout step

### var step as Activity.WorkoutStep or Activity.WorkoutIntervalStep

Duration and target information about the step

### var subSport as Activity.SubSport or Null

The subsport for the workout step. Currently only valid for breathing and swim workouts
