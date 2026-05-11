---
title: Include Exclude vs Show Hide vs Conditional Logic - Meta Box Documentation
source: https://docs.metabox.io/include-exclude-show-hide-conditional-logic/
version: 5.12.0
fetched: 2026-05-11
---

We have 3 extensions that can help you control the visibility of a meta box for a certain post/page:

- [MB Include Exclude](extensions/meta-box-include-exclude.md)
- [MB Show Hide](extensions/meta-box-show-hide.md)
- [MB Conditional Logic](extensions/meta-box-conditional-logic.md)

That might be confused as you don't know which extension is the right choice for you. So the main difference between them is the following: **MB Include Exclude** hides meta boxes **by PHP**, meaning:

- Meta boxes are removed completely from the editing screen, no HTML markup is outputted at all
- Since meta boxes are removed completely, there are no inputs at all and thus, there are no meta values are saved at all
- There is no way to show the meta boxes again unless reloading the page

Both **MB Conditional Logic** and **Show Hide** hide meta boxes **by Javascript**, meaning:

- The HTML of meta boxes are outputted, inputs are only hidden and the meta values are submitted when saving post and are saved in the database
- You can show them without reloading the page

The **MB Conditional Logic** differs from [Show Hide](extensions/meta-box-conditional-logic.md): it has **more advanced options** which allows you to show/hide not only meta boxes but also fields and specific HTML elements. The Show/Hide extension can show/hide only meta boxes. Besides, the number of conditions in Conditional Logic are more than Show/Hide extension (greater, less than, not equal, etc.).
