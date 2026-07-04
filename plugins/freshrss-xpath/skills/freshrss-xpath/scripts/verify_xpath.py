#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["lxml"]
# ///
"""Verify candidate FreshRSS "HTML + XPath" expressions against real HTML.

Emulates FreshRSS's evaluation semantics: `--item` is evaluated against the
whole document to find the repeating item nodes, and every other field
expression is evaluated *relative to each item node* (matching how FreshRSS's
xPathItem* fields work). Prints sample values for the first few items plus a
per-field non-empty summary across all items, warning when a non-categories
field matches more than one value on the same item (likely an over-broad
selector), and exits non-zero if `--item` matches nothing or if any provided
field is empty for every item.

Example:

    uv run verify_xpath.py page.html \\
        --item '//*[contains(concat(" ", normalize-space(@class), " "), " card ")]' \\
        --title 'normalize-space(descendant::h3)' \\
        --uri 'descendant::a/@href' \\
        --thumbnail 'descendant::img/@src'

`source` may also be an http(s) URL, in which case it is fetched directly.
"""

import argparse
import sys
import urllib.request

from lxml import html

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

FIELDS = [
    "title",
    "content",
    "uri",
    "author",
    "timestamp",
    "thumbnail",
    "categories",
    "uid",
]

TRUNCATE_LEN = 80


def load_document(source: str):
    if source.startswith("http://") or source.startswith("https://"):
        req = urllib.request.Request(source, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
    else:
        with open(source, "rb") as f:
            content = f.read()
    return html.fromstring(content)


def node_to_str(node) -> str:
    """Normalize a single XPath result node/value to a display string."""
    if isinstance(node, str):
        # lxml "smart strings" for attribute values, text nodes, or the
        # result of string functions like normalize-space()/substring-after().
        return node
    if hasattr(node, "text_content"):
        # Element node: collapse its text content like FreshRSS/PHP would
        # when treating it as a plain-text field.
        return " ".join(node.text_content().split())
    return str(node)


def eval_values(context, expr: str) -> list[str]:
    """Evaluate an XPath expression and return all matched values as strings."""
    result = context.xpath(expr)
    if isinstance(result, (str, float, int)):
        return [str(result)]
    if isinstance(result, list):
        return [node_to_str(n) for n in result]
    return [str(result)]


def truncate(value: str) -> str:
    if len(value) > TRUNCATE_LEN:
        return value[: TRUNCATE_LEN - 1] + "…"
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("source", help="Local HTML file path or an http(s) URL")
    parser.add_argument(
        "--item",
        required=True,
        help="XPath selecting item nodes (evaluated against the document)",
    )
    parser.add_argument(
        "--feed-title", help="XPath for the feed title (evaluated against the document)"
    )
    for field in FIELDS:
        parser.add_argument(
            f"--{field}",
            help=f"XPath for item {field} (evaluated relative to each item node)",
        )
    parser.add_argument(
        "--samples",
        type=int,
        default=3,
        help="Number of items to print sample values for (default: 3)",
    )
    args = parser.parse_args()

    # Print expressions as parsed (for debugging shell-escaping issues)
    print("Expressions as parsed:")
    print(f"  item: {args.item!r}")
    if args.feed_title:
        print(f"  feed-title: {args.feed_title!r}")
    for field in FIELDS:
        expr = getattr(args, field)
        if expr:
            print(f"  {field}: {expr!r}")
    print()

    doc = load_document(args.source)

    if args.feed_title:
        feed_title_values = eval_values(doc, args.feed_title)
        feed_title = feed_title_values[0] if feed_title_values else ""
        print(f"feed-title: {truncate(feed_title)!r}")

    items = doc.xpath(args.item)
    if not isinstance(items, list):
        items = [items]
    print(f"item: {len(items)} node(s) matched by --item")

    if not items:
        print("ERROR: --item matched 0 nodes.", file=sys.stderr)
        return 1

    field_exprs = {
        field: getattr(args, field) for field in FIELDS if getattr(args, field)
    }
    if not field_exprs:
        print("No field expressions provided; nothing more to verify.")
        return 0

    # Evaluate every field against every item, up front, so samples and the
    # summary are computed from the same data.
    per_item_values: dict[str, list[list[str]]] = {field: [] for field in field_exprs}
    for item in items:
        for field, expr in field_exprs.items():
            try:
                values = eval_values(item, expr)
            except Exception as exc:  # invalid expression, wrong context, etc.
                values = []
                print(
                    f"WARNING: --{field} expression failed on an item: {exc}",
                    file=sys.stderr,
                )
            per_item_values[field].append(values)

    n_samples = min(args.samples, len(items))
    print(f"\nSample values (first {n_samples} of {len(items)} items):")
    for i in range(n_samples):
        print(f"  [item {i}]")
        for field in field_exprs:
            values = per_item_values[field][i]
            if field == "categories":
                display = (
                    ", ".join(truncate(v) for v in values) if values else "(empty)"
                )
            else:
                display = truncate(values[0]) if values else "(empty)"
            print(f"    {field}: {display}")

    print("\nNon-empty summary (all items):")
    any_fully_empty = False
    for field in field_exprs:
        non_empty = sum(
            1 for values in per_item_values[field] if any(v.strip() for v in values)
        )
        total = len(items)
        line = f"  {field}: {non_empty}/{total} non-empty"

        multi_match_count = 0
        first_multi_index = None
        first_multi_len = None
        if field != "categories":
            for i, values in enumerate(per_item_values[field]):
                if len(values) > 1:
                    multi_match_count += 1
                    if first_multi_index is None:
                        first_multi_index = i
                        first_multi_len = len(values)
            if multi_match_count:
                line += f", multiple matches on {multi_match_count}/{total} item(s)"
        print(line)

        if non_empty == 0:
            any_fully_empty = True
            print(f"ERROR: --{field} is empty for every item.", file=sys.stderr)
        elif non_empty < total:
            print(
                f"WARNING: --{field} is empty for {total - non_empty} of {total} item(s).",
                file=sys.stderr,
            )

        if multi_match_count:
            print(
                f"WARNING: --{field} matched more than one value on {multi_match_count} item(s) "
                f"(e.g. item {first_multi_index}: {first_multi_len} values) — the expression may be "
                "over-broad; FreshRSS uses these fields as single values.",
                file=sys.stderr,
            )

    return 1 if any_fully_empty else 0


if __name__ == "__main__":
    sys.exit(main())
