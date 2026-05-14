---
title: Toybox.Test.Logger
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Test/Logger.html
---

## Class: Toybox.Test.Logger

## Overview

The Logger class provides output capabilities to tests.

It is not necessary to instantiate the Logger class. This is done automatically behind the scenes.

## Instance Method Summary

- [**debug**](#debug-instance_function "debug (Instance Function)") (str as [Lang.Object](../Lang/Object.md)) as **Void**
	Write a debug [String](../Lang/String.md) to the output stream.
- [**error**](#error-instance_function "error (Instance Function)") (str as [Lang.Object](../Lang/Object.md)) as **Void**
	Write an error [String](../Lang/String.md) to the output stream.
- [**warning**](#warning-instance_function "warning (Instance Function)") (str as [Lang.Object](../Lang/Object.md)) as **Void**
	Write a warning [String](../Lang/String.md) to the output stream.

## Instance Method Details

### debug(str as Lang.Object) as Void

Write a debug [String](../Lang/String.md) to the output stream.

The String is prefixed with DEBUG and a time stamp.

### error(str as Lang.Object) as Void

Write an error [String](../Lang/String.md) to the output stream.

The String is prefixed with ERROR and time stamp.

### warning(str as Lang.Object) as Void

Write a warning [String](../Lang/String.md) to the output stream.

The String is prefixed with WARNING and a time stamp.
