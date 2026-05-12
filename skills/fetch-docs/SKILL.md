---
name: fetch-docs
description: Fetch web-based development documentation and save it as clean markdown files while preserving the site's directory structure. Use this skill whenever the user wants to download, archive, or save online documentation locally — including phrases like "fetch the docs from X", "save this documentation as markdown", "download the docs at [URL]", "convert these web docs to markdown", "archive this docs site", or "cache the API reference from [URL]". Also trigger when a user pastes a docs URL and says they want it saved or stored locally.
---

# fetch-docs

Crawls web-based development documentation and saves it as clean markdown files in a directory structure that mirrors the URL paths.

## Prerequisites

```bash
npx agent-browser --version   # verify
npx defuddle --version        # verify
URL_UTILS="$(find ~/.claude ~/.local/share/chezmoi/.claude -name url_utils.py -path '*/fetch-docs/*' 2>/dev/null | head -1)"
```

## Tool Roles

| Tool | Role |
|------|------|
| **agent-browser** | Opens pages in a real browser and navigates links (handles SPA/JS rendering) |
| **defuddle** | Extracts main content from each page and converts it to clean markdown |
| **url_utils.py** | URL normalization, file path conversion, and scope filtering |

## File Path Resolution Rules

When mapping URLs to file paths, **collect the full URL list first**, then determine all paths at once using the `smart-filepaths` command.
If a URL has child URLs, it is saved as `path/index.md`; otherwise as `path.md`:

```
/reference/commands/   (children: /add/, /apply/ exist)  → reference/commands/index.md
/reference/commands/add/  (no children)                  → reference/commands/add.md
/user-guide/daily-ops/    (no children)                  → user-guide/daily-ops.md
```

## Workflow

### Step 1: Confirm Parameters

```bash
BASE_URL="https://docs.example.com"   # Starting URL for crawl (domain root recommended)
OUTPUT_DIR="./docs-example-com"       # Output directory
COPYRIGHT="(c) Example Corp."         # Upstream copyright holder
LICENSE="All rights reserved (no open license granted)"  # or e.g. "CC-BY-4.0", "GPL-2.0-or-later"
```

Confirm with the user:
- **Start URL**: The root URL of the documentation (may include a path)
- **Output directory**: Defaults to a domain-based name (`./docs-example-com/`)
- **Copyright holder**: Who owns the upstream content (check the site footer / Terms)
- **License**: SPDX identifier if the site grants an open license, otherwise
  "All rights reserved (no open license granted)". See "Attribution Metadata".

### Step 2: Full Navigation Traversal → URL Collection

This is the most critical step. **Every URL must be collected without omission** to determine correct file paths.

```bash
agent-browser open "$BASE_URL"
agent-browser wait --load networkidle
```

#### Expand All Navigation

Many documentation sites have a collapsed sidebar. All sections must be expanded:

```bash
# 1. Take a full snapshot to identify collapsed sections
agent-browser snapshot -i -u

# 2. Click all collapsed sections (toggles/accordions) to expand them
#    Find toggles in the form [LabelText], [button], [details summary] in the snapshot
agent-browser click @e5   # e.g. "Advanced" section toggle
agent-browser click @e9   # e.g. "Reference" section toggle

# 3. Take another snapshot after expanding
agent-browser snapshot -i -u
```

#### URL Extraction Strategy

Choose based on the documentation site's navigation pattern:

**Pattern A — Full Sidebar Traversal** (MkDocs, Docusaurus, etc.):
```bash
# Scope to sidebar area only and extract all links
agent-browser snapshot -i -u -s "nav"
agent-browser snapshot -i -u -s ".sidebar"
agent-browser snapshot -i -u -s ".md-nav"
```

**Pattern B — Per-Section Tab Traversal** (when each section has its own navigation):
```bash
# Navigate to each top-level section page and snapshot its sidebar
for SECTION_URL in "https://docs.ex.com/user-guide/" "https://docs.ex.com/reference/"; do
  agent-browser open "$SECTION_URL"
  agent-browser wait --load networkidle
  agent-browser snapshot -i -u -s "nav"
done
```

**Pattern C — Sitemap** (fast and complete collection):
```bash
# Many sites provide a sitemap.xml
curl -s "https://docs.example.com/sitemap.xml" | grep -oP '<loc>\K[^<]+'
```

#### Supplementing Missing URLs via Iterative Traversal

After saving each page, new links may be discovered on that page:
```bash
# Check for additional links on each saved page
agent-browser open "$PAGE_URL"
agent-browser wait --load networkidle
agent-browser snapshot -i -u
# Add newly discovered URLs to the queue
```

### Step 3: Finalize URL List and Batch-Determine File Paths

Filter the collected URLs and determine file paths:

```bash
# Build all collected links as a JSON array
LINKS='["/guide/install", "https://docs.example.com/guide/usage", ...]'

# Filter in-scope URLs (remove external links, binary files, and duplicates)
VISITED='["https://docs.example.com"]'
FILTERED=$(python3 "$URL_UTILS" filter "$BASE_URL" "$VISITED" "$LINKS")

# Once the full URL list is finalized, determine file paths in batch
# smart-filepaths: automatically chooses path.md vs path/index.md based on whether child URLs exist
echo "$FILTERED" | python3 "$URL_UTILS" smart-filepaths "$BASE_URL"
# Output: {"https://docs.ex.com/guide/": "guide.md", "https://docs.ex.com/reference/": "reference/index.md", ...}
```

### Step 4: Fetch and Save Each Page

Process each URL using the file path mapping:

