---
title: Toybox.Activity.SplitInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/SplitInfo.html
---

## Class: Toybox.Activity.SplitInfo

## Overview

## Constant Summary

### SplitType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SPLIT\_TYPE\_PACE\_PRO\_SPLIT | 0 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_ASCENT\_SPLIT | 1 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_DESCENT\_SPLIT | 2 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_INTERVAL\_ACTIVE | 3 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_INTERVAL\_REST | 4 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_INTERVAL\_WARMUP | 5 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_INTERVAL\_COOLDOWN | 6 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_INTERVAL\_RECOVERY | 7 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_INTERVAL\_OTHER | 8 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_CLIMB\_ACTIVE | 9 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_CLIMB\_REST | 10 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_SURF\_ACTIVE | 11 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_RUN\_ACTIVE | 12 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_RUN\_REST | 13 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_WORKOUT\_ROUND | 14 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_LIVE\_EVENT\_SPLIT | 15 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_POWER\_GUIDANCE\_SPLIT | 16 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_RWD\_RUN | 17 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_RWD\_WALK | 18 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_CLIMB\_PRO\_CYCLING\_CLIMB | 19 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_CLIMB\_PRO\_CYCLING\_CLIMB\_SECTION | 20 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_WINDSURF\_ACTIVE | 21 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_RWD\_STAND | 22 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_TRANSITION | 23 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_SWIM\_STRAIGHTNESS | 25 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_ROUND\_ACTIVE | 26 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_ROUND\_REST | 27 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_SKI\_LIFT\_SPLIT | 28 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_SKI\_RUN\_SPLIT | 29 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_OBSTACLE | 30 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_CYCLING\_GROUP\_RIDE | 31 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_DIVE | 32 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_DIVE\_SECTION | 33 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_SURFACE\_TYPE\_UNPAVED | 34 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_MARKER\_MILE | 38 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_MARKER\_KILOMETER | 39 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_MARKER\_HALF\_MARATHON | 40 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_MARKER\_MANUAL | 41 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_SURFACE\_TYPE\_PAVED | 42 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_TIMING\_GATE | 43 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_TIMING\_RUN | 44 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_TACX\_COURSE | 45 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_DOWNHILL\_RUN | 46 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_DOWNHILL\_LIFT | 47 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_SKI\_RUN\_SPLIT\_SECTION | 48 | API Level 5.2.2 |  |
| SPLIT\_TYPE\_INVALID | \-1 | API Level 5.2.2 |  |

## Instance Member Summary

- [**averageSpeed**](#averageSpeed-var "averageSpeed (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Average speed for split in meters per second.
- [**elapsedTime**](#elapsedTime-var "elapsedTime (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Elapsed time for split in milliseconds.
- [**maxSpeed**](#maxSpeed-var "maxSpeed (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Max speed for split in meters per second.
- [**splitDistance**](#splitDistance-var "splitDistance (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Split distance in meters.
- [**splitType**](#splitType-var "splitType (Var)") as [SplitInfo.SplitType](SplitInfo.md#SplitType-module) or **Null**
	Type of split.
- [**timerTime**](#timerTime-var "timerTime (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	Timer time for split in milliseconds.
- [**totalAscent**](#totalAscent-var "totalAscent (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Split ascent in meters.
- [**totalDescent**](#totalDescent-var "totalDescent (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	Split descent in meters.
