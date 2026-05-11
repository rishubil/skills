---
title: Toybox.Activity
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html
---

## Module: Toybox.Activity

## Overview

## Classes Under Namespace

**Classes:** [Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html), [ProfileInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/ProfileInfo.html), [SplitInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/SplitInfo.html), [WorkoutIntervalStep](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/WorkoutIntervalStep.html), [WorkoutStep](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/WorkoutStep.html), [WorkoutStepInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/WorkoutStepInfo.html)

## Constant Summary

### SwimStrokeType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SWIM\_STROKE\_FREESTYLE | 0 | API Level 1.2.2 | Freestyle stroke |
| SWIM\_STROKE\_BACKSTROKE | 1 | API Level 1.2.2 | Backstroke |
| SWIM\_STROKE\_BREASTSTROKE | 2 | API Level 1.2.2 | Breaststroke |
| SWIM\_STROKE\_BUTTERFLY | 3 | API Level 1.2.2 | Butterfly stroke |
| SWIM\_STROKE\_DRILL | 4 | API Level 1.2.2 | Drill mode |
| SWIM\_STROKE\_MIXED | 5 | API Level 1.2.2 | Mixed stroke mode |
| SWIM\_STROKE\_IM | 6 | API Level 1.2.2 | Mixed interval with equal number of butterfly, backstroke, breaststroke, and freestyle, in that order. |

### TimerState

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| TIMER\_STATE\_OFF | 0 | API Level 2.1.0 | The timer is off. There is not an active recording |
| TIMER\_STATE\_STOPPED | 1 | API Level 2.1.0 | The timer is stopped. The recording is active, with the timer stopped. |
| TIMER\_STATE\_PAUSED | 2 | API Level 2.1.0 | The timer is paused. The recording is active with the timer paused. This state occurs when the timer is active, but has been stopped with the Auto-Pause feature. |
| TIMER\_STATE\_ON | 3 | API Level 2.1.0 | The timer is on. The recording is active and the timer is running. |

