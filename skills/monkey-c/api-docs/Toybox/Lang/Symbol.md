---
title: Toybox.Lang.Symbol
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html
---

## Class: Toybox.Lang.Symbol

## Overview

A Symbol is a lightweight constant identifier.

The Monkey C compiler will assign a new value when it encounters a new Symbol. This allows a developer to use Symbol objects as keys or constant values without explicitly declaring a `constant` or `enum`. While Symbol values are constant for a build, their values may change across builds.

For this reason, Symbol objects should not be used for persistent data.

## Instance Method Summary

- [**toNumber**](#toNumber-instance_function "toNumber (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Convert a Symbol to a Number This will return a number containing the integer value of the symbol.
- [**toString**](#toString-instance_function "toString (Instance Function)") () as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Convert a Symbol to a String This will return the string for the name of the symbol in development builds.

## Instance Method Details

### toNumber() as Lang.Number

Convert a Symbol to a Number

This will return a number containing the integer value of the symbol.

### toString() as Lang.String

Convert a Symbol to a String

This will return the string for the name of the symbol in development builds. Because Monkey C does not contain runtime reflection information in release builds, the returned string will be different and will follow the format "symbol (num)". In this format, "num" is the integer value of the symbol.
