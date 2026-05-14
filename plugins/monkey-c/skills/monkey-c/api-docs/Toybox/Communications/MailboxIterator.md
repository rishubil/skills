---
title: Toybox.Communications.MailboxIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/MailboxIterator.html
---

## Class: Toybox.Communications.MailboxIterator

## Overview

**This has been deprecated**

This class may be removed after System 4.

## See Also:

- [Communications.registerForPhoneAppMessages()](../Communications.md#registerForPhoneAppMessages-instance_function)

## Typedef Summary

- [**MailboxKeyType**](#MailboxKeyType-named_type "MailboxKeyType (Named Type)") as [Lang.Number](../Lang/Number.md) or [Lang.Float](../Lang/Float.md) or [Lang.Long](../Lang/Long.md) or [Lang.Double](../Lang/Double.md) or [Lang.String](../Lang/String.md) or [Lang.Boolean](../Lang/Boolean.md) or [Lang.Char](../Lang/Char.md)
- [**MailboxValueType**](#MailboxValueType-named_type "MailboxValueType (Named Type)") as [MailboxIterator.MailboxKeyType](MailboxIterator.md#MailboxKeyType-named_type) or [Lang.Array](../Lang/Array.md) < [MailboxIterator.MailboxValueType](MailboxIterator.md#MailboxValueType-named_type) > or [Lang.Dictionary](../Lang/Dictionary.md) < [MailboxIterator.MailboxKeyType](MailboxIterator.md#MailboxKeyType-named_type), [MailboxIterator.MailboxValueType](MailboxIterator.md#MailboxValueType-named_type) >

## Instance Method Summary

- [**next**](#next-instance_function "next (Instance Function)") () as [MailboxIterator.MailboxValueType](MailboxIterator.md#MailboxValueType-named_type) or **Null**
	Get the next message from the mailbox.
