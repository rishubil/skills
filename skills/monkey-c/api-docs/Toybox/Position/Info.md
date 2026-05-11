---
title: Toybox.Position.Info
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Info.html
---

## Class: Toybox.Position.Info

## Overview

The Position.Info class contains all of the information provided by the positioning system.

Position Info can be retrieved on every call of [onUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onUpdate-instance_function) or it can be obtained on demand. Fields in this class may return `null` so should be checked for `null` values prior to use.

## Instance Member Summary

- [**accuracy**](#accuracy-var "accuracy (Var)") as [Position.Quality](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#Quality-module)
	The positional accuracy.
- [**altitude**](#altitude-var "altitude (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The elevation above mean sea level in meters (m).
- [**heading**](#heading-var "heading (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The true north referenced heading in radians.
- [**position**](#position-var "position (Var)") as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) or **Null**
	The latitude and longitude of the position.
- [**speed**](#speed-var "speed (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The horizontal speed in meters per second (mps).
- [**when**](#when-var "when (Var)") as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) or **Null**
	The GPS time stamp of the obtained [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) fix.

## Instance Attribute Details

### var accuracy as Position.Quality

The positional accuracy.

This is given as one of the following values: good, usable, poor, or not available, which corresponds with the Position.QUALITY\_\* constants. This cannot be `null`.

### var altitude as Lang.Float or Null

The elevation above mean sea level in meters (m).

Elevation is obtained from the GPS. If no GPS is present, then no valid elevation will be returned.

### var heading as Lang.Float or Null

The true north referenced heading in radians.

This provides the direction of travel when moving. If supported by the device, it provides compass orientation when stopped.

### var position as Position.Location or Null

The latitude and longitude of the position.

If no GPS is available or is between GPS fix intervals (typically 1 second), the position is propagated (i.e. dead-reckoned) using the last known heading and last known speed. After a short period of time, the position will cease to be propagated to avoid excessive accumulation of position errors.

### var speed as Lang.Float or Null

The horizontal speed in meters per second (mps).

Speed is derived from the most accurate source in the following order:

1. GPS
2. Foot pod
3. Accelerometer

### var when as Time.Moment or Null

The GPS time stamp of the obtained [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) fix.
