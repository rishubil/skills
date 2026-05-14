---
title: Toybox.Notifications
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html
---

## Module: Toybox.Notifications

## Overview

## Classes Under Namespace

**Classes:** [NotificationMessage](Notifications/NotificationMessage.md)

## Constant Summary

### NotificationMessageType

Notification message types

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| NOTIFICATION\_MESSAGE\_TYPE\_DISMISSED | 1 | API Level 5.1.0 | The notification was dismissed by the user |
| NOTIFICATION\_MESSAGE\_TYPE\_SELECTED | 2 | API Level 5.1.0 | The notification action was selected by the user |

## Typedef Summary

- [**Action**](#Action-named_type "Action (Named Type)") as {:label as [Lang.String](Lang/String.md),:data as [Notifications.NotificationDataType](Notifications.md#NotificationDataType-named_type) }
	A notification action.
- [**NotificationDataKeyType**](#NotificationDataKeyType-named_type "NotificationDataKeyType (Named Type)") as [Lang.Number](Lang/Number.md) or [Lang.Float](Lang/Float.md) or [Lang.Long](Lang/Long.md) or [Lang.Double](Lang/Double.md) or [Lang.String](Lang/String.md) or [Lang.Boolean](Lang/Boolean.md) or [Lang.Char](Lang/Char.md)
- [**NotificationDataType**](#NotificationDataType-named_type "NotificationDataType (Named Type)") as [Notifications.NotificationDataKeyType](Notifications.md#NotificationDataKeyType-named_type) or [Lang.Array](Lang/Array.md) < [Notifications.NotificationDataType](Notifications.md#NotificationDataType-named_type) > or [Lang.Dictionary](Lang/Dictionary.md) < [Notifications.NotificationDataKeyType](Notifications.md#NotificationDataKeyType-named_type), [Notifications.NotificationDataType](Notifications.md#NotificationDataType-named_type) > or **Null**
- [**NotificationMessageCallback**](#NotificationMessageCallback-named_type "NotificationMessageCallback (Named Type)") as [Lang.Method](Lang/Method.md) (message as [Notifications.NotificationMessage](Notifications/NotificationMessage.md)) as **Void**
- [**ShowNotificationOptions**](#ShowNotificationOptions-named_type "ShowNotificationOptions (Named Type)") as {:icon as [WatchUi.BitmapResource](WatchUi/BitmapResource.md) or [Graphics.BitmapReference](Graphics/BitmapReference.md) or [Lang.ResourceId](Lang/ResourceId.md),:body as [Lang.String](Lang/String.md) or [Lang.ResourceId](Lang/ResourceId.md),:data as [Notifications.NotificationDataType](Notifications.md#NotificationDataType-named_type),:actions as [Lang.Array](Lang/Array.md) < [Notifications.Action](Notifications.md#Action-named_type) >,:dismissPrevious as [Lang.Boolean](Lang/Boolean.md) }
	Notification options.

## Instance Method Summary

- [**registerForNotificationMessages**](#registerForNotificationMessages-instance_function "registerForNotificationMessages (Instance Function)") (callback as [Notifications.NotificationMessageCallback](Notifications.md#NotificationMessageCallback-named_type) or **Null**) as **Void**
- [**showNotification**](#showNotification-instance_function "showNotification (Instance Function)") (title as [Lang.String](Lang/String.md) or [Lang.ResourceId](Lang/ResourceId.md), subTitle as [Lang.String](Lang/String.md) or [Lang.ResourceId](Lang/ResourceId.md), options as [Notifications.ShowNotificationOptions](Notifications.md#ShowNotificationOptions-named_type) or **Null**) as **Void**
	Push a notification to the display.
