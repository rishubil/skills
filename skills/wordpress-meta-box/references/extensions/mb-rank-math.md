---
title: MB Rank Math - Meta Box Documentation
source: https://docs.metabox.io/extensions/mb-rank-math/
version: 5.12.0
fetched: 2026-05-11
---

MB Rank Math helps you to add content of custom fields to Rank Math Content Analysis to have better SEO score.

![MB Rank Math Integration](https://imgur.elightup.com/tIyC0u9.jpg)

## Settings

To let Rank Math get a field's content to analyze, add `'rank_math_analysis' => true` to the field:

```php
[
    'name' => 'My custom editor',
    'id'   => 'custom_content',
    'type' => 'wysiwyg',
    'rank_math_analysis' => true,
],
```

The plugin supports all types of fields, such as text, textarea and wysiwyg.

This is the video tutorial:
