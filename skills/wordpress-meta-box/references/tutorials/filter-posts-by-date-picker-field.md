---
title: Filtering posts by date picker field - Meta Box Documentation
source: https://docs.metabox.io/tutorials/filter-posts-by-date-picker-field/
---

In this tutorial, we’ll show you how to **filter posts on the front end using a date picker custom field** with Meta Box. This is ideal for time-sensitive content such as events or movie schedules, allowing visitors to quickly find posts by a specific date or within a date range.

![result](https://docs.metabox.io/assets/images/result-73e2ff6d4c09ba4ff0585978d782657c.gif)

## Video Version

## Preparation

In this tutorial, we’ll create a custom post type to manage all the films in our cinema schedule. Each movie will have its own details, such as genres, show date, and showtimes, which we’ll store in custom fields created with Meta Box.

So I recommend using [Meta Box AIO](https://metabox.io/aio/), which includes the framework and all extensions.

## Creating a new custom post type

As I mentioned, we’ll start by creating a new custom post type called **Movies** to store the films. Each movie will be saved as a post in this post type.

Now, go to **Meta Box** > **Post Types** to create a new custom post type for the movies. After publishing, you’ll see the created custom post type in the dashboard’s menu.

![create movie post type](https://docs.metabox.io/assets/images/create-movie-post-type-c329296189479c271c1719e532ec0bbc.png)

## Creating custom fields for movies

Now, we’ll create some custom fields to store information for each movie.

These fields will include details like genres, show dates, and showtimes, everything we need for the movie listings. We’ll make the movie schedule as a group to keep things more organized.

![Fields in post editor](https://docs.metabox.io/assets/images/fields-in-post-editor-65f9307a76b7c6db2c8ad2dfce9d9f00.png)

The most important one in this tutorial is the Date Picker field for the show date. This is what we’ll later use to filter movies on the front end.

Now, go to **Meta Box** > **Custom Fields** to create a new field group.

![Create field group](https://docs.metabox.io/assets/images/create-field-group-8031ba8284f46242b9a5a3b9572336fe.png)

First, choose the **Select Advanced** field for movie genres. Add some choice in the **Choices** box. And you can also enable multiple selections so that each movie can belong to several genres at once.

![Genre field](https://docs.metabox.io/assets/images/genre-field-c5fec6f80530a23c44198449ee714cca.png)

Next, create another field called Movie Schedule, which contains the date and time information. Here, we’ll use a **Group** field to keep related fields together. And turning on the **Admin column** for this group. It’s available when you have the **MB Admin Column** extension activated. Thus, I can quickly view movie schedules directly in the post list

![Group field](https://docs.metabox.io/assets/images/group-field-5e260d5f2dbef3a0afb12f20f5213e30.png)

Inside this group, add a **Date Picker** field for the date. Then, go to the **Advanced** tab and set the **minDate** option to “ **today** ”. This way, you can’t select past dates.

![Date field setting](https://docs.metabox.io/assets/images/date-field-setting-1c62ef2ba13058529661bdb10a5b4525.png)

After that, select the **Time Picker** field for the time. Since each movie might have multiple showtimes on the same day, enable the **Cloneable** option for this field.

![Time field](https://docs.metabox.io/assets/images/time-field-82f0321e9e3e5afd937cb6a9bac50cec.png)

Once done, move to the **Settings** tab and set the **Location** as **Post Type**. Choose **Movies** to ensure that the custom fields appear only for movie posts.

![Field group location](https://docs.metabox.io/assets/images/field-group-location-4c9f3f97f07af8459ec5c846e6fe8858.png)

Now, you’ll see all the fields we’ve just created displayed under the post editor. You can now fill in movie details.

![Fields in post editor](https://docs.metabox.io/assets/images/fields-in-post-editor-65f9307a76b7c6db2c8ad2dfce9d9f00.png)

The movie schedules are now visible here in the admin dashboard.

![Field in admin dashboard](https://docs.metabox.io/assets/images/field-in-admin-dashboard-b3bdd3972949a2a977e7deff0f092fd2.png)

## Showing posts on the page

Before adding the date filter, we first need to make sure that the specific page can already display all the movies.

First, create a new page especially for the cinema schedule.

Next, go to **Meta Box** > **MB Views**, and create a new template specifically for this page.

![Create a template.](https://docs.metabox.io/assets/images/create-template-ae3fca4c02be9c4f877fade315e0dbb7.png)

With **MB Views**, I get all movie posts by adding some code in the **Template** tab.

![Get all posts by adding code](https://docs.metabox.io/assets/images/add-code-get-all-posts-624b0621101649685252745a5b966c1e.png)

**In there**:

```php
{% set args = { post_type: 'movie', posts_per_page: -1, orderby: 'date', order: 'ASC' } %}
```

This whole line is used to query and display posts from a specific post type, sorted by publish date. Particularly, it declares that we’ll get posts from the post type with the `movie` slug. And, `posts_per_page: -1` helps fetch all posts in that post type. You can change the number to get the expected number of posts.

Then, I display each movie’s details, especially the date fields for later filtering. I simply click the **Insert Field** button and choose the fields I need.

![Insert fields in the template with view](https://docs.metabox.io/assets/images/insert-field-views-89b665c3db86acab06ff013bd4dbfa22.png)

After inserting all the fields, move to the **Settings** section to set where this template will appear. Set the **Type** as **Page**, and choose the location as the page you created earlier for the movie listings.

![Template setting](data:image/png;base64,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)

On the frontend, view the page, and you’ll see all the movie information displayed. However, it appears as a basic list without any styling for now. To make it look more visually appealing, we need to apply some styling.

![Information display without styling](https://docs.metabox.io/assets/images/infor-displays-no-styling-ae60d2b3019c1943cbeae4593883f861.gif)

Back to the **Template** tab, add some div tags and classes for styling. And modify the code.

![Add classes and div](https://docs.metabox.io/assets/images/add-div-classes-b2b480364a6dfa1c53834f6362b8cc2f.png)

Move to the **CSS** tab to add some lines of code.

```markdown
.movie-list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 35px 20px;
}

.movie-item {
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 3px 10px rgba(0, 0, 0, .08);
    transition: transform .2s ease, box-shadow .2s ease;
    padding-bottom: 14px;
}

.movie-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, .12);
}

.movie-thumb {
    position: relative;
    width: 100%;
    aspect-ratio: 16/9;
    overflow: hidden;
    background: #eef1f4;
    border-bottom: 1px solid #eef2f7;
}

.movie-thumb img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.movie-title {
    font-size: 18px;
    font-weight: 700;
    color: #213;
}

.movie-title a {
    text-decoration: none;
    color: #282828;
}

.genres {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.genre {
    padding: 0px 10px;
    background: #e6e7e9;
    color: #213;
    font-size: 13px;
    font-weight: 500;
    border-radius: 6px;
}

.movie-content {
    padding: 20px 10px 0px;
    line-height: 2.0
}

.showtimes {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 5px 0;
}

.showtime {
    padding: 0px 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    background: #d14141;
    color: #fff;
    cursor: pointer;
}

.movie-date {
    font-size: 15px;
    color: #32abb9;
    font-weight: 700;
}
```

![Add css for styling](https://docs.metabox.io/assets/images/add-css-styling-23c49e7db681985f71c8af1e6e39a101.png)

Now, the movie listings look much better. Let’s move on to creating the search box and adding the date filter.

## Filtering posts by date picker

Back to the template created by **MB Views**, let’s add some more code to display the search box and filter options for the movie listings.

```php
<div class="filters">
    <div class="filter-inputs">
        <label>From Date: <input type="date" id="from-date"></label>
        <label>To Date: <input type="date" id="to-date"></label>
        <label class="specific-date">Specific Date: <input type="date" id="specific-date"></label>
    </div>
    <button id="clear-filters" type="button">Clear All Filters</button>
</div>
```

**In there**:

```php
<label>From Date: <input type="date" id="from-date"></label>
<label>To Date: <input type="date" id="to-date"></label>
<label class="specific-date">Specific Date: <input type="date" id="specific-date"></label>
```

We add three date inputs: **From Date**, **To Date**, and **Specific Date**. They let users pick days directly from a calendar to filter the movies. For example, you can choose a range of days or just one specific day to see which movies are showing. Each input has an ID, so we can later handle them in JavaScript.

```php
<button id="clear-filters" type="button">Clear All Filters</button>
```

This line of code is to add the **Clear All Filters** button to reset the date filters with one click, so you can start a new search easily.

Turn to the CSS tab and add styles to make the search section look cleaner.

```markdown
.filters {
    border-radius: 12px;
    padding: 15px;
    background: #f1f1f180;
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin: 20px 0 35px;
}

.filter-inputs {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

.filters label {
    display: flex;
    flex-direction: column;
    font-weight: 600;
    font-size: 16px;
    gap: 6px;
}

#clear-filters {
    align-self: flex-start;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
    background: #a3372c;
    color: #fff;
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
    transition: background 0.2s ease;
}

#clear-filters:hover {
    background: #81281e;
}

#clear-filters:active {
    background: #051325;
}

label.specific-date {
    margin-left: 150px;
}
```

It looks nice now, but we still need to make it work.

![Filter doesn’t work](https://docs.metabox.io/assets/images/filter-not-work-8bd334cac719b27e9ad60a58415d895d.gif)

In the template again, add the line of code below to load the **jQuery** library to make it easier to write JavaScript for the filter later.

```php
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
```

And, I add the following code to assign the date field value in the ‘ **Y-m-d** ’ format to the data-date attribute. Since both the movie date and the date filter input return the same year-month-day format, it’s easy to compare them.

```php
<div class="movie-item" data-date="{{ post.movie_schedule.date | date( 'Y-m-d' ) }}">
```

![Date format](https://docs.metabox.io/assets/images/date-fomat-5e976d12b8ea7904c9f634730ca06be9.png)

Now, switch to the **JavaScript** tab, add the main script to handle the filtering of the posts.

```js
jQuery(function ($) {
    var $from = $('#from-date');
    var $to = $('#to-date');
    var $spec = $('#specific-date');
    var $items = $('.movie-item');

    $from.on('change', function () {
        $spec.val('');

        if (this.value) {
            $to.attr('min', this.value);
        } else {
            $to.removeAttr('min');
        }

        applyFilter();
    });

    $to.on('change', function () {
        $spec.val('');
        if (this.value) {
            $from.attr('max', this.value);
        } else {
            $from.removeAttr('max');
        }
        applyFilter();
    });

    $spec.on('change', function () {
        $from.val('').removeAttr('max');
        $to.val('').removeAttr('min');
        applyFilter();
    });

    $('#clear-filters').on('click', function (e) {
        e.preventDefault();

        $from.val('').removeAttr('max');
        $to.val('').removeAttr('min');
        $spec.val('');
        $items.show();
    });

    function applyFilter() {
        var from = $from.val();
        var to = $to.val();
        var spec = $spec.val();

        $items.each(function () {
            var d = $(this).data('date');
            var show = true;

            if (spec) {
                show = (d === spec);
            } else {
                if (from) {
                    if (d < from) {
                        show = false;
                    }
                }
                if (to) {
                    if (d > to) {
                        show = false;
                    }
                }
            }

            $(this).toggle(show);
        });
    }
});
```

![Add Javascript](https://docs.metabox.io/assets/images/add-javascript-18501e37f41d57b1f1be10f5d2463e8e.png)

Go through it in more detail.

```js
var $from = $('#from-date');
var $to = $('#to-date');
var $spec = $('#specific-date');
var $items = $('.movie-item');
```

This part initializes variables for selecting the start date, end date, specific date, and all post items.

```js
$from.on('change', function () {
    $spec.val('');

    if (this.value) {
        $to.attr('min', this.value);
    } else {
        $to.removeAttr('min');
    }

    applyFilter();
});
```

When the user picks a start date, the specific date field is automatically cleared. Then, the end date input is limited; you can’t choose a date earlier than the start date. If the start date is cleared, that restriction is removed. And finally, the script calls the `applyFilter()` function to update the filtered movie list.

As the user picks a to-date, it does the same as before. Just the reverse of the from-date logic. It clears the specific date and adjusts the date limit.

```js
$to.on('change', function () {
    $spec.val('');
    if (this.value) {
        $from.attr('max', this.value);
    } else {
        $from.removeAttr('max');
    }
    applyFilter();
});
```

If a specific date is chosen instead, it clears both the start and end dates, removes any date limits, and then calls the created function to update the results.

```js
$spec.on('change', function () {
    $from.val('').removeAttr('max');
    $to.val('').removeAttr('min');
    applyFilter();
});
```

When the user clicks “Clear All Filters,” it resets all date selections to default, removes any date limits, and shows all posts again, just like before filtering.

```js
$('#clear-filters').on('click', function (e) {
    e.preventDefault();

    $from.val('').removeAttr('max');
    $to.val('').removeAttr('min');
    $spec.val('');
    $items.show();
});
```

At this point, the script below retrieves the current values of the start, end, and specific date fields so it knows which filters are active.

```js
var from = $from.val();
var to = $to.val();
var spec = $spec.val();
```

We use `$items.each(function () {}` loops through each post item to check one by one whether the post should be visible based on the selected dates.

We get the date value from the post’s data-date attribute.

```js
var d = $(this).data('date');
```

This gives JavaScript the exact date of each post to compare with the selected filters.

`var show = true;` is to set a variable to indicate that each post is visible by default.

If a specific date is chosen, only posts with the same date are shown. Otherwise, if the post’s date is earlier than the start date, it’s hidden. Similarly, if the post’s date is later than the end date, it’s also hidden.

```js
if (spec) {
    show = (d === spec);
} else {
    if (from) {
        if (d < from) {
            show = false;
        }
    }
    if (to) {
        if (d > to) {
            show = false;
        }
    }
}
```

After these checks, the last script updates the display, showing posts that meet the filter conditions and hiding those that don’t.

```js
$(this).toggle(show);
```

That's all for the code, you can refer it [here](https://github.com/wpmetabox/tutorials/tree/master/filter-posts-by-date-picker).

On the frontend, pick the date you want to filter, and then only the movies on that date will be returned and displayed on the page.

![result](https://docs.metabox.io/assets/images/result-73e2ff6d4c09ba4ff0585978d782657c.gif)

You can also refer to other Meta Box filtering tutorials, such as [filtering by taxonomy](https://metabox.io/filter-posts-by-taxonomy-mb-views/), [relationships](https://metabox.io/filter-posts-by-relationshipd-mb-views/), or multiple conditions to build more advanced and flexible search experiences. Happy building with Meta Box!
