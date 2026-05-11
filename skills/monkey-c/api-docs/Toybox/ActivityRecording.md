---
title: Toybox.ActivityRecording
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording.html
---

## Module: Toybox.ActivityRecording

## Overview

## See Also:

- [Toybox.FitContributor](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor.html)

## Classes Under Namespace

**Classes:** [Session](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording/Session.html)

## Constant Summary

### Sport1

**This has been deprecated**

This enum may be removed after System 8.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SPORT\_GENERIC | 0 | API Level 1.0.0 | Sport used for sports not on the list |
| SPORT\_RUNNING | 1 | API Level 1.0.0 | Sport used for running |
| SPORT\_CYCLING | 2 | API Level 1.0.0 | Sport used for multi-sport transitions |
| SPORT\_TRANSITION | 3 | API Level 1.0.0 |  |
| SPORT\_FITNESS\_EQUIPMENT | 4 | API Level 1.0.0 | Sport used for ANT enabled exercise equipment |
| SPORT\_SWIMMING | 5 | API Level 1.0.0 | Sport used for swimming |
| SPORT\_BASKETBALL | 6 | API Level 1.0.0 | Sport used for basketball |
| SPORT\_SOCCER | 7 | API Level 1.0.0 | Sport used for soccer |
| SPORT\_TENNIS | 8 | API Level 1.0.0 | Sport used for Tennis |
| SPORT\_AMERICAN\_FOOTBALL | 9 | API Level 1.0.0 | Sport used for American football |
| SPORT\_TRAINING | 10 | API Level 1.0.0 | Sport used for activities such as strength training, cardio, etc |
| SPORT\_WALKING | 11 | API Level 1.0.0 | Sport used for walking |
| SPORT\_CROSS\_COUNTRY\_SKIING | 12 | API Level 1.0.0 | Sport used for cross-country skiing |
| SPORT\_ALPINE\_SKIING | 13 | API Level 1.0.0 | Sport used for alpine skiing |
| SPORT\_SNOWBOARDING | 14 | API Level 1.0.0 | Sport used for snowboarding |
| SPORT\_ROWING | 15 | API Level 1.0.0 | Sport used for rowing |
| SPORT\_MOUNTAINEERING | 16 | API Level 1.0.0 | Sport used for mountaineering |
| SPORT\_HIKING | 17 | API Level 1.0.0 | Sport used for hiking |
| SPORT\_MULTISPORT | 18 | API Level 1.0.0 | Sport used for multi-sport events |
| SPORT\_PADDLING | 19 | API Level 1.0.0 | Sport used for paddling |

### Sport2

**This has been deprecated**

This enum may be removed after System 8.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SPORT\_FLYING | 20 | API Level 3.0.10 | Sport used for flying |
| SPORT\_E\_BIKING | 21 | API Level 3.0.10 | Sport used for riding an e-bike |
| SPORT\_MOTORCYCLING | 22 | API Level 3.0.10 | Sport used for motorcycling |
| SPORT\_BOATING | 23 | API Level 3.0.10 | Sport used for boating |
| SPORT\_DRIVING | 24 | API Level 3.0.10 | Sport used for driving |
| SPORT\_GOLF | 25 | API Level 3.0.10 | Sport used for golfing |
| SPORT\_HANG\_GLIDING | 26 | API Level 3.0.10 | Sport used for hang gliding |
| SPORT\_HORSEBACK\_RIDING | 27 | API Level 3.0.10 | Sport used for horseback riding |
| SPORT\_HUNTING | 28 | API Level 3.0.10 | Sport used for hunting |
| SPORT\_FISHING | 29 | API Level 3.0.10 | Sport used for fishing |
| SPORT\_INLINE\_SKATING | 30 | API Level 3.0.10 | Sport used for inline skating |
| SPORT\_ROCK\_CLIMBING | 31 | API Level 3.0.10 | Sport used for rock climbing |
| SPORT\_SAILING | 32 | API Level 3.0.10 | Sport used for sailing |
| SPORT\_ICE\_SKATING | 33 | API Level 3.0.10 | Sport used for ice skating |
| SPORT\_SKY\_DIVING | 34 | API Level 3.0.10 | Sport used for sky diving |
| SPORT\_SNOWSHOEING | 35 | API Level 3.0.10 | Sport used for showshoeing |
| SPORT\_SNOWMOBILING | 36 | API Level 3.0.10 | Sport used for snowmobiling |
| SPORT\_STAND\_UP\_PADDLEBOARDING | 37 | API Level 3.0.10 | Sport used for paddle boarding |
| SPORT\_SURFING | 38 | API Level 3.0.10 | Sport used for surfing |
| SPORT\_WAKEBOARDING | 39 | API Level 3.0.10 | Sport used for wakeboarding |
| SPORT\_WATER\_SKIING | 40 | API Level 3.0.10 | Sport used for water skiing |
| SPORT\_KAYAKING | 41 | API Level 3.0.10 | Sport used for kayaking |
| SPORT\_RAFTING | 42 | API Level 3.0.10 | Sport used for rafting |
| SPORT\_WINDSURFING | 43 | API Level 3.0.10 | Sport used for windsurfing |
| SPORT\_KITESURFING | 44 | API Level 3.0.10 | Sport used for kite surfing |
| SPORT\_TACTICAL | 45 | API Level 3.0.10 | Sport used for tactical |
| SPORT\_JUMPMASTER | 46 | API Level 3.0.10 | Sport used for jumpmaster |
| SPORT\_BOXING | 47 | API Level 3.0.10 | Sport used for boxing |
| SPORT\_FLOOR\_CLIMBING | 48 | API Level 3.0.10 | Sport used for climbing |
| SPORT\_BASEBALL | 49 | API Level 3.0.10 | Sport used for baseball |
| SPORT\_SOFTBALL\_FAST\_PITCH | 50 | API Level 3.0.10 | Sport used for fast pitch softball |
| SPORT\_SOFTBALL\_SLOW\_PITCH | 51 | API Level 3.0.10 | Sport used for slow pitch softball |
| SPORT\_SHOOTING | 56 | API Level 3.0.10 | Sport used for shooting |
| SPORT\_AUTO\_RACING | 57 | API Level 3.0.10 | Sport used for auto racing |

