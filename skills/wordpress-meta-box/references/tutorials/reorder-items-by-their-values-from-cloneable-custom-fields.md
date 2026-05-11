---
title: Reordering items by their values from cloneable custom fields - Meta Box + Bricks - Meta Box Documentation
source: https://docs.metabox.io/tutorials/reorder-items-by-their-values-from-cloneable-custom-fields/
---

Today, we’ll **reorder items by their values from cloneable custom fields**. Imagine that you have a list of services, each with its own name and price, and you want to display them in order from the lowest to the highest. That’s exactly when this method comes in handy. In this tutotial, we’ll walk through a simple case study to show you how it’s done.

I created a car services pricing as an example. As you can see, this page contains the services and its price is sorted in ascending order. All of this information will be saved in the custom fields.

![I created a car services pricing as an example](https://docs.metabox.io/assets/images/demo-min-1838ffffa89413896605b293f06a28da.png)

In this practice, I’ll show you two different ways to do it. If you use a page builder, you can refer to the method with **Bricks**. In case you only use **Meta Box**, you can still do it with the support of **MB Views**. I will go into detail on both of these methods, so you can choose the most suitable method for yourself.

Let’s get started!

## Video Version

## Preparation

I will use a cloneable group for demonstration in this practice. So, I recommend that you should use [Meta Box AIO](https://metabox.io/aio/) to have the framework for creating custom fields. As well as the Meta Box extensions inside it provide you with advanced features, specifically:

- [MB Builder](https://metabox.io/plugins/meta-box-builder/): to have a UI on the backend to create custom fields easily;
- [MB Group](https://metabox.io/plugins/meta-box-group/): to organize custom fields into the groups.

If you don't use any page builder like I mentioned before, you will need [MB Views](https://metabox.io/plugins/mb-views/) to create a template for displaying prices information and create order cloneable fields by value.

Otherwise, **Bricks** is used to build the layout and create a real-time filtering system using query loops and dynamic data.

Now, let’s go step by step.

## 1\. Creating custom fields

To store car services details, we need to create a group of custom fields. They will cover key information such as services name and prices. Feel free to add additional fields depending on your needs.

Now, go to **Meta Box** > **Custom Fields**, and create a new field group. Here I created fields with this structure:

| Field | Types of Field | ID |
| --- | --- | --- |
| Services | Group | services |
| Service Name | Text | service\_name |
| Price | Number | price |

This is a group with 2 subfields inside. I also set this group as cloneable to have more spaces to add different services information.

![This is a group with 2 subfields inside. I also set this group as cloneable to have more spaces to add different services information](https://docs.metabox.io/assets/images/cloneable-min-750f076d63178ffbf7edb50365a9485e.png)

After saving, go to the page editor then you will see all of the custom fields. Just enter information for each service, you can press the **Add more** button to add another service for your needs.

![Just enter information for each service, you can press the Add more button to add another service for your needs](https://docs.metabox.io/assets/images/add-more-min-490f89f251162f3ceb1db56750dbfae0.png)

## 2\. Method 1: Reordering items by their values from cloneable custom fields with Bricks

Let's sort the car service pricing from low to high by using **Bricks**. I have displayed the information on page first, if you want to see the details, you can find it on this practice. As you can see, the list of services' names and prices is fully displayed, but it is not sorted in any order.

![As you can see, the list of services' names and prices is fully displayed, but it is not sorted in any order](https://docs.metabox.io/assets/images/before-min-e39e2932f348091c14976098a8f4a502.png)

Now I will arrange the value of the items as I want.

Since **Bricks** doesn't support sorting clonable field values directly, I need to use code to do it.

Now, go to **Appearance** > **Theme File Editor** to add some code functions:

```php
$target_field_id = 'services';
$sort_field = 'price';
$location = 'page';

add_filter( 'bricks/query/run', function( $results, $query_obj ) use ( $target_field_id, $sort_field, $location ) {
    $expected_object_type = 'mb_' . $location . '_' . $target_field_id;
    if ( $query_obj->object_type !== $expected_object_type ) {
        return $results;
    }
    if ( is_array( $results ) && ! empty( $results ) ) {
        usort( $results, function( $a, $b ) use ( $sort_field ) {
            return ( $a[$sort_field] ) <=> ( $b[$sort_field] );
        });
    }
    return $results;
}, 20, 2 );
```

![Now, go to Appearance > Theme File Editor to add some code functions](https://docs.metabox.io/assets/images/code-bricks-min-c9a3832c4f01b49d25b00fc0757185cd.png)

**Explanation**:

- `$target_field_id = 'services'`: is the ID of the group that I want to sort.
- `$sort_field = 'price'`: is the subfield of the group whose value I want to sort.
- `$location = 'page'`: is the location of the field group that is applied to.
- `add_filter( 'bricks/query/run', function( $results, $query_obj ) use ( $target_field_id, $sort_field, $location ) {`: is to add a function. It will help process the queried data above based on the declared variables.
- `$expected_object_type = 'mb_' . $location . '_' . $target_field_id`: is to create the name of the object type that I want Bricks to query from the Meta Box data. It is related to these two variables: `$location`; `$target_field_id`.
```php
if ( $query_obj->object_type !== $expected_object_type ) {
    return $results;
}
```

This part is to show that if the current query is not the query we want to intervene in, return the intact, unchanged result to avoid affecting other queries.

- `if ( is_array( $results ) && ! empty( $results ) ) {`: is to check if the data is an empty array or not.
```php
usort( $results, function( $a, $b ) use ( $sort_field ) {
    return ( $a[$sort_field] ) <=> ( $b[$sort_field] );
});
```

This part is to sort the values in the array of this subfield in ascending order.

Here is the front-end page after I sorted items by value. As you can see, these values are sorted in ascending order along with their corresponding service.

![Here is the front-end page after I sorted items by value](https://docs.metabox.io/assets/images/item13-before-min-0b9ec129443f6631ec0fe86ce80b4496.png)

The data of price can be dynamic, and the code still works well. For example, pay attention to this item.

![For example, pay attention to this item](https://docs.metabox.io/assets/images/item13-setting-min-3ceefe808218294fc0e52b1f65ea15c2.png)

Now, I change its value.

![Now, I change its value](https://docs.metabox.io/assets/images/item13-fix-min-ed216e96d8181b283f747a56eda1d72b.png)

Then, that item is moved up to the top. That’s the result I expected.

![Then, that item is moved up to the top](https://docs.metabox.io/assets/images/item13-after-min-960da24d75564d21b38efac06d257a5b.png)

## 3\. Method 2: Reordering items by their values from cloneable custom fields with MB Views

In the case that you don’t use any page builder, you can refer to this method. It is also simpler than the above method with the help of **MB Views** from **Meta Box**. I will also display the data first, then sort them.

Go to **Meta Box** > **Views**, and add a new view.

![Go to Meta Box > Views, and add a new view](https://docs.metabox.io/assets/images/add-new-view-min-6964c6e84899f5944f1f6f49e3db2608.png)

In the **Template** tab, you can use the **Insert Field** button to insert fields or add code directly.

First, add this code:

```php
{% for clone in post.services %}
    {{ clone.service_name }} <br/>      
    {{ clone.price }} <br/>    
{% endfor %}
```

![First, add this code](https://docs.metabox.io/assets/images/insert-field-min-d2d7ec5c2d1a41a42360e55ea20feca6.png)

**In there**:

`{% for clone in post.services %}`: is to insert the service name and the price inside. Since it is a clonable group, it’ll be a loop. Inside this loop, insert the subfield you want to get the value of as usual. `{{ clone.service_name }} <br/>`: is to get all values of subfield in group with ID service\_name `{{ clone.price }} <br/>`: is to get all values of subfield in group with ID price

After inserting all the fields you need, scroll down to the **Settings** section, choose the type of the template as **Singular**, set the **Location** as **Page**, then select your page you created for the car service pricing listing.

![After inserting all the fields you need, scroll down to the Settings section, choose the type of the template as Singular, set the Location as Page, then select your page you created for the car service pricing listing](https://docs.metabox.io/assets/images/location-as-page-min-e3d005bbe60af4467a0632c83232a237.png)

Now, go to the page editor and view it on the frontend, you can see all the data is displayed.

![Now, go to the page editor and view it on the frontend, you can see all the data is displayed](https://docs.metabox.io/assets/images/before-view-min-6ccf9be7a10fbdc6696e0cb3f26fdfbc.png)

To make the page more beautiful, I’m adding some div tags and classes, as well as modifying the code a little bit.

![To make the page more beautiful, I’m adding some div tags and classes, as well as modifying the code a little bit](https://docs.metabox.io/assets/images/add-div-tags-min-575e26d9bef79ed47c5c6bbd3032c5fc.png)

Then, move to the **CSS** tab and add code.

![Then, move to the CSS tab and add code](https://docs.metabox.io/assets/images/CSS-min-c9f69d441e432506c5fdf5199486591e.png)

After styling, our page is like this.

![After styling, our page is like this](https://docs.metabox.io/assets/images/before-min-e39e2932f348091c14976098a8f4a502.png)

Now, it’s time to order them. Back to the created template to add code for this purpose.

![Back to the created template to add code for this purpose](https://docs.metabox.io/assets/images/add-code-mbview-min-558d462df18d62939227d0c27f499f20.png)

**Specifically**:

```php
{% set sorted_services = post.services|sort((a, b) => a.price <=> b.price) %}
```

This line is to declare that we’ll create a new array containing a list of services with their prices sorted from low to high. This value will be taken from the subfield with ID price.

Don't forget to update the array you'll be querying for this loop.

![Don't forget to update the array you'll be querying for this loop](https://docs.metabox.io/assets/images/update-code-min-d9642234feab2993b58ec23f548e2d49.png)

That's all. It's so simple. All the code is updated on [GitHub](https://github.com/wpmetabox/tutorials/tree/master/ordering-cloneable-fields-by-value) for your reference.

Now, let’s check the page on the frontend; these are our expected results.

![Now, let’s check the page on the frontend; these are our expected results](https://docs.metabox.io/assets/images/after-min-1ac33f390db2f9915776c06efba7b55b.png)
