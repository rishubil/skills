---
title: Toybox.Authentication
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication.html
---

## Module: Toybox.Authentication

## Overview

## Classes Under Namespace

**Classes:** [Message](https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication/Message.html), [OAuthMessage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication/OAuthMessage.html)

## Constant Summary

### OAuthResultType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| OAUTH\_RESULT\_TYPE\_URL | 0 | API Level 3.3.0 | How the OAuth token will be returned in the final step. |

### OAuthSigningMethod

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| OAUTH\_SIGNING\_METHOD\_HMAC\_SHA1 | 0 | API Level 3.3.0 | How the OAuth request will be signed |

## Instance Method Summary

- [**makeOAuthRequest**](#makeOAuthRequest-instance_function "makeOAuthRequest (Instance Function)") (requestUrl as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), requestParams as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) >, resultUrl as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), resultType as [Authentication.OAuthResultType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication.html#OAuthResultType-module), resultKeys as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) >) as **Void**
	Request an OAuth sign-in through Garmin Connect IQ Mobile App A notification will trigger on the phone, that when clicked, provides a web view that shows `requestUrl`.
- [**registerForOAuthMessages**](#registerForOAuthMessages-instance_function "registerForOAuthMessages (Instance Function)") (method as [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html) (message as [Authentication.OAuthMessage](https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication/OAuthMessage.html)) as **Void**) as **Void**
