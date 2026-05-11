---
title: Toybox.Ant.BurstPayloadIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayloadIterator.html
---

## Class: Toybox.Ant.BurstPayloadIterator

## Overview

An iterator to use with a [BurstPayload](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayload.html).

The BurstPayloadIterator is used to iterate over the BurstPayload and and access each data packet.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (newBurstPayload as [Ant.BurstPayload](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayload.html))
	Constructor.
- [**next**](#next-instance_function "next (Instance Function)") () as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) > or **Null**
	Return the next message in the [BurstPayload](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayload.html) object.

## Instance Method Details

### initialize(newBurstPayload as Ant.BurstPayload)

Constructor

### next() as Lang.Array<Lang.Number> or Null

Return the next message in the [BurstPayload](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayload.html) object.
