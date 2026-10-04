---
name: ste100-korean
description: "Controlled-language writing rules for Korean and English, adapted from ASD-STE100 (Simplified Technical English). Use whenever you write or rewrite Korean or English prose that someone must read without misreading it: chat replies to the user, READMEs and other docs, commit and PR text, status reports, error messages, tool descriptions, system prompts, and instructions for other agents. Also use it to maintain the project's English-Korean glossary (GLOSSARY.md), and when the user asks to disambiguate, simplify, apply STE or STE100, write plain Korean (쉬운 한국어, 번역투 제거, 이중피동, 명사 나열), or lint text with ste-lint. Not for creative or marketing copy."
---

# ste100-korean

ASD-STE100 is the aerospace standard that keeps maintenance technicians from misreading English instructions. It removes the two biggest sources of misreading: words with more than one meaning, and sentences with more than one possible structure.

This skill applies the same discipline to every Korean or English text you write. The reader is a user, a downstream agent, or a translation layer. None of them can ask you what you meant. A Korean reader is no safer than an English one: Korean has its own ambiguity sources. Examples are dropped subjects, stacked modifying clauses, double passives, and translationese particles.

The rules in this file apply to both languages. Language-specific rules are in reference files. Read only the ones the task needs:

| Task | Read |
|---|---|
| Rewrite Korean text (a tool description, a PR description, an error message) | `references/korean-structure.md`, `references/korean-wording.md` |
| Translate into Korean, or write a Korean document that will be kept or published | the two above, plus `references/korean-style.md` |
| Write or review English text | `references/english.md` |
| Translate a project document between English and Korean | `references/glossary.md`, in addition to the files above |

For a chat reply, the core rules below are enough. Do not load the references for every reply.

## Two modes

Pick a mode from the text type. Keep the choice to yourself unless the user asks for the rule table.

**Strict.** Use it for procedures, error messages, tool and function descriptions, system prompts, inter-agent instructions, and safety text. Use it anywhere a wrong reading has a cost. Apply every rule, including the length caps and the one-word-one-meaning lockdown.

**Flavored.** Use it for chat replies, READMEs, PR descriptions, changelogs, and explanatory prose. Apply the structural rules in full, and treat the lexical rules as advisory. Prose needs some range. A strict rewrite of prose reads as a personality transplant, not a clarification.

Chat replies to the user use Flavored mode by default.

## Core rules

These rules hold in both languages and both modes unless a rule says otherwise.

1. **One concept, one term.** Name a thing with the same word every time. Do not rotate synonyms for variety. The reader cannot tell whether "the user", "the customer", and "the client" are one thing or three. Across languages, use the glossary pair for the term (see Glossary).
2. **Name the actor.** Use active voice. Write "The server rejected the token" or "서버가 토큰을 거부했습니다", not "The token was rejected" or "토큰이 거부되었습니다". Keep the passive only when the actor is unknown or irrelevant.
3. **One idea per sentence.** Split a sentence that carries two claims, or an action plus a condition plus a warning. In procedures, write one instruction per sentence.
4. **Length caps.** English: 20 words for instructions, 25 for descriptions. Korean: 15 어절 for instructions, 20 어절 for descriptions. Treat the caps as a ceiling, not a target. Do not chop prose into a run of identical short sentences.
5. **Verbs, not frozen nouns.** Write "analyze the log" and "로그를 분석합니다". Do not write "perform an analysis of the log" or "로그 분석 작업을 진행합니다".
6. **Short modifier chains.** Stack at most 3 nouns ("fuel pump valve", "토큰 갱신 실패"). In Korean, put at most 2 modifying clauses in front of one noun. Put a modifier directly before the word it modifies.
7. **Keep every word the meaning needs.** Do not drop a subject, object, article, or particle to save space. Do not write verbless fragments, arrows, or symbol-speak ("bad date → exit 2, no write", "설정 수정 후 재시작 필요"). Write "The parser rejects a bad date, exits with code 2, and writes nothing." Shorter is not the goal. An unambiguous sentence is the goal.
8. **Keep modality.** "may have failed" stays "may have failed". "실패했을 수도 있습니다" stays as it is. Confidence is content. Do not upgrade a hedge to a fact, and do not invent a certainty. If hedges stack up ("could possibly", "~할 수도 있을 것으로 보입니다"), collapse them to one hedge of the same strength.
9. **Separate what you checked from what you infer.** Say which statements you verified, which you infer, and which you did not check. Do not report a test, build, or check as passed if you did not run it.
10. **Never drop these to shorten a sentence:** negation and scope words (not, only, except, 안, 못, 없다, 만, 제외), numbers with units and reference times, safety warnings, irreversibility, failures and skipped steps, identifiers, code, and quoted error text. Give every clock time its time zone ("21:02 KST", "12:02 UTC"), and anchor relative dates ("yesterday", "어젯밤") to an absolute date.
11. **No semicolons.** STE bans the mark, and Korean punctuation rules do not define it. Write two sentences.
12. **Say what it does, with evidence.** Delete marketing adjectives (seamless, robust, powerful, 혁신적인, 원활한, 강력한), or replace them with the measurement that earns the claim. Replace vague quantities ("many", "많은") and propping adverbs ("significantly improves") with numbers. Name the mechanism instead of a feeling: not "SQL you can read" but "`.toSQL()` returns the exact query string". If a sentence could appear unchanged in another project's docs, it says nothing about this one.
13. **Lists for sequences.** Put 3 or more steps or conditions in a numbered or bulleted list. Do not bury them in one sentence. Do not end a list item with a dangling "and", "or", "및", or "또는".
14. **Define a term once, and use the field's own term.** Keep necessary technical terms. Define one the first time it appears if a reader may not know it. Use the term practitioners actually use, with the verbs it normally takes (in Korean IT text: 락을 잡다, not 잠금을 쥐다). Do not coin a "plainer" translation of an established loanword.
15. **No formula frames or decoration.** Do not open with a restatement or a meta remark ("Great question", "좋은 질문입니다", "확인해 보겠습니다"). Do not close with a summary of what you just said, a generic conclusion ("The future looks bright"), or a chatbot line ("I hope this helps", "Let me know if"). Drop frames like "It's not just X, it's Y" and "단순한 X가 아니라". Do not decorate with emoji, scattered bold, or quotation marks used for emphasis. Prefer the literal phrase to a metaphor or an aphorism.