### SubSport

**This has been deprecated**

This enum may be removed after System 8.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SUB\_SPORT\_GENERIC | 0 | API Level 1.0.0 | Sub-sport used if no other sub-sport is applicable |
| SUB\_SPORT\_TREADMILL | 1 | API Level 1.0.0 | Sub-sport for Running and Fitness Equipment |
| SUB\_SPORT\_STREET | 2 | API Level 1.0.0 | Sub-sport for Running |
| SUB\_SPORT\_TRAIL | 3 | API Level 1.0.0 | Sub-sport for Running |
| SUB\_SPORT\_TRACK | 4 | API Level 1.0.0 | Sub-sport for Running |
| SUB\_SPORT\_SPIN | 5 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_INDOOR\_CYCLING | 6 | API Level 1.0.0 | Sub-sport for Cycling and Fitness Equipment |
| SUB\_SPORT\_ROAD | 7 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_MOUNTAIN | 8 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_DOWNHILL | 9 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_RECUMBENT | 10 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_CYCLOCROSS | 11 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_HAND\_CYCLING | 12 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_TRACK\_CYCLING | 13 | API Level 1.0.0 | Sub-sport for Cycling |
| SUB\_SPORT\_INDOOR\_ROWING | 14 | API Level 1.0.0 | Sub-sport for Rowing and Fitness Equipment |
| SUB\_SPORT\_ELLIPTICAL | 15 | API Level 1.0.0 | Sub-sport for Fitness Equipment |
| SUB\_SPORT\_STAIR\_CLIMBING | 16 | API Level 1.0.0 | Sub-sport for Fitness Equipment |
| SUB\_SPORT\_LAP\_SWIMMING | 17 | API Level 1.0.0 | Sub-sport for Swimming |
| SUB\_SPORT\_OPEN\_WATER | 18 | API Level 1.0.0 | Sub-sport for Swimming |
| SUB\_SPORT\_FLEXIBILITY\_TRAINING | 19 | API Level 1.0.0 | Sub-sport for Training |
| SUB\_SPORT\_STRENGTH\_TRAINING | 20 | API Level 1.0.0 | Sub-sport for Training |
| SUB\_SPORT\_WARM\_UP | 21 | API Level 1.0.0 | Sub-sport for Activity Warm-up |
| SUB\_SPORT\_MATCH | 22 | API Level 1.0.0 | Sub-sport for Sports with Matches (e.g. Tennis) |
| SUB\_SPORT\_EXERCISE | 23 | API Level 1.0.0 | Sub-sport for Exercise |
| SUB\_SPORT\_CHALLENGE | 24 | API Level 1.0.0 | Sub-sport for a Sport Challenge |
| SUB\_SPORT\_INDOOR\_SKIING | 25 | API Level 1.0.0 | Sub-sport for Fitness Equipment |
| SUB\_SPORT\_CARDIO\_TRAINING | 26 | API Level 1.0.0 | Sub-sport for Training |

### TimerEventType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| TIMER\_EVENT\_START | 0 | API Level 3.0.10 | Timer start event |
| TIMER\_EVENT\_STOP | 1 | API Level 3.0.10 | Timer stop event |
| TIMER\_EVENT\_PAUSE | 2 | API Level 3.0.10 | Timer pause event |
| TIMER\_EVENT\_RESUME | 3 | API Level 3.0.10 | Timer resume event |
| TIMER\_EVENT\_LAP | 4 | API Level 3.0.10 | Timer lap event |
| TIMER\_EVENT\_RESET | 5 | API Level 3.0.10 | Timer reset |
| TIMER\_EVENT\_WORKOUT\_STEP\_COMPLETE | 6 | API Level 3.0.10 | Workout step complete |
| TIMER\_EVENT\_NEXT\_MULTISPORT\_LEG | 7 | API Level 3.0.10 | Multisport leg started |

## Typedef Summary

- [**Sport**](#Sport-named_type "Sport (Named Type)") as [ActivityRecording.Sport1](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording.html#Sport1-module) or [ActivityRecording.Sport2](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording.html#Sport2-module)

## Instance Method Summary

- [**createSession**](#createSession-instance_function "createSession (Instance Function)") (options as {:sport as [ActivityRecording.Sport](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording.html#Sport-named_type) or [Activity.Sport](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#Sport-module),:subSport as [ActivityRecording.SubSport](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording.html#SubSport-module) or [Activity.SubSport](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SubSport-module),:name as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html),:poolLength as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html),:sensorLogger as [SensorLogging.SensorLogger](https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorLogging/SensorLogger.html),:autoLap as {:type as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html),:entry as \[ [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html), [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) \],:exit as \[ [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html), [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) \] } }) as [ActivityRecording.Session](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording/Session.html)
	Create a [Session](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording/Session.html) object with options determined by the caller.
