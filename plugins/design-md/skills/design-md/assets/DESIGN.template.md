---
version: alpha
name: <Project Name>
description: <One sentence describing this design system>
# The values below are a sensible dark-first default worth starting a new
# project from — not a mandate. Retune them freely. The palette and the font
# stacks are the tokens most likely to change per project; the structural
# tokens (rounded, spacing, the component shapes) tend to travel as-is.
#
# Color tokens: any valid CSS color (hex is the recommended default). At
# least `primary` must be defined. This is a dark-first, layered-flat-surface
# palette: `bg` (page canvas) sits one step *below* `panel` (cards), which
# sits below `control` (interactive fills) — so a recessed element like an
# input reads as a well below the card, not a slab on top of it.
colors:
  bg: "#12141a"
  panel: "#1c1f28"
  control: "#2a2e3a"
  control-hover: "#343948"
  # Hairline separator. There is no border sub-token in the components
  # schema below (valid component properties are only backgroundColor,
  # textColor, typography, rounded, padding, size, height, width), so this
  # token can't be wired to any component. Applying it as a global 1px rule
  # instead of a component property is correct, and `designmd lint` will
  # report one `orphaned-tokens` warning for it — that warning is expected
  # and accepted, not a bug to fix by deleting the token.
  border: "#3a3f4d"
  text: "#e8e8ee"
  muted: "#8b8fa3"
  # The single accent. Reserve it for meaning (live/active state, the one
  # emphasized action, progress) — never for decoration.
  primary: "#2dd4bf"
  # A dimmed companion fill for the primary button's resting state, so the
  # accent reads as an outline rather than a solid slab until hover — the
  # button only becomes a full block of color once it is interacted with.
  primary-dim: "#134e4a"
  # Text/icon color for anything sitting on a solid `primary` fill.
  on-primary: "#12141a"
  # One reserved alert/critical color. Spend it on a single meaning (e.g. a
  # destructive action or a critical alarm state) and nowhere else, so it
  # keeps its urgency.
  alert: "#f87171"
  backdrop: "rgba(0, 0, 0, 0.6)"
# Typography tokens: fontFamily, fontSize, fontWeight, lineHeight, and
# (optionally) letterSpacing, fontFeature, fontVariation. Add one entry per
# level your system needs (headline, body, label, etc).
#
# A three-role system: sans for interface chrome, serif for real prose,
# monospace for numerics/data. Each stack ends in system fallbacks so the
# spec renders correctly before any webfont has loaded. The leads
# (Pretendard Variable / Noto Serif KR / D2Coding) carry full Korean
# coverage — keep them if that's a standing requirement for your project;
# otherwise swap the lead font but keep the fallback chain behind it.
typography:
  heading:
    fontFamily: "'Pretendard Variable', Pretendard, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 1.5rem
    fontWeight: 700
  body:
    fontFamily: "'Noto Serif KR', 'Noto Serif', Georgia, 'Times New Roman', serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "'Pretendard Variable', Pretendard, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
    fontSize: 0.9rem
    fontWeight: 500
  # Tabular numerals (`tnum`) hold every digit to the same width, so a
  # live/changing value never jitters as it updates. Apply `fontFeature:
  # tnum` to any level — big or small — that displays such a value.
  data:
    fontFamily: "'D2Coding', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace"
    fontSize: 1.5rem
    fontWeight: 700
    letterSpacing: 0.02em
    fontFeature: tnum
  caption:
    fontFamily: "'D2Coding', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace"
    fontSize: 0.8rem
    fontWeight: 400
    fontFeature: tnum
# Corner-radius scale, referenced from `components` below. Radius grows with
# the size of the surface it's applied to: small controls stay tight and
# precise, large surfaces read calmer and softer.
rounded:
  sm: 6px # inputs
  md: 8px # buttons
  lg: 12px # panels, modals
  full: 9999px # circular utility buttons
# Spacing scale (rem-based), used for padding, margins, and layout rhythm.
spacing:
  xs: 0.35rem
  sm: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.25rem
  2xl: 1.5rem
  3xl: 2rem
