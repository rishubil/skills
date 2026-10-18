#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["ddgs>=9.16"]
# ///
"""x-collector: collect public X.com (Twitter) posts without the paid API and without logging in.

Backends (all public, read-only, no credentials):
  oEmbed      publish.twitter.com/oembed        official, text + date only
  FxTwitter   api.fxtwitter.com/2/...           third-party, full data incl. metrics and media
  Syndication cdn.syndication.twimg.com         undocumented embed-widget JSON
  Search      SearXNG (SEARXNG_URL) or ddgs     finds post URLs through web search engines
"""
from __future__ import annotations

import argparse
import html.parser
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

UA = "x-collector/0.1 (+https://github.com/rishubil/skills)"
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
TIMEOUT = 20
POLITE_DELAY = 0.5  # seconds between consecutive per-post fetches
FX_BASE = "https://api.fxtwitter.com"
X_HOSTS = {"x.com", "twitter.com", "mobile.twitter.com", "fxtwitter.com", "fixupx.com", "vxtwitter.com",
           "fixvx.com", "m.twitter.com"}
HANDLE_RE = re.compile(r"^\w{1,15}$")
DEFAULT_BACKENDS = ["duckduckgo", "yahoo"]  # bing/yandex are disabled in ddgs 9.16; others return nothing for x.com


class CollectorError(Exception):
    """Expected failure; reported as a one-line `error: ...` message."""


class HttpError(CollectorError):
    def __init__(self, status: int, message: str):
        super().__init__(message)
        self.status = status


# --------------------------------------------------------------------------- HTTP

def http_get(url: str) -> tuple[int, bytes]:
    """GET with our UA; retry once with a browser UA if the endpoint answers 403."""
    for ua in (UA, BROWSER_UA):
        req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 403 and ua == UA:
                continue
            return e.code, e.read()
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            host = urllib.parse.urlsplit(url).netloc
            raise CollectorError(f"network error talking to {host}: {getattr(e, 'reason', e)}") from e
    raise AssertionError("unreachable")


def get_json(url: str):
    """Return parsed JSON, or None for an empty body (HTTP 204). Raises HttpError on status >= 400."""
    status, body = http_get(url)
    text = body.decode("utf-8", errors="replace").strip()
    if status >= 400:
        msg = ""
        try:
            msg = json.loads(text).get("message") or ""
        except (ValueError, AttributeError):
            pass
        raise HttpError(status, f"HTTP {status}" + (f" ({msg})" if msg else ""))
    if not text:
        return None
    try:
        return json.loads(text)
    except ValueError:
        raise CollectorError(f"HTTP {status} but the response was not JSON") from None


def fx_get(path: str, **params):
    qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    return get_json(f"{FX_BASE}{path}" + (f"?{qs}" if qs else ""))


def polite(i: int) -> None:
    if i:
        time.sleep(POLITE_DELAY)


# --------------------------------------------------------------------------- input parsing

def parse_post_ref(ref: str) -> tuple[str, str | None]:
    """Return (status id, handle or None) from a URL or bare numeric id."""
    ref = ref.strip()
    if ref.isdigit():
        return ref, None
    url = ref if "://" in ref else "https://" + ref
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    segs = [s for s in parts.path.split("/") if s]
    if host in X_HOSTS:
        # /<handle>/status/<id>, /i/status/<id>, /i/web/status/<id>
        for i, seg in enumerate(segs):
            if seg in ("status", "statuses") and i + 1 < len(segs) and segs[i + 1].isdigit():
                handle = segs[0] if i >= 1 and segs[0] not in ("i", "web") else None
                if handle and not HANDLE_RE.match(handle):
                    handle = None
                return segs[i + 1], handle
    raise CollectorError(f"not a recognizable X post URL or id: {ref!r}")


def norm_handle(s: str) -> str:
    """Accept `handle`, `@handle` or a profile URL."""
    s = s.strip()
    if "/" in s or s.lower().startswith(("x.com", "twitter.com")):
        segs = [p for p in urllib.parse.urlsplit(s if "://" in s else "https://" + s).path.split("/") if p]
        s = segs[0] if segs else ""
    s = s.lstrip("@")
    if not HANDLE_RE.match(s):
        raise CollectorError(f"invalid X handle: {s!r}")
    return s


