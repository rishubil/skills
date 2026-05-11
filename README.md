# rishubil/skills

개인적으로 사용하는 Claude [Agent Skills](https://agentskills.io) 모음입니다. Claude Code 플러그인 마켓플레이스로 등록하여 사용할 수 있습니다.

## 저장소 구조

```
.
├── .claude-plugin/
│   └── marketplace.json   # 마켓플레이스 정의
├── skills/                # 스킬 모음 (각 폴더가 하나의 스킬)
│   └── <skill-name>/
│       └── SKILL.md
├── LICENSE
└── README.md
```

각 스킬은 `skills/<skill-name>/SKILL.md` 파일 하나만 있어도 동작합니다. 필요하면 같은 폴더에 스크립트나 보조 파일을 자유롭게 추가하면 됩니다.

> **새 스킬을 추가할 때는 `.claude-plugin/marketplace.json`의 `plugins[].skills` 배열에 해당 스킬 경로(`./skills/<skill-name>`)를 함께 등록해야 합니다.**

## Claude Code에서 사용하기

마켓플레이스를 등록합니다.

```
/plugin marketplace add rishubil/skills
```

플러그인을 설치합니다.

```
/plugin install personal-skills@rishubil-skills
```

설치 후에는 스킬 이름이나 설명을 언급하면 Claude가 자동으로 해당 스킬을 활용합니다.

## 참고

- [Agent Skills 공식 스펙](https://agentskills.io)
- [Anthropic의 예시 스킬 저장소](https://github.com/anthropics/skills)
- [커스텀 스킬 만들기 가이드](https://support.claude.com/en/articles/12512198-creating-custom-skills)
