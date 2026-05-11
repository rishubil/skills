---
title: Filter posts by relationships - Meta Box + Bricks - Meta Box Documentation
source: https://docs.metabox.io/tutorials/role-based-access-control-with-bricks/
version: 5.12.0
fetched: 2026-05-11
---

Imagine that you’re building an internal company portal with training documents. Each document is linked to a department through a **Meta Box relationship**. When employees in different departments log in, they should only see the documents assigned to their department, not the ones from others.

![Role-Based Access Control with Meta Box + Bricks](https://docs.metabox.io/assets/images/result-14edc647b4284f654149d65222ca2e09.gif)

Normally, you might filter posts by taxonomy, or by a custom field value. That works fine in many cases. But here, instead of that, we’ll filter **based on relationships between posts**. This approach is different, and can be applied to a variety of scenarios. For example:

- Showing announcements targeted to specific groups of employees.
- Assigning work shifts, like on-duty doctors for a given day.
- Listing staff members by department or specialty.

The key idea is that access control relies on conditional display. Bricks supports conditions out of the box, and in this tutorial, I’ll walk you through how to combine that with Meta Box relationships to restrict and display posts exactly as needed.

Let’s dive in!

## Video version

## Preparation

In this tutorial, we’ll use the default **WordPress Posts** for the documents and a separate custom post type for **Departments**. Each post will represent a piece of document, and we’ll connect it to one or more departments using a **Meta Box relationship**. Logged-in users will then only see posts linked to their own department.

To make the setup smoother, I recommend using [Meta Box AIO](https://metabox.io/aio/). It gives you all the necessary extensions in one package without having to install each separately.

And, **Bricks** is used to build the layout and set up the filter so that only the posts belonging to the logged-in user’s department are displayed.

Now, let’s go step by step.

## Creating a custom post type

Go to **Meta Box** to create a new custom post type for the **Departments**.

![Create post type](https://docs.metabox.io/assets/images/create-post-type-3108b4b139c0074dc3c9c5d995d15198.png)

After publishing, you’ll see the created custom post types in the admin menu. And you can see some departments I created as posts, such as Marketing, Development, Human Resources, and Sales.

![Department post type](https://docs.metabox.io/assets/images/department-post-type-ee62d165dd566c5ceec672faa8f45fca.png)

## Creating the relationship

Go to **Meta Box** > **Relationships** to create a relationship between the default Posts - documents - and the **Departments** post type.

![create a relationship between posts and the Departments](https://docs.metabox.io/assets/images/create-relationship-d783c667ef171a34b1c783cb452d9f57.png)

We have the **From** and **To** sections. The relationship is bidirectional, which means it doesn’t matter which side you set up first - data will be linked both ways.

In this case, both sections will have the Object Type set to Post, since we’re connecting the default Posts with the Departments custom post type.

![From and To relationship section](https://docs.metabox.io/assets/images/from-to-relationship-sections-6d7b6ba66c52df99f36aabd20671911d.png)

In the **From** section, choose Post in the **Post type** option because I set it for the default posts, and the rest is **Department** post type.

![choose Post type option](https://docs.metabox.io/assets/images/post-type-option-for-relationship-17bb0779a941e673475bc61e14962f12.png)

Pay attention to the **Show as an admin column** setting. It’s available when you activate the **MB Admin Columns** extension. When you check it, there’ll be a column in the dashboard to show which departments are related to the document and which posts are related to departments.

![Show admin columns](https://docs.metabox.io/assets/images/show-admin-columns-bac2bcfdc1af7ada7a7866837a3bba21.png)

After publishing, go to create a new post; you can see a section allowing you to select several departments.

![Department section in post editor](https://docs.metabox.io/assets/images/department-section-in-post-editor-dcb49717c476c0fe02244d9fb0e96a4c.png)

Here’s an example of how the relationship between learning posts and departments looks in the admin dashboard.

![relationship admin dashboard](https://docs.metabox.io/assets/images/relationship-admin-dashboard-7f8770997bccbdc706792e60a7648467.png)

## Creating a custom field for the users

To assign each user to a specific department, we’ll create a custom field that stores this information.

Now, go to **Meta Box** > **Custom Fields**, and create a new field group.

![Create custom fields](https://i0.wp.com/images.elightup.com/meta-box/blog/filter-post-relationship-metabox-bricks/create-custom-fields.png)

Choose the field type as **Post**. And in the **Post types** option, select the exact post type. This will allow us to assign the correct department to each user.

![(Post field type](https://docs.metabox.io/assets/images/post-field-type-59613367d3f17d175f4c2170ce1ae778.png)

For better usability, you can also enable the **Admin columns** option to display the user’s department directly in the user list.

![Admin columns for field](https://docs.metabox.io/assets/images/admin-columns-for-field-33651e56ea601e26fe5cfd0f84d5fe43.png)

Next, switch to the **Settings** tab and set the **Location** to **User** so the field appears in the user profile editing screen.

![Field-group-settings](https://docs.metabox.io/assets/images/field-group-settings-ba94155d761395b768807faa55aa57fe.png)

After publishing, open any user profile editor, and you’ll see the new **Department** section. Simply select the department you want to assign to that user and update the profile.

![Department in profile editor](https://docs.metabox.io/assets/images/department-in-profile-editor-ce909dfee19c4ded549fb2cac68c4f03.png)

At this point, every user is now placed into their respective department.

## Showing all posts on the page

Now, let’s display the full list of documents on a page, whether or not they have assigned departments. Later, we’ll add a filter to show only those from a specific department.

First, create a new page named **Documents**. Then, edit the page with **Bricks**.

![Edit with Bricks](https://docs.metabox.io/assets/images/edit-page-with-bricks-9a2b1861d7df15a2d56718f79a43fe1f.png)

To start building the layout, add a **Section** element to cover all the page content. There’s already a **Container** available inside, so we’ll add elements into this container to show the list of documents.

![A Section element to cover all the page content](https://docs.metabox.io/assets/images/section-cover-documents-640afa731e6223b693076c6645f5b7d7.png)

Before going further, add a **Post Title** element. It will automatically display the title of the current page on the frontend.

![Get page type](https://docs.metabox.io/assets/images/get-page-title-d42985c2b4b91f8e4d06fa62a4f76bbb.png)

We want to display all documents, so we need to use a query loop. To do that, select a **Div** as the wrapper, and enable the **Query loop** button. And in the **Query** section, choose the default Posts. And enter `-1` in the Posts per page section so that it will retrieve all the documents. I mean all the posts

![Query all posts](https://docs.metabox.io/assets/images/query-all-posts-db5323c09953b2ed5551db8e00bcd5b3.png)

Also, add the second **div** that will later be used to filter the documents into their respective departments. That part will come in the next step.

![Div to filter posts](https://docs.metabox.io/assets/images/div-to-filter-posts-d809593ef178b71cb33ae3f7d96cb43b.png)

Inside this div, add some elements to display each document’s details.

Choose the **Image** element for the post’s image. Since these are the post’s featured images, click the **Dynamic Data** icon and choose the **Featured Image** option. As you can see, the image is displayed in the preview.

![Get post image](https://docs.metabox.io/assets/images/get-post-image-831a979895f3b9eb6ca36ddaea7ea956.png)

Next, add another **Div** to hold the other information, like the title, department, and publish date, for styling purposes.

Now, choose the **Post Title** element to display the title of each document within the query loop. This is different from the page’s Post Title element added earlier, as it specifically pulls the title from each post in the loop.

![Get post title](https://docs.metabox.io/assets/images/get-post-title-9014334e0808967724501a65897cab13.png)

To show the department that the document is assigned, add a **Basic Text** element. As this info is saved in Meta Box’s relationship, in the **Content** section, we’ll use the **Dynamic Data** and then look for the relationship to connect posts with departments. This ensures each document displays its correct department. So, now we can see the department for that post.

![Display-department](https://docs.metabox.io/assets/images/display-department-e3804c678fd1318a688d44cc42d5bb0b.png)

Finally, for the date of publishing, select another **Basic Text** element. Add a label as you want. Then, use the **Dynamic data** button again and choose the **Post date** option. The label will always display alongside the post date.

![Get post date](https://docs.metabox.io/assets/images/get-post-date-ec9c744f5da4b257b91ea4e2f4961730.png)

All the information for the documents and their assigned departments is in place.

View the page on the frontend: the list of documents is now showing up whether they are assigned to a department or not. However, the layout is still quite basic, so let’s make it more visually appealing.

![Documents display before-styling](https://docs.metabox.io/assets/images/documents-display-before-styling-a6197f7d948acef875e7672420a26bc7.gif)

To style it, choose each element and adjust its settings as desired. Once styled, the list will look much better.

![Document after styling](https://docs.metabox.io/assets/images/all-document-after-styling-be4d5aec139f3eae69e3f767b9e77d17.png)

Next, we’ll move on to filtering the posts conditionally by their department relationship.

## Filtering posts conditionally by relationship

Now we’re going to add conditions so the list only shows posts that belong to the logged-in user’s department.

Head back to the page editor with **Brick**. In the second div that we created earlier, click the **Conditions** icon to start setting them up.

![Set conditions](https://docs.metabox.io/assets/images/set-conditions-d372e8f30288ba472226024500a1842b.png)

**In there**:

1. Add a condition to check whether the user is logged in. For that, select **User login**, set the operator to **Is**, and the value to **logged in**. This way, if the user isn’t logged in, they won’t see any posts at all.
2. Set the second condition to match the post’s department with the user’s department. Choose **Dynamic data**, then select the relationship between posts and departments. This returns the list of department names that are linked to the current post. Set the operator to **contains**, meaning we’re checking whether that list includes a certain value. For the value, choose **Department** custom fields, which retrieves the department assigned to the currently logged-in user. This way, Bricks will only display posts whose related departments include the user’s own department.

Let’s tidy things up a bit. Add a custom class named `mb-content` to the parent div that wraps each post. After that, add this snippet to the **CSS** tab. This hides any div that doesn’t contain post content, so we don’t get any awkward blank spaces on the page.

![Add css](https://docs.metabox.io/assets/images/add-css-560b06dfe670dcf646c96e93c54372f8.png)

With this setup, only posts whose department matches the logged-in user’s department will be displayed. For example, if you log in as a Developer staff member, you’ll only see posts from the Developer department. If you switch to an HR account, you’ll only see posts from HR and so on.

![ressult](https://docs.metabox.io/assets/images/result-14edc647b4284f654149d65222ca2e09.gif)
