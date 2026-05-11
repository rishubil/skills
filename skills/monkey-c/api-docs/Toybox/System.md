---
title: Toybox.System
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html
---

## Module: Toybox.System

## Overview

## Classes Under Namespace

**Classes:** [AppNotInstalledException](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/AppNotInstalledException.html), [ClockTime](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/ClockTime.html), [ConnectionInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/ConnectionInfo.html), [DeviceSettings](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/DeviceSettings.html), [Intent](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Intent.html), [PreviousOperationNotCompleteException](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/PreviousOperationNotCompleteException.html), [ServiceDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/ServiceDelegate.html), [Stats](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Stats.html), [UnexpectedAppTypeException](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/UnexpectedAppTypeException.html)

## Constant Summary

### UnitsSystem

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| UNIT\_METRIC | 0 | API Level 1.0.0 | Display units in metric units |
| UNIT\_STATUTE | 1 | API Level 1.0.0 | Display units in statute units |

### ScreenShape

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SCREEN\_SHAPE\_ROUND | 1 | API Level 1.2.0 |  |
| SCREEN\_SHAPE\_SEMI\_ROUND | 2 | API Level 1.2.0 |  |
| SCREEN\_SHAPE\_RECTANGLE | 3 | API Level 1.2.0 |  |
| SCREEN\_SHAPE\_SEMI\_OCTAGON | 4 | API Level 3.3.0 |  |

### ButtonInputs

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BUTTON\_INPUT\_SELECT | 0x00000001 | API Level 1.2.0 |  |
| BUTTON\_INPUT\_UP | 0x00000002 | API Level 1.2.0 |  |
| BUTTON\_INPUT\_DOWN | 0x00000004 | API Level 1.2.0 |  |
| BUTTON\_INPUT\_CLOCK | 0x00000010 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_DOWN\_LEFT | 0x00000020 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_DOWN\_RIGHT | 0x00000040 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_ESC | 0x00000080 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_FIND | 0x00000100 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_LAP | 0x00000200 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_LEFT | 0x00000400 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_LIGHT | 0x00000800 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_MODE | 0x00001000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_PAGE | 0x00002000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_POWER | 0x00004000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_RESET | 0x00008000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_RIGHT | 0x00010000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_SPORT | 0x00020000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_START | 0x00040000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_UP\_LEFT | 0x00080000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_UP\_RIGHT | 0x00100000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_ZIN | 0x00200000 | API Level 3.1.0 |  |
| BUTTON\_INPUT\_ZOUT | 0x00400000 | API Level 3.1.0 |  |

### ConnectionState

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONNECTION\_STATE\_NOT\_INITIALIZED | 0 | API Level 3.0.0 | Indicates that the connection is not setup or is inactive. |
| CONNECTION\_STATE\_NOT\_CONNECTED | 1 | API Level 3.0.0 | Indicates that the connection has been setup but is not in range. |
| CONNECTION\_STATE\_CONNECTED | 2 | API Level 3.0.0 | Indicates that the connection is available for use. |

### Language

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LANGUAGE\_ARA | 8389920 | API Level 3.1.0 | Arabic |
| LANGUAGE\_BUL | 8389921 | API Level 3.1.0 | Bulgarian |
| LANGUAGE\_CES | 8389352 | API Level 3.1.0 | Czech |
| LANGUAGE\_CHS | 8389372 | API Level 3.1.0 | Chinese (Simplified) |
| LANGUAGE\_CHT | 8389371 | API Level 3.1.0 | Chinese (Traditional) |
| LANGUAGE\_DAN | 8389353 | API Level 3.1.0 | Danish |
| LANGUAGE\_DEU | 8389358 | API Level 3.1.0 | German |
| LANGUAGE\_DUT | 8389354 | API Level 3.1.0 | Dutch |
| LANGUAGE\_ENG | 8389355 | API Level 3.1.0 | English |
| LANGUAGE\_EST | 8390796 | API Level 3.1.0 | Estonian |
| LANGUAGE\_FIN | 8389356 | API Level 3.1.0 | Finnish |
| LANGUAGE\_FRE | 8389357 | API Level 3.1.0 | French |
| LANGUAGE\_GRE | 8389359 | API Level 3.1.0 | Greek |
| LANGUAGE\_HEB | 8389919 | API Level 3.1.0 | Hebrew |
| LANGUAGE\_HRV | 8389361 | API Level 3.1.0 | Croatian |
| LANGUAGE\_HUN | 8389360 | API Level 3.1.0 | Hungarian |
| LANGUAGE\_IND | 8389578 | API Level 3.1.0 | Bahasa Indonesia |
| LANGUAGE\_ITA | 8389362 | API Level 3.1.0 | Italian |
| LANGUAGE\_JPN | 8389373 | API Level 3.1.0 | Japanese |
| LANGUAGE\_KOR | 8389696 | API Level 3.1.0 | Korean |
| LANGUAGE\_LAV | 8390797 | API Level 3.1.0 | Latvian |
| LANGUAGE\_LIT | 8390798 | API Level 3.1.0 | Lithuanian |
| LANGUAGE\_NOB | 8389363 | API Level 3.1.0 | Norwegian |
| LANGUAGE\_POL | 8389364 | API Level 3.1.0 | Polish |
| LANGUAGE\_POR | 8389365 | API Level 3.1.0 | Portuguese |
| LANGUAGE\_RON | 8390799 | API Level 3.1.0 | Romanian |
| LANGUAGE\_RUS | 8389366 | API Level 3.1.0 | Russian |
| LANGUAGE\_SLO | 8389367 | API Level 3.1.0 | Slovak |
| LANGUAGE\_SLV | 8389368 | API Level 3.1.0 | Slovenian |
| LANGUAGE\_SPA | 8389369 | API Level 3.1.0 | Spanish |
| LANGUAGE\_SWE | 8389370 | API Level 3.1.0 | Swedish |
| LANGUAGE\_THA | 8389548 | API Level 3.1.0 | Thai |
| LANGUAGE\_TUR | 8389774 | API Level 3.1.0 | Turkish |
| LANGUAGE\_UKR | 8390800 | API Level 3.1.0 | Ukrainian |
| LANGUAGE\_VIE | 8390206 | API Level 3.1.0 | Vietnamese |
| LANGUAGE\_ZSM | 8389579 | API Level 3.1.0 | Standard (Bahasa) Malay |

