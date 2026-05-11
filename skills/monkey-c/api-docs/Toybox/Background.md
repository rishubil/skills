---
title: Toybox.Background
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Background.html
---

## Module: Toybox.Background

## Overview

## See Also:

- [Toybox.System.ServiceDelegate](System/ServiceDelegate.md)
- [AppBase.onBackgroundData()](Application/AppBase.md#onBackgroundData-instance_function)

## Classes Under Namespace

**Classes:** [ExitDataSizeLimitException](Background/ExitDataSizeLimitException.md), [InvalidBackgroundTimeException](Background/InvalidBackgroundTimeException.md), [MessageSizeLimitException](Background/MessageSizeLimitException.md)

## Instance Method Summary

- [**deleteActivityCompletedEvent**](#deleteActivityCompletedEvent-instance_function "deleteActivityCompletedEvent (Instance Function)") () as **Void**
	Stops the application from receiving activity completed events.
- [**deleteGoalEvent**](#deleteGoalEvent-instance_function "deleteGoalEvent (Instance Function)") (goalType as [Application.GoalType](Application.md#GoalType-module)) as **Void**
	Remove the active goal background event of specified type for the application.
- [**deleteOAuthResponseEvent**](#deleteOAuthResponseEvent-instance_function "deleteOAuthResponseEvent (Instance Function)") () as **Void**
	Remove the OAuth response background event.
- [**deletePhoneAppMessageEvent**](#deletePhoneAppMessageEvent-instance_function "deletePhoneAppMessageEvent (Instance Function)") () as **Void**
	Stops the application from receiving background phone app messages.
- [**deleteSleepEvent**](#deleteSleepEvent-instance_function "deleteSleepEvent (Instance Function)") () as **Void**
	Remove the active sleep background event for the application.
- [**deleteStepsEvent**](#deleteStepsEvent-instance_function "deleteStepsEvent (Instance Function)") () as **Void**
	Remove the active steps background event for the application.
- [**deleteTemporalEvent**](#deleteTemporalEvent-instance_function "deleteTemporalEvent (Instance Function)") () as **Void**
	Remove the active temporal background event for the application.
- [**deleteWakeEvent**](#deleteWakeEvent-instance_function "deleteWakeEvent (Instance Function)") () as **Void**
	Remove the active wake background event for the application.
- [**exit**](#exit-instance_function "exit (Instance Function)") (backgroundData as [Application.PropertyValueType](Application.md#PropertyValueType-named_type)) as **Void**
	Terminates the current background process.
- [**getActivityCompletedEventRegistered**](#getActivityCompletedEventRegistered-instance_function "getActivityCompletedEventRegistered (Instance Function)") () as [Lang.Boolean](Lang/Boolean.md)
	Get whether a background event is registered with [registerForActivityCompletedEvent()](Background.md#registerForActivityCompletedEvent-instance_function).
- [**getBackgroundData**](#getBackgroundData-instance_function "getBackgroundData (Instance Function)") () as [Application.PropertyValueType](Application.md#PropertyValueType-named_type)
	Get data previously saved by a background process.
- [**getGoalEventRegistered**](#getGoalEventRegistered-instance_function "getGoalEventRegistered (Instance Function)") (goalType as [Application.GoalType](Application.md#GoalType-module)) as [Lang.Boolean](Lang/Boolean.md)
	Get whether a background event is registered with [registerForGoalEvent()](Background.md#registerForGoalEvent-instance_function).
- [**getLastTemporalEventTime**](#getLastTemporalEventTime-instance_function "getLastTemporalEventTime (Instance Function)") () as [Time.Moment](Time/Moment.md) or **Null**
	Get the time the last temporal background event was triggered.
- [**getOAuthResponseEventRegistered**](#getOAuthResponseEventRegistered-instance_function "getOAuthResponseEventRegistered (Instance Function)") () as [Lang.Boolean](Lang/Boolean.md)
	Get whether a background event is registered with [registerForOAuthResponseEvent()](Background.md#registerForOAuthResponseEvent-instance_function).
- [**getPhoneAppMessageEventRegistered**](#getPhoneAppMessageEventRegistered-instance_function "getPhoneAppMessageEventRegistered (Instance Function)") () as [Lang.Boolean](Lang/Boolean.md)
	Get whether a background event is registered with [registerForPhoneAppMessageEvent()](Background.md#registerForPhoneAppMessageEvent-instance_function).
- [**getSleepEventRegistered**](#getSleepEventRegistered-instance_function "getSleepEventRegistered (Instance Function)") () as [Lang.Boolean](Lang/Boolean.md)
	Get whether a background event is registered with [registerForSleepEvent()](Background.md#registerForSleepEvent-instance_function).
- [**getStepsEventRegistered**](#getStepsEventRegistered-instance_function "getStepsEventRegistered (Instance Function)") () as [Lang.Boolean](Lang/Boolean.md)
	Get whether a background event is registered with [registerForStepsEvent()](Background.md#registerForStepsEvent-instance_function).
- [**getTemporalEventRegisteredTime**](#getTemporalEventRegisteredTime-instance_function "getTemporalEventRegisteredTime (Instance Function)") () as [Time.Moment](Time/Moment.md) or [Time.Duration](Time/Duration.md) or **Null**
	Get the Moment or Duration with which a background event is registered by [registerForTemporalEvent()](Background.md#registerForTemporalEvent-instance_function).
- [**getWakeEventRegistered**](#getWakeEventRegistered-instance_function "getWakeEventRegistered (Instance Function)") () as [Lang.Boolean](Lang/Boolean.md)
	Get whether a background event is registered with [registerForWakeEvent()](Background.md#registerForWakeEvent-instance_function).
- [**registerForActivityCompletedEvent**](#registerForActivityCompletedEvent-instance_function "registerForActivityCompletedEvent (Instance Function)") () as **Void**
	Registers the application to receive an event whenever an activity is completed.
- [**registerForGoalEvent**](#registerForGoalEvent-instance_function "registerForGoalEvent (Instance Function)") (goalType as [Application.GoalType](Application.md#GoalType-module)) as **Void**
	Register a background event that triggers when the user reaches a specified goal.
- [**registerForOAuthResponseEvent**](#registerForOAuthResponseEvent-instance_function "registerForOAuthResponseEvent (Instance Function)") () as **Void**
	Registers a background event that triggers each time an OAuth login request completes and the token becomes available on the system for use.
- [**registerForPhoneAppMessageEvent**](#registerForPhoneAppMessageEvent-instance_function "registerForPhoneAppMessageEvent (Instance Function)") () as **Void**
	Registers the application to receive an event whenever a phone app message is received.
- [**registerForSleepEvent**](#registerForSleepEvent-instance_function "registerForSleepEvent (Instance Function)") () as **Void**
	Register a background event that triggers at the sleep time configured on the device.
- [**registerForStepsEvent**](#registerForStepsEvent-instance_function "registerForStepsEvent (Instance Function)") () as **Void**
	Registers a background event that triggers each time a multiple of 1000 steps is reached.
- [**registerForTemporalEvent**](#registerForTemporalEvent-instance_function "registerForTemporalEvent (Instance Function)") (time as [Time.Moment](Time/Moment.md) or [Time.Duration](Time/Duration.md)) as **Void**
	Register a background event that triggers at a specific time or at a regular interval.
- [**registerForWakeEvent**](#registerForWakeEvent-instance_function "registerForWakeEvent (Instance Function)") () as **Void**
	Register a background event that triggers at the wake time configured on the device.
- [**requestApplicationWake**](#requestApplicationWake-instance_function "requestApplicationWake (Instance Function)") (message as [Lang.String](Lang/String.md)) as **Void**
	Display a confirmation dialog requesting to launch the application to which the background task belongs.
