#!/usr/bin/env python3
"""URL management utilities for fetch-docs skill."""
import sys
import json
import urllib.parse
import os


def normalize_url(url: str) -> str:
    """Remove fragments and trailing slashes for deduplication."""
    parsed = urllib.parse.urlparse(url.strip())
    if parsed.scheme not in ("http", "https"):
        return ""
    cleaned = parsed._replace(fragment="")
    return cleaned.geturl().rstrip("/")


def _strip_base(path: str, base_path: str) -> str:
    """Strip the base path prefix from a URL path."""
    base_path = base_path.rstrip("/")
    if base_path and path.startswith(base_path + "/"):
        path = path[len(base_path):]
    elif base_path and path == base_path:
        path = "/"
    return path or "/"


def url_to_filepath(url: str, base_url: str) -> str:
    """
    Map a URL to a relative markdown file path.
    Trailing-slash URLs become path.md (not path/index.md) because whether
    they need a directory depends on the full URL set — use smart_filepath
    when you have the complete list.

    Examples:
        https://docs.ex.com/        -> index.md
        https://docs.ex.com/guide   -> guide.md
        https://docs.ex.com/guide/  -> guide.md   (leaf assumed)
        https://docs.ex.com/api/ref -> api/ref.md
    """
    parsed = urllib.parse.urlparse(url)
    base_parsed = urllib.parse.urlparse(base_url)

    path = _strip_base(parsed.path, base_parsed.path)

    # Treat the root as index
    if path == "/" or not path.strip("/"):
        return "index.md"

    # Strip trailing slash and append .md
    return path.strip("/") + ".md"


def smart_filepath(url: str, base_url: str, all_urls: list[str]) -> str:
    """
    Map a URL to a markdown path, using subdirectory (path/index.md) only
    when other URLs exist that are direct children of this URL's path.

    Rules:
      - Root URL                 → index.md
      - URL with children        → path/index.md
      - URL without children     → path.md

    Examples (given full URL set):
        /reference/commands/     has children /reference/commands/add/  → reference/commands/index.md
        /user-guide/daily-ops/   no children                            → user-guide/daily-ops.md
        /reference/commands/add/ no children                            → reference/commands/add.md
    """
    parsed = urllib.parse.urlparse(url)
    base_parsed = urllib.parse.urlparse(base_url)

    path = _strip_base(parsed.path, base_parsed.path)

    if path == "/" or not path.strip("/"):
        return "index.md"

    clean_path = path.strip("/")  # e.g. "reference/commands"

    # Check if any other URL is a direct child of this path
    norm_self = normalize_url(url)
    has_children = any(
        normalize_url(u).startswith(norm_self + "/") and normalize_url(u) != norm_self
        for u in all_urls
        if normalize_url(u) != norm_self
    )

    if has_children:
        return clean_path + "/index.md"
    else:
        return clean_path + ".md"


def is_same_scope(url: str, base_url: str) -> bool:
    """Return True if url is within the same host and base path as base_url."""
    try:
        parsed = urllib.parse.urlparse(url)
        base = urllib.parse.urlparse(base_url)
    except Exception:
        return False

    if parsed.scheme not in ("http", "https"):
        return False
    if parsed.netloc != base.netloc:
        return False

    base_path = base.path.rstrip("/")
    if base_path and not parsed.path.startswith(base_path):
        return False

    return True


def filter_doc_links(raw_links: list[str], base_url: str, visited: set[str]) -> list[str]:
    """
    Filter a raw list of href strings to only in-scope, unvisited doc URLs.
    Skips binary extensions, mailto, javascript, and already-visited URLs.
    """
    SKIP_EXTENSIONS = {
        ".pdf", ".zip", ".tar", ".gz", ".png", ".jpg", ".jpeg",
        ".gif", ".svg", ".ico", ".woff", ".woff2", ".ttf", ".eot",
        ".mp4", ".webm", ".mp3", ".ogx",
    }

    seen = set()
    result = []
    for raw in raw_links:
        raw = raw.strip()
        if not raw or raw.startswith(("mailto:", "javascript:", "tel:")):
            continue
        if raw.startswith("#"):
            continue

        resolved = urllib.parse.urljoin(base_url, raw)
        normalized = normalize_url(resolved)
        if not normalized:
            continue

        ext = os.path.splitext(urllib.parse.urlparse(normalized).path)[1].lower()
        if ext in SKIP_EXTENSIONS:
            continue

        if not is_same_scope(normalized, base_url):
            continue
        if normalized in visited or normalized in seen:
            continue

        seen.add(normalized)
        result.append(normalized)

    return result


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""

    if cmd == "filepath":
        # Usage: url_utils.py filepath <url> <base_url>
        url, base_url = sys.argv[2], sys.argv[3]
        print(url_to_filepath(url, base_url))

    elif cmd == "smart-filepath":
        # Usage: url_utils.py smart-filepath <url> <base_url> <all_urls_json>
        url, base_url = sys.argv[2], sys.argv[3]
        all_urls = json.loads(sys.argv[4])
        print(smart_filepath(url, base_url, all_urls))

    elif cmd == "smart-filepaths":
        # Batch version: reads JSON array of URLs from stdin, outputs JSON object {url: path}
        # Usage: echo '["url1","url2"]' | url_utils.py smart-filepaths <base_url>
        base_url = sys.argv[2]
        all_urls = json.loads(sys.stdin.read())
        result = {u: smart_filepath(u, base_url, all_urls) for u in all_urls}
        print(json.dumps(result, indent=2))

    elif cmd == "normalize":
        # Usage: url_utils.py normalize <url>
        print(normalize_url(sys.argv[2]))

    elif cmd == "filter":
        # Usage: url_utils.py filter <base_url> <visited_json> <links_json>
        base_url = sys.argv[2]
        visited = set(json.loads(sys.argv[3]))
        raw_links = json.loads(sys.argv[4])
        filtered = filter_doc_links(raw_links, base_url, visited)
        print(json.dumps(filtered))

    elif cmd == "in-scope":
        # Usage: url_utils.py in-scope <url> <base_url>
        url, base_url = sys.argv[2], sys.argv[3]
        print("true" if is_same_scope(url, base_url) else "false")

    else:
        print(
            "Commands: filepath, smart-filepath, smart-filepaths, normalize, filter, in-scope",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
