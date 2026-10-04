# English rules

These rules apply the core rules of `SKILL.md` to English. They are adapted from the upstream ASD-STE100 skill ([danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), MIT). Rule numbers in parentheses refer to ASD-STE100 Issue 9.

STE rules come in two kinds. **Structural rules** describe sentence shape, and you can apply them from the description alone. **Lexical rules** depend on the official ~900-word STE dictionary, which this skill does not reproduce (see `sources.md`). Apply the structural rules with confidence. Treat the lexical rules as a direction of travel, and do not claim dictionary compliance.

## Structural rules

| Rule | Do | Don't |
|---|---|---|
| Active voice | "The agent deletes the file." | "The file is deleted (by the agent)." Keep the passive only when the actor is unknown or irrelevant. |
| No phrasal verbs (9.3) | "Remove the panel." "Start the job." | "Take off the panel." "Spin up the job." A two-word verb has meanings that its parts do not predict. |
| One instruction per sentence | "Open the file. Read line 3." | "Open the file and read line 3, then check if it matches." |
| Sentence length | 20 words or fewer for instructions, 25 or fewer for descriptions | Long compound or subordinate-clause sentences |
| No semicolons (8.1) | Split into separate sentences. | Any semicolon. STE permits every other standard mark, including the em dash, although an em dash often signals a sentence to split. |
| Noun clusters | 3 words or fewer as one noun phrase ("fuel pump valve") | 4 or more stacked nouns ("high pressure fuel pump inlet valve assembly") |
| No ellipsis | Keep the subject, verb, and article explicit. | "Files not backed up will be lost" (which files?) |
| Keep modality | "The request **may have** failed." | "The request failed." (a hedge promoted to a fact) |
| Paragraphs | One topic per paragraph, 6 sentences or fewer | Multi-topic paragraphs |
| Lists for sequences | A numbered or bulleted list for 3 or more steps or conditions | A sequence buried in one sentence |

## Lexical rules: direction of travel only

| Rule | Do | Don't | Why it is weaker here |
|---|---|---|---|
| One word, one meaning | Pick one verb per action and reuse it ("check" every time). | Rotate "check", "verify", "confirm" for one action. | Consistency is checkable. Which word is the *approved* one needs the dictionary. |
| One part of speech per word | "Apply oil to the valve." | "Oil the valve." | Whether "oil" is approved as a noun only is a dictionary fact. |
| Verb, not noun (3.7) | "Analyze the log." | "Perform an analysis of the log." | Preferring the verb is always safe. Which verb is approved needs the dictionary. |
| Domain terms | Keep necessary terms and define each once. Record cross-language pairs in the glossary. | Use jargon without defining it. | STE allows a project glossary on top of its base dictionary, but the base dictionary is absent here. |

## Simple tenses, with one exception

STE permits the infinitive, imperative, simple present, simple past, simple future, and the past participle as an adjective. It excludes the present perfect and other compound forms: "we received the report", not "we have received the report".

Aircraft manuals never need the present perfect. Status text sometimes does. "The job has completed" (and its output is available now) and "the job completed" (at some past point) are different statements. **Where the compound form carries information that the simple form cannot (current relevance, or a hedge as in "may have failed"), keep it.** Elsewhere, follow the rule.

## Scan checklist

These six habits cause most misreadings in machine-written English. Each one is mechanical: you can point at the word or mark that breaks the rule.

1. **Synonym rotation.** One thing gets several names ("the user", "the customer", "the client"). Pick one name.
2. **Hedge stacking.** Qualifiers pile up until the sentence asserts nothing ("it is important to note that this may potentially help to improve"). Collapse them to one hedge of the same strength, or delete the empty sentence.
3. **Nominalization.** An action frozen into a noun ("perform an analysis of", "provide assistance to"). Use the verb.
4. **Marketing adjectives.** Seamless, robust, powerful, cutting-edge, effortless, blazing-fast. Delete them, or replace them with a measurement.
5. **Run-on sentences.** Several ideas joined by semicolons or em dashes. Write one idea per sentence.
6. **Soft phrasal verbs.** Spin up, reach out, dive into, kick off, circle back, touch base. Use the single plain verb (start, contact, read, begin).

## AI tells and plain words

These patterns come from the `unslop` skill (cursor/plugins `pstack`, MIT). They mark text as machine-written, and most of them also add words that carry no meaning.

| Pattern | Fix |
|---|---|
| AI vocabulary: delve, crucial, pivotal, tapestry, testament, underscore (verb), showcase, foster, garner, intricate, interplay, vibrant, enduring, "Additionally," | The plain word, or nothing |
| Filler: "in order to", "due to the fact that", "it is important to note that", "in the event that" | "to", "because", delete, "if" |
| Fancy words: utilize, leverage (verb), facilitate, numerous | use, use, help, many |
| Fancy "is": "serves as", "stands as", "boasts" | "is", "has" |
| Superficial -ing tails: "..., highlighting the need for", "..., ensuring that" | Delete, or make it a sentence with a real subject |
| False ranges: "from small scripts to large systems" when the ends are not on one scale | List the items |
| Mid-sentence colons used as connectors | Let the point stand as its own sentence. Keep colons before a list or an example. |
| Em dashes | End the sentence, or use a comma |
| Bold labels that restate the line: "**Performance:** Performance improved" | Prose. A bold lead-in that ends in a period and is followed by new detail is fine. |
| Title Case Headings | Sentence case |
| Curly quotes in English text | Straight quotes |
| Mannered prose: aphorisms ("wire it or delete it"), figurative verbs ("rides along"), code personified for effect ("the plan holds it") | The literal phrase. A system component that really acts is not personification: "the server rejects the request" is correct. |

Parentheses stay allowed. The glossary first-use form 토큰(token) and abbreviation expansions need them. Do not nest them.

## Linter coverage

`ste-lint.py` checks these English rules: `semicolon`, `phrasal-verb`, `marketing-adjective`, `nominalization`, `long-sentence`, `synonym-rotation`, and `dangling-conjunction` (hard), plus `passive-voice`, `present-perfect`, `ai-vocabulary`, `filler-phrase`, `plain-word`, `fancy-is`, `chatbot-phrase`, `em-dash`, `curly-quote`, `arrow-speak`, `title-case-heading`, and `inline-header` (advisory). It does not check noun-cluster length in English, and it knows only a short list of phrasal verbs, so "take off the panel" passes. It never flags hedges or modal perfects ("may have failed").
