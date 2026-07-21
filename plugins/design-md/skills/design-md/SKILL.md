---
name: design-md
description: >
  Creates, maintains, and applies a DESIGN.md — the Google Labs format that
  pins a project's visual identity as design tokens plus prose so UI stays
  consistent across sessions, agents, and tools. Use whenever the user talks
  about a project's design system, visual identity,
  brand look and feel, color palette, typography scale, spacing/radius tokens,
  or component styling; whenever DESIGN.md or "design tokens" is mentioned
  explicitly; whenever the complaint is that the UI keeps drifting or looking
  inconsistent between sessions or agents; whenever the user wants to export a
  theme to Tailwind or tokens.json; and whenever a DESIGN.md already exists
  anywhere in the repo and the user asks for ANY UI work, even if they never
  say the word "design".
---

<!-- Based on the DESIGN.md format from Google Labs:
     https://github.com/google-labs-code/design.md -->

# DESIGN.md

DESIGN.md is a plain-text, checked-in file that records a project's visual
identity — colors, typography, spacing, shape, and component styling — as
both machine-readable tokens and human-readable prose. Read it before any UI
work, write it when a project doesn't have one, and keep it current as the
design evolves.

## Why the file exists

An agent has no memory between sessions, and different agents and tools
working on the same project have no shared memory with each other. Without a
written record, every session that touches UI re-derives "what does this
product look like" from scratch — usually by inventing something plausible
and slightly different each time. Buttons drift, spacing scales multiply,
and two features built a week apart look like they came from different
products. DESIGN.md exists to make the visual identity a durable artifact
instead of something reconstructed from vibes on every run: one file that
every session, every agent, and every tool can read and follow.

## The file at a glance

```markdown
---
name: Daylight Prestige
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  on-primary: "#F7F5F2"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
---

## Overview

A graduate-level computer science lecture handout in the tradition of an
old established university. Austere, informationally dense, and proudly
unconcerned with first impressions.

## Colors

- **Primary** {colors.primary} is a deep ink used for headlines and core
  text to give maximum readability and a sense of permanence.
```

The YAML front matter holds design tokens (`colors`, `typography`,
`rounded`, `spacing`, `components`, and any custom group). The markdown body
is eight `##` sections, in a fixed order, that explain what the tokens mean
and why. Sections may be omitted, but any that are present must stay in
order: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes
→ Components → Do's and Don'ts.

## The rule that decides quality

Everything below matters more than getting the token values exactly right.
A DESIGN.md with perfect hex codes and thin prose produces worse output
than one with rough tokens and a sharp, specific Overview.

**Prose, not tokens, is the specification.** The tokens are context for the
prose, not rendering instructions the agent executes literally. A model
reading `primary: "#1A1C1E"` on its own has a color and no idea what it's
for. A model reading "{colors.primary} is a deep ink used for headlines and
core text to give a sense of permanence, never used as a background fill"
has a rule it can apply to cases the token alone could never cover. Treat
the token block as an index into the prose, not the other way around.

**A specific reference beats a pile of adjectives.** "Modern, clean,
trustworthy, premium" describes a large, fuzzy region of design space — a
model asked to hit that region produces something generic, because
"generic-but-premium" is the centroid of the region. "A 1970s graduate CS
lecture handout from an old university" or "a Braun kitchen appliance
manual" names a single point. That one sentence carries the one-ink color
system, the generous margins, the reading-size serif, and the absence of
decoration — all without being stated. Whenever a design brief arrives as
adjectives, push back and ask for the concrete object those adjectives are
approximating.

**Negative constraints arrive for free with a specific reference.** A model
that knows what a lecture handout *is* also knows what it *is not* — no
gradients, no glow, no hero imagery — the same way naming a dog tells you
it doesn't meow. A long, rambling "Don't" list is usually a symptom that
the reference was too vague to carry its own restrictions; a short,
pointed list layered on top of a strong reference is the sweet spot.
Adjective soup and an over-long Don'ts section are the same failure wearing
two faces.

**Prose should name tokens inline**, e.g. "{colors.ink} carries all
typography and never appears in a background fill," so the value and the
reasoning behind it stay welded together instead of drifting apart as the
file is edited over time.

