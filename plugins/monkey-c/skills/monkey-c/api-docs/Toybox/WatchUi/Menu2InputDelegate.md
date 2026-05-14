---
title: Toybox.WatchUi.Menu2InputDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu2InputDelegate.html
---

## Class: Toybox.WatchUi.Menu2InputDelegate

## Overview

## See Also:

- [Toybox.WatchUi.Menu2](Menu2.md)
- [Toybox.WatchUi.MenuItem](MenuItem.md)

## Instance Method Summary

- [**onBack**](#onBack-instance_function "onBack (Instance Function)") () as **Void**
	A Menu2 Back key was pressed.
- [**onDone**](#onDone-instance_function "onDone (Instance Function)") () as **Void**
	A Menu2 Done item was selected.
- [**onFooter**](#onFooter-instance_function "onFooter (Instance Function)") () as **Void**
- [**onNextPage**](#onNextPage-instance_function "onNextPage (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Next* *Page* behavior.
- [**onPreviousPage**](#onPreviousPage-instance_function "onPreviousPage (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Represents the *Previous* *Page* behavior.
- [**onSelect**](#onSelect-instance_function "onSelect (Instance Function)") (item as [WatchUi.MenuItem](MenuItem.md)) as **Void**
	A Menu2 MenuItem was selected.
- [**onTitle**](#onTitle-instance_function "onTitle (Instance Function)") () as **Void**
	A CustomMenu title was selected.
- [**onWrap**](#onWrap-instance_function "onWrap (Instance Function)") (key as [WatchUi.Key](../WatchUi.md#Key-module)) as [Lang.Boolean](../Lang/Boolean.md)
	A Menu2 is preparing to wrap.

## Instance Method Details

### onBack() as Void

### onDone() as Void

### onFooter() as Void

Note:

Prior to ConnectIQ API version 5.1.0, this function was only called on [CustomMenu](CustomMenu.md). It is now used for all [Menu2](Menu2.md) types.

### onNextPage() as Lang.Boolean

### onPreviousPage() as Lang.Boolean

### onSelect(item as WatchUi.MenuItem) as Void

### onTitle() as Void

Note:

Prior to ConnectIQ API version 5.1.0, this function was only called on [CustomMenu](CustomMenu.md). It is now used for all [Menu2](Menu2.md) types.
