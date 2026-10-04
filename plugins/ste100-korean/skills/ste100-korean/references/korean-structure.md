# Korean rules: sentence structure

These rules apply the core rules of `SKILL.md` to Korean sentence structure: length, actor and voice, frozen nouns, modifier scope, omission, negation, tense, and modality. Read this file for every Korean document or rewrite.

The Korean rules are split across three files that share one numbering (K1-K39):

- `korean-structure.md` (this file): K1-K17, plus known linter false positives.
- `korean-wording.md`: word choice, translationese, English inside Korean, calques, technical vocabulary (K18-K23, K29-K31, K39).
- `korean-style.md`: speech level, punctuation, AI tells, honorifics, labels, spelling, rhythm (K24-K28, K32-K38).

Each rule names the `ste-lint.py` rule ID when the linter checks it. "Source" lines point to `sources.md`. A rule marked *own calibration* has no published Korean norm behind it, and this skill chose the value.

## Sentences and length

### K1. Length caps: 15 어절 for instructions, 20 어절 for descriptions

Count 어절 (space-separated units). No Korean guideline gives a number. The 2015 공공언어 진단 기준 asks only whether "문장을 적절한 길이로 작성하였는가". These caps are *own calibration*. A Korean 어절 carries its particles and endings, so one 어절 holds more than one English word. The caps scale the English STE caps (20 and 25 words) down to match.

Lint: `ko-long-sentence` (cap 20, change with `--ko-max`).

### K2. One or two pieces of information per sentence

> 나쁨: 설정 파일을 읽은 뒤 값이 비어 있으면 기본값을 쓰고 경고를 로그에 남기며 다음 단계로 넘어갑니다.
> 좋음: 서버가 설정 파일을 읽습니다. 값이 비어 있으면 서버는 기본값을 쓰고 로그에 경고를 남깁니다. 그다음 서버는 다음 단계를 실행합니다.

When you split a sentence, add a connective (그다음, 따라서, 그러나) so the relation between the parts survives.

Source: 국립국어원 2021 지침 ("한 문장에는 한두 가지 정보만").

### K3. Do not chain 3 or more clauses with connective endings

Chains of -고, -며, -는데, -아서/-어서, -지만 delay the main verb to the end of a long sentence. The reader holds every clause in memory until the verb arrives. Split after the second clause.

Source: 2015 진단 기준 1.2.2 ("과도한 접속"), ste-ko 4.3.

## Actor and voice

### K4. Name the actor. Rewrite passives that hide it.

Korean forms passives with -되다, -받다, -당하다, and -어지다. Status text often uses them to hide who did what.

> 나쁨: 요청이 거부되었습니다.
> 좋음: 서버가 요청을 거부했습니다.

> 나쁨: 설정이 변경되었습니다.
> 좋음: 배포 스크립트가 설정을 바꿨습니다.

Keep the passive when the actor is unknown or irrelevant ("파일이 손상되었습니다" when nobody knows the cause). **Do not touch hedging verbs.** 예상되다, 추정되다, 판단되다, 생각되다, 예측되다, 전망되다, and 우려되다 carry the writer's confidence (K17). They are not passives to rewrite.

Lint: `ko-passive` (advisory, skips hedging verbs).

### K5. No double passives

A double passive stacks two passive markers. It is always wrong, and a single marker carries the same meaning.

| Double passive | Single |
|---|---|
| 되어지다, 되어집니다 | 되다, 됩니다 |
| 보여지다 | 보이다 |
| 잊혀지다 | 잊히다 |
| 쓰여지다 | 쓰이다 |
| 불려지다 | 불리다 |
| 닫혀지다, 열려지다 | 닫히다, 열리다 |
| 나뉘어지다 | 나뉘다 |

Often the best fix is K4: make it active and name the actor. "파일이 삭제되어졌습니다" becomes "서버가 파일을 삭제했습니다".

Lint: `ko-double-passive`. Source: 2021 지침, 2015 진단 기준 1.2.3, ste-ko 3.2.

### K6. Use -하다, not -시키다, when the subject acts directly

> 나쁨: 서비스를 재시작시킵니다. / 성능을 개선시켰습니다.
> 좋음: 서비스를 재시작합니다. / 성능을 개선했습니다.

Keep -시키다 only when the subject makes *someone else* act ("직원에게 교육을 받게 했다" is clearer than "직원을 교육시켰다" anyway).

Lint: part of `ko-translationese`. Source: 2021 지침.

## Frozen nouns

### K7. Use the verb. Do not freeze an action into a noun plus a light verb.