Custom top-level token groups (e.g. `motion`, `iconography`) and custom
sections are legal and preserved by the format — the spec standardizes only
the categories where cross-project consistency helps (colors, typography,
spacing, rounded, components) and leaves everything else open. Add a
`## Motion` section with its own YAML block the same way you'd add
`## Colors`; the linter and downstream consumers accept it without a spec
change.

## Workflow 1 — Authoring a new DESIGN.md

1. **Harvest evidence before inventing anything.** Check `tailwind.config.*`,
   CSS custom properties, theme provider files, existing component styles,
   and any brand assets already in the repo or supplied by the user. Real
   values already in use are ground truth; a value you make up is a value
   someone has to rip out later.
2. **Interview the user for the intent evidence can't supply.** The
   questions that produce a usable DESIGN.md ask for a concrete reference
   object ("what's an existing product, object, or printed artifact this
   should feel like?"), the emotional register (calm vs. energetic, dense
   vs. spacious), and what the design must never do. If the user answers
   with adjectives, follow up by asking what real thing embodies them.
3. **Write the Overview section first.** Everything else in the file — the
   color roles, the shadow style, the corner radius, the component prose —
   should read as a consequence of the Overview, not as an independent
   decision. If a later section contradicts the Overview's reference, the
   Overview is wrong or the later section is guessing.
4. **Fill the template** at `assets/DESIGN.template.md` rather than writing
   a file from scratch — it has the correct section order, valid starter
   tokens, and inline guidance comments to delete as you go. The template's
   starter tokens are a dark-first house default meant to be retuned per
   project, and linting the untouched template reports one expected
   `orphaned-tokens` warning for its `border` color — the components schema
   has no border property, so that warning is accepted rather than fixed.
5. **Lint before calling it done** (see Validation below).

## Workflow 2 — Building or restyling UI when a DESIGN.md exists

Read the whole file before writing any UI code — not just the front
matter. The prose tells you how to apply a token, and skipping it produces
technically-token-correct code that still looks wrong (e.g. using
`{colors.primary}` as a page background when the prose reserves it for a
single CTA).

Pull values through whatever theming mechanism the project actually uses
(Tailwind theme, CSS variables, a JS/TS token module, a native theme
object) — never invent a color, size, or radius that isn't in the file. A
missing value is a signal the file is incomplete, not a license to
hardcode: add the token to DESIGN.md first, write one line of prose
explaining what it's for, lint, then use it. A hardcoded value that happens
to match an existing token is still a bug — it drifts the next time that
token changes.

Before finishing, check the result against the Do's and Don'ts section —
it's the fastest way to catch a violation a token-level diff would miss.

## Workflow 3 — Evolving an existing DESIGN.md

1. Keep a copy of the file before editing (or rely on git — commit or stash
   first if the working tree isn't clean).
2. Apply the change, including updated prose — a token edit without a prose
   update is exactly the drift this file exists to prevent.
3. Run `diff` between the before and after copies to see precisely which
   tokens were added, removed, or modified, and whether the tool flags a
   `regression`.
4. Propagate the change to every place in the code that consumed the
   affected tokens.

Renaming a token is the sharpest edge here: it silently breaks every
`{old.name}` reference still pointing at it, and nothing about the rename
itself looks wrong in isolation. Running `lint` after a rename is what
catches this — its `broken-ref` rule is an error, not a warning, precisely
because a dangling reference is often invisible until an agent tries to
resolve it.

## Workflow 4 — Exporting

| Format | Command | Use when |
|---|---|---|
| Tailwind v3 | `export --format json-tailwind` | project's `tailwind.config.js` uses `theme.extend` |
| Tailwind v4 | `export --format css-tailwind` | project uses the CSS-first `@theme {}` config |
| DTCG tokens.json | `export --format dtcg` | feeding a design tool (Figma variables), or any pipeline expecting the W3C Design Tokens format |

Export projects the token block only, not the prose. Treat DESIGN.md as the
source of truth and the export as a generated artifact — if a token
changes, re-export rather than hand-editing the generated file.

## Validation is mandatory

A PostToolUse hook already runs `lint` automatically after any Write/Edit to
a `DESIGN.md`-named file. On an error finding it halts the turn and hands
the findings back — the write has already landed on disk, so fixing it is
the next required step, not something to defer. That safety net only covers
files changed through Write/Edit, so a DESIGN.md touched any other way (a
shell redirect, a generated export, a merge) goes unchecked. Run `lint`
yourself before declaring the file done.

| Command | What it does |
|---|---|
| `npx -y -p @google/design.md designmd lint <file>` | Validates one file; JSON findings on stdout; exit 1 if any error finding. |
| `npx -y -p @google/design.md designmd diff <before> <after>` | Token-level added/removed/modified per group, plus a `regression` flag; exit 1 on regression. |
| `npx -y -p @google/design.md designmd export --format <json-tailwind\|css-tailwind\|dtcg> <file>` | Projects the token block into a theme/tokens file. |
| `npx -y -p @google/design.md designmd spec [--rules\|--rules-only] [--format json]` | Prints the spec — useful for injecting into another agent's prompt. |

Use the `-p @google/design.md designmd` form exactly as written; the bare
`design.md` binary name collides with the Windows Markdown file
association and will not resolve correctly.

Treat any **error** finding (currently only `broken-ref`) as blocking —
fix it before moving on. Treat **warning** findings (`missing-primary`,
`contrast-ratio`, `orphaned-tokens`, `missing-typography`, `section-order`,
`unknown-key`) as needing either a fix or a stated reason you're leaving
them — don't silently ignore them. **Info** findings (`token-summary`,
`missing-sections`) are informational only.

