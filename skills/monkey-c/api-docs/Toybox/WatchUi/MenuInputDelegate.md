---
title: Toybox.WatchUi.MenuInputDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuInputDelegate.html
---

## Class: Toybox.WatchUi.MenuInputDelegate

Inherits:

Toybox.Lang.Object
- [Toybox.Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)
- [Toybox.WatchUi.MenuInputDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/MenuInputDelegate.html)
[show all](#)

## Overview

MenuInputDelegate responds to a Menu selection.

This class should be extended to handle selected Menu items.

## See Also:

- [Toybox.WatchUi.Menu](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Menu.html)

## Instance Method Summary

- [**onMenuItem**](#onMenuItem-instance_function "onMenuItem (Instance Function)") (item as [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html)) as **Void**
	A Menu item was chosen.

## Instance Method Details

### onMenuItem(item as Lang.Symbol) as Void

A Menu item was chosen.

This method is called when a Menu item has been selected, and receives the Menu item as an argument.
