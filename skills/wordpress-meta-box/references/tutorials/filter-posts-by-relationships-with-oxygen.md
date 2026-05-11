---
title: Filtering posts by Relationships - Meta Box + Oxygen - Meta Box Documentation
source: https://docs.metabox.io/tutorials/filter-posts-by-relationships-with-oxygen/
---

Are you building an internal company portal to manage training materials? Each document is connected to a department by a Meta Box relationship. When staff log in, they’ll only see the documents for their own department, not others. If so, you should not skip this article because today, I will show you how to **create a filter posts by relationships** using **Meta Box** and **Oxygen**.

You may find this topic useful if you are looking to build an internal website. Besides, if you are a seller, like selling courses, you can create courses associated with student groups where each student can only see the courses they have purchased or have permissions for.

Check out the page I made as an example for users:

![Check out the page I made as an example for users](https://docs.metabox.io/assets/images/demo-min-a2ba7a1390a31ddc3da767756cee9630.gif)

## Video version

## Preparation

Here I have several **Documents** and each of them will be a **Post**. I will create a custom post type for **Departments**. Then I will **create a bi-directional relationship** between them. The relationship connects which department will have related posts and vice versa.

Next, I will create a custom field for the **work department** to classify the department for each **user**. When the user logs in, they will see the archive page displaying related posts of their department by filter condition. This page is built by **Oxygen**.

So, we need **Oxygen** to build the page.

Next, you need [**Meta Box AIO**](https://metabox.io/aio/) to have the framework for creating custom post types, custom fields and relationships. As well as the Meta Box extensions inside it provide you with advanced features, specifically:

- [MB Admin Columns](https://metabox.io/plugins/mb-admin-columns/): to display the related posts and related departments as a column in the dashboard.
- [MB Custom Post Type](https://metabox.io/plugins/custom-post-type/): to create a custom post type for the departments.
- [MB Relationships](https://metabox.io/plugins/mb-relationships/): to create relationships between these post types.
- [MB User Meta](https://metabox.io/plugins/mb-user-meta/): to add a work department to user profile.
- [MB Builder](https://metabox.io/plugins/meta-box-builder/): to have a UI on the backend to create custom fields and relationships easily.

That’s all. Let’s get started now.

## Creating custom post types

Go to **Meta Box** and create a new post type for the **Departments**.

![Go to Meta Box and create a new post type for the Departments](https://docs.metabox.io/assets/images/add-new-post-type-min-257e4b7f0be847bcc563d362d9cdc640.png)

After creating, you can see the post types displayed in the **Admin Dashboard**. This is the list I have.

![This is the list I have](https://docs.metabox.io/assets/images/list-departments-min-56b119c9c387babac0f150c2547446e0.png)

## Creating a relationship

Go to **Meta Box**, **Relationship**, and create a new one.

![Go to Meta Box, Relationship, and create a new one](https://docs.metabox.io/assets/images/add-new-relationship-min-2087f614819b9238207005104e411d3f.png)

There’ll be the **From** and **To** sections as follows. The relationship is bidirectional, so you can put the two post types into any section.

Since they are post types, remember to set the object type as **Post** in both sections.

![Since they are post types, remember to set the object type as Post in both sections](https://docs.metabox.io/assets/images/object-type-edit-min-079183a5ff6bab91aaed25a01bba577d.png)

Set the **Post type** in the **From** section as one that we want to be in the relationship. In this case I set **Posts**, so the rest one in the **To** section will be the **Departments**.

![Set the Post type in the From section as one that we want to be in the relationship](https://docs.metabox.io/assets/images/post-type-edit-min-f2aaaa77b0ae3d0f758bcec026721ee8.png)

Enable this setting if you want to show them as an admin column.

![Enable this setting if you want to show them as an admin column](https://docs.metabox.io/assets/images/admin-column-edit-min-61433a6f7414322f93777d55b979b603.png)

After publishing, go to the post editor, you will see the section for setting relationships. Just fill the post information and choose its departments.

![Just fill the post information and choose its departments](https://docs.metabox.io/assets/images/choose-department-for-post-min-e5837deb2860f9ff126dea5538638eb5.png)

These are some posts I have. And, you can easily view the **Posts** and the related **Departments** information in these columns.

![And, you can easily view the Posts and the related Departments information in these columns](https://docs.metabox.io/assets/images/list-posts-department-min-d395e2bb26020e7edbca051b91ba8d20.png)

## Creating a custom field

To add departments to each user, I will create a custom field. Feel free to add additional fields depending on your needs.

Now, go to **Meta Box** > **Custom Fields**, and create a new field group.

![Now, go to Meta Box > Custom Fields, and create a new field group](https://docs.metabox.io/assets/images/add-new-custom-field-min-7206455f5c29da879fb322125e038ca5.png)

For the user department, choose the **Post** field type, then choose **Post** type as **Department**.

![For the user department, choose the Post field type, then choose Post type as Department](https://docs.metabox.io/assets/images/user-departments-type-36f8bf0a8268751c356378a7c45e6c2c.png)

Enable this setting to show them as an admin column.

![Enable this setting to show them as an admin column](https://docs.metabox.io/assets/images/admin-column-for-custom-field-min-51741614aaedc3b911d31926bc35f3a9.png)

Then, move to the **Settings** tab, choose **Location** as **User** to apply the field to it.

![Then, move to the Settings tab, choose Location as User to apply the field to it](https://docs.metabox.io/assets/images/location-as-user-min-a66599a2375c9d231eeb1ae61598d559.png)

Now, in each user profile, you can see the **Department** field section. Click on it to select the department.

![Now, in each user profile, you can see the Department field section](https://docs.metabox.io/assets/images/work-department-field-min-db9c3da213195edbced11737952d2b80.png)

After updating, you can see users with related work departments in the dashboard like this.

![After updating, you can see users with related work departments in the dashboard like this](https://docs.metabox.io/assets/images/user-department-min-79369bad197410564d44f8c6df04e4e4.png)

## Displaying posts on an archive page

Navigate to the **Oxygen** > **Templates**, and add a new template.

![Navigate to the Oxygen > Templates, and add a new template](data:image/png;base64,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)

Next, go to **Pages**, create a new page for the **Documents**.

![Next, go to Pages, create a new page for the Documents](data:image/png;base64,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)

Then, scroll down to the **Oxygen** section, and choose the created template to render the page using it. Edit the page with **Oxygen**.

![Edit the page with Oxygen](https://docs.metabox.io/assets/images/edit-page-with-oxygen-min-f7106f33a2ba02447d55c57f74577683.png)

Choose the **Documents** for the **Editing** and **Previewing**.

![Choose the Documents for the Editing and Previewing](https://docs.metabox.io/assets/images/editing-and-previewing-min-b3d5f6e3185e057b7503d642f79bc245.png)

First, select a **Section** component to contain all of the page content.

![select a Section component to contain all of the page content](https://docs.metabox.io/assets/images/add-section-1c609461a11a7a012e53b3a7a2da74c3.png)

To get the title of the page automatically, add a **Heading** component, then click **Insert Data**, **Post**, **Title** to connect it with the title of the page.

![To get the title of the page automatically, add a Heading component, then click Insert Data, Post, Title to connect it with the title of the page](https://docs.metabox.io/assets/images/add-heading-min-375303af27aa5dfd6a8670c5cbb67f22.gif)

Since we have more than one post on the page, you should add a Repeater component to define information structure for them all.

![Since we have more than one post on the page, you should add a Repeater component to define information structure for them all](https://docs.metabox.io/assets/images/add-repeater-min-07fee6b8d59dd2032aebb6e71c8a695b.png)

Go to **Query** > **Advanced**, and add parameters for the query like this.

![Go to Query > Advanced, and add parameters for the query like this](https://docs.metabox.io/assets/images/advanced-query-min-ec51db5ed27b7904b9dfce61f0e00f30.gif)

In there, `post` is the slug of the **Post** post type. It means that we’ll get posts from this post type.

![It means that we’ll get posts from this post type](https://docs.metabox.io/assets/images/post-type-slug-min-53c4af74deec303a6f9c9a9178833d07.png)

I want to get all the posts we have, so the setting will be like this.

![I want to get all the posts we have, so the setting will be like this](https://docs.metabox.io/assets/images/post-per-page-min-2b675e9c3d5f5200cab8e39a9d24b5d1.png)

Inside the **Repeater** component, there’ll be a **Div**. Add some components inside this **Div** to display the posts’ information.

I added an **Image** component and inserted data from the **Featured Image** of the post.

![I added an Image component and inserted data from the Featured Image of the post](https://docs.metabox.io/assets/images/add-image-min-36a3c7e4db1232f108221502823834ef.gif)

Next, add a **Heading** then insert data from the **Post Title** for the course name.

![Next, add a Heading then insert data from the Post Title for the course name](https://docs.metabox.io/assets/images/add-post-tittle-min-5feecb47687d83911084f5b3595ea481.gif)

You may get the wrong name and image of the course, but don't worry about it. Just keep moving, you will see the right things later.

To get the department information of the post, add a **Text** component and insert data from **Meta Box Field**. If you want to display the department’ name along with the **link**, choose the **Post URL** option when inserting data like this. Immediately, you can see the post is displayed exactly with the related department’ name as follows.

![To get the department information of the post, add a Text component and insert data from Meta Box Field](https://docs.metabox.io/assets/images/add-department-information-min-c8c1030c0aaa90162851891104028920.gif)

The last information of the post is date, add another **Text** below. Click on this to insert dynamic data. Choose the **Date** and fill the format that you want. In my example, I will put the format like this.

![The last information of the post is date, add another Text below](https://docs.metabox.io/assets/images/add-date-min-85152767230a474e34dfe7cdc052a862.gif)

After getting all the wanted information for posts, view the page on frontend. You will see the image along with their information displayed correctly. But, it seems like we should style the page a little bit to have a better appearance.

![After getting all the wanted information for posts, view the page on frontend](https://docs.metabox.io/assets/images/view-on-frontend-min-134fc9dbeed5051895b405a3df608b68.gif)

Back to the template, you can change the settings of each component to get the wanted look for the page. Here is the one that I got after styling.

![Here is the one that I got after styling](https://docs.metabox.io/assets/images/after-styling-min-c37fec9afd86d66abc2a1d2a759176bc.png)

## Filtering posts by relationships

Let’s add filter posts by **Relationships** so users can see the related posts of their department. **Oxygen** allows you to set rules for displaying posts easily.

In the **Oxygen** settings, click on the **div** right below the **repeater** component, move to the **setting** tabs, choose the **Conditional Settings** icon to set the conditions.

![choose the Conditional Settings icon to set the conditions](https://docs.metabox.io/assets/images/conditional-setting-min-1c0d7d42b1b0fac0e722f536c52639ce.png)

In the conditions’ pop up, add a new rule. Select **User Logged In** below the list and set the next box of the conditions setting like this. This rule means that only valid users will see the displayed posts.

![Select User Logged In below the list](https://docs.metabox.io/assets/images/user-logged-in-min-fd524dbffda2c85a027f81060d8249e4.png)

Next, add the second rule. In the dropdown, choose **Dynamic Data**, **Meta Box Field** and **Departments**. Choose **Post Object ID** so that **Users** can see the related posts of their department.

![Next, add the second rule](https://docs.metabox.io/assets/images/2nd-rule-min-79aafc8e39b65bd0fe7b2f287a3df31c.gif)

In the next box of the conditions setting, choose **contains** to compare whether the data above contains a certain value. Then in the last box, click on the **data** button, move to **Current User** and choose **Meta or Custom** field. Fill the **Meta Key** as `user_department` so that we can get the department field value of the current user.

![In the next box of the conditions setting](https://docs.metabox.io/assets/images/next-box-setting-min-31a15e258b7ad55a919c7b3b1a92f672.gif)

Now, go to the page on frontend, You will see the filter works well.

First, all posts are displayed in the admin account. Log out and log back in to each user account.You can see users in different departments will only see posts from the related department.

![Now, go to the page on frontend, You will see the filter works well](https://docs.metabox.io/assets/images/demo-min-a2ba7a1390a31ddc3da767756cee9630.gif)
