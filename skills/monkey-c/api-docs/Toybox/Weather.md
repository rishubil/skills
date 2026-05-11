---
title: Toybox.Weather
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Weather.html
---

## Module: Toybox.Weather

## Overview

## Classes Under Namespace

**Classes:** [CurrentConditions](Weather/CurrentConditions.md), [DailyForecast](Weather/DailyForecast.md), [HourlyForecast](Weather/HourlyForecast.md)

## Constant Summary

### Condition

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONDITION\_CLEAR | 0 | API Level 3.2.0 | Clear |
| CONDITION\_PARTLY\_CLOUDY | 1 | API Level 3.2.0 | Partly cloudy |
| CONDITION\_MOSTLY\_CLOUDY | 2 | API Level 3.2.0 | Mostly cloudy |
| CONDITION\_RAIN | 3 | API Level 3.2.0 | Rain |
| CONDITION\_SNOW | 4 | API Level 3.2.0 | Snow |
| CONDITION\_WINDY | 5 | API Level 3.2.0 | Windy |
| CONDITION\_THUNDERSTORMS | 6 | API Level 3.2.0 | Thunderstorms |
| CONDITION\_WINTRY\_MIX | 7 | API Level 3.2.0 | Wintry mix |
| CONDITION\_FOG | 8 | API Level 3.2.0 | Fog |
| CONDITION\_HAZY | 9 | API Level 3.2.0 | Hazy |
| CONDITION\_HAIL | 10 | API Level 3.2.0 | Hail |
| CONDITION\_SCATTERED\_SHOWERS | 11 | API Level 3.2.0 | Scattered showers |
| CONDITION\_SCATTERED\_THUNDERSTORMS | 12 | API Level 3.2.0 | Scattered thunderstorms |
| CONDITION\_UNKNOWN\_PRECIPITATION | 13 | API Level 3.2.0 | Unknown precipitation |
| CONDITION\_LIGHT\_RAIN | 14 | API Level 3.2.0 | Light rain |
| CONDITION\_HEAVY\_RAIN | 15 | API Level 3.2.0 | Heavy rain |
| CONDITION\_LIGHT\_SNOW | 16 | API Level 3.2.0 | Light snow |
| CONDITION\_HEAVY\_SNOW | 17 | API Level 3.2.0 | Heavy snow |
| CONDITION\_LIGHT\_RAIN\_SNOW | 18 | API Level 3.2.0 | Light rain snow |
| CONDITION\_HEAVY\_RAIN\_SNOW | 19 | API Level 3.2.0 | Heavy rain snow |
| CONDITION\_CLOUDY | 20 | API Level 3.2.0 | Cloudy |
| CONDITION\_RAIN\_SNOW | 21 | API Level 3.2.0 | Rain snow |
| CONDITION\_PARTLY\_CLEAR | 22 | API Level 3.2.0 | Partly clear |
| CONDITION\_MOSTLY\_CLEAR | 23 | API Level 3.2.0 | Mostly clear |
| CONDITION\_LIGHT\_SHOWERS | 24 | API Level 3.2.0 | Light showers |
| CONDITION\_SHOWERS | 25 | API Level 3.2.0 | Showers |
| CONDITION\_HEAVY\_SHOWERS | 26 | API Level 3.2.0 | Heavy showers |
| CONDITION\_CHANCE\_OF\_SHOWERS | 27 | API Level 3.2.0 | Chance of showers |
| CONDITION\_CHANCE\_OF\_THUNDERSTORMS | 28 | API Level 3.2.0 | Chance of thunderstorms |
| CONDITION\_MIST | 29 | API Level 3.2.0 | Mist |
| CONDITION\_DUST | 30 | API Level 3.2.0 | Dust |
| CONDITION\_DRIZZLE | 31 | API Level 3.2.0 | Drizzle |
| CONDITION\_TORNADO | 32 | API Level 3.2.0 | Tornado |
| CONDITION\_SMOKE | 33 | API Level 3.2.0 | Smoke |
| CONDITION\_ICE | 34 | API Level 3.2.0 | Ice |
| CONDITION\_SAND | 35 | API Level 3.2.0 | Sand |
| CONDITION\_SQUALL | 36 | API Level 3.2.0 | Squall |
| CONDITION\_SANDSTORM | 37 | API Level 3.2.0 | Sandstorm |
| CONDITION\_VOLCANIC\_ASH | 38 | API Level 3.2.0 | Volcanic ash |
| CONDITION\_HAZE | 39 | API Level 3.2.0 | Haze |
| CONDITION\_FAIR | 40 | API Level 3.2.0 | Fair |
| CONDITION\_HURRICANE | 41 | API Level 3.2.0 | Hurricane |
| CONDITION\_TROPICAL\_STORM | 42 | API Level 3.2.0 | Tropical storm |
| CONDITION\_CHANCE\_OF\_SNOW | 43 | API Level 3.2.0 | Chance of snow |
| CONDITION\_CHANCE\_OF\_RAIN\_SNOW | 44 | API Level 3.2.0 | Chance of rain snow |
| CONDITION\_CLOUDY\_CHANCE\_OF\_RAIN | 45 | API Level 3.2.0 | Cloudy chance of rain |
| CONDITION\_CLOUDY\_CHANCE\_OF\_SNOW | 46 | API Level 3.2.0 | Cloudy chance of snow |
| CONDITION\_CLOUDY\_CHANCE\_OF\_RAIN\_SNOW | 47 | API Level 3.2.0 | Cloudy chance of rain snow |
| CONDITION\_FLURRIES | 48 | API Level 3.2.0 | Flurries |
| CONDITION\_FREEZING\_RAIN | 49 | API Level 3.2.0 | Freezing rain |
| CONDITION\_SLEET | 50 | API Level 3.2.0 | Sleet |
| CONDITION\_ICE\_SNOW | 51 | API Level 3.2.0 | Ice snow |
| CONDITION\_THIN\_CLOUDS | 52 | API Level 3.2.0 | Thin clouds |
| CONDITION\_UNKNOWN | 53 | API Level 3.2.0 | Unknown |

## Instance Method Summary

- [**getCurrentConditions**](#getCurrentConditions-instance_function "getCurrentConditions (Instance Function)") () as [Weather.CurrentConditions](Weather/CurrentConditions.md) or **Null**
	Get the most recently cached weather conditions.
- [**getDailyForecast**](#getDailyForecast-instance_function "getDailyForecast (Instance Function)") () as [Lang.Array](Lang/Array.md) < [Weather.DailyForecast](Weather/DailyForecast.md) > or **Null**
	Get the daily forecast.
- [**getHourlyForecast**](#getHourlyForecast-instance_function "getHourlyForecast (Instance Function)") () as [Lang.Array](Lang/Array.md) < [Weather.HourlyForecast](Weather/HourlyForecast.md) > or **Null**
	Get the hourly forecast.
- [**getSunrise**](#getSunrise-instance_function "getSunrise (Instance Function)") (location as [Position.Location](Position/Location.md), date as [Time.Moment](Time/Moment.md)) as [Time.Moment](Time/Moment.md) or **Null**
	Get sunrise time for the provided location and date.
- [**getSunset**](#getSunset-instance_function "getSunset (Instance Function)") (location as [Position.Location](Position/Location.md), date as [Time.Moment](Time/Moment.md)) as [Time.Moment](Time/Moment.md) or **Null**
	Get sunrise time for the provided location and date.
