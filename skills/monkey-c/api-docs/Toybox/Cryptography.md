---
title: Toybox.Cryptography
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography.html
---

## Module: Toybox.Cryptography

## Overview

## Classes Under Namespace

**Classes:** [Cipher](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Cipher.html), [CipherBasedMessageAuthenticationCode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/CipherBasedMessageAuthenticationCode.html), [Hash](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Hash.html), [HashBasedMessageAuthenticationCode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/HashBasedMessageAuthenticationCode.html), [InvalidBlockSizeException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/InvalidBlockSizeException.html), [Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html), [KeyAgreement](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyAgreement.html), [KeyPair](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyPair.html)

## Constant Summary

### HashAlgorithm

| Name | Value | Since | Description | See Also | Note |
| --- | --- | --- | --- | --- | --- |
| HASH\_SHA1 | 0 | API Level 3.0.0 | SHA-1 implementation for Hash objects | - [https://en.wikipedia.org/wiki/SHA-1](https://en.wikipedia.org/wiki/SHA-1) | The SHA-1 algorithm has known vulnerabilities and should not be used for security purposes. |
| HASH\_SHA256 | 1 | API Level 3.0.0 | SHA-256 implementation for Hash objects | - [https://en.wikipedia.org/wiki/SHA-2](https://en.wikipedia.org/wiki/SHA-2) |  |
| HASH\_MD5 | 2 | API Level 3.0.0 | MD5 implementation for Hash objects | - [https://en.wikipedia.org/wiki/MD5](https://en.wikipedia.org/wiki/MD5) | The MD5 algorithm has known vulnerabilities and should not be used for security purposes. |

### CipherAlgorithm

| Name | Value | Since | Description | See Also |
| --- | --- | --- | --- | --- |
| CIPHER\_AES128 | 0 | API Level 3.0.0 | AES128 implementation for Cipher objects | - [https://en.wikipedia.org/wiki/Advanced\_Encryption\_Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) |
| CIPHER\_AES256 | 1 | API Level 3.0.0 | AES256 implementation for Cipher objects | - [https://en.wikipedia.org/wiki/Advanced\_Encryption\_Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) |

### EncryptionMode

| Name | Value | Since | Description | See Also |
| --- | --- | --- | --- | --- |
| MODE\_ECB | 0 | API Level 3.0.0 | Electronic Code Book (ECB)  This is the simplest encryption mode. Each plaintext block is directly encrypted into a ciphertext block, independent of any other block. This mode exposes frequency of symbols in your plaintext. Other modes (e.g. CBC) are recommended. | - [https://en.wikipedia.org/wiki/Block\_cipher\_mode\_of\_operation#Electronic\_Codebook\_(ECB)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_\(ECB\)) |
| MODE\_CBC | 1 | API Level 3.0.0 | Cipher-Block Chaining  Each ciphertext block depends on the current and all previous plaintext blocks. An Initialization Vector (IV) is required. The IV is a data block to be transmitted to the receiver. The IV can be made public, but it must be authenticated by the receiver and it should be picked randomly. | - [https://en.wikipedia.org/wiki/Block\_cipher\_mode\_of\_operation#Cipher\_Block\_Chaining\_(CBC)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_\(CBC\)) |

### KeyPairAlgorithm

| Name | Value | Since | Description | See Also |
| --- | --- | --- | --- | --- |
| KEY\_PAIR\_ELLIPTIC\_CURVE\_SECP224R1 | 0 | API Level 3.0.0 | 224-bit secp224r1 Elliptic Curve  Based on the algebraic structure of elliptic curves over finite fields. ECC requires smaller keys compared to non-ECC cryptography to provide equivalent security. | - [https://en.wikipedia.org/wiki/Elliptic-curve\_cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) |
| KEY\_PAIR\_ELLIPTIC\_CURVE\_SECP256R1 | 1 | API Level 3.0.0 | 256-bit secp256r1 Elliptic Curve  Based on the algebraic structure of elliptic curves over finite fields. ECC requires smaller keys compared to non-ECC cryptography to provide equivalent security. | - [https://en.wikipedia.org/wiki/Elliptic-curve\_cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) |

### KeyAgreementProtocol

| Name | Value | Since | Description | See Also |
| --- | --- | --- | --- | --- |
| KEY\_AGREEMENT\_ECDH | 0 | API Level 3.0.0 | Elliptic Curve Diffie-Hellman (ECDH) | - [https://en.wikipedia.org/wiki/Elliptic-curve\_Diffie%E2%80%93Hellman](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman) |

## Instance Method Summary

- [**createPublicKey**](#createPublicKey-instance_function "createPublicKey (Instance Function)") (algorithm as [Cryptography.HashAlgorithm](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography.html#HashAlgorithm-module), bytes as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)) as [Cryptography.Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html)
	Create a public [Key](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/Key.html) object from bytes to be added to a [KeyAgreement](https://developer.garmin.com/connect-iq/api-docs/Toybox/Cryptography/KeyAgreement.html).
- [**randomBytes**](#randomBytes-instance_function "randomBytes (Instance Function)") (size as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as [Lang.ByteArray](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/ByteArray.html)
	Generates cryptographically random bytes.

## Instance Method Details

### createPublicKey(algorithm as Cryptography.HashAlgorithm, bytes as Lang.ByteArray) as Cryptography.Key

Note:

bytes is expected to be in little-endian byte order.
