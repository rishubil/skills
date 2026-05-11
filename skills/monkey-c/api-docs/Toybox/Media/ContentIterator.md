---
title: Toybox.Media.ContentIterator
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/ContentIterator.html
---

## Class: Toybox.Media.ContentIterator

## Overview

A user-defined iterator that returns referenced to media content on the system for use by the system media player.

## Instance Method Summary

- [**canSkip**](#canSkip-instance_function "canSkip (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Determine if the the current track can be skipped.
- [**get**](#get-instance_function "get (Instance Function)") () as [Media.Content](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/Content.html) or **Null**
	Get the current media content object.
- [**getPlaybackProfile**](#getPlaybackProfile-instance_function "getPlaybackProfile (Instance Function)") () as [Media.PlaybackProfile](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/PlaybackProfile.html) or **Null**
	Get the current media content playback profile.
- [**next**](#next-instance_function "next (Instance Function)") () as [Media.Content](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/Content.html) or **Null**
	Get the next media content object.
- [**peekNext**](#peekNext-instance_function "peekNext (Instance Function)") () as [Media.Content](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/Content.html) or **Null**
	Get the next media content object without incrementing the iterator.
- [**peekPrevious**](#peekPrevious-instance_function "peekPrevious (Instance Function)") () as [Media.Content](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/Content.html) or **Null**
	Get the previous media content object without decrementing the iterator.
- [**previous**](#previous-instance_function "previous (Instance Function)") () as [Media.Content](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/Content.html) or **Null**
	Get the previous media content object.
- [**repeatMode**](#repeatMode-instance_function "repeatMode (Instance Function)") () as [Media.RepeatMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html#RepeatMode-module) or **Null**
	Get the current repeat state.
- [**shuffling**](#shuffling-instance_function "shuffling (Instance Function)") () as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Determine if playback is currently set to shuffle.

## Instance Method Details

### canSkip() as Lang.Boolean

Determine if the the current track can be skipped.

### get() as Media.Content or Null

Get the current media content object.

### getPlaybackProfile() as Media.PlaybackProfile or Null

Get the current media content playback profile

### next() as Media.Content or Null

Get the next media content object.

### peekNext() as Media.Content or Null

Get the next media content object without incrementing the iterator.

### peekPrevious() as Media.Content or Null

Get the previous media content object without decrementing the iterator.

### previous() as Media.Content or Null

Get the previous media content object.

### repeatMode() as Media.RepeatMode or Null

Get the current repeat state

### shuffling() as Lang.Boolean

Determine if playback is currently set to shuffle.

Returns `true` if shuffle is on, otherwise `false`.