> 나쁨: 데이터베이스 백업 작업을 진행합니다. / 점검을 실시합니다. / 검증을 수행했습니다. / 배포가 이루어졌습니다.
> 좋음: 데이터베이스를 백업합니다. / 점검합니다. / 검증했습니다. / 배포했습니다.

The light verbs 진행하다, 실시하다, 수행하다, 시행하다, and 이루어지다 add length and hide the actor. Also rewrite "~중에 있다" as "~하고 있다".

Lint: `ko-light-verb`. Source: 2015 진단 기준 1.2.3, STE Rule 3.7.

### K8. Stack at most 3 nouns

> 나쁨: 인증 토큰 갱신 실패 처리 로직을 수정합니다.
> 좋음: 인증 토큰을 갱신하지 못했을 때 실행하는 코드를 고칩니다.

Untie a long stack with particles (의, 을/를) or with a clause. Headings and labels may stack nouns. The 2015 진단 기준 flags "세 단어 이상의 과도한 명사화 구성" outside titles, so prefer 2 when it reads equally well.

Lint: `ko-noun-stack` (needs the morphological analyzer, skips headings).

## Modifiers and scope

### K9. At most 2 modifying clauses in front of one noun. Put each modifier right before its target.

Korean puts modifying clauses before the noun. When clauses stack, the reader cannot tell which noun each one modifies.

> 나쁨: 사용자가 업로드한 이미지를 변환한 결과를 저장한 경로를 반환합니다.
> 좋음: 사용자가 이미지를 업로드합니다. 서버는 이미지를 변환하고 결과를 저장합니다. 이 함수는 저장 경로를 반환합니다.

> 모호함: 내가 좋아한 순이의 여동생 (내가 좋아한 사람이 순이인가, 여동생인가?)
> 명확함: 순이의 여동생 중 내가 좋아한 사람 / 내가 좋아한 순이, 그 순이의 여동생

Lint: `ko-adnominal-stack` (advisory, counts only clauses that modify a content noun, so "-ㄹ 수 있다" and "-는 것" do not count).
Source: 도재학 2018, 국립국어원 2021 지침 ("도내 내외국인 일용근로자를 고용하는 자"), ste-ko 2.3.

### K10. Make the scope of 와/과, 또는, and 및 explicit

> 모호함: 엄마는 아빠와 딸에게 선물을 했다. (엄마와 아빠가 함께 딸에게? 엄마가 아빠와 딸 둘에게?)
> 명확함: 엄마는 아빠에게도 딸에게도 선물을 했다.

> 모호함: 폐업 또는 허가 취소된 업체
> 명확함: 폐업했거나 허가가 취소된 업체

A long modifier in front of "A 또는 B" may cover only A or both. Repeat the modifier, or move it after the pair.

Source: 도재학 2018, 2015 진단 기준 1.2.2, 법제처 정비기준.

## Omission and reference

### K11. Do not drop a subject or object that the reader cannot recover

Korean drops subjects freely, and a human recovers them from context. An agent reading one message or one log line has no context. In a report, name who acted ("내가", "서버가", "사용자가"). In a procedure, the imperative implies the reader as subject, so that omission is fine.

> 나쁨: 확인했는데 문제없습니다.
> 좋음: 로그를 확인했습니다. 오류는 없었습니다.

The second version also names what was checked. "문제없습니다" alone hides the scope of the check (core rule 9).

Copyediting guides often recommend dropping English-style pronouns (그는, 그녀의) and turning an inanimate subject into a person or an adverbial clause ("이 그래프는 매출 증가를 보여 준다" becomes "이 그래프를 보면 매출이 늘었다"). Follow that advice only for rhetorical subjects in prose. In technical text, a system component is a real actor: "이 함수는 경로를 반환합니다" and "서버가 요청을 거부했습니다" are the clearest forms. Do not drop a pronoun if two possible referents exist.

Source: 2015 진단 기준 1.2.2 ("필수 성분 누락"), Hong & Kim 2008 (subject-predicate mismatch was the second-largest MT error source).

### K12. Name the referent instead of 이것, 그것, 해당, 위, 아래

"해당 파일" is common in Korean technical writing and is ambiguous as soon as two files appear. Repeat the noun ("설정 파일"). Use 위/아래 for direction only when the layout is fixed.

Source: 법제처 정비기준 ("지시어는 되도록 쓰지 않는다").

### K13. Do not drop particles in sentences

> 나쁨: 설정 파일 수정 후 서버 재시작 필요.
> 좋음: 설정 파일을 고친 다음 서버를 다시 시작하십시오.

