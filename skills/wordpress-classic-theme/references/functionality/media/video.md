---
title: Video
source: https://developer.wordpress.org/themes/classic-themes/functionality/media/video/
updated: 2026-05-11
---

# Video

**First published:** January 13, 2017  
**Last updated:** October 25, 2022

## Video

WordPress provides a video embedding capability using the `[video]` shortcode. The system supports mp4, m4v, webm, ogv, wmv, and flv formats.

### Video shortcode

To display a video player, use the basic shortcode syntax:

```php
[video src="pepper.mp4"]
```

For template implementations, employ the `do_shortcode()` function combined with `get_template_directory_uri()`:

```php
$video_file = get_template_directory_uri() . "/videos/pepper.mp4";
echo do_shortcode( '[video mp4=' . $video_file . ']' );
```

### Loop and Autoplay

To initiate playback upon page load while enabling looping:

```php
echo do_shortcode( '[video mp4=' . $video_file . ' loop="on" autoplay=1]' );
```

### Initial image and Styling

#### Poster

Set a placeholder image displaying before media playback begins:

```php
echo do_shortcode( '[video mp4=' . $video_file . ' poster=' . 
get_template_directory_uri() . '/images/album_cover.jpg]' );
```

#### Height and Width

Specify player dimensions:

```php
echo do_shortcode( '[video mp4=' . $video_file . ' width=320 height=240]' );
```

#### Styling

Target the "wp-video-shortcode" class to customize player appearance:

```css
.wp-video-shortcode {
    height: 240px;
    width: 320px;
}
```

### Supported Video formats

* mp4
* m4v
* webm
* ogv
* flv

## Navigation

- **Previous:** [Images](images.md)
- **Next:** [Navigation Menus](../navigation-menus.md)
