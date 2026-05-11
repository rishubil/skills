---
title: Toybox.WatchUi.DataField
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html
---

## Class: Toybox.WatchUi.DataField

## Overview

## See Also:

- [Toybox.WatchUi.SimpleDataField](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SimpleDataField.html)
- [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html)
- [Toybox.Graphics](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html)
Note:

The system will call the onUpdate() method inherited from View when a Data Field is displayed by the system. Because compute() and onUpdate() are asynchronous, there is no guarantee that compute() will be called before onUpdate(). For this reason, variables should never be initialized in compute().

## Direct Known Subclasses

[WatchUi.SimpleDataField](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SimpleDataField.html)

## Constant Summary

### Obscurity

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| OBSCURE\_LEFT | 1 | API Level 1.0.0 | Some of the left edge of the device context is obscured |
| OBSCURE\_TOP | 2 | API Level 1.0.0 | Some of the top edge of the device context is obscured |
| OBSCURE\_RIGHT | 4 | API Level 1.0.0 | Some of the right edge of the device context is obscured |
| OBSCURE\_BOTTOM | 8 | API Level 1.0.0 | Some of the bottom edge of the device context is obscured |

### LapTriggerType

Reason for lap creation

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LAP\_TRIGGER\_MANUAL | 0 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_TIME | 1 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_DISTANCE | 2 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_POSITION\_START | 3 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_POSITION\_LAP | 4 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_POSITION\_WAYPOINT | 5 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_POSITION\_MARKED | 6 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_SESSION\_END | 7 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_FITNESS\_EQUIPMENT | 8 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_HEART\_RATE | 9 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_POWER | 10 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_CALORIES | 11 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_PAUSE | 12 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_DOWNHILL\_RUN | 13 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_REP\_COUNTING\_START | 14 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_REP\_COUNTING\_STOP | 15 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_WORKOUT\_STEP\_MANUAL\_RESTART | 16 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_SET\_STOP | 17 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_REP\_STOP | 18 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_POLYLINE | 19 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_EXIT\_CURRENT\_REPEAT | 20 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_WORKOUT\_STEP\_PREVIOUS | 21 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_DEPTH | 22 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_TIMING\_GATE | 23 | API Level 5.2.2 |  |
| LAP\_TRIGGER\_WORKOUT\_CANCELLED | 24 | API Level 5.2.2 |  |

## Typedef Summary

