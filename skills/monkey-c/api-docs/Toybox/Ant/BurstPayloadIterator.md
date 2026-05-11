---
title: Toybox.Ant.BurstPayloadIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayloadIterator.html
---

## Class: Toybox.Ant.BurstPayloadIterator

## Overview

An iterator to use with a [BurstPayload](BurstPayload.md).

The BurstPayloadIterator is used to iterate over the BurstPayload and and access each data packet.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (newBurstPayload as [Ant.BurstPayload](BurstPayload.md))
	Constructor.
- [**next**](#next-instance_function "next (Instance Function)") () as [Lang.Array](../Lang/Array.md) < [Lang.Number](../Lang/Number.md) > or **Null**
	Return the next message in the [BurstPayload](BurstPayload.md) object.

## Instance Method Details

### initialize(newBurstPayload as Ant.BurstPayload)

Constructor

### next() as Lang.Array<Lang.Number> or Null

Return the next message in the [BurstPayload](BurstPayload.md) object.
