---
title: Toybox.Activity.Info
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html
---

## Class: Toybox.Activity.Info

## Overview

## Instance Member Summary

- [**altitude**](#altitude-var "altitude (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The altitude above mean sea level in meters (m).
- [**ambientPressure**](#ambientPressure-var "ambientPressure (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The ambient pressure in Pascals (Pa).
- [**averageCadence**](#averageCadence-var "averageCadence (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The average cadence during the current activity in revolutions per minute (rpm).
- [**averageDistance**](#averageDistance-var "averageDistance (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The average swim stroke distance from the previous interval in meters (m).
- [**averageHeartRate**](#averageHeartRate-var "averageHeartRate (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The average heart rate during the current activity in beats per minute (bpm).
- [**averagePower**](#averagePower-var "averagePower (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The average power during the current activity in Watts (W).
- [**averageSpeed**](#averageSpeed-var "averageSpeed (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The average speed during the current activity in meters per second (mps).
- [**bearing**](#bearing-var "bearing (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The current bearing in radians.
- [**bearingFromStart**](#bearingFromStart-var "bearingFromStart (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The bearing from the starting location to the destination in radians.
- [**calories**](#calories-var "calories (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The calories burned throughout the current activity in kilocalories (kcal).
- [**currentCadence**](#currentCadence-var "currentCadence (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The current cadence in revolutions per minute (rpm).
- [**currentHeading**](#currentHeading-var "currentHeading (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The true north referenced heading in radians.
- [**currentHeartRate**](#currentHeartRate-var "currentHeartRate (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The current heart rate in beats per minute (bpm).
- [**currentLocation**](#currentLocation-var "currentLocation (Var)") as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) or **Null**
	The current location.
- [**currentLocationAccuracy**](#currentLocationAccuracy-var "currentLocationAccuracy (Var)") as [Position.Quality](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#Quality-module) or **Null**
	The current GPS accuracy.
- [**currentOxygenSaturation**](#currentOxygenSaturation-var "currentOxygenSaturation (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The current oxygen saturation in percent (%).
- [**currentPower**](#currentPower-var "currentPower (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The current power in Watts (W).
- [**currentSpeed**](#currentSpeed-var "currentSpeed (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The current speed in meters per second (mps).
- [**distanceToDestination**](#distanceToDestination-var "distanceToDestination (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The distance to the destination in meters (m).
- [**distanceToNextPoint**](#distanceToNextPoint-var "distanceToNextPoint (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The distance to the next point in meters (m).
- [**elapsedDistance**](#elapsedDistance-var "elapsedDistance (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The elapsed distance of the current activity in meters (m).
- [**elapsedTime**](#elapsedTime-var "elapsedTime (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Elapsed time of the current activity in milliseconds (ms).
- [**elevationAtDestination**](#elevationAtDestination-var "elevationAtDestination (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The elevation at the destination in meters (m).
- [**elevationAtNextPoint**](#elevationAtNextPoint-var "elevationAtNextPoint (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The elevation at the next point in meters (m).
- [**energyExpenditure**](#energyExpenditure-var "energyExpenditure (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The current energy expenditure in kilocalories per minute (kcals/min).
- [**frontDerailleurIndex**](#frontDerailleurIndex-var "frontDerailleurIndex (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The current front bicycle derailleur index.
- [**frontDerailleurMax**](#frontDerailleurMax-var "frontDerailleurMax (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The front bicycle derailleur maximum index.
- [**frontDerailleurSize**](#frontDerailleurSize-var "frontDerailleurSize (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The front bicycle derailleur gear size in number of teeth.
- [**maxCadence**](#maxCadence-var "maxCadence (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The maximum cadence recorded during the current activity in revolutions per minute (rpm).
- [**maxHeartRate**](#maxHeartRate-var "maxHeartRate (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The maximum heart rate recorded during the current activity in beats per minute (bpm).
- [**maxPower**](#maxPower-var "maxPower (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The maximum power recorded during the current activity in Watts (W).
- [**maxSpeed**](#maxSpeed-var "maxSpeed (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The maximum speed recorded during the current activity in meters per second (mps).
- [**meanSeaLevelPressure**](#meanSeaLevelPressure-var "meanSeaLevelPressure (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The mean sea level barometric pressure in Pascals (Pa).
- [**nameOfDestination**](#nameOfDestination-var "nameOfDestination (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	The name of the destination.
- [**nameOfNextPoint**](#nameOfNextPoint-var "nameOfNextPoint (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	The name of the next point.
- [**offCourseDistance**](#offCourseDistance-var "offCourseDistance (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The distance to the nearest point on the current course in meters (m).
- [**rawAmbientPressure**](#rawAmbientPressure-var "rawAmbientPressure (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The raw ambient pressure in Pascals (Pa).
- [**rearDerailleurIndex**](#rearDerailleurIndex-var "rearDerailleurIndex (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The current rear bicycle derailleur index.
- [**rearDerailleurMax**](#rearDerailleurMax-var "rearDerailleurMax (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The rear bicycle derailleur maximum index.
- [**rearDerailleurSize**](#rearDerailleurSize-var "rearDerailleurSize (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The rear bicycle derailleur gear size in number of teeth.
- [**startLocation**](#startLocation-var "startLocation (Var)") as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) or **Null**
	The starting location of the current activity.
- [**startTime**](#startTime-var "startTime (Var)") as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) or **Null**
	The starting time of the current activity.
- [**swimStrokeType**](#swimStrokeType-var "swimStrokeType (Var)") as [Activity.SwimStrokeType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SwimStrokeType-module) or **Null**
	The swim stroke type from the previous length.
- [**swimSwolf**](#swimSwolf-var "swimSwolf (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The SWOLF score from the previous length.
- [**timerState**](#timerState-var "timerState (Var)") as [Activity.TimerState](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#TimerState-module) or **Null**
	The recording timer state.
- [**timerTime**](#timerTime-var "timerTime (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The current Timer value in milliseconds (ms).
- [**totalAscent**](#totalAscent-var "totalAscent (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The total ascent during the current activity in meters (m).
- [**totalDescent**](#totalDescent-var "totalDescent (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	The total descent during the current activity in meters (m).
- [**track**](#track-var "track (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The current track in radians.
- [**trainingEffect**](#trainingEffect-var "trainingEffect (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or **Null**
	The Training Effect score of the current activity.
