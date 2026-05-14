---
title: Toybox.Activity.ProfileInfo
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/ProfileInfo.html
---

## Class: Toybox.Activity.ProfileInfo

## Overview

The ProfileInfo class contains information about the active profile.

This information can be retrieved with the [getProfileInfo()](../Activity.md#getProfileInfo-instance_function) method. Fields in this class may return `null` so should be checked for `null` values prior to use.

## Instance Member Summary

- [**name**](#name-var "name (Var)") as [Lang.String](../Lang/String.md)
	The profile name.
- [**sport**](#sport-var "sport (Var)") as [Activity.Sport](../Activity.md#Sport-module)
	A [SPORT\_\*](../Activity.md#SPORT_GENERIC-const) enum value.
- [**subSport**](#subSport-var "subSport (Var)") as [Activity.SubSport](../Activity.md#SubSport-module) or **Null**
	A [SUB\_SPORT\_\*](../Activity.md#SUB_SPORT_GENERIC-const) enum value.
- [**uniqueIdentifier**](#uniqueIdentifier-var "uniqueIdentifier (Var)") as [Lang.Long](../Lang/Long.md)
	An unique identifer of the profile.

## Instance Attribute Details

### var name as Lang.String

The profile name

### var sport as Activity.Sport

A [SPORT\_\*](../Activity.md#SPORT_GENERIC-const) enum value

### var subSport as Activity.SubSport or Null

A [SUB\_SPORT\_\*](../Activity.md#SUB_SPORT_GENERIC-const) enum value. Can be `null`.

### var uniqueIdentifier as Lang.Long

An unique identifer of the profile
