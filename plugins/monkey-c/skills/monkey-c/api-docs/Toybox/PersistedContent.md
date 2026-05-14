---
title: Toybox.PersistedContent
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/PersistedContent.html
---

## Module: Toybox.PersistedContent

## Overview

## See Also:

- [Toybox.System.Intent](System/Intent.md)
- [Toybox.Communications](Communications.md)
- [Core Topics - Downloading Content](https://developer.garmin.com/connect-iq/core-topics/downloading-content/)
Note:

As a general rule, Fitness and Edge devices will support.FIT format. Outdoor devices will support.GPX format.

## Classes Under Namespace

**Classes:** [Course](PersistedContent/Course.md), [Iterator](PersistedContent/Iterator.md), [Route](PersistedContent/Route.md), [Track](PersistedContent/Track.md), [Waypoint](PersistedContent/Waypoint.md), [Workout](PersistedContent/Workout.md)

## Typedef Summary

- [**Content**](#Content-named_type "Content (Named Type)") as interface {  
	function getName() as [Lang.String](Lang/String.md);  
	function getId() as [Lang.Number](Lang/Number.md);  
	function toIntent() as [System.Intent](System/Intent.md);  
	function remove() as **Void**;  
	}

## Instance Method Summary

- [**getAppCourses**](#getAppCourses-instance_function "getAppCourses (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the subset of courses installed on the system that are owned by the application.
- [**getAppRoutes**](#getAppRoutes-instance_function "getAppRoutes (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the subset of routes installed on the system that are owned by the application.
- [**getAppTracks**](#getAppTracks-instance_function "getAppTracks (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the subset of tracks installed on the system that are owned by the application.
- [**getAppWaypoints**](#getAppWaypoints-instance_function "getAppWaypoints (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the subset of waypoints installed on the system that are owned by the application.
- [**getAppWorkouts**](#getAppWorkouts-instance_function "getAppWorkouts (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the subset of workouts installed on the system that are owned by the application.
- [**getCourses**](#getCourses-instance_function "getCourses (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the courses installed on the system.
- [**getRoutes**](#getRoutes-instance_function "getRoutes (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the routes installed on the system.
- [**getTracks**](#getTracks-instance_function "getTracks (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the tracks installed on the system.
- [**getWaypoints**](#getWaypoints-instance_function "getWaypoints (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the waypoints installed on the system.
- [**getWorkouts**](#getWorkouts-instance_function "getWorkouts (Instance Function)") () as [PersistedContent.Iterator](PersistedContent/Iterator.md)
	Get the workouts installed on the system.
- [**saveWaypoint**](#saveWaypoint-instance_function "saveWaypoint (Instance Function)") (location as [Position.Location](Position/Location.md), options as {:name as [Lang.String](Lang/String.md) } or **Null**) as **Void**
	Save a [Location](Position/Location.md) as a [Waypoint](PersistedContent/Waypoint.md) to the device's location list.