### DisplayMode

Enum class for display mode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DISPLAY\_MODE\_HIGH\_POWER | 0 | API Level 5.0.0 | Display in high power mode. [View.onUpdate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onUpdate-instance_function) are not subject to burn-in protection. |
| DISPLAY\_MODE\_LOW\_POWER | 1 | API Level 5.0.0 | Display in low power mode, including watch face always-on mode. [View.onUpdate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onUpdate-instance_function) subject to burn-in protection. |
| DISPLAY\_MODE\_OFF | 2 | API Level 5.0.0 | Display is off. |

### PhoneOperatingSystem

The platform associated with a connected phone.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| PHONE\_OS\_NOT\_KNOWN | 0 | API Level 5.1.0 |  |
| PHONE\_OS\_ANDROID | 1 | API Level 5.1.0 |  |
| PHONE\_OS\_IOS | 2 | API Level 5.1.0 |  |

## Instance Method Summary

- [**error**](#error-instance_function "error (Instance Function)") (msg as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as **Void**
	Write an error to the console and exit the system.
- [**exit**](#exit-instance_function "exit (Instance Function)") () as **Void**
	End execution of the current app.
- [**exitTo**](#exitTo-instance_function "exitTo (Instance Function)") (intent as [System.Intent](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Intent.html)) as **Void**
	Exit the current app and launch a new app.
- [**getClockTime**](#getClockTime-instance_function "getClockTime (Instance Function)") () as [System.ClockTime](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/ClockTime.html)
	Get the current clock time.
- [**getDeviceSettings**](#getDeviceSettings-instance_function "getDeviceSettings (Instance Function)") () as [System.DeviceSettings](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/DeviceSettings.html)
	Get the current device settings.
- [**getDisplayMode**](#getDisplayMode-instance_function "getDisplayMode (Instance Function)") () as [System.DisplayMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#DisplayMode-module)
	Get the current display mode, only available in devices with AMOLED or LCD screens.
- [**getSystemStats**](#getSystemStats-instance_function "getSystemStats (Instance Function)") () as [System.Stats](https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Stats.html)
	Get the current system stats.
- [**getTimer**](#getTimer-instance_function "getTimer (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the current millisecond timer value.
- [**isAppInstalled**](#isAppInstalled-instance_function "isAppInstalled (Instance Function)") (uri as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Check the installation status of an app.
- [**print**](#print-instance_function "print (Instance Function)") (output as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as **Void**
	Print to the console.
- [**println**](#println-instance_function "println (Instance Function)") (output as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html) or **Null**) as **Void**
	Print to the console with a line terminator.

## Instance Method Details

### error(msg as Lang.String) as Void

Note:

There are never really too many bananas.

### exit() as Void

### exitTo(intent as System.Intent) as Void

### getClockTime() as System.ClockTime

### getDeviceSettings() as System.DeviceSettings

### getDisplayMode() as System.DisplayMode

### getSystemStats() as System.Stats

### getTimer() as Lang.Number

Note:

The returned value typically starts at zero on device boot and will roll over periodically. Assuming the timer starts at zero, this will happen ~25 days after a reboot, and every ~50 days thereafter.
