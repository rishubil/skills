# fetch-docs

A Claude Code plugin that crawls web-based development documentation and saves it as clean markdown files in a directory structure mirroring the URL paths.

## What it does

When triggered, this skill:

1. Crawls the given documentation URL and its linked pages
2. Converts each page to clean markdown (strips nav, ads, boilerplate)
3. Saves files locally, preserving the site's directory structure

## Prerequisites

```bash
npx agent-browser --version   # headless browser for JS-rendered pages
npx defuddle --version        # HTML-to-markdown converter
```

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install fetch-docs@rishubil-skills
```

## Usage

Trigger phrases include:

- "fetch the docs from X"
- "save this documentation as markdown"
- "download the docs at [URL]"
- "convert these web docs to markdown"
- "archive this docs site"
- "cache the API reference from [URL]"

Also triggers when you paste a docs URL and say you want it saved or stored locally.
