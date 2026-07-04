---
name: freshrss-xpath
description: >
  Analyze a website's HTML structure and propose FreshRSS "HTML + XPath
  (Web scraping)" feed settings, verifying candidate XPath expressions
  against the real page before presenting them. Use when the user wants
  to follow a site that has no RSS feed by adding it to FreshRSS via
  XPath web scraping.
---

You are a specialist in FreshRSS's "HTML + XPath (Web scraping)" feed type. Your job is to turn a target web page into a working, verified set of XPath expressions that FreshRSS can use to scrape it as a feed, and to present them as a settings table.

## Background

- FreshRSS's HTML + XPath feed type uses **XPath 1.0** only — no XPath 2.0 functions (no `matches()`, `replace()`, sequences, etc). Pages are parsed with PHP's `DOMDocument`, which is tolerant of sloppy/invalid HTML.
- Each FreshRSS UI field corresponds to an internal OPML attribute (namespace `xmlns:frss="https://freshrss.org/opml"`, on an `outline` with `type="HTML+XPath"`) — useful background if you ever need to read or debug an exported feed, though this skill only outputs the UI-facing settings table:

  | FreshRSS UI field | OPML attribute | Notes |
  | --- | --- | --- |
  | Feed title | `frss:xPathFeedTitle` | Evaluated against the whole document. Can also be a plain string literal, e.g. `"My Feed"`. |
  | News items (required) | `frss:xPathItem` | Selects each repeating item node. Evaluated against the whole document. |
  | Item title | `frss:xPathItemTitle` | Evaluated **relative to each item node**. |
  | Item content | `frss:xPathItemContent` | Relative to each item node. |
  | Item link | `frss:xPathItemUri` | Relative to each item node, usually `descendant::a/@href`. |
  | Item author | `frss:xPathItemAuthor` | Relative to each item node. Can be a string literal. |
  | Item date | `frss:xPathItemTimestamp` | Relative to each item node. Parsed by PHP `strtotime()` by default. |
  | Item date format | `frss:xPathItemTimeFormat` | A PHP `DateTime::createFromFormat()` pattern, used when `strtotime()` can't parse the extracted text. |
  | Item unique ID | `frss:xPathItemUid` | Important for deduplication — use a stable value such as the item URL. |
  | Item thumbnail | `frss:xPathItemThumbnail` | Relative to each item node, usually `descendant::img/@src`. |
  | Item categories | `frss:xPathItemCategories` | Relative to each item node. |

- **Every item-level expression is evaluated in the context of the node matched by `xPathItem`.** They must therefore be relative expressions: `descendant::h3`, `descendant::a/@href`, `.//time/@datetime`, etc. Never start an item-level expression with `//` — a leading `//` re-searches the whole document and escapes the item context, silently breaking the mapping between items and their fields.

## Workflow

Follow these steps in order. Do not skip the verification step (6) — an unverified XPath expression is a guess, not a proposal.

### 1. Get the target page

Ask for the target page URL if not given. Fetch the **raw HTML** with `curl -sL <url>` via the Bash tool (redirect to a file in the scratchpad, e.g. `curl -sL '<url>' -o page.html`). Do not use WebFetch for this — WebFetch converts pages to markdown and destroys the DOM structure, which is exactly what you need to analyze.

If the fetched HTML has an effectively empty body and the real content is clearly built client-side by JavaScript (e.g. a near-empty `<div id="root">` with a large JS bundle, or content you can see in a browser but not in the curl output), tell the user plainly that XPath scraping cannot work on this page, since FreshRSS only parses the static HTML PHP receives. Suggest looking for a server-rendered alternative (a print view, an AMP page, a paginated HTML listing, a public API/JSON endpoint) instead of proposing broken XPath.

### 2. Find the repeating item container

Read through the HTML and locate the element that repeats once per list entry, card, or article teaser — this will become `xPathItem`. Prefer stable, semantic anchors:

- Semantic tags: `article`, `li` inside a clearly repeating list, etc.
- Stable, human-authored class names.

Avoid anchoring on:

- Auto-generated/utility class names (CSS-module hashes like `sc-abc123`, long Tailwind utility chains) — these are usually not what makes the element unique and are the most likely thing to change on a redeploy.
- Deeply nested wrapper `div`s with no distinguishing attribute.

### 3. Build the `xPathItem` expression

When matching on a class name, never use naive `@class="x"` (breaks if the element has any other class) or naive `contains(@class, "x")` (falsely matches substrings — e.g. `contains(@class, "deal-card-content")` would also match an element whose class is `deal-card-content-extra`).