### Sport

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SPORT\_GENERIC | 0 | API Level 3.2.0 |  |
| SPORT\_RUNNING | 1 | API Level 3.2.0 |  |
| SPORT\_CYCLING | 2 | API Level 3.2.0 |  |
| SPORT\_TRANSITION | 3 | API Level 3.2.0 |  |
| SPORT\_FITNESS\_EQUIPMENT | 4 | API Level 3.2.0 |  |
| SPORT\_SWIMMING | 5 | API Level 3.2.0 |  |
| SPORT\_BASKETBALL | 6 | API Level 3.2.0 |  |
| SPORT\_SOCCER | 7 | API Level 3.2.0 |  |
| SPORT\_TENNIS | 8 | API Level 3.2.0 |  |
| SPORT\_AMERICAN\_FOOTBALL | 9 | API Level 3.2.0 |  |
| SPORT\_TRAINING | 10 | API Level 3.2.0 |  |
| SPORT\_WALKING | 11 | API Level 3.2.0 |  |
| SPORT\_CROSS\_COUNTRY\_SKIING | 12 | API Level 3.2.0 |  |
| SPORT\_ALPINE\_SKIING | 13 | API Level 3.2.0 |  |
| SPORT\_SNOWBOARDING | 14 | API Level 3.2.0 |  |
| SPORT\_ROWING | 15 | API Level 3.2.0 |  |
| SPORT\_MOUNTAINEERING | 16 | API Level 3.2.0 |  |
| SPORT\_HIKING | 17 | API Level 3.2.0 |  |
| SPORT\_MULTISPORT | 18 | API Level 3.2.0 |  |
| SPORT\_PADDLING | 19 | API Level 3.2.0 |  |
| SPORT\_FLYING | 20 | API Level 3.2.0 |  |
| SPORT\_E\_BIKING | 21 | API Level 3.2.0 |  |
| SPORT\_MOTORCYCLING | 22 | API Level 3.2.0 |  |
| SPORT\_BOATING | 23 | API Level 3.2.0 |  |
| SPORT\_DRIVING | 24 | API Level 3.2.0 |  |
| SPORT\_GOLF | 25 | API Level 3.2.0 |  |
| SPORT\_HANG\_GLIDING | 26 | API Level 3.2.0 |  |
| SPORT\_HORSEBACK\_RIDING | 27 | API Level 3.2.0 |  |
| SPORT\_HUNTING | 28 | API Level 3.2.0 |  |
| SPORT\_FISHING | 29 | API Level 3.2.0 |  |
| SPORT\_INLINE\_SKATING | 30 | API Level 3.2.0 |  |
| SPORT\_ROCK\_CLIMBING | 31 | API Level 3.2.0 |  |
| SPORT\_SAILING | 32 | API Level 3.2.0 |  |
| SPORT\_ICE\_SKATING | 33 | API Level 3.2.0 |  |
| SPORT\_SKY\_DIVING | 34 | API Level 3.2.0 |  |
| SPORT\_SNOWSHOEING | 35 | API Level 3.2.0 |  |
| SPORT\_SNOWMOBILING | 36 | API Level 3.2.0 |  |
| SPORT\_STAND\_UP\_PADDLEBOARDING | 37 | API Level 3.2.0 |  |
| SPORT\_SURFING | 38 | API Level 3.2.0 |  |
| SPORT\_WAKEBOARDING | 39 | API Level 3.2.0 |  |
| SPORT\_WATER\_SKIING | 40 | API Level 3.2.0 |  |
| SPORT\_KAYAKING | 41 | API Level 3.2.0 |  |
| SPORT\_RAFTING | 42 | API Level 3.2.0 |  |
| SPORT\_WINDSURFING | 43 | API Level 3.2.0 |  |
| SPORT\_KITESURFING | 44 | API Level 3.2.0 |  |
| SPORT\_TACTICAL | 45 | API Level 3.2.0 |  |
| SPORT\_JUMPMASTER | 46 | API Level 3.2.0 |  |
| SPORT\_BOXING | 47 | API Level 3.2.0 |  |
| SPORT\_FLOOR\_CLIMBING | 48 | API Level 3.2.0 |  |
| SPORT\_BASEBALL | 49 | API Level 3.2.0 |  |
| SPORT\_SOFTBALL\_FAST\_PITCH | 50 | API Level 3.2.0 |  |
| SPORT\_SOFTBALL\_SLOW\_PITCH | 51 | API Level 3.2.0 |  |
| SPORT\_SHOOTING | 56 | API Level 3.2.0 |  |
| SPORT\_AUTO\_RACING | 57 | API Level 3.2.0 |  |
| SPORT\_WINTER\_SPORT | 58 | API Level 4.1.6 |  |
| SPORT\_GRINDING | 59 | API Level 4.1.6 |  |
| SPORT\_HEALTH\_MONITORING | 60 | API Level 4.1.6 |  |
| SPORT\_MARINE | 61 | API Level 4.1.6 |  |
| SPORT\_HIIT | 62 | API Level 4.1.6 |  |
| SPORT\_VIDEO\_GAMING | 63 | API Level 4.1.6 |  |
| SPORT\_RACKET | 64 | API Level 4.1.6 |  |
| SPORT\_WHEELCHAIR\_PUSH\_WALK | 65 | API Level 4.1.6 |  |
| SPORT\_WHEELCHAIR\_PUSH\_RUN | 66 | API Level 4.1.6 |  |
| SPORT\_MEDITATION | 67 | API Level 4.1.6 |  |
| SPORT\_PARA\_SPORT | 68 | API Level 4.1.6 |  |
| SPORT\_DISC\_GOLF | 69 | API Level 4.1.6 |  |
| SPORT\_TEAM\_SPORT | 70 | API Level 4.1.6 |  |
| SPORT\_CRICKET | 71 | API Level 4.1.6 |  |
| SPORT\_RUGBY | 72 | API Level 4.1.6 |  |
| SPORT\_HOCKEY | 73 | API Level 4.1.6 |  |
| SPORT\_LACROSSE | 74 | API Level 4.1.6 |  |
| SPORT\_VOLLEYBALL | 75 | API Level 4.1.6 |  |
| SPORT\_WATER\_TUBING | 76 | API Level 4.1.6 |  |
| SPORT\_WAKESURFING | 77 | API Level 4.1.6 |  |
| SPORT\_INVALID | 255 | API Level 3.2.0 |  |

