# CLAUDE.md

이 저장소는 Claude Code 플러그인 마켓플레이스(`rishubil-skills`)로 등록되는 개인용 Agent Skills 모음입니다. 작업할 때 다음 규칙을 따르세요.

## 저장소 구조

- `.claude-plugin/marketplace.json` — 마켓플레이스 매니페스트. 플러그인 항목과 각 플러그인에 포함되는 스킬 경로를 정의.
- `skills/<skill-name>/SKILL.md` — 개별 스킬. 폴더 하나가 곧 하나의 스킬이며 `SKILL.md`는 YAML frontmatter(`name`, `description`)와 본문 지시사항으로 구성.
- `skills/<skill-name>/` 하위에 스크립트나 보조 리소스를 자유롭게 둘 수 있음.

## 플러그인 구성 원칙

- 이 마켓플레이스는 **스킬 하나당 플러그인 하나**를 원칙으로 한다. 사용자가 필요한 스킬만 골라 설치할 수 있어야 하기 때문이다.
- 플러그인 이름(`plugins[].name`)은 포함된 스킬의 폴더명과 동일하게 맞춘다.
- 여러 스킬을 묶어야 할 합당한 이유가 생기기 전까지는 새 스킬마다 새 플러그인 항목을 추가한다.

## 새 스킬을 추가할 때

1. `skills/<new-skill-name>/SKILL.md` 를 생성한다.
   - `name`은 폴더명과 동일하게, 소문자와 하이픈만 사용.
   - `description`은 "무엇을 하는지 + 언제 사용해야 하는지"가 한두 문장에 모두 드러나도록 작성.
2. **반드시** `.claude-plugin/marketplace.json` 의 `plugins` 배열에 새 플러그인 항목을 추가한다.
   - `name`은 스킬 폴더명과 동일.
   - `description`은 영어 한 문장 정도로 간결하게.
   - `source`는 `"./"`, `strict`는 `false`.
   - `skills` 배열에 `./skills/<new-skill-name>` 경로 추가.
   - 누락하면 마켓플레이스를 통해 설치되지 않는다.
3. 필요하면 `README.md` 의 "제공 플러그인" 표에도 새 항목을 추가한다.

## 스킬 수정/삭제 시

- 스킬 폴더를 삭제하거나 이름을 바꾸면 `marketplace.json` 의 해당 플러그인 항목(또는 그 `skills` 배열)도 동기화하고, `README.md` 의 플러그인 목록도 함께 갱신한다.
- `SKILL.md` 의 `name` 필드는 폴더명과 일치해야 한다.

## 커밋/푸시

- 작업 브랜치는 사용자가 지정한 브랜치를 사용하고, 임의로 `main`에 직접 푸시하지 않는다.
- 커밋 메시지는 변경의 "왜"를 1~2문장으로 간결하게 작성한다.

## 참고 링크

- [Agent Skills 스펙](https://agentskills.io)
- [Anthropic 예시 스킬 저장소](https://github.com/anthropics/skills)