```bash
PAGE_URL="https://docs.example.com/guide/installation"
REL_PATH="guide/installation.md"   # from smart-filepaths output

# Extract markdown with defuddle
npx defuddle parse "$PAGE_URL" --markdown --output /tmp/page_content.md

# Extract page title
PAGE_TITLE=$(npx defuddle parse "$PAGE_URL" --property title 2>/dev/null)

# Save (include copyright/license metadata — see "Attribution Metadata" below)
FULL_PATH="$OUTPUT_DIR/$REL_PATH"
mkdir -p "$(dirname "$FULL_PATH")"
{
  printf -- "---\ntitle: %s\nsource: %s\ncopyright: %q\nlicense: %q\nretrieved: %s\n---\n\n" \
    "$PAGE_TITLE" "$PAGE_URL" "$COPYRIGHT" "$LICENSE" "$(date +%F)"
  cat /tmp/page_content.md
} > "$FULL_PATH"

echo "Saved: $FULL_PATH"
```

### Step 5: Completion Report

```bash
echo "=== Collection Complete ==="
find "$OUTPUT_DIR" -name "*.md" | sort
echo "Total files: $(find "$OUTPUT_DIR" -name "*.md" | wc -l)"
agent-browser close
```

## URL → File Path Mapping Examples

When `smart-filepaths` is applied (based on the full URL list):

| URL | Has Child URLs | Save Path |
|-----|:---:|-----------|
| `https://docs.ex.com/` | ✓ | `index.md` |
| `https://docs.ex.com/install/` | ✗ | `install.md` |
| `https://docs.ex.com/reference/` | ✓ | `reference/index.md` |
| `https://docs.ex.com/reference/commands/` | ✓ | `reference/commands/index.md` |
| `https://docs.ex.com/reference/commands/add/` | ✗ | `reference/commands/add.md` |
| `https://docs.ex.com/user-guide/daily-ops/` | ✗ | `user-guide/daily-ops.md` |

## Attribution Metadata

Fetched documentation belongs to its original authors. To avoid
implicitly relicensing it under the destination repository's
license, every saved file MUST record source and license metadata,
and each output directory should carry a `NOTICE.md`.

### Per-file frontmatter

```yaml
---
title: <page title>
source: <upstream URL>
copyright: "(c) <original author>"
license: <SPDX id, or "All rights reserved (no open license granted)">
license_url: <license text URL, optional>
retrieved: YYYY-MM-DD
---
```

### Directory NOTICE.md

After the crawl finishes, write a `NOTICE.md` in `OUTPUT_DIR` that
states the upstream source URL, copyright holder, license, and
clarifies that the destination repository's license does not apply
to the cached files:

```bash
cat > "$OUTPUT_DIR/NOTICE.md" <<EOF
# Third-Party Content Notice

Source:    $BASE_URL
Copyright: $COPYRIGHT
License:   $LICENSE

The destination repository's license does NOT apply to the files in
this directory; they remain under the upstream copyright and license
above. If you are the rights holder and wish these files removed,
please open an issue.
EOF
```

### Choosing the license string

- Site is silent about reuse → `"All rights reserved (no open license granted)"`
- Site explicitly grants an open license (CC, GPL, MIT, Apache, etc.)
  → use the SPDX identifier (`CC-BY-4.0`, `GPL-2.0-or-later`, ...)
- When in doubt, ask the user before writing — do NOT invent a
  license that the upstream did not actually grant.

## Edge Cases

### SPA Sites (React, Vue, Vite official docs, etc.)
- `wait --load networkidle` is required
- If there are sidebar toggle buttons, click them and re-snapshot

### Fully Expanding Collapsed Navigation
```bash
# Click all toggles in [LabelText] or [button] form
agent-browser snapshot -i  # check ref
agent-browser click @e12   # click toggle
agent-browser snapshot -i -u  # verify expanded links
```

### When defuddle Extraction Fails
```bash
npx defuddle parse "$PAGE_URL" --json | python3 -c "
import json, sys
d = json.load(sys.stdin)
print('length:', len(d.get('content', '')))
"
# If content is too short, log it and move on
```

### Documentation Requiring Login
```bash
agent-browser auth save docs-site --url https://docs.example.com/login \
  --username user@example.com --password-stdin
agent-browser auth login docs-site
```

## scripts/url_utils.py Command Reference

```bash
# URL → file path (single, simple conversion without child URL info)
python3 "$URL_UTILS" filepath "https://docs.ex.com/guide/install" "https://docs.ex.com"
# → guide/install.md

# URL → file path (single, based on full URL list)
python3 "$URL_UTILS" smart-filepath "https://docs.ex.com/guide/" "https://docs.ex.com" \
  '["https://docs.ex.com/guide/", "https://docs.ex.com/guide/install/"]'
# → guide/index.md  (because child /install/ exists)

# URL → file path batch processing (JSON array via stdin)
echo '["https://docs.ex.com/guide/", "https://docs.ex.com/guide/install/"]' \
  | python3 "$URL_UTILS" smart-filepaths "https://docs.ex.com"
# → {"https://docs.ex.com/guide/": "guide/index.md", "https://docs.ex.com/guide/install/": "guide/install.md"}

# URL normalization (remove fragments)
python3 "$URL_UTILS" normalize "https://docs.ex.com/guide#section"
# → https://docs.ex.com/guide

# Filter link array
python3 "$URL_UTILS" filter \
  "https://docs.ex.com" \
  '["https://docs.ex.com/guide"]' \
  '["/api/ref", "https://external.com", "#skip", "/guide"]'
# → ["https://docs.ex.com/api/ref"]

# Check if URL is in scope
python3 "$URL_UTILS" in-scope "https://docs.ex.com/guide/foo" "https://docs.ex.com"
# → true
```
