---
title: Toybox.WatchUi.SelectableEvent
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SelectableEvent.html
---

## Class: Toybox.WatchUi.SelectableEvent

## Overview

SelectableEvent is an object sent to [InputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/InputDelegate.html) when a [Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html) is manipulated using physical buttons or touch screen.

## See Also:

- [Toybox.WatchUi.Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html)

## Instance Method Summary

- [**getInstance**](#getInstance-instance_function "getInstance (Instance Function)") () as [WatchUi.Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html)
	Get the instance of the manipulated [Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html).
- [**getPreviousState**](#getPreviousState-instance_function "getPreviousState (Instance Function)") () as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html)
	Get the previous state of the Selectable that generated the event.

## Instance Method Details

### getInstance() as WatchUi.Selectable

Get the instance of the manipulated [Selectable](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Selectable.html).

### getPreviousState() as Lang.Symbol

Get the previous state of the Selectable that generated the event.
