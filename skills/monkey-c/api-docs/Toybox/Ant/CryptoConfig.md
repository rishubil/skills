---
title: Toybox.Ant.CryptoConfig
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/CryptoConfig.html
---

## Class: Toybox.Ant.CryptoConfig

## Overview

## See Also:

- [ANT Downloads & Resources - ANT Message Protocol](https://www.thisisant.com/developer/resources/downloads/)

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | DEFAULT\_ENCRYPTION\_ID | 0 | API Level 2.3.0 |  |
| Type | DEFAULT\_USER\_INFO\_STRING | 0 | API Level 2.3.0 |  |
| Type | ENCRYPTION\_KEY\_LENGTH | 16 | API Level 2.3.0 |  |
| Type | USER\_INFO\_STRING\_LENGTH | 19 | API Level 2.3.0 |  |

## Typedef Summary

- [**EncryptionKey**](#EncryptionKey-named_type "EncryptionKey (Named Type)") as \[ [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) \]
- [**UserInfoString**](#UserInfoString-named_type "UserInfoString (Named Type)") as \[ [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) \]

## Instance Member Summary

- [**decimationRate**](#decimationRate-var "decimationRate (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The division factor of the encryption counter.
- [**encryptionId**](#encryptionId-var "encryptionId (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	The unique 4 byte identifier of the encrypted master or the negotiating slave.
- [**encryptionKey**](#encryptionKey-var "encryptionKey (Var)") as [CryptoConfig.EncryptionKey](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/CryptoConfig.html#EncryptionKey-named_type)
	The 128-bit encryption key used to encrypt/decrypt ANT packets.
- [**userInfoString**](#userInfoString-var "userInfoString (Var)") as [CryptoConfig.UserInfoString](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/CryptoConfig.html#UserInfoString-named_type) or **Null**
	The (optional) user information String to be sent to the master channel on successful negotiation of encryption (Slave channels only).

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:encryptionId as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:encryptionKey as [CryptoConfig.EncryptionKey](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/CryptoConfig.html#EncryptionKey-named_type),:userInfoString as [CryptoConfig.UserInfoString](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/CryptoConfig.html#UserInfoString-named_type),:decimationRate as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) })
	Constructor.
