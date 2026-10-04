# ste100-korean

## What it does

Applies controlled-language writing rules, adapted from ASD-STE100 (Simplified Technical English), to every Korean and English text the agent writes. The goal is text that a user, another agent, or a translation layer cannot misread.

- **Both languages, one skill.** Shared core rules: one term per concept, named actors, one idea per sentence, length caps, verbs instead of frozen nouns, short modifier chains, kept hedges, and no dropped negation or numbers. Korean adds its own ambiguity rules: double passives (되어지다), translationese (~에 대한, ~을 통해), light verbs (작업을 진행하다), stacked modifying clauses, negation scope, speech-level mixing, and single-tilde ranges. The English rules are ported from the upstream skill.
- **Always on.** A `SessionStart` hook puts a short rule summary into context at every session start, resume, clear, and compaction. The full skill loads when the agent writes a document or rewrites text.
- **English-Korean glossary.** Each project keeps `GLOSSARY.md`, a table that maps each domain term one-to-one between English and Korean. The agent reads it before writing and adds every new term it translates.
- **Bilingual linter.** `ste-lint.py` checks both languages in one run. Korean rules use the [Kiwi](https://github.com/bab2min/kiwipiepy) morphological analyzer when available, and regex otherwise. It never flags hedges.

It is not for creative or marketing copy, legal text, or quotations.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install ste100-korean@rishubil-skills
```

On the first session after installation, the hook installs kiwipiepy (about 140 MB with its model and numpy) into the plugin's data directory, `~/.claude/plugins/data/ste100-korean-rishubil-skills/venv`. The install runs in the background and does not block the session. It uses `uv` when available and `python3 -m venv` otherwise. It runs again only when a plugin update changes `requirements.txt`. Set `STE100_KOREAN_NO_INSTALL=1` to skip it. Without kiwipiepy, the linter still runs, but the Korean noun-stack and modifier-clause rules are off and the other Korean rules use regex.

## Usage

No command is needed. Write or ask for Korean or English text as usual, and the rules shape it.

Explicit requests also work:

```
이 도구 설명을 에이전트가 오해하지 않게 다시 써줘
```

```
Rewrite this error message so an agent cannot misparse it, and show which rules it broke
```

```
이 README의 한국어 문장을 ste-lint로 검사하고 고쳐줘
```

```
GLOSSARY.md를 만들고 이 문서에 나오는 용어를 정리해줘
```

To run the linter yourself:

```bash
plugins/ste100-korean/skills/ste100-korean/scripts/ste-lint.sh README.md docs/*.md
```

Add `--json` for structured output, `--baseline N` to tolerate N existing hard findings, `--disable RULE,RULE` to silence rules, and `--selftest` to check the linter.

## Scripts

| Path | Purpose |
|---|---|
| `hooks/hooks.json` | Registers the `SessionStart` hook. |
| `hooks/session-context.md` | The rule summary that the hook puts into context. |
| `scripts/session-start.sh` | Prints the rule summary and the project glossary status. Starts the background install of kiwipiepy when needed. |
| `scripts/install-deps.sh` | Installs `requirements.txt` into `${CLAUDE_PLUGIN_DATA}/venv`, with a lock and a version stamp. |
| `requirements.txt` | The pinned kiwipiepy version. |
| `skills/ste100-korean/scripts/ste-lint.sh` | Linter launcher. Uses the plugin venv, then `uv run`, then `python3`. |
| `skills/ste100-korean/scripts/ste-lint.py` | The bilingual linter (standard library plus optional kiwipiepy, PEP 723 metadata). |

## Source

This plugin adapts four MIT-licensed projects:

- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), (c) 2026 Dustin Yuchen Teng. The original English ASD-STE100 skill: structure, process, output format, modality rule, English rules, and linter.
- [beamonic/ste-ko](https://github.com/beamonic/ste-ko), (c) 2026 Beamonic. A Korean controlled-language spec: several Korean rule ideas and the regex stem-expansion technique.
- [Turtle-Hwan/im-ai-copyeditor](https://github.com/Turtle-Hwan/im-ai-copyeditor), (c) 2026 Turtle-Hwan. A Korean copyediting skill: rule ideas for filler, English-syntax calques, AI tells, decoration, honorifics, labels, and spelling. Its vocabulary-variation and fixed-sentence-count principles are not adopted, because they conflict with one term per concept and one idea per sentence.
- [cursor/plugins `pstack` unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md), (c) 2026 Lauren Tan. An English AI-tell checklist: rule ideas for AI vocabulary, filler, plain words, over-compression, chatbot phrases, and mechanism-over-feeling. Its blanket ban on parentheses is not adopted, because the glossary first-use form needs them.

The Korean rules also draw on 국립국어원 public-language guidelines, the 법제처 plain-legislation standard, Korean linguistics research on ambiguity, and the Kakao Developers documentation guide. See [`skills/ste100-korean/references/sources.md`](./skills/ste100-korean/references/sources.md).

This plugin does not contain the ASD-STE100 rule text or its approved-word dictionary, which ASD does not allow to be redistributed. See [`skills/ste100-korean/NOTICE.md`](./skills/ste100-korean/NOTICE.md) for the upstream notices.
