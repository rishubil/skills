---
title: Toybox.Communications
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications.html
---

## Module: Toybox.Communications

## Overview

Note:

This module was made available to foreground data fields with API 5.0.0

## Classes Under Namespace

**Classes:** [ConnectionListener](Communications/ConnectionListener.md), [MailboxIterator](Communications/MailboxIterator.md), [Message](Communications/Message.md), [OAuthMessage](Communications/OAuthMessage.md), [PhoneAppMessage](Communications/PhoneAppMessage.md), [SyncDelegate](Communications/SyncDelegate.md)

## Constant Summary

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BLE\_HOST\_TIMEOUT | \-2 | API Level 1.0.0 | We timed out waiting for a response from the host. |
| BLE\_SERVER\_TIMEOUT | \-3 | API Level 1.0.0 | We timed out waiting for a response from a server. |
| BLE\_NO\_DATA | \-4 | API Level 1.0.0 | Response contained no data. |
| BLE\_REQUEST\_CANCELLED | \-5 | API Level 1.0.0 | The request was cancelled at the request of the system. |
| BLE\_QUEUE\_FULL | \-101 | API Level 1.0.0 | Too many requests have been made. |
| BLE\_REQUEST\_TOO\_LARGE | \-102 | API Level 1.0.0 | Serialized input data for the request was too large. |
| BLE\_CONNECTION\_UNAVAILABLE | \-104 | API Level 1.0.0 | No BLE connection is available. |
| INVALID\_HTTP\_HEADER\_FIELDS\_IN\_REQUEST | \-200 | API Level 1.0.0 | Request contained invalid http header fields. |
| INVALID\_HTTP\_BODY\_IN\_REQUEST | \-201 | API Level 1.0.0 | Request contained an invalid http body. |
| INVALID\_HTTP\_METHOD\_IN\_REQUEST | \-202 | API Level 1.0.0 | Request used an invalid http method. |
| NETWORK\_REQUEST\_TIMED\_OUT | \-300 | API Level 1.0.0 | Request timed out before a response was received. |
| INVALID\_HTTP\_BODY\_IN\_NETWORK\_RESPONSE | \-400 | API Level 1.0.0 | Response body data is invalid for the request type. |
| INVALID\_HTTP\_HEADER\_FIELDS\_IN\_NETWORK\_RESPONSE | \-401 | API Level 1.0.0 | Response contained invalid http header fields. |
| NETWORK\_RESPONSE\_TOO\_LARGE | \-402 | API Level 1.0.0 | Serialized response was too large. |
| NETWORK\_RESPONSE\_OUT\_OF\_MEMORY | \-403 | API Level 3.0.0 | Ran out of memory processing network response. |
| STORAGE\_FULL | \-1000 | API Level 2.2.0 | Filesystem too full to store response data. |
| SECURE\_CONNECTION\_REQUIRED | \-1001 | API Level 2.3.0 | Indicates an https connection is required for the request. |
| UNSUPPORTED\_CONTENT\_TYPE\_IN\_RESPONSE | \-1002 | API Level 2.4.1 | Content type given in response is not supported or does not match what is expected. |
| REQUEST\_CANCELLED | \-1003 | API Level 2.4.2 | Http request was cancelled by the system. |
| REQUEST\_CONNECTION\_DROPPED | \-1004 | API Level 3.0.0 | Connection was lost before a response could be obtained. |
| UNABLE\_TO\_PROCESS\_MEDIA | \-1005 | API Level 3.0.2 | Downloaded media file was unable to be read. |
| UNABLE\_TO\_PROCESS\_IMAGE | \-1006 | API Level 3.0.3 | Downloaded image file was unable to be processed. |
| UNABLE\_TO\_PROCESS\_HLS | \-1007 | API Level 3.0.10 | HLS content could not be downloaded. Most often occurs when requested and provided bit rates do not match. |

### TokenResult

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| OAUTH\_RESULT\_TYPE\_URL | 0 | API Level 1.3.0 | How the OAuth token will be returned in the final step. |

### SigningMethod

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| OAUTH\_SIGNING\_METHOD\_HMAC\_SHA1 | 0 | API Level 1.3.0 | How the OAuth request will be signed |

