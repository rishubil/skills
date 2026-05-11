---
title: Migrating data when switching from cloneable fields to groups - Meta Box Documentation
source: https://docs.metabox.io/tutorials/migrate-data-switching-from-cloneable-fields-to-groups/
---

Learn how to safely migrate existing data when switching from cloneable fields to a Group field in Meta Box, so you can upgrade to a more structured setup without losing any information.

![result](https://docs.metabox.io/assets/images/gif%20result-8efbed1c543e93f1bfc852c6f3ab7785.gif) result

## Video version

## Preparation

For this guide, we naturally use Meta Box to create custom fields and a post type. Since the goal is to switch the field to a group structure, some premium Meta Box extensions are required. For convenience, we recommend using Meta Box AlO, which includes the framework and all extensions. In this case, I already have a custom post type called Events, along with a custom field created for it. The field is currently set as cloneable to add multiple speakers.

![cloneable field](https://docs.metabox.io/assets/images/cloneable-field-e336adce5e0c1a200b3b817314e8e192.png)

Fill in the information in post editor.

![cloneable field in post editor](data:image/png;base64,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)

Now, convert it to a group field type to store multiple related pieces of information.

## Migrating data from cloneable fields to groups

In real-world scenarios, you may need to group related information to create a better structure. Instead of storing only the speaker name, I also want to add another piece of information, for example, an avatar.

So now, go back to the field editor and change the standalone cloneable field to a Group field.

![Group-field](https://docs.metabox.io/assets/images/change-group-field-2203417357a9ba5cbd21773537a616c1.png)

Then, add subfields you need. The most important subfield is the one that stores the speaker name because we’ll migrate the data from the old cloneable field into this new Group structure. And also add a field to store the speaker’s avatar.

![Subfield](https://docs.metabox.io/assets/images/subfields-1847797a724382bb940a6d2e1e80648e.png)

In the old post editor, you'll see that the Group field appears correctly. However, the speaker names we previously entered are no longer displayed. But again, the data is still in the database.

![(the speaker names we previously entered are no longer displayed](https://docs.metabox.io/assets/images/group-field-in-post-editor-08f58a3c1c3adc4fa233bb7da593e094.png)

So instead of re-entering everything manually, we’ll reconnect the data using a small piece of code. Go to the theme file editor and add the following code:

![Theme-file editor](https://docs.metabox.io/assets/images/theme-file-editor-9337b79b6d072c9277a77bb571b51065.png)

```php
add_action( 'admin_init', function () {
    if ( get_option( 'event_speaker_migrated' ) ) {
        return;
    }
    $query = new WP_Query( [
        'post_type'      => 'event',
        'posts_per_page' => 100,
        'post_status'    => 'any',
        'meta_query'     => [
            [
                'key'     => 'speaker',
                'compare' => 'EXISTS',
            ],
        ],
    ] );
    foreach ( $query->posts as $post ) {
        $old = get_post_meta( $post->ID, 'speaker', true );
        if ( empty( $old ) || is_array( $old[0] ) ) {
            continue;
        }
        $new = [];
        foreach ( $old as $name ) {
            $new[] = [
                'name'   => $name,
                'title'  => '',
                'avatar' => '',
            ];
        }
        update_post_meta( $post->ID, 'speaker', $new );
    }
    update_option( 'event_speaker_migrated', true );
} );
```

**Explanation**:

```php
add_action( 'admin_init', function () {

  if ( get_option( 'event_speaker_migrated' ) ) {
       return;
   }
```

I create a hook that runs when entering the WordPress admin area. This means the code only runs in the admin dashboard, not on the front end.

We next check whether the migration has already been executed:

If the option event speaker migrated exists, it means the migration already ran before, so we stop the process to prevent it from running again.

Then we query the Event posts. Here, we retrieve up to 100 posts of the event post type and only those that have the meta key as speaker.

```php
$query = new WP_Query( [
        'post_type'      => 'event',
        'posts_per_page' => 100,
        'post_status'    => 'any',
        'meta_query'     => [
            [
                'key'     => 'speaker',
                'compare' => 'EXISTS',
            ],
        ],
    ] );
```

We use speaker because that was the field ID of the original cloneable field. Next, we loop through each post:

```php
foreach ( $query->posts as $post ) {
```

We get the old data: This returns the entire array stored by the old cloneable field.

```php
$old = get_post_meta( $post->ID, 'speaker', true );
```

After that, we check whether the data is empty or already in group format.

```php
if ( empty( $old ) || is_array( $old[0] ) ) {
           continue;
       }
```

Next, we create a new empty array:

```php
$new = [];
```

Here, we convert the old array of strings into an array of structured objects that match the Group field format.

```php
foreach ( $old as $name ) {
    $new[] = [
        'name'   => $name,
        'title'  => '',
        'avatar' => '',
    ];
}
```

We update the post meta and overwrite the old structure:

```php
update_post_meta( $post->ID, 'speaker', $new );
}
```

After processing all posts, we save a small option in the WordPress database to mark that the migration is complete. This ensures the migration won’t run again the next time you enter the admin area.

```php
update_option( 'event_speaker_migrated', true );
} );
```

That’s all for the code. You can find the full code on GitHub. After confirming everything works correctly, make sure to remove the code to avoid unexpected problems later.

Refresh the post editor. You’ll see that the speaker names are back, this time inside the new Group structure.

![Data return](https://docs.metabox.io/assets/images/data-return-264e232b8f1ea3b15d30ae03f594d112.png)

From here, you can safely add avatars or any additional subfields without losing your existing data.

If you also need to [migrate data when changing field IDs](https://docs.metabox.io/tutorials/change-id-meta-box-field/), we have a dedicated tutorial for that. You can check it out to learn how to update field IDs without losing existing values.
