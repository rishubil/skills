---
title: Toybox.WatchUi
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html
---

## Module: Toybox.WatchUi

## Overview

Note:

All keys in the key types enum listed after EXTENDED\_KEYS (16) were added after ConnectIQ version 1.1.2. Before evaluating these keys, check for the availability of these keys with a `has` check: if (Toybox.WatchUi has:EXTENDED\_KEYS) [...](https://developer.garmin.com/connect-iq/api-docs/index.html)

## Classes Under Namespace

**Classes:** [ActionMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ActionMenu.html), [ActionMenuDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ActionMenuDelegate.html), [ActionMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ActionMenuItem.html), [AnimationDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationDelegate.html), [AnimationLayer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationLayer.html), [AnimationResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationResource.html), [BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html), [Bitmap](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Bitmap.html), [BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html), [Button](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Button.html), [CheckboxMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CheckboxMenu.html), [CheckboxMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CheckboxMenuItem.html), [ClickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ClickEvent.html), [ComplicationDrawableRef](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ComplicationDrawableRef.html), [Confirmation](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Confirmation.html), [ConfirmationDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ConfirmationDelegate.html), [CustomMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenu.html), [CustomMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/CustomMenuItem.html), [DataField](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html), [DataFieldAlert](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataFieldAlert.html), [DragEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DragEvent.html), [Drawable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Drawable.html), [FlickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FlickEvent.html), [FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html), [GlanceView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/GlanceView.html), [GlanceViewDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/GlanceViewDelegate.html), [IconMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/IconMenuItem.html), [InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html), [InvalidMenuItemTypeException](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InvalidMenuItemTypeException.html), [InvalidPointException](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InvalidPointException.html), [InvalidSelectableStateException](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InvalidSelectableStateException.html), [KeyEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html), [Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html), [MapMarker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapMarker.html), [MapPolyline](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapPolyline.html), [MapTrackView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapTrackView.html), [MapView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html), [Menu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu.html), [Menu2](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2.html), [Menu2InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2InputDelegate.html), [MenuInputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuInputDelegate.html), [MenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuItem.html), [NumberPicker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPicker.html), [NumberPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPickerDelegate.html), [Picker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Picker.html), [PickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerDelegate.html), [PickerFactory](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerFactory.html), [ProgressBar](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ProgressBar.html), [ReviewResponseToken](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ReviewResponseToken.html), [Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html), [SelectableEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SelectableEvent.html), [SimpleDataField](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SimpleDataField.html), [SwipeEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SwipeEvent.html), [Text](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Text.html), [TextArea](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextArea.html), [TextPicker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPicker.html), [TextPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPickerDelegate.html), [ToggleMenuItem](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ToggleMenuItem.html), [TransparentProgressBar](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TransparentProgressBar.html), [View](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html), [ViewLoop](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoop.html), [ViewLoopDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoopDelegate.html), [ViewLoopFactory](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoopFactory.html), [WatchFace](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFace.html), [WatchFaceDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFaceDelegate.html), [WatchFacePowerInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFacePowerInfo.html)

## Constant Summary

### Key

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| KEY\_POWER | 0 | API Level 1.0.0 | The power key |
| KEY\_LIGHT | 1 | API Level 1.0.0 | The light key |
| KEY\_ZIN | 2 | API Level 1.0.0 | The zoom in key |
| KEY\_ZOUT | 3 | API Level 1.0.0 | The zoom out key |
| KEY\_ENTER | 4 | API Level 1.0.0 | The enter key |
| KEY\_ESC | 5 | API Level 1.0.0 | The escape key |
| KEY\_FIND | 6 | API Level 1.0.0 | The find key |
| KEY\_DOWN | 8 | API Level 1.0.0 | The down key |
| KEY\_DOWN\_LEFT | 9 | API Level 1.0.0 | The down left key |
| KEY\_DOWN\_RIGHT | 10 | API Level 1.0.0 | The down key |
| KEY\_LEFT | 11 | API Level 1.0.0 | The left key |
| KEY\_RIGHT | 12 | API Level 1.0.0 | The right key |
| KEY\_UP | 13 | API Level 1.0.0 | The up key |
| KEY\_UP\_LEFT | 14 | API Level 1.0.0 | The up-left |
| KEY\_UP\_RIGHT | 15 | API Level 1.0.0 | The up-right key |
| EXTENDED\_KEYS | 16 | API Level 1.1.2 | Indicates extended key support |
| KEY\_PAGE | 17 | API Level 1.1.2 | The page key |
| KEY\_START | 18 | API Level 1.1.2 | The start key |
| KEY\_LAP | 19 | API Level 1.1.2 | The lap key |
| KEY\_RESET | 20 | API Level 1.1.2 | The reset key |
| KEY\_SPORT | 21 | API Level 1.1.2 | The sport key |
| KEY\_CLOCK | 22 | API Level 1.1.2 | The clock key |
| KEY\_MODE | 23 | API Level 1.1.2 | The mode key |

### AnimationType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ANIM\_TYPE\_LINEAR | 0 | API Level 1.0.0 | Animation with a constant speed |
| ANIM\_TYPE\_EASE\_IN | 1 | API Level 1.0.0 | Animation that increases in speed from start to end |
| ANIM\_TYPE\_EASE\_OUT | 2 | API Level 1.0.0 | Animation that decreases in speed from start to end |
| ANIM\_TYPE\_EASE\_IN\_OUT | 3 | API Level 1.0.0 | Animation that increases in speed from the start, then decreases in speed toward the end |

### KeyPressType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| PRESS\_TYPE\_DOWN | 0 | API Level 1.1.2 | The key is pressed down |
| PRESS\_TYPE\_UP | 1 | API Level 1.1.2 | The key is released |
| PRESS\_TYPE\_ACTION | 2 | API Level 1.1.2 | The key's action is performed |

### ClickType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CLICK\_TYPE\_TAP | 0 | API Level 1.0.0 | A tap on the screen |
| CLICK\_TYPE\_HOLD | 1 | API Level 1.0.0 | A press and hold on the screen |
| CLICK\_TYPE\_RELEASE | 2 | API Level 1.0.0 | A release of a hold on the screen |

### MapMarkerIcon

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MAP\_MARKER\_ICON\_PIN | 0 | API Level 3.0.0 | The default Garmin map marker pin icon |

### MapMode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MAP\_MODE\_PREVIEW | 0 | API Level 3.0.0 | The preview mode for a [MapView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html) |
| MAP\_MODE\_BROWSE | 1 | API Level 3.0.0 | The browse mode for a [MapView](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MapView.html) |

### SwipeDirection

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SWIPE\_UP | 0 | API Level 1.0.0 | A swipe in the upward direction |
| SWIPE\_RIGHT | 1 | API Level 1.0.0 | A swipe towards the right |
| SWIPE\_DOWN | 2 | API Level 1.0.0 | A swipe in the downward direction |
| SWIPE\_LEFT | 3 | API Level 1.0.0 | A swipe towards the left |

### DragType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DRAG\_TYPE\_START | 0 | API Level 3.3.0 | Start of a screen drag |
| DRAG\_TYPE\_CONTINUE | 1 | API Level 3.3.0 | Continuation of a screen drag |
| DRAG\_TYPE\_STOP | 2 | API Level 3.3.0 | Stop of a screen drag |

### ControlBarLeftButton

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONTROL\_BAR\_LEFT\_BUTTON\_BACK | 0 | API Level 4.1.2 |  |
| CONTROL\_BAR\_LEFT\_BUTTON\_CANCEL | 1 | API Level 4.1.2 |  |

### ControlBarRightButton

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONTROL\_BAR\_RIGHT\_BUTTON\_ACCEPT | 2 | API Level 4.1.2 |  |

### AnalogClockState

Set the state for analog clock hands

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ANALOG\_CLOCK\_STATE\_RESTING | 0 | API Level 3.3.0 | Set the clock hands to resting position |
| ANALOG\_CLOCK\_STATE\_SYSTEM\_TIME | 1 | API Level 3.3.0 | Set the clock hands to system time |
| ANALOG\_CLOCK\_STATE\_HOLDING | 2 | API Level 3.3.0 | Set the clock hands to the specified position |

### WatchFaceConfigType

WatchFace config types.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| WATCH\_FACE\_CONFIG\_TYPE\_STYLE | 0 | API Level 5.1.0 |  |
| WATCH\_FACE\_CONFIG\_TYPE\_COMPLICATION | 1 | API Level 5.1.0 |  |
| WATCH\_FACE\_CONFIG\_TYPE\_ACCENT\_COLOR | 2 | API Level 5.1.0 |  |
| WATCH\_FACE\_CONFIG\_TYPE\_COMPLICATION\_COLOR | 3 | API Level 5.1.0 |  |

### MenuTheme

Menu theme for supported devices

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MENU\_THEME\_DEFAULT | 0 | API Level 4.1.8 | The default theme color as specified by the device. |
| MENU\_THEME\_BLUE | 1 | API Level 4.1.8 |  |
| MENU\_THEME\_CYAN | 2 | API Level 4.1.8 |  |
| MENU\_THEME\_GREEN | 3 | API Level 4.1.8 |  |
| MENU\_THEME\_YELLOW | 4 | API Level 4.1.8 |  |
| MENU\_THEME\_ORANGE | 5 | API Level 4.1.8 |  |
| MENU\_THEME\_RED | 6 | API Level 4.1.8 |  |
| MENU\_THEME\_PINK | 7 | API Level 4.1.8 |  |
| MENU\_THEME\_PURPLE | 8 | API Level 4.1.8 |  |
| MENU\_THEME\_GREEN\_YELLOW | 9 | API Level 4.1.8 |  |

### Confirm

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONFIRM\_NO | 0 | API Level 1.0.0 |  |
| CONFIRM\_YES | 1 | API Level 1.0.0 |  |

### NumberPickerMode

**This has been deprecated**

This enum may be removed after System 3.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| NUMBER\_PICKER\_DISTANCE | 0 | API Level 1.0.0 | A Float in meters (m) |
| NUMBER\_PICKER\_TIME | 1 | API Level 1.0.0 | A Duration |
| NUMBER\_PICKER\_TIME\_MIN\_SEC | 2 | API Level 1.0.0 | A Duration |
| NUMBER\_PICKER\_TIME\_OF\_DAY | 3 | API Level 1.0.0 | A Duration representing the number of seconds since midnight |
| NUMBER\_PICKER\_WEIGHT | 4 | API Level 1.0.0 | A Float in kilograms (kg) |
| NUMBER\_PICKER\_HEIGHT | 5 | API Level 1.0.0 | A Float in meters (m) |
| NUMBER\_PICKER\_CALORIES | 6 | API Level 1.0.0 | A Number |
| NUMBER\_PICKER\_BIRTH\_YEAR | 7 | API Level 1.0.0 | A Number |

### SlideType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SLIDE\_IMMEDIATE | 0 | API Level 1.0.0 | No transition. |
| SLIDE\_LEFT | 1 | API Level 1.0.0 | The View slides to the left. |
| SLIDE\_RIGHT | 2 | API Level 1.0.0 | The View slides to the right. |
| SLIDE\_DOWN | 3 | API Level 1.0.0 | The View slides down. |
| SLIDE\_UP | 4 | API Level 1.0.0 | The View slides up. |
| SLIDE\_BLINK | 5 | API Level 3.1.0 | The View fades in. |

### LayoutVerticalAlignment

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LAYOUT\_VALIGN\_TOP | \-0x7FFFFFFF | API Level 1.2.0 | Set a Drawable object's locY property to this to align it to the top edge of the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)). |
| LAYOUT\_VALIGN\_BOTTOM | \-0x7FFFFFFE | API Level 1.2.0 | Set a Drawable object's locY property to this to align it to the bottom edge of the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)). |
| LAYOUT\_VALIGN\_CENTER | \-0x7FFFFFFD | API Level 1.2.0 | Set a Drawable object's locY property to this to center it vertically in the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)). |
| LAYOUT\_VALIGN\_START | \-0x7FFFFFFC | API Level 1.2.0 | Set a Drawable object's locY property to this to make it equal to its parent's locY property. |

### LayoutHorizontalAlignment

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LAYOUT\_HALIGN\_LEFT | \-0x7FFFFFFF | API Level 1.2.0 | Set a Drawable object's locX property to this to align it along the left edge of the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)). |
| LAYOUT\_HALIGN\_RIGHT | \-0x7FFFFFFE | API Level 1.2.0 | Set a Drawable object's locX property to this to align it along the right edge of the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)). |
| LAYOUT\_HALIGN\_CENTER | \-0x7FFFFFFD | API Level 1.2.0 | Set a Drawable object's locX property to this to center it horizontally in the device context ([Dc](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/Dc.html)). |
| LAYOUT\_HALIGN\_START | \-0x7FFFFFFC | API Level 1.2.0 | Set a Drawable object's locX property to this to make it equal to its parent's locX property. |

### AnimationEvent

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ANIMATION\_EVENT\_COMPLETE | 0 | API Level 3.1.0 | Indicates the completion of an animation. |
| ANIMATION\_EVENT\_CANCELED | 1 | API Level 3.1.0 | Indicates the cancel of the animation playback |

### ActionMenuTheme

The theme for the ActionMenu

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ACTION\_MENU\_THEME\_DARK | 0 | API Level 3.4.0 | Dark theme for the action menu |
| ACTION\_MENU\_THEME\_LIGHT | 1 | API Level 3.4.0 | Light theme for the action menu |

### ReviewRequestStatus

Enum class for makeReviewTokenRequest return status

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| REVIEW\_REQUEST\_STATUS\_GRANTED | 0 | API Level 3.4.2 |  |
| REVIEW\_REQUEST\_STATUS\_DENIED | 1 | API Level 3.4.2 |  |
| REVIEW\_REQUEST\_STATUS\_FAILED | 2 | API Level 3.4.2 |  |

## Typedef Summary

- [**InputDelegates**](#InputDelegates-named_type "InputDelegates (Named Type)") as [WatchUi.InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html) or [WatchUi.BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html) or [WatchUi.ConfirmationDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ConfirmationDelegate.html) or [WatchUi.MenuInputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuInputDelegate.html) or [WatchUi.NumberPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPickerDelegate.html) or [WatchUi.PickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/PickerDelegate.html) or [WatchUi.TextPickerDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPickerDelegate.html) or [WatchUi.WatchFaceDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/WatchFaceDelegate.html) or [WatchUi.Menu2InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2InputDelegate.html) or [WatchUi.ViewLoopDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoopDelegate.html)
- [**Resource**](#Resource-named_type "Resource (Named Type)") as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [WatchUi.AnimationResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/AnimationResource.html) or [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [WatchUi.FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) or [Graphics.FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html)
- [**TouchEventSettings**](#TouchEventSettings-named_type "TouchEventSettings (Named Type)") as {:enabled as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) }
- [**Views**](#Views-named_type "Views (Named Type)") as [WatchUi.View](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html) or [WatchUi.Menu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu.html) or [WatchUi.TextPicker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/TextPicker.html) or [WatchUi.ProgressBar](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ProgressBar.html) or [WatchUi.Confirmation](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Confirmation.html) or [WatchUi.NumberPicker](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/NumberPicker.html) or [WatchUi.ViewLoop](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoop.html)

## Instance Method Summary

- [**animate**](#animate-instance_function "animate (Instance Function)") (object as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html), property as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html), type as [WatchUi.AnimationType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#AnimationType-module), start as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), stop as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), period as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type), callback as **Null** or [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html) () as **Void**) as **Void**
	Animate an Object.
- [**cancelAllAnimations**](#cancelAllAnimations-instance_function "cancelAllAnimations (Instance Function)") () as **Void**
	Cancel animations started with [WatchUi.animate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#animate-instance_function) Stop all animations that were started with [WatchUi.animate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#animate-instance_function).
- [**configureTouchEvents**](#configureTouchEvents-instance_function "configureTouchEvents (Instance Function)") (options as [WatchUi.TouchEventSettings](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#TouchEventSettings-named_type)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Configurate touch event settings, only allowed for Watch Apps and Audio Content Providers when running in the foreground mode.
- [**getCurrentView**](#getCurrentView-instance_function "getCurrentView (Instance Function)") () as \[ [WatchUi.View](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html) or **Null**, [WatchUi.InputDelegates](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#InputDelegates-named_type) or **Null** \]
	Get the current view that is displayed in the UI.
- [**getSubscreen**](#getSubscreen-instance_function "getSubscreen (Instance Function)") () as [Graphics.BoundingBox](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BoundingBox.html) or **Null**
	Get the subscreen area in the display.
- [**getTouchEventsConfiguration**](#getTouchEventsConfiguration-instance_function "getTouchEventsConfiguration (Instance Function)") () as [WatchUi.TouchEventSettings](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#TouchEventSettings-named_type)
	Returns the current touch event settings.
- [**loadResource**](#loadResource-instance_function "loadResource (Instance Function)") (resource as [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html)) as [WatchUi.Resource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Resource-named_type)
	Load a resource from the executable.
- [**makeReviewTokenRequest**](#makeReviewTokenRequest-instance_function "makeReviewTokenRequest (Instance Function)") (callback as [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html) (responseStatus as [WatchUi.ReviewRequestStatus](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#ReviewRequestStatus-module), token as [WatchUi.ReviewResponseToken](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ReviewResponseToken.html) or **Null**) as **Void**) as **Void**
	Initiate a request to ask for this app to be reviewed.
- [**popView**](#popView-instance_function "popView (Instance Function)") (transition as [WatchUi.SlideType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#SlideType-module)) as **Void**
	Pop the current View from the View stack.
- [**pushView**](#pushView-instance_function "pushView (Instance Function)") (view as [WatchUi.Views](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Views-named_type), delegate as [WatchUi.InputDelegates](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#InputDelegates-named_type) or **Null**, transition as [WatchUi.SlideType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#SlideType-module)) as **Void**
	Push a View onto the View stack.
- [**requestUpdate**](#requestUpdate-instance_function "requestUpdate (Instance Function)") () as **Void**
	Request a call to the [onUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onUpdate-instance_function) method for the current View.
- [**showActionMenu**](#showActionMenu-instance_function "showActionMenu (Instance Function)") (menu as [WatchUi.ActionMenu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ActionMenu.html), delegate as [WatchUi.ActionMenuDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ActionMenuDelegate.html)) as **Void**
- [**showToast**](#showToast-instance_function "showToast (Instance Function)") (text as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), options as {:icon as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html) } or **Null**) as **Void**
	Push a toast notification to the display.
- [**startUserReview**](#startUserReview-instance_function "startUserReview (Instance Function)") (token as [WatchUi.ReviewResponseToken](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ReviewResponseToken.html)) as **Void**
	Start the app review UI flow.
- [**switchToView**](#switchToView-instance_function "switchToView (Instance Function)") (view as [WatchUi.Views](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Views-named_type), delegate as [WatchUi.InputDelegates](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#InputDelegates-named_type) or **Null**, transition as [WatchUi.SlideType](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#SlideType-module)) as **Void**
	Pop the current View from the View stack and push a new one.

## Instance Method Details

### animate(object as Lang.Object, property as Lang.Symbol, type as WatchUi.AnimationType, start as Lang.Numeric, stop as Lang.Numeric, period as Lang.Numeric, callback as Null or Lang.Method() as Void) as Void

Note:

Will cause an app crash if called from background or data field app, or from watch face while in low power mode

### cancelAllAnimations() as Void

### configureTouchEvents(options as WatchUi.TouchEventSettings) as Lang.Boolean

### getCurrentView() as \[ WatchUi.View or Null, WatchUi.InputDelegates or Null \]

### getSubscreen() as Graphics.BoundingBox or Null

### getTouchEventsConfiguration() as WatchUi.TouchEventSettings

### loadResource(resource as Lang.ResourceId) as WatchUi.Resource

Note:

[Toybox::Graphics::BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) and [Toybox::Graphics::FontReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/FontReference.html) are returned for [Toybox::WatchUi::BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) and [Toybox::WatchUi::FontResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FontResource.html) in CIQ 4.0.0 and later.

### makeReviewTokenRequest(callback as Lang.Method(responseStatus as WatchUi.ReviewRequestStatus, token as WatchUi.ReviewResponseToken or Null) as Void) as Void

### popView(transition as WatchUi.SlideType) as Void

### pushView(view as WatchUi.Views, delegate as WatchUi.InputDelegates or Null, transition as WatchUi.SlideType) as Void

### requestUpdate() as Void

### showToast(text as Lang.String or Lang.ResourceId, options as {:icon as WatchUi.BitmapResource or Graphics.BitmapReference or Lang.ResourceId } or Null) as Void

### startUserReview(token as WatchUi.ReviewResponseToken) as Void

### switchToView(view as WatchUi.Views, delegate as WatchUi.InputDelegates or Null, transition as WatchUi.SlideType) as Void

Note:

Prior to ConnectIQ 3.1, this method only supported switching to user-defined View objects, and would only accept InputDelegate or BehaviorDelegate objects as delegates for the given View.
