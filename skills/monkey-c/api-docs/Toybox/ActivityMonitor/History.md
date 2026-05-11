---
title: Toybox.ActivityMonitor.History
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/History.html
---

## Class: Toybox.ActivityMonitor.History

## Overview

A class containing information about the user's activity history.

The fields in this class may return `null`. It is recommended to `null` check a value before using it. If the value is not available, an error indicating that the symbol was not found will be thrown.

## Instance Member Summary

- [**activeMinutes**](#activeMinutes-var "activeMinutes (Var)") as [ActivityMonitor.ActiveMinutes](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/ActiveMinutes.html) or **Null**
	Number of active minutes.
- [**calories**](#calories-var "calories (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The calories for the day in kilocalories (kCal).
- [**distance**](#distance-var "distance (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The distance for the day in centimeters (cm).
- [**floorsClimbed**](#floorsClimbed-var "floorsClimbed (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The number of floors climbed for the day.
- [**floorsClimbedGoal**](#floorsClimbedGoal-var "floorsClimbedGoal (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Floors climbed goal for the day.
- [**floorsDescended**](#floorsDescended-var "floorsDescended (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The number of floors descended for the day.
- [**pushDistance**](#pushDistance-var "pushDistance (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The wheelchair push distance for the day in centimeters (cm).
- [**pushGoal**](#pushGoal-var "pushGoal (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The wheelchair push goal for the day in number of pushes.
- [**pushes**](#pushes-var "pushes (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Wheelchair push count for the day in number of pushes.
- [**startOfDay**](#startOfDay-var "startOfDay (Var)") as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) or **Null**
	A [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) object representing the start time of the day recorded by this History object.
- [**stepGoal**](#stepGoal-var "stepGoal (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The step goal for the day in number of steps.
- [**steps**](#steps-var "steps (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The step count for the day in number of steps.

## Instance Attribute Details

### var activeMinutes as ActivityMonitor.ActiveMinutes or Null

Number of active minutes.

Contains the moderate, vigorous, and total accumulated minutes for the day.

### var calories as Lang.Number or Null

The calories for the day in kilocalories (kCal).

### var distance as Lang.Number or Null

The distance for the day in centimeters (cm).

### var floorsClimbed as Lang.Number or Null

The number of floors climbed for the day.

### var floorsClimbedGoal as Lang.Number or Null

Floors climbed goal for the day.

### var floorsDescended as Lang.Number or Null

The number of floors descended for the day.

### var pushDistance as Lang.Number or Null

The wheelchair push distance for the day in centimeters (cm).

### var pushGoal as Lang.Number or Null

The wheelchair push goal for the day in number of pushes.

### var pushes as Lang.Number or Null

Wheelchair push count for the day in number of pushes.

### var startOfDay as Time.Moment or Null

A [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) object representing the start time of the day recorded by this History object

### var stepGoal as Lang.Number or Null

The step goal for the day in number of steps.

### var steps as Lang.Number or Null

The step count for the day in number of steps.
