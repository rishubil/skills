---
title: Audio
source: https://developer.wordpress.org/themes/classic-themes/functionality/media/audio/
updated: 2026-05-11
---

# Audio

**Published:** January 13, 2017  
**Last Updated:** January 15, 2017

## Audio

You can directly embed audio files and play them back using a simple shortcode **[audio]**. The compatible formats include mp3, ogg, wma, m4a, and wav files.

### Audio shortcode

A basic implementation displays an audio player that loads a music file:

```php
[audio src="music.mp3"]
```

To integrate this into a template file, use the `do_shortcode` function. For audio stored in a theme's sounds directory:

```php
$music_file = get_template_directory_uri() . "/sounds/music.mp3";
echo do_shortcode('[audio mp3=' . $music_file . ']');
```

### Loop and Autoplay

The shortcode supports two main options:

**loop**
- "off" – Prevents looping (default setting)
- "on" – Media repeats from the beginning when finished

**autoplay**
- 0 – Media does not start automatically (default)
- 1 – Media begins playing when ready

Example combining both features:

```php
echo do_shortcode('[audio mp3=' . $music_file . ' loop = "on" autoplay = 1]');
```

### Styling

Customize the player's appearance by targeting the "wp-audio-shortcode" class:

```css
.wp-audio-shortcode {
  width: 50%;
}
```

### Supported Audio formats

- mp3
- ogg
- wma
- m4a
- wav

## Navigation

- **Previous:** [Media](index.md)
- **Next:** [Galleries](galleries.md)
