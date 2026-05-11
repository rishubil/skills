---
title: Toybox.Media
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Media.html
---

## Module: Toybox.Media

## Overview

## Classes Under Namespace

**Classes:** [ActiveContent](Media/ActiveContent.md), [AlbumArt](Media/AlbumArt.md), [AudioFormat](Media/AudioFormat.md), [CacheStatistics](Media/CacheStatistics.md), [Content](Media/Content.md), [ContentDelegate](Media/ContentDelegate.md), [ContentIterator](Media/ContentIterator.md), [ContentMetadata](Media/ContentMetadata.md), [ContentRef](Media/ContentRef.md), [ContentRefIterator](Media/ContentRefIterator.md), [CustomButton](Media/CustomButton.md), [PlaybackProfile](Media/PlaybackProfile.md), [PlayerColors](Media/PlayerColors.md), [ProviderIconInfo](Media/ProviderIconInfo.md), [SyncDelegate](Media/SyncDelegate.md), [SystemButton](Media/SystemButton.md)

## Constant Summary

### PlaybackPosition

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| PLAYBACK\_POSITION\_START | 0 | API Level 3.0.0 | The playback position when the song has begun to play |

### ContentType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONTENT\_TYPE\_INVALID | 0 | API Level 3.0.0 | Invalid content type |
| CONTENT\_TYPE\_AUDIO | 1 | API Level 3.0.0 | Content type for Audio |

### Encoding

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| ENCODING\_INVALID | 0 | API Level 3.0.0 | Invalid encoding type |
| ENCODING\_ADTS | 1 | API Level 3.0.0 | ADTS audio encoding type |
| ENCODING\_MP3 | 2 | API Level 3.0.0 | MP3 audio encoding type |
| ENCODING\_M4A | 3 | API Level 3.0.0 | M4A audio encoding type |
| ENCODING\_WAV | 4 | API Level 3.0.0 | WAV audio encoding type |

### ImageFormat

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| IMAGE\_FORMAT\_INVALID | 0 | API Level 3.0.0 | Invalid media content image format |
| IMAGE\_FORMAT\_JPEG | 1 | API Level 3.0.0 | JPEG media content image format |
| IMAGE\_FORMAT\_PNG | 2 | API Level 3.0.0 | PNG media content image format |

### PlaybackControl

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| PLAYBACK\_CONTROL\_SHUFFLE | 2 | API Level 3.0.0 | The "shuffle" operation is allowed |
| PLAYBACK\_CONTROL\_PREVIOUS | 3 | API Level 3.0.0 | The "previous track" operation is allowed |
| PLAYBACK\_CONTROL\_SKIP\_FORWARD | 5 | API Level 3.0.0 | The "skip forward x seconds" operation is allowed |
| PLAYBACK\_CONTROL\_SKIP\_BACKWARD | 6 | API Level 3.0.0 | The "skip backward x seconds" operation is allowed |
| PLAYBACK\_CONTROL\_REPEAT | 7 | API Level 3.0.0 | The "repeat" operation is allowed |
| PLAYBACK\_CONTROL\_RATING | 9 | API Level 3.0.3 | The track "rating" operation is allowed |
| PLAYBACK\_CONTROL\_PLAYBACK | 10 | API Level 3.0.3 | The "play/pause" operation is allowed |
| PLAYBACK\_CONTROL\_VOLUME | 11 | API Level 3.0.3 | The "volume" button - if not provided it will be added to the end of the playback controls |
| PLAYBACK\_CONTROL\_SOURCE | 12 | API Level 3.0.3 | The "source" button - if not provided it will be added to the end of the playback controls |
| PLAYBACK\_CONTROL\_LIBRARY | 13 | API Level 3.0.3 | The "library" button - If provided it will be used for the library button UI. |

### SongEvent

