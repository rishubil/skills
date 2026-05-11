---
title: Toybox.Authentication.OAuthMessage
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication/OAuthMessage.html
---

## Class: Toybox.Authentication.OAuthMessage

## Overview

An OAuthMessage received by the callback registered in [registerForOAuthMessages()](../Authentication.md#registerForOAuthMessages-instance_function).

Unlike the `data` in the [Message](Message.md) parent class, data in an OAuthMessage should always be a [Dictionary](../Lang/Dictionary.md).

## Instance Member Summary

- [**responseCode**](#responseCode-var "responseCode (Var)") as [Lang.Number](../Lang/Number.md)
	An HTTP response code (positive value) or BLE error code (negative value).

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.

## Instance Attribute Details

### var responseCode as Lang.Number

An HTTP response code (positive value) or BLE error code (negative value).

## Instance Method Details

### initialize()

Constructor
