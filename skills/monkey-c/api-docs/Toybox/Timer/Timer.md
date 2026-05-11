---
title: Toybox.Timer.Timer
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Timer/Timer.html
---

## Class: Toybox.Timer.Timer

## Overview

A Timer object will invoke a callback function after a specified number of milliseconds.

There are two types of timers: one-shot or repeating. A one-shot Timer will only run once after the Timer expires, while a repeating Timer will invoke the callback function every n milliseconds until stop() is called. If a repeating Timer fails to run before its next execution time, then any missed executions will be skipped.

The number of available timers (default 3) and the minimum time value (default 50 ms) depends on the host system. An error will occur if too many timers are set.

## Instance Method Summary

- [**start**](#start-instance_function "start (Instance Function)") (callback as [Lang.Method](../Lang/Method.md) () as **Void**, time as [Lang.Number](../Lang/Number.md), repeat as [Lang.Boolean](../Lang/Boolean.md)) as **Void**
	Start the Timer.
- [**stop**](#stop-instance_function "stop (Instance Function)") () as **Void**
	Stops the Timer from running.

## Instance Method Details

### start(callback as Lang.Method() as Void, time as Lang.Number, repeat as Lang.Boolean) as Void

Start the Timer.

Note:

Will cause an app crash if called from a watch face app while in low power mode

### stop() as Void

Stops the Timer from running.

This only needs to be called for repeating timers. A Timer can be started again by calling start().
