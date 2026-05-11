---
title: Toybox.System.DeviceSettings
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System/DeviceSettings.html
---

## Class: Toybox.System.DeviceSettings

## Overview

## See Also:

- [getDeviceSettings()](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#getDeviceSettings-instance_function)
- [Lang.format()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#format-instance_function)

## Instance Member Summary

- [**activityTrackingOn**](#activityTrackingOn-var "activityTrackingOn (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The activity tracking setting mode.
- [**alarmCount**](#alarmCount-var "alarmCount (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The number of alarms set on the device.
- [**connectionAvailable**](#connectionAvailable-var "connectionAvailable (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Indicates if any communication channel is connected and available for use.
- [**connectionInfo**](#connectionInfo-var "connectionInfo (Var)") as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html), [System.ConnectionInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/ConnectionInfo.html) >
	The state of connections available to the device.
- [**distanceUnits**](#distanceUnits-var "distanceUnits (Var)") as [System.UnitsSystem](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#UnitsSystem-module)
	The distance unit setting mode.
- [**doNotDisturb**](#doNotDisturb-var "doNotDisturb (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The Do Not Disturb setting mode.
- [**elevationUnits**](#elevationUnits-var "elevationUnits (Var)") as [System.UnitsSystem](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#UnitsSystem-module)
	The elevation unit setting mode.
- [**firmwareVersion**](#firmwareVersion-var "firmwareVersion (Var)") as \[ [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) \]
	The current firmware version of the device.
- [**firstDayOfWeek**](#firstDayOfWeek-var "firstDayOfWeek (Var)") as [Gregorian.DayOfWeek](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian.html#DayOfWeek-module)
	The first day of the week.
- [**fontScale**](#fontScale-var "fontScale (Var)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)
	Scale factor to be used for displayed text.
- [**heightUnits**](#heightUnits-var "heightUnits (Var)") as [System.UnitsSystem](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#UnitsSystem-module)
	The height unit setting mode.
- [**inputButtons**](#inputButtons-var "inputButtons (Var)") as [System.ButtonInputs](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#ButtonInputs-module)
	The physical buttons supported by the device.
- [**is24Hour**](#is24Hour-var "is24Hour (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The clock mode mode.
- [**isEnhancedReadabilityModeEnabled**](#isEnhancedReadabilityModeEnabled-var "isEnhancedReadabilityModeEnabled (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Indicates the device is currently using Enhanced Readability Mode.
- [**isGlanceModeEnabled**](#isGlanceModeEnabled-var "isGlanceModeEnabled (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Indicates if widget glances are enabled on the device.
- [**isNightModeEnabled**](#isNightModeEnabled-var "isNightModeEnabled (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Indicates the device is currently using night mode colors.
- [**isTouchScreen**](#isTouchScreen-var "isTouchScreen (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The availability of a touch screen on the device.
- [**monkeyVersion**](#monkeyVersion-var "monkeyVersion (Var)") as \[ [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) \]
	The Connect IQ version supported by the device.
- [**notificationCount**](#notificationCount-var "notificationCount (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The number of active notifications.
- [**paceUnits**](#paceUnits-var "paceUnits (Var)") as [System.UnitsSystem](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#UnitsSystem-module)
	The pace unit setting mode.
- [**partNumber**](#partNumber-var "partNumber (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	The part number of the device.
- [**phoneConnected**](#phoneConnected-var "phoneConnected (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The phone connection status mode.
- [**phoneOperatingSystem**](#phoneOperatingSystem-var "phoneOperatingSystem (Var)") as [System.PhoneOperatingSystem](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#PhoneOperatingSystem-module) or **Null**
	Operating System of the BLE-connected mobile device.
- [**requiresBurnInProtection**](#requiresBurnInProtection-var "requiresBurnInProtection (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	This flag indicates whether the device screen requires burn-in protection.
- [**screenHeight**](#screenHeight-var "screenHeight (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The height of the device screen in pixels.
- [**screenShape**](#screenShape-var "screenShape (Var)") as [System.ScreenShape](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#ScreenShape-module)
	The screen shape of the device.
- [**screenWidth**](#screenWidth-var "screenWidth (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The width of the device screen in pixels.
- [**systemLanguage**](#systemLanguage-var "systemLanguage (Var)") as [System.Language](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#Language-module)
	The language being used by the system.
- [**temperatureUnits**](#temperatureUnits-var "temperatureUnits (Var)") as [System.UnitsSystem](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#UnitsSystem-module)
	The temperature unit setting mode.
- [**tonesOn**](#tonesOn-var "tonesOn (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The tone setting mode.
- [**uniqueIdentifier**](#uniqueIdentifier-var "uniqueIdentifier (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	A unique alphanumeric device identifier.
- [**vibrateOn**](#vibrateOn-var "vibrateOn (Var)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The vibration setting mode.
- [**weightUnits**](#weightUnits-var "weightUnits (Var)") as [System.UnitsSystem](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#UnitsSystem-module)
	The weight unit setting mode.
