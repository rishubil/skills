# resticprofile 설정 설명

## 구성 개요

이 설정은 TOML 형식으로 작성된 resticprofile 구성 파일로, `base` 프로필과 이를 상속하는 `documents`, `photos` 두 프로필로 구성됩니다.

---

## `base` 프로필

공통 설정을 담는 부모 프로필입니다.

- **`repository`**: 백업 저장소 경로를 `/mnt/nas/backup`으로 설정합니다.
- **`password-file`**: restic 저장소 암호화에 사용할 패스워드 파일 경로를 `/root/.restic-password`로 지정합니다.
- **`[base.retention]`**: 보존 정책을 정의합니다.
  - `keep-daily = 7` — 일별 스냅샷 7개 유지
  - `keep-weekly = 4` — 주별 스냅샷 4개 유지
  - `keep-monthly = 12` — 월별 스냅샷 12개 유지
  - `after-backup = true` — 백업 완료 후 자동으로 `forget`을 실행하여 보존 정책을 적용

---

## `documents` 프로필

`base`를 상속하며 `/srv/documents` 디렉터리를 백업합니다.

- **`inherit = "base"`**: `base` 프로필의 저장소, 패스워드, retention 설정을 모두 물려받습니다.
- **`[documents.backup]`**:
  - `source = ["/srv/documents"]` — 백업 대상 경로

---

## `photos` 프로필

`base`를 상속하며 `/srv/photos` 디렉터리를 백업합니다. `*.tmp` 파일은 제외합니다.

- **`inherit = "base"`**: `base` 프로필 설정을 물려받습니다.
- **`[photos.backup]`**:
  - `source = ["/srv/photos"]` — 백업 대상 경로
  - `exclude = ["*.tmp"]` — `.tmp` 확장자 파일 제외

> **주의**: `exclude`는 반드시 `[profile.backup]` 섹션 내부에 위치해야 합니다. 프로필 최상위 레벨에 두면 무시됩니다.

---

## 주요 명령어

```bash
# documents 백업 실행
resticprofile --name documents backup

# photos 백업 실행
resticprofile --name photos backup

# 유효 설정 확인 (상속 결과 확인)
resticprofile --name documents show
resticprofile --name photos show
```
