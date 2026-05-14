---
title: Toybox.WatchUi.SelectableEvent
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SelectableEvent.html
---

## Class: Toybox.WatchUi.SelectableEvent

## Overview

SelectableEvent is an object sent to [InputDelegate](InputDelegate.md) when a [Selectable](Selectable.md) is manipulated using physical buttons or touch screen.

## See Also:

- [Toybox.WatchUi.Selectable](Selectable.md)

## Instance Method Summary

- [**getInstance**](#getInstance-instance_function "getInstance (Instance Function)") () as [WatchUi.Selectable](Selectable.md)
	Get the instance of the manipulated [Selectable](Selectable.md).
- [**getPreviousState**](#getPreviousState-instance_function "getPreviousState (Instance Function)") () as [Lang.Symbol](../Lang/Symbol.md)
	Get the previous state of the Selectable that generated the event.

## Instance Method Details

### getInstance() as WatchUi.Selectable

Get the instance of the manipulated [Selectable](Selectable.md).

### getPreviousState() as Lang.Symbol

Get the previous state of the Selectable that generated the event.
