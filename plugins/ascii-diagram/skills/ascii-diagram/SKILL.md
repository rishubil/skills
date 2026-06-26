---
name: ascii-diagram
description: >
  Render a simple Mermaid flowchart or sequence diagram as ASCII art using the
  mermaid-ascii CLI and insert the output into documentation, README files, or
  code comments. Use when asked for an "ASCII diagram", "text diagram", or to
  "draw as plain text"; when inserting a diagram into a file that cannot render
  images; or when converting Mermaid syntax to ASCII art.
---

# ascii-diagram

Render simple Mermaid diagrams as ASCII art using the `mermaid-ascii` CLI and
insert the output into the target location.

## Step 1: Locate the binary

```bash
which mermaid-ascii 2>/dev/null || echo "NOT_FOUND"
```

If not found, also check the Go binary path:

```bash
"$(go env GOPATH 2>/dev/null)/bin/mermaid-ascii" --help 2>/dev/null && echo "FOUND_GOPATH" || echo "NOT_FOUND"
```

**If still not found**, present the user with two options and wait for a
response — do NOT proceed automatically:

1. **Install the binary (recommended)**:
   ```bash
   go install github.com/AlexanderGrooff/mermaid-ascii@latest
   ```
   Or download a prebuilt binary from:
   https://github.com/AlexanderGrooff/mermaid-ascii/releases

2. **Use the public web API (no installation needed)**:
   ```bash
   curl https://mermaid-ascii.art -d 'mermaid=graph LR\nA --> B'
   ```
   **Warning**: The diagram content is sent to an external server
   (`mermaid-ascii.art`). Do NOT use this option if the diagram contains
   sensitive information such as internal system names, architecture details,
   or confidential data. Always confirm with the user before sending.

## Step 2: Design the diagram

Work strictly within the supported feature set. Generating unsupported syntax
produces either a fatal error or silently wrong output.

### Supported

| Diagram type | Supported syntax |
|---|---|
| `graph LR` | Left-to-right flowchart, rectangular nodes only |
| `graph TD` / `graph TB` | Top-down flowchart, rectangular nodes only |
| `flowchart LR` / `flowchart TD` | Identical to `graph` equivalents |
| All flowchart types | Labeled edges: `A -->|label| B` |
| All flowchart types | `subgraph name ... end` |
| `sequenceDiagram` | Solid arrow `->>`, dashed arrow `-->>` |
| `sequenceDiagram` | Self-message: `A->>A: text` |
| `sequenceDiagram` | Participant alias: `participant A as Alice` |

### NOT supported — never generate these

| Feature | What happens |
|---|---|
| Non-rectangular node shapes: `A((circle))`, `B{diamond}`, `C([stadium])` | Renders without error but shows raw mermaid syntax as the label text — wrong output |
| `classDiagram`, `stateDiagram`, `gantt`, `pie`, `erDiagram`, `gitGraph` | Fatal parse error |
| Sequence `activate` / `deactivate` | Fatal parse error |
| Sequence `Note right of` / `Note left of` / `Note over` | Fatal parse error |
| Sequence `loop ... end` | Fatal parse error |
| Sequence `alt ... else ... end` | Fatal parse error |
| Sequence `opt ... end` | Fatal parse error |

When the user's request requires unsupported features, say so clearly and
propose a simplified equivalent that stays within the supported set.

### Complexity guideline

Keep diagrams small. More than ~8 nodes or ~10 edges in a flowchart, or
more than ~6 participants with many messages in a sequence diagram, risks
producing illegible ASCII output. When in doubt, split into smaller diagrams.

## Step 3: Write the diagram to a temporary file

Use a heredoc to avoid escaping issues:

```bash
cat > /tmp/diagram.mmd << 'EOF'
graph LR
    A[Start] --> B[Process]
    B --> C[End]
EOF
```

Replace the body with the diagram you designed in Step 2.

**stdin alternative** (if writing to `/tmp` is unavailable):
```bash
printf 'graph LR\n    A[Start] --> B[End]\n' | mermaid-ascii -f -
```

## Step 4: Render

```bash
mermaid-ascii -f /tmp/diagram.mmd -a
```

Use `-a` (pure ASCII: `+---+`, `|`, `-->`) by default. This is the safest
choice for code comments, plain-text files, and environments where Unicode
box-drawing characters may not render correctly.

Omit `-a` only when the output is intended for a Unicode-capable terminal
preview and the user explicitly wants the box-drawing character style.

### Optional padding flags

| Flag | Default | When to adjust |
|---|---|---|
| `-x <n>` | 5 | Reduce to compact wide diagrams |
| `-y <n>` | 5 | Reduce to compact tall diagrams |
| `-p <n>` | 1 | Reduce for a tighter border |

## Step 5: Validate the output

Before inserting, check the result:

- **Raw mermaid syntax visible as a label** (e.g. `A((circle))` inside a box):
  the diagram used an unsupported node shape. Go back to Step 2 and replace
  with a plain rectangular node (`A[circle]`).
- **Fatal error / non-zero exit code**: report the error verbatim to the user.
  Simplify the diagram and retry if the cause is clear.
- **Output wider than ~120 columns**: warn the user and suggest either reducing
  node labels or splitting into multiple smaller diagrams.
- **Empty output**: the diagram may be malformed. Check syntax and retry.

Never insert broken or malformed ASCII art silently.

## Step 6: Insert the output

**In a Markdown file** — wrap in a fenced code block with no language tag:

~~~
```
+-------+     +-----+
|       |     |     |
| Start |---->| End |
|       |     |     |
+-------+     +-----+
```
~~~

**In source code comments** — use the appropriate comment syntax for the
language (e.g. `//`, `#`, `/* ... */`) and indent to match surrounding code.
