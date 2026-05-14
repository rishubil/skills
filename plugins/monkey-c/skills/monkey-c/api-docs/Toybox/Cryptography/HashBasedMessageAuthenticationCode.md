---
title: Toybox.Cryptography.HashBasedMessageAuthenticationCode
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/HashBasedMessageAuthenticationCode.html
---

## Class: Toybox.Cryptography.HashBasedMessageAuthenticationCode

## Overview

Hash-Based Message Authentication Code (HMAC) object.

A HashBasedMessageAuthenticationCode is an object that can be used to compute a message authentication code using the HMAC algorithm.

## See Also:

- [http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.198-1.pdf](http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.198-1.pdf)

## Instance Method Summary

- [**digest**](#digest-instance_function "digest (Instance Function)") () as [Lang.ByteArray](../Lang/ByteArray.md)
	Return the digest of the authentication code.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:algorithm as [Cryptography.HashAlgorithm](../Cryptography.md#HashAlgorithm-module),:key as [Lang.ByteArray](../Lang/ByteArray.md) })
	Constructor.
- [**update**](#update-instance_function "update (Instance Function)") (message as [Lang.ByteArray](../Lang/ByteArray.md)) as **Void**
	Continue computation of the HMAC by consuming the next chunk of data.

## Instance Method Details

### digest() as Lang.ByteArray

Return the digest of the authentication code.

The state of the object is reset and can be used to compute a new authentication code with the same options.

### initialize(options as {:algorithm as Cryptography.HashAlgorithm,:key as Lang.ByteArray })

Constructor

### update(message as Lang.ByteArray) as Void

Continue computation of the HMAC by consuming the next chunk of data.

Repeated calls are equivalent to a single call with the concatenation of all the arguments.
