---
title: Toybox.UserProfile
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/UserProfile.html
---

## Module: Toybox.UserProfile

## Overview

## Classes Under Namespace

**Classes:** [Profile](UserProfile/Profile.md), [UserActivity](UserProfile/UserActivity.md), [UserActivityHistoryIterator](UserProfile/UserActivityHistoryIterator.md)

## Constant Summary

### Gender

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| GENDER\_FEMALE | 0 | API Level 1.0.0 |  |
| GENDER\_MALE | 1 | API Level 1.0.0 |  |
| GENDER\_UNSPECIFIED | 2 | API Level 4.2.3 |  |

### SportHrZone

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| HR\_ZONE\_SPORT\_GENERIC | 0 | API Level 1.2.6 |  |
| HR\_ZONE\_SPORT\_RUNNING | 1 | API Level 1.2.6 |  |
| HR\_ZONE\_SPORT\_BIKING | 2 | API Level 1.2.6 |  |
| HR\_ZONE\_SPORT\_SWIMMING | 3 | API Level 1.2.6 |  |

## Instance Method Summary

- [**getCurrentSport**](#getCurrentSport-instance_function "getCurrentSport (Instance Function)") () as [UserProfile.SportHrZone](UserProfile.md#SportHrZone-module)
	Return the sport for which the current activity retrieves heart rate zone thresholds.
- [**getCurrentSport2**](#getCurrentSport2-instance_function "getCurrentSport2 (Instance Function)") () as \[ [Activity.Sport](Activity.md#Sport-module), [Activity.SubSport](Activity.md#SubSport-module) \]
	Return the sport for the current activity.
- [**getFunctionalThresholdPower**](#getFunctionalThresholdPower-instance_function "getFunctionalThresholdPower (Instance Function)") (sport as [Activity.Sport](Activity.md#Sport-module)) as [Lang.Number](Lang/Number.md) or **Null**
	Return the user's functional threshold power (FTP).
- [**getHeartRateZones**](#getHeartRateZones-instance_function "getHeartRateZones (Instance Function)") (sport as [UserProfile.SportHrZone](UserProfile.md#SportHrZone-module)) as [Lang.Array](Lang/Array.md) < [Lang.Number](Lang/Number.md) >
	Retrieve an [Array](Lang/Array.md) of the current heart rate zone threshold values in beats per minute (bpm) The returned Array contains zone values as follows: \* min zone 1 - The minimum heart rate threshold for zone 1 \* max zone 1 - The maximum heart rate threshold for zone 1 \* max zone 2 - The maximum heart rate threshold for zone 2 \* max zone 3 - The maximum heart rate threshold for zone 3 \* max zone 4 - The maximum heart rate threshold for zone 4 \* max zone 5 - The maximum heart rate threshold for zone 5.
- [**getHeartRateZones2**](#getHeartRateZones2-instance_function "getHeartRateZones2 (Instance Function)") (sport as [Activity.Sport](Activity.md#Sport-module)) as [Lang.Array](Lang/Array.md) < [Lang.Number](Lang/Number.md) > or **Null**
	Retrieve an [Array](Lang/Array.md) of the current heart rate zone threshold values in beats per minute (bpm) The returned Array contains zone values as follows: \* min zone 1 - The minimum heart rate threshold for zone 1 \* max zone 1 - The maximum heart rate threshold for zone 1 \* max zone 2 - The maximum heart rate threshold for zone 2 \* max zone 3 - The maximum heart rate threshold for zone 3 \* max zone 4 - The maximum heart rate threshold for zone 4 \* max zone 5 - The maximum heart rate threshold for zone 5.
- [**getPowerZones**](#getPowerZones-instance_function "getPowerZones (Instance Function)") (sport as [Activity.Sport](Activity.md#Sport-module)) as [Lang.Array](Lang/Array.md) < [Lang.Number](Lang/Number.md) > or **Null**
	Retrieve an [Array](Lang/Array.md) of the current power zone threshold values in watts (W).
- [**getProfile**](#getProfile-instance_function "getProfile (Instance Function)") () as [UserProfile.Profile](UserProfile/Profile.md)
	Retrieve the current [Profile](UserProfile/Profile.md) object.
- [**getUserActivityHistory**](#getUserActivityHistory-instance_function "getUserActivityHistory (Instance Function)") () as [UserProfile.UserActivityHistoryIterator](UserProfile/UserActivityHistoryIterator.md)
	Get an iterator for Activity history for the user.