### SubSport

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SUB\_SPORT\_GENERIC | 0 | API Level 3.2.0 |  |
| SUB\_SPORT\_TREADMILL | 1 | API Level 3.2.0 |  |
| SUB\_SPORT\_STREET | 2 | API Level 3.2.0 |  |
| SUB\_SPORT\_TRAIL | 3 | API Level 3.2.0 |  |
| SUB\_SPORT\_TRACK | 4 | API Level 3.2.0 |  |
| SUB\_SPORT\_SPIN | 5 | API Level 3.2.0 |  |
| SUB\_SPORT\_INDOOR\_CYCLING | 6 | API Level 3.2.0 |  |
| SUB\_SPORT\_ROAD | 7 | API Level 3.2.0 |  |
| SUB\_SPORT\_MOUNTAIN | 8 | API Level 3.2.0 |  |
| SUB\_SPORT\_DOWNHILL | 9 | API Level 3.2.0 |  |
| SUB\_SPORT\_RECUMBENT | 10 | API Level 3.2.0 |  |
| SUB\_SPORT\_CYCLOCROSS | 11 | API Level 3.2.0 |  |
| SUB\_SPORT\_HAND\_CYCLING | 12 | API Level 3.2.0 |  |
| SUB\_SPORT\_TRACK\_CYCLING | 13 | API Level 3.2.0 |  |
| SUB\_SPORT\_INDOOR\_ROWING | 14 | API Level 3.2.0 |  |
| SUB\_SPORT\_ELLIPTICAL | 15 | API Level 3.2.0 |  |
| SUB\_SPORT\_STAIR\_CLIMBING | 16 | API Level 3.2.0 |  |
| SUB\_SPORT\_LAP\_SWIMMING | 17 | API Level 3.2.0 |  |
| SUB\_SPORT\_OPEN\_WATER | 18 | API Level 3.2.0 |  |
| SUB\_SPORT\_FLEXIBILITY\_TRAINING | 19 | API Level 3.2.0 |  |
| SUB\_SPORT\_STRENGTH\_TRAINING | 20 | API Level 3.2.0 |  |
| SUB\_SPORT\_WARM\_UP | 21 | API Level 3.2.0 |  |
| SUB\_SPORT\_MATCH | 22 | API Level 3.2.0 |  |
| SUB\_SPORT\_EXERCISE | 23 | API Level 3.2.0 |  |
| SUB\_SPORT\_CHALLENGE | 24 | API Level 3.2.0 |  |
| SUB\_SPORT\_INDOOR\_SKIING | 25 | API Level 3.2.0 |  |
| SUB\_SPORT\_CARDIO\_TRAINING | 26 | API Level 3.2.0 |  |
| SUB\_SPORT\_INDOOR\_WALKING | 27 | API Level 4.1.6 |  |
| SUB\_SPORT\_E\_BIKE\_FITNESS | 28 | API Level 4.1.6 |  |
| SUB\_SPORT\_BMX | 29 | API Level 4.1.6 |  |
| SUB\_SPORT\_CASUAL\_WALKING | 30 | API Level 4.1.6 |  |
| SUB\_SPORT\_SPEED\_WALKING | 31 | API Level 4.1.6 |  |
| SUB\_SPORT\_BIKE\_TO\_RUN\_TRANSITION | 32 | API Level 4.1.6 |  |
| SUB\_SPORT\_RUN\_TO\_BIKE\_TRANSITION | 33 | API Level 4.1.6 |  |
| SUB\_SPORT\_SWIM\_TO\_BIKE\_TRANSITION | 34 | API Level 4.1.6 |  |
| SUB\_SPORT\_ATV | 35 | API Level 4.1.6 |  |
| SUB\_SPORT\_MOTOCROSS | 36 | API Level 4.1.6 |  |
| SUB\_SPORT\_BACKCOUNTRY | 37 | API Level 4.1.6 |  |
| SUB\_SPORT\_RESORT | 38 | API Level 4.1.6 |  |
| SUB\_SPORT\_RC\_DRONE | 39 | API Level 4.1.6 |  |
| SUB\_SPORT\_WINGSUIT | 40 | API Level 4.1.6 |  |
| SUB\_SPORT\_WHITEWATER | 41 | API Level 4.1.6 |  |
| SUB\_SPORT\_SKATE\_SKIING | 42 | API Level 4.1.6 |  |
| SUB\_SPORT\_YOGA | 43 | API Level 4.1.6 |  |
| SUB\_SPORT\_PILATES | 44 | API Level 4.1.6 |  |
| SUB\_SPORT\_INDOOR\_RUNNING | 45 | API Level 4.1.6 |  |
| SUB\_SPORT\_GRAVEL\_CYCLING | 46 | API Level 4.1.6 |  |
| SUB\_SPORT\_E\_BIKE\_MOUNTAIN | 47 | API Level 4.1.6 |  |
| SUB\_SPORT\_COMMUTING | 48 | API Level 4.1.6 |  |
| SUB\_SPORT\_MIXED\_SURFACE | 49 | API Level 4.1.6 |  |
| SUB\_SPORT\_NAVIGATE | 50 | API Level 4.1.6 |  |
| SUB\_SPORT\_TRACK\_ME | 51 | API Level 4.1.6 |  |
| SUB\_SPORT\_MAP | 52 | API Level 4.1.6 |  |
| SUB\_SPORT\_SINGLE\_GAS\_DIVING | 53 | API Level 4.1.6 |  |
| SUB\_SPORT\_MULTI\_GAS\_DIVING | 54 | API Level 4.1.6 |  |
| SUB\_SPORT\_GAUGE\_DIVING | 55 | API Level 4.1.6 |  |
| SUB\_SPORT\_APNEA\_DIVING | 56 | API Level 4.1.6 |  |
| SUB\_SPORT\_APNEA\_HUNTING | 57 | API Level 4.1.6 |  |
| SUB\_SPORT\_VIRTUAL\_ACTIVITY | 58 | API Level 4.1.6 |  |
| SUB\_SPORT\_OBSTACLE | 59 | API Level 4.1.6 |  |
| SUB\_SPORT\_ASSISTANCE | 60 | API Level 4.1.6 |  |
| SUB\_SPORT\_INCIDENT\_DETECTED | 61 | API Level 4.1.6 |  |
| SUB\_SPORT\_BREATHING | 62 | API Level 4.1.6 |  |
| SUB\_SPORT\_CCR\_DIVING | 63 | API Level 4.1.6 |  |
| SUB\_SPORT\_AREA\_CALC | 64 | API Level 4.1.6 |  |
| SUB\_SPORT\_SAIL\_RACE | 65 | API Level 4.1.6 |  |
| SUB\_SPORT\_EXPEDITION | 66 | API Level 4.1.6 |  |
| SUB\_SPORT\_ULTRA | 67 | API Level 4.1.6 |  |
| SUB\_SPORT\_INDOOR\_CLIMBING | 68 | API Level 4.1.6 |  |
| SUB\_SPORT\_BOULDERING | 69 | API Level 4.1.6 |  |
| SUB\_SPORT\_HIIT | 70 | API Level 4.1.6 |  |
| SUB\_SPORT\_INDOOR\_GRINDING | 71 | API Level 4.1.6 |  |
| SUB\_SPORT\_HUNTING\_WITH\_DOGS | 72 | API Level 4.1.6 |  |
| SUB\_SPORT\_AMRAP | 73 | API Level 4.1.6 |  |
| SUB\_SPORT\_EMOM | 74 | API Level 4.1.6 |  |
| SUB\_SPORT\_TABATA | 75 | API Level 4.1.6 |  |
| SUB\_SPORT\_FALL\_DETECTED | 76 | API Level 4.1.6 |  |
| SUB\_SPORT\_ESPORT | 77 | API Level 4.1.6 |  |
| SUB\_SPORT\_TRIATHLON | 78 | API Level 4.1.6 |  |
| SUB\_SPORT\_DUATHLON | 79 | API Level 4.1.6 |  |
| SUB\_SPORT\_BRICK | 80 | API Level 4.1.6 |  |
| SUB\_SPORT\_SWIM\_RUN | 81 | API Level 4.1.6 |  |
| SUB\_SPORT\_ADVENTURE\_RACE | 82 | API Level 4.1.6 |  |
| SUB\_SPORT\_TRUCKER\_WORKOUT | 83 | API Level 4.1.6 |  |
| SUB\_SPORT\_PICKLEBALL | 84 | API Level 4.1.6 |  |
| SUB\_SPORT\_PADEL | 85 | API Level 4.1.6 |  |
| SUB\_SPORT\_INDOOR\_WHEELCHAIR\_WALK | 86 | API Level 4.1.6 |  |
| SUB\_SPORT\_INDOOR\_WHEELCHAIR\_RUN | 87 | API Level 4.1.6 |  |
| SUB\_SPORT\_INDOOR\_HAND\_CYCLING | 88 | API Level 4.1.6 |  |
| SUB\_SPORT\_ANCHOR | 89 | API Level 4.1.6 |  |
| SUB\_SPORT\_FIELD | 90 | API Level 4.1.6 |  |
| SUB\_SPORT\_ICE | 91 | API Level 4.1.6 |  |
| SUB\_SPORT\_ULTIMATE | 92 | API Level 4.1.6 |  |
| SUB\_SPORT\_PLATFORM | 93 | API Level 4.1.6 |  |
| SUB\_SPORT\_SQUASH | 94 | API Level 4.1.6 |  |
| SUB\_SPORT\_BADMINTON | 95 | API Level 4.1.6 |  |
| SUB\_SPORT\_RACQUETBALL | 96 | API Level 4.1.6 |  |
| SUB\_SPORT\_TABLE\_TENNIS | 97 | API Level 4.1.6 |  |
| SUB\_SPORT\_INVALID | 255 | API Level 3.2.0 |  |

