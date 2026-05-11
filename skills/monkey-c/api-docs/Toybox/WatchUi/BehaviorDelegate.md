---
title: Toybox.WatchUi.BehaviorDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html
---

## Class: Toybox.WatchUi.BehaviorDelegate

## Overview

## See Also:

- [Toybox.WatchUi.InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html)

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onActionMenu**](#onActionMenu-instance_function "onActionMenu (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
- [**onBack**](#onBack-instance_function "onBack (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Represents the *Back* behavior.
- [**onMenu**](#onMenu-instance_function "onMenu (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
- [**onNextMode**](#onNextMode-instance_function "onNextMode (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Represents the *Next* behavior.
- [**onNextPage**](#onNextPage-instance_function "onNextPage (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Represents the *Next* *Page* behavior.
- [**onPreviousMode**](#onPreviousMode-instance_function "onPreviousMode (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Represents the *Previous* *Mode* behavior.
- [**onPreviousPage**](#onPreviousPage-instance_function "onPreviousPage (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Represents the *Previous* *Page* behavior.
- [**onSelect**](#onSelect-instance_function "onSelect (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Represents the *Selection* behavior.

## Instance Method Details

### initialize()

### onActionMenu() as Lang.Boolean

### onBack() as Lang.Boolean

Note:

Some devices interpret [SWIPE\_RIGHT](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#SWIPE_RIGHT-const) [SwipeEvents](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SwipeEvent.html) as [KEY\_ESC](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#KEY_ESC-const) events. On these devices, returning `false` will cause [onKey()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html#onKey-instance_function) to be called rather than [onSwipe()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html#onSwipe-instance_function).