- [**LapInfoType**](#LapInfoType-named_type "LapInfoType (Named Type)") as {:lapTrigger as [DataField.LapTriggerType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html#LapTriggerType-module) }
- [**RouteTarget**](#RouteTarget-named_type "RouteTarget (Named Type)") as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) or [PersistedContent.Waypoint](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Waypoint.html)
- [**Workout**](#Workout-named_type "Workout (Named Type)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Activity.WorkoutStepInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/WorkoutStepInfo.html) > or [PersistedContent.Workout](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Workout.html)

## Instance Method Summary

- [**compute**](#compute-instance_function "compute (Instance Function)") (info as [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html))
	Retrieve [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html) in a DataField.
- [**createField**](#createField-instance_function "createField (Instance Function)") (name as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), fieldId as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), type as [FitContributor.DataType](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor.html#DataType-module), options as {:count as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:mesgType as [FitContributor.MessageType](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor.html#MessageType-module),:units as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) }) as [FitContributor.Field](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html)
	Create a new custom FIT [Field](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html).
- [**getBackgroundColor**](#getBackgroundColor-instance_function "getBackgroundColor (Instance Function)") () as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type)
	Get the current Data Field background color.
- [**getObscurityFlags**](#getObscurityFlags-instance_function "getObscurityFlags (Instance Function)") () as [DataField.Obscurity](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html#Obscurity-module)
	Get the screen regions that are obscured.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onNextMultisportLeg**](#onNextMultisportLeg-instance_function "onNextMultisportLeg (Instance Function)") () as **Void**
	The device has transitioned to the next multisport leg.
- [**onTimerLap**](#onTimerLap-instance_function "onTimerLap (Instance Function)") () as **Void**
	A lap event has occurred.
- [**onTimerLap2**](#onTimerLap2-instance_function "onTimerLap2 (Instance Function)") (trigger as [DataField.LapInfoType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html#LapInfoType-named_type)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A lap event has occurred.
- [**onTimerPause**](#onTimerPause-instance_function "onTimerPause (Instance Function)") () as **Void**
	The activity timer is paused.
- [**onTimerReset**](#onTimerReset-instance_function "onTimerReset (Instance Function)") () as **Void**
	The current activity has ended.
- [**onTimerResume**](#onTimerResume-instance_function "onTimerResume (Instance Function)") () as **Void**
	The activity time has resumed.
- [**onTimerSplitEnd**](#onTimerSplitEnd-instance_function "onTimerSplitEnd (Instance Function)") (info as [Activity.SplitInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/SplitInfo.html)) as **Void**
	A split has ended This method is called when a split is ended in the current activity.
- [**onTimerSplitStart**](#onTimerSplitStart-instance_function "onTimerSplitStart (Instance Function)") (info as [Activity.SplitInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/SplitInfo.html)) as **Void**
	A split has started This method is called when a split is added to the current activity.
- [**onTimerStart**](#onTimerStart-instance_function "onTimerStart (Instance Function)") () as **Void**
	The activity timer has started.
- [**onTimerStop**](#onTimerStop-instance_function "onTimerStop (Instance Function)") () as **Void**
	The activity timer has stopped.
- [**onWorkoutStarted**](#onWorkoutStarted-instance_function "onWorkoutStarted (Instance Function)") () as **Void**
	The current workout is started.
- [**onWorkoutStepComplete**](#onWorkoutStepComplete-instance_function "onWorkoutStepComplete (Instance Function)") () as **Void**
	The current workout step is complete.
- [**routeTo**](#routeTo-instance_function "routeTo (Instance Function)") (target as [DataField.RouteTarget](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html#RouteTarget-named_type), options as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Set the activity's destination.
- [**setWorkout**](#setWorkout-instance_function "setWorkout (Instance Function)") (workout as [DataField.Workout](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html#Workout-named_type), options as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Set the activity's workout.
- [**showAlert**](#showAlert-instance_function "showAlert (Instance Function)") (alertView as [WatchUi.DataFieldAlert](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataFieldAlert.html)) as **Void**
	Show an alert.

## Typedef Details

### LapInfoType as {:lapTrigger as DataField.LapTriggerType }

### RouteTarget as Position.Location or PersistedContent.Waypoint

### Workout as Lang.Array<Activity.WorkoutStepInfo> or PersistedContent.Workout

## Instance Method Details

### compute(info as Activity.Info)

### createField(name as Lang.String, fieldId as Lang.Number, type as FitContributor.DataType, options as {:count as Lang.Number,:mesgType as FitContributor.MessageType,:units as Lang.String }) as FitContributor.Field

### getBackgroundColor() as Graphics.ColorType

### getObscurityFlags() as DataField.Obscurity

### initialize()

### onNextMultisportLeg() as Void

### onTimerLap() as Void

### onTimerLap2(trigger as DataField.LapInfoType) as Lang.Boolean

### onTimerPause() as Void

### onTimerReset() as Void

### onTimerResume() as Void

### onTimerSplitEnd(info as Activity.SplitInfo) as Void

### onTimerSplitStart(info as Activity.SplitInfo) as Void

### onTimerStart() as Void

### onTimerStop() as Void

### onWorkoutStarted() as Void

### onWorkoutStepComplete() as Void

### routeTo(target as DataField.RouteTarget, options as Lang.Dictionary or Null) as Lang.Boolean

### setWorkout(workout as DataField.Workout, options as Lang.Dictionary or Null) as Lang.Boolean

If using a Toybox::Activity:WorkoutStepInfo to set the workout, `WorkoutStepInfo.sport` and `WorkoutStepInfo.subsport` will be ignored and set to the current activity's settings. If setting `.WorkoutStepInfo.step` to a Toybox::Activity.WorkoutStep:

```
* +WorkoutStep.durationType+ can only be set to +Activity.WORKOUT_STEP_DURATION_TIME+ or +Activity.WORKOUT_STEP_DURATION_DISTANCE+.
```
- For `Activity.WORKOUT_STEP_DURATION_TIME`, `WorkoutStep.durationValue` is in seconds.
- For `Activity.WORKOUT_STEP_DURATION_DISTANCE`, `WorkoutStep.durationValue` is in meters.
- The values of `WorkoutStep.targetValueLow` and `WorkoutStep.targetValueHigh` depends on the value of `WorkoutStep.targetType`. See the FIT SDK for more details. If setting `.WorkoutStepInfo.step` to a Toybox::Activity.WorkoutIntervalStep:
- `WorkoutIntervalStep.repetitionNumber` is the number of times to repeat the interval.
- The `WorkoutIntervalStep.activeStep` will occur first, followed by `WorkoutIntervalStep.restStep`.
- If the intensity of the step following a `WorkoutIntervalStep` is `Activity.WORKOUT_INTENSITY_COOLDOWN`, the final rest step will be skipped. If using a Toybox::PersistedContent::Workout, note that:
- The workout's sport must match the current activity.
- The workout's subsport must either match the current activity or set to generic, all or invalid.
