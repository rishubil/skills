---
title: Toybox.Cryptography.KeyPair
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyPair.html
---

## Class: Toybox.Cryptography.KeyPair

## Overview

## See Also:

- [Toybox.Cryptography.KeyAgreement](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyAgreement.html)

## Instance Method Summary

- [**getPrivateKey**](#getPrivateKey-instance_function "getPrivateKey (Instance Function)") () as [Cryptography.Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html)
	Get the private key.
- [**getPublicKey**](#getPublicKey-instance_function "getPublicKey (Instance Function)") () as [Cryptography.Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html)
	Get the public key.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:algorithm as [Cryptography.KeyPairAlgorithm](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography.html#KeyPairAlgorithm-module),:privateKey as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html) })
	Constructor A KeyPair can be initialized from a private key by passing a private key [ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html) from an initialized [Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html) object into the `:privateKey` option of the initialize method for this class.

## Instance Method Details

### getPrivateKey() as Cryptography.Key

### getPublicKey() as Cryptography.Key

### initialize(options as {:algorithm as Cryptography.KeyPairAlgorithm,:privateKey as Lang.ByteArray })

Note:

privateKey is expected to be in little-endian byte order.
