---
title: Toybox.Cryptography.KeyAgreement
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyAgreement.html
---

## Class: Toybox.Cryptography.KeyAgreement

## Overview

A local private key in combination with a public key to generate a shared secret.

## Instance Method Summary

- [**addKey**](#addKey-instance_function "addKey (Instance Function)") (key as [Cryptography.Key](Key.md)) as **Void**
	Add a public [Key](Key.md) to KeyAgreement.
- [**generateSecret**](#generateSecret-instance_function "generateSecret (Instance Function)") () as [Lang.ByteArray](../Lang/ByteArray.md)
	Generate a shared secret for the KeyAgreement.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:protocol as [Cryptography.KeyAgreementProtocol](../Cryptography.md#KeyAgreementProtocol-module),:privateKey as [Cryptography.Key](Key.md) })
	Constructor.

## Instance Method Details

### addKey(key as Cryptography.Key) as Void

Add a public [Key](Key.md) to KeyAgreement.

### generateSecret() as Lang.ByteArray

Generate a shared secret for the KeyAgreement.

### initialize(options as {:protocol as Cryptography.KeyAgreementProtocol,:privateKey as Cryptography.Key })

Constructor
