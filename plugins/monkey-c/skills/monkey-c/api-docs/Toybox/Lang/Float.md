---
title: Toybox.Lang.Float
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html
---

## Class: Toybox.Lang.Float

## Overview

## Instance Method Summary

- [**abs**](#abs-instance_function "abs (Instance Function)") () as [Lang.Float](Float.md)
	Get the absolute value of a Float.
- [**compareTo**](#compareTo-instance_function "compareTo (Instance Function)") (other as [Lang.Object](Object.md)) as [Lang.Number](Number.md)
	Compare the numeric value of self to some other numeric value.
- [**format**](#format-instance_function "format (Instance Function)") (format as [Lang.String](String.md)) as [Lang.String](String.md)
	Format a Float using a formatting String.
- [**toDouble**](#toDouble-instance_function "toDouble (Instance Function)") () as [Lang.Double](Double.md)
	Convert a Float to a Double.
- [**toFloat**](#toFloat-instance_function "toFloat (Instance Function)") () as [Lang.Float](Float.md)
	Convert a Float to a Float.
- [**toLong**](#toLong-instance_function "toLong (Instance Function)") () as [Lang.Long](Long.md)
	Convert a Float to a Long.
- [**toNumber**](#toNumber-instance_function "toNumber (Instance Function)") () as [Lang.Number](Number.md)
	Convert a Float to a Number.

## Instance Method Details

### abs() as Lang.Float

### compareTo(other as Lang.Object) as Lang.Number

Compare the numeric value of self to some other numeric value. NaN is

```
considered greater than all numbers and equal to itself.
```

### format(format as Lang.String) as Lang.String

Format a Float using a formatting String.

The formatting string is similar to that available in `printf` from the C stdio library, though the `length` option is not available:

```
"%[flags][width][.precision]specifier"
```

specifiers

- **d** or **i** - signed decimal integer
- **e** - scientific notation (mantissa/exponent) using 'e' character
- **E** - scientific notation (mantissa/exponent) using 'E' character
- **f** - decimal floating point
- **o** - signed octal
- **u** - unsigned decimal integer
- **x** - unsigned hexadecimal integer
- **X** - unsigned hexadecimal integer (capital letters)

flags

- \+ - Prepends the result with a plus or minus sign ('+' or '-'), including positive numbers. By default, only negative numbers are preceded with a '-' sign.
- **0** - Left-pads the number with zeros (0) instead of spaces, where padding is specified (see width sub-specifier).