## Format quick reference

Section order (all optional, but present sections must stay in this
order):

| # | Section | Alias |
|---|---|---|
| 1 | Overview | Brand & Style |
| 2 | Colors | — |
| 3 | Typography | — |
| 4 | Layout | Layout & Spacing |
| 5 | Elevation & Depth | Elevation |
| 6 | Shapes | — |
| 7 | Components | — |
| 8 | Do's and Don'ts | — |

Token types:

- **Color** — any valid CSS color string (hex, named, `rgb()`/`hsl()`,
  `oklch()`/`oklab()`, `color-mix()`...). Hex is the recommended default.
- **Dimension** — a number with a unit suffix: `px`, `em`, or `rem`.
- **Typography** — object with `fontFamily`, `fontSize` (Dimension),
  `fontWeight` (number), `lineHeight` (Dimension or unitless multiplier),
  `letterSpacing` (Dimension), and optionally `fontFeature` /
  `fontVariation` for OpenType settings.
- **Token reference** — `{path.to.token}`, pointing at a primitive value
  elsewhere in the tree (composite references like `{typography.label-md}`
  are allowed only inside `components`).

Valid `components.*` sub-token properties: `backgroundColor`, `textColor`,
`typography`, `rounded`, `padding`, `size`, `height`, `width`. State
variants are sibling keys, not nested objects — `button-primary`,
`button-primary-hover`, `button-primary-active` are three separate
top-level entries, associated by name prefix.

For anything not covered here — the exact schema, the recommended token
name list, or how consumers should handle unknown content — read
`references/spec.md`.

## Failure modes worth naming

- **Adjective soup in Overview** ("modern, clean, trustworthy, premium")
  produces generic UI. Push for a concrete reference instead.
- **Orphaned tokens** — defined in the front matter but never referenced by
  any component — trigger the `orphaned-tokens` warning and usually mean
  either the token is dead weight or a component definition is missing.
- **Prose that just restates hex values** ("Primary is #1A1C1E") wastes the
  one part of the file that's supposed to carry reasoning. Say what the
  color is *for*.
- **Hardcoded values in code** that duplicate or contradict a token are a
  correctness bug, not a style nit — they will silently diverge the next
  time the token changes.
- **Duplicate `##` headings** (e.g. two `## Colors` sections) are a hard
  parse error, not a lint warning.
- **Sections out of canonical order** trigger `section-order`.
- **Contrast pairs below the WCAG AA minimum of 4.5:1** trigger
  `contrast-ratio` — check this explicitly for any new `textColor` /
  `backgroundColor` pairing in `components`.

## Reference files

| File | Read it when |
|---|---|
| `references/spec.md` | You need the exact schema, the full section descriptions, recommended token names, or how unknown content should be handled. |
| `references/philosophy.md` | You need the reasoning behind "prose over tokens" and "specific reference over adjectives" in more depth, e.g. to explain a pushback to the user. |
| `references/example-paws-and-paths.md` | You want a complete, lint-clean worked example to model structure and prose density on. |
| `assets/DESIGN.template.md` | You're authoring a new DESIGN.md and need a structurally valid starting point to fill in. |
