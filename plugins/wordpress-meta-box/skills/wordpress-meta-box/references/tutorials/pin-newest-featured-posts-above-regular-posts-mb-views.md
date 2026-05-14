---
title: Pining newest featured posts above regular posts using MB Views - Meta Box Documentation
source: https://docs.metabox.io/tutorials/pin-newest-featured-posts-above-regular-posts-mb-views/
version: 5.12.0
fetched: 2026-05-11
---

In the previous tut, we focused on [displaying only the featured posts](show-featured-restaurants-mb-views.md). But in many real-world cases, highlighting important content without hiding the rest is a common need. Instead of splitting featured items into a separate section, you can simply prioritize them within the same list for better visibility. In this tutorial, we’re going to explore how to do it using the **MB Views** extension of **Meta Box**.

![result](https://docs.metabox.io/assets/images/result-6fc1ad2cc49436dbcac50fae59f910ff.png)

## Video version

## Preparation

In this tutorial, we’ll create a custom post type to manage all the tours on our travel website. Each tour will include essential information, such as price, duration, and whether it’s featured for the month. All details will be stored in custom fields created with Meta Box.

So I recommend using [Meta Box AlO](show-featured-restaurants-mb-views.md), which includes the framework and all extensions you’ll need for this setup.

- [MB Admin Columns](https://metabox.io/plugins/mb-admin-columns/): help you show whether a tour is marked as featured directly in the dashboard, making it easy to quickly scan and manage which tours should be pushed to the top;
- [MB Custom Post Type](https://metabox.io/plugins/custom-post-type/): create a custom post type for tours;
- [MB Views](https://metabox.io/plugins/mb-views/): create a template and control the logic that displays featured tours first.
- [MB Builder](https://metabox.io/plugins/meta-box-builder/): help you create the custom information for each tour, such as price, duration, and the featured status.

## 1\. Creating a new custom post type and custom fields

For this tutorial, I’ve already prepared a custom post type called **Tours** to store all the tour packages on the travel website. Each tour is saved as a post inside this post type, making it easy to manage and display them later with MB Views.

![create post type](https://docs.metabox.io/assets/images/custom-post-type-520e1997d9276fda69b8167ef91e3294.png)

I also created a custom field group to store all the essential information for each tour.

![Field group](https://docs.metabox.io/assets/images/field-group-a7c2dbdbb55de032c905d1e7f5e26bc0.png)

You can see some fields. Pay attention to an important field called ‘The Trend of Month\*\*\*\*’. We use the **Checkbox** field type so that you can easily tick it whenever you want to highlight a tour.

![Trend of month field](https://docs.metabox.io/assets/images/trend-of-month-field-b63e3ff7b91dbb422961be39ed21e767.png)

For this field, I enabled the **Admin Column** feature. With the **MB Admin Columns** extension activated, it allows me to quickly see whether a tour is marked as featured directly from the post list.

![Set admin column](https://docs.metabox.io/assets/images/set-admin-collumn-4e8b0006f4b8501f0f51466977968b71.png)

You can create any other fields you need depending on the information you want to display for each tour. Once everything is set up, move to the **Settings** tab and set the **Location** as **Post Type**. Choose **Tours** to ensure that the custom fields appear only for tour posts.

![Set location](https://docs.metabox.io/assets/images/set-location-1d0349047fdb63599c07ae483a0f336f.png)

Now, all the fields we’ve created will appear right under the post editor, and you can start filling in the tour details right away.

![Fields in post editor](data:image/png;base64,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)

The featured status is now visible in the admin dashboard, making it very convenient to manage highlighted tours.

![The trend of month in admin dashboard](https://docs.metabox.io/assets/images/trend-of-month-in-admin-cef1f3515b0dfa80978f6a2166cc23e2.png)

## 2\. Showing the tour listing on the page

Before displaying the newest featured posts at the top of the page, we first need to show all the tours.

First, create a new page specifically for the tour listings.

![create page](https://docs.metabox.io/assets/images/tour-page-d90700f1baa2f430f5f68dadd6f905d5.png)

Next, go to **Meta Box** > **MB Views** and create a new template for this page.

![Create template](https://docs.metabox.io/assets/images/create-template-fd1a5a8938fb01779756ee1c7dd6493c.png)

With **MB Views**, you can add some lines of code directly in the **Template** tab to query and retrieve all posts from the **Tours** post type. To display the tour information from your custom fields, simply click the **Insert Field** button and select any fields from the right sidebar, especially the **Trend of Month** field, which we’ll use in the next step to pin featured tours at the top.

![Insert fields](https://docs.metabox.io/assets/images/insert-fields-745c8082d34f77609de35557e2c92d2a.png)

After inserting all the fields, move to the **Settings** section to set where this template will appear. Set the **Type** to **Singular**, and choose the page you created for the tour listings.

![Set template location](https://docs.metabox.io/assets/images/set-template-location-6a0408081e1fae5a8cc6ca6b01f5dbe3.png)

On the frontend, you’ll see all the tour information displayed. At this stage, it appears as a basic list without any styling.

![result before styling](https://docs.metabox.io/assets/images/result-before-styling-fd703635c8941bbaa167820596e734f2.png)

To make it look more visually appealing, add some div tags and classes in the **Template** tab, then switch to the **CSS** tab to style the layout.

![Add css](https://docs.metabox.io/assets/images/Add-css-5e5a476d78cabe104016b05d84605813.png)

```markdown
.restaurant-wrapper {
    padding: 20px 0;
    font-family: Arial, sans-serif;
}

.below-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
}

.card-grid-item {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #eee;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform .15s, box-shadow .15s;
}

.card-grid-item .thumb {
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
}

.card-grid-item .thumb img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.card-grid-item .info {
    padding: 10px;
}

.card-grid-item .title {
    margin: 0;
    font-size: 16px;
    color: #222;
}

.card-grid-item:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.06);
}

.card-grid-item .title a,
.featured-large-card .title a {
    text-decoration: none;
}

.tour-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 6px;
    font-size: 14px;
    color: #444;
}

.tour-meta .duration {
    font-weight: 500;
    font-size: 17px;
    font-style: italic;
}

.tour-meta .price {
    font-weight: 700;
    color: #e35858;
    font-size: 18px;
}
```

Now, the tour listings look much better. Let’s move on to displaying the newest featured tours appearing first on the page.

![Tour after styling](https://docs.metabox.io/assets/images/tour-after-styling-79187b8f090c9a2013705febbbd23c47.png)

## 3\. Displaying newest featured tours first

Back to the template created with **MB Views**, we’ll add a small piece of logic to control the display order by adding some code, so the featured tours appear first, without duplicating any posts.

![add code to pin featured posts](https://docs.metabox.io/assets/images/add-code-pin-featured-posts-101c4a9588702035d62ba743be7271a1.png)

**In there**:

```php
{% set trending_posts = [] %}
{% set normal_posts = [] %}
```

Two empty arrays to categorize the tours: one for Hot Trend tours and one for regular tours.

We loop through all the tours from the existing query to process them one by one.

```php
{% for post in posts %}
```

Inside the loop, we check the value of the **Trend of Month** field. If it’s set to 1, it means this tour is marked as a Hot Trend, so we add it to the trending posts array. Otherwise, the tour is treated as a normal one and pushed into the normal posts array.

```php
{% if post.the_trend_of_month == '1' %}
    {% set trending_posts = trending_posts | merge([post]) %}
{% else %}
    {% set normal_posts = normal_posts | merge([post]) %}
{% endif %}

{% set top_trending = trending_posts[:3] %}
{% set remaining_trending = trending_posts[3:] %}
```

This code is to split the Hot Trend posts into two groups. The first three latest Hot Trend posts are used at the top of the page, while the remaining featured posts are pushed down and displayed together with the normal tours. You can easily change this number to control how many featured tours appear at the top.

This line below combines the two lists into one.

```php
{% set normal_posts = remaining_trending | merge(normal_posts) %}
```

We use the following code to display the featured tours at the top of the page. I did modify the code a bit so that the specified tour posts have a highlighted layout, with the number of columns adjusting dynamically based on how many featured items we have. Each featured tour is highlighted with a Hot Trend badge to make it stand out from the rest.

```php
<div class="featured-top-row columns-{{ top_trending|length }}">
    {% if top_trending|length > 0 %}
        {% for post in top_trending %}
            <div class="featured-large-card">
                <a class="thumb" href="{{ post.link }}">
                    <img src="{{ post.thumbnail.full.url }}" alt="{{ post.thumbnail.full.alt }}" loading="lazy">
                </a>
                <div class="info">
                    <span class="badge">Hot Trend</span>
                    <h3 class="title"><a href="{{ post.url }}">{{ post.title }}</a></h3>
                    <div class="tour-meta">
                        <span class="duration">{{ post.duration.value }}</span>
                        <span class="price">{{ post.price }}$</span>
                    </div>
                </div>
            </div>
        {% endfor %}
    {% endif %}
</div>
```

And, this code below stays unchanged for displaying normal posts as we did before.

```php
<div class="below-grid">
    {% for post in normal_posts %}
        <div class="card-grid-item">
            <a class="thumb" href="{{ post.link }}">
                <img src="{{ post.thumbnail.full.url }}" alt="{{ post.thumbnail.full.alt }}" loading="lazy">
            </a>
            <div class="info">                    
                <h4 class="title"><a href="{{ post.url }}">{{ post.title }}</a></h4>
                <div class="tour-meta">
                    <span class="duration">{{ post.duration.value }}</span>
                    <span class="price">{{ post.price }}$</span>
                </div>
            </div>
        </div>
    {% endfor %}
</div>
```

Turn to the **CSS** tab and add styles to make the highlight section look cleaner.

```markdown
.featured-top-row {
    display: grid;
    gap: 20px;
    margin-bottom: 24px;
}

.featured-top-row.columns-1 {
    grid-template-columns: 1fr;
}

.featured-top-row.columns-2 {
    grid-template-columns: repeat(2, 1fr);
}

.featured-top-row.columns-3 {
    grid-template-columns: repeat(3, 1fr);
}

.featured-top-row.columns-4 {
    grid-template-columns: repeat(4, 1fr);
}

.featured-large-card {
    background: #fff;
    border: 2px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    min-height: 260px;
    transition: transform .18s, box-shadow .18s;
}

.featured-large-card.empty {
    background: transparent;
    border: 2px dashed #eee;
    display: block;
    min-height: 260px;
}

.featured-large-card .thumb {
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
}

.featured-large-card .thumb img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.featured-large-card .info {
    padding: 14px;
    flex: 1;
}

.featured-large-card .badge {
    display: inline-block;
    background: #00c1b3;
    color: #fff;
    padding: 6px 10px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 10px;
}

.featured-large-card .title {
    margin: 0 0 8px;
    font-size: 20px;
    line-height: 1.15;
}

.featured-large-card .excerpt {
    margin: 0;
    color: #555;
    font-size: 14px;
}

/* Hover */
.featured-large-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

@keyframes blink {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0.4;
    }
}

.featured-large-card .badge {
    animation: blink 1s infinite;
}

@keyframes shake {
    0% {
        transform: rotate(0deg);
    }

    25% {
        transform: rotate(5deg);
    }

    50% {
        transform: rotate(-5deg);
    }

    75% {
        transform: rotate(3deg);
    }

    100% {
        transform: rotate(0deg);
    }
}

.featured-large-card .badge {
    display: inline-block;
    animation: shake 0.8s infinite;
}

@keyframes zoom {

    0%,
    100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.2);
    }
}

.featured-large-card .badge {
    display: inline-block;
    animation: zoom 1s infinite;
}

.featured-large-card .badge {
    display: inline-block;
    background: #00c1b3;
    color: #fff;
    padding: 6px 10px;
    border-radius: 4px;
}

.featured-large-card .badge {
    display: inline-block;
    font-size: 13px;
    font-weight: 700;
    color: #e35858;
    background: transparent;
    border: 1px solid #e35858;
    border-radius: 3px;
    padding: 2px 6px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

@keyframes ticker {

    0%,
    100% {
        transform: scale(1) translateX(0);
    }

    50% {
        transform: scale(1.1) translateX(2px);
    }
}

.featured-large-card .badge {
    animation: ticker 1s infinite;
}
```

It looks nice now; Hot Trend posts show at the top, but they also appear in the normal list below.

![Featured-post-at-top](https://docs.metabox.io/assets/images/duplicated-featured-post-at-top-fba48fb2e139a5f64aeb06601cafda1b.png)

We need to remove these duplicates.

Back to the template with **MB Views**. Currently, the posts array contains all posts, including those already shown at the top. To avoid duplicates, we replace it with normal posts, which include regular posts plus any Hot Trend posts not featured at the top.

![remove duplication](https://docs.metabox.io/assets/images/remove-duplication-5154a419f746738126c02b3afc60105b.gif)

For example, if we have 5 Hot Trend posts but only show 3 at the top, the remaining 2 are displayed below without repeating.

That’s all for the code. I’ve put everything on [Github](https://github.com/wpmetabox/tutorials/tree/master/pin-newest-featured-posts), so you can check it out there.

Now the featured posts are displaying as intended, without any duplicates

![Result](https://docs.metabox.io/assets/images/result-6fc1ad2cc49436dbcac50fae59f910ff.png)

You can go to the backend and change a post’s Featured status to test if it works correctly.
