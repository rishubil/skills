---
title: Toybox.Background.InvalidBackgroundTimeException
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Background/InvalidBackgroundTimeException.html
---

## Class: Toybox.Background.InvalidBackgroundTimeException

## Overview

Indicates a invalid time was provided to [registerForTemporalEvent()](../Background.md#registerForTemporalEvent-instance_function), which may be invalid because it either:

- Occurs less than five minutes after the last background event occurred
- Has a duration of less than five minutes

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (msg as [Lang.String](../Lang/String.md))
	Constructor.

## Instance Method Details

### initialize(msg as Lang.String)

Constructor
