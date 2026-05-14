---
title: Toybox.ActivityMonitor.Info
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/Info.html
---

## Class: Toybox.ActivityMonitor.Info

## Overview

Note:

Unless otherwise indicated, Info data is calculated for the current day starting at midnight as provided by the device.

## Instance Member Summary

- [**activeMinutesDay**](#activeMinutesDay-var "activeMinutesDay (Var)") as [ActivityMonitor.ActiveMinutes](ActiveMinutes.md) or **Null**
	The number of active minutes for the current day.
- [**activeMinutesWeek**](#activeMinutesWeek-var "activeMinutesWeek (Var)") as [ActivityMonitor.ActiveMinutes](ActiveMinutes.md) or **Null**
	The number of active minutes for the current week.
- [**activeMinutesWeekGoal**](#activeMinutesWeekGoal-var "activeMinutesWeekGoal (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The value of the active minutes goal for the current week.
- [**calories**](#calories-var "calories (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The calories burned so far for the current day in kilocalories (kCal).
- [**distance**](#distance-var "distance (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The distance since midnight for the current day in centimeters (cm).
- [**floorsClimbed**](#floorsClimbed-var "floorsClimbed (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The number of floors climbed for the current day.
- [**floorsClimbedGoal**](#floorsClimbedGoal-var "floorsClimbedGoal (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The current floor climb goal.
- [**floorsDescended**](#floorsDescended-var "floorsDescended (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The number of floors descended for the current day.
- [**isSleepMode**](#isSleepMode-var "isSleepMode (Var)") as [Lang.Boolean](../Lang/Boolean.md) or **Null** deprecated
	Determine whether the device is in sleep mode.
- [**metersClimbed**](#metersClimbed-var "metersClimbed (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The vertical distance of floors climbed in meters (m).
- [**metersDescended**](#metersDescended-var "metersDescended (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The vertical distance of floors descended in meters (m).
- [**moveBarLevel**](#moveBarLevel-var "moveBarLevel (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The current level of the move bar between [MOVE\_BAR\_LEVEL\_MIN](../ActivityMonitor.md#MOVE_BAR_LEVEL_MIN-const) and [MOVE\_BAR\_LEVEL\_MAX](../ActivityMonitor.md#MOVE_BAR_LEVEL_MAX-const).
- [**pushDistance**](#pushDistance-var "pushDistance (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The wheelchair push distance for the day in centimeters (cm).
- [**pushGoal**](#pushGoal-var "pushGoal (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The wheelchair push goal for the day in number of pushes.
- [**pushes**](#pushes-var "pushes (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Wheelchair push count for the day in number of pushes.
- [**respirationRate**](#respirationRate-var "respirationRate (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Current respiration rate for the user, in breaths per minute Value may be `null`.
- [**stepGoal**](#stepGoal-var "stepGoal (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The step goal for the current day in number of steps.
- [**steps**](#steps-var "steps (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The step count since midnight for the current day in number of steps.
- [**stressScore**](#stressScore-var "stressScore (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The current stress score The stress score calculated using a rolling average of the last 30 seconds of stress level readings.
- [**timeToRecovery**](#timeToRecovery-var "timeToRecovery (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Time to recovery from the last activity, in hours Value may be `null`.

## Instance Attribute Details

### var activeMinutesDay as ActivityMonitor.ActiveMinutes or Null

### var activeMinutesWeek as ActivityMonitor.ActiveMinutes or Null

### var activeMinutesWeekGoal as Lang.Number or Null

### var calories as Lang.Number or Null

### var distance as Lang.Number or Null

### var floorsClimbed as Lang.Number or Null

### var floorsClimbedGoal as Lang.Number or Null

### var floorsDescended as Lang.Number or Null

### var isSleepMode as Lang.Boolean or Null

**This has been deprecated**

This value may be removed after System 4.