### HttpRequestMethod

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| HTTP\_REQUEST\_METHOD\_GET | 1 | API Level 1.2.0 | Specifies a request be executed using the GET method. |
| HTTP\_REQUEST\_METHOD\_PUT | 2 | API Level 1.2.0 | Specifies a request be executed using the PUT method. |
| HTTP\_REQUEST\_METHOD\_POST | 3 | API Level 1.2.0 | Specifies a request be executed using the POST method. |
| HTTP\_REQUEST\_METHOD\_DELETE | 4 | API Level 1.2.0 | Specifies a request be executed using the DELETE method. |

### HttpResponseContentType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_JSON | 0 | API Level 1.3.0 | Content type specifier for response is expected to be a json type. Content type string must be "application/json". |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_URL\_ENCODED | 1 | API Level 1.3.0 | Content type specifier for response is expected to indicate url encoding. Content type string must be "application/x-www-form-urlencoded". |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_GPX | 2 | API Level 2.2.0 | Content type specifier for response is expected to be a gpx type. |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_FIT | 3 | API Level 2.2.0 | Content type specifier for response is expected to be a FIT type. |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_AUDIO | 4 | API Level 3.0.0 | Content type specifier for response is expected to be an audio type. Content type string must be of the "audio/\*" format. |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_TEXT\_PLAIN | 5 | API Level 3.0.0 | Content type specifier for response is expected to be plain text type. Content type string must be "text/plain" |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_HLS\_DOWNLOAD | 6 | API Level 3.0.10 | Content type specifier for response is expected to be an HLS data type. Content type string must be either "application/vnd.apple.mpegurl" or "audio/mpegurl". |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_ANIMATION\_MANIFEST | 7 | API Level 3.1.0 | Content type specifier for response is expected to be a CIQ animation manifest data type. Content type string must be "application/vnd.garmin.connectiq.animation.manifest". |
| HTTP\_RESPONSE\_CONTENT\_TYPE\_ANIMATION | 8 | API Level 3.1.0 | Content type specifier for response is expected to be a CIQ animation data type. Content type string must be "image/vnd.garmin.connectiq.animation". |

### WifiConnectionStatus

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| WIFI\_CONNECTION\_STATUS\_LOW\_BATTERY | 1 | API Level 3.2.0 | Specifies an error condition, battery is too low to start a WIFI connection. |
| WIFI\_CONNECTION\_STATUS\_NO\_ACCESS\_POINTS | 2 | API Level 3.2.0 | Specifies an error condition, no access-point is stored on the device. |
| WIFI\_CONNECTION\_STATUS\_UNSUPPORTED | 3 | API Level 3.2.0 | Specifies an error condition, WIFI is not supported on current device. |
| WIFI\_CONNECTION\_STATUS\_USER\_DISABLED | 4 | API Level 3.2.0 | Specifies an error condition, WIFI is disabled by user. |
| WIFI\_CONNECTION\_STATUS\_BATTERY\_SAVER\_ACTIVE | 5 | API Level 3.2.0 | Specifies an error condition, WIFI is disabled by battery saver. |
| WIFI\_CONNECTION\_STATUS\_STEALTH\_MODE\_ACTIVE | 6 | API Level 3.2.0 | Specifies an error condition, WIFI is disabled by stealth mode. |
| WIFI\_CONNECTION\_STATUS\_AIRPLANE\_MODE\_ACTIVE | 7 | API Level 3.2.0 | Specifies an error condition, WIFI is disabled by airplane mode. |
| WIFI\_CONNECTION\_STATUS\_POWERED\_DOWN | 8 | API Level 3.2.0 | Specifies an error condition, WIFI is disabled by the device. |
| WIFI\_CONNECTION\_STATUS\_UNKNOWN | 9 | API Level 3.2.0 | Specifies an error condition, WIFI is not usable but status is unknown. |
| WIFI\_CONNECTION\_STATUS\_CANNOT\_CONNECT\_TO\_ACCESS\_POINT | 10 | API Level 3.3.0 | Specifies an error condition, WIFI can not connect to saved AccessPoint. |
| WIFI\_CONNECTION\_STATUS\_TRANSFER\_ALREADY\_IN\_PROGRESS | 11 | API Level 3.3.0 | Specifies an error condition, WIFI transfer already in progress |

