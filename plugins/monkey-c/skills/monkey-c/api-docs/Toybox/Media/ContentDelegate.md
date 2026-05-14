---
title: Toybox.Media.ContentDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/ContentDelegate.html
---

## Class: Toybox.Media.ContentDelegate

## Overview

A delegate object that the user implements to respond to certain media events from the native media player

## Instance Method Summary

- [**getContentIterator**](#getContentIterator-instance_function "getContentIterator (Instance Function)") () as [Media.ContentIterator](ContentIterator.md) or **Null**
	Return a [ContentIterator](ContentIterator.md) object for the system to use to iterate over media tracks.
- [**onAdAction**](#onAdAction-instance_function "onAdAction (Instance Function)") (adContext as [Lang.Object](../Lang/Object.md)) as **Void**
	Respond to a user ad click.
- [**onCustomButton**](#onCustomButton-instance_function "onCustomButton (Instance Function)") (button as [Media.CustomButton](CustomButton.md)) as **Void**
	Handle a CustomButton being selected in the Media Player.
- [**onRepeat**](#onRepeat-instance_function "onRepeat (Instance Function)") () as **Void**
	Respond to a command to change repeat mode.
- [**onShuffle**](#onShuffle-instance_function "onShuffle (Instance Function)") () as **Void**
	Respond to a command to turn shuffle on or off.
- [**onSong**](#onSong-instance_function "onSong (Instance Function)") (contentRefId as [Lang.Object](../Lang/Object.md), songEvent as [Media.SongEvent](../Media.md#SongEvent-module), playbackPosition as [Lang.Number](../Lang/Number.md) or [Media.PlaybackPosition](../Media.md#PlaybackPosition-module)) as **Void**
	Handle a notification from a system that a song has been played.
- [**onThumbsDown**](#onThumbsDown-instance_function "onThumbsDown (Instance Function)") (contentRefId as [Lang.Object](../Lang/Object.md)) as **Void**
	Respond to a thumbs-down action.
- [**onThumbsUp**](#onThumbsUp-instance_function "onThumbsUp (Instance Function)") (contentRefId as [Lang.Object](../Lang/Object.md)) as **Void**
	Respond to a thumbs-up action.
- [**resetContentIterator**](#resetContentIterator-instance_function "resetContentIterator (Instance Function)") () as [Media.ContentIterator](ContentIterator.md) or **Null**
	Reset the [ContentIterator](ContentIterator.md) to the beginning of the current playlist.

## Instance Method Details

### getContentIterator() as Media.ContentIterator or Null

Return a [ContentIterator](ContentIterator.md) object for the system to use to iterate over media tracks.

### onAdAction(adContext as Lang.Object) as Void

Respond to a user ad click.

### onCustomButton(button as Media.CustomButton) as Void

Handle a CustomButton being selected in the Media Player

### onRepeat() as Void

Respond to a command to change repeat mode

### onShuffle() as Void

Respond to a command to turn shuffle on or off.

### onSong(contentRefId as Lang.Object, songEvent as Media.SongEvent, playbackPosition as Lang.Number or Media.PlaybackPosition) as Void

Handle a notification from a system that a song has been played.

### onThumbsDown(contentRefId as Lang.Object) as Void

Respond to a thumbs-down action.

The thumbs-down option is native to the device media player. When a user selects the thumbs-down function on the device, a corresponding onThumbsDown() event is sent to application.

### onThumbsUp(contentRefId as Lang.Object) as Void

Respond to a thumbs-up action.

The thumbs-up option is native to the device media player. When a user selects the thumbs-up function on the device, a corresponding onThumbsUp() event is sent to the application.

### resetContentIterator() as Media.ContentIterator or Null

Reset the [ContentIterator](ContentIterator.md) to the beginning of the current playlist.
