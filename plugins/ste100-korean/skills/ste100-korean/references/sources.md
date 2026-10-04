# Sources

This file lists the standards, guidelines, and research behind the rules, and states what was not verified. Research date: 2026-10-04.

## ASD-STE100

ASD-STE100 (Simplified Technical English) is a controlled-language standard from ASD, the AeroSpace and Defence Industries Association of Europe. It was first released in 1986. The current edition is Issue 9 (January 2025). It has 53 writing rules in 9 sections and a dictionary of about 900 approved words (one meaning and one part of speech each) plus about 1,200 words to avoid.

The standard is free to obtain but not free to redistribute. Issue 9 allows reproduction only with ASD's written authority, or by eight listed categories of organization. This skill belongs to none of them. It therefore paraphrases rule categories and does not reproduce the rule text or the dictionary. Request the standard at <https://www.asd-ste100.org/STE_downloads.html> when exact approved wording matters.

- <https://www.asd-ste100.org/>
- <https://www.asd-europe.org/standards-specifications/simplified-technical-english/>
- <https://en.wikipedia.org/wiki/Simplified_Technical_English>

## Upstream skills

- **danyuchn/asd-ste100-skill** (MIT, (c) 2026 Dustin Yuchen Teng). This skill adapts its structure, process, output format, modality rule, English rules, and linter. <https://github.com/danyuchn/asd-ste100-skill>
- **beamonic/ste-ko** (MIT, (c) 2026 Beamonic). A Korean controlled-language spec with 73 rules. This skill borrows several rule ideas from it (tilde ranges, modifier-clause limit, connective-chain limit, slash and nested parentheses, guess vs. fact) and its regex stem-expansion technique. <https://github.com/beamonic/ste-ko>
- **Turtle-Hwan/im-ai-copyeditor** (MIT, (c) 2026 Turtle-Hwan). A Korean copyediting skill with sentence, AI-tell, style, and spelling rulebooks. Rules K30-K38 and parts of K16-K19 adapt its rule ideas, with new examples. This skill rejects its vocabulary-variation and fixed-sentence-count principles because they conflict with one-term-one-meaning and one-idea-per-sentence. Its sentence rulebook credits 김정선, 『내 문장이 그렇게 이상한가요?』 (유유, 2016) as inspiration. Its AI-tell rulebook cites 박종향·김은영 (2025), 「생성형 AI 텍스트와 인간 텍스트의 내용 및 문체 비교 연구」, 교양교육연구 19(6). <https://github.com/Turtle-Hwan/im-ai-copyeditor>
- **cursor/plugins `pstack` unslop skill** (MIT, (c) 2026 Lauren Tan). A checklist of AI tells in English prose. `english.md` "AI tells and plain words" and parts of core rules 7, 12, and 15 adapt it. This skill does not adopt its blanket ban on parentheses, because the glossary first-use form needs them. <https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md>

## Korean public-language guidance

- **국어기본법 제14조**: public institutions must write official documents "일반 국민이 알기 쉬운 용어와 문장으로". The 2026 text was not re-verified.
- **국립국어원, 「2015년 중앙행정기관 공공언어 진단」** (연구책임 최홍열). Criteria 1.2.2 and 1.2.3: missing required constituents, agreement errors, excessive conjunction, ambiguity, noun stacks of three or more words, excessive modifier clauses, unnecessary passives and causatives, translationese. It gives no numeric sentence length.
- **국립국어원, 「행정문서 표현 개선 및 쉬운 공공언어 쓰기 지침 개발」** (2021, 연구책임 정희창). The guideline in appendix 7 covers plain words, double passives, "한 문장에는 한두 가지 정보만", modifier placement, double negatives, and abbreviations in brackets. <https://www.korean.go.kr/front/reportData/reportDataView.do?mn_id=45&report_seq=1122>
- **국립국어원, 「쉬운 공문서 쓰기 길잡이」** (2022). The PDF exceeded the fetch limit and was not read directly.
- **법제처, 「알기 쉬운 법령 정비기준」**, chapter 3 (문장편). It covers explicit subjects and objects, long-sentence splitting, ambiguity, double negatives, active voice, modifier scope around "A 또는 B", demonstratives, and the 일본어투 replacement table. <https://opinion.lawmaking.go.kr/lmKnlg/abRprStd>
- **행정안전부, 행정업무운영 편람**: accuracy (6하원칙, no ambiguous wording) and ease ("문장은 가급적 짧게 끊어서 항목별로", conclusion first). Core rule 16 (lead with the outcome) follows it, together with the Kakao guide's inverted-pyramid rule and ste-ko 6.1.
- **양명희, 「문장 부호의 이해」** (국립국어연구원, about 2000): the semicolon is not a Korean punctuation mark. The 2015 punctuation rule text itself was not read.

## Korean linguistics and controlled-language research

- **도재학 (2018), 「국어 문장의 중의성에 대하여」**, 아시아문화연구 46, pp. 39-72. Modifier-scope, negation-scope, 와/과-scope, quantifier, pronoun, and -었- ambiguity.
- **곽혜영·이미선 (2010)**, 「언어」 35(3). Quantifier and negation scope in Korean. Abstract only.
- **Hong & Kim (2008), "Controlled Korean for Korean-English MT"**, PACLIC 22, pp. 391-396. Eight error types, including subject-predicate mismatch, sentence-initial topic -은/는, ambiguous words, and light verbs. <https://aclanthology.org/Y08-1040.pdf>
- **함수진·류수린 (2010)**, 번역학연구 11(4). -되다 ambiguity (passive vs. change of state) in Korean-Japanese technical MT. Abstract only.
- **김순영 (2012), 「영한 번역에 나타난 번역투 문장」**, 새국어생활 22(1). Translationese catalog. <https://www.korean.go.kr/nkview/nklife/2012_1/22_0105.pdf>

## Industry style guides

- **Kakao Developers 문서 가이드**: one term per concept, concrete numbers with 이상/이하/초과/미만 instead of vague quantities, present tense, active voice, first-use English in parentheses. <https://developers.kakao.com/docs/ko/documentation-guideline/document-style-open>
- **Microsoft Korean localization style guide**: translationese fixes (X에 대한 Y, 수행하다), referents made explicit when unclear, unnecessary -들 dropped.

## Not verified, or own calibration

- No Korean source gives a numeric sentence-length limit. The 15/20 어절 caps are own calibration (see `korean-structure.md` K1).
- No Korean source gives a rule on hedges. K17 follows the upstream skill.
- The "-고 있다" progressive/resultative ambiguity note was not checked against a published source.
- The 2015 punctuation rule text and the current 국어기본법 text were not read directly.