| Name | Value | Since | Description | See Also |
| --- | --- | --- | --- | --- |
| SONG\_EVENT\_START | 0 | API Level 3.0.0 | Indicates that a song was started from the beginning. | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_SKIP\_PREVIOUS | 2 | API Level 3.0.0 | Indicates that a song was skipped and the previous song was requested. | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_PLAYBACK\_NOTIFY | 3 | API Level 3.0.0 | Indicates that a song was played for the duration set in [PlaybackProfile.playbackNotificationThreshold](Media/PlaybackProfile.md#playbackNotificationThreshold-var). | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_COMPLETE | 4 | API Level 3.0.0 | Indicates that a song was completed. | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_STOP | 5 | API Level 3.0.0 | Indicates that a song was stopped in the middle of playback. | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_PAUSE | 6 | API Level 3.0.0 | Indicates that a song was paused in the middle of playback. | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_RESUME | 7 | API Level 3.0.0 | Indicates that a song was resumed after being paused. | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_SKIP\_FORWARD | 8 | API Level 4.2.4 | Indicates that a song was skipped forward by the number of seconds specified in [PlaybackProfile.skipForwardTimeDelta](Media/PlaybackProfile.md#skipForwardTimeDelta-var). | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |
| SONG\_EVENT\_SKIP\_BACKWARD | 9 | API Level 4.2.4 | Indicates that a song was skipped forward by the number of seconds specified in [PlaybackProfile.skipBackwardTimeDelta](Media/PlaybackProfile.md#skipBackwardTimeDelta-var). | - [ContentDelegate.onSong()](Media/ContentDelegate.md#onSong-instance_function) |

### RepeatMode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| REPEAT\_MODE\_OFF | 0 | API Level 3.0.0 | Repeat is off |
| REPEAT\_MODE\_ONE | 1 | API Level 3.0.0 | Repeat the current track |
| REPEAT\_MODE\_ALL | 2 | API Level 3.0.0 | Repeat all tracks |

### ButtonState

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BUTTON\_STATE\_DEFAULT | 0 | API Level 3.0.3 | The default state for a button. This is a valid state for all buttons. |
| BUTTON\_STATE\_DISABLED | 1 | API Level 3.0.3 | The button is shown but not selectable. This is a valid state for all buttons. |
| BUTTON\_STATE\_ON | 2 | API Level 3.0.3 | The button is considered "on". This is a valid state for the PLAYBACK\_CONTROL\_PLAYBACK, PLAYBACK\_CONTROL\_SHUFFLE, and PLAYBACK\_CONTROL\_REPEAT buttons. |
| BUTTON\_STATE\_OFF | 3 | API Level 3.0.3 | The button is considered "off". This is a valid state for the PLAYBACK\_CONTROL\_PLAYBACK, PLAYBACK\_CONTROL\_SHUFFLE, and PLAYBACK\_CONTROL\_REPEAT buttons. |
| BUTTON\_STATE\_ALL | 4 | API Level 3.0.3 | The button is considered in the "on" and "all" states. This is a valid state the for the PLAYBACK\_CONTROL\_SHUFFLE (shuffle all) and PLAYBACK\_CONTROL\_REPEAT (repeat all) buttons. |
| BUTTON\_STATE\_POSITIVE | 5 | API Level 3.0.3 | The button is considered in the "positive" state. This is a valid state the for the PLAYBACK\_CONTROL\_RATING button. |
| BUTTON\_STATE\_NEGATIVE | 6 | API Level 3.0.3 | The button is considered in the "negative" state. This is a valid state the for the PLAYBACK\_CONTROL\_RATING button. |
| BUTTON\_STATE\_NEUTRAL | 7 | API Level 3.0.3 | The button is considered in the "neutral" state. This is a valid state the for the PLAYBACK\_CONTROL\_RATING button. |

### ButtonImage

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BUTTON\_IMAGE\_ICON | 0 | API Level 3.0.3 | The normal sized button image |
| BUTTON\_IMAGE\_DETAIL | 1 | API Level 3.0.3 | The larger image for when the icon is highlighted |

## Instance Method Summary

- [**deleteCachedItem**](#deleteCachedItem-instance_function "deleteCachedItem (Instance Function)") (contentRef as [Media.ContentRef](Media/ContentRef.md)) as **Void**
	Delete an individual cached media item.
- [**getCacheStatistics**](#getCacheStatistics-instance_function "getCacheStatistics (Instance Function)") () as [Media.CacheStatistics](Media/CacheStatistics.md)
	Get the current size statistics of the media cache.
- [**getCachedContentObj**](#getCachedContentObj-instance_function "getCachedContentObj (Instance Function)") (contentRef as [Media.ContentRef](Media/ContentRef.md)) as [Media.Content](Media/Content.md)
	Get a [Content](Media/Content.md) object by ID from what has been persisted on the system.
- [**getContentRefIter**](#getContentRefIter-instance_function "getContentRefIter (Instance Function)") (options as {:contentType as [Media.ContentType](Media.md#ContentType-module),:shuffle as [Lang.Boolean](Lang/Boolean.md) }) as [Media.ContentRefIterator](Media/ContentRefIterator.md)
	Get a [ContentRefIterator](Media/ContentRefIterator.md) object.
- [**notifySyncComplete**](#notifySyncComplete-instance_function "notifySyncComplete (Instance Function)") (errorMessage as [Lang.String](Lang/String.md) or **Null**) as **Void** deprecated
	Send a system notification to indicate that the sync completed.
- [**notifySyncProgress**](#notifySyncProgress-instance_function "notifySyncProgress (Instance Function)") (percentageComplete as [Lang.Number](Lang/Number.md)) as **Void** deprecated
	Send a system notification to indicate overall sync progress.
- [**requestPlaybackProfileUpdate**](#requestPlaybackProfileUpdate-instance_function "requestPlaybackProfileUpdate (Instance Function)") () as **Void**
	Request that the media player call [ContentIterator.getPlaybackProfile()](Media/ContentIterator.md#getPlaybackProfile-instance_function).
- [**resetContentCache**](#resetContentCache-instance_function "resetContentCache (Instance Function)") () as **Void**
	Delete the cached media content and reset the encryption key for the app.
- [**setAlbumArt**](#setAlbumArt-instance_function "setAlbumArt (Instance Function)") (albumArt as [Graphics.BitmapType](Graphics.md#BitmapType-named_type) or **Null**) as **Void**
	Set the album art for the currently playing song.
- [**startPlayback**](#startPlayback-instance_function "startPlayback (Instance Function)") (args as [Application.PersistableType](Application.md#PersistableType-named_type)) as **Void**
	Exit the [AudioContentProviderApp](Application/AudioContentProviderApp.md) in its current mode and launch it in playback mode.
- [**startSync**](#startSync-instance_function "startSync (Instance Function)") () as **Void** deprecated
	Exit the [AudioContentProviderApp](Application/AudioContentProviderApp.md) in its current mode and launch it in sync mode.
- [**stopPlayback**](#stopPlayback-instance_function "stopPlayback (Instance Function)") () as **Void**
	Stops playback if it was initiated by the app.

## Instance Method Details

### deleteCachedItem(contentRef as Media.ContentRef) as Void

### getCacheStatistics() as Media.CacheStatistics

### getCachedContentObj(contentRef as Media.ContentRef) as Media.Content

### getContentRefIter(options as {:contentType as Media.ContentType,:shuffle as Lang.Boolean }) as Media.ContentRefIterator

### notifySyncComplete(errorMessage as Lang.String or Null) as Void

**This has been deprecated**

This method may be removed after System 9.

### notifySyncProgress(percentageComplete as Lang.Number) as Void

**This has been deprecated**

This method may be removed after System 9.

### requestPlaybackProfileUpdate() as Void

### resetContentCache() as Void

### setAlbumArt(albumArt as Graphics.BitmapType or Null) as Void

Note:

[BitmapReference](Graphics/BitmapReference.md) is only supported in CIQ 4.0.0 and later

### startPlayback(args as Application.PersistableType) as Void

### startSync() as Void

**This has been deprecated**

This method may be removed after System 9.