### WorkoutIntensity

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| WORKOUT\_INTENSITY\_ACTIVE | 0 | API Level 3.2.0 |  |
| WORKOUT\_INTENSITY\_REST | 1 | API Level 3.2.0 |  |
| WORKOUT\_INTENSITY\_WARMUP | 2 | API Level 3.2.0 |  |
| WORKOUT\_INTENSITY\_COOLDOWN | 3 | API Level 3.2.0 |  |
| WORKOUT\_INTENSITY\_RECOVERY | 4 | API Level 3.2.0 |  |
| WORKOUT\_INTENSITY\_INTERVAL | 5 | API Level 3.2.0 |  |
| WORKOUT\_INTENSITY\_INVALID | 255 | API Level 3.2.0 |  |

### WorkoutStepDurationType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| WORKOUT\_STEP\_DURATION\_TIME | 0 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_DISTANCE | 1 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_HR\_LESS\_THAN | 2 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_HR\_GREATER\_THAN | 3 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_CALORIES | 4 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_OPEN | 5 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_STEPS\_COMPLETE | 6 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_TIME | 7 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_DISTANCE | 8 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_CALORIES | 9 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_HR\_LESS\_THAN | 10 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_HR\_GREATER\_THAN | 11 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_POWER\_LESS\_THAN | 12 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_POWER\_GREATER\_THAN | 13 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_LESS\_THAN | 14 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_GREATER\_THAN | 15 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_TRAINING\_PEAKS\_TRAINING\_STRESS\_SCORE | 16 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_POWER\_LAST\_LAP\_LESS\_THAN | 17 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_MAX\_POWER\_LAST\_LAP\_LESS\_THAN | 18 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_3S\_LESS\_THAN | 19 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_10S\_LESS\_THAN | 20 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_30S\_LESS\_THAN | 21 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_3S\_GREATER\_THAN | 22 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_10S\_GREATER\_THAN | 23 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_30S\_GREATER\_THAN | 24 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_LAP\_LESS\_THAN | 25 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_POWER\_LAP\_GREATER\_THAN | 26 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPEAT\_UNTIL\_TRAINING\_PEAKS\_TRAINING\_STRESS\_SCORE | 27 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPETITION\_TIME | 28 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_REPS | 29 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_DURATION\_INVALID | 255 | API Level 3.2.0 |  |

