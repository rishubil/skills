---
title: Toybox.Cryptography.Hash
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Hash.html
---

## Class: Toybox.Cryptography.Hash

## Overview

## See Also:

- [https://en.wikipedia.org/wiki/Hash\_function](https://en.wikipedia.org/wiki/Hash_function)

## Instance Method Summary

- [**digest**](#digest-instance_function "digest (Instance Function)") () as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Get the current digest of the message that has been hashed.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:algorithm as [Cryptography.HashAlgorithm](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography.html#HashAlgorithm-module) })
	Constructor.
- [**update**](#update-instance_function "update (Instance Function)") (message as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)) as **Void**
	Continue hashing of a message by consuming the next chunk of data.

## Instance Method Details

### digest() as Lang.ByteArray

Note:

This method resets the state of the Hash object, which can be used to compute a new hash
