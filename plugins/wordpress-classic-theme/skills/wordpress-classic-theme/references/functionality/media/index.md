---
title: Media
source: https://developer.wordpress.org/themes/classic-themes/functionality/media/
updated: 2026-05-11
---

# Media

**Author:** Samuel Sidler  
**Published:** October 23, 2014  
**Last Modified:** January 15, 2017

## Overview

WordPress enables theme developers to customize the look, feel, and functionality of the platform's core media capabilities.

## General

WordPress allows users to upload, store, and display various media types including images, videos, and audio files through the Media > Add New section or the Post/Page Editor's Add Media button.

Media uploaded during post editing automatically attaches to that post. Media uploaded separately through the Media Library remains unattached until inserted into a post.

### Retrieving Attachment ID or Image ID

To retrieve attachment IDs, use the `get_posts()` or `get_children()` functions:

```php
// Insert into the Loop
$args = array(
    'post_parent'    => get_the_ID(),
    'post_type'      => 'attachment',
);
$attachments = get_posts( $args );
if ( $attachments ) {
    foreach ( $attachments as $attachment ) {
        $meta_data = wp_get_attachment_metadata( $attachment->ID, false );
    }
}
```

To retrieve only images, add `'post_mime_type' => 'image'` to the arguments array.

**Related Functions:**
- `get_posts()`
- `get_children()`
- `wp_get_attachment_metadata()`

## Special Considerations

### Compatible Media Formats

The Media Library accepts various file types including images, videos, audio, documents, and binary files. Audio and Video files use the internal MediaElement.js library for processing.

### Troubleshooting

**Cannot Retrieve Attachment:** If `get_posts()` or `get_children()` don't return expected results, verify the media is attached to the post by checking the "Uploaded to" column in Media > Library.

## Sub-pages

- [Audio](audio.md)
- [Galleries](galleries.md)
- [Images](images.md)
- [Video](video.md)

## Navigation

- **Previous:** [Localization](../localization.md)
- **Next:** [Audio](audio.md)
