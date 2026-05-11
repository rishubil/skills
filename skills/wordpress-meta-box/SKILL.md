---
name: wordpress-meta-box
description: WordPress Meta Box 플러그인 전문 스킬. 커스텀 필드·메타 박스·커스텀 포스트 타입을 코드 또는 UI 빌더로 구현하거나, Meta Box API(필드 설정, 액션·필터·함수 레퍼런스)를 조회해야 할 때 사용하세요.
---

# WordPress Meta Box 개발 가이드

> 공식 문서: https://docs.metabox.io/

Meta Box는 WordPress에서 커스텀 필드와 메타 박스를 생성·관리하는 플러그인입니다. 코드 기반 설정과 GUI 빌더(MB Builder) 양쪽을 지원합니다.

## 핵심 개념

| 개념 | 설명 |
|------|------|
| **Meta Box** | WordPress 편집 화면에 삽입되는 커스텀 필드 그룹 |
| **Field** | 텍스트·이미지·날짜 등 개별 입력 컨트롤 |
| **Field Group** | 여러 필드를 묶는 컨테이너 (메타 박스와 동의어) |
| **MB Builder** | 코드 없이 필드 그룹을 만드는 GUI 도구 |
| **MB Views** | Twig 템플릿으로 필드를 출력하는 확장 기능 |

## 기본 사용 패턴

### 코드로 메타 박스 등록

```php
add_filter( 'rwmb_meta_boxes', function( $meta_boxes ) {
    $meta_boxes[] = [
        'title'  => 'Event Details',
        'id'     => 'event-details',
        'post_types' => ['event'],
        'fields' => [
            [
                'name' => 'Start Date',
                'id'   => 'start_date',
                'type' => 'date',
            ],
            [
                'name' => 'Location',
                'id'   => 'location',
                'type' => 'text',
            ],
        ],
    ];
    return $meta_boxes;
} );
```

### 필드 값 출력

```php
// 단일 값
$value = rwmb_meta( 'field_id' );

// 포맷된 HTML 출력
rwmb_the_value( 'field_id' );

// 특정 포스트 지정
$value = rwmb_meta( 'field_id', [], $post_id );
```

## 주요 필드 타입

| 타입 | 용도 |
|------|------|
| `text`, `textarea` | 텍스트 입력 |
| `number`, `range` | 숫자 |
| `email`, `url`, `password` | 형식 검증 포함 텍스트 |
| `date`, `datetime`, `time` | 날짜·시간 선택기 |
| `select`, `radio`, `checkbox` | 선택 입력 |
| `select_advanced` | Select2 기반 고급 선택기 |
| `image`, `file`, `video`, `audio` | 미디어 업로드 |
| `image_advanced` | 다중 이미지 업로드 |
| `wysiwyg` | TinyMCE 에디터 |
| `oembed` | 미디어 임베드 URL |
| `color` | 색상 선택기 |
| `map`, `osm` | 지도 필드 |
| `post`, `taxonomy`, `user` | WordPress 객체 관계 |
| `group` | 중첩 필드 그룹 |

## 로컬 문서 (반드시 먼저 참고할 것)

이 스킬 디렉터리의 `references/` 폴더에 공식 문서 전체가 마크다운으로 저장되어 있습니다. API, 필드 옵션, 액션·필터·함수를 확인할 때는 **외부 URL을 열지 말고 로컬 파일을 Read하여 정확한 정보를 사용**하세요.

### references/ 디렉터리 구조

```
references/
├── index.md                        # 홈 (전체 개요)
├── getting-started.md              # 설치 및 시작하기
├── custom-fields.md                # 커스텀 필드 개요
├── custom-post-types.md            # 커스텀 포스트 타입
├── creating-fields-with-code.md    # 코드로 필드 생성
├── displaying-fields-with-code.md  # 코드로 필드 출력
├── cloning-fields.md               # 필드 복제(반복 필드)
├── database.md                     # 데이터 저장 방식
├── edit-meta-boxes.md              # 메타 박스 편집
├── extensions/                     # 확장 플러그인
│   └── *.md
├── field-settings/                 # 각 필드 타입 설정
│   └── *.md
├── fields/                         # 필드 타입별 상세 가이드
│   └── *.md
├── actions/                        # 액션 훅 레퍼런스
│   └── rwmb-*.md
├── filters/                        # 필터 훅 레퍼런스
│   └── rwmb-*.md
└── functions/                      # 함수 레퍼런스
    └── *.md
```

### 자주 찾는 문서 예시

| 주제 | 파일 경로 |
|------|-----------|
| 시작하기 | `references/getting-started.md` |
| 필드 타입 전체 목록 | `references/field-types.md` |
| 필드 공통 설정 | `references/field-settings/index.md` |
| 이미지 필드 | `references/fields/image-advanced.md` |
| 날짜 필드 | `references/fields/date.md` |
| 그룹 필드 | `references/fields/group.md` |
| 포스트 관계 필드 | `references/fields/post.md` |
| rwmb_meta() 함수 | `references/functions/rwmb-meta.md` |
| rwmb_the_value() 함수 | `references/functions/rwmb-the-value.md` |
| 저장 후 액션 | `references/actions/rwmb-after-save-post.md` |

문서를 찾을 때는 위 경로를 직접 Read하거나, `find /home/user/skills/skills/wordpress-meta-box/references -name "*.md" | grep <키워드>`로 검색하세요.
