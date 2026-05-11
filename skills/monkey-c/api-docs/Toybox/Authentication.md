---
title: Toybox.Authentication
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication.html
---

## Module: Toybox.Authentication

## Overview

## Classes Under Namespace

**Classes:** [Message](Authentication/Message.md), [OAuthMessage](Authentication/OAuthMessage.md)

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

- [**makeOAuthRequest**](#makeOAuthRequest-instance_function "makeOAuthRequest (Instance Function)") (requestUrl as [Lang.String](Lang/String.md), requestParams as [Lang.Dictionary](Lang/Dictionary.md) < [Lang.String](Lang/String.md), [Lang.String](Lang/String.md) >, resultUrl as [Lang.String](Lang/String.md), resultType as [Authentication.OAuthResultType](Authentication.md#OAuthResultType-module), resultKeys as [Lang.Dictionary](Lang/Dictionary.md) < [Lang.String](Lang/String.md), [Lang.String](Lang/String.md) >) as **Void**
	Request an OAuth sign-in through Garmin Connect IQ Mobile App A notification will trigger on the phone, that when clicked, provides a web view that shows `requestUrl`.
- [**registerForOAuthMessages**](#registerForOAuthMessages-instance_function "registerForOAuthMessages (Instance Function)") (method as [Lang.Method](Lang/Method.md) (message as [Authentication.OAuthMessage](Authentication/OAuthMessage.md)) as **Void**) as **Void**