Headings, table cells, and UI labels may drop particles. Sentences may not. Do not use arrows or symbols as verbs either: "설정 수정 → 재시작" becomes "설정을 고친 다음 서버를 다시 시작하십시오".

Source: 2015 진단 기준 ("과도한 조사 생략").

## Negation

### K14. Write double negatives as positives

> 나쁨: 재시작하지 않을 수 없습니다. / 영향이 없지 않습니다.
> 좋음: 재시작해야 합니다. / 영향이 있습니다.

Check the strength. "영향이 없지 않다" often means "조금 있다". Keep that hedge ("영향이 조금 있습니다") instead of asserting a full effect.

Lint: `ko-double-negation` (advisory). Source: 2021 지침, 법제처 정비기준.

### K15. Make negation scope explicit with 모두, 다, and 매우

> 모호함: 테스트가 모두 통과하지 않았습니다. (전부 실패? 일부만 실패?)
> 명확함: 테스트 12개 중 3개가 실패했습니다.

> 모호함: 그 응답은 매우 정확하지 않다.
> 명확함: 그 응답은 정확도가 낮다.

Replace the quantifier with a count when you have one. Korean negation markers are short (안, 못, -지 않-), so never cut them while shortening (core rule 10).

Source: 도재학 2018, 곽혜영·이미선 2010.

## Tense and aspect

### K16. Say whether a state holds now

"-었-" marks both a past event and a resulting state. "서버가 꺼졌습니다" can mean "the server went down at some point" or "the server is down now". "-고 있다" can mean an action in progress or a resulting state ("장갑을 끼고 있다").

Status text usually needs the current state. Write it out:

> 모호함: 배포가 끝났습니다.
> 명확함: 배포가 14시 20분(KST)에 끝났습니다. 지금 새 버전이 실행 중입니다.

This is the Korean counterpart of the English present-perfect exception in `english.md`. Avoid the double past "-었었-" ("노력했었어야 했다" becomes "노력해야 했다"). Shorten progressive and perfect calques when they add nothing: "도착하는 중입니다" becomes "도착합니다", and "노력을 기울여 왔다" becomes "노력했다". Keep them when the ongoing state or the duration is the point.

Source: 도재학 2018 (-었- ambiguity). The "-고 있다" note is *not verified* against a published source.

## Modality

### K17. Keep hedges. Collapse hedge stacks. Separate guess from fact.

Hedges carry the writer's confidence: ~ㄹ 수 있다, ~ㄹ 수도 있다, ~것 같다, ~로 보인다, ~ㄹ 가능성이 있다, 아마, 예상되다, 추정되다. Do not cut a hedge to shorten a sentence. Do not add one either.

When hedges stack, collapse them to one hedge of the same strength:

> 나쁨: 원인은 캐시 설정일 수도 있을 것으로 보입니다.
> 좋음: 원인은 캐시 설정일 수 있습니다.

Keep plan and schedule markers the same way: "4.0에서 제거될 예정입니다" must not become "4.0에서 제거됩니다" if the source only announced a plan.

"-ㄹ 수 있다" has two jobs. As ability filler, it can go: "읽을 수 있는 책이 많다" becomes "읽을 책이 많다". As possibility or uncertainty, it is a hedge and stays: "요청이 실패할 수 있다" keeps "수 있다". When you cannot tell which job it does, keep it.

Use the verb to show what you verified. "원인은 캐시 설정입니다" claims a verified fact. "원인은 캐시 설정으로 보입니다" claims an inference. Pick the one that matches the evidence.

No Korean guideline addresses hedges. This rule follows the upstream STE skill and ste-ko 3.7. The linter never flags hedges.

## Known linter false positives

The linter uses regex plus an optional morphological analyzer. It has no semantic understanding. Expect these misfires and judge each finding:

- `ko-translationese`: literal uses. "터널을 통해", "가방을 가지고 있다", "고객으로부터 받은 문의" (the source matters there).
- `ko-passive`: a passive where the actor is genuinely unknown.
- `ko-synonym-rotation`: two words that the glossary defines as different concepts.
- `ko-vague-quantity`: "일부" in a sentence that already gives the count elsewhere.
- Quoted source text: a `모호한 점:` line or a reply that quotes the original ("관리자에 의해 접수된") gets the original's findings. Do not rewrite a quotation.
- Regex fallback mode (no analyzer): `ko-noun-stack` and `ko-adnominal-stack` are off. Double-passive and light-verb detection rely on surface patterns and miss unusual conjugations.

Do not rewrite a correct sentence only to silence the linter. Use `--disable RULE`, or leave the finding and say why.
