---
title: Renaming taxonomy without losing assigned posts with Meta Box - Meta Box Documentation
source: https://docs.metabox.io/tutorials/rename-taxonomy-without-losing-data/
---

Assuming that you already have a taxonomy with posts assigned to it. However, in some cases, you may want to rename that taxonomy for SEO purposes or to make it more meaningful. Normally, if you rename a taxonomy, WordPress treats it as a completely new one. As a result, all previously assigned posts will be detached and no longer linked to their terms.

But in this tutorial, we’ll do it differently. We’ll **rename the taxonomy in a way that keeps all existing assignments intact**, so the posts remain connected just as before; no need to reassign anything manually.

![result](https://docs.metabox.io/assets/images/result-3f1446def3fcd75473aa4df834c9356e.gif)

Let’s see how to do that.

## Video version

## Preparation

For this practice, we only need the free version - [Meta Box Lite](https://metabox.io/lite/) to have the framework and [MB Custom Post Type](https://metabox.io/plugins/custom-post-type/) for creating custom post types and taxonomies.

For demonstration purposes, I’ll create a sample post type and taxonomy so you can clearly see how the relationships behave before and after renaming.

## Creating a custom post type & taxonomy

First, go to **Meta Box** > **Post Types** to create a custom post type for hotels as an example.

![post type](https://docs.metabox.io/assets/images/post-type-f0f42de26ed3c984fb289cda44a89fa4.png)

Next, still in the **Meta Box** screen, create a new taxonomy for location information.

![taxonomy](https://docs.metabox.io/assets/images/taxonomy-42ee1dfaf4f82e57914c6f39f0113290.png)

In the **Advanced** tab, pay attention to this setting. It’s available when you activate the **MB Admin Columns** extension. It’s optional, so I did not mention it before. When you check it, there’ll be a column in the dashboard to show the hotel’s location so that you can compare the results conveniently.

![associated post type](https://docs.metabox.io/assets/images/show-admin-column-option-55efb9aca654d4933b816e5ef361db84.png)

Back to the **General** tab, in the **Associated post type** section, choose the Hotel to assign the custom taxonomy that we’ve created to that post type.

![associated post types](https://docs.metabox.io/assets/images/associated-post-type-35e396a8dd8af4c2246b3152c53eaebb.png)

Let’s create each term for that taxonomy.

![terms](https://docs.metabox.io/assets/images/terms-85f9c39146c99951689483dcb093dcee.png)

Now, in the post editor of the Hotel post type, we’ll see the taxonomy section, where we can enter the hotel location.

![taxonomy section](https://docs.metabox.io/assets/images/taxonomy-section-ddb5e158ab8d28829db76795e2374060.png)

Just fill in all the information.

These are some posts, for example, that I created. The locations as well as the taxonomy are also displayed in the admin dashboard. Everything works normally at this stage.

![all-posts](https://docs.metabox.io/assets/images/all-posts-55ba0e3515b1aae8a02efd0dca404844.png)

## Renaming taxonomy without losing assigned posts

Now let’s say we want to rename the taxonomy from Location to Address to make it clearer and more SEO-friendly.

I change the taxonomy slug from `location` to `address`.

![Change slug](https://docs.metabox.io/assets/images/change-taxonomy-slug-380582db2373ab318e2f08518828c9c0.png)

After saving, you’ll notice that the terms previously created under the Location taxonomy no longer appear. When going back to the posts, all assigned terms disappear.

![Terms disappear](https://docs.metabox.io/assets/images/terms-dissapear-7c93326db67791ce9973a327cff02321.png)

The hotels are no longer connected to their locations. This happens because WordPress treats address as a brand-new taxonomy, even though the old relationships still exist in the database.

So instead of reassigning everything manually, we’ll reconnect the data using a small piece of code. Now, go to the theme file editor and add the following code.

![theme file editor](https://docs.metabox.io/assets/images/add-code-to-theme-file-7f6855a23490383a42173c3e01dc87ea.png)

```php
function rename_taxonomy_location_to_address() { 
    global $wpdb;
    $wpdb->query( "UPDATE $wpdb->term_taxonomy SET taxonomy = 'address' WHERE taxonomy = 'location'" );
}
rename_taxonomy_location_to_address();
```

**In there**:

```php
function rename_taxonomy_location_to_address() {
```

This one is to declare a function.

The `global $wpdb` variable allows us to access the WordPress database.

Most importantly, the following line finds all terms that belong to the location taxonomy and converts them to addresses.

```php
$wpdb->query( "UPDATE $wpdb->term_taxonomy SET taxonomy = 'address' WHERE taxonomy = 'location'" );
```

Finally, we run the function.

```php
rename_taxonomy_location_to_address();
```

That’s all for the code. Note that this code should run only once. After confirming that everything works correctly, remove the code immediately.

![result](https://docs.metabox.io/assets/images/result-3f1446def3fcd75473aa4df834c9356e.gif)

You’ll see that all posts have their taxonomy terms back. The taxonomy now has the new name, but the terms remain exactly as before. That’s how you rename a taxonomy without losing assigned data.

If you also want to do a similar [migration with custom fields](https://docs.metabox.io/tutorials/change-id-meta-box-field/), we already have a dedicated tutorial for that. You can check it out to learn how to change field IDs without losing existing values.
