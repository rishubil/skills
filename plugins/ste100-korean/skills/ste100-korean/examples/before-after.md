# Before / after examples

These are original illustrations, not quotes from any real system. The English examples in Part 2 are adapted from the upstream ASD-STE100 skill (MIT).

Korean length is counted in 어절 (space-separated units). English length is counted in words (`text.split()`).

## Part 1: Korean

### Example K-A: Tool description (Strict)

**Before:**
> 이 도구는 설정된 여러 백엔드 간의 상태 동기화를 수행하며, 충돌이 감지될 경우 설정된 전략에 따라 자동으로 해결될 수 있고, 그렇지 않은 경우에는 수동 검토를 위해 충돌이 표시되어집니다.

**Violations:**
- One sentence carries three claims: sync, automatic resolution, and the manual fallback (K2). It has 22 어절, over the 20 어절 cap (K1).
- 동기화를 수행하며: a frozen noun (K7).
- 감지될, 해결될, 표시되어집니다: passives that hide the actor (K4). 표시되어집니다 is also a double passive (K5).
- ~할 경우: translationese (K18).

Not a violation: 해결될 수 있고. That is a hedge. The tool does not promise to resolve every conflict, and the rewrite must not promise it either.

**After:**
> 이 도구는 설정한 백엔드의 상태를 동기화합니다. 충돌을 찾으면 도구는 설정한 전략을 읽습니다. 전략이 자동 해결을 허용하면 도구가 충돌을 해결할 수 있습니다. 도구가 충돌을 해결하지 않으면 수동 검토를 위해 충돌을 보고합니다.

The last sentence branches on whether the tool resolved the conflict, not on what the strategy allows. That is what 그렇지 않은 경우 meant: the fallback also covers a permitted resolution that did not happen.

### Example K-B: Error message (Strict)

**Before:**
> 요청 처리 과정에서 예상 데이터 형식과의 불일치로 인한 오류가 발생했을 가능성이 있으며, 이는 구버전 클라이언트 사용에 의한 것일 수 있습니다.

**Violations:**
- Three claims in one sentence: the request may have failed, a format mismatch, and an old client (K2).
- 요청 처리 과정, 예상 데이터 형식: noun stacks that hide the actor (K8).
- ~에 의한: translationese (K18).

Not violations: 발생했을 가능성이 있으며 and 것일 수 있습니다. The system does not know what went wrong. Both hedges report that uncertainty accurately.

**After:**
> 요청이 실패했을 수 있습니다. 데이터 형식이 서버가 예상한 형식과 다를 수 있습니다. 클라이언트 버전이 오래되면 이 불일치가 생길 수 있습니다. 클라이언트 버전을 확인하십시오.

**This example is the reason for core rule 8.** A tempting rewrite is "요청이 실패했습니다. 원인은 대부분 구버전 클라이언트입니다." It reads better, and it is wrong twice. It asserts a failure that the system only suspects, and it invents a frequency ("대부분") that the source never stated.

### Example K-C: Instruction for another agent (Strict, 한다체)

**Before:**
> 업스트림 작업이 완료되고 에러가 발생되지 않았다는 전제 하에, 다운스트림 에이전트는 결과물 아티팩트에 대한 소비를 진행해야 하며, 타임아웃 상황에서는 부분적인 아티팩트가 생성되는 경우도 있다는 점에 유의할 필요가 있다.

**Violations:**
- One sentence carries a condition, an action, and a warning (K2). It has 22 어절, over the 15 어절 instruction cap (K1).
- 발생되지: an unnecessary passive (K4). 에 대한 소비를 진행해야: translationese plus a frozen noun (K7, K18).
- 에러 and 오류 rotate in this project's other docs. The glossary fixes 오류 (K22).

**After:**
> 업스트림 작업이 오류 없이 끝날 때까지 기다린다. 그다음 결과 아티팩트를 읽는다. 경고: 시간 초과가 나면 아티팩트가 일부만 만들어질 수 있다. 아티팩트를 쓰기 전에 아티팩트가 완전한지 확인한다.

Two deliberate calls:
- 진행해야 하며 became the plain imperative 읽는다. In an instruction for the executing agent, a recommendation is a command. Do not make this move in descriptive text.
- The last sentence is **new**. The source warned about partial artifacts but did not say what to do. The added check makes the warning actionable, but it is added content, so it is called out here. Drop it if the source's silence was deliberate.

