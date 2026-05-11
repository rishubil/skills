---
title: Toybox.Notifications.NotificationMessage
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications/NotificationMessage.html
---

## Class: Toybox.Notifications.NotificationMessage

## Overview

A NotificationMessage is received by the callback registered in [registerForNotificationMessages()](../Notifications.md#registerForNotificationMessages-instance_function).

## Instance Member Summary

- [**action**](#action-var "action (Var)") as [Notifications.NotificationDataType](../Notifications.md#NotificationDataType-named_type) or **Null**
	The action payload associated with the selected action The value of the selected action from the `:actions` option provided to [showNotification()](../Notifications.md#showNotification-instance_function).
- [**data**](#data-var "data (Var)") as [Notifications.NotificationDataType](../Notifications.md#NotificationDataType-named_type) or **Null**
	The data payload associated with the notification The value of the `:data` option provided to [showNotification()](../Notifications.md#showNotification-instance_function).
- [**type**](#type-var "type (Var)") as [Notifications.NotificationMessageType](../Notifications.md#NotificationMessageType-module)
	The notification message type.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.

## Instance Attribute Details

### var action as Notifications.NotificationDataType or Null

The action payload associated with the selected action

The value of the selected action from the `:actions` option provided to [showNotification()](../Notifications.md#showNotification-instance_function). This will be `null` if the selected action had a `null` value, or if the notification was dismissed.

### var data as Notifications.NotificationDataType or Null

The data payload associated with the notification

The value of the `:data` option provided to [showNotification()](../Notifications.md#showNotification-instance_function). This will be `null` if no value was provided or it was `null`.

### var type as Notifications.NotificationMessageType

The notification message type

## Instance Method Details

### initialize()

Constructor
