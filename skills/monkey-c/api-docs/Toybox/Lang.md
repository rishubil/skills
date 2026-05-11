---
title: Toybox.Lang
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang.html
---

## Module: Toybox.Lang

## Overview

## Classes Under Namespace

**Classes:** [Array](Lang/Array.md), [Boolean](Lang/Boolean.md), [ByteArray](Lang/ByteArray.md), [Char](Lang/Char.md), [Dictionary](Lang/Dictionary.md), [Double](Lang/Double.md), [Exception](Lang/Exception.md), [Float](Lang/Float.md), [InvalidOptionsException](Lang/InvalidOptionsException.md), [InvalidValueException](Lang/InvalidValueException.md), [Long](Lang/Long.md), [Method](Lang/Method.md), [Number](Lang/Number.md), [Object](Lang/Object.md), [OperationNotAllowedException](Lang/OperationNotAllowedException.md), [ResourceId](Lang/ResourceId.md), [SerializationException](Lang/SerializationException.md), [StorageFullException](Lang/StorageFullException.md), [String](Lang/String.md), [Symbol](Lang/Symbol.md), [SymbolNotAllowedException](Lang/SymbolNotAllowedException.md), [UnexpectedTypeException](Lang/UnexpectedTypeException.md), [ValueOutOfBoundsException](Lang/ValueOutOfBoundsException.md), [WeakReference](Lang/WeakReference.md)

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
	function compareTo(other as [Lang.Object](Lang/Object.md)) as [Lang.Number](Lang/Number.md);  
	}
	Comparable defines an ordering between an object and others.
- [**Comparator**](#Comparator-named_type "Comparator (Named Type)") as interface {  
	function compare(a as [Lang.Object](Lang/Object.md), b as [Lang.Object](Lang/Object.md)) as [Lang.Number](Lang/Number.md);  
	}
	Comparator defines an ordering between objects.
- [**Decimal**](#Decimal-named_type "Decimal (Named Type)") as [Lang.Float](Lang/Float.md) or [Lang.Double](Lang/Double.md)
- [**Integer**](#Integer-named_type "Integer (Named Type)") as [Lang.Number](Lang/Number.md) or [Lang.Long](Lang/Long.md)
- [**Numeric**](#Numeric-named_type "Numeric (Named Type)") as [Lang.Number](Lang/Number.md) or [Lang.Float](Lang/Float.md) or [Lang.Long](Lang/Long.md) or [Lang.Double](Lang/Double.md)

## Instance Method Summary

- [**format**](#format-instance_function "format (Instance Function)") (format as [Lang.String](Lang/String.md), parameters as [Lang.Array](Lang/Array.md)) as [Lang.String](Lang/String.md)
	Create a formatted String by substituting the given parameters into the given format at the corresponding locations.