### HttpRequestContentType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| REQUEST\_CONTENT\_TYPE\_URL\_ENCODED | 0 | API Level 1.2.0 | Specifies a content type of application/x-www-form-urlencoded |
| REQUEST\_CONTENT\_TYPE\_JSON | 1 | API Level 1.2.0 | Specifies a content type of application/json |

### PackingFormat

Image packing format used for image request.

The packing format describes the encoding a requested image should use when being transmitted. The encoding used affects the transfer size, decoding time, and image quality.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| PACKING\_FORMAT\_DEFAULT | 0 | API Level 4.2.0 | Image data is encoded in the device native format, a lossless encoding that available on all devices. It is very efficient to decode, but often results in large transfer sizes so is slow to download. |
| PACKING\_FORMAT\_YUV | 1 | API Level 4.2.0 | Image data is encoded in YUV format. This is a lossy encoding that is compressed, and is fast to load. It is ideal for photographic imagery with transparency. |
| PACKING\_FORMAT\_PNG | 2 | API Level 4.2.0 | Image data is encoded in PNG format. This is a lossless encoding that is compressed, but is relatively slow to load. It is ideal for non-photographic imagery. |
| PACKING\_FORMAT\_JPG | 3 | API Level 4.2.0 | Image data is encoded in JPG format. This is a lossy encoding that is compressed, and is reasonably fast to load. It is ideal for photographic imagery. |

### HlsBandwidth

TVM will select the HLS audio stream with the highest bandwidth that's less than or equal to the maximum

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| HLS\_AUDIO\_BANDWIDTH\_48K | 49152 | API Level 3.0.10 |  |
| HLS\_AUDIO\_BANDWIDTH\_128K | 131072 | API Level 3.0.10 |  |
| HLS\_AUDIO\_BANDWIDTH\_256K | 262144 | API Level 3.0.10 |  |

### Dithering

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| IMAGE\_DITHERING\_NONE | 1 | API Level 1.2.0 | Do not apply dithering to an image. |
| IMAGE\_DITHERING\_FLOYD\_STEINBERG | 2 | API Level 1.2.0 | Apply Floyd-Steinberg dithering to an image. |

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| PHONE\_APP\_MESSAGE\_ERROR\_OUT\_OF\_MEMORY | 0 | API Level 6.0.0 |  |
| PHONE\_APP\_MESSAGE\_ERROR\_OUT\_OF\_STORAGE | 1 | API Level 6.0.0 |  |

## Typedef Summary