def parse_since(s: str) -> int:
    if re.fullmatch(r"\d{9,}", s):
        return int(s)
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        raise CollectorError(f"--since must be an ISO date/datetime or unix seconds, got {s!r}") from None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp())


def iso_from_ts(ts: int | float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------- normalized post model

def make_post(pid: str, handle: str | None, source: str, **kw) -> dict:
    return {
        "id": str(pid),
        "url": f"https://x.com/{handle or 'i'}/status/{pid}",
        "author": {"handle": handle, "name": kw.get("name"), "id": kw.get("user_id")},
        "created_at": kw.get("created_at"),
        "text": kw.get("text", ""),
        "lang": kw.get("lang"),
        "metrics": kw.get("metrics"),
        "media": kw.get("media", []),
        "quote": kw.get("quote"),
        "reply_to": kw.get("reply_to"),
        "is_repost": False,
        "repost_of": None,
        "community_note": kw.get("community_note"),
        "source": source,
    }


def media_type(raw: str | None) -> str:
    raw = (raw or "").lower()
    if "gif" in raw:
        return "gif"
    if "vid" in raw:
        return "video"
    return "photo"


# ---- FxTwitter

def norm_fx(s: dict) -> dict:
    a = s.get("author") or {}
    handle = a.get("screen_name")
    ts = s.get("created_timestamp")
    media = []
    for m in (s.get("media") or {}).get("all") or []:
        media.append({"type": media_type(m.get("type")), "url": m.get("url"),
                      "thumbnail_url": m.get("thumbnail_url")})
    rt = s.get("replying_to")
    reply_to = None
    if isinstance(rt, dict):
        reply_to = {"handle": rt.get("screen_name"), "id": rt.get("status")}
    elif rt:
        reply_to = {"handle": str(rt), "id": None}
    note = s.get("community_note")
    if isinstance(note, dict):
        note = note.get("text") or json.dumps(note, ensure_ascii=False)
    metrics = {
        "likes": s.get("likes"),
        "reposts": s["reposts"] if "reposts" in s else s.get("retweets"),
        "replies": s.get("replies"),
        "quotes": s.get("quotes"),
        "views": s.get("views"),
        "bookmarks": s.get("bookmarks"),
    }
    post = make_post(
        s["id"], handle, "fxtwitter", name=a.get("name"), user_id=a.get("id"),
        created_at=iso_from_ts(ts) if ts else None, text=s.get("text") or "", lang=s.get("lang"),
        metrics=metrics, media=media, quote=norm_fx(s["quote"]) if s.get("quote") else None,
        reply_to=reply_to, community_note=note or None)
    rb = s.get("reposted_by")
    if rb:
        post["is_repost"] = True
        post["repost_of"] = {"reposted_by": {"handle": rb.get("screen_name"), "name": rb.get("name"),
                                              "id": rb.get("id")}}
    return post


def fetch_fx(pid: str, handle: str | None) -> dict:
    d = fx_get(f"/2/status/{pid}")
    if not d or not d.get("status"):
        raise CollectorError("empty response")
    return norm_fx(d["status"])


# ---- Syndication

def syndication_token(pid: str) -> str:
    """Port of JS `((Number(id)/1e15)*Math.PI).toString(36).replace(/(0+|\\.)/g, '')`."""
    x = (int(pid) / 1e15) * math.pi
    n = int(x)
    frac = x - n
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    ip = ""
    while n:
        n, r = divmod(n, 36)
        ip = digits[r] + ip
    fp = ""
    for _ in range(11):
        frac *= 36
        d = int(frac)
        fp += digits[d]
        frac -= d
    return (ip + fp).replace("0", "")


def norm_syndication(t: dict) -> dict:
    text = t.get("text") or ""
    ent = t.get("entities") or {}
    for u in ent.get("urls") or []:
        text = text.replace(u["url"], u.get("expanded_url") or u["url"])
    for m in ent.get("media") or []:
        text = text.replace(m["url"], "")
    user = t.get("user") or {}
    media = []
    for m in t.get("mediaDetails") or []:
        kind = media_type(m.get("type") if m.get("type") != "animated_gif" else "gif")
        url = m.get("media_url_https")
        if kind != "photo":
            mp4 = [v for v in (m.get("video_info") or {}).get("variants", []) if v.get("content_type") == "video/mp4"]
            if mp4:
                url = max(mp4, key=lambda v: v.get("bitrate", 0))["url"]
        media.append({"type": kind, "url": url, "thumbnail_url": m.get("media_url_https")})
    created = t.get("created_at")
    if created:
        created = re.sub(r"\.\d+Z$", "Z", created)
    reply_to = None
    if t.get("in_reply_to_screen_name") or t.get("in_reply_to_status_id_str"):
        reply_to = {"handle": t.get("in_reply_to_screen_name"), "id": t.get("in_reply_to_status_id_str")}
    metrics = {"likes": t.get("favorite_count"), "reposts": None, "replies": t.get("conversation_count"),
               "quotes": None, "views": None, "bookmarks": None}
    return make_post(
        t["id_str"], user.get("screen_name"), "syndication", name=user.get("name"), user_id=user.get("id_str"),
        created_at=created, text=text.strip(), lang=t.get("lang"), metrics=metrics, media=media,
        quote=norm_syndication(t["quoted_tweet"]) if t.get("quoted_tweet") else None, reply_to=reply_to)


def fetch_syndication(pid: str, handle: str | None) -> dict:
    d = None
    last: CollectorError | None = None
    for token in (syndication_token(pid), "a"):
        try:
            d = get_json(f"https://cdn.syndication.twimg.com/tweet-result?id={pid}&token={token}")
        except CollectorError as e:
            last = e
            if isinstance(e, HttpError) and e.status == 404:
                break
            continue
        if d:
            break
    if not d:
        raise last or CollectorError("empty response")
    if d.get("__typename") != "Tweet":
        raise CollectorError(f"post unavailable ({d.get('__typename', 'unknown type')})")
    return norm_syndication(d)


# ---- oEmbed

class OEmbedParser(html.parser.HTMLParser):
    """Extract text, language and date from the oEmbed blockquote HTML."""

    def __init__(self):
        super().__init__()
        self.in_p = False
        self.depth_a = 0
        self.parts: list[str] = []
        self.lang: str | None = None
        self.last_a_text = ""
        self._a_buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "p" and not self.parts and not self.in_p:
            self.in_p = True
            self.lang = dict(attrs).get("lang")
        elif tag == "br" and self.in_p:
            self.parts.append("\n")
        elif tag == "a":
            self.depth_a += 1
            self._a_buf = []

    def handle_endtag(self, tag):
        if tag == "p" and self.in_p:
            self.in_p = False
        elif tag == "a" and self.depth_a:
            self.depth_a -= 1
            self.last_a_text = "".join(self._a_buf).strip()

    def handle_data(self, data):
        if self.in_p:
            self.parts.append(data)
        if self.depth_a:
            self._a_buf.append(data)


def fetch_oembed(pid: str, handle: str | None) -> dict:
    target = f"https://twitter.com/{handle or 'i'}/status/{pid}"
    d = get_json("https://publish.twitter.com/oembed?" + urllib.parse.urlencode(
        {"url": target, "omit_script": 1, "dnt": 1}))
    if not isinstance(d, dict) or "html" not in d:
        raise CollectorError("no oEmbed data")
    p = OEmbedParser()
    p.feed(d["html"])
    text = "".join(p.parts).strip()
    created = None
    try:
        created = datetime.strptime(p.last_a_text, "%B %d, %Y").date().isoformat()
    except ValueError:
        pass
    segs = [s for s in urllib.parse.urlsplit(d.get("author_url", "")).path.split("/") if s]
    author = segs[0] if segs else handle
    return make_post(pid, author, "oembed", name=d.get("author_name"), created_at=created,
                     text=text, lang=p.lang)


FETCHERS = {"oembed": fetch_oembed, "fxtwitter": fetch_fx, "syndication": fetch_syndication}


def fetch_post(pid: str, handle: str | None, source: str = "auto", rich: bool = False) -> dict:
    if source == "auto":
        order = ["fxtwitter", "syndication", "oembed"] if rich else ["oembed", "fxtwitter", "syndication"]
    else:
        order = [source]
    errors = []
    for name in order:
        try:
            return FETCHERS[name](pid, handle)
        except CollectorError as e:
            errors.append(f"{name}: {e}")
        except (KeyError, TypeError, ValueError) as e:
            errors.append(f"{name}: unexpected response shape ({e!r})")
    raise CollectorError(f"could not fetch post {pid}; tried " + "; ".join(errors))


# --------------------------------------------------------------------------- timeline

def fx_statuses(handle: str, count: int, cursor: str | None = None, with_replies: bool = False):
    """One page of profile statuses. Returns (normalized posts, next cursor or None)."""
    d = fx_get(f"/2/profile/{handle}/statuses", count=count, cursor=cursor,
               with_replies=1 if with_replies else None)
    if not d:
        return [], None
    posts = [norm_fx(s) for s in d.get("results") or []]
    return posts, (d.get("cursor") or {}).get("bottom")


def collect_timeline(handle: str, count: int, pages: int, with_replies: bool, include_reposts: bool,
                     since: int | None) -> list[dict]:
    seen: dict[str, dict] = {}
    cursor = None
    for page in range(pages):
        polite(page)
        posts, cursor = fx_statuses(handle, count, cursor, with_replies)
        if not posts:
            break
        for p in posts:
            seen.setdefault(p["id"], p)
        if since is not None:
            # Stop paging once a page reaches posts older than --since (skip the first item: may be pinned).
            tail = [p for p in posts[1:] if not p["is_repost"] and p["created_at"]] or posts
            if any(datetime.fromisoformat(p["created_at"].replace("Z", "+00:00")).timestamp() < since
                   for p in tail if p["created_at"]):
                break
        if not cursor:
            break
    out = list(seen.values())
    if not include_reposts:
        out = [p for p in out if not p["is_repost"]]
    if since is not None:
        out = [p for p in out if p["created_at"] and
               datetime.fromisoformat(p["created_at"].replace("Z", "+00:00")).timestamp() >= since]
    out.sort(key=lambda p: int(p["id"]), reverse=True)
    # FxTwitter currently ignores `count` and returns ~20-25 per page, so cap client-side.
    # With --since the date filter is the limit instead.
    return out if since is not None else out[:count * pages]


# --------------------------------------------------------------------------- search

STATUS_URL_RE = re.compile(
    r"https?://(?:www\.|mobile\.|m\.)?(?:x|twitter)\.com/(\w{1,15})/status(?:es)?/(\d+)", re.I)
TIME_RANGE = {"d": "day", "w": "week", "m": "month", "y": "year"}


def add_hit(items: dict, url: str, title, snippet, engine: str, backend) -> None:
    m = STATUS_URL_RE.match(url or "")
    if not m or m.group(1).lower() in ("i", "web") or m.group(2) in items:
        return
    handle, pid = m.group(1), m.group(2)
    items[pid] = {"id": pid, "url": f"https://x.com/{handle}/status/{pid}", "handle": handle,
                  "title": title, "snippet": snippet, "engine": engine, "backend": backend}


def search_ddgs(query: str, max_n: int, timelimit: str | None, backends: list[str]) -> tuple[dict, list[str]]:
    try:
        from ddgs import DDGS
    except ImportError as e:
        raise CollectorError(f"ddgs is not installed ({e}); run via `uv run --script`") from e
    try:
        from ddgs.engines import ENGINES
        bad = [b for b in backends if b != "auto" and b not in ENGINES["text"]]
        if bad:  # ddgs would silently fall back to 'auto' for unknown names
            raise CollectorError(f"unknown ddgs backend(s): {', '.join(bad)}; available: "
                                 + ", ".join(sorted(ENGINES["text"])))
    except ImportError:
        pass
    items: dict = {}
    errors: list[str] = []
    for b in backends:
        try:
            # Ask for extra results: many hits are profiles or non-post pages and get filtered out.
            res = DDGS(timeout=15).text(query, backend=b, max_results=max(max_n * 3, 20), timelimit=timelimit)
        except Exception as e:  # DDGSException, timeouts, rate limits: tolerate per backend
            errors.append(f"ddgs/{b}: {str(e).strip() or type(e).__name__}")
            continue
        before = len(items)
        for r in res or []:
            add_hit(items, r.get("href", ""), r.get("title"), r.get("body"), "ddgs", b)
        if len(items) == before:
            errors.append(f"ddgs/{b}: no post URLs in {len(res or [])} results")
        if len(items) >= max_n:
            break
    return items, errors


def search_searxng(query: str, max_n: int, timelimit: str | None, base: str) -> tuple[dict, list[str]]:
    items: dict = {}
    for page in range(1, 4):
        params = {"q": query, "format": "json", "pageno": page}
        if timelimit:
            params["time_range"] = TIME_RANGE[timelimit]
        try:
            d = get_json(f"{base.rstrip('/')}/search?" + urllib.parse.urlencode(params))
        except HttpError as e:
            hint = " (enable `json` under search.formats in the instance's settings.yml)" if e.status == 403 else ""
            return items, [f"searxng: {e}{hint}"]
        except CollectorError as e:
            return items, [f"searxng: {e}"]
        results = (d or {}).get("results") or []
        for r in results:
            add_hit(items, r.get("url", ""), r.get("title"), r.get("content"), "searxng", r.get("engine"))
        if not results or len(items) >= max_n:
            break
    return items, ([] if items else ["searxng: no post URLs in results"])


def search_fxtwitter(query: str, max_n: int) -> tuple[dict, list[str]]:
    try:
        d = fx_get("/2/search", q=query, feed="latest", count=min(max_n, 100))
    except CollectorError as e:
        return {}, [f"fxtwitter: search endpoint failed: {e} (it is currently non-functional upstream)"]
    results = (d or {}).get("results") or []
    if not results:
        return {}, ["fxtwitter: search returned no results (the endpoint is currently non-functional upstream)"]
    items = {}
    for s in results:
        p = norm_fx(s)
        items[p["id"]] = {"id": p["id"], "url": p["url"], "handle": p["author"]["handle"], "title": None,
                          "snippet": p["text"], "engine": "fxtwitter", "backend": None, "post": p}
    return items, []


def cmd_search(args):
    q = args.query.strip()
    engine = args.engine
    if engine == "auto":
        engine = "searxng" if os.environ.get("SEARXNG_URL") else "ddgs"
    if engine == "fxtwitter":
        items, errors = search_fxtwitter(q, args.max)
    else:
        if args.from_handle:
            if "site:" in q.lower():
                raise CollectorError("--from cannot be combined with an explicit site: operator in the query")
            q = f"site:x.com/{norm_handle(args.from_handle)} {q}"
        elif "site:" not in q.lower():
            q = f"site:x.com {q}"
        if engine == "searxng":
            base = os.environ.get("SEARXNG_URL")
            if not base:
                raise CollectorError("--engine searxng needs the SEARXNG_URL environment variable "
                                     "(e.g. http://localhost:8080)")
            items, errors = search_searxng(q, args.max, args.timelimit, base)
        else:
            backends = [b.strip() for b in args.backend.split(",") if b.strip()] if args.backend else DEFAULT_BACKENDS
            items, errors = search_ddgs(q, args.max, args.timelimit, backends)
    if not items:
        raise CollectorError(f"no post URLs found for {q!r}; tried " + "; ".join(errors))
    out = list(items.values())[:args.max]
    if errors and len(out) < args.max:
        print("warning: some backends gave nothing: " + "; ".join(errors), file=sys.stderr)
    print("note: search engine indexes lag by hours to days and favour popular posts; "
          "use `timeline` for fresh posts from a known account.", file=sys.stderr)
    if args.enrich:
        for i, it in enumerate(out):
            if "post" in it:
                continue
            polite(i)
            try:
                it["post"] = fetch_post(it["id"], it["handle"], "auto", rich=True)
            except CollectorError as e:
                it["post_error"] = str(e)
    return out


# --------------------------------------------------------------------------- output

def fmt_num(n) -> str:
    return f"{n:,}" if isinstance(n, int) else str(n)


def post_md(p: dict, prefix: str = "") -> str:
    a = p["author"]
    who = f"{a['name']} (@{a['handle']})" if a.get("name") else f"@{a['handle']}"
    head = f"**{who}** · {p['created_at'] or 'date unknown'} · {p['url']}"
    if p.get("is_repost"):
        rb = (p.get("repost_of") or {}).get("reposted_by") or {}
        head = f"[reposted by @{rb.get('handle')}] " + head
    lines = [head, ""] + (p["text"].split("\n") if p["text"] else [])
    m = p.get("metrics")
    if m:
        shown = [f"{k} {fmt_num(v)}" for k, v in m.items() if v is not None]
        if shown:
            lines += ["", " · ".join(shown)]
    if p.get("reply_to"):
        rt = p["reply_to"]
        lines += ["", f"in reply to @{rt.get('handle')}" + (f" ({rt['id']})" if rt.get("id") else "")]
    if p.get("media"):
        lines += [""] + [f"- {x['type']}: {x['url']}" for x in p["media"]]
    if p.get("community_note"):
        lines += ["", f"community note: {p['community_note']}"]
    if p.get("quote"):
        lines += [""] + ["> " + ln if ln else ">" for ln in post_md(p["quote"]).split("\n")]
    return "\n".join(prefix + ln if ln else prefix.rstrip() for ln in lines)


def to_md(obj, kind: str) -> str:
    if kind == "posts":
        if isinstance(obj, dict):
            obj = [obj]
        blocks = []
        for p in obj:
            if isinstance(p, list):  # --thread with several refs
                blocks.append("\n\n---\n\n".join(post_md(x) for x in p))
            elif "error" in p and "text" not in p:
                blocks.append(f"error for {p.get('ref')}: {p['error']}")
            else:
                blocks.append(post_md(p))
        return "\n\n---\n\n".join(blocks)
    if kind == "search":
        blocks = []
        for it in obj:
            line = f"- {it['url']}" + (f" ({it['engine']}/{it['backend']})" if it.get("backend") else f" ({it['engine']})")
            if it.get("title"):
                line += f"\n  {it['title']}"
            if it.get("snippet"):
                line += f"\n  {' '.join(it['snippet'].split())}"
            if it.get("post"):
                line += "\n\n" + post_md(it["post"], "  ") + "\n"
            if it.get("post_error"):
                line += f"\n  enrich failed: {it['post_error']}"
            blocks.append(line)
        return "\n".join(blocks)


def emit(obj, fmt: str, kind: str) -> None:
    if fmt == "md":
        print(to_md(obj, kind))
    else:
        print(json.dumps(obj, ensure_ascii=False, indent=2))


# --------------------------------------------------------------------------- command handlers

def cmd_post(args):
    refs = [parse_post_ref(r) for r in args.refs]
    out, failed = [], False
    for i, (pid, handle) in enumerate(refs):
        polite(i)
        try:
            if args.thread:
                d = fx_get(f"/2/thread/{pid}")
                posts = [norm_fx(s) for s in (d or {}).get("thread") or []]
                if not posts:
                    raise CollectorError("FxTwitter returned an empty thread")
                posts.sort(key=lambda p: int(p["id"]))
                out.append(posts)
            else:
                out.append(fetch_post(pid, handle, args.source, args.rich))
        except CollectorError as e:
            failed = True
            msg = f"could not fetch thread for {pid} via fxtwitter: {e}" if args.thread else str(e)
            if len(refs) == 1:
                raise CollectorError(msg) from None
            print(f"error: {msg}", file=sys.stderr)
            out.append({"ref": args.refs[i], "id": pid, "error": msg})
    return (out[0] if len(out) == 1 else out), failed


def cmd_timeline(args):
    handle = norm_handle(args.handle)
    if not 1 <= args.count <= 100:
        raise CollectorError("--count must be between 1 and 100")
    pages = args.pages if args.pages is not None else (10 if args.since else 1)
    if pages < 1:
        raise CollectorError("--pages must be >= 1")
    since = parse_since(args.since) if args.since else None
    return collect_timeline(handle, args.count, pages, args.with_replies, args.include_reposts, since)


def build_parser() -> argparse.ArgumentParser:
    def common(p: argparse.ArgumentParser, top: bool = False):
        p.add_argument("--format", choices=["json", "md"], default="json" if top else argparse.SUPPRESS,
                       help="output format (default: json)")

    ap = argparse.ArgumentParser(
        prog="x_collector.py",
        description="Collect public X.com posts without the paid API or a login. Read-only; no credentials.",
        epilog="Environment: SEARXNG_URL (search via SearXNG). "
               "Errors go to stderr as `error: ...` with exit code 1.")
    common(ap, top=True)
    sub = ap.add_subparsers(dest="cmd", required=True, metavar="COMMAND")

    p = sub.add_parser("post", help="fetch one or more posts by URL or id",
                       description="Fetch posts. Default chain: oembed -> fxtwitter -> syndication "
                                   "(official first). --rich flips it to fxtwitter -> syndication -> oembed.")
    p.add_argument("refs", nargs="+", metavar="URL_OR_ID",
                   help="x.com/twitter.com/fxtwitter.com/... status URL, /i/status/ID, or numeric id")
    p.add_argument("--rich", action="store_true", help="prefer sources with metrics, media, quote, author id")
    p.add_argument("--thread", action="store_true", help="return the author's self-thread (FxTwitter only)")
    p.add_argument("--source", choices=["auto", "oembed", "fxtwitter", "syndication"], default="auto",
                   help="force one backend (default: auto)")
    common(p)
    p.set_defaults(fn=cmd_post, kind="posts")

    p = sub.add_parser("timeline", help="recent posts of an account (FxTwitter)",
                       description="List recent posts of a public account, newest first. Reposts and replies "
                                   "are excluded unless requested.")
    p.add_argument("handle", help="handle, @handle or profile URL")
    p.add_argument("--count", type=int, default=20,
                   help="posts per page, 1-100 (default: 20); ignored when --since is given")
    p.add_argument("--pages", type=int, help="max pages to fetch (default: 1, or 10 with --since)")
    p.add_argument("--since", help="only posts at/after this ISO date, ISO datetime (UTC if no tz) or unix seconds")
    p.add_argument("--with-replies", action="store_true", help="include the account's replies")
    p.add_argument("--include-reposts", action="store_true", help="include reposts (marked is_repost)")
    common(p)
    p.set_defaults(fn=cmd_timeline, kind="posts")

    p = sub.add_parser("search", help="find posts through web search engines (SearXNG or ddgs)",
                       description="Search for posts with a web search engine (site:x.com ...). Index lag is "
                                   "hours to days and popular posts are favoured. Use --enrich for full data.")
    p.add_argument("query")
    p.add_argument("--max", type=int, default=10, help="max results (default: 10)")
    p.add_argument("--timelimit", choices=["d", "w", "m", "y"], help="day/week/month/year")
    p.add_argument("--engine", choices=["auto", "searxng", "ddgs", "fxtwitter"], default="auto",
                   help="auto = searxng if SEARXNG_URL is set, else ddgs. fxtwitter is opt-in and "
                        "currently non-functional upstream")
    p.add_argument("--backend", help="comma-separated ddgs backends tried in order (default: duckduckgo,yahoo; "
                                     "google/brave/mojeek/startpage currently return nothing for x.com)")
    p.add_argument("--enrich", action="store_true", help="fetch each result with the --rich post chain")
    p.add_argument("--from", dest="from_handle", metavar="HANDLE", help="only posts of this account")
    common(p)
    p.set_defaults(fn=cmd_search, kind="search")
    return ap


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.cmd == "post":
            result, failed = args.fn(args)
            emit(result, args.format, "posts")
            return 1 if failed else 0
        result = args.fn(args)
        emit(result, args.format, args.kind)
        return 0
    except CollectorError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    except BrokenPipeError:
        return 0
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
