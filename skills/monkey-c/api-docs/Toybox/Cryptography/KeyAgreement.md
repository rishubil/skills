---
title: Toybox.Cryptography.KeyAgreement
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyAgreement.html
---

## Class: Toybox.Cryptography.KeyAgreement

## Overview

A local private key in combination with a public key to generate a shared secret.

## Instance Method Summary

- [**addKey**](#addKey-instance_function "addKey (Instance Function)") (key as [Cryptography.Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html)) as **Void**
	Add a public [Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html) to KeyAgreement.
- [**generateSecret**](#generateSecret-instance_function "generateSecret (Instance Function)") () as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Generate a shared secret for the KeyAgreement.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (options as {:protocol as [Cryptography.KeyAgreementProtocol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography.html#KeyAgreementProtocol-module),:privateKey as [Cryptography.Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html) })
	Constructor.

## Instance Method Details

### addKey(key as Cryptography.Key) as Void

Add a public [Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html) to KeyAgreement.

### generateSecret() as Lang.ByteArray

Generate a shared secret for the KeyAgreement.

### initialize(options as {:protocol as Cryptography.KeyAgreementProtocol,:privateKey as Cryptography.Key })

Constructor
