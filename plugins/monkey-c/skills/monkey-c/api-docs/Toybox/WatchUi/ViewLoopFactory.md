---
title: Toybox.WatchUi.ViewLoopFactory
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoopFactory.html
---

## Class: Toybox.WatchUi.ViewLoopFactory

## Overview

## Typedef Summary

- [**Delegates**](#Delegates-named_type "Delegates (Named Type)") as [WatchUi.BehaviorDelegate](BehaviorDelegate.md) or [WatchUi.Menu2InputDelegate](Menu2InputDelegate.md)
	Delegate types that can be provided by a ViewLoopFactory.
- [**Views**](#Views-named_type "Views (Named Type)") as [WatchUi.View](View.md)
	View types that can be provided by a ViewLoopFactory.

## Instance Method Summary

- [**getSize**](#getSize-instance_function "getSize (Instance Function)") () as [Lang.Number](../Lang/Number.md)
	Return the number of view/delegate pairs that are managed by this factory.
- [**getView**](#getView-instance_function "getView (Instance Function)") (page as [Lang.Number](../Lang/Number.md)) as \[ [ViewLoopFactory.Views](ViewLoopFactory.md#Views-named_type) \] or \[ [ViewLoopFactory.Views](ViewLoopFactory.md#Views-named_type), [ViewLoopFactory.Delegates](ViewLoopFactory.md#Delegates-named_type) \]
	This function will be called by the system to retrieve a view/delegate pair for the page at the given index.

## Typedef Details

### Delegates as WatchUi.BehaviorDelegate or WatchUi.Menu2InputDelegate

### Views as WatchUi.View

## Instance Method Details

### getSize() as Lang.Number

### getView(page as Lang.Number) as \[ ViewLoopFactory.Views \] or \[ ViewLoopFactory.Views, ViewLoopFactory.Delegates \]

Note:

This method must be overridden in derived classes. If called, this function will cause the application to crash.

Note:

[Menu2](Menu2.md) and [Menu2InputDelegate](Menu2InputDelegate.md) support added for API version 5.1.0.
