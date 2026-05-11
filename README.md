# rishubil/skills

개인적으로 사용하는 Claude [Agent Skills](https://agentskills.io) 모음입니다. Claude Code 플러그인 마켓플레이스로 등록하여 사용할 수 있습니다.

## 저장소 구조

```
.
├── .claude-plugin/
│   └── marketplace.json   # 마켓플레이스 정의 (플러그인 = 스킬 1:1)
├── skills/                # 스킬 모음 (각 폴더가 하나의 스킬)
│   └── <skill-name>/
│       └── SKILL.md
├── LICENSE
└── README.md
```

각 스킬은 `skills/<skill-name>/SKILL.md` 파일 하나만 있어도 동작합니다. 필요하면 같은 폴더에 스크립트나 보조 파일을 자유롭게 추가하면 됩니다.

이 마켓플레이스는 **스킬 하나를 플러그인 하나**로 분리해 등록합니다. 원하는 스킬만 골라 설치할 수 있도록 하기 위함입니다.

> **새 스킬을 추가할 때는 `.claude-plugin/marketplace.json`의 `plugins` 배열에 항목을 추가하고, 해당 항목의 `skills`에 `./skills/<skill-name>` 경로를 등록해야 합니다.**

## 제공 플러그인

| 플러그인 | 설명 |
| --- | --- |
| `shell-script` | Bash 셸 스크립트 작성 베스트 프랙티스와 에러 처리 패턴. |
| `fetch-docs` | 웹 기반 개발 문서를 깔끔한 마크다운으로 내려받아 디렉터리 구조 그대로 보관. |
| `monkey-c` | Garmin Connect IQ용 Monkey C 앱(Watch Face, Device App, Widget, Data Field 등) 개발. |
| `wordpress-meta-box` | WordPress Meta Box 플러그인 — 커스텀 필드·메타 박스·CPT 및 Meta Box API 전반. |
| `wordpress-classic-theme` | WordPress 클래식(PHP) 테마 — 템플릿 계층, 루프, 위젯, Customizer API 등. (블록 테마 제외) |
| `commit` | Conventional Commits 형식에 *왜* 변경했는지를 본문에 담아 커밋 메시지 작성. |

## Claude Code에서 사용하기

먼저 마켓플레이스를 등록합니다.

```
/plugin marketplace add rishubil/skills
```

필요한 플러그인을 개별적으로 설치합니다.

```
/plugin install <plugin-name>@rishubil-skills
```

예시:

```
/plugin install shell-script@rishubil-skills
/plugin install commit@rishubil-skills
```

설치 후에는 스킬 이름이나 설명을 언급하면 Claude가 자동으로 해당 스킬을 활용합니다.

## 참고

- [Agent Skills 공식 스펙](https://agentskills.io)
- [Anthropic의 예시 스킬 저장소](https://github.com/anthropics/skills)
- [커스텀 스킬 만들기 가이드](https://support.claude.com/en/articles/12512198-creating-custom-skills)
