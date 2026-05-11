---
title: Toybox.Activity.ProfileInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/ProfileInfo.html
---

## Class: Toybox.Activity.ProfileInfo

## Overview

The ProfileInfo class contains information about the active profile.

This information can be retrieved with the [getProfileInfo()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#getProfileInfo-instance_function) method. Fields in this class may return `null` so should be checked for `null` values prior to use.

## Instance Member Summary

- [**name**](#name-var "name (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	The profile name.
- [**sport**](#sport-var "sport (Var)") as [Activity.Sport](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#Sport-module)
	A [SPORT\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SPORT_GENERIC-const) enum value.
- [**subSport**](#subSport-var "subSport (Var)") as [Activity.SubSport](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SubSport-module) or **Null**
	A [SUB\_SPORT\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SUB_SPORT_GENERIC-const) enum value.
- [**uniqueIdentifier**](#uniqueIdentifier-var "uniqueIdentifier (Var)") as [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html)
	An unique identifer of the profile.

## Instance Attribute Details

### var name as Lang.String

The profile name

### var sport as Activity.Sport

A [SPORT\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SPORT_GENERIC-const) enum value

### var subSport as Activity.SubSport or Null

A [SUB\_SPORT\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity.html#SUB_SPORT_GENERIC-const) enum value. Can be `null`.

### var uniqueIdentifier as Lang.Long

An unique identifer of the profile
