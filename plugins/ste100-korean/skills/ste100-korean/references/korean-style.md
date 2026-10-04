# Korean rules: style

These rules cover the surface of Korean text: sentence-ending level, punctuation, AI tells and decoration, honorifics, labels, spelling, and rhythm. Read this file when you write or polish a document that will be kept or published, and when a reply has headings or lists. Structure rules are in `korean-structure.md`, and word-choice rules are in `korean-wording.md`.

Rules K32-K38 adapt rule ideas from [im-ai-copyeditor](https://github.com/Turtle-Hwan/im-ai-copyeditor) (MIT), a Korean copyediting skill. That skill varies vocabulary and keeps the sentence count fixed. This skill fixes one term per concept and splits sentences. Where the two conflict, the rule says which way it goes.

## Speech level

### K24. Use one sentence-ending level per text

Pick one level and keep it:

- 합니다체 (하십시오체): docs, reports, error messages, and chat with the user unless the user's own register suggests otherwise.
- 해요체: chat and UI text when the product or the user uses it.
- 한다체: specs, commit bodies, and prompts or instructions for other agents.

Mixing levels makes the reader wonder whether a change in level signals a change in authority or audience. List items, headings, and table cells may use noun endings (~함, ~음, or a bare noun), but use the same form for every item in one list.

Lint: `ko-speech-level` (advisory). Source: Kakao Developers 문서 가이드, Microsoft Korean localization style guide.

## Punctuation

### K25. No semicolons

The Korean punctuation rules (한글 맞춤법 문장 부호) do not define the semicolon. Use a period, or join clauses with -고 or -며 within the K3 limit.

Lint: `semicolon`. Source: 양명희, 국립국어연구원. The 2015 rule text itself is *not verified*.

### K26. Do not write a range with a single tilde

Many Markdown renderers, including GitHub, read a single `~` as strikethrough. `3~5개` can render as broken text.

> 나쁨: 3~5개, 10~20초
> 좋음: 3-5개, 10-20초, or 3개 이상 5개 이하

Lint: `ko-tilde-range`. Source: ste-ko 8.1.

### K27. Do not use a slash for "and/or"

"A/B" can mean A and B, A or B, or A per B. Write "A와 B", "A 또는 B", or "A나 B 중 하나 이상".

Source: ste-ko 8.4.

### K28. Do not nest parentheses

Put the inner remark in its own sentence.

Source: ste-ko 8.2.

## AI tells and decoration

These patterns mark text as machine-written. They also add words that carry no meaning, so they cost every reader time.

### K32. Drop formula frames

| Frame | Fix |
|---|---|
| Grand openers: "오늘날 빠르게 변화하는 시대에", "바야흐로" | Start with the content. |
| Meta openers: "좋은 질문입니다", "말씀하신 대로", "확인해 보겠습니다", "다음과 같습니다", "간단히 말하자면" | Delete. Give the answer or the result. |
| Closers: "결국 균형이 중요합니다", "결론적으로" before a restatement | Delete the restatement. End with the next action or the last fact. |
| "단순한 X가 아니라 Y입니다" | State Y and the evidence. |
| "중요한 것은 X입니다", "X라는 점에서 의미가 있습니다" | "X가 중요합니다", or say why X matters. |
| "~라는 것이다", "~라는 점이다" at the end | End with the predicate: "꾸준해야 한다". |
| "이 기술은 효율 향상을 가능하게 한다" | "이 기술로 효율을 높일 수 있다" |
| Slogans: "검색을 넘어 발견으로" | Say what the thing does. |

Keep a formula only when it carries content that the rewrite would lose.

Lint: `ko-ai-tell` (advisory). Source: im-ai-copyeditor AI-1, AI-2, AI-3, and AI-8.

### K33. Do not decorate

- No emoji in docs, reports, commit text, or replies unless the user writes with emoji.
- Use bold for at most one key term or warning per paragraph.
- Do not put quotation marks around a word for emphasis. Quotation marks mark a quotation or a literal string.
- In Korean prose, do not list items with a middle dot (·). Write "A와 B", "A, B, C". A middle dot may stay in a heading, a table cell, or a fixed name.
- In Korean prose, do not attach a clause with an em dash (—) or a spaced hyphen. Split the sentence, or use a comma or a colon. Keep hyphens in identifiers (`react-joyride`) and ranges (3-5개).

Lint: `ko-middle-dot`, `ko-dash` (advisory). Source: im-ai-copyeditor AI-6.

### K34. Mark vague sources. Never invent one.

"많은 전문가들은 ~라고 말합니다" and "한 연구에 따르면" without a citation make a claim that the reader cannot check. Name the source if you know it. If you do not, say so ("출처를 확인하지 못했습니다") or drop the claim. Never invent a source, a number, or a quotation to make a sentence concrete (core rules 8 and 9).

Source: im-ai-copyeditor AI-9.

## Honorifics, labels, and spelling

### K35. Do not honor objects

Put the honorific -시- only on a person or on something closely tied to a person (간접높임: "선생님은 말씀이 있으시다").

> 나쁨: 요청하신 작업이 완료되셨습니다. / 결제 금액은 만 원이십니다.
> 좋음: 요청하신 작업이 끝났습니다. / 결제 금액은 만 원입니다.

Do not use "-실게요" for an action the reader takes. Write "확인해 주세요", not "확인해 보실게요".

Lint: `ko-honorific-object` (advisory, narrow patterns only). Source: im-ai-copyeditor ST-3 and ST-4.

### K36. End labels with a noun

Headings, table headers, bold list lead-ins, step names, captions, and button labels end with a noun, whatever the body's speech level is. This includes headings inside a chat reply.

> 나쁨: ## 설치하기 / ## 무엇을 고치나요 / 표 헤더 "하는 일" / ## 다시 배포해도 되는지
> 좋음: ## 설치 / ## 고치는 항목 / 표 헤더 "기능" / ## 재배포 가능 여부

Source: im-ai-copyeditor ST-9.

### K37. Spell correctly

Spelling errors make a reader doubt the rest. The errors agents make most often:

| Wrong | Right | Note |
|---|---|---|
| 되요, 됬다 | 돼요, 됐다 | 돼 = 되어 |
| 안되요, 않돼요 | 안 돼요 | 안 = 아니 (adverb), 않 = 아니하 (verb stem) |
| 할께요 | 할게요 | |
| 아니예요, 책이예요 | 아니에요, 책이에요 | 이에요 after a consonant (책이에요), 예요 after a vowel (사과예요), 아니에요 always |
| 관리자로써 승인한다 | 관리자로서 승인한다 | 로서 marks a role, 로써 marks a means (대화로써 해결한다) |
| 몇일 | 며칠 | |
| 어떻해 | 어떡해, 어떻게 | |
| 금새 | 금세 | |
| 비률, 효률, 성공율 | 비율, 효율, 성공률 | -율 after a vowel or ㄴ, -률 elsewhere |
| 카드로 결재했다 | 카드로 결제했다 | 결제 = payment, 결재 = approval |

For anything else, check the 국립국어원 rules (<https://korean.go.kr/kornorms/>). Source: im-ai-copyeditor G-1 to G-24.

## Rhythm in Flavored mode

### K38. Vary sentence length and endings. Never vary terms.

A run of sentences with the same length and the same ending (~합니다. ~합니다. ~합니다.) reads as machine text. In Flavored mode, vary the length, and vary the ending within the same speech level (~합니다, ~입니다, ~습니까, ~하십시오). Do not mechanically number every paragraph (첫째, 둘째, 셋째) unless the order matters.

Copyediting guides also recommend varying vocabulary. **This skill does not.** Repeating the same word for the same concept is core rule 1, not a style flaw. Vary the sentence, not the term.

Strict mode keeps a fixed pattern on purpose: a procedure is easier to follow when every step has the same shape.

Source: im-ai-copyeditor AI-5 and §8, ste-ko 4.8.

