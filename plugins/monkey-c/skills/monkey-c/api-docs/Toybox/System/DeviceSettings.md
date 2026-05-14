---
title: Toybox.System.DeviceSettings
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System/DeviceSettings.html
---

## Class: Toybox.System.DeviceSettings

## Overview

## See Also:

- [getDeviceSettings()](../System.md#getDeviceSettings-instance_function)
- [Lang.format()](../Lang.md#format-instance_function)

## Instance Member Summary

- [**activityTrackingOn**](#activityTrackingOn-var "activityTrackingOn (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The activity tracking setting mode.
- [**alarmCount**](#alarmCount-var "alarmCount (Var)") as [Lang.Number](../Lang/Number.md)
	The number of alarms set on the device.
- [**connectionAvailable**](#connectionAvailable-var "connectionAvailable (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	Indicates if any communication channel is connected and available for use.
- [**connectionInfo**](#connectionInfo-var "connectionInfo (Var)") as [Lang.Dictionary](../Lang/Dictionary.md) < [Lang.Symbol](../Lang/Symbol.md), [System.ConnectionInfo](ConnectionInfo.md) >
	The state of connections available to the device.
- [**distanceUnits**](#distanceUnits-var "distanceUnits (Var)") as [System.UnitsSystem](../System.md#UnitsSystem-module)
	The distance unit setting mode.
- [**doNotDisturb**](#doNotDisturb-var "doNotDisturb (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The Do Not Disturb setting mode.
- [**elevationUnits**](#elevationUnits-var "elevationUnits (Var)") as [System.UnitsSystem](../System.md#UnitsSystem-module)
	The elevation unit setting mode.
- [**firmwareVersion**](#firmwareVersion-var "firmwareVersion (Var)") as \[ [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md) \]
	The current firmware version of the device.
- [**firstDayOfWeek**](#firstDayOfWeek-var "firstDayOfWeek (Var)") as [Gregorian.DayOfWeek](../Time/Gregorian.md#DayOfWeek-module)
	The first day of the week.
- [**fontScale**](#fontScale-var "fontScale (Var)") as [Lang.Float](../Lang/Float.md)
	Scale factor to be used for displayed text.
- [**heightUnits**](#heightUnits-var "heightUnits (Var)") as [System.UnitsSystem](../System.md#UnitsSystem-module)
	The height unit setting mode.
- [**inputButtons**](#inputButtons-var "inputButtons (Var)") as [System.ButtonInputs](../System.md#ButtonInputs-module)
	The physical buttons supported by the device.
- [**is24Hour**](#is24Hour-var "is24Hour (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The clock mode mode.
- [**isEnhancedReadabilityModeEnabled**](#isEnhancedReadabilityModeEnabled-var "isEnhancedReadabilityModeEnabled (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	Indicates the device is currently using Enhanced Readability Mode.
- [**isGlanceModeEnabled**](#isGlanceModeEnabled-var "isGlanceModeEnabled (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	Indicates if widget glances are enabled on the device.
- [**isNightModeEnabled**](#isNightModeEnabled-var "isNightModeEnabled (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	Indicates the device is currently using night mode colors.
- [**isTouchScreen**](#isTouchScreen-var "isTouchScreen (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The availability of a touch screen on the device.
- [**monkeyVersion**](#monkeyVersion-var "monkeyVersion (Var)") as \[ [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md), [Lang.Number](../Lang/Number.md) \]
	The Connect IQ version supported by the device.
- [**notificationCount**](#notificationCount-var "notificationCount (Var)") as [Lang.Number](../Lang/Number.md)
	The number of active notifications.
- [**paceUnits**](#paceUnits-var "paceUnits (Var)") as [System.UnitsSystem](../System.md#UnitsSystem-module)
	The pace unit setting mode.
- [**partNumber**](#partNumber-var "partNumber (Var)") as [Lang.String](../Lang/String.md)
	The part number of the device.
- [**phoneConnected**](#phoneConnected-var "phoneConnected (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The phone connection status mode.
- [**phoneOperatingSystem**](#phoneOperatingSystem-var "phoneOperatingSystem (Var)") as [System.PhoneOperatingSystem](../System.md#PhoneOperatingSystem-module) or **Null**
	Operating System of the BLE-connected mobile device.
- [**requiresBurnInProtection**](#requiresBurnInProtection-var "requiresBurnInProtection (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	This flag indicates whether the device screen requires burn-in protection.
- [**screenHeight**](#screenHeight-var "screenHeight (Var)") as [Lang.Number](../Lang/Number.md)
	The height of the device screen in pixels.
- [**screenShape**](#screenShape-var "screenShape (Var)") as [System.ScreenShape](../System.md#ScreenShape-module)
	The screen shape of the device.
- [**screenWidth**](#screenWidth-var "screenWidth (Var)") as [Lang.Number](../Lang/Number.md)
	The width of the device screen in pixels.
- [**systemLanguage**](#systemLanguage-var "systemLanguage (Var)") as [System.Language](../System.md#Language-module)
	The language being used by the system.
- [**temperatureUnits**](#temperatureUnits-var "temperatureUnits (Var)") as [System.UnitsSystem](../System.md#UnitsSystem-module)
	The temperature unit setting mode.
- [**tonesOn**](#tonesOn-var "tonesOn (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The tone setting mode.
- [**uniqueIdentifier**](#uniqueIdentifier-var "uniqueIdentifier (Var)") as [Lang.String](../Lang/String.md) or **Null**
	A unique alphanumeric device identifier.
- [**vibrateOn**](#vibrateOn-var "vibrateOn (Var)") as [Lang.Boolean](../Lang/Boolean.md)
	The vibration setting mode.
- [**weightUnits**](#weightUnits-var "weightUnits (Var)") as [System.UnitsSystem](../System.md#UnitsSystem-module)
	The weight unit setting mode.
