---
version: alpha
name: <Project Name>
description: <One sentence describing this design system>
# A light-first "ink on paper" preset: Tailwind gray plus one teal accent,
# square corners, no shadows, Pretendard for reading and D2Coding for data,
# with a dark theme that follows the system setting. Retune the tokens per
# project, but keep the prose in sync with every change.
colors:
  bg: "#ffffff"
  panel: "#f9fafb"
  border: "#d1d5db"
  text: "#111827"
  muted: "#4b5563"
  primary: "#0f766e"
  on-primary: "#ffffff"
  alert: "#b91c1c"
  alert-bg: "#fef2f2"
  success: "#15803d"
  success-bg: "#f0fdf4"
  code-bg: "#f5f5f5"
  code-text: "#24292e"
  # The dark theme, which follows the system setting (`prefers-color-scheme: dark`).
  # Each `dark-*` token has the role of the light token with the same name.
  dark-bg: "#111827"
  dark-panel: "#1f2937"
  dark-border: "#374151"
  dark-text: "#f3f4f6"
  dark-muted: "#9ca3af"
  dark-primary: "#2dd4bf"
  dark-on-primary: "#111827"
  dark-alert: "#f87171"
  dark-alert-bg: "#2a1215"
  dark-success: "#4ade80"
  dark-success-bg: "#0f2a1a"
  dark-code-bg: "#282c34"
  dark-code-text: "#abb2bf"
typography:
  page-title:
    fontFamily: "'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
    fontSize: 1.875rem
    fontWeight: 900
    lineHeight: 1.2
  section-title:
    fontFamily: "'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
    fontSize: 1.25rem
    fontWeight: 800
    lineHeight: 1.3
  body:
    fontFamily: "'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  nav:
    fontFamily: "'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
    fontSize: 0.9375rem
    fontWeight: 800
  subsection-title:
    fontFamily: "'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
    fontSize: 1rem
    fontWeight: 800
    lineHeight: 1.4
  label:
    fontFamily: "'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
    fontSize: 0.875rem
    fontWeight: 600
  caption:
    fontFamily: "'Pretendard Variable', Pretendard, -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
    fontSize: 0.8125rem
    fontWeight: 400
    lineHeight: 1.5
  data:
    fontFamily: "D2Coding, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace"
    fontSize: 0.875rem
    fontWeight: 400
    fontFeature: tnum
rounded:
  none: 0px
spacing:
  xs: 0.25rem
  sm: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  2xl: 2rem
  3xl: 3rem
  # Column widths of the page (see Layout).
  content-width: 72rem
  reading-width: 48rem
  # The widest a URL or a select gets before it is cut (see Layout).
  url-width: 24rem
  # Line widths (see Components).
  hairline: 1px
  focus-width: 2px
  rule-width: 4px
components:
  page:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
  panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  nav-link:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.primary}"
    typography: "{typography.nav}"
    padding: "0.5rem 0.75rem"
    rounded: "{rounded.none}"
  nav-link-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  nav-link-current:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  button:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    padding: "0.375rem 0.75rem"
    rounded: "{rounded.none}"
  button-hover:
    backgroundColor: "{colors.border}"
    textColor: "{colors.text}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    padding: "0.375rem 0.75rem"
    rounded: "{rounded.none}"
  button-danger:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    padding: "0.375rem 0.75rem"
    rounded: "{rounded.none}"
  input:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    padding: "0.375rem 0.5rem"
    rounded: "{rounded.none}"
  table-header:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
  flash-info:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    padding: "{spacing.md}"
  flash-error:
    backgroundColor: "{colors.alert-bg}"
    textColor: "{colors.alert}"
    padding: "{spacing.md}"
  code-block:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.code-text}"
    typography: "{typography.data}"
    padding: "{spacing.md}"
  caption-text:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  data-text:
    textColor: "{colors.text}"
    typography: "{typography.data}"
  page-title:
    textColor: "{colors.text}"
    typography: "{typography.page-title}"
  section-title:
    textColor: "{colors.text}"
    typography: "{typography.section-title}"
  # Dark theme variants: the same components with the `dark-*` colors.
  page-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-text}"
  panel-dark:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.dark-text}"
  nav-link-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-primary}"
  nav-link-hover-dark:
    backgroundColor: "{colors.dark-primary}"
    textColor: "{colors.dark-on-primary}"
  button-dark:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.dark-text}"
  button-hover-dark:
    backgroundColor: "{colors.dark-border}"
    textColor: "{colors.dark-text}"
  button-primary-dark:
    backgroundColor: "{colors.dark-primary}"
    textColor: "{colors.dark-on-primary}"
  button-danger-dark:
    backgroundColor: "{colors.dark-alert}"
    textColor: "{colors.dark-on-primary}"
  input-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-text}"
  flash-info-dark:
    backgroundColor: "{colors.dark-success-bg}"
    textColor: "{colors.dark-success}"
  flash-error-dark:
    backgroundColor: "{colors.dark-alert-bg}"
    textColor: "{colors.dark-alert}"
  code-block-dark:
    backgroundColor: "{colors.dark-code-bg}"
    textColor: "{colors.dark-code-text}"
  caption-text-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-muted}"
