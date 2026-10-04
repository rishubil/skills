# Korean rules: wording

These rules cover word choice in Korean text: translationese, plain words, vague quantities, one term per concept, abbreviations, English inside Korean text, filler, English-syntax calques, and the technical vocabulary Korean developers actually use. Read this file for every Korean rewrite and translation. Structure rules are in `korean-structure.md`, and style rules are in `korean-style.md`.

Rules K30, K31, and parts of K18-K19 adapt rule ideas from [im-ai-copyeditor](https://github.com/Turtle-Hwan/im-ai-copyeditor) (MIT), a Korean copyediting skill. That skill polishes text for human readers, keeps the sentence count fixed, and varies vocabulary. This skill disambiguates text, splits sentences, and fixes one term per concept. Where the two conflict, the rule says which way it goes.

## Word choice

### K18. Rewrite translationese

| Translationese | Write instead |
|---|---|
| ~에 대한, ~에 대해(서) | ~을/를, ~의, or delete: "오류에 대한 처리" becomes "오류 처리" |
| ~을/를 통해(서) | ~(으)로, ~에: "이번 기회를 통해" becomes "이번 기회에" |
| ~에 있어(서) | ~에서, ~할 때 |
| ~(으)로부터 | ~에게서, ~에서 |
| ~에 의해(서), ~에 의한 | ~(으)로, or an active sentence with the actor as subject |
| ~을/를 필요로 하다 | ~이 필요하다, ~해야 한다 |
| ~중에 있다 | ~하고 있다 |
| ~하는 것이 가능하다 | ~할 수 있다 |
| ~을/를 가지고 있다 (have) | ~이 있다 |
| ~할 경우 | ~하면 |
| 회의를 가지다 | 회의하다, 회의를 열다 |
| ~(으)로 인하여, ~(으)로 인한 | ~(으)로, ~때문에 |
| ~의 경우 | ~은/는, ~에는: "주말의 경우" becomes "주말에는" |
| ~에도 불구하고 | ~지만 |
| ~에 다름 아니다 | 바로 ~다 |
| ~을/를 요하다 | ~해야 한다 |
| ~에 의거하여 | ~에 따라 |
| ~에 위치하다 | ~에 있다 |
| ~하게 만들다 (make + adjective) | the intransitive or adjective form: "속도를 느리게 만든다" becomes "속도가 느려진다" |
| ~하기 위해(서) | ~하려고, ~하도록, when the purpose clause stacks on another clause |

"~(으)ㄹ 필요가 있다" is not translationese. The 2021 지침 uses it itself.

Lint: `ko-translationese` (advisory, because literal uses are legitimate: "터널을 통해 지나간다", "가방을 가지고 있다").
Source: 법제처 정비기준 일본어투 table, 김순영 2012, 2021 지침, 2015 진단 기준, im-ai-copyeditor S-9 to S-13 and S-26.

### K19. Use the plain word

| Hard | Plain |
|---|---|
| 제고 | 높임 |
| 소정의 | 정해진 |
| 득하여 | 받아 |
| 금일 | 오늘 |
| 익일 | 다음 날 |
| 컨펌 | 확인 |
| 로드맵 | 이행안, 일정 |
| 금번 | 이번 |
| 상기 내용 | 위 내용 |
| 불가합니다 | 할 수 없습니다 |
| 숙지하다 | 확인하다, 익히다 |

This table targets administrative and Sino-Korean jargon. It does not apply to technical terms. Do not turn an established IT loanword into a native word (락 into 잠금, 오퍼레이터 into 운영자). See K39. Domain terms follow the glossary (see `glossary.md`). Keep fixed wording in laws and contracts.

Lint: `ko-plain-word` (advisory). Source: 2021 지침, im-ai-copyeditor ST-7 and S-26.

### K20. Replace vague quantities with numbers

> 나쁨: 많은 요청이 실패했습니다. / 대량의 데이터를 처리합니다.
> 좋음: 요청 1,200건 중 340건이 실패했습니다. / 데이터 50 GB를 처리합니다.

For bounds, use 이상, 이하, 초과, 미만, and keep the boundary meaning exact: 이상 and 이하 include the boundary, 초과 and 미만 exclude it.

Give clock times a time zone, and anchor relative dates to an absolute date:

> 모호함: 어젯밤 21:02에 배포가 실패했습니다.
> 명확함: 10월 3일 21:02(KST)에 배포가 실패했습니다.

If the source does not state the time zone (a log line without an offset), say so instead of guessing.

Lint: `ko-vague-quantity` (advisory). Source: Kakao Developers 문서 가이드.

### K21. Delete unsupported quality claims

혁신적, 획기적, 원활한, 완벽한, 강력한, 매끄러운, 최첨단, 압도적, 손쉽게, 차세대, 극대화. Delete them, or replace them with the measurement that earns the claim.

Lint: `ko-marketing`.

### K22. One concept, one word

Pick one word per concept in a document. Common rotations in Korean technical text:

| Pick one |
|---|
| 오류 / 에러 |
| 삭제 / 제거 |
| 중지 / 중단 / 정지 |
| 사용 / 이용 / 활용 |
| 시작 / 개시 / 착수 |
| 사용자 / 유저 |
| 설정 / 세팅 |
| 확인 / 검증 / 점검 |
| 수정 / 변경 |
| 표시 / 출력 |

Some pairs differ in meaning in a given domain (확인 vs 검증, 중지 vs 정지). If both meanings are needed, define each in the glossary and use each only in its meaning.

Lint: `ko-synonym-rotation`. Source: STE one-word-one-meaning, Kakao Developers 문서 가이드 ("한 용어는 한 개념에만").

### K23. Spell out an abbreviation the first time

Write the Korean first and the abbreviation in parentheses: 인공지능(AI), 지속적 통합(CI). After the first use, use one form consistently. The glossary records which form the project uses.

Source: 2021 지침, Kakao Developers 문서 가이드.

## English inside Korean text

### K29. Follow the glossary for terms. Leave identifiers verbatim.

- A domain term takes its glossary form. On first use in a document, write the Korean form with the English in parentheses: 토큰(token). Do not add these parentheses in chat replies.
- When you rewrite the user's text and no glossary maps a term, keep the user's choice. If the source writes `retry`, `flaky test`, and `CI pipeline` in English, keep them in English. Fix only inconsistency within the text.
- Code identifiers, commands, file names, and error codes stay in English, inside backticks: `retry_count`, `npm install`.
- Choose the particle by how the word is read aloud in Korean. "API" reads 에이피아이, which ends in a vowel, so write "API를" and "API가". "token" reads 토큰, so write "token을". When the reading is unclear, rephrase so no particle follows the English word.

Lint: `glossary-avoid`, `glossary-bare-english`.

## Filler and English-syntax calques

### K30. Delete filler -적, -의, 것, and -들 when the meaning holds

> 나쁨: 기술적 문제로 인해 서버들의 응답의 지연이 발생했습니다.
> 좋음: 기술 문제로 서버 응답이 늦어졌습니다.

- **-적**: 환경적 요인 becomes 환경 요인. Keep -적 when it changes the meaning (기술적으로 가능하다).
- **-의**: 회사의 성장 becomes 회사 성장. Untie a chain of 3 or more 의 with particles or a verb.
- **것**: 백업하는 것이 중요하다 becomes 백업이 중요하다.
- **-들**: 여러 파일들을 becomes 여러 파일을. Keep -들 when the plural is the point and nothing else marks it.

Lint: `ko-genitive-chain` (advisory). Source: im-ai-copyeditor S-1 and S-17, 김순영 2012 (-들).

### K31. Undo English-syntax calques

| Calque | Write instead |
|---|---|
| 그 어떤 오류도 / 그 자신의 | 어떤 오류도 / 자신의 |
| 이것은 하나의 예시다 | 이것은 예시다 |
| ~라는 것은 분명하다 (dummy subject) | 분명히 ~다 |
| 가장 흔한 원인 중 하나다 | 흔한 원인이다, or give the rank if you know it |
| A는 B보다 더 빠르다 | A는 B보다 빠르다 |
| 왜 실패했는가를 분석했다 | 왜 실패했는지 분석했다 |
| 로그로 확인한 사실은 이것입니다. / 원인은 다음입니다. (Here's what...) | 로그를 보면 ~했습니다. / 원인은 ~입니다. |
| 여기서부터는 추정입니다. (From here on, this is speculation.) | 다음은 추정입니다. / ~로 추정합니다. |
| 결과가 없으면 vacuum이 끝났습니다. (If no rows, the vacuum has finished.) | 행이 하나도 나오지 않으면 vacuum이 끝난 상태입니다. |

Check the meaning first. "중 하나" sometimes carries real information (there are several causes). Keep it then.

Source: im-ai-copyeditor S-15, S-19, and S-20.

## Technical vocabulary

### K39. Use the field's own terms and the verbs they pair with

Korean developers use many loanwords as the standard terms, and each term pairs with particular verbs. A literal translation of either part reads as machine output, even when every word is correct Korean.

| English | Write | Pairs with | Not |
|---|---|---|---|
| lock | 락 | 락을 잡다, 락을 얻다, 락을 기다리다, 락이 풀리다 | 잠금을 쥐다 |
| lock timeout | 락 타임아웃 | 락 타임아웃이 나다, 락 타임아웃에 걸리다 | 잠금 대기 시간 초과 |
| statement (SQL) | 구문, 쿼리 | 쿼리를 취소하다, 구문이 실패하다 | 문장 |
| operator (a person or a k8s operator) | 오퍼레이터 | 오퍼레이터가 확인하다 | 운영자 (unless the project already uses it) |
| heartbeat | 하트비트 | 하트비트를 보내다 | 심장 박동 신호 |
| lease | 리스 | 리스를 잡다, 리스를 해제하다 | 임대 |
| deploy | 배포 | 배포하다, 배포가 실패하다 | 디플로이하다 |
| retry | 재시도 | 재시도하다 | 다시 시도 반복 |
| merge | 머지, 병합 | 머지하다 | |
| issue (tracker) | 이슈 | 이슈를 올리다 | 문제 제기 |

Check which form the project's existing documents and the glossary use, and follow them. If the user writes a term in English, keep it in English (K29). When you are unsure, write the form you would expect in a Korean engineering blog or in Korean documentation for the same tool.

