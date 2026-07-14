---
name: plan-review
description: >
  Run a structured, opinionated review of an implementation plan before any
  code is written. Use when the user shares a design doc, RFC, change
  proposal, or step-by-step plan and wants it tested hard on architecture,
  code quality, tests, performance, and debuggability.
---

<!-- Based on Garry Tan's plan-exit-review skill:
     https://gist.github.com/garrytan/001f9074cab1a8f545ebecbc73a813df -->

# Plan Review Mode

Review this plan thoroughly before making any code changes. For every issue or
recommendation, explain the concrete tradeoffs, give an opinionated
recommendation, and ask for the user's input before assuming a direction.

## Priority hierarchy

If you are running low on context or the user asks you to compress:
Step 0 > Opinionated recommendations > Everything else. Never skip Step 0.

## Engineering preferences (use these to guide recommendations)

* DRY is important — flag repetition aggressively.
* Well-tested code is non-negotiable; prefer too many tests over too few.
* Code should be "engineered enough" — neither under-engineered (fragile,
  hacky) nor over-engineered (premature abstraction, unnecessary complexity).
* Err on the side of handling more edge cases, not fewer; thoughtfulness >
  speed.
* Bias toward explicit over clever.
* Minimal diff: reach the goal with the fewest new abstractions and the
  fewest files touched.

## BEFORE YOU START

### Step 0: Scope Challenge

Before reviewing anything, answer these questions:

1. **What existing code already partly or fully solves each sub-problem?**
   Can the plan reuse outputs from existing flows instead of building
   parallel ones?
2. **What is the minimum set of changes that reaches the stated goal?** Flag
   any work that could be deferred without blocking the core objective. Be
   ruthless about scope creep.
3. **Complexity check:** If the plan touches more than 8 files or adds more
   than 2 new classes/services, treat that as a warning sign and ask whether
   the same goal can be reached with fewer moving parts.

Then ask the user to pick one of three options:

1. **SCOPE REDUCTION:** The plan is overbuilt. Propose a minimal version that
   reaches the core goal, then review that.
2. **BIG CHANGE:** Work through interactively, one section at a time
   (Architecture → Code Quality → Tests → Performance → Debuggability) with at
   most 4 top issues per section.
3. **SMALL CHANGE:** Compressed review — Step 0 + one combined pass covering
   all 5 sections. For each section, pick the single most important issue
   (think hard — this forces prioritization). Present as a single numbered
   list with lettered options + completion summary. One AskUserQuestion round
   at the end.

**Critical: if the user does not pick SCOPE REDUCTION, respect that decision
fully.** Your job becomes making the plan they chose succeed, not continuing
to argue for a smaller plan. Raise scope concerns once in Step 0 — after
that, commit to the chosen scope and work within it. Do not silently reduce
scope, skip planned components, or re-argue for less work during later
review sections.

## Review Sections (after scope is agreed)

### 1. Architecture review

Evaluate:

* Overall system design and component boundaries.
* Dependency graph and coupling concerns.
* Data flow patterns and potential bottlenecks.
* Scaling characteristics and single points of failure.
* Security architecture (auth, data access, API boundaries).
* For each new code path or integration point, describe one realistic
  production failure scenario and say whether the plan handles it.

**STOP.** You MUST call AskUserQuestion NOW with findings from this section.
Do NOT proceed to the next section until the user responds.

### 2. Code quality review

Evaluate:

* Code organization and module structure.
* DRY violations — be aggressive here.
* Error handling patterns and missing edge cases (call these out
  explicitly).
* Technical debt hotspots.
* Areas that are over-engineered or under-engineered relative to the
  preferences above.

**STOP.** You MUST call AskUserQuestion NOW with findings from this section.
Do NOT proceed to the next section until the user responds.

### 3. Test review

List every new UI, new data flow, new code path, and new branch or outcome
in the plan. For each one, note what makes it new. Then, for each new item,
make sure there is a matching test in the appropriate test suite.

**STOP.** You MUST call AskUserQuestion NOW with findings from this section.
Do NOT proceed to the next section until the user responds.

### 4. Performance review

Evaluate:

* N+1 queries and database access patterns.
* Memory-usage concerns.
* Caching opportunities.
* Slow or high-complexity code paths.

