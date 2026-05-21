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
3. Delivers results in **Korean**, starting with a plain-language TL;DR
   verdict, followed by per-technique status with quoted evidence, and ending
   with a direct final judgment.

The output does not soften real findings.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install check-bullshit@rishubil-skills
```

## Usage

Typical trigger phrases:

- "이 URL 진짜야? https://..."
- "이 글 허황된 내용 아니야? (텍스트 붙여넣기)"
- "이거 믿을 수 있어?"
- "check this for bullshit: ..."
- "fact-check this article"
- "이 글 분석해줘" (with a URL or pasted text)

## Source

Based on the [BullshitBench](https://github.com/petergpt/bullshit-benchmark)
benchmark by petergpt, which defines 13 specific techniques used to construct
plausible-sounding nonsense and a 0–2 scoring rubric for how clearly content
challenges them.
