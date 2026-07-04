# freshrss-xpath

A Claude Code plugin that analyzes a website's HTML structure and proposes FreshRSS "HTML + XPath (Web scraping)" feed settings for sites that don't publish an RSS feed.

## What it does

When triggered, this skill:

1. **Fetches** the target page's raw HTML with `curl` (not WebFetch, which destroys DOM structure by converting to markdown)
2. **Identifies** the repeating item container (the element that appears once per list entry/card/article) using stable, semantic anchors
3. **Builds** XPath 1.0 expressions for each FreshRSS field (item, title, link, content, date, thumbnail, unique ID, categories), using robust class-matching and relative `descendant::` expressions
4. **Verifies** every candidate expression against the downloaded HTML with the bundled `verify_xpath.py` script before proposing anything, showing sample extracted values as evidence
5. **Presents** the result as a FreshRSS settings table

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install freshrss-xpath@rishubil-skills
```

## Usage

Trigger phrases include:

- "Add https://example.com/news to FreshRSS as an XPath scraped feed"
- "This site has no RSS feed, help me scrape it with FreshRSS XPath"
- "Build FreshRSS HTML+XPath settings for this page"

Give the skill a target page URL; it will fetch, analyze, verify, and hand back the FreshRSS settings.

## Scripts

| Path | Purpose |
|---|---|
| `scripts/verify_xpath.py` | Verifies candidate XPath expressions against the real page HTML with FreshRSS-like semantics (`--item` against the document, every other field relative to each item node). Runs via `uv run` (PEP 723 inline deps, only `lxml`). |

## Source

Based on:

- [FreshRSS docs — Website scraping (HTML + XPath)](https://freshrss.github.io/FreshRSS/en/users/11_website_scraping.html)
- [Dan Q — FreshRSS + XPath](https://danq.me/2022/09/27/freshrss-xpath/)
- [gedankenstuecke/freshrss-xpath-scraping-settings-examples](https://codeberg.org/gedankenstuecke/freshrss-xpath-scraping-settings-examples)
