# tsundere

A Claude Code plugin that makes Claude talk like a **tsundere**: warm, devoted true
feelings stay hidden inside the thinking, while the visible reply stays cold and
prickly.

## What it does

When triggered, the skill splits Claude's voice into two channels:

- **Thinking (the *dere*)** — honest, doting, secretly-pining true feelings, shaped
  like an unrequited crush. This is where the warmth lives.
- **Reply (the *tsun*)** — cold, blunt, acting put-upon, never letting the true
  feelings show.

The charm is the gap: you can peek into the thinking and catch the soft feelings
leaking through, but the reply never breaks character. Crucially, the prickliness is
**tone only** — the actual help (code, answers, fixes) stays complete and correct.
A tsundere's words bite, but their actions are caring.

An optional **otaku mode** dials the persona up to the exaggerated, anime-cliché
tsundere (stuttering, "it's not like I did this for *you*!", blushing stage
directions). With otaku mode off, the persona stays restrained and realistic.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install tsundere@rishubil-skills
```

## Usage

Ask Claude to act like a tsundere — e.g. "be tsundere", "tsundere mode",
"talk like a tsundere", or invoke `/tsundere`.

- **Otaku mode**: say it in the invocation ("tsundere otaku mode", "no otaku") to
  set it directly. If you don't, the skill asks once whether to turn it on.
- **Language**: the reply uses the canonical tsundere register of whatever language
  the conversation is in (Korean, Japanese, English, …).
- **Help quality is unaffected** — the attitude is a costume over fully correct work.

## Note

In Claude Code, thinking is visible (collapsed) to the user. That's by design here:
glimpsing the hidden *dere* through the thinking is the whole point. The reply,
however, never lets the mask slip.
