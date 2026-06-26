# ascii-diagram

A Claude Code plugin that renders simple Mermaid diagrams as ASCII art using
the [`mermaid-ascii`](https://github.com/AlexanderGrooff/mermaid-ascii) Go CLI
tool and inserts the output into documentation, README files, or code comments.

## What it does

When triggered, this skill:

1. Checks that `mermaid-ascii` is installed; if not, guides you through
   installation or offers the public web API as a fallback.
2. Designs a Mermaid diagram within the tool's supported constraints.
3. Renders the diagram to ASCII art and validates the output.
4. Inserts the result as a plain-text fenced code block (or inline comment) in
   the target location.

### Supported diagram types

| Type | Notes |
|---|---|
| `graph LR` / `graph TD` / `graph TB` | Left-right or top-down flowcharts |
| `flowchart LR` / `flowchart TD` | Identical to `graph` equivalents |
| Subgraphs | `subgraph name ... end` blocks |
| Labeled edges | `A -->|label| B` |
| `sequenceDiagram` | Basic `->>` and `-->>` messages, self-messages, participant aliases |

### Not supported

Non-rectangular node shapes (`((circle))`, `{diamond}`, `([stadium])`),
sequence `activate`/`Note`/`loop`/`alt`/`opt` blocks, and diagram types other
than flowchart and sequence (class, state, Gantt, pie, ER, gitGraph) are not
supported by `mermaid-ascii` and produce errors or wrong output.

## Installation

### 1. Install the mermaid-ascii binary

```bash
go install github.com/AlexanderGrooff/mermaid-ascii@latest
```

Or download a prebuilt binary from the
[releases page](https://github.com/AlexanderGrooff/mermaid-ascii/releases).

> **No Go?** The tool also exposes a public web API at
> https://mermaid-ascii.art that Claude can call via `curl`. Because diagram
> content is sent to an external server, Claude will ask for your confirmation
> before using it and will refuse if the diagram contains sensitive information.

### 2. Install the plugin

```
/plugin marketplace add rishubil/skills
/plugin install ascii-diagram@rishubil-skills
```

## Usage

Typical trigger phrases:

- "add an ASCII diagram showing the request flow"
- "convert this Mermaid diagram to ASCII"
- "draw the architecture as a text diagram for the README"
- "insert a plain-text flowchart in this comment"

## Source

Built around [mermaid-ascii](https://github.com/AlexanderGrooff/mermaid-ascii)
by Alexander Grooff — a Go CLI tool that converts Mermaid diagram syntax to
ASCII art. Official web interface: https://mermaid-ascii.art/
