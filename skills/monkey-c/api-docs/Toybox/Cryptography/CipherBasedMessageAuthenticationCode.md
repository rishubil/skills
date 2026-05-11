---
title: Toybox.Cryptography.CipherBasedMessageAuthenticationCode
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/CipherBasedMessageAuthenticationCode.html
---

## Class: Toybox.Cryptography.CipherBasedMessageAuthenticationCode

## Overview

Cipher-Based Message Authentication Code (CMAC) object.

A CipherBasedMessageAuthenticationCode is an object that can be used to compute a message authentication code using the CMAC algorithm.

## See Also:

- [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38b.pdf)

## Instance Method Summary

- [**digest**](#digest-instance_function "digest (Instance Function)") () as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Return the digest of the authentication code.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:algorithm as [Cryptography.CipherAlgorithm](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography.html#CipherAlgorithm-module),:key as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html) })
	Constructor.
- [**update**](#update-instance_function "update (Instance Function)") (message as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)) as **Void**
	Continue the computation of the CMAC by consuming the next chunk of data.

## Instance Method Details

### digest() as Lang.ByteArray

Return the digest of the authentication code.

The state of the object is reset and can be used to compute a new authentication code with the same options.

### initialize(options as {:algorithm as Cryptography.CipherAlgorithm,:key as Lang.ByteArray })

Constructor

### update(message as Lang.ByteArray) as Void

Continue the computation of the CMAC by consuming the next chunk of data.

Repeated calls are equivalent to a single call with the concatenation of all the arguments.
