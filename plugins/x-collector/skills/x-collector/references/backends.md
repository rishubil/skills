# x-collector backends

Read this when a command fails or when the user asks how the data is obtained.
Status lines record the last manual check; treat them as history, not
guarantees.

## Constraints behind the design

- No paid X API, no X login, public posts only, read-only.
- Prefer official or crawler-sanctioned paths; accept third-party gray-zone
  paths only where nothing official exists.
- X's `robots.txt` admits only `Googlebot` and `Bingbot` among search
  crawlers, so free full-text search means querying Google- or Bing-derived
  indexes with `site:x.com`.

## Fetch (post by URL)

| Backend | Endpoint | Gives | ToS risk | Last check (2026-10-18) |
| --- | --- | --- | --- | --- |
| oEmbed | `publish.twitter.com/oembed` (301 → `publish.x.com`) | HTML blockquote: text, author, date; no metrics, no media URLs, `t.co` links unexpanded | Low (official) | Works |
| FxTwitter v2 | `api.fxtwitter.com/2/status/{id}`, `/2/thread/{id}` | JSON: full text, author, metrics, media, quote, reply target, community note | Medium (third-party wrapper around X private API) | Works |
| Syndication | `cdn.syndication.twimg.com/tweet-result?id=&token=` | Embed-widget JSON | Medium (undocumented) | Works; tombstones and 404s happen for some posts |

FxTwitter is documented at <https://docs.fxembed.com/api/introduction/>
(OpenAPI: `https://api.fxtwitter.com/2/openapi.json`). Its v2 rate limit is
1,000 requests per minute per IP. Some datacenter egress IPs are refused.

## Account timelines

| Backend | Endpoint | Notes | Last check |
| --- | --- | --- | --- |
| FxTwitter profile statuses | `api.fxtwitter.com/2/profile/{handle}/statuses?cursor=&with_replies=` | `cursor.bottom` pages into older posts; results include reposts and possibly a pinned post out of order, so the script sorts by numeric id instead of trusting order | Works |

## Search

| Engine | How | Last check (ddgs 9.16, residential IP, `site:x.com NASA Artemis`) |
| --- | --- | --- |
| ddgs `duckduckgo` | DuckDuckGo (Bing-derived) | Returns post URLs; rate-limits back-to-back queries (see below) |
| ddgs `yahoo` | Bing-derived | Returns post URLs |
| ddgs `bing`, `yandex` | — | Not registered in ddgs 9.16; ddgs silently falls back to `auto` for unknown names, so the script rejects them |
| ddgs `google`, `startpage` | Google-derived | No results (scraping blocked) |
| ddgs `brave`, `mojeek` | Own crawlers, blocked by robots.txt | No results |
| SearXNG (`SEARXNG_URL`) | Self-hosted metasearch over Google, Bing, DuckDuckGo, Startpage… | Not tested against a real instance; more resilient than one backend |
| FxTwitter `/2/search` | Documented endpoint | `404` with empty results, from both datacenter and residential IPs |

DuckDuckGo answers "No results found" for roughly 20–30 seconds after a few
quick queries; Yahoo then carries the results, and if both are blocked the
search fails outright. From a datacenter IP an earlier test found only
`duckduckgo` returning x.com results. Expect index lag of hours to days,
bias toward popular posts, and blocking under load.

## FxTwitter quirks seen on 2026-10-18

- `/2/profile/{handle}/statuses` ignores `count` and returns about 20–25
  posts per page; the script caps output itself.
- Its `since` parameter returns posts older than the cutoff, so the script
  never sends it and filters by timestamp locally.
- A repost appears as the original post with `reposted_by` set; its `id` is
  the original post's id.
- `/2/thread/{id}` on a post that is not part of a thread returns a
  one-item list.

## Rejected options

| Option | Reason |
| --- | --- |
| X web client internal GraphQL with a session | Clear ToS violation, ban risk, endpoints change often |
| Official X API | Paid |
| Email notifications | Digests only, no per-account alerts, high latency |
| Mobile push (FCM/APNs) | Same scope as web push, harder to emulate |
| Nitter-style front ends | Mostly non-functional |
| xAI API X search | Paid; not evaluated |
| Stateful subscriptions (local store, browser web push, crosspost following) | Left out of scope; use `timeline --since` for new-post checks |
