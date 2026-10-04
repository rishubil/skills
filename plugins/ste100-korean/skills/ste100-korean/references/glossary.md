# Glossary protocol

Core rule 1 says to name each concept with one term. In a project that writes in both English and Korean, that rule needs one more step: each English term maps to exactly one Korean term, and each Korean term maps back to exactly one English term. The glossary file records these pairs, so every session and every agent uses the same words.

## Location

Use the first file that exists, relative to the project root:

1. `GLOSSARY.md`
2. `docs/GLOSSARY.md`
3. `docs/glossary.md`

If none exists, create `GLOSSARY.md` at the project root the first time you translate a project document (a README, docs, a spec) from English to Korean or the reverse, or write a new one in both languages.

Do not create a glossary for a chat reply, a status report in chat, a rewrite of text the user pasted, or a polish of an existing document, even a bilingual one. A glossary file the user did not ask for is noise. If the existing text uses mismatched terms across the two languages, suggest a glossary in one line of your reply. In those cases, follow an existing glossary if there is one, and otherwise keep the source's terms consistent within the text. If no project directory applies, do not create files at all.

## Format

One Markdown table. The `English` and `한국어` columns are required. `Definition` and `Avoid` are optional but recommended. Sort rows by the English term.

```markdown
# Glossary

English-Korean term pairs for this project. Each English term maps to one Korean term, and each Korean term maps to one English term.

| English | 한국어 | Definition | Avoid |
|---|---|---|---|
| API | API | Keep as-is. | 에이피아이 |
| rollback | 롤백 | Restore the previous release after a failed deploy. | 되돌리기, revert |
| token | 토큰 | An opaque credential string that the auth server issues. | 징표, 토컨 |
| repository | 저장소 | A Git repository. | 리포지토리, 레포, repo |
```

- **English**: the canonical English term, in lowercase unless it is a proper noun or an acronym.
- **한국어**: the canonical Korean term. It may equal the English term (keep-as-is).
- **Definition**: one sentence. It settles which meaning the pair carries, so a word with two senses does not slip into a second meaning.
- **Avoid**: comma-separated variants in either language that writers must not use for this concept. List the variants that people actually write.

Wrap a cell in backticks only when the term is a code identifier. The linter strips backticks.

## Choosing the Korean term

The test is what Korean developers actually say and write in this field, not what a dictionary offers. A coined Korean translation of an established loanword reads as machine translation. Decide in this order:

1. **Keep as-is** for code identifiers, product and brand names, file formats, protocol names, and acronyms that Korean developers say in English (API, URL, JSON, Git). Write the same string in both columns.
2. **Transliterate** when the loanword is the term the field already uses (락, 토큰, 서버, 캐시, 오퍼레이터, 하트비트). Follow the 외래어 표기법 spelling (메서드, not 메소드). In IT text this is the usual case. Do not replace an established loanword with a native word because it looks plainer (잠금 for lock, 운영자 for operator).
3. **Translate** only when the Korean word is itself the established term (배포 for deploy, 저장소 for repository, 재시도 for retry).

See `korean-wording.md` K39 for common terms and the verbs they pair with.

If the project's existing documents already use a form consistently, keep that form even if this order suggests another. If the user names a preferred term, the user's choice wins. Record it.

## Workflow

**Before writing.** If a glossary exists, read it before you write Korean or English prose that uses domain terms. Use the paired term. Never use a term from the `Avoid` column.

**When a project document introduces a term.** If a document you write or translate uses a domain term that is not in the glossary, add a row in the same change. Put the variants you rejected in `Avoid`. Mention the new rows in one line of your reply ("GLOSSARY.md에 `rollback | 롤백`을 추가했습니다").

**When you rewrite the user's text.** Keep the source's term choices, including English terms inside Korean text, unless the glossary maps them. The user chose those words. Fix inconsistency (two names for one thing), not the choice of language.

**First use in a document.** In a Korean document, write the Korean term with the English in parentheses the first time: 롤백(rollback). After that, write the Korean term alone. In an English document, write the English term alone. Do not add these parentheses in chat replies. There, write the term the way the conversation already uses it.

**When a pair must change.** Changing an existing pair renames a concept across the project. Ask the user first. Then update every document that uses the old term, and move the old term into `Avoid`.

**Conflicts.** If two rows map one English term to two Korean terms, or one Korean term to two English terms, the glossary is broken. Either the concepts differ, and then each pair needs its own definition and a distinct term, or they are one concept, and then you merge the rows. Ask the user when you cannot tell.

## What not to put in the glossary

- Ordinary words that every reader translates the same way (file, list, everyday verbs). Add a word anyway when writers in this project actually rotate variants of it, such as 오류 and 에러 for "error".
- Every code identifier in the project. Identifiers stay verbatim in backticks and need no pair. Add one only when prose also refers to the concept by name.
- Temporary names from one conversation.

## Linter checks

`ste-lint.py` loads the glossary automatically from the locations above, or from `--glossary PATH`. It checks:

- `glossary-duplicate` (hard): a term maps to two partners, or an `Avoid` term equals a canonical term.
- `glossary-avoid` (hard): an `Avoid` term appears in the linted text.
- `glossary-bare-english` (advisory): a Korean sentence uses an English glossary term without its Korean partner. The accepted first-use form is 토큰(token).
