---
title: Toybox.Complications.Complication
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications/Complication.html
---

## Class: Toybox.Complications.Complication

## Overview

Complication object

## Instance Member Summary

- [**complicationId**](#complicationId-var "complicationId (Var)") as [Complications.Id](Id.md) or **Null**
- [**longLabel**](#longLabel-var "longLabel (Var)") as [Complications.Label](../Complications.md#Label-named_type) or **Null**
- [**ranges**](#ranges-var "ranges (Var)") as [Complications.Ranges](../Complications.md#Ranges-named_type) or **Null**
- [**shortLabel**](#shortLabel-var "shortLabel (Var)") as [Complications.Label](../Complications.md#Label-named_type) or **Null**
- [**unit**](#unit-var "unit (Var)") as [Complications.Unit](../Complications.md#Unit-module) or [Lang.String](../Lang/String.md) or **Null**
- [**value**](#value-var "value (Var)") as [Complications.Value](../Complications.md#Value-named_type) or **Null**

## Instance Method Summary

- [**getIcon**](#getIcon-instance_function "getIcon (Instance Function)") () as [Complications.Icon](../Complications.md#Icon-named_type) or **Null**
	Get the complication icon.
- [**getType**](#getType-instance_function "getType (Instance Function)") () as [Complications.Type](../Complications.md#Type-module) or **Null**
	Get the complication type.

## Instance Attribute Details

### var complicationId as Complications.Id or Null

### var longLabel as Complications.Label or Null

### var ranges as Complications.Ranges or Null

### var shortLabel as Complications.Label or Null

### var unit as Complications.Unit or Lang.String or Null

### var value as Complications.Value or Null

## Instance Method Details

### getIcon() as Complications.Icon or Null

Get the complication icon. This is only available for user complications

### getType() as Complications.Type or Null

Get the complication type
