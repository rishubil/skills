---
title: Toybox.System.Intent
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/System/Intent.html
---

## Class: Toybox.System.Intent

## Overview

An Intent sends content from one app to another app.

Strictly speaking, content is sent to a **URI** by an Intent, which can either be a native activity (e.g. Run, Bike, etc.) or another Connect IQ app. Used in conjunction with [System.exitTo()](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#exitTo-instance_function), Intents can exit the current app and launch a second app, passing information from the originating app to the newly open app.

For example, a widget might collect data from a service via a [Communications](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications.html) call and pass that data to a device app via Intent for use during an activity.

## See Also:

- [System.exitTo()](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#exitTo-instance_function)

## Instance Member Summary

- [**arguments**](#arguments-var "arguments (Var)") as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or **Null**
- [**uri**](#uri-var "uri (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (aURI as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), aArgs as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or **Null**)
	Constructor.

## Instance Attribute Details

### var arguments as Lang.Dictionary or Null

### var uri as Lang.String

## Instance Method Details

### initialize(aURI as Lang.String, aArgs as Lang.Dictionary or Null)

Constructor
