---
title: Toybox.Communications.SyncDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/SyncDelegate.html
---

## Class: Toybox.Communications.SyncDelegate

## Overview

A delegate object that the user implements to respond to sync requests from the system.

## Instance Method Summary

- [**isSyncNeeded**](#isSyncNeeded-instance_function "isSyncNeeded (Instance Function)") () as [Lang.Boolean](../Lang/Boolean.md)
	Check if a sync is needed.
- [**onStartSync**](#onStartSync-instance_function "onStartSync (Instance Function)") () as **Void**
	Called when a sync is started by the system.
- [**onStopSync**](#onStopSync-instance_function "onStopSync (Instance Function)") () as **Void**
	Called when an active sync is cancelled.

## Instance Method Details

### isSyncNeeded() as Lang.Boolean

Check if a sync is needed.

### onStartSync() as Void

Called when a sync is started by the system.

This method should be used to kick-off the application sync process. This includes any setup required to fetch the data needed to prepare the sync, as well as the initial call to [makeWebRequest()](../Communications.md#makeWebRequest-instance_function) to download the first piece of content. Note that, when using this method, you must chain your makeWebRequest() calls together manually. Additionally, you must call [notifySyncProgress()](../Communications.md#notifySyncProgress-instance_function) intermittently to enable sync progress updates to be displayed in the native user interface for the device. Finally, [notifySyncComplete()](../Communications.md#notifySyncComplete-instance_function) must be called either when the sync has successfully completed, or if an error occurs, so that the device can be properly notified that the sync process is finished.

### onStopSync() as Void

Called when an active sync is cancelled.

This method will be called when an active sync is being cancelled by the user. The app is responsible for calling the [cancelAllRequests()](../Communications.md#cancelAllRequests-instance_function) to cancel any requests made for a sync process. The app is also responsible to let the system know that sync has successfully been cancelled by calling [notifySyncComplete()](../Communications.md#notifySyncComplete-instance_function).
