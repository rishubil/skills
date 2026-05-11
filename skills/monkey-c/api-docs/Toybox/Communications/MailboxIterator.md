---
title: Toybox.Communications.MailboxIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/MailboxIterator.html
---

## Class: Toybox.Communications.MailboxIterator

## Overview

**This has been deprecated**

This class may be removed after System 4.

## See Also:

- [Communications.registerForPhoneAppMessages()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications.html#registerForPhoneAppMessages-instance_function)

## Typedef Summary

- [**MailboxKeyType**](#MailboxKeyType-named_type "MailboxKeyType (Named Type)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Float](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Float.html) or [Lang.Long](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Long.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Char](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Char.html)
- [**MailboxValueType**](#MailboxValueType-named_type "MailboxValueType (Named Type)") as [MailboxIterator.MailboxKeyType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/MailboxIterator.html#MailboxKeyType-named_type) or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [MailboxIterator.MailboxValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/MailboxIterator.html#MailboxValueType-named_type) > or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [MailboxIterator.MailboxKeyType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/MailboxIterator.html#MailboxKeyType-named_type), [MailboxIterator.MailboxValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/MailboxIterator.html#MailboxValueType-named_type) >

## Instance Method Summary

- [**next**](#next-instance_function "next (Instance Function)") () as [MailboxIterator.MailboxValueType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Communications/MailboxIterator.html#MailboxValueType-named_type) or **Null**
	Get the next message from the mailbox.
