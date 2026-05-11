---
name: fetch-docs
description: Fetch web-based development documentation and save it as clean markdown files while preserving the site's directory structure. Use this skill whenever the user wants to download, archive, or save online documentation locally — including phrases like "fetch the docs from X", "save this documentation as markdown", "download the docs at [URL]", "convert these web docs to markdown", "archive this docs site", or "cache the API reference from [URL]". Also trigger when a user pastes a docs URL and says they want it saved or stored locally.
---

# fetch-docs

웹 기반 개발 문서를 크롤링하여 URL 경로를 유지한 디렉터리 구조로 깔끔한 마크다운 파일로 저장합니다.

## 사전 준비

```bash
npx agent-browser --version   # 확인
npx defuddle --version        # 확인
URL_UTILS="$(find ~/.claude ~/.local/share/chezmoi/.claude -name url_utils.py -path '*/fetch-docs/*' 2>/dev/null | head -1)"
```

## 핵심 도구 역할

| 도구 | 역할 |
|------|------|
| **agent-browser** | 실제 브라우저로 페이지를 열고 네비게이션 링크를 탐색 (SPA/JS 렌더링 대응) |
| **defuddle** | 각 페이지에서 본문만 추출하여 깔끔한 마크다운으로 변환 |
| **url_utils.py** | URL 정규화, 파일 경로 변환, 범위 필터링 |

## 파일 경로 결정 원칙

URL → 파일 경로 매핑 시 **전체 URL 목록을 먼저 수집한 뒤** `smart-filepaths` 명령으로 일괄 결정합니다.
하위 URL이 있으면 `path/index.md`, 없으면 `path.md`로 저장합니다:

```
/reference/commands/   (하위: /add/, /apply/ 존재)  → reference/commands/index.md
/reference/commands/add/  (하위 없음)               → reference/commands/add.md
/user-guide/daily-ops/    (하위 없음)               → user-guide/daily-ops.md
```

## 워크플로

### 1단계: 파라미터 확인

```bash
BASE_URL="https://docs.example.com"   # 크롤링 시작 URL (경로 없이 도메인 루트 권장)
OUTPUT_DIR="./docs-example-com"       # 저장 디렉터리
```

사용자에게 확인:
- **시작 URL**: 문서 루트 URL (경로 포함 가능)
- **저장 디렉터리**: 기본값은 도메인명 기반 (`./docs-example-com/`)

### 2단계: 네비게이션 완전 탐색 → URL 목록 수집

이 단계가 가장 중요합니다. **모든 URL을 누락 없이 수집해야** 올바른 파일 경로를 결정할 수 있습니다.

```bash
agent-browser open "$BASE_URL"
agent-browser wait --load networkidle
```

#### 네비게이션 완전 펼치기

많은 문서 사이트는 사이드바가 접혀 있습니다. 모든 섹션을 펼쳐야 합니다:

```bash
# 1. 전체 스냅샷으로 접힌 섹션 파악
agent-browser snapshot -i -u

# 2. 접힌 섹션(토글/아코디언)을 모두 클릭해서 펼치기
#    스냅샷에서 [LabelText], [button], [details summary] 형태의 토글을 찾아 클릭
agent-browser click @e5   # 예: "Advanced" 섹션 토글
agent-browser click @e9   # 예: "Reference" 섹션 토글

# 3. 펼친 후 다시 스냅샷
agent-browser snapshot -i -u
```

#### URL 추출 전략

문서 사이트의 네비게이션 패턴에 맞게 선택:

**패턴 A — 사이드바 전체 탐색** (MkDocs, Docusaurus 등):
```bash
# 사이드바 영역만 스코프해서 모든 링크 추출
agent-browser snapshot -i -u -s "nav"
agent-browser snapshot -i -u -s ".sidebar"
agent-browser snapshot -i -u -s ".md-nav"
```

**패턴 B — 메인 탭/섹션별 탐색** (섹션마다 별도 네비게이션이 있는 경우):
```bash
# 각 상위 섹션 페이지로 이동해 그 섹션의 사이드바를 스냅샷
for SECTION_URL in "https://docs.ex.com/user-guide/" "https://docs.ex.com/reference/"; do
  agent-browser open "$SECTION_URL"
  agent-browser wait --load networkidle
  agent-browser snapshot -i -u -s "nav"
done
```

**패턴 C — 사이트맵 활용** (빠른 완전 수집):
```bash
# 많은 사이트가 sitemap.xml을 제공
curl -s "https://docs.example.com/sitemap.xml" | grep -oP '<loc>\K[^<]+'
```

#### 반복 탐색으로 누락 URL 보완

각 페이지를 저장한 후 그 페이지에서도 새 링크를 발견할 수 있습니다:
```bash
# 저장한 각 페이지에서 추가 링크 확인
agent-browser open "$PAGE_URL"
agent-browser wait --load networkidle
agent-browser snapshot -i -u
# 새로 발견한 URL을 큐에 추가
```

### 3단계: URL 목록 완성 및 파일 경로 일괄 결정

수집한 URL들을 필터링하고 파일 경로를 결정합니다:

```bash
# 수집한 모든 링크를 JSON 배열로 구성
LINKS='["/guide/install", "https://docs.example.com/guide/usage", ...]'

# 범위 내 URL 필터링 (외부 링크, 이진 파일, 중복 제거)
VISITED='["https://docs.example.com"]'
FILTERED=$(python3 "$URL_UTILS" filter "$BASE_URL" "$VISITED" "$LINKS")

# 전체 URL 목록이 확정되면 파일 경로를 일괄 결정
# smart-filepaths: 하위 URL 유무를 기준으로 path.md vs path/index.md 자동 선택
echo "$FILTERED" | python3 "$URL_UTILS" smart-filepaths "$BASE_URL"
# 출력: {"https://docs.ex.com/guide/": "guide.md", "https://docs.ex.com/reference/": "reference/index.md", ...}
```

### 4단계: 각 페이지 수집 및 저장

파일 경로 매핑을 얻은 뒤 각 URL을 처리합니다:

```bash
PAGE_URL="https://docs.example.com/guide/installation"
REL_PATH="guide/installation.md"   # smart-filepaths 결과에서

# defuddle로 마크다운 추출
npx defuddle parse "$PAGE_URL" --markdown --output /tmp/page_content.md

# 페이지 제목 추출
PAGE_TITLE=$(npx defuddle parse "$PAGE_URL" --property title 2>/dev/null)

# 저장
FULL_PATH="$OUTPUT_DIR/$REL_PATH"
mkdir -p "$(dirname "$FULL_PATH")"
{
  printf -- "---\ntitle: %s\nsource: %s\n---\n\n" "$PAGE_TITLE" "$PAGE_URL"
  cat /tmp/page_content.md
} > "$FULL_PATH"

echo "저장됨: $FULL_PATH"
```

### 5단계: 완료 리포트

```bash
echo "=== 수집 완료 ==="
find "$OUTPUT_DIR" -name "*.md" | sort
echo "총 파일 수: $(find "$OUTPUT_DIR" -name "*.md" | wc -l)"
agent-browser close
```

## URL → 파일 경로 매핑 예시

`smart-filepaths` 적용 시 (전체 URL 목록 기준):

| URL | 하위 URL 있음 | 저장 경로 |
|-----|:---:|-----------|
| `https://docs.ex.com/` | ✓ | `index.md` |
| `https://docs.ex.com/install/` | ✗ | `install.md` |
| `https://docs.ex.com/reference/` | ✓ | `reference/index.md` |
| `https://docs.ex.com/reference/commands/` | ✓ | `reference/commands/index.md` |
| `https://docs.ex.com/reference/commands/add/` | ✗ | `reference/commands/add.md` |
| `https://docs.ex.com/user-guide/daily-ops/` | ✗ | `user-guide/daily-ops.md` |

## 엣지 케이스

### SPA 사이트 (React, Vue, Vite 등 공식 문서)
- `wait --load networkidle` 필수
- 사이드바 토글 버튼이 있으면 클릭 후 재스냅샷

### 접힌 네비게이션 완전 펼치기
```bash
# LabelText나 button 형태 토글을 모두 클릭
agent-browser snapshot -i  # ref 확인
agent-browser click @e12   # 토글 클릭
agent-browser snapshot -i -u  # 펼쳐진 링크 확인
```

### defuddle 추출 실패 시
```bash
npx defuddle parse "$PAGE_URL" --json | python3 -c "
import json, sys
d = json.load(sys.stdin)
print('length:', len(d.get('content', '')))
"
# 내용이 너무 짧으면 로그에 기록하고 넘어감
```

### 로그인이 필요한 문서
```bash
agent-browser auth save docs-site --url https://docs.example.com/login \
  --username user@example.com --password-stdin
agent-browser auth login docs-site
```

## scripts/url_utils.py 명령 참조

```bash
# URL → 파일 경로 (단일, 하위 URL 정보 없이 단순 변환)
python3 "$URL_UTILS" filepath "https://docs.ex.com/guide/install" "https://docs.ex.com"
# → guide/install.md

# URL → 파일 경로 (단일, 전체 URL 목록 기반)
python3 "$URL_UTILS" smart-filepath "https://docs.ex.com/guide/" "https://docs.ex.com" \
  '["https://docs.ex.com/guide/", "https://docs.ex.com/guide/install/"]'
# → guide/index.md  (하위 /install/ 존재하므로)

# URL → 파일 경로 일괄 처리 (stdin에 JSON 배열 입력)
echo '["https://docs.ex.com/guide/", "https://docs.ex.com/guide/install/"]' \
  | python3 "$URL_UTILS" smart-filepaths "https://docs.ex.com"
# → {"https://docs.ex.com/guide/": "guide/index.md", "https://docs.ex.com/guide/install/": "guide/install.md"}

# URL 정규화 (프래그먼트 제거)
python3 "$URL_UTILS" normalize "https://docs.ex.com/guide#section"
# → https://docs.ex.com/guide

# 링크 배열 필터링
python3 "$URL_UTILS" filter \
  "https://docs.ex.com" \
  '["https://docs.ex.com/guide"]' \
  '["/api/ref", "https://external.com", "#skip", "/guide"]'
# → ["https://docs.ex.com/api/ref"]

# 범위 내 URL 확인
python3 "$URL_UTILS" in-scope "https://docs.ex.com/guide/foo" "https://docs.ex.com"
# → true
```
