---
title: Toybox.Cryptography.KeyPair
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyPair.html
---

## Class: Toybox.Cryptography.KeyPair

## Overview

## See Also:

- [Toybox.Cryptography.KeyAgreement](KeyAgreement.md)

## Instance Method Summary

- [**getPrivateKey**](#getPrivateKey-instance_function "getPrivateKey (Instance Function)") () as [Cryptography.Key](Key.md)
	Get the private key.
- [**getPublicKey**](#getPublicKey-instance_function "getPublicKey (Instance Function)") () as [Cryptography.Key](Key.md)
	Get the public key.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:algorithm as [Cryptography.KeyPairAlgorithm](../Cryptography.md#KeyPairAlgorithm-module),:privateKey as [Lang.ByteArray](../Lang/ByteArray.md) })
	Constructor A KeyPair can be initialized from a private key by passing a private key [ByteArray](../Lang/ByteArray.md) from an initialized [Key](Key.md) object into the `:privateKey` option of the initialize method for this class.

## Instance Method Details

### getPrivateKey() as Cryptography.Key

### getPublicKey() as Cryptography.Key

### initialize(options as {:algorithm as Cryptography.KeyPairAlgorithm,:privateKey as Lang.ByteArray })

Note:

privateKey is expected to be in little-endian byte order.
