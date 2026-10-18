# x-collector

A Claude Code plugin that collects public X.com (Twitter) posts without the paid X API and without logging in.

## What it does

The skill gives Claude one bundled CLI script with three jobs:

1. **Read a post or thread** from its URL — official oEmbed first (lowest Terms-of-Service exposure), then FxTwitter and the syndication endpoint for metrics, media and quoted posts
2. **List an account's recent posts** through FxTwitter's profile timeline, optionally everything since a given date
3. **Search posts** through search engines that index x.com (`site:x.com` via ddgs, or a self-hosted SearXNG instance)

Everything is read-only and public-only, and the script keeps no state between runs. Search depends on Google/Bing indexes, so it lags hours to days and is never complete.

No MCP server is included; Claude calls the script directly.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install x-collector@rishubil-skills
```

Requires [`uv`](https://docs.astral.sh/uv/). The script declares its own dependencies (PEP 723), so there is nothing else to install.

## Usage

Trigger phrases include:

- "What does this post say? https://x.com/NASA/status/2111180963661435219"
- "Show me what @NASA posted this week"
- "What has SpaceX posted on X since Monday?"
- "Find X posts about the Artemis II launch"

The script can also be run directly:

```bash
uv run --no-project plugins/x-collector/skills/x-collector/scripts/x_collector.py --help
```

### Environment variables

| Variable | Purpose |
| --- | --- |
| `SEARXNG_URL` | Base URL of a SearXNG instance with the JSON format enabled; when set, `search` uses it instead of ddgs |

## Scripts

| Path | Purpose |
|---|---|
| `skills/x-collector/scripts/x_collector.py` | `uv`-run CLI with `post`, `timeline` and `search` subcommands. Normalizes oEmbed, FxTwitter and syndication responses into one post schema and queries ddgs or SearXNG for search. Outputs JSON or Markdown. |

## Caveats

FxTwitter and the syndication endpoint sit on X's private or undocumented endpoints and can break without notice; search-engine scraping gets rate-limited at volume. See [`skills/x-collector/references/backends.md`](skills/x-collector/references/backends.md) for each backend's risk and last verified status.

## Source

Based on the author's own research notes on free, low-ToS-risk access to X content for AI agents (October 2026), using:

- [FxTwitter / FxEmbed API](https://docs.fxembed.com/api/introduction/)
- [X oEmbed API](https://developer.x.com/en/docs/x-for-websites/oembed-api)
- [ddgs](https://pypi.org/project/ddgs/)
- [SearXNG](https://docs.searxng.org/)
