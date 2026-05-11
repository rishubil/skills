---
title: Toybox.Authentication.OAuthMessage
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication/OAuthMessage.html
---

## Class: Toybox.Authentication.OAuthMessage

## Overview

An OAuthMessage received by the callback registered in [registerForOAuthMessages()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication.html#registerForOAuthMessages-instance_function).

Unlike the `data` in the [Message](https://developer.garmin.com/connect-iq/api-docs/Toybox/Authentication/Message.html) parent class, data in an OAuthMessage should always be a [Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html).

## Instance Member Summary

- [**responseCode**](#responseCode-var "responseCode (Var)") as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)
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
