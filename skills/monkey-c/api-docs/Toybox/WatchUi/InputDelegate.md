---
title: Toybox.WatchUi.InputDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html
---

## Class: Toybox.WatchUi.InputDelegate

## Overview

InputDelegate handles basic input events.

There are four types of basic inputs InputDelegate can handle:

- Key, represented by [KeyEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html)
- Touch, represented by [ClickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ClickEvent.html)
- Swipe, represented by [SwipeEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SwipeEvent.html)
- Selectable, represented by [SelectableEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SelectableEvent.html)

This class is the base class for [BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html), which goes beyond simple key and screen-based input.

## See Also:

- [Toybox.WatchUi.BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html)

## Direct Known Subclasses

[WatchUi.BehaviorDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BehaviorDelegate.html)

## Instance Method Summary

- [**onDrag**](#onDrag-instance_function "onDrag (Instance Function)") (dragEvent as [WatchUi.DragEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DragEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A touch screen drag event has occurred.
- [**onFlick**](#onFlick-instance_function "onFlick (Instance Function)") (flickEvent as [WatchUi.FlickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/FlickEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A touch screen flick event has occurred.
- [**onHold**](#onHold-instance_function "onHold (Instance Function)") (clickEvent as [WatchUi.ClickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ClickEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A touch screen hold event has occurred.
- [**onKey**](#onKey-instance_function "onKey (Instance Function)") (keyEvent as [WatchUi.KeyEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A physical button has been pressed and released.
- [**onKeyPressed**](#onKeyPressed-instance_function "onKeyPressed (Instance Function)") (keyEvent as [WatchUi.KeyEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A physical button has been pressed down.
- [**onKeyReleased**](#onKeyReleased-instance_function "onKeyReleased (Instance Function)") (keyEvent as [WatchUi.KeyEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A physical button has been released.
- [**onRelease**](#onRelease-instance_function "onRelease (Instance Function)") (clickEvent as [WatchUi.ClickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ClickEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A touch screen release event has occurred.
- [**onSelectable**](#onSelectable-instance_function "onSelectable (Instance Function)") (selectableEvent as [WatchUi.SelectableEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SelectableEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	The state of a [Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html) has changed.
- [**onSwipe**](#onSwipe-instance_function "onSwipe (Instance Function)") (swipeEvent as [WatchUi.SwipeEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SwipeEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A touch screen swipe event has occurred.
- [**onTap**](#onTap-instance_function "onTap (Instance Function)") (clickEvent as [WatchUi.ClickEvent](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ClickEvent.html)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	A screen tap event has occurred.

## Instance Method Details

### onDrag(dragEvent as WatchUi.DragEvent) as Lang.Boolean

A touch screen drag event has occurred.

This is sent when the touch screen is dragged.

### onFlick(flickEvent as WatchUi.FlickEvent) as Lang.Boolean

A touch screen flick event has occurred.

This is sent when the touch screen is flicked.

### onHold(clickEvent as WatchUi.ClickEvent) as Lang.Boolean

A touch screen hold event has occurred.

This is sent when the touch screen is touched and not released.

### onKey(keyEvent as WatchUi.KeyEvent) as Lang.Boolean

A physical button has been pressed and released.

To find out which key was pressed, use [KeyEvent.getKey()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html#getKey-instance_function) to get the button's [WatchUi.KEY\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#KEY_POWER-const) enum value.

### onKeyPressed(keyEvent as WatchUi.KeyEvent) as Lang.Boolean

A physical button has been pressed down.

To find out which key was pressed, use [KeyEvent.getKey()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html#getKey-instance_function) to get the button's [WatchUi.KEY\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#KEY_POWER-const) enum value.

### onKeyReleased(keyEvent as WatchUi.KeyEvent) as Lang.Boolean

A physical button has been released.

To find out which key was pressed, use [KeyEvent.getKey()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/KeyEvent.html#getKey-instance_function) to get the button's [WatchUi.KEY\_\*](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#KEY_POWER-const) enum value.

### onRelease(clickEvent as WatchUi.ClickEvent) as Lang.Boolean

A touch screen release event has occurred.

This is only sent after an [onHold()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html#onHold-instance_function) event, once the hold on the touch screen is released.

### onSelectable(selectableEvent as WatchUi.SelectableEvent) as Lang.Boolean

The state of a [Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html) has changed.

### onSwipe(swipeEvent as WatchUi.SwipeEvent) as Lang.Boolean

A touch screen swipe event has occurred.

This is sent when the touch screen is swiped.

### onTap(clickEvent as WatchUi.ClickEvent) as Lang.Boolean

A screen tap event has occurred.

This is sent when the touch screen is tapped (a quick touch and release).
