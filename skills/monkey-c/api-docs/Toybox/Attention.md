---
title: Toybox.Attention
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html
---

## Module: Toybox.Attention

## Overview

## Classes Under Namespace

**Classes:** [BacklightOnTooLongException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention/BacklightOnTooLongException.html), [ToneProfile](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention/ToneProfile.html), [VibeProfile](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention/VibeProfile.html)

## Constant Summary

### Tone

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| TONE\_KEY | 0 | API Level 1.0.0 | Indicates that a key was pressed |
| TONE\_START | 1 | API Level 1.0.0 | Indicates that an activity has started |
| TONE\_STOP | 2 | API Level 1.0.0 | Indicates that an activity has stopped |
| TONE\_MSG | 3 | API Level 1.0.0 | Indicates that a message is available |
| TONE\_ALERT\_HI | 4 | API Level 1.0.0 | An alert ending with a high note |
| TONE\_ALERT\_LO | 5 | API Level 1.0.0 | An alert ending with a low note |
| TONE\_LOUD\_BEEP | 6 | API Level 1.0.0 | A loud beep |
| TONE\_INTERVAL\_ALERT | 7 | API Level 1.0.0 | Indicates a change in interval |
| TONE\_ALARM | 8 | API Level 1.0.0 | Indicates an alarm has triggered |
| TONE\_RESET | 9 | API Level 1.0.0 | Indicates that the activity was reset |
| TONE\_LAP | 10 | API Level 1.0.0 | Indicates that the user has completed a lap |
| TONE\_CANARY | 11 | API Level 1.0.0 | An annoying sound to get the users attention |
| TONE\_TIME\_ALERT | 12 | API Level 1.0.0 | An alert that a time threshold has been met |
| TONE\_DISTANCE\_ALERT | 13 | API Level 1.0.0 | An alert that a distance threshold has been met |
| TONE\_FAILURE | 14 | API Level 1.0.0 | Indicates that the activity was a failure |
| TONE\_SUCCESS | 15 | API Level 1.0.0 | Indicates that the activity was a success |
| TONE\_POWER | 16 | API Level 1.0.0 | The power on tone |
| TONE\_LOW\_BATTERY | 17 | API Level 1.0.0 | Indicates that the device has low battery power |

### FlashlightMode

Flashlight modes

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FLASHLIGHT\_MODE\_OFF | 0 | API Level 3.4.3 |  |
| FLASHLIGHT\_MODE\_ON | 1 | API Level 3.4.3 |  |
| FLASHLIGHT\_MODE\_STROBE | 2 | API Level 3.4.3 |  |

### FlashlightColor

Flashlight colors

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FLASHLIGHT\_COLOR\_WHITE | 0xFFFFFF | API Level 3.4.3 |  |
| FLASHLIGHT\_COLOR\_GREEN | 0x00FF00 | API Level 3.4.3 |  |
| FLASHLIGHT\_COLOR\_RED | 0xFF0000 | API Level 3.4.3 |  |

### FlashlightBrightness

Flashlight brightness

Constants map to device-specific brightness levels

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FLASHLIGHT\_BRIGHTNESS\_LOW | 255 | API Level 3.4.3 |  |
| FLASHLIGHT\_BRIGHTNESS\_MEDIUM | 254 | API Level 3.4.3 |  |
| FLASHLIGHT\_BRIGHTNESS\_HIGH | 253 | API Level 3.4.3 |  |

### FlashlightStrobeMode

Flashlight strobe modes

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FLASHLIGHT\_STROBE\_MODE\_BLINK | 0 | API Level 3.4.3 |  |
| FLASHLIGHT\_STROBE\_MODE\_PULSE | 1 | API Level 3.4.3 |  |
| FLASHLIGHT\_STROBE\_MODE\_BEACON | 2 | API Level 3.4.3 |  |
| FLASHLIGHT\_STROBE\_MODE\_BLITZ | 3 | API Level 3.4.3 |  |