---

<!--
  This is a filled preset, not an empty skeleton. Only the reference object
  in the Overview is left open: replace that comment with the project's own
  reference, then retune any token the project needs and update the prose
  that names it. Delete every comment before calling the file done, and run:
    npx -y -p @google/design.md designmd lint <this file>
-->

## Overview

<!--
  Name ONE concrete reference object this project should look like — an
  existing site, a printed artifact, a product manual — in one or two
  sentences, and say what the project is (a reading site, a daily
  operations tool, ...). Then add the sentence that makes the reference a
  test: "if a screen would look out of place as a page of <reference>, it
  is wrong." The paragraphs below describe the preset's look and stay true
  for any reference that fits it; if the reference you pick contradicts
  them, this preset is the wrong starting point.
-->

The UI is ink on white paper, set in Pretendard, with one teal accent, a centered column, and very heavy headings. Nothing floats, glows, or rounds off. It reads as a text document that happens to have links and forms, not as an app.

The same look serves two kinds of page. A reading page is a narrow column of prose. A working page (lists, tables, forms, settings) is the same page with a wider column: tables and forms replace long prose, but the paper, the ink, and the type do not change.

The look brings its restrictions: no dashboard chrome, no cards with shadows, no icons for decoration, and no second brand color.

## Colors

The palette is Tailwind's gray scale plus one teal.

- {colors.bg} is the paper. Every page sits on it, and inputs use it too, so a field reads as a hole in the page.
- {colors.panel} is one step darker. It marks a group (a fieldset, a summary box, the table header row, the site header bar). There is no third surface level.
- {colors.border} draws hairlines between rows, around fieldsets, and under the header. It is also the hover fill of a plain button.
- {colors.text} carries all reading text and headings.
- {colors.muted} is for help text, timestamps, counts, and other secondary information. Never use it for something the user must read to act.
- {colors.primary} is the one accent: links, the navigation, and the one main action of a form. On white it is Tailwind teal-700, not teal-600, because teal-600 text on white has a contrast of about 3.7:1, below WCAG AA for normal text. {colors.on-primary} is the text on a solid teal fill.
- {colors.alert} and {colors.alert-bg} mean "something failed or needs action": error messages, failed runs, stale states, destructive buttons. Do not use red for anything else, so that red always means trouble.
- {colors.success} and {colors.success-bg} mean "this worked": the confirmation flash after an action, a healthy status.
- {colors.code-bg} and {colors.code-text} are a GitHub-style light code block. Use them for JSON payloads, logs, rules, and other raw values.

The dark theme follows the system setting (`prefers-color-scheme: dark`) and needs no switch or JavaScript. Each `dark-*` color has the role of the light color with the same name: {colors.dark-bg} is Tailwind gray-900, the accent becomes {colors.dark-primary} (teal-400), and the code block uses One Dark colors. In the CSS, both themes set the same custom property names (the dark ones in a `prefers-color-scheme: dark` block), so a component never needs a dark-specific rule. The `*-dark` components in the front matter exist so that the contrast of the dark pairs is checked too.

## Typography

There are two families:

