---
title: Toybox.ActivityRecording.Session
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording/Session.html
---

## Class: Toybox.ActivityRecording.Session

## Overview

Session objects control the FIT recording state machine.

## Instance Method Summary

- [**addLap**](#addLap-instance_function "addLap (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Add a lap to the current recording.
- [**createField**](#createField-instance_function "createField (Instance Function)") (name as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), fieldId as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), type as [FitContributor.DataType](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor.html#DataType-module), options as {:count as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:mesgType as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:units as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html),:nativeNum as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) }) as [FitContributor.Field](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html)
	Create a new [Field](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html).
- [**discard**](#discard-instance_function "discard (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Complete the Session by discarding the recorded data.
- [**isRecording**](#isRecording-instance_function "isRecording (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Check if recording is active for this Session.
- [**save**](#save-instance_function "save (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Complete the session by storing the FIT file on the file system.
- [**setTimerEventListener**](#setTimerEventListener-instance_function "setTimerEventListener (Instance Function)") (listener as [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html) (eventType as [ActivityRecording.TimerEventType](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording.html#TimerEventType-module), eventData as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html)) as **Void**) as **Void**
	Set the listener for Session timer events The listener method is called whenever a new timer event occurs.
- [**start**](#start-instance_function "start (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Begin recording a FIT file on the system.
- [**stop**](#stop-instance_function "stop (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Stop recording a FIT file on the system.

## Instance Method Details

### addLap() as Lang.Boolean

Add a lap to the current recording.

### createField(name as Lang.String, fieldId as Lang.Number, type as FitContributor.DataType, options as {:count as Lang.Number,:mesgType as Lang.Number,:units as Lang.String,:nativeNum as Lang.Number }) as FitContributor.Field

Create a new [Field](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html).

Field objects allow developers to store information in FIT developer fields. This information can be displayed in Garmin Connect as a per-second graph, as lap information, or as workout summary information.

### discard() as Lang.Boolean

Complete the Session by discarding the recorded data.

### isRecording() as Lang.Boolean

Check if recording is active for this Session.

### save() as Lang.Boolean

Complete the session by storing the FIT file on the file system.

### setTimerEventListener(listener as Lang.Method(eventType as ActivityRecording.TimerEventType, eventData as Lang.Dictionary) as Void) as Void

Set the listener for Session timer events

The listener method is called whenever a new timer event occurs.

The keys in the Dictionary passed to the listener callback depend on the the value of the eventType parameter.

### start() as Lang.Boolean

Begin recording a FIT file on the system.

### stop() as Lang.Boolean

Stop recording a FIT file on the system.
