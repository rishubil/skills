---
title: Toybox.WatchUi.SimpleDataField
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SimpleDataField.html
---

## Class: Toybox.WatchUi.SimpleDataField

## Overview

Create a SimpleDataField.

A SimpleDataField is a special View that automatically provides [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html) once per second via the [compute()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SimpleDataField.html#compute-instance_function) method.

Just like in a [DataField](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html), a SimpleDataField automatically provides [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html) once per second via the [compute()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SimpleDataField.html#compute-instance_function) method. In exchange for the flexibility offered in a DataField, all field layout is handled automatically in a SimpleDataField.

A SimpleDataField requires two items:

- A [compute()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/SimpleDataField.html#compute-instance_function) method should return the value to be displayed by the SimpleDataField. Allowed types are Number, Float, Long, Double, Duration, and String.
- A "label" variable, which should be assigned a String label for the field.

## See Also:

- [Toybox.WatchUi.DataField](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/DataField.html)
- [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html)
Note:

The system will call the onUpdate() method inherited from View when a Data Field is displayed by the system. Because compute() and onUpdate() are asynchronous, there is no guarantee that compute() will be called before onUpdate(). For this reason, variables should never be initialized in compute().

## Instance Member Summary

- [**label**](#label-var "label (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	The field label String.

## Instance Method Summary

- [**compute**](#compute-instance_function "compute (Instance Function)") (info as [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html)) as [Lang.Numeric](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html#Numeric-named_type) or [Time.Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	Retrieve [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html) in a SimpleDataField.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.

## Instance Attribute Details

### var label as Lang.String

The field label String.

## Instance Method Details

### compute(info as Activity.Info) as Lang.Numeric or Time.Duration or Lang.String or Null

Retrieve [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html) in a SimpleDataField.

This method is called once per second and automatically provides [Activity.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Activity/Info.html) to the SimpleDataField object for display or additional computation. It is necessary to override `compute()` when implementing a SimpleDataField. The value to be displayed in the field must be returned by this method.

### initialize()

Constructor
