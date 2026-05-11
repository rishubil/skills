---
title: Toybox.StringUtil
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/StringUtil.html
---

## Module: Toybox.StringUtil

## Overview

## Classes Under Namespace

**Classes:** [InvalidHexStringException](StringUtil/InvalidHexStringException.md)

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

- [**charArrayToString**](#charArrayToString-instance_function "charArrayToString (Instance Function)") (charArray as [Lang.Array](Lang/Array.md) < [Lang.Char](Lang/Char.md) >) as [Lang.String](Lang/String.md)
	Given an Array of [Char](Lang/Char.md) objects, return the String equivalent.
- [**convertEncodedString**](#convertEncodedString-instance_function "convertEncodedString (Instance Function)") (input as [Lang.String](Lang/String.md) or [Lang.ByteArray](Lang/ByteArray.md), options as {:fromRepresentation as [StringUtil.Representation](StringUtil.md#Representation-module),:toRepresentation as [StringUtil.Representation](StringUtil.md#Representation-module),:encoding as [StringUtil.CharacterEncoding](StringUtil.md#CharacterEncoding-module) }) as [Lang.String](Lang/String.md) or [Lang.ByteArray](Lang/ByteArray.md)
	Convert a String or ByteArray representation to a String or ByteArray representation whose underlying byte format corresponds to the provided input options.
- [**encodeBase64**](#encodeBase64-instance_function "encodeBase64 (Instance Function)") (string as [Lang.String](Lang/String.md)) as [Lang.String](Lang/String.md)
	Encodes a String in base64.
- [**utf8ArrayToString**](#utf8ArrayToString-instance_function "utf8ArrayToString (Instance Function)") (utf8Array as [Lang.Array](Lang/Array.md) < [Lang.Number](Lang/Number.md) >) as [Lang.String](Lang/String.md)
	Given an Array of UTF-8 bytes, return the String equivalent.