- [**PhoneMessageCallback**](#PhoneMessageCallback-named_type "PhoneMessageCallback (Named Type)") as [Lang.Method](Lang/Method.md) (msg as [Communications.PhoneAppMessage](Communications/PhoneAppMessage.md)) as **Void**
- [**PhoneMessageErrorCallback**](#PhoneMessageErrorCallback-named_type "PhoneMessageErrorCallback (Named Type)") as [Lang.Method](Lang/Method.md) (error as [Communications.PhoneAppMessageError](Communications.md#PhoneAppMessageError-module)) as **Void**
- [**TransmitKeyType**](#TransmitKeyType-named_type "TransmitKeyType (Named Type)") as [Lang.Number](Lang/Number.md) or [Lang.Float](Lang/Float.md) or [Lang.Long](Lang/Long.md) or [Lang.Double](Lang/Double.md) or [Lang.String](Lang/String.md) or [Lang.Boolean](Lang/Boolean.md) or [Lang.Char](Lang/Char.md)
- [**TransmitType**](#TransmitType-named_type "TransmitType (Named Type)") as [Communications.TransmitKeyType](Communications.md#TransmitKeyType-named_type) or [Lang.ByteArray](Lang/ByteArray.md) or [Lang.Array](Lang/Array.md) < [Communications.TransmitType](Communications.md#TransmitType-named_type) > or [Lang.Dictionary](Lang/Dictionary.md) < [Communications.TransmitKeyType](Communications.md#TransmitKeyType-named_type), [Communications.TransmitType](Communications.md#TransmitType-named_type) > or **Null**

## Instance Method Summary

- [**cancelAllRequests**](#cancelAllRequests-instance_function "cancelAllRequests (Instance Function)") () as **Void**
	Cancel all pending JSON and Image requests.
- [**checkWifiConnection**](#checkWifiConnection-instance_function "checkWifiConnection (Instance Function)") (connectionStatusCallback as [Lang.Method](Lang/Method.md) (result as {:wifiAvailable as [Lang.Boolean](Lang/Boolean.md),:errorCode as [Communications.WifiConnectionStatus](Communications.md#WifiConnectionStatus-module) }) as **Void**) as **Void**
	Checks if an internet-enabled WIFI access point is visible and can be connected to.
- [**emptyMailbox**](#emptyMailbox-instance_function "emptyMailbox (Instance Function)") () as **Void** deprecated
	Clear the contents of the mailbox.
- [**encodeURL**](#encodeURL-instance_function "encodeURL (Instance Function)") (url as [Lang.String](Lang/String.md)) as [Lang.String](Lang/String.md)
	Convert a URL String into a percent-encoded string.
- [**generateSignedOAuthHeader**](#generateSignedOAuthHeader-instance_function "generateSignedOAuthHeader (Instance Function)") (url as [Lang.String](Lang/String.md), params as [Lang.Dictionary](Lang/Dictionary.md) < [Lang.String](Lang/String.md), [Lang.Object](Lang/Object.md) >, requestMethod as [Communications.HttpRequestMethod](Communications.md#HttpRequestMethod-module), signatureMethod as [Communications.SigningMethod](Communications.md#SigningMethod-module), token as [Lang.String](Lang/String.md) or **Null**, tokenSecret as [Lang.String](Lang/String.md), consumerKey as [Lang.String](Lang/String.md), consumerSecret as [Lang.String](Lang/String.md)) as [Lang.String](Lang/String.md) deprecated
	Generate the value for the "Authorization" header in an OAuth 1.0a request.
- [**getMailbox**](#getMailbox-instance_function "getMailbox (Instance Function)") () as [Communications.MailboxIterator](Communications/MailboxIterator.md) deprecated
	Get the MailboxIterator for this Application's mailbox.
- [**makeImageRequest**](#makeImageRequest-instance_function "makeImageRequest (Instance Function)") (url as [Lang.String](Lang/String.md), parameters as [Lang.Dictionary](Lang/Dictionary.md) or **Null**, options as {:palette as [Lang.Array](Lang/Array.md) < [Lang.Number](Lang/Number.md) >,:maxWidth as [Lang.Number](Lang/Number.md),:maxHeight as [Lang.Number](Lang/Number.md),:dithering as [Communications.Dithering](Communications.md#Dithering-module),:packingFormat as [Communications.PackingFormat](Communications.md#PackingFormat-module) }, responseCallback as [Lang.Method](Lang/Method.md) (responseCode as [Lang.Number](Lang/Number.md), data as [WatchUi.BitmapResource](WatchUi/BitmapResource.md) or [Graphics.BitmapReference](Graphics/BitmapReference.md) or **Null**) as **Void**) as **Void**
	Initiate an image download request.
- [**makeJsonRequest**](#makeJsonRequest-instance_function "makeJsonRequest (Instance Function)") (url as [Lang.String](Lang/String.md), parameters as [Lang.Dictionary](Lang/Dictionary.md) < [Lang.Object](Lang/Object.md), [Lang.Object](Lang/Object.md) > or **Null**, options as {:method as [Communications.HttpRequestMethod](Communications.md#HttpRequestMethod-module),:headers as [Lang.Dictionary](Lang/Dictionary.md) } or **Null**, responseCallback as [Lang.Method](Lang/Method.md) (responseCode as [Lang.Number](Lang/Number.md), data as [Lang.Dictionary](Lang/Dictionary.md) or [Lang.String](Lang/String.md) or [PersistedContent.Iterator](PersistedContent/Iterator.md) or **Null**) as **Void**) as **Void** deprecated
	Initiate a download request.
- [**makeOAuthRequest**](#makeOAuthRequest-instance_function "makeOAuthRequest (Instance Function)") (requestUrl as [Lang.String](Lang/String.md), requestParams as [Lang.Dictionary](Lang/Dictionary.md), resultUrl as [Lang.String](Lang/String.md), resultType as [Communications.TokenResult](Communications.md#TokenResult-module), resultKeys as [Lang.Dictionary](Lang/Dictionary.md) < [Lang.String](Lang/String.md), [Lang.String](Lang/String.md) >) as **Void**
	Request an OAuth sign-in through Garmin Connect Mobile.
- [**makeWebRequest**](#makeWebRequest-instance_function "makeWebRequest (Instance Function)") (url as [Lang.String](Lang/String.md), parameters as [Lang.Dictionary](Lang/Dictionary.md) < [Lang.Object](Lang/Object.md), [Lang.Object](Lang/Object.md) > or **Null**, options as {:method as [Communications.HttpRequestMethod](Communications.md#HttpRequestMethod-module),:headers as [Lang.Dictionary](Lang/Dictionary.md),:responseType as [Communications.HttpResponseContentType](Communications.md#HttpResponseContentType-module),:context as [Lang.Object](Lang/Object.md) or **Null**,:maxBandwidth as [Lang.Number](Lang/Number.md),:fileDownloadProgressCallback as [Lang.Method](Lang/Method.md) (totalBytesTransferred as [Lang.Number](Lang/Number.md), fileSize as [Lang.Number](Lang/Number.md) or **Null**) as **Void** } or **Null**, responseCallback as [Lang.Method](Lang/Method.md) (responseCode as [Lang.Number](Lang/Number.md), data as [Lang.Dictionary](Lang/Dictionary.md) or [Lang.String](Lang/String.md) or [PersistedContent.Iterator](PersistedContent/Iterator.md) or **Null**) as **Void** or [Lang.Method](Lang/Method.md) (responseCode as [Lang.Number](Lang/Number.md), data as [Lang.Dictionary](Lang/Dictionary.md) or [Lang.String](Lang/String.md) or [PersistedContent.Iterator](PersistedContent/Iterator.md) or **Null**, context as [Lang.Object](Lang/Object.md)) as **Void**) as **Void**
	Initiate a download request.
- [**notifySyncComplete**](#notifySyncComplete-instance_function "notifySyncComplete (Instance Function)") (errorMessage as [Lang.String](Lang/String.md) or **Null**) as **Void**
	Send a system notification to indicate that the sync completed.
- [**notifySyncProgress**](#notifySyncProgress-instance_function "notifySyncProgress (Instance Function)") (percentageComplete as [Lang.Number](Lang/Number.md)) as **Void**
	Send a system notification to indicate overall sync progress.
- [**openWebPage**](#openWebPage-instance_function "openWebPage (Instance Function)") (url as [Lang.String](Lang/String.md), params as [Lang.Dictionary](Lang/Dictionary.md) or **Null**, options as [Lang.Dictionary](Lang/Dictionary.md) or **Null**) as **Void**
	Request that GCM issue a phone notification that will open a web page.
- [**registerForOAuthMessages**](#registerForOAuthMessages-instance_function "registerForOAuthMessages (Instance Function)") (method as [Lang.Method](Lang/Method.md) (data as [Communications.OAuthMessage](Communications/OAuthMessage.md)) as **Void**) as **Void**
- [**registerForPhoneAppMessageErrors**](#registerForPhoneAppMessageErrors-instance_function "registerForPhoneAppMessageErrors (Instance Function)") (method as [Communications.PhoneMessageErrorCallback](Communications.md#PhoneMessageErrorCallback-named_type) or **Null**) as **Void**
- [**registerForPhoneAppMessages**](#registerForPhoneAppMessages-instance_function "registerForPhoneAppMessages (Instance Function)") (method as [Communications.PhoneMessageCallback](Communications.md#PhoneMessageCallback-named_type) or **Null**) as **Void**
- [**setMailboxListener**](#setMailboxListener-instance_function "setMailboxListener (Instance Function)") (listener as [Lang.Method](Lang/Method.md) (mailboxIterator as [Communications.MailboxIterator](Communications/MailboxIterator.md)) as **Void**) as **Void** deprecated
	Add a listener for mailbox events.
- [**startSync**](#startSync-instance_function "startSync (Instance Function)") () as **Void**
	Exit the [AppBase](Application/AppBase.md) and launch it in sync mode.
- [**startSync2**](#startSync2-instance_function "startSync2 (Instance Function)") (options as {:message as [Lang.String](Lang/String.md) } or **Null**) as **Void**
	Exit the [AppBase](Application/AppBase.md) and launch it in sync mode with the provided message.
- [**transmit**](#transmit-instance_function "transmit (Instance Function)") (content as [Communications.TransmitType](Communications.md#TransmitType-named_type), options as [Lang.Dictionary](Lang/Dictionary.md) or **Null**, listener as [Communications.ConnectionListener](Communications/ConnectionListener.md)) as **Void**
	Send data across the the BLE link.

## Typedef Details

### PhoneMessageCallback as Lang.Method(msg as Communications.PhoneAppMessage) as Void

### PhoneMessageErrorCallback as Lang.Method(error as Communications.PhoneAppMessageError) as Void

### TransmitKeyType as Lang.Number or Lang.Float or Lang.Long or Lang.Double or Lang.String or Lang.Boolean or Lang.Char

### TransmitType as Communications.TransmitKeyType or Lang.ByteArray or Lang.Array<Communications.TransmitType> or Lang.Dictionary<Communications.TransmitKeyType, Communications.TransmitType> or Null

## Instance Method Details

### cancelAllRequests() as Void

### checkWifiConnection(connectionStatusCallback as Lang.Method(result as {:wifiAvailable as Lang.Boolean,:errorCode as Communications.WifiConnectionStatus }) as Void) as Void

### emptyMailbox() as Void

**This has been deprecated**

This method may be removed after System 4.

### encodeURL(url as Lang.String) as Lang.String

### getMailbox() as Communications.MailboxIterator

**This has been deprecated**

This method may be removed after System 4.

### makeImageRequest(url as Lang.String, parameters as Lang.Dictionary or Null, options as {:palette as Lang.Array<Lang.Number>,:maxWidth as Lang.Number,:maxHeight as Lang.Number,:dithering as Communications.Dithering,:packingFormat as Communications.PackingFormat }, responseCallback as Lang.Method(responseCode as Lang.Number, data as WatchUi.BitmapResource or Graphics.BitmapReference or Null) as Void) as Void

Note:

This method can be used when connected to WiFi or a mobile device over Bluetooth.

### makeJsonRequest(url as Lang.String, parameters as Lang.Dictionary<Lang.Object, Lang.Object> or Null, options as {:method as Communications.HttpRequestMethod,:headers as Lang.Dictionary } or Null, responseCallback as Lang.Method(responseCode as Lang.Number, data as Lang.Dictionary or Lang.String or PersistedContent.Iterator or Null) as Void) as Void

**This has been deprecated**

This method may be removed after System 4.

Note:

This method can be used when connected to WiFi or a mobile device over Bluetooth.

### makeOAuthRequest(requestUrl as Lang.String, requestParams as Lang.Dictionary, resultUrl as Lang.String, resultType as Communications.TokenResult, resultKeys as Lang.Dictionary<Lang.String, Lang.String>) as Void

Note:

This method can only be used when connected to a mobile device over Bluetooth.

### makeWebRequest(url as Lang.String, parameters as Lang.Dictionary<Lang.Object, Lang.Object> or Null, options as {:method as Communications.HttpRequestMethod,:headers as Lang.Dictionary,:responseType as Communications.HttpResponseContentType,:context as Lang.Object or Null,:maxBandwidth as Lang.Number,:fileDownloadProgressCallback as Lang.Method(totalBytesTransferred as Lang.Number, fileSize as Lang.Number or Null) as Void } or Null, responseCallback as Lang.Method(responseCode as Lang.Number, data as Lang.Dictionary or Lang.String or PersistedContent.Iterator or Null) as Void or Lang.Method(responseCode as Lang.Number, data as Lang.Dictionary or Lang.String or PersistedContent.Iterator or Null, context as Lang.Object) as Void) as Void

Note:

This method can be used when connected to WiFi or a mobile device over Bluetooth.

### notifySyncComplete(errorMessage as Lang.String or Null) as Void

### notifySyncProgress(percentageComplete as Lang.Number) as Void

### openWebPage(url as Lang.String, params as Lang.Dictionary or Null, options as Lang.Dictionary or Null) as Void

Note:

This method can only be used when connected to a mobile device over Bluetooth.

### registerForOAuthMessages(method as Lang.Method(data as Communications.OAuthMessage) as Void) as Void

### registerForPhoneAppMessageErrors(method as Communications.PhoneMessageErrorCallback or Null) as Void

### registerForPhoneAppMessages(method as Communications.PhoneMessageCallback or Null) as Void

### setMailboxListener(listener as Lang.Method(mailboxIterator as Communications.MailboxIterator) as Void) as Void

**This has been deprecated**

This method may be removed after System 4.