# Component styling. Each key is a component, or a state variant of one
# (e.g. `button-primary-hover`, `button-primary-active`). Valid properties:
# backgroundColor, textColor, typography, rounded, padding, size, height,
# width. Values may be literals or {path.to.token} references.
components:
  panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  button:
    backgroundColor: "{colors.control}"
    textColor: "{colors.text}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0.5rem 1rem"
  button-hover:
    backgroundColor: "{colors.control-hover}"
  # The single emphasized action on screen: an outline (via `primary-dim`)
  # until hover, then an inverted solid `primary` fill. Keep at most one
  # `button-primary` visible per view.
  button-primary:
    backgroundColor: "{colors.primary-dim}"
    textColor: "{colors.text}"
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  input:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
    typography: "{typography.data}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  modal:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    width: 90%
  backdrop:
    backgroundColor: "{colors.backdrop}"
  progress:
    backgroundColor: "{colors.primary}"
    height: 0.4rem
  # Secondary/meta text — hints, idle placeholders, low-emphasis labels —
  # set in the muted foreground.
  caption-text:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  # The one reserved alert color, applied only to the single state it means
  # (e.g. a critical/destructive status), never as general-purpose emphasis.
  alert-text:
    textColor: "{colors.alert}"
---

<!--
  This is a skeleton, not a finished design. Replace every placeholder
  above and every comment below with real content, then delete the
  comments — a finished DESIGN.md should have none left. Prose is the
  actual specification here; the tokens above only exist to give the
  prose something concrete to point at.

  When you are done, run:
    npx -y -p @google/design.md designmd lint <this file>
  Fix every error finding. Fix or consciously accept every warning.
-->

## Overview

<!--
  Also called "Brand & Style". This is the section everything else in the
  file follows from — write it first.

  Name ONE concrete reference object, not a list of adjectives: not
  "modern, clean, premium" but something like "a 1970s graduate CS lecture
  handout" or "a Braun kitchen appliance manual, translated to a phone
  screen." A specific reference carries the audience, the emotional
  register, and a whole set of "don'ts" for free — adjectives only mark out
  a vague region and tend to produce generic output.

  The format is extensible beyond the eight sections below: custom sections
  (e.g. `## Themes`, `## Motion`) and custom top-level token groups in the
  front matter (e.g. a `motion:` block alongside `colors:`/`spacing:`) are
  both legal and preserved by the linter. Add one if your project has a
  concern this skeleton doesn't cover — don't force it into a section it
  doesn't belong in.
-->

## Colors

<!--
  Explain what each palette is FOR, not just what it looks like. Name the
  token inline so the value and the reasoning stay welded together, e.g.:
  "{colors.primary} is reserved for live/active meaning — never decoration —
  and only shows as a solid fill on hover/active; at rest it shows through
  {colors.primary-dim} so the accent reads as an outline, not a slab."

  If your palette layers surfaces (canvas → card → interactive fill, as the
  starter tokens do), say which token sits below which and why — e.g. why
  {colors.bg} sits one step *below* {colors.panel} rather than above it.
-->

## Typography

<!--
  Name the typeface(s) and explain the role of each level (why it exists),
  not just its size and weight. If you use a multi-role system (e.g. sans
  for chrome, serif for prose, monospace for numerics), say which role each
  level belongs to and why. Call out where `fontFeature: tnum` (tabular
  numerals) matters: any level that displays a live or changing number
  should hold digits to a fixed width so they don't jitter as they update.
-->

## Layout

<!--
  Also called "Layout & Spacing". Describe the grid or spacing model and
  the visual rhythm it is meant to produce.
-->

## Elevation & Depth

<!--
  Also called "Elevation". If you use shadows, specify their color, blur,
  and spread. If the design is flat, explain what conveys hierarchy
  instead (borders, tonal contrast, spacing).
-->

## Shapes

<!--
  Describe the corner-radius language and what mood it is meant to signal
  (sharp and engineered vs. soft and approachable).
-->

## Components

<!--
  Walk through the components defined in the front matter and explain how
  their tokens should be applied. Add prose for every component you add
  above, especially variants (hover, active, disabled).
-->

## Do's and Don'ts

<!--
  Keep this short and specific. If the Overview reference is strong, most
  of these should already follow from it — a long rambling list here is
  usually a sign the Overview was too vague. The four below are generic
  starting examples; keep the ones that still apply to your design and
  delete or replace the rest.
-->

- **Do** reserve `{colors.primary}` for live/active meaning, never decoration.
  **Don't** use the accent as a default color for chrome that isn't
  communicating something.
- **Do** express hierarchy through fill steps (`{colors.bg}` →
  `{colors.panel}` → `{colors.control}`) and hairline `{colors.border}`.
  **Don't** introduce drop shadows or extra surface colors to fake depth.
- **Do** pull every gap, radius, and color from the tokens above (`spacing`,
  `rounded`, `colors`). **Don't** hard-code one-off values in the CSS.
- **Do** keep exactly one emphasized (`button-primary`) button on screen.
  **Don't** promote secondary actions to primary styling.
