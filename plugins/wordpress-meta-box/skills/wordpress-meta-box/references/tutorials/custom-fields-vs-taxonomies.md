---
title: Custom fields vs custom taxonomies - Meta Box Documentation
source: https://docs.metabox.io/tutorials/custom-fields-vs-taxonomies/
version: 5.12.0
fetched: 2026-05-11
---

With the help of [Meta Box](https://metabox.io/), today you can easily create both custom fields and custom taxonomies to store data for the custom post types. However, many users may be confused about when they should use each of them. Let’s clarify it.

## Why are custom fields and taxonomies necessary?

Since version 3.0, WordPress gives you the capability to add your own custom post types and to use them in different ways. Your website can contain more content types than just "post". They can be "listing" for a real estate website, "product" for an e-commerce website, or "hotel" for a travel website.

When creating a listing, for example, the post title and content are not enough, **you may want to add more info such as area, location, and price for the listing**. That’s why we need to use custom fields and custom taxonomies to handle this problem.

## What's the difference between custom fields and taxonomies?

[Custom fields](https://metabox.io/what-is-custom-fields-in-wordpress/) are used to store arbitrary extra information for a post

**Custom taxonomies are utilized to group posts together**

Therefore, grouping is the main difference between these two things.

For example, I’m building a new site that has a custom post type for television shows. I have to identify which item of a TV show (including Title, Actors, Episode numbers, and Season numbers) makes sense as a taxonomy, which one is a custom field, or (rarely) both.

| Custom Taxonomy | Custom Field |
| --- | --- |
| Title | Yes | Yes | Each TV show has lots of episodes so you can group all of them together in a taxonomy, then people can see an episode listing. |
| Actors | Yes | Yes | Since actors act in many roles, it would be great to see what shows and episodes they’ve joined by grouping them into a taxonomy for actors. |
| Season / Episode | No | Yes | Every TV series has a season 1 so it doesn’t make sense if we group season 1 of all TV shows into a taxonomy. It should be a post meta only. |

In conclusion:

- Use custom fields if you want to add extra data to a post. Use custom taxonomies if that data is utilized to group posts together.
- Custom fields are bits of information that are specific to the post item itself. Taxonomies are bits of information shared by many different items.

### Querying posts

You can make a complex query and get your desired posts by using the meta query (with custom fields) and `tax_query` (with custom taxonomies).

There are 2 different things between querying posts by custom fields and custom taxonomies:

1. **You can order posts by custom fields, not by taxonomies.**

This is due to the way WordPress saves data. With custom fields, it saves both meta keys and values, thus you can order by values. With taxonomies, it saves only the key (`term_id`) which is a reference to the terms table.

Simply understand that custom fields are added to posts and are considered a part of posts, so you can order them by that. Conversely, taxonomies are groups of posts, thus it doesn’t make sense if you order posts by taxonomy since each term has a group of posts.

2. **Querying posts by taxonomy is faster than querying by custom fields.**

Taxonomies are built to organize things and provide a way of filtering down to a specific set of posts. Custom fields should only be used for information that isn't going to be searched or filtered for.

Since the taxonomy is a main front-end presentation feature in the WordPress core, queries by it are well optimized. Conversely, the value column in the custom field table is not indexed – so when you query posts by custom fields, it means that you are basically doing a search through data that is not intended for that purpose. Even when you add an index to the post meta table, it won't fix it.

## Front-end template

**Taxonomies have templates, whereas custom fields don’t**. This is the significant difference between them.

For custom taxonomies, WordPress supports various hierarchies of templates, namely `taxonomy-{taxonomy}-{term}.php`, `taxonomy-{taxonomy}.php`, `taxonomy.php`.

About custom fields, you don’t have that. You need to make a custom page template, then put a custom query to get posts and use a [helper function](https://docs.metabox.io/displaying-fields/) to show the info. You have to do a lot of work by yourself. And as mentioned before, if you have to query by custom fields, make sure you [avoid performance problems](https://vip.wordpress.com/documentation/querying-on-meta_value/).

## Conclusion

Although custom fields and custom taxonomies have the same main purposes, choosing to use which one may have long-term effects on your website. Making the right decision will help you save a ton of time when developing and using custom fields and custom taxonomies.

The following table can help in your decision-making:

| Question | Custom Fields | Custom Taxonomies |
| --- | --- | --- |
| Is the info specific/unique for the post? | Y | N |
| Is the info used for display purposes only? | Y | N |
| Do you order posts by that info? | Y | N |
| Is the info shared between posts? | N | Y |
| Is the info reusable? | N | Y |
| Do you need to manage (add, edit, remove) the values? | N | Y |
| Do you need hierarchical values? | N | Y |
| Do you need to browse posts by value? | N | Y |
| Do you need to search by the value? | N | Y |
| Do you need to filter by the value? | N | Y |
| Do you need a template in the front-end? | N | Y |