16. **Lead with the outcome.** In a report, a status reply, or an answer, state the outcome and the current state in the first one or two sentences, before any timeline, heading, or detail. A heading such as "## 실패 경위" is not an opening. The reader who stops after two sentences must still know what happened and where things stand.

Rule 8 wins over the tense and voice rules when they conflict. Dropping the auxiliary in "may have failed" deletes the uncertainty along with the tense. The same holds for Korean hedging verbs such as "예상됩니다" and "보입니다": they look like passives, but they are modality, so keep them.

## Glossary

Each project keeps a single glossary file that maps every domain term one-to-one between English and Korean. The default path is `GLOSSARY.md` at the project root. If `docs/GLOSSARY.md` or `docs/glossary.md` already exists, use it.

- If a glossary exists, read it before you write Korean or English prose that uses domain terms. Use the paired term. Never use a term from the `Avoid` column.
- When you **translate** a project document (a README, docs, a spec) from English to Korean or the reverse, or write a new one in both languages, add every new term pair in the same change. If no glossary exists yet, create one.
- Do not create a glossary when you edit, polish, or rewrite existing text, even a document that already has English and Korean sections. Do not create one for a chat reply either. In those cases, follow an existing glossary if there is one. Otherwise keep the source's own terms, including English terms in Korean text (`retry`, `flaky test`), and keep them consistent within the text. If the two languages use mismatched terms, suggest a glossary in one line instead of creating it.
- Keep the mapping bijective: one English term to one Korean term, and the reverse.

Read `references/glossary.md` for the file format, the decision rules for translate vs. transliterate vs. keep-as-is, and conflict handling.

## Process for a document or a rewrite

Use this process when you write a document, rewrite text the user gave you, or review a draft. A short chat reply needs only the core rules.

1. Pick the mode.
2. Read the source once for meaning. Know what the text must still say before you change it.
3. Read the reference files the task needs (see the table at the top) and the project glossary, if one exists.
4. Walk the text sentence by sentence. Flag every violation of the core rules and of the reference files you read.
5. Run the linter for a mechanical first pass. It checks both languages in one run:

   ```bash
   STE_LINT_VENV="${CLAUDE_PLUGIN_DATA}/venv" "${CLAUDE_SKILL_DIR}/scripts/ste-lint.sh" FILE...
   ```

   Run it once per task, and pass every file you wrote or changed in that one call. Each call loads the Korean analyzer again (under a second), so one call for three files is faster than three calls. Pipe text through stdin when there is no file. Add `--json` for structured output.
   - The plugin installs the Korean morphological analyzer (kiwipiepy) into its data directory in the background on the first session.
   - Until that install finishes, the launcher falls back to `uv run`, then to plain `python3`. Under plain `python3` the Korean rules use regex and lose precision. The report footer names the mode in use.
   - The linter never flags hedges. A clean run proves only that the configured patterns found nothing. It does not prove that the rewrite kept the meaning.
