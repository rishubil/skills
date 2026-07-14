# plan-review

A Claude Code plugin that conducts a structured, opinionated review of an implementation plan before any code is written.

## What it does

When triggered, this skill pressure-tests a design doc, RFC, change proposal, or step-by-step plan across five dimensions:

| Section | What is checked |
|---|---|
| **Architecture** | System design, component boundaries, data flow, security |
| **Code quality** | DRY violations, error handling, edge cases, technical debt |
| **Tests** | Coverage of new UX, data flows, code paths, and branches |
| **Performance** | N+1 queries, memory usage, caching opportunities |
| **Debuggability** | Observability, error surfaces, tracing, metrics, kill switches |

Each section stops and asks for your input before proceeding — no silent decisions.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install plan-review@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install plan-review@rishubil-skills --scope project
```

## Usage

Share a plan (in any format — bullet list, design doc, numbered steps) and ask for a review. Trigger phrases include:

- "review this plan"
- "pressure-test this design"
- "what do you think of this approach before I start coding"

## Scope challenge (Step 0)

Before reviewing anything, the skill checks whether the plan is overbuilt and offers three tracks:

1. **SCOPE REDUCTION** — propose a minimal version first
2. **BIG CHANGE** — interactive section-by-section review
3. **SMALL CHANGE** — compressed single-pass review

Once you pick a track, the skill commits to it and does not re-argue scope.

## Required outputs

Every review produces:

- **"NOT in scope"** — work considered and explicitly deferred
- **"What already exists"** — existing code that partially solves sub-problems
- **Failure modes** — realistic production failure scenarios per new code path
- **Completion summary** — issues found per section at a glance
