---
title: Toybox.System.ServiceDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System/ServiceDelegate.html
---

## Class: Toybox.System.ServiceDelegate

## Overview

ServiceDelegate is a class used to service [Background](https://developer.garmin.com/connect-iq/api-docs/Toybox/Background.html) events.

This class is used as the main entry point for background processes. A callback function within the delegate can be used to initiate other system events (e.g. [Communications](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications.html)), but only the delegate function is guaranteed to complete. The Background process may be shut down at any time to handle higher priority processes.

## See Also:

- [Toybox.Background](https://developer.garmin.com/connect-iq/api-docs/Toybox/Background.html)

## Instance Method Summary

- [**onActivityCompleted**](#onActivityCompleted-instance_function "onActivityCompleted (Instance Function)") (activity as {:sport as [Activity.Sport](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#Sport-module),:subSport as [Activity.SubSport](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SubSport-module) }) as **Void**
	The callback method that is triggered when an activity is completed.
- [**onGoalReached**](#onGoalReached-instance_function "onGoalReached (Instance Function)") (goalType as [Application.GoalType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#GoalType-module)) as **Void**
	A callback method that is triggered in the background when a fitness goal is reached.
- [**onOAuthResponse**](#onOAuthResponse-instance_function "onOAuthResponse (Instance Function)") () as **Void**
	The callback method that is triggered in the background when an OAuth response is received from the system.
- [**onPhoneAppMessage**](#onPhoneAppMessage-instance_function "onPhoneAppMessage (Instance Function)") (msg as [Communications.PhoneAppMessage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/PhoneAppMessage.html)) as **Void**
	The callback method that is triggered when a phone app message arrives for this app.
- [**onSleepTime**](#onSleepTime-instance_function "onSleepTime (Instance Function)") () as **Void**
	The callback method that is triggered in the background at the configured sleep time.
- [**onSteps**](#onSteps-instance_function "onSteps (Instance Function)") () as **Void**
	The callback method that is triggered in the background when a step goal is reached.
- [**onTemporalEvent**](#onTemporalEvent-instance_function "onTemporalEvent (Instance Function)") () as **Void**
	A callback method that is triggered in the background when time-based events occur.
- [**onWakeTime**](#onWakeTime-instance_function "onWakeTime (Instance Function)") () as **Void**
	A callback method that is triggered in the background at the configured wake time.

## Instance Method Details

### onActivityCompleted(activity as {:sport as Activity.Sport,:subSport as Activity.SubSport }) as Void

The callback method that is triggered when an activity is completed

### onGoalReached(goalType as Application.GoalType) as Void

A callback method that is triggered in the background when a fitness goal is reached.

### onOAuthResponse() as Void

The callback method that is triggered in the background when an OAuth response is received from the system

### onPhoneAppMessage(msg as Communications.PhoneAppMessage) as Void

The callback method that is triggered when a phone app message arrives for this app

### onSleepTime() as Void

The callback method that is triggered in the background at the configured sleep time.

### onSteps() as Void

The callback method that is triggered in the background when a step goal is reached.

Step goals occur at 1000 step increments.

### onTemporalEvent() as Void

A callback method that is triggered in the background when time-based events occur.

### onWakeTime() as Void

A callback method that is triggered in the background at the configured wake time.