- Pretendard Variable for everything a person reads: titles, body text, labels, and the navigation. It covers Korean and Latin text in one design. Serve the font file from the project's own static files, never from an external CDN, so the page renders the same without outside network access (for example inside a private network). The stack falls back to the system's Korean sans fonts before the file loads.
- D2Coding for data: URLs, IDs, JSON, rules, counts in tables, and code. {typography.data} turns on tabular numerals (`tnum`), so numbers in table columns line up.

Levels:

- {typography.page-title} is the one `h1` of a page, in black weight (900). One per page.
- {typography.section-title} heads a part of a page (`h2`).
- {typography.body} is the running text, 16px with a line height of 1.6. Korean text needs the line height.
- {typography.nav} is the extra-bold navigation link of the header.
- {typography.subsection-title} heads a smaller part inside a section (`h3`), such as one fieldset group.
- {typography.label} is for form labels, buttons, and table headers.
- {typography.caption} is for help text and metadata under a field or a row.

## Layout

- The page is a centered column with a small side padding: {spacing.sm} on a phone, {spacing.lg} on wider screens.
- Working pages (lists, tables, forms, settings) use {spacing.content-width}, so a data table fits without horizontal scrolling on a desktop.
- Reading pages (an article, a summary, a long description) use {spacing.reading-width}, a 768px column, so a line of Korean text stays readable.
- Spacing comes from the `spacing` scale only. {spacing.lg} separates the parts of a form. {spacing.xl} and {spacing.2xl} separate the sections of a page. Table cells use {spacing.sm} and {spacing.xs}.
- On a narrow screen (phone), the header wraps, forms become one column, and a wide table scrolls inside its own box. The page itself never scrolls sideways.
- A long URL in a table cell, and a select with long option labels, stop at {spacing.url-width}. A cell cuts the URL with an ellipsis and keeps the full URL in its `title`.
- Korean text breaks only between words (`word-break: keep-all`), and a button label never breaks.

## Elevation & Depth

The design is flat. There are no shadows. Hierarchy comes from three things only: the weight and size of the titles, the one step from {colors.bg} to {colors.panel}, and the {colors.border} hairlines. A dialog or a confirmation is a separate page, not a floating box.

## Shapes

Every corner is square ({rounded.none}). The navigation highlight is a square teal block, and buttons, inputs, panels, and flash messages follow it. The square shape keeps the UI in the register of a text document, not an app.

## Components

- `page` sets the paper, the ink, and the body type for the whole document.
- `nav-link` is the header navigation: extra-bold teal text with padding. `nav-link-hover` fills the block with {colors.primary} and turns the text white. `nav-link-current` uses the same filled block, so the user always sees which page is open.
- `button` is every ordinary action (filter, save in a list row, cancel). `button-hover` darkens it to {colors.border}.
- `button-primary` is the one main action of a form, such as "저장" or "로그인". At most one per form.
- `button-danger` is for actions that delete, clear, or cannot be undone. It always sits behind a confirmation step.
- `input` covers text fields, selects, and textareas: paper background, a {colors.border} hairline, and a {colors.primary} outline of 2px when focused. Never remove the focus outline.
- `table-header` is the header row of a data table. Body rows have {colors.border} hairlines between them and no zebra stripes.
- `flash-info` and `flash-error` are the messages after an action, at the top of the content, with a left rule of 4px in the text color.
- A note is a neutral explanation, such as why a search found nothing: a `flash` box with the {colors.panel} fill and a {colors.border} rule, because it is neither a success nor a failure.
- `code-block` shows raw values such as JSON and logs. Long lines wrap or scroll inside the block.
- `caption-text`, `data-text`, `page-title`, and `section-title` apply the type levels above.

The component tokens have no border property, so the hairline color {colors.border} is applied directly in the CSS for rows, fieldsets, inputs, and the header.
Lines have three widths: {spacing.hairline} for every border, {spacing.focus-width} for the focus outline, and {spacing.rule-width} for the left rule of a flash message.

## Do's and Don'ts

- **Do** keep teal for links, the navigation, and the main action. **Don't** use it for decoration, icons, or headings.
- **Do** keep red for failures and destructive actions only.
- **Do** take every color, size, and gap from this file through CSS custom properties in the project's stylesheet. **Don't** write a new hex value or pixel size in a template or the CSS without adding its token here first.
- **Don't** add shadows, rounded corners, gradients, or a third surface color.
- **Don't** load fonts, icons, or styles from an external CDN.