### FlashlightStrobeSpeed

Flashlight strobe speeds

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FLASHLIGHT\_STROBE\_SPEED\_SLOW | 0 | API Level 3.4.3 |  |
| FLASHLIGHT\_STROBE\_SPEED\_MEDIUM | 1 | API Level 3.4.3 |  |
| FLASHLIGHT\_STROBE\_SPEED\_FAST | 2 | API Level 3.4.3 |  |

### FlashlightResult

Flashlight result codes

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FLASHLIGHT\_RESULT\_SUCCESS | 0 | API Level 3.4.3 |  |
| FLASHLIGHT\_RESULT\_INVALID\_COLOR | 1 | API Level 3.4.3 |  |
| FLASHLIGHT\_RESULT\_INVALID\_BRIGHTNESS | 2 | API Level 3.4.3 |  |
| FLASHLIGHT\_RESULT\_INVALID\_MODE | 3 | API Level 3.4.3 |  |
| FLASHLIGHT\_RESULT\_INVALID\_SPEED | 4 | API Level 3.4.3 |  |
| FLASHLIGHT\_RESULT\_FAILURE | 5 | API Level 3.4.3 |  |

## Instance Method Summary

- [**backlight**](#backlight-instance_function "backlight (Instance Function)") (setting as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)) as **Void**
	Control the display backlight.
- [**hasFlashlightColor**](#hasFlashlightColor-instance_function "hasFlashlightColor (Instance Function)") (color as [Attention.FlashlightColor](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#FlashlightColor-module)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Determine if a given flashlight color is supported by this device.
- [**playTone**](#playTone-instance_function "playTone (Instance Function)") (options as [Attention.Tone](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#Tone-module) or {:toneProfile as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Attention.ToneProfile](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention/ToneProfile.html) >,:repeatCount as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) }) as **Void**
	Play a tone.
- [**setFlashlightMode**](#setFlashlightMode-instance_function "setFlashlightMode (Instance Function)") (mode as [Attention.FlashlightMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#FlashlightMode-module), options as {:color as [Attention.FlashlightColor](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#FlashlightColor-module),:brightness as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Attention.FlashlightBrightness](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#FlashlightBrightness-module),:strobeMode as [Attention.FlashlightStrobeMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#FlashlightStrobeMode-module),:strobeSpeed as [Attention.FlashlightStrobeSpeed](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#FlashlightStrobeSpeed-module) } or **Null**) as [Attention.FlashlightResult](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention.html#FlashlightResult-module)
- [**vibrate**](#vibrate-instance_function "vibrate (Instance Function)") (vibeProfiles as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Attention.VibeProfile](https://developer.garmin.com/connect-iq/api-docs/Toybox/Attention/VibeProfile.html) >) as **Void**
	Engage the vibration motor.

## Instance Method Details

### backlight(setting as Lang.Boolean or Lang.Float) as Void

Note:

Passing a [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) is only supported with ConnectIQ 3.2.1 and later.

### hasFlashlightColor(color as Attention.FlashlightColor) as Lang.Boolean

### playTone(options as Attention.Tone or {:toneProfile as Lang.Array<Attention.ToneProfile>,:repeatCount as Lang.Number }) as Void

Note:

Passing an options [Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) is only supported with ConnectIQ 3.1.0 and later.

### setFlashlightMode(mode as Attention.FlashlightMode, options as {:color as Attention.FlashlightColor,:brightness as Lang.Number or Attention.FlashlightBrightness,:strobeMode as Attention.FlashlightStrobeMode,:strobeSpeed as Attention.FlashlightStrobeSpeed } or Null) as Attention.FlashlightResult

### vibrate(vibeProfiles as Lang.Array<Attention.VibeProfile>) as Void

Note:

Forerunner devices do not support vibration patterns. Vibration may still be used, but the vibration will always run at the same duty cycle.
