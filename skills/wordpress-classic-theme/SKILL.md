---
name: wordpress-classic-theme
description: WordPress 클래식 테마 개발 전문 스킬. PHP 기반 클래식 테마를 처음 만들거나, 템플릿 계층·루프·테마 함수·사이드바·위젯·커스터마이저 API 등 클래식 테마 고유의 기능을 구현하거나 디버깅할 때 사용하세요. 블록 테마(FSE)는 다루지 않습니다.
---

# WordPress 클래식 테마 개발 가이드

> 공식 문서: https://developer.wordpress.org/themes/classic-themes/

WordPress 클래식 테마는 `index.php`, `style.css`를 필수 파일로 하는 PHP 기반 테마입니다. 템플릿 계층 구조, The Loop, 테마 함수, 커스터마이저 API 등 WordPress 고유 메커니즘을 직접 다룹니다.

## 핵심 개념

| 개념 | 설명 |
|------|------|
| **Template Hierarchy** | 요청 URL에 따라 어떤 템플릿 파일을 사용할지 결정하는 규칙 |
| **The Loop** | DB에서 포스트를 가져와 반복 출력하는 WordPress 핵심 패턴 |
| **Template Tags** | `the_title()`, `the_content()` 등 템플릿 내 출력 함수 |
| **Theme Functions** | `functions.php`에 등록하는 훅·기능 |
| **Conditional Tags** | `is_single()`, `is_archive()` 등 조건 분기 함수 |
| **Customizer API** | 실시간 미리보기를 지원하는 테마 옵션 UI |

## 기본 파일 구조

```
my-theme/
├── style.css          # 필수: 테마 메타데이터 + 스타일
├── index.php          # 필수: 기본 템플릿
├── functions.php      # 훅·기능 등록
├── header.php
├── footer.php
├── sidebar.php
├── single.php         # 단일 포스트
├── page.php           # 페이지
├── archive.php        # 아카이브
├── search.php
└── 404.php
```

## 자주 쓰는 패턴

### style.css 테마 헤더

```css
/*
Theme Name: My Theme
Theme URI: https://example.com
Author: Your Name
Description: A classic WordPress theme.
Version: 1.0.0
License: GNU General Public License v2 or later
Text Domain: my-theme
*/
```

### functions.php 기본 뼈대

```php
function my_theme_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    add_theme_support( 'menus' );
    register_nav_menus( [ 'primary' => __( 'Primary Menu', 'my-theme' ) ] );
}
add_action( 'after_setup_theme', 'my_theme_setup' );

function my_theme_scripts() {
    wp_enqueue_style( 'my-theme-style', get_stylesheet_uri() );
    wp_enqueue_script( 'my-theme-script', get_template_directory_uri() . '/js/main.js', [], '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'my_theme_scripts' );
```

### The Loop

```php
<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
    <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
    <?php the_excerpt(); ?>
<?php endwhile; else : ?>
    <p><?php esc_html_e( 'No posts found.', 'my-theme' ); ?></p>
<?php endif; ?>
```

## 로컬 문서 (반드시 먼저 참고할 것)

이 스킬 디렉터리의 `references/` 폴더에 공식 문서 전체가 마크다운으로 저장되어 있습니다. 템플릿 파일·훅·함수·Customizer API를 확인할 때는 **외부 URL을 열지 말고 로컬 파일을 Read하여 정확한 정보를 사용**하세요.

### references/ 디렉터리 구조

```
references/
├── index.md                              # 클래식 테마 개요
├── your-first-theme.md                   # 첫 번째 테마 만들기
├── basics/
│   ├── index.md                          # 기초 개요
│   ├── template-files.md                 # 템플릿 파일
│   ├── template-hierarchy.md             # 템플릿 계층 구조
│   ├── template-tags.md                  # 템플릿 태그
│   ├── the-loop.md                       # The Loop
│   ├── theme-functions.md                # functions.php
│   ├── post-types.md                     # 포스트 타입
│   ├── conditional-tags.md               # 조건 태그
│   ├── categories-tags-custom-taxonomies.md  # 분류체계
│   ├── main-stylesheet-style-css.md      # style.css
│   ├── organizing-theme-files.md         # 파일 구조
│   ├── including-css-javascript.md       # CSS/JS 로드
│   ├── linking-theme-files-directories.md # 파일 경로
│   ├── reworking-theme-files-organization.md
│   └── tools-resources.md
├── templates/
│   ├── index.md                          # 템플릿 파일 개요
│   ├── post-template-files.md            # 포스트 템플릿
│   ├── page-template-files.md            # 페이지 템플릿 파일
│   ├── page-templates.md                 # 페이지 템플릿 (커스텀)
│   ├── attachment-template-files.md      # 첨부파일 템플릿
│   ├── custom-post-type-template-files.md # CPT 템플릿
│   ├── taxonomy-templates.md             # 택소노미 템플릿
│   └── partial-and-miscellaneous-template-files/
│       ├── index.md                      # 부분 템플릿
│       └── comment-template.md           # 댓글 템플릿
├── functionality/
│   ├── index.md                          # 기능 개요
│   ├── custom-headers.md                 # 커스텀 헤더
│   ├── custom-backgrounds.md             # 커스텀 배경
│   ├── custom-logo.md                    # 커스텀 로고
│   ├── custom-front-page-templates.md    # 프론트 페이지
│   ├── featured-images-post-thumbnails.md # 대표 이미지
│   ├── navigation-menus.md               # 내비게이션 메뉴
│   ├── sidebars.md                       # 사이드바
│   ├── widgets.md                        # 위젯
│   ├── pagination.md                     # 페이지네이션
│   ├── post-formats.md                   # 포스트 포맷
│   ├── sticky-posts.md                   # 스티키 포스트
│   ├── 404-pages.md                      # 404 페이지
│   ├── media/
│   │   ├── index.md
│   │   ├── images.md
│   │   ├── video.md
│   │   ├── audio.md
│   │   └── galleries.md
│   ├── internationalization.md           # 국제화(i18n)
│   ├── localization.md                   # 현지화(l10n)
│   ├── accessibility.md                  # 접근성
│   ├── administration-menus.md           # 관리자 메뉴
│   ├── core-supported.md                 # 코어 지원 기능
│   └── block-theme-accessibility.md
├── customize-api/
│   ├── index.md                          # Customizer API 개요
│   ├── customizer-objects.md             # Panel·Section·Setting·Control
│   ├── the-customizer-javascript-api.md  # JS API
│   ├── javascriptunderscore-js-rendered-custom-controls.md
│   ├── tools-for-improved-user-experience.md # Selective Refresh 등
│   ├── advanced-usage.md                 # 고급 활용
│   └── other-resources.md
└── references/
    ├── index.md                          # 레퍼런스 목록
    ├── list-of-template-tags.md          # 템플릿 태그 전체 목록
    └── list-of-conditional-tags.md       # 조건 태그 전체 목록
```

### 자주 찾는 문서

| 주제 | 파일 경로 |
|------|-----------|
| 첫 테마 만들기 | `references/your-first-theme.md` |
| 템플릿 계층 구조 | `references/basics/template-hierarchy.md` |
| The Loop | `references/basics/the-loop.md` |
| 템플릿 태그 목록 | `references/references/list-of-template-tags.md` |
| 조건 태그 목록 | `references/references/list-of-conditional-tags.md` |
| functions.php | `references/basics/theme-functions.md` |
| CSS/JS 로드 | `references/basics/including-css-javascript.md` |
| 내비게이션 메뉴 | `references/functionality/navigation-menus.md` |
| 사이드바·위젯 | `references/functionality/sidebars.md` |
| 커스텀 로고 | `references/functionality/custom-logo.md` |
| 대표 이미지 | `references/functionality/featured-images-post-thumbnails.md` |
| Customizer 기본 | `references/customize-api/index.md` |
| Customizer 객체 | `references/customize-api/customizer-objects.md` |
| 페이지 템플릿 | `references/templates/page-templates.md` |
| 택소노미 템플릿 | `references/templates/taxonomy-templates.md` |

문서를 찾을 때는 위 경로를 직접 Read하거나, `find <스킬경로>/references -name "*.md" | grep <키워드>`로 검색하세요.
