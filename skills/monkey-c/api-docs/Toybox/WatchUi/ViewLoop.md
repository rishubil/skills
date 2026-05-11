---
title: Toybox.WatchUi.ViewLoop
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoop.html
---

## Class: Toybox.WatchUi.ViewLoop

## Overview

## Constant Summary

### Direction

Specifies the direction to transition views

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DIRECTION\_PREVIOUS | 1 | API Level 3.4.0 | Loop in the backward direction |

## Instance Method Summary

- [**changeView**](#changeView-instance_function "changeView (Instance Function)") (direction as [ViewLoop.Direction](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoop.html#Direction-module)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Change the view to the next/previous one in the view loop based on the direction and display the page indicator after transitioning.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (factory as [WatchUi.ViewLoopFactory](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/ViewLoopFactory.html), options as {:page as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:wrap as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html),:color as [Graphics.ColorType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics.html#ColorType-named_type) } or **Null**)
	Constructor for the ViewLoop.
