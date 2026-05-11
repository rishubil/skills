---
title: Toybox.ActivityMonitor.HeartRateIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/HeartRateIterator.html
---

## Class: Toybox.ActivityMonitor.HeartRateIterator

## Overview

A class containing heart rate data for a given period of time.

## Instance Method Summary

- [**getMax**](#getMax-instance_function "getMax (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Get the maximum heart rate contained in this iterator.
- [**getMin**](#getMin-instance_function "getMin (Instance Function)") () as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or **Null**
	Get the minimum heart rate contained in this iterator.
- [**next**](#next-instance_function "next (Instance Function)") () as [ActivityMonitor.HeartRateSample](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityMonitor/HeartRateSample.html) or **Null**
	Get the next entry in the iterator.

## Instance Method Details

### getMax() as Lang.Number or Null

Get the maximum heart rate contained in this iterator.

### getMin() as Lang.Number or Null

Get the minimum heart rate contained in this iterator.

### next() as ActivityMonitor.HeartRateSample or Null

Get the next entry in the iterator.

This must be called to get the initial data from the iterator.
