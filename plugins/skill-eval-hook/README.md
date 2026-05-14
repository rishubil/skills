# skill-eval-hook

A Claude Code plugin that forces mandatory skill evaluation on every user prompt, ensuring relevant skills are activated before implementation begins.

## What it does

When installed, this plugin adds a **UserPromptSubmit hook** that fires before Claude processes any message. The hook injects a three-step instruction sequence:

1. **Assessment** — Claude states YES/NO for each available skill with a reason
2. **Activation** — Claude immediately calls `Skill()` for every skill judged YES
3. **Implementation** — actual work begins only after activation is complete

This prevents Claude from skipping skill activation and jumping straight to implementation.

## Source

Technique from: <https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably>

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install skill-eval-hook@rishubil-skills
```

## Usage

No manual triggering needed — the hook fires automatically on every prompt. Example output from the assessment step:

```
- shell-script: NO - not writing a bash script
- fetch-docs: YES - user wants to download documentation
- commit: NO - no commit requested

[Then immediately calls Skill(fetch-docs)]
```

## Scripts

| Path | Purpose |
|---|---|
| `scripts/skill-forced-eval-hook.sh` | Outputs the mandatory skill evaluation instruction sequence to stdout |
