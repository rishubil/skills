# check-bullshit

A Claude Code plugin that analyzes a URL or block of text for bullshit using
the 13-technique diagnostic framework from the BullshitBench benchmark.

## What it does

When triggered, this skill:

1. Fetches the content at a given URL (via WebFetch), or uses the supplied
   text directly.
2. Evaluates the content against 13 specific bullshit techniques — fabricated
   frameworks, false precision, misapplied mechanisms, reified metaphors,
   confident extrapolation, and more.
3. Reports a plain-language TL;DR verdict first (Clear bullshit / Suspicious /
   Largely clean / Inconclusive), followed by per-technique status with quoted
   evidence, and ends with a direct final judgment.

The skill responds in the same language the user used. It does not soften
real findings.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install check-bullshit@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install check-bullshit@rishubil-skills --scope project
```

## Usage

Typical trigger phrases:

- "check this URL for bullshit: https://..."
- "is this article credible? (paste text)"
- "fact-check this for me"
- "is this real or made up?"
- "analyze this for misleading claims"

## Source

Based on the [BullshitBench](https://github.com/petergpt/bullshit-benchmark)
benchmark by petergpt, which defines 13 specific techniques used to construct
plausible-sounding nonsense and a 0–2 scoring rubric for how clearly content
challenges them.