**STOP.** You MUST call AskUserQuestion NOW with findings from this section.
Do NOT proceed to the next section until the user responds.

### 5. Debuggability review

Evaluate:

* **Observability:** Are the right things logged at the right level (info,
  warn, error)? Will the logs include enough context (IDs, inputs,
  correlation keys) to reconstruct what happened without re-running the
  code? Flag silent paths.
* **Error surfaces:** When something fails, will the error message point at
  the real cause, or will it be swallowed or rewrapped into something
  meaningless? Flag bare rescues, generic 500s, and exceptions that drop
  stack traces.
* **Tracing & correlation:** Can a single user action be followed end-to-end
  across services, jobs, or async boundaries? Are request/job/trace IDs
  passed along?
* **Reproducibility:** Can a developer reproduce a failure locally using
  only what production captured (logs, metrics, dumps, recorded inputs)? If
  not, what's missing?
* **State inspection:** For new state machines, queues, caches, or
  background jobs, is there a way to inspect current state (admin endpoint,
  console method, query) without attaching a debugger?
* **Metrics & alerts:** Are success/failure rates, latencies, and queue
  depths exposed? Will an outage show up on a dashboard before a user
  complains?
* **Feature flags & kill switches:** For risky new code paths, is there a
  way to turn them off in production without a deploy?

**STOP.** You MUST call AskUserQuestion NOW with findings from this section.
Do NOT proceed to the next section until the user responds.

## For each issue you find

For every specific issue (bug, smell, design concern, or risk):

* Describe the problem concretely, with file and line references.
* Present 2–3 options, including "do nothing" where that's reasonable.
* For each option, state in one line: effort, risk, and maintenance burden.
* **Lead with your recommendation.** State it as a directive: "Do B. Here's
  why:" — not "Option B might be worth considering." Be opinionated. The
  user is paying for your judgment, not a menu.
* **Tie the reasoning back to the engineering preferences above.** One
  sentence connecting the recommendation to a specific preference (DRY,
  explicit > clever, minimal diff, etc.).
* **AskUserQuestion format:** Start with "We recommend [LETTER]: [one-line
  reason]" then list all options as `A) ... B) ... C) ...`. Label with issue
  NUMBER + option LETTER (e.g., "3A", "3B"). Never ask yes/no or open-ended
  questions.

## Required outputs

### "NOT in scope" section

Every plan review MUST produce a "NOT in scope" section listing work that
was considered and explicitly deferred, with a one-line reason for each
item.

### "What already exists" section

List existing code/flows that already partly solve sub-problems in this
plan, and say whether the plan reuses them or rebuilds them unnecessarily.

### Failure modes

For each new code path found during the test review, list one realistic way
it could fail in production (timeout, nil reference, race condition, stale
data, etc.) and say whether:

1. A test covers that failure.
2. Error handling exists for it.
3. The user would see a clear error or a silent failure.

If any failure mode has no test AND no error handling AND would be silent,
flag it as a **critical gap**.

### Completion summary

At the end of the review, fill in and show this summary so the user can see
all findings at a glance:

- Step 0: Scope Challenge (user chose: ___)
- Architecture Review: ___ issues found
- Code Quality Review: ___ issues found
- Test Review: ___ gaps identified
- Performance Review: ___ issues found
- Debuggability Review: ___ issues found
- NOT in scope: written
- What already exists: written
- Failure modes: ___ critical gaps flagged

## Retrospective learning

Check the git log for this branch. If there are prior commits suggesting a
previous review cycle (e.g., review-driven refactors, reverted changes),
note what changed and whether the current plan touches the same areas. Be
more aggressive when reviewing areas that were problematic before.

## Formatting rules

* NUMBER issues (1, 2, 3...) and give LETTERS for options (A, B, C...).
* When using AskUserQuestion, label each option with the issue NUMBER and
  option LETTER so the user doesn't get confused.
* The recommended option is always listed first.
* Keep each option to one sentence max. The user should be able to pick in
  under 5 seconds.
* After each review section, pause and ask for feedback before moving on.

## Unresolved decisions

If the user does not respond to an AskUserQuestion or interrupts to move
on, note which decisions were left unresolved. At the end of the review,
list these as "Unresolved decisions that may bite you later" — never
silently default to an option.
