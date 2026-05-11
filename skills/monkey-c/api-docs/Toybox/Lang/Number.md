---
title: Toybox.Lang.Number
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html
---

## Class: Toybox.Lang.Number

## Overview

## Instance Method Summary

- [**abs**](#abs-instance_function "abs (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Get the absolute value of a Number.
- [**compareTo**](#compareTo-instance_function "compareTo (Instance Function)") (other as [Lang.Object](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Object.html)) as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Compare the numeric value of self to some other numeric value.
- [**format**](#format-instance_function "format (Instance Function)") (format as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)) as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	Format a Number using a formatting String.
- [**toChar**](#toChar-instance_function "toChar (Instance Function)") () as [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)
	Convert a Number to a Char.
- [**toDouble**](#toDouble-instance_function "toDouble (Instance Function)") () as [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html)
	Convert a Number to a Double.
- [**toFloat**](#toFloat-instance_function "toFloat (Instance Function)") () as [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html)
	Convert a Number to a Float.
- [**toLong**](#toLong-instance_function "toLong (Instance Function)") () as [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html)
	Convert a Number to a Long.
- [**toNumber**](#toNumber-instance_function "toNumber (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
	Convert a Number to a Number.

## Instance Method Details

### abs() as Lang.Number

### compareTo(other as Lang.Object) as Lang.Number

### format(format as Lang.String) as Lang.String

Format a Number using a formatting String.

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
