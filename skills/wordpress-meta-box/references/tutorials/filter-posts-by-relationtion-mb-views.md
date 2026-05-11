---
title: Filtering posts by relationships - MB Views - Meta Box Documentation
source: https://docs.metabox.io/tutorials/filter-posts-by-relationtion-mb-views/
version: 5.12.0
fetched: 2026-05-11
---

Filtering and displaying posts based on certain criteria is one of the most common functionalities every website needs. And today, let me show you another method: **filtering by relationship**. We’ll do it with the help of **MB Views** from **Meta Box**.

For demonstration purposes, I’ll build an internal company portal with training documents. When employees in different departments log in, they should only see the documents assigned to their department.

![Example of filtering posts by relationships](https://docs.metabox.io/assets/images/result-14edc647b4284f654149d65222ca2e09.gif)

## Video version

## Preparation

The key idea is that access control relies on conditional display. In this tutorial, we’ll use the default WordPress Posts for the learning materials, and a separate custom post type for Departments. Each post will connect to one or more departments using a Meta Box relationship. To add the user to a department, I use a custom field for the user.

So, you just need [**Meta Box AIO**](https://metabox.io/aio/). It gives you a framework and all the necessary extensions in one package without having to install each separately, specifically:

- [MB Admin Columns](https://metabox.io/plugins/mb-admin-columns/): to display related information neatly in the admin panel;
- [MB Custom Post Type](https://metabox.io/plugins/custom-post-type/): to create the custom post type for departments;
- [MB Relationships](https://metabox.io/plugins/mb-user-meta/): to create the relationship between material posts and departments;
- [MB User Meta](https://metabox.io/plugins/mb-user-meta/): to add the custom field for selecting a work department in each user profile;
- [MB Views](https://metabox.io/plugins/mb-views/): to create the template for displaying the posts belonging to the logged-in user’s department only;
- [MB Builder](https://metabox.io/plugins/meta-box-builder/): to visually create the custom field for the user without writing code.

Now, let’s go step by step.

## 1\. Creating a custom post type

Go to **Meta Box** > **Post Types** to create a new custom post type for the Departments.

![Go to Meta Box, Post Types to create a new custom post type.](https://docs.metabox.io/assets/images/create-cpt-f861191dbfbcc16c43e016f8a12e89ab.png)

After publishing, you’ll see the created custom post type in the menu.

![The created post type.](https://docs.metabox.io/assets/images/cpt-ac28bf17438d9b987060329c0e6b7b7e.png)

You can see some departments I created as posts here.

## 2\. Creating the relationship

Since we want to show documentation based on the department, we need to create a relationship between them.

Go to **Meta Box** > **Relationships** to create a new one.

![Go to Meta Box, Relationships to create a new one.](https://docs.metabox.io/assets/images/create-relationship-17493e81d92a0e07825b8b09cb1a7f02.png)

In the interface of MB Relationships, there are the **From** and **To** sections. Setting them up is the same.

Because we’re setting the relationship between the default post and a custom post type, set the **Object Type** as **Post** in both sections.

![Set the Object Type as Post in both sections.](https://docs.metabox.io/assets/images/object-type-ee31992865a8a610b1fc5799121401f1.png)

The relationship is bidirectional, which means it doesn’t matter which side you set up first, data will be linked both ways. For instance, in the **From** section, I set the **Posts** as default posts, and the rest will be `department` post type.

![Set the Posts as default posts, and the rest will be department post type.](https://docs.metabox.io/assets/images/post-type-d819b12b1502e69aa23e3b4bda9fd1e5.png)

If you want to show which departments are related to learning material and vice versa, just check the setting of the admin column as below:

![Check the setting of the admin column](https://docs.metabox.io/assets/images/column-relationship-8bd4901cc82398bb2061c2ca7a383098.png)

After publishing, go to the post editor, you can see a relationship section on the right panel. Absolutely, you can connect it to more than one department.

![The relationship in the post editor.](https://docs.metabox.io/assets/images/post-editor-b8d4f7a4e74b89b621482530614ad0fc.png)

In the admin dashboard, there is an additional column that shows the relationship we set.

## 3\. Creating a custom field for the users

To define a specific department for each user, we’ll use user meta, it means adding a custom field for the user.

Navigate to **Meta Box** > **Custom Fields** and create a new field group.

![Navigate to Meta Box, Custom Fields and create a new field group](https://docs.metabox.io/assets/images/create-field-d2a4032f4e0489c9cb123b1647053a43.png)

We already have departments as posts of the created post type. So, add a **Post** field.

![Add a Post field](https://docs.metabox.io/assets/images/add-post-field-76bbdd4495d91b82898e2a5115697834.png)

Then, in the **Post types** option, select the exact post type. This will allow us to assign the correct department to each user.

![Set the post type](https://docs.metabox.io/assets/images/choose-post-type-0fe94355360f1f50e51a6ff844fb56db.png)

For better usability, you can also enable **Show as an admin column** to display the user’s department directly in the user list. Its functionality is the same as the admin column in the creating relationship above.

![Set the admin column](https://docs.metabox.io/assets/images/column-field-f3a8e10254e71628b8b6ccc630df5309.png)

Next, switch to the **Settings** panel and set the **Location** to **User**. As a result, the field will appear in the user profile editing screen.

![Set location for field group](https://docs.metabox.io/assets/images/location-0048800053a03cc24dc34f09596f771d.png)

After publishing, open any user profile editor, and you’ll see the created field. Simply select the department to assign the user to it.

![The field in the user profile](https://docs.metabox.io/assets/images/user-profile-453053047babcc9b80b1b154902d051a.png)

At this point, every user is now placed into their respective department.

## 4\. Showing all posts on the page

We’ll display all the documentation on an archive page first. Then, adding a filter to show only those from a specific department will be done later.

We need to have a new page that contains all the posts.

![Create a new page](https://docs.metabox.io/assets/images/create-page-c15bf67a4ffea8bcf81e87b4ebea3e64.png)

Now, I’ll use MB Views to create a template for displaying documentation.

Navigate to **Meta Box** > **Views**, and create a new one.

![Navigate to Meta Box > Views, and create a new one](https://docs.metabox.io/assets/images/create-view-04dff897423aab79bf5ee0e9fb7660f3.png)

In the **Template** tab, let’s add code or insert fields to show posts and their details. This is already quite familiar in many of our tutorials. At the beginning, I add this code:

```php
{% set args = {post_type: 'post', posts_per_page: -1,orderby: 'date',order: 'DESC'} %}
{% set posts = mb.get_posts(args) %}

{% for post in posts %}
    {% set related_args = {
            relationship: { id: 'post-to-department', from: post.ID },
            post_type: 'department',
            posts_per_page: -1
        } %}
    {% set related_departments = mb.get_posts(related_args) %}
{% endfor %}
```

![Add code to get posts](https://docs.metabox.io/assets/images/get-posts-c2767fd68c40630ec909ccdf8f2f13ed.png)

**In there**:

- `{% set args = {post_type: 'post', posts_per_page: -1,orderby: 'date',order: 'DESC'} %}`: is to declare that we’ll get posts on the site through the post slug. If you want to get posts from a custom post type, just change that slug.
- `mb.get_posts`: is a Meta Box function to get the post.
- `{% for post in posts %}...{% endfor %}`: is a loop to display all of posts since there are various posts.
- `post-to-department`: the ID of the relationship. The whole of code is used to retrieve the post from the `department` post type that is connected to the recent post through the post ID.
- `related_departments`: the attribute that stores all the retrieved departments.

Then, also in the loop, I use the **Insert Field** button get and display material information. Just click on the field from the drop-down list on the right panel.

![Insert field](https://docs.metabox.io/assets/images/insert-field-933516cc32770d7fe89c1260f7e28f81.png)

MB Views also supports you in choosing the size or output of some special fields. A documentation can be assigned to more than one department. So, I have a nested loop here for the variable we have had. I just get the department name, I mean the post title. And this is my template after inserting fields:

![Inserts all fields you need](https://docs.metabox.io/assets/images/all-fields-a7bb30143002c6c3b7324b62fa66842c.png)

Then, move down to the **Settings** section to apply this template for the page that we created before. I set the **Type** as **Singular**, then, choose the page.

![Set location for template](https://docs.metabox.io/assets/images/template-location-b6f7a77bb3c43f54d791e03f9067b023.png)

Now, view the page on the frontend, you can see all the data is displayed, including the department.

![The data is displayed](https://docs.metabox.io/assets/images/view-frontend-96458c7e049871dd2dd14cb81fc0fd03.png)

To make the page more beautiful, go back to the template and add some `**div**` tags and classes.

![Add div tags and classes](https://docs.metabox.io/assets/images/div-34ca014fb52a779bfa23381975dea159.png)

Then, move to the CSS tab to add some code for styling.

![Add CSS](https://docs.metabox.io/assets/images/css-8b0f3de3adc6a7512bc8d9a0c26638aa.png) This is the new look of the page I have.

![The page after styling](https://docs.metabox.io/assets/images/frontend-style-74eaed38d2cbd0d4ff624d3b5707fcb3.png)

You can click on a post to read its content.

## 5\. Filtering posts by relationships

Our aim is only showing posts that belong to the logged-in user’s department. I’m still the template that was created in the previous step and add some code.

```php
{% set show = false %}
{% if mb.is_user_logged_in() %}
    {% if user.department and user.department.title is not empty %}
        {% set user_dept_name = user.department.title|trim %}
        {% for dept in related_departments %}
            {% if dept.post_title|trim == user_dept_name %}
                {% set show = true %}
            {% endif %}
        {% endfor %}
    {% else %}
        {% set show = true %}
    {% endif %}
{% endif %}
```

![Add code to filter by relationship](https://docs.metabox.io/assets/images/filter-aef78886d8fe0ea0a21f7ed88ad737e4.png)

Specifically, I use `mb.is_user_logged_in()` function that checks whether the current user is logged in. Then, we check whether the user has a department value to run the code below. Because in the case that the user logged in, but doesn’t have a department, such as admin or founder, he can see all the posts of departments.

In the case that the user is assigned to a specific department, the department title will be get and stored in the `user_dept_name` variable.

Next, I compare the user’s department with the post’s related departments. If they are matches, the documentation will be shown. It means the post will only be shown if the user belongs to the same department.

That’s done.

Now, let’s check it on the frontend. It works well.

![Final result of filtering posts by relationships](https://docs.metabox.io/assets/images/result-14edc647b4284f654149d65222ca2e09.gif)
