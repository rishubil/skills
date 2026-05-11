---
title: Toybox.PersistedContent
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent.html
---

## Module: Toybox.PersistedContent

## Overview

## See Also:

- [Toybox.System.Intent](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Intent.html)
- [Toybox.Communications](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications.html)
- [Core Topics - Downloading Content](https://developer.garmin.com/connect-iq/core-topics/downloading-content/)
Note:

As a general rule, Fitness and Edge devices will support.FIT format. Outdoor devices will support.GPX format.

## Classes Under Namespace

**Classes:** [Course](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Course.html), [Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html), [Route](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Route.html), [Track](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Track.html), [Waypoint](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Waypoint.html), [Workout](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Workout.html)

## Typedef Summary

- [**Content**](#Content-named_type "Content (Named Type)") as interface {  
	function getName() as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html);  
	function getId() as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html);  
	function toIntent() as [System.Intent](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Intent.html);  
	function remove() as **Void**;  
	}

## Instance Method Summary

- [**getAppCourses**](#getAppCourses-instance_function "getAppCourses (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the subset of courses installed on the system that are owned by the application.
- [**getAppRoutes**](#getAppRoutes-instance_function "getAppRoutes (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the subset of routes installed on the system that are owned by the application.
- [**getAppTracks**](#getAppTracks-instance_function "getAppTracks (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the subset of tracks installed on the system that are owned by the application.
- [**getAppWaypoints**](#getAppWaypoints-instance_function "getAppWaypoints (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the subset of waypoints installed on the system that are owned by the application.
- [**getAppWorkouts**](#getAppWorkouts-instance_function "getAppWorkouts (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the subset of workouts installed on the system that are owned by the application.
- [**getCourses**](#getCourses-instance_function "getCourses (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the courses installed on the system.
- [**getRoutes**](#getRoutes-instance_function "getRoutes (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the routes installed on the system.
- [**getTracks**](#getTracks-instance_function "getTracks (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the tracks installed on the system.
- [**getWaypoints**](#getWaypoints-instance_function "getWaypoints (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the waypoints installed on the system.
- [**getWorkouts**](#getWorkouts-instance_function "getWorkouts (Instance Function)") () as [PersistedContent.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Iterator.html)
	Get the workouts installed on the system.
- [**saveWaypoint**](#saveWaypoint-instance_function "saveWaypoint (Instance Function)") (location as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html), options as {:name as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) } or **Null**) as **Void**
	Save a [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) as a [Waypoint](https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent/Waypoint.html) to the device's location list.
