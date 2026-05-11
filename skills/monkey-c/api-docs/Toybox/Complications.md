---
title: Toybox.Complications
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html
---

## Module: Toybox.Complications

## Overview

## Classes Under Namespace

**Classes:** [Complication](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Complication.html), [ComplicationNotFoundException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/ComplicationNotFoundException.html), [Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html), [Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Iterator.html)

## Constant Summary

### Unit

Units reported by a complication

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| UNIT\_INVALID | 0 | API Level 4.2.0 |  |
| UNIT\_DISTANCE | 1 | API Level 4.2.0 | Complication is a distance; value is in meters |
| UNIT\_ELEVATION | 2 | API Level 4.2.0 | Complication is a elevation; value is in meters |
| UNIT\_HEIGHT | 3 | API Level 4.2.0 | Complication is a height; value is in meters |
| UNIT\_SPEED | 4 | API Level 4.2.0 | Complication is a speed; value is in meters/second |
| UNIT\_TEMPERATURE | 5 | API Level 4.2.0 | Complication is a temperature; value is in degrees Celsius |
| UNIT\_WEIGHT | 6 | API Level 4.2.0 | Complication is a weight; value is in grams |

### Type

System build-in complication type

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| COMPLICATION\_TYPE\_INVALID | 0 | API Level 4.2.0 | Invalid build-in complication type |
| COMPLICATION\_TYPE\_BATTERY | 1 | API Level 4.2.0 | Value is a non-negative Number percent 0 to 100 representing battery charge or `null` |
| COMPLICATION\_TYPE\_STEPS | 2 | API Level 4.2.0 | Value is a non-negative Number of steps for the current day, not available in wheelchair mode |
| COMPLICATION\_TYPE\_CALORIES | 3 | API Level 4.2.0 | Value is a non-negative Number of calories burned for the current day |
| COMPLICATION\_TYPE\_FLOORS\_CLIMBED | 4 | API Level 4.2.0 | Value is a non-negative Number of floors climbed, not available in wheelchair mode |
| COMPLICATION\_TYPE\_INTENSITY\_MINUTES | 5 | API Level 4.2.0 | Value is a non-negative Number of intensity minutes that resets weekly |
| COMPLICATION\_TYPE\_DATE | 6 | API Level 4.2.0 | Value is a String with the day of the month and the month e.g., 28 Mar |
| COMPLICATION\_TYPE\_WEEKDAY\_MONTHDAY | 7 | API Level 4.2.0 | Value is a String with the day of the week and the day of the month e.g., Mon 28 |
| COMPLICATION\_TYPE\_CURRENT\_WEATHER | 8 | API Level 4.2.0 | Value is a [Weather.CONDITION\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Weather.html#CONDITION_CLEAR-const) for the current weather |
| COMPLICATION\_TYPE\_FORECAST\_WEATHER\_1DAY | 9 | API Level 4.2.0 | Value is a [Weather.CONDITION\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Weather.html#CONDITION_CLEAR-const) for the forecast weather one day in the future |
| COMPLICATION\_TYPE\_FORECAST\_WEATHER\_2DAY | 10 | API Level 4.2.0 | Value is a [Weather.CONDITION\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Weather.html#CONDITION_CLEAR-const) for the forecast weather two days in the future |
| COMPLICATION\_TYPE\_FORECAST\_WEATHER\_3DAY | 11 | API Level 4.2.0 | Value is a [Weather.CONDITION\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Weather.html#CONDITION_CLEAR-const) for the forecast weather three days in the future |
| COMPLICATION\_TYPE\_CALENDAR\_EVENTS | 12 | API Level 4.2.0 | Value is a String with the time of your next calendar event or `null` |
| COMPLICATION\_TYPE\_SUNRISE | 13 | API Level 4.2.0 | Value is a non-negative Number representing seconds since midnight local time of the sunrise or `null` |
| COMPLICATION\_TYPE\_SUNSET | 14 | API Level 4.2.0 | Value is a non-negative Number representing seconds since midnight local time of the sunset or `null` |
| COMPLICATION\_TYPE\_ALTITUDE | 15 | API Level 4.2.0 | Value is a Float of the current altitude in meters or `null`. Prior to ConnectIQ API version 5.1.0, the value was a Number. |
| COMPLICATION\_TYPE\_SEA\_LEVEL\_PRESSURE | 16 | API Level 4.2.0 | Value is a Float in pascals of the current pressure or `null` |
| COMPLICATION\_TYPE\_NOTIFICATION\_COUNT | 17 | API Level 4.2.0 | Value is a non-negative Number of notifications or `null` |
| COMPLICATION\_TYPE\_HEART\_RATE | 18 | API Level 4.2.0 | Value is a non-negative Number in beats per minute or `null` |
| COMPLICATION\_TYPE\_WEEKLY\_RUN\_DISTANCE | 19 | API Level 4.2.0 | Value is a Float of your weekly run distance in meters |
| COMPLICATION\_TYPE\_WEEKLY\_BIKE\_DISTANCE | 20 | API Level 4.2.0 | Value is a Float of your weekly bike distance in meters |
| COMPLICATION\_TYPE\_RECOVERY\_TIME | 21 | API Level 4.2.0 | Value is a Number of minutes remaining in your recovery time |
| COMPLICATION\_TYPE\_STRESS | 22 | API Level 4.2.0 | Value is a Number representing your current stress level or `null` |
| COMPLICATION\_TYPE\_BODY\_BATTERY | 23 | API Level 4.2.0 | Value is a Number representing your current body battery or `null` |
| COMPLICATION\_TYPE\_VO2MAX\_RUN | 24 | API Level 4.2.0 | Value is a Number representing your running VO2 max or `null` |
| COMPLICATION\_TYPE\_VO2MAX\_BIKE | 25 | API Level 4.2.0 | Value is a Number representing your cycling VO2 max or `null` |
| COMPLICATION\_TYPE\_TRAINING\_STATUS | 26 | API Level 4.2.0 | Value is a String representing your training status |
| COMPLICATION\_TYPE\_RACE\_PREDICTOR\_5K | 27 | API Level 4.2.0 | Value is a Number representing your predicted 5K time in seconds |
| COMPLICATION\_TYPE\_RACE\_PREDICTOR\_10K | 28 | API Level 4.2.0 | Value is a Number representing your predicted 10k time in seconds |
| COMPLICATION\_TYPE\_RACE\_PREDICTOR\_HALF\_MARATHON | 29 | API Level 4.2.0 | Value is a Number representing your predicted half marathon time in seconds |
| COMPLICATION\_TYPE\_RACE\_PREDICTOR\_MARATHON | 30 | API Level 4.2.0 | Value is a Number representing your predicted your marathon time in seconds |
| COMPLICATION\_TYPE\_RACE\_PACE\_PREDICTOR\_5K | 31 | API Level 4.2.0 | Value is a Float representing your 5k pace in meters/second |
| COMPLICATION\_TYPE\_RACE\_PACE\_PREDICTOR\_10K | 32 | API Level 4.2.0 | Value is a Float representing your 10k pace in meters/second |
| COMPLICATION\_TYPE\_RACE\_PACE\_PREDICTOR\_HALF\_MARATHON | 33 | API Level 4.2.0 | Value is a Float representing your half marathon pace in meters/second |
| COMPLICATION\_TYPE\_RACE\_PACE\_PREDICTOR\_MARATHON | 34 | API Level 4.2.0 | Value is a Float representing your marathon pace in meters/second |
| COMPLICATION\_TYPE\_PULSE\_OX | 35 | API Level 4.2.0 | Value is a non-negative Number as a percent from 0 to 100 representing your blood oxygen or `null` |
| COMPLICATION\_TYPE\_RESPIRATION\_RATE | 36 | API Level 4.2.0 | Value is a non-negative Number representing your breaths per minute or `null` |
| COMPLICATION\_TYPE\_SOLAR\_INPUT | 37 | API Level 4.2.0 | Value is a non-negative Number representing percent between 0 to 100 of solar charge or `null` |
| COMPLICATION\_TYPE\_CURRENT\_TEMPERATURE | 38 | API Level 4.2.0 | Value is a Float representing temperature in degrees Celsius or `null`. Prior to ConnectIQ API version 5.0.0, the value was a Number. |
| COMPLICATION\_TYPE\_HIGH\_LOW\_TEMPERATURE | 39 | API Level 4.2.0 | Value is a String providing the high and low temperature values in a format similar to "H <high> / L <low>" |
| COMPLICATION\_TYPE\_WHEELCHAIR\_PUSHES | 40 | API Level 4.2.3 | Value is a non-negative Number of pushes for the current day, only available in wheelchair mode |
| COMPLICATION\_TYPE\_LAST\_GOLF\_ROUND\_SCORE | 41 | API Level 5.0.0 | Value is a String in the format "<LastRoundTotalScore>(<Offset>)" where Offset is "E" for even-par, a negative value for under par, or a positive value for over par |

## Typedef Summary

- [**ComplicationChangedCallback**](#ComplicationChangedCallback-named_type "ComplicationChangedCallback (Named Type)") as [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html) (id as [Complications.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html)) as **Void**
	Callback for subscribers to be notified of complication updates.
- [**Data**](#Data-named_type "Data (Named Type)") as {:shortLabel as [Complications.Label](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#Label-named_type),:value as [Complications.Value](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#Value-named_type),:unit as [Complications.Unit](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#Unit-module) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html),:ranges as [Complications.Ranges](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#Ranges-named_type) }
- [**Icon**](#Icon-named_type "Icon (Named Type)") as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html)
- [**Label**](#Label-named_type "Label (Named Type)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
- [**RangeValue**](#RangeValue-named_type "RangeValue (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html)
- [**Ranges**](#Ranges-named_type "Ranges (Named Type)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Complications.RangeValue](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#RangeValue-named_type) >
- [**Value**](#Value-named_type "Value (Named Type)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Complications.RangeValue](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#RangeValue-named_type)

## Instance Method Summary

- [**exitTo**](#exitTo-instance_function "exitTo (Instance Function)") (id as [Complications.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html)) as **Void**
	Launches the app associated with the complication.
- [**getComplication**](#getComplication-instance_function "getComplication (Instance Function)") (id as [Complications.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html)) as [Complications.Complication](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Complication.html)
	Given a complication Id, get the complication.
- [**getComplications**](#getComplications-instance_function "getComplications (Instance Function)") () as [Complications.Iterator](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Iterator.html)
	Provide an iterator over complication id that we have access to.
- [**registerComplicationChangeCallback**](#registerComplicationChangeCallback-instance_function "registerComplicationChangeCallback (Instance Function)") (callback as [Complications.ComplicationChangedCallback](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#ComplicationChangedCallback-named_type) or **Null**) as **Void**
- [**subscribeToUpdates**](#subscribeToUpdates-instance_function "subscribeToUpdates (Instance Function)") (id as [Complications.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Subscribes to complication.
- [**unsubscribeFromAllUpdates**](#unsubscribeFromAllUpdates-instance_function "unsubscribeFromAllUpdates (Instance Function)") () as **Void**
	Unsubscribes from all subscribed complications.
- [**unsubscribeFromUpdates**](#unsubscribeFromUpdates-instance_function "unsubscribeFromUpdates (Instance Function)") (id as [Complications.Id](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Id.html)) as **Void**
	Unsubscribes from complication.
- [**updateComplication**](#updateComplication-instance_function "updateComplication (Instance Function)") (index as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), data as [Complications.Data](https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html#Data-named_type)) as **Void**
	Update the complication data Values not specified in \`data\` will not be updated from the last update or what is specified in the resource definition.