### Example K-D: Status reply to the user (Flavored, 합니다체)

**Before:**
> 말씀하신 배포 건 확인해 봤는데요, 인증서 쪽에서 문제가 발생된 것으로 보여지며 조만간 안정화 작업이 진행될 예정입니다.

**Violations:**
- 보여지며: double passive (K5). 발생된: an unnecessary passive (K4).
- 안정화 작업이 진행될: a frozen noun plus a passive, so nobody owns the next step (K4, K7).
- 확인해 봤는데요: the scope of the check is hidden (K11, core rule 9). Mixed speech levels: 해요체 and 합니다체 (K24).
- 조만간: a vague time that the writer cannot back up.

**After:**
> 배포는 인증서 문제로 실패한 것으로 보입니다. 배포 로그에서 인증서 검증 오류를 확인했습니다. 인증서 만료일은 아직 확인하지 않았습니다. 지금 만료일을 확인하고 결과를 알려 드리겠습니다.

The rewrite keeps the hedge (것으로 보입니다), separates the checked fact from the unchecked one, and gives the next action an owner. "배포 로그에서 ... 확인했습니다" must be true. If the writer checked nothing, write "아직 아무것도 확인하지 않았습니다" instead. Never invent the check.

### Example K-E: README prose (Flavored)

**Before:**
> 저희 캐싱 레이어는 기존 스택에 원활하게 통합되도록 설계되었으며, 시맨틱 유사도를 활용하여 LLM 워크로드의 캐시 미스를 획기적으로 감소시킵니다.

**Violations:**
- 원활하게, 획기적으로: unsupported quality claims (K21).
- 감소시킵니다: -시키다 where -하다 works (K6).
- 설계되었으며: a passive that hides the actor (K4).

**After:**
> 일반 캐시는 요청을 글자 그대로 비교합니다. 그래서 표현이 조금만 달라도 캐시 미스가 납니다. 이 캐시는 새 프롬프트의 뜻을 저장된 프롬프트와 비교해서 캐시 미스를 줄입니다. 기존 스택을 바꾸지 않고 붙여 쓸 수 있습니다.

The source gives no measurement for 획기적으로, so the rewrite says only 줄입니다. If the measured reduction exists, add it. Do not invent one. 기존 스택을 바꾸지 않고 is the rewrite's reading of 원활하게 통합. Check it with the author if the source meant something narrower.

Flavored mode kept the explanatory rhythm and did not lock every term. It still cut the claims and the passive.

### Example K-F: Glossary in action

The project's `GLOSSARY.md` has these rows:

| English | 한국어 | Definition | Avoid |
|---|---|---|---|
| rollback | 롤백 | Restore the previous release after a failed deploy. | 되돌리기, revert |
| token | 토큰 | An opaque credential string that the auth server issues. | 징표 |

**English source:**
> If the token refresh fails, the deploy script triggers a rollback.

**Before (Korean draft):**
> 징표 갱신이 실패하면 배포 스크립트가 되돌리기를 실행합니다.

**After:**
> 토큰(token) 갱신이 실패하면 배포 스크립트가 롤백(rollback)을 실행합니다.

징표 and 되돌리기 are in the `Avoid` column. This is the first use in the document, so each Korean term carries its English in parentheses. Later sentences write 토큰 and 롤백 alone.

## Part 2: English

### Example E-A: Tool description (Strict)

**Before:**
> This tool will attempt to synchronize state across the various backends that have been configured, and if a conflict is detected it may resolve it automatically depending on the strategy that has been set, or otherwise it will surface the conflict for manual review.

**Violations:** two instructions in one sentence, present perfect in the relative clauses ("have been configured", "has been set"), and 44 words against a 25-word cap. Not flagged: "will attempt to" and "may resolve". Those are hedges.

**After:**
> The tool tries to synchronize state across the configured backends. If it finds a conflict, it reads the configured strategy. If the strategy allows automatic resolution, the tool may resolve the conflict without a user. If the tool does not resolve the conflict, it reports the conflict for manual review.

### Example E-B: Error message (Strict)

**Before:**
> An error may have occurred while processing your request due to a possible mismatch in the expected data format, which could be caused by an outdated client version.

**After:**
> Your request may have failed. The cause may be a data format that does not match what the server expects. An outdated client can cause this mismatch. Check your client version.

"may have failed" keeps a compound verb form that the simple-tense rule would remove. When the tense rule and the modality rule conflict, modality wins.
