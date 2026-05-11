---
title: Toybox.Application.AudioContentProviderApp
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Application/AudioContentProviderApp.html
---

## Class: Toybox.Application.AudioContentProviderApp

## Overview

## Instance Method Summary

- [**getContentDelegate**](#getContentDelegate-instance_function "getContentDelegate (Instance Function)") (args as [Application.PersistableType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Application.html#PersistableType-named_type)) as [Media.ContentDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/ContentDelegate.html)
	Get a [ContentDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/ContentDelegate.html) for use by the system to get and iterate through media content on the device.
- [**getPlaybackConfigurationView**](#getPlaybackConfigurationView-instance_function "getPlaybackConfigurationView (Instance Function)") () as \[ [WatchUi.Views](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Views-named_type) \] or \[ [WatchUi.Views](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Views-named_type), [WatchUi.InputDelegates](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#InputDelegates-named_type) \]
	Override to provide the initial View and Input Delegate for configuring playback.
- [**getProviderIconInfo**](#getProviderIconInfo-instance_function "getProviderIconInfo (Instance Function)") () as [Media.ProviderIconInfo](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/ProviderIconInfo.html) or **Null**
	Get audio provider icon information.
- [**getSyncConfigurationView**](#getSyncConfigurationView-instance_function "getSyncConfigurationView (Instance Function)") () as \[ [WatchUi.Views](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Views-named_type) \] or \[ [WatchUi.Views](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#Views-named_type), [WatchUi.InputDelegates](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi.html#InputDelegates-named_type) \]
	Override to provide the initial View and Input Delegate for configuring sync.
- [**getSyncDelegate**](#getSyncDelegate-instance_function "getSyncDelegate (Instance Function)") () as [Communications.SyncDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/SyncDelegate.html) or **Null** deprecated
	Get a [SyncDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/SyncDelegate.html) object that communicates sync status to the system for syncing media content to the device.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.

## Instance Method Details

### getContentDelegate(args as Application.PersistableType) as Media.ContentDelegate

Note:

This method must be overridden in derived classes. If called, this function will cause the application to crash.

### getPlaybackConfigurationView() as \[ WatchUi.Views \] or \[ WatchUi.Views, WatchUi.InputDelegates \]

Note:

This method must be overridden in derived classes. If called, this function will cause the application to crash.

### getProviderIconInfo() as Media.ProviderIconInfo or Null

### getSyncConfigurationView() as \[ WatchUi.Views \] or \[ WatchUi.Views, WatchUi.InputDelegates \]

Note:

This method must be overridden in derived classes. If called, this function will cause the application to crash.

### getSyncDelegate() as Communications.SyncDelegate or Null

**This has been deprecated**

This method may be removed after System 9.
