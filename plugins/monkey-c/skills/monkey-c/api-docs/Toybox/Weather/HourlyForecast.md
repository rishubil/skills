---
title: Toybox.Weather.HourlyForecast
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Weather/HourlyForecast.html
---

## Class: Toybox.Weather.HourlyForecast

## Overview

Represents the forecast for a given hour

## Instance Member Summary

- [**cloudCover**](#cloudCover-var "cloudCover (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The cloud cover \[0-100%\].
- [**condition**](#condition-var "condition (Var)") as [Weather.Condition](../Weather.md#Condition-module) or **Null**
	The weather condition.
- [**dewPoint**](#dewPoint-var "dewPoint (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The dew point in Celsius.
- [**forecastTime**](#forecastTime-var "forecastTime (Var)") as [Time.Moment](../Time/Moment.md) or **Null**
	The time the forecast is valid in UTC time.
- [**precipitationChance**](#precipitationChance-var "precipitationChance (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The chance of precipitation \[0-100%\].
- [**relativeHumidity**](#relativeHumidity-var "relativeHumidity (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The relative humidity \[0-100%\].
- [**temperature**](#temperature-var "temperature (Var)") as [Lang.Numeric](../Lang.md#Numeric-named_type) or **Null**
	The current temperature in Celsius.
- [**uvIndex**](#uvIndex-var "uvIndex (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The UV index \[0-10\].
- [**windBearing**](#windBearing-var "windBearing (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The wind bearing in degrees.
- [**windSpeed**](#windSpeed-var "windSpeed (Var)") as [Lang.Float](../Lang/Float.md) or **Null**
	The current wind speed in meters per second.

## Instance Attribute Details

### var cloudCover as Lang.Number or Null

The cloud cover \[0-100%\]

### var condition as Weather.Condition or Null

The weather condition

### var dewPoint as Lang.Float or Null

The dew point in Celsius

### var forecastTime as Time.Moment or Null

The time the forecast is valid in UTC time

### var precipitationChance as Lang.Number or Null

The chance of precipitation \[0-100%\]

### var relativeHumidity as Lang.Number or Null

The relative humidity \[0-100%\]

### var temperature as Lang.Numeric or Null

The current temperature in Celsius

### var uvIndex as Lang.Float or Null

The UV index \[0-10\]

### var windBearing as Lang.Number or Null

The wind bearing in degrees. North = 0, East = 90, South = 180, West = 270

### var windSpeed as Lang.Float or Null

The current wind speed in meters per second