### WorkoutStepTargetType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| WORKOUT\_STEP\_TARGET\_SPEED | 0 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_HEART\_RATE | 1 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_OPEN | 2 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_CADENCE | 3 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_POWER | 4 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_GRADE | 5 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_RESISTANCE | 6 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_POWER\_3S | 7 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_POWER\_10S | 8 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_POWER\_30S | 9 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_POWER\_LAP | 10 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_SWIM\_STROKE | 11 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_SPEED\_LAP | 12 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_HEART\_RATE\_LAP | 13 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_INHALE\_DURATION | 14 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_INHALE\_HOLD\_DURATION | 15 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_EXHALE\_DURATION | 16 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_EXHALE\_HOLD\_DURATION | 17 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_POWER\_CURVE | 18 | API Level 3.2.0 |  |
| WORKOUT\_STEP\_TARGET\_INVALID | 255 | API Level 3.2.0 |  |

## Instance Method Summary

- [**getActivityInfo**](#getActivityInfo-instance_function "getActivityInfo (Instance Function)") () as [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html) or **Null**
	Get the current Activity Info.
- [**getCurrentWorkoutStep**](#getCurrentWorkoutStep-instance_function "getCurrentWorkoutStep (Instance Function)") () as [Activity.WorkoutStepInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/WorkoutStepInfo.html) or **Null**
	Get information about the current workout step.
- [**getNextWorkoutStep**](#getNextWorkoutStep-instance_function "getNextWorkoutStep (Instance Function)") () as [Activity.WorkoutStepInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/WorkoutStepInfo.html) or **Null**
	Get information about the next workout step.
- [**getProfileInfo**](#getProfileInfo-instance_function "getProfileInfo (Instance Function)") () as [Activity.ProfileInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/ProfileInfo.html)
	Get information about the current profile.
