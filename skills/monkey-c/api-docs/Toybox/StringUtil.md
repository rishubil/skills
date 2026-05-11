---
title: Toybox.StringUtil
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/StringUtil.html
---

## Module: Toybox.StringUtil

## Overview

## Classes Under Namespace

**Classes:** [InvalidHexStringException](https://developer.garmin.com/connect-iq/api-docs/Toybox/StringUtil/InvalidHexStringException.html)

## Constant Summary

### CharacterEncoding

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CHAR\_ENCODING\_UTF8 | 0 | API Level 3.0.0 |  |

### Representation

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| REPRESENTATION\_STRING\_BASE64 | 0 | API Level 3.0.0 |  |
| REPRESENTATION\_STRING\_HEX | 1 | API Level 3.0.0 |  |
| REPRESENTATION\_STRING\_PLAIN\_TEXT | 2 | API Level 3.0.0 |  |
| REPRESENTATION\_BYTE\_ARRAY | 3 | API Level 3.0.0 |  |

## Instance Method Summary

- [**charArrayToString**](#charArrayToString-instance_function "charArrayToString (Instance Function)") (charArray as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html) >) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Given an Array of [Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html) objects, return the String equivalent.
- [**convertEncodedString**](#convertEncodedString-instance_function "convertEncodedString (Instance Function)") (input as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html), options as {:fromRepresentation as [StringUtil.Representation](https://developer.garmin.com/connect-iq/api-docs/Toybox/StringUtil.html#Representation-module),:toRepresentation as [StringUtil.Representation](https://developer.garmin.com/connect-iq/api-docs/Toybox/StringUtil.html#Representation-module),:encoding as [StringUtil.CharacterEncoding](https://developer.garmin.com/connect-iq/api-docs/Toybox/StringUtil.html#CharacterEncoding-module) }) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Convert a String or ByteArray representation to a String or ByteArray representation whose underlying byte format corresponds to the provided input options.
- [**encodeBase64**](#encodeBase64-instance_function "encodeBase64 (Instance Function)") (string as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Encodes a String in base64.
- [**utf8ArrayToString**](#utf8ArrayToString-instance_function "utf8ArrayToString (Instance Function)") (utf8Array as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) >) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Given an Array of UTF-8 bytes, return the String equivalent.
