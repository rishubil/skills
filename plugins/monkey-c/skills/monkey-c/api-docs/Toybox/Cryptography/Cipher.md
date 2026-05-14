---
title: Toybox.Cryptography.Cipher
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Cipher.html
---

## Class: Toybox.Cryptography.Cipher

## Overview

A Cipher object.

## See Also:

- [https://en.wikipedia.org/wiki/Cipher](https://en.wikipedia.org/wiki/Cipher)

## Instance Method Summary

- [**decrypt**](#decrypt-instance_function "decrypt (Instance Function)") (ciphertext as [Lang.ByteArray](../Lang/ByteArray.md)) as [Lang.ByteArray](../Lang/ByteArray.md)
	Decrypt data with the key, depending on how the cipher was initialized.
- [**encrypt**](#encrypt-instance_function "encrypt (Instance Function)") (plaintext as [Lang.ByteArray](../Lang/ByteArray.md)) as [Lang.ByteArray](../Lang/ByteArray.md)
	Encrypt data with the key, depending on how the cipher was initialized.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:algorithm as [Cryptography.CipherAlgorithm](../Cryptography.md#CipherAlgorithm-module),:mode as [Cryptography.EncryptionMode](../Cryptography.md#EncryptionMode-module),:key as [Lang.ByteArray](../Lang/ByteArray.md),:iv as [Lang.ByteArray](../Lang/ByteArray.md) })
	Constructor.

## Instance Method Details

### decrypt(ciphertext as Lang.ByteArray) as Lang.ByteArray

Decrypt data with the key, depending on how the cipher was initialized.

Decryption can be broken up into two or more calls to decrypt(). For MODE\_CBC, the `ciphertext` length (in bytes) must be a multiple of the block size.

### encrypt(plaintext as Lang.ByteArray) as Lang.ByteArray

Encrypt data with the key, depending on how the cipher was initialized.

Encryption can be broken up into two or more calls to encrypt. For MODE\_CBC, the `plaintext` length (in bytes) must be a multiple of the block size.

### initialize(options as {:algorithm as Cryptography.CipherAlgorithm,:mode as Cryptography.EncryptionMode,:key as Lang.ByteArray,:iv as Lang.ByteArray })

Constructor