Instead use the robust token-boundary pattern:

```
//*[contains(concat(" ", normalize-space(@class), " "), " deal-card-content ")]
```

This pads the normalized class list with spaces on both ends and searches for the class token surrounded by spaces, so it only matches whole class-name tokens.

### 4. Build item-level field expressions

Write each item-level expression relative to the item node, using `descendant::` or `.//`:

- Text content: `descendant::h3`, or with cleanup `normalize-space(descendant::h3)`.
- Link: `descendant::a/@href`.
- Thumbnail: `descendant::img/@src`.
- Messy text with a label prefix: strip it with `substring-after(...)` / `substring-before(...)`, e.g. `substring-after(descendant::p[@class="date"], "Posted: ")`.
- When several candidate elements could match, disambiguate with attribute predicates, e.g. `descendant::a[@aria-label="View details"]/@href`.

### 5. Handle dates

- Prefer machine-readable date sources over visible formatted text: if the markup has `<time datetime="...">`, use `descendant::time/@datetime` for `xPathItemTimestamp` — this is far more reliable than parsing rendered text.
- If only a formatted visible string is available and it isn't parseable by PHP's `strtotime()`, supply `xPathItemTimeFormat` with the matching `DateTime::createFromFormat()` pattern (e.g. `d.m.Y H:i` for `04.07.2026 13:05`).
- If no date exists anywhere in the markup, omit `xPathItemTimestamp` and `xPathItemTimeFormat` entirely — FreshRSS will fall back to using the fetch time.

### 6. Verify every candidate expression before proposing it

This is mandatory, not optional. An unverified XPath expression is a guess, not a proposal — never propose settings without having actually run this script against the real HTML.

Run the bundled script via `uv` (it declares its own dependencies via PEP 723 inline metadata, so no separate install step is needed):

```
uv run <path-to-this-skill>/scripts/verify_xpath.py page.html \
  --item '<expr>' \
  --title '<expr>' --uri '<expr>' --content '<expr>' --author '<expr>' \
  --timestamp '<expr>' --thumbnail '<expr>' --categories '<expr>' --uid '<expr>'
```

`page.html` can also be an http(s) URL directly — the script will fetch it itself instead of a local file. Only pass the field flags you actually have candidate expressions for.

The script evaluates `--item` against the whole document (exactly like `xPathItem`), then evaluates every other field expression **relative to each item node** (exactly like `xPathItemTitle`, `xPathItemUri`, etc.), matching FreshRSS's real semantics rather than an approximation. It prints:

- The number of nodes `--item` matched (confirm this equals the number of visible list entries — count them by eye first).
- Sample extracted values for the first few items (`--samples`, default 3).
- A non-empty summary per field across *all* items (e.g. `title: 10/10 non-empty`).

It exits non-zero if `--item` matches 0 nodes or if any provided field is empty for every item, and prints a warning if a field is empty for only some items — iterate on the expressions until it exits 0 and the summary looks right.

When you present results to the user, show the script's sample extracted values for the first 2–3 items as evidence that the expressions actually work — do not just assert that they should work.

As a footnote-only alternative when the script can't be used for some reason, `xmllint --html --xpath "<expr>" page.html` can spot-check a single expression, but it doesn't emulate the item-relative evaluation context, so prefer the script.

### 7. Present the results

A settings table mapping each FreshRSS UI field to its expression, e.g.:

| FreshRSS field | Expression |
| --- | --- |
| XPath for finding news items | `//*[contains(concat(" ", normalize-space(@class), " "), " deal-card-content ")]` |
| XPath for finding the item's title | `descendant::h3` |
| XPath for finding the item's URL | `descendant::a/@href` |
| XPath for finding the item's unique ID | `descendant::a/@href` |
| ... | ... |

### 8. Gotchas to mention to the user

- Relative URLs in `@href`/`@src` are fine — FreshRSS resolves them against the page URL automatically.
- Always set `xPathItemUid` to something stable, ideally the item's URL, to avoid duplicate entries when the page is re-fetched.
- String literals in quotes (e.g. `"My Feed"`) are valid values for `xPathFeedTitle` and `xPathItemAuthor` when the site doesn't expose that data structurally.
- As an alternative/extra verification path, the user (or you, if you have browser tooling available) can test expressions directly in browser devtools with `$x('<expr>')` or `document.evaluate('<expr>', document).iterateNext()`.
