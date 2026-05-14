---
title: Toybox.Media.PlaybackProfile
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media/PlaybackProfile.html
---

## Class: Toybox.Media.PlaybackProfile

## Overview

Provides the media player with specific rules about what playback options are supported.

## Instance Member Summary

- [**attemptSkipAfterThumbsDown**](#attemptSkipAfterThumbsDown-var "attemptSkipAfterThumbsDown (Var)") as [Lang.Boolean](../Lang/Boolean.md) or **Null**
	Defines if the current song is skipped if a thumbs-down operation is given.
- [**playbackControls**](#playbackControls-var "playbackControls (Var)") as [Lang.Array](../Lang/Array.md) < [Media.PlaybackControl](../Media.md#PlaybackControl-module) or [Media.CustomButton](CustomButton.md) or [Media.SystemButton](SystemButton.md) > or **Null**
	Playback controls that should be rendered in the player.
- [**playbackNotificationThreshold**](#playbackNotificationThreshold-var "playbackNotificationThreshold (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The number of seconds a song must play to trigger a "played" notification.
- [**playerColors**](#playerColors-var "playerColors (Var)") as [Media.PlayerColors](PlayerColors.md) or **Null**
	The colors for the media player.
- [**requirePlaybackNotification**](#requirePlaybackNotification-var "requirePlaybackNotification (Var)") as [Lang.Boolean](../Lang/Boolean.md) or **Null**
	Defines if the system notifies the app when each song is played.
- [**skipBackwardTimeDelta**](#skipBackwardTimeDelta-var "skipBackwardTimeDelta (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The number of seconds to move backward in a track during a skip backward event.
- [**skipForwardTimeDelta**](#skipForwardTimeDelta-var "skipForwardTimeDelta (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The number of seconds to move forward in a track during a skip forward event.
- [**skipPreviousThreshold**](#skipPreviousThreshold-var "skipPreviousThreshold (Var)") as [Lang.Number](../Lang/Number.md) or **Null**
	The amount of time a song must be played so that pressing back restarts the track and requires a second back press to skip to the previous track in seconds.

## Instance Attribute Details

### var attemptSkipAfterThumbsDown as Lang.Boolean or Null

Defines if the current song is skipped if a thumbs-down operation is given

### var playbackControls as Lang.Array<Media.PlaybackControl or Media.CustomButton or Media.SystemButton> or Null

Playback controls that should be rendered in the player.

This is an Array that holds a combination of [PLAYBACK\_CONTROL\_\*](../Media.md#PlaybackControl-module), [CustomButton](CustomButton.md), and [SystemButton](SystemButton.md) values defined by the developer. The values in this Array determine which native media player control options are rendered and available to the end user of the current device. The first entry in the array may be used as a hotkey in the media player. This is device dependent.

### var playbackNotificationThreshold as Lang.Number or Null

The number of seconds a song must play to trigger a "played" notification. A value of 0 means notify as soon as the song begins playing.

### var playerColors as Media.PlayerColors or Null

The colors for the media player. If set to `null` the default colors that are device-dependent will be used.

### var requirePlaybackNotification as Lang.Boolean or Null

Defines if the system notifies the app when each song is played

### var skipBackwardTimeDelta as Lang.Number or Null

The number of seconds to move backward in a track during a skip backward event. If set to `null` the default value of 30 seconds will be used.

### var skipForwardTimeDelta as Lang.Number or Null

The number of seconds to move forward in a track during a skip forward event. If set to `null` the default value of 30 seconds will be used.

### var skipPreviousThreshold as Lang.Number or Null

The amount of time a song must be played so that pressing back restarts the track and requires a second back press to skip to the previous track in seconds. If set to `null` a default value that is device-dependent will be used.
