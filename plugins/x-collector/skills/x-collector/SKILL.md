---
name: x-collector
description: >
  Collect public X.com (Twitter) posts without the paid X API or a login —
  read a post or thread from its URL, list an account's recent posts, and
  search posts through search engines that index x.com. Use this whenever the
  user shares an x.com or twitter.com link, asks what someone posted on
  X/Twitter, wants an account's posts since some date, or wants to find X
  posts about a topic, even if they don't name X explicitly (e.g. "what did
  @NASA say today?").
---

# Collect public posts from X

All work goes through one bundled script. It runs with `uv` and installs its
own dependencies on first use:

```
uv run --no-project <path-to-this-skill>/scripts/x_collector.py <command> ...
```

Run `<command> --help` for every option. Output is JSON by default; add
`--format md` when you only need to read the posts yourself, because it is
much shorter.

## Pick the command by what the user has

| User has / wants | Command | Backend |
| --- | --- | --- |
| A post URL or ID | `post <url>` | oEmbed → FxTwitter → syndication |
| Metrics, media URLs, quoted post | `post <url> --rich` | FxTwitter → syndication → oEmbed |
| A whole self-thread | `post <url> --thread` | FxTwitter only |
| An account's recent posts | `timeline <handle>` | FxTwitter |
| Posts about a topic | `search "<query>"` | SearXNG or ddgs with `site:x.com` |

Discovery is the hard part, fetching is easy. If the user gives a URL, use
`post`. If they name an account, use `timeline`. Use
`search` only when you have neither, because search results come from Google
and Bing indexes: they lag hours to days, favour popular posts, and are never
complete. Say so when you report search results, so the user does not read
"no results" as "nobody posted about this".

## Reading posts

```
x_collector.py post https://x.com/NASA/status/2111180963661435219 --format md
x_collector.py post <url1> <url2> --rich
x_collector.py post <url> --thread
```

Plain `post` tries the official oEmbed endpoint first because it has the
lowest Terms-of-Service exposure. oEmbed gives only text, author and date;
`t.co` links stay unexpanded and media shows as `pic.twitter.com/...`. Add
`--rich` only when the task needs metrics, media URLs, a quoted post, or a
precise timestamp.

## Account timelines

```
x_collector.py timeline NASA --count 10 --format md
x_collector.py timeline @NASA --since 2026-10-15 --with-replies
x_collector.py timeline NASA --pages 3 --count 100
```

Reposts are excluded unless you pass `--include-reposts`; a repost comes
back as the original post with `is_repost: true`. `--since` pages back until
it reaches the cutoff (up to 10 pages unless `--pages` says otherwise).

The script keeps no state between runs. To check an account for new posts,
pass the time of the last check (or the newest `created_at` you already
have) as `--since`.

## Search

```
x_collector.py search "Artemis II launch" --max 10 --format md
x_collector.py search "rate limit" --from github --timelimit w
x_collector.py search "NASA Artemis" --enrich --max 5
```

- `site:x.com` is added for you. `--from HANDLE` limits results to one account.
- With `SEARXNG_URL` set, the script uses that SearXNG instance (JSON format
  must be enabled); otherwise it uses ddgs with the duckduckgo and yahoo
  backends. Override with `--engine` / `--backend`.
- Search results hold only the engine's title and snippet. `--enrich` fetches
  each post for full text and metrics; it costs one request per result.
- DuckDuckGo blocks quick repeated queries for about 20–30 seconds and then
  reports "No results found". Put everything you need into one query with a
  higher `--max` rather than firing several searches in a row. If a search
  fails with "No results found" on every backend right after another search,
  wait about 30 seconds and retry once before concluding there are no
  results.

## When something fails

The error message names every backend tried and why it failed. Each backend
can break without notice — see [references/backends.md](references/backends.md)
for what each one depends on, its risk, and the last verified status. Report
the failure to the user plainly; do not try a logged-in X session or the X
web client's internal API to work around it. Those violate X's Terms of
Service and risk the user's account.

## Limits to respect

- Public posts only, read-only. The script never posts, likes or logs in.
- Keep volume modest. FxTwitter and the search engines rate-limit or block
  heavy use; do not loop `search` or `timeline` in tight cycles.
- Deleted, protected or age-restricted posts usually fail on every backend.
