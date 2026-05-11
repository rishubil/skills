---
title: Toybox.WatchUi.BehaviorDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html
---

## Class: Toybox.WatchUi.BehaviorDelegate

## Overview

## See Also:

- [Toybox.WatchUi.InputDelegate](InputDelegate.md)

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.
- [**onActionMenu**](#onActionMenu-instance_function "onActionMenu (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
- [**onBack**](#onBack-instance_function "onBack (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Back* behavior.
- [**onMenu**](#onMenu-instance_function "onMenu (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
- [**onNextMode**](#onNextMode-instance_function "onNextMode (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Next* behavior.
- [**onNextPage**](#onNextPage-instance_function "onNextPage (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Next* *Page* behavior.
- [**onPreviousMode**](#onPreviousMode-instance_function "onPreviousMode (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Previous* *Mode* behavior.
- [**onPreviousPage**](#onPreviousPage-instance_function "onPreviousPage (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Previous* *Page* behavior.
- [**onSelect**](#onSelect-instance_function "onSelect (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Selection* behavior.

## Instance Method Details

### initialize()

### onActionMenu() as Lang.Boolean

### onBack() as Lang.Boolean

Note:

Some devices interpret [SWIPE\_RIGHT](../WatchUi.md#SWIPE_RIGHT-const) [SwipeEvents](SwipeEvent.md) as [KEY\_ESC](../WatchUi.md#KEY_ESC-const) events. On these devices, returning `false` will cause [onKey()](InputDelegate.md#onKey-instance_function) to be called rather than [onSwipe()](InputDelegate.md#onSwipe-instance_function).
