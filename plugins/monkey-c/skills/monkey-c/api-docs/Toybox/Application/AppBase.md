---
title: Toybox.Application.AppBase
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/AppBase.html
---

## Class: Toybox.Application.AppBase

## Overview

## Direct Known Subclasses

[Application.AudioContentProviderApp](AudioContentProviderApp.md)

## Constant Summary

### GlanceTheme

Glance color themes for supported devices

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| GLANCE\_THEME\_DEFAULT | 0 | API Level 4.0.0 |  |
| GLANCE\_THEME\_BLUE | 1 | API Level 4.0.0 |  |
| GLANCE\_THEME\_GOLD | 2 | API Level 4.0.0 |  |
| GLANCE\_THEME\_GREEN | 3 | API Level 4.0.0 |  |
| GLANCE\_THEME\_LIGHT\_BLUE | 4 | API Level 4.0.0 |  |
| GLANCE\_THEME\_RED | 5 | API Level 4.0.0 |  |
| GLANCE\_THEME\_WHITE | 6 | API Level 4.0.0 |  |
| GLANCE\_THEME\_PURPLE | 7 | API Level 4.0.0 |  |

## Instance Method Summary

- [**allowTrialMessage**](#allowTrialMessage-instance_function "allowTrialMessage (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Check if application trial messages are allowed.
- [**clearProperties**](#clearProperties-instance_function "clearProperties (Instance Function)") () as **Void** deprecated
	Clear the object store for the application.
- [**deleteProperty**](#deleteProperty-instance_function "deleteProperty (Instance Function)") (key as [Application.PropertyKeyType](../Application.md#PropertyKeyType-named_type)) as **Void** deprecated
	Delete the given key from the object store.
- [**getGlanceTheme**](#getGlanceTheme-instance_function "getGlanceTheme (Instance Function)") () as [AppBase.GlanceTheme](AppBase.md#GlanceTheme-module)
	Method to get the glance theme.
- [**getGlanceView**](#getGlanceView-instance_function "getGlanceView (Instance Function)") () as \[ [WatchUi.GlanceView](../WatchUi/GlanceView.md) \] or \[ [WatchUi.GlanceView](../WatchUi/GlanceView.md), [WatchUi.GlanceViewDelegate](../WatchUi/GlanceViewDelegate.md) \] or **Null**
	Override to provide the [WatchUi.GlanceView](../WatchUi/GlanceView.md) and [WatchUi.GlanceViewDelegate](../WatchUi/GlanceViewDelegate.md) for the glance preview.
- [**getGoalView**](#getGoalView-instance_function "getGoalView (Instance Function)") (goalType as [Application.GoalType](../Application.md#GoalType-module)) as \[ [WatchUi.View](../WatchUi/View.md) \] or **Null**
	Override to provide a [WatchUi.View](../WatchUi/View.md) for a goal that has triggered within a watch face.
- [**getInitialView**](#getInitialView-instance_function "getInitialView (Instance Function)") () as \[ [WatchUi.Views](../WatchUi.md#Views-named_type) \] or \[ [WatchUi.Views](../WatchUi.md#Views-named_type), [WatchUi.InputDelegates](../WatchUi.md#InputDelegates-named_type) \]
	Override to provide the initial View and Input Delegate of the application.
- [**getProperty**](#getProperty-instance_function "getProperty (Instance Function)") (key as [Application.PropertyKeyType](../Application.md#PropertyKeyType-named_type)) as [Application.PropertyValueType](../Application.md#PropertyValueType-named_type) deprecated
	Get the data associated with a given key from the object store.
- [**getSensorConfigurationView**](#getSensorConfigurationView-instance_function "getSensorConfigurationView (Instance Function)") (sensor as [Sensor.SensorInfo](../Sensor/SensorInfo.md)) as \[ [WatchUi.Views](../WatchUi.md#Views-named_type) \] or \[ [WatchUi.Views](../WatchUi.md#Views-named_type), [WatchUi.InputDelegates](../WatchUi.md#InputDelegates-named_type) \]
	Override to provide the pairing config View and Input Delegate of the application.
- [**getSensorDelegate**](#getSensorDelegate-instance_function "getSensorDelegate (Instance Function)") () as [Sensor.SensorDelegate](../Sensor/SensorDelegate.md) or **Null**
	Override to provide the Sensor Delegate object.
- [**getServiceDelegate**](#getServiceDelegate-instance_function "getServiceDelegate (Instance Function)") () as \[ [System.ServiceDelegate](../System/ServiceDelegate.md) \]
	Get a [ServiceDelegate](../System/ServiceDelegate.md) to run background tasks for this app.
- [**getSettingsView**](#getSettingsView-instance_function "getSettingsView (Instance Function)") () as \[ [WatchUi.Views](../WatchUi.md#Views-named_type) \] or \[ [WatchUi.Views](../WatchUi.md#Views-named_type), [WatchUi.InputDelegates](../WatchUi.md#InputDelegates-named_type) \] or **Null**
	Override to provide the settings View and Input Delegate of the application.
- [**getSyncDelegate**](#getSyncDelegate-instance_function "getSyncDelegate (Instance Function)") () as [Communications.SyncDelegate](../Communications/SyncDelegate.md) or **Null**
	Get a [SyncDelegate](../Communications/SyncDelegate.md) object that communicates sync status to the system for syncing content to the device.
- [**getTrialDaysRemaining**](#getTrialDaysRemaining-instance_function "getTrialDaysRemaining (Instance Function)") () as [Lang.Number](../Lang/Number.md) or **Null**
	Override to return the number of days remaining in the trial If a developer wishes to implement time-based app trials, they will need to override this function to return the number of days remaining in the trial.
- [**isActive**](#isActive-instance_function "isActive (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	return true if app is currently in active state, otherwise false.
- [**isTrial**](#isTrial-instance_function "isTrial (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Check if the application is in trial mode.
- [**loadProperties**](#loadProperties-instance_function "loadProperties (Instance Function)") () as **Void** deprecated
	Load the properties for the application.
- [**onActive**](#onActive-instance_function "onActive (Instance Function)") (state as [Lang.Dictionary](../Lang/Dictionary.md) or **Null**) as **Void**
	Invoked when app enters active mode, i.e.
- [**onAppInstall**](#onAppInstall-instance_function "onAppInstall (Instance Function)") () as **Void**
	The callback method that is triggered in the background when the app is installed.
- [**onAppUpdate**](#onAppUpdate-instance_function "onAppUpdate (Instance Function)") () as **Void**
	The callback method that is triggered in the background when the app is updated Requires the Background permission to be enabled and your application class to carry the:background annotation.
- [**onAuthenticationRequest**](#onAuthenticationRequest-instance_function "onAuthenticationRequest (Instance Function)") () as **Void**
	Called when an Application requests to run code on demand, during an authentication process.
- [**onBackgroundData**](#onBackgroundData-instance_function "onBackgroundData (Instance Function)") (data as [Application.PersistableType](../Application.md#PersistableType-named_type)) as **Void**
	Handle data passed from a ServiceDelegate to the application.
- [**onDeviceSettingChanged**](#onDeviceSettingChanged-instance_function "onDeviceSettingChanged (Instance Function)") (aSymbol as [Lang.Symbol](../Lang/Symbol.md), aValue as [Lang.Object](../Lang/Object.md)) as **Void**
	A device setting has changed This method is called when a device setting value is changed.
- [**onDisplayModeChanged**](#onDisplayModeChanged-instance_function "onDisplayModeChanged (Instance Function)") () as **Void**
	The display mode has changed, only available in AMOLED or LCD screen products.
- [**onEnhancedReadabilityModeChanged**](#onEnhancedReadabilityModeChanged-instance_function "onEnhancedReadabilityModeChanged (Instance Function)") () as **Void**
	The font mode has changed This method is called when the system changes to or from Enhanced Readability Mode.
- [**onInactive**](#onInactive-instance_function "onInactive (Instance Function)") (state as [Lang.Dictionary](../Lang/Dictionary.md) or **Null**) as **Void**
	Invoked when app enters inactive mode, i.e.
- [**onNightModeChanged**](#onNightModeChanged-instance_function "onNightModeChanged (Instance Function)") () as **Void**
	The display mode has changed This method is called when the system changes to or from night mode.
- [**onSettingsChanged**](#onSettingsChanged-instance_function "onSettingsChanged (Instance Function)") () as **Void**
	Called when the application settings have been changed by Garmin Connect Mobile (GCM) while while the app is running.
- [**onStart**](#onStart-instance_function "onStart (Instance Function)") (state as [Lang.Dictionary](../Lang/Dictionary.md) or **Null**) as **Void**
	Method called at startup to allow handling of app initialization.
- [**onStop**](#onStop-instance_function "onStop (Instance Function)") (state as [Lang.Dictionary](../Lang/Dictionary.md) or **Null**) as **Void**
	Override to handle application cleanup upon termination.
- [**onStorageChanged**](#onStorageChanged-instance_function "onStorageChanged (Instance Function)") () as **Void**
	Called when Application storage is changed by the other running instance, of the app i.e Background Process while the CIQ app is running or vice-versa.
- [**onValidateProperty**](#onValidateProperty-instance_function "onValidateProperty (Instance Function)") (key as [Lang.String](../Lang/String.md), value as [Properties.ValueType](Properties.md#ValueType-named_type)) as [Lang.Boolean](../Lang/Boolean.md) or [Lang.String](../Lang/String.md)
	Called when a property needs to be validated by the application.
- [**openAppSettingsEditor**](#openAppSettingsEditor-instance_function "openAppSettingsEditor (Instance Function)") () as **Void**
	Function to open application settings editor.
- [**saveProperties**](#saveProperties-instance_function "saveProperties (Instance Function)") () as **Void** deprecated
	Save the properties for the application.
- [**setProperty**](#setProperty-instance_function "setProperty (Instance Function)") (key as [Application.PropertyKeyType](../Application.md#PropertyKeyType-named_type), value as [Application.PropertyValueType](../Application.md#PropertyValueType-named_type)) as **Void** deprecated
	Store the given data in the object.
- [**validateProperty**](#validateProperty-instance_function "validateProperty (Instance Function)") (key as [Application.PropertyKeyType](../Application.md#PropertyKeyType-named_type), value as [Application.PropertyValueType](../Application.md#PropertyValueType-named_type)) as **Void**
	Validate a property being stored.

## Instance Method Details

### allowTrialMessage() as Lang.Boolean

### clearProperties() as Void

**This has been deprecated**

This method may be removed after System 4.

Note:

Background processes cannot clear properties.

### deleteProperty(key as Application.PropertyKeyType) as Void

**This has been deprecated**

This method may be removed after System 4.

Note:

Background processes cannot delete properties.

### getGlanceTheme() as AppBase.GlanceTheme

### getGlanceView() as \[ WatchUi.GlanceView \] or \[ WatchUi.GlanceView, WatchUi.GlanceViewDelegate \] or Null

### getGoalView(goalType as Application.GoalType) as \[ WatchUi.View \] or Null

### getInitialView() as \[ WatchUi.Views \] or \[ WatchUi.Views, WatchUi.InputDelegates \]

Note:

This method must be overridden in derived classes. If called, this function will cause the application to crash.

### getProperty(key as Application.PropertyKeyType) as Application.PropertyValueType

**This has been deprecated**

This method may be removed after System 4.

Note:

Symbols can change from build to build and are not to be used for for Keys or Values.

### getSensorConfigurationView(sensor as Sensor.SensorInfo) as \[ WatchUi.Views \] or \[ WatchUi.Views, WatchUi.InputDelegates \]

### getSensorDelegate() as Sensor.SensorDelegate or Null

### getServiceDelegate() as \[ System.ServiceDelegate \]

### getSettingsView() as \[ WatchUi.Views \] or \[ WatchUi.Views, WatchUi.InputDelegates \] or Null

### getSyncDelegate() as Communications.SyncDelegate or Null

### getTrialDaysRemaining() as Lang.Number or Null

### isActive() as Lang.Boolean

### isTrial() as Lang.Boolean

### loadProperties() as Void

**This has been deprecated**

This method may be removed after System 4.

### onActive(state as Lang.Dictionary or Null) as Void

### onAppInstall() as Void

### onAppUpdate() as Void

### onAuthenticationRequest() as Void

### onBackgroundData(data as Application.PersistableType) as Void

### onDeviceSettingChanged(aSymbol as Lang.Symbol, aValue as Lang.Object) as Void

### onDisplayModeChanged() as Void

### onEnhancedReadabilityModeChanged() as Void

### onInactive(state as Lang.Dictionary or Null) as Void

### onNightModeChanged() as Void

### onSettingsChanged() as Void

### onStart(state as Lang.Dictionary or Null) as Void

Note:

the suspension state can be cleared in the event of reboot or app update.

### onStop(state as Lang.Dictionary or Null) as Void

Note:

the suspension state can be cleared in the event of reboot or app update.

### onStorageChanged() as Void

### onValidateProperty(key as Lang.String, value as Properties.ValueType) as Lang.Boolean or Lang.String

### openAppSettingsEditor() as Void

### saveProperties() as Void

**This has been deprecated**

This method may be removed after System 4.

### setProperty(key as Application.PropertyKeyType, value as Application.PropertyValueType) as Void

**This has been deprecated**

This method may be removed after System 4.

Note:

Background processes cannot save properties.

Note:

Symbols can change from build to build and are not to be used for for Keys or Values.
