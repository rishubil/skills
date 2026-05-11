---
title: Toybox.Ant.BurstListener
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstListener.html
---

## Class: Toybox.Ant.BurstListener

## Overview

A class that provides a set of callback methods to handle the different burst transmission scenarios in the Ant SDK.

## Instance Method Summary

- [**onReceiveComplete**](#onReceiveComplete-instance_function "onReceiveComplete (Instance Function)") (burstPayload as [Ant.BurstPayload](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant/BurstPayload.html)) as **Void**
	Callback when a burst reception completes successfully.
- [**onReceiveFail**](#onReceiveFail-instance_function "onReceiveFail (Instance Function)") (errorCode as [Ant.BurstError](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#BurstError-module)) as **Void**
	Callback when a burst reception fails over the air.
- [**onTransmitComplete**](#onTransmitComplete-instance_function "onTransmitComplete (Instance Function)") () as **Void**
	Callback when a burst transmission completes successfully.
- [**onTransmitFail**](#onTransmitFail-instance_function "onTransmitFail (Instance Function)") (errorCode as [Ant.BurstError](https://developer.garmin.com/connect-iq/api-docs/Toybox/Ant.html#BurstError-module)) as **Void**
	Callback when a burst transmission fails over the air.

## Instance Method Details

### onReceiveComplete(burstPayload as Ant.BurstPayload) as Void

Callback when a burst reception completes successfully

### onReceiveFail(errorCode as Ant.BurstError) as Void

Callback when a burst reception fails over the air

### onTransmitComplete() as Void

Callback when a burst transmission completes successfully

### onTransmitFail(errorCode as Ant.BurstError) as Void

Callback when a burst transmission fails over the air
