# Claude Code Web — Cloud Session Plugin Setup

Claude Code web에서 새 세션을 시작할 때 플러그인이 자동으로 설치된 상태로 시작하도록 설정하는 방법을 설명합니다.

## 배경

현재 Claude Code web 환경에서는 `/plugin marketplace add <github-repo>` 명령으로 마켓플레이스를 직접 추가할 수 없습니다. 이 제한을 우회하기 위해 **SessionStart 훅**을 사용합니다. 훅 스크립트가 GitHub에서 마켓플레이스 저장소를 ZIP으로 다운로드해 로컬 경로에 풀어놓고, 그 경로를 마켓플레이스로 등록한 뒤 원하는 플러그인을 설치합니다.

## 동작 원리

```
SessionStart 훅 실행
  └─ add_marketplace()
       ├─ GitHub에서 저장소 ZIP 다운로드
       ├─ ~/.claude/plugins/local-marketplaces/<name>/ 에 압축 해제
       ├─ (선택) marketplace.json 의 name 필드를 중립 이름으로 교체
       └─ claude plugin marketplace add <로컬 경로>
  └─ claude plugins install <plugin>@<marketplace>
```

`rename_marketplace`가 필요한 이유: `anthropics/claude-plugins-official` 같은 저장소의 `marketplace.json`에는 공식 이름(`claude-plugins-official` 등)이 들어 있는데, 타인이 동일한 이름의 마켓플레이스를 등록하면 사칭 방지 로직에 의해 거부될 수 있습니다. `name` 필드를 `local-mirror` 같은 중립 이름으로 바꿔서 이를 우회합니다.

## 설정 방법

### 1. 훅 스크립트 작성

아래 템플릿을 `.claude/hooks/session-start.sh`로 저장한 뒤, 필요에 맞게 마켓플레이스와 플러그인 목록을 수정합니다.

```bash
#!/usr/bin/env bash
set -euo pipefail

# 웹 세션에서만 실행
if [[ "${CLAUDE_CODE_REMOTE:-}" != "true" ]]; then
    exit 0
fi

DEBIAN_FRONTEND=noninteractive apt-get update -qq && apt-get install -y -q gh jq

MARKETPLACE_BASE="$HOME/.claude/plugins/local-marketplaces"
mkdir -p "$MARKETPLACE_BASE"

get_default_branch() {
    local branch
    branch=$(curl -sSL "https://api.github.com/repos/$1" 2>/dev/null \
        | jq -r '.default_branch // empty' 2>/dev/null || true)
    echo "${branch:-main}"
}

# rename_marketplace <dir> <new_name>
rename_marketplace() {
    local dir="$1" new_name="$2"
    local manifest="$dir/.claude-plugin/marketplace.json"
    if [[ -f "$manifest" ]]; then
        local tmp
        tmp=$(mktemp)
        jq --arg n "$new_name" '.name = $n' "$manifest" > "$tmp" && mv "$tmp" "$manifest"
        echo "[rename] marketplace.json name -> $new_name"
    else
        echo "[rename] WARN: manifest not found at $manifest" >&2
    fi
}

# add_marketplace <dir_name> <repo> [manifest_name_override]
add_marketplace() {
    local name="$1" repo="$2" rename_to="${3:-}"
    local branch
    branch=$(get_default_branch "$repo")
    echo "[$name] default branch: $branch"

    local tmp_zip tmp_dir
    tmp_zip=$(mktemp /tmp/mktmp-XXXXXX.zip)
    tmp_dir=$(mktemp -d /tmp/mktmp-XXXXXX)

    curl -fsSL "https://github.com/$repo/archive/refs/heads/$branch.zip" -o "$tmp_zip"
    unzip -q "$tmp_zip" -d "$tmp_dir"
    rm "$tmp_zip"

    rm -rf "$MARKETPLACE_BASE/$name"
    mv "$tmp_dir/${repo##*/}-$branch" "$MARKETPLACE_BASE/$name"
    rm -rf "$tmp_dir"

    if [[ -n "$rename_to" ]]; then
        rename_marketplace "$MARKETPLACE_BASE/$name" "$rename_to"
    fi

    claude plugin marketplace add "$MARKETPLACE_BASE/$name"
    echo "[$name] added"
}

# ── 마켓플레이스 등록 ────────────────────────────────────────────
add_marketplace "rishubil-skills"   "rishubil/skills"
add_marketplace "local-mirror"      "anthropics/claude-plugins-official" "local-mirror"
add_marketplace "karpathy-skills"   "multica-ai/andrej-karpathy-skills"

# ── 플러그인 설치 ────────────────────────────────────────────────
claude plugins install shell-script@rishubil-skills
claude plugins install commit@rishubil-skills
claude plugins install plan-review@rishubil-skills
claude plugins install fetch-docs@rishubil-skills
npm install -g agent-browser defuddle   # fetch-docs 의존성
claude plugins install skill-eval-hook@rishubil-skills
claude plugins install ascii-diagram@rishubil-skills
claude plugins install andrej-karpathy-skills@karpathy-skills
claude plugins install skill-creator@local-mirror
```

```bash
chmod +x .claude/hooks/session-start.sh
```

### 2. SessionStart 훅 등록

`.claude/settings.json`에 아래 내용을 추가합니다 (파일이 없으면 새로 생성).

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  }
}
```

### 3. 커밋 및 푸시

```bash
git add .claude/hooks/session-start.sh .claude/settings.json
git commit -m "chore: add SessionStart hook for cloud session plugin setup"
git push
```

이후 이 저장소로 열리는 모든 Claude Code web 세션에서 훅이 자동으로 실행되어 플러그인이 설치됩니다.

## 커스터마이징

### 마켓플레이스 추가

```bash
add_marketplace "<로컬-폴더명>" "<owner>/<repo>"
# 이름 충돌이 우려되는 공식 저장소는 세 번째 인자로 중립 이름 지정
add_marketplace "my-mirror" "<owner>/<official-repo>" "my-mirror"
```

### 플러그인 추가/제거

`claude plugins install` / `claude plugins uninstall` 줄을 추가하거나 삭제합니다. `@<마켓플레이스명>`은 `add_marketplace` 첫 번째 인자(또는 rename 시 세 번째 인자)와 일치해야 합니다.

### 로컬 세션 제외

스크립트 상단의 `CLAUDE_CODE_REMOTE` 체크가 웹 세션에서만 훅을 실행하도록 보장합니다. 로컬 Claude Code CLI에서는 아무 동작도 하지 않습니다.

## 주의사항

- 훅은 세션 시작 시 **동기적으로** 실행됩니다. 설치에 걸리는 시간만큼 세션 시작이 지연됩니다.
- 네트워크 환경에 따라 GitHub ZIP 다운로드가 실패할 수 있습니다. 재시도 로직이 없으므로 필요하다면 `add_marketplace` 에 `curl` 재시도 옵션(`--retry 3`)을 추가하세요.
- `apt-get install gh jq`는 Debian/Ubuntu 기반 컨테이너를 가정합니다. Claude Code web의 실행 환경이 변경되면 이 부분도 함께 수정해야 합니다.
