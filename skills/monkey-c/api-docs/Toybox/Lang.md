---
title: Toybox.Lang
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html
---

## Module: Toybox.Lang

## Overview

## Classes Under Namespace

**Classes:** [Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html), [Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html), [ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html), [Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html), [Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html), [Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html), [Exception](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Exception.html), [Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html), [InvalidOptionsException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/InvalidOptionsException.html), [InvalidValueException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/InvalidValueException.html), [Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html), [Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html), [Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html), [Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html), [OperationNotAllowedException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/OperationNotAllowedException.html), [ResourceId](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ResourceId.html), [SerializationException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/SerializationException.html), [StorageFullException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/StorageFullException.html), [String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), [Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html), [SymbolNotAllowedException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/SymbolNotAllowedException.html), [UnexpectedTypeException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/UnexpectedTypeException.html), [ValueOutOfBoundsException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ValueOutOfBoundsException.html), [WeakReference](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/WeakReference.html)

## Constant Summary

### NumberFormat

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| NUMBER\_FORMAT\_FLOAT | 0 | API Level 3.1.0 | IEEE 754 Single Precision Float Value (32-bits) |
| NUMBER\_FORMAT\_SINT16 | 1 | API Level 3.1.0 | Signed 16-bit Integer Value |
| NUMBER\_FORMAT\_SINT32 | 2 | API Level 3.1.0 | Signed 32-bit Integer Value |
| NUMBER\_FORMAT\_SINT8 | 3 | API Level 3.1.0 | Signed 8-bit Integer Value |
| NUMBER\_FORMAT\_UINT16 | 4 | API Level 3.1.0 | Unsigned 16-bit Integer Value |
| NUMBER\_FORMAT\_UINT32 | 5 | API Level 3.1.0 | Unsigned 32-bit Integer Value |
| NUMBER\_FORMAT\_UINT8 | 6 | API Level 3.1.0 | Unsigned 8-bit Integer Value |

### Endian

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ENDIAN\_LITTLE | 0 | API Level 3.1.0 |  |
| ENDIAN\_BIG | 1 | API Level 3.1.0 |  |

## Typedef Summary

- [**Comparable**](#Comparable-named_type "Comparable (Named Type)") as interface {  
	function compareTo(other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html);  
	}
	Comparable defines an ordering between an object and others.
- [**Comparator**](#Comparator-named_type "Comparator (Named Type)") as interface {  
	function compare(a as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html), b as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html);  
	}
	Comparator defines an ordering between objects.
- [**Decimal**](#Decimal-named_type "Decimal (Named Type)") as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html)
- [**Integer**](#Integer-named_type "Integer (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html)
- [**Numeric**](#Numeric-named_type "Numeric (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html)

## Instance Method Summary

- [**format**](#format-instance_function "format (Instance Function)") (format as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), parameters as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html)) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Create a formatted String by substituting the given parameters into the given format at the corresponding locations.
