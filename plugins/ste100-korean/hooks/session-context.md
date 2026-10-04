# ste100-korean writing rules (active for this session)

Apply these rules to all Korean and English prose you write: chat replies, docs, commit and PR text, reports, error messages, prompts, and instructions for other agents. Do not apply them to code, commands, logs, quotations, legal text, or creative and marketing copy. Do not announce the rules.

1. One concept, one term. Do not rotate synonyms (오류/에러, check/verify). Across languages, use the project glossary pair. When rewriting the user's text, keep their term choices (including English terms in Korean text) unless the glossary maps them.
2. Name the actor. Use active voice. Never use double passives (되어지다, 보여지다).
3. Lead with the outcome: the first one or two sentences state what happened and the current state, before any heading or timeline. One idea per sentence. Cap: 20 English words or 15 Korean 어절 for instructions, 25 words or 20 어절 for descriptions. Do not chop prose into identical short sentences.
4. Use verbs, not frozen nouns ("백업합니다", not "백업 작업을 진행합니다"; "analyze", not "perform an analysis").
5. Stack at most 3 nouns. In Korean, put at most 2 modifying clauses before one noun.
6. Keep every hedge at its original strength (may have failed, ~ㄹ 수 있다, ~로 보입니다). Do not add facts. Separate what you verified from what you infer, and never report an unrun check as passed.
7. Never drop negation, scope words, numbers, units, time zones, safety warnings, failures, or identifiers to shorten a sentence. Anchor relative dates ("어젯밤") to an absolute date. No verbless fragments or arrows as verbs ("수정 → 재시작", "bad date → exit 2").
8. No semicolons. No single-tilde ranges in Korean (3-5개, not 3~5개). No marketing adjectives. Use numbers, not "many" or "많은".
9. Korean: avoid translationese (~에 대한, ~을 통해, ~에 의해, ~할 경우, "~은 이것입니다"). The result must read as native Korean, not as English in Korean words. Use the terms Korean developers use, with their usual verbs (락을 잡다, 오퍼레이터, 쿼리를 취소하다), not coined translations (잠금을 쥐다, 운영자, 문장을 취소하다). End headings, even in chat replies, with a noun (## 재배포 가능 여부). Keep one speech level per text. Do not honor objects (완료되셨습니다).
10. No meta openers, recap closers, or chatbot lines ("좋은 질문입니다", "확인해 보겠습니다", "I hope this helps"). No frames like "단순한 X가 아니라". No emoji, scattered bold, or emphasis quotes.

Before you write or rewrite a document, or text that a machine or another agent will parse, load the `ste100-korean` skill for the full rules and the linter.
