---
title: Toybox.Notifications
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html
---

## Module: Toybox.Notifications

## Overview

## Classes Under Namespace

**Classes:** [NotificationMessage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications/NotificationMessage.html)

## Constant Summary

### NotificationMessageType

Notification message types

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| NOTIFICATION\_MESSAGE\_TYPE\_DISMISSED | 1 | API Level 5.1.0 | The notification was dismissed by the user |
| NOTIFICATION\_MESSAGE\_TYPE\_SELECTED | 2 | API Level 5.1.0 | The notification action was selected by the user |

## Typedef Summary

- [**Action**](#Action-named_type "Action (Named Type)") as {:label as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html),:data as [Notifications.NotificationDataType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#NotificationDataType-named_type) }
	A notification action.
- [**NotificationDataKeyType**](#NotificationDataKeyType-named_type "NotificationDataKeyType (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)
- [**NotificationDataType**](#NotificationDataType-named_type "NotificationDataType (Named Type)") as [Notifications.NotificationDataKeyType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#NotificationDataKeyType-named_type) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Notifications.NotificationDataType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#NotificationDataType-named_type) > or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Notifications.NotificationDataKeyType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#NotificationDataKeyType-named_type), [Notifications.NotificationDataType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#NotificationDataType-named_type) > or **Null**
- [**NotificationMessageCallback**](#NotificationMessageCallback-named_type "NotificationMessageCallback (Named Type)") as [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html) (message as [Notifications.NotificationMessage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications/NotificationMessage.html)) as **Void**
- [**ShowNotificationOptions**](#ShowNotificationOptions-named_type "ShowNotificationOptions (Named Type)") as {:icon as [WatchUi.BitmapResource](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/BitmapResource.html) or [Graphics.BitmapReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Graphics/BitmapReference.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:body as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html),:data as [Notifications.NotificationDataType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#NotificationDataType-named_type),:actions as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Notifications.Action](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#Action-named_type) >,:dismissPrevious as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) }
	Notification options.

## Instance Method Summary

- [**registerForNotificationMessages**](#registerForNotificationMessages-instance_function "registerForNotificationMessages (Instance Function)") (callback as [Notifications.NotificationMessageCallback](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#NotificationMessageCallback-named_type) or **Null**) as **Void**
- [**showNotification**](#showNotification-instance_function "showNotification (Instance Function)") (title as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), subTitle as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), options as [Notifications.ShowNotificationOptions](https://developer.garmin.com/connect-iq/api-docs/Toybox/Notifications.html#ShowNotificationOptions-named_type) or **Null**) as **Void**
	Push a notification to the display.
