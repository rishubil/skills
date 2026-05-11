---
title: Toybox.System.UnexpectedAppTypeException
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System/UnexpectedAppTypeException.html
---

## Class: Toybox.System.UnexpectedAppTypeException

## Overview

This exception indicates that the app targeted by an Intent when exiting to the app is not an allowed app type.

Allowed app types currently include watch-apps (both native activities and Connect IQ apps) and widgets. Watch faces and data fields cannot be targeted. If a native activity that has a Connect IQ data field configured is targeted, the native app will receive the Intent, not the data field.

## See Also:

- [Toybox.Lang.Exception](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Exception.html)

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (msg as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html))
	Constructor.

## Instance Method Details

### initialize(msg as Lang.String)

Constructor