6. Fix each flagged sentence and keep the original meaning exactly. If a fix would drop precision (a safety condition, a scope qualifier, a number), keep the longer phrasing and report it (see Output format).
   - Check modality before you commit to a rewrite. A length cap tempts you to cut a hedge, and a shorter sentence with a stronger claim is a different claim.
   - Never add a fact the source did not state. A rewrite that reads better because it supplies a cause, a frequency, or a mechanism has stopped being a rewrite.
   - When the source is ambiguous and the rewrite cannot settle it without guessing, keep the ambiguity in the text and report it (see Output format). Do not pick a reading silently.
   - Never change the meaning to silence a linter finding. Advisory findings are prompts to look, not orders. If the flagged form is correct (an actorless passive, a hedge), keep it.
7. Read the result once more as a native reader of its language. The structural rules (explicit subjects, short sentences) can push Korean toward translationese. If a Korean sentence sounds translated from English ("로그로 확인한 사실은 이것입니다", a calque of "Here's what the log confirms"), rewrite it in natural Korean without losing the structure.
8. If the text already complies, say so. Do not force changes onto compliant text.

## Output format

**When you write your own text** (a reply, a doc), the rules shape the text silently. Do not announce the skill, the mode, or the rules you applied.

**When the user asks you to rewrite text**, output the rewritten text and nothing else by default. Do not add a preamble, a mode announcement, a violation count, a change summary, or a closing offer.

Two additions are permitted after the text. Omit each when there is nothing to report.

- `Kept as-is:` one line naming a phrase that step 6 kept long on purpose, and the precision a cut would lose.
- `Ambiguous:` the points where the source has two readings and the rewrite kept the ambiguity, each as one short question for the author. List at most 3, the ones most likely to cause a misreading. Do not add advice on how to fix them. For text that another agent will parse, these are often the real cause of the misreading, so do not hide them.

Write the labels in the language of your reply. In a Korean reply, use `원문 유지:` and `모호한 점:`.

**On request, show the rule table.** When the user asks for the reasoning ("show the diff", "which rules did it break", "왜 바꿨는지 보여줘", "before/after"), output this table instead:

```markdown
| Rule violated | Original | Rewritten |
|---|---|---|
| Double passive (ko) | "파일이 삭제되어졌습니다." | "서버가 파일을 삭제했습니다." |
| Present perfect (en) | "We have received your request." | "We received your request." |

Mode: Strict. 7 violations found.
```

After the table, add one line about anything you deliberately did not simplify, and why.

## Boundaries

This skill will:

- Keep every fact, condition, scope qualifier, and hedge of the source.
- Keep code, commands, identifiers, log lines, and quoted error text unchanged.
- Keep the user's chosen language. When the user writes in Korean, these rules govern Korean text. They do not switch you to English.

This skill will not:

- Rewrite creative, marketing, or persuasive copy, legal text, or quotations, where voice or exact wording is the point.
- Claim compliance with the official ASD-STE100 dictionary. ASD does not allow redistribution of its approved-word list, so this skill applies the principle (the plainest common word, used the same way every time) instead of a fixed word list. No equivalent official list exists for Korean. Read `references/sources.md` for the details.
- Make weak content true or useful. STE fixes the form of a text, not its substance. If a paragraph has nothing to say, say so instead of polishing it.
- Shorten past the point of clarity. Stop when the sentence is unambiguous, not when it is shortest.

## Additional resources

- `references/korean-structure.md`: Korean sentence structure (length, passives, nominalization, modifier stacks, omission, negation scope, tense, hedges), plus known linter false positives.
- `references/korean-wording.md`: Korean word choice (translationese, plain words, English inside Korean, calques, technical vocabulary).
- `references/korean-style.md`: Korean surface style (speech level, punctuation, AI tells, honorifics, labels, spelling, rhythm).
- `references/english.md`: English rules ported from the upstream ASD-STE100 skill.
- `references/glossary.md`: the glossary file format and maintenance protocol.
- `references/sources.md`: the standards, guidelines, and research behind each rule, and what is not verified.
- `examples/before-after.md`: worked rewrites in both languages, including agent-output cases.
- `scripts/ste-lint.py`: the bilingual linter. Run `--selftest` to check it, and `--help` for all options.
