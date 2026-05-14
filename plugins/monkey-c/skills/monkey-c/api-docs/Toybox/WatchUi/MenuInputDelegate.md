---
title: Toybox.WatchUi.MenuInputDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuInputDelegate.html
---

## Class: Toybox.WatchUi.MenuInputDelegate

Inherits:

Toybox.Lang.Object
- [Toybox.Lang.Object](../Lang/Object.md)
- [Toybox.WatchUi.MenuInputDelegate](MenuInputDelegate.md)
[show all](#)

## Overview

MenuInputDelegate responds to a Menu selection.

This class should be extended to handle selected Menu items.

## See Also:

- [Toybox.WatchUi.Menu](Menu.md)

## Instance Method Summary

- [**onMenuItem**](#onMenuItem-instance_function "onMenuItem (Instance Function)") (item as [Lang.Symbol](../Lang/Symbol.md)) as **Void**
	A Menu item was chosen.

## Instance Method Details

### onMenuItem(item as Lang.Symbol) as Void

A Menu item was chosen.

This method is called when a Menu item has been selected, and receives the Menu item as an argument.
