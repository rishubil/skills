# resticprofile 설정 설명

## 구조 개요

TOML 형식으로 작성된 resticprofile 설정 파일로, `base`, `documents`, `photos` 세 개의 프로필로 구성됩니다.

---

## base 프로필

```toml
[base]
  repository = "/mnt/nas/backup"
  password-file = "/root/.restic-password"

  [base.retention]
    keep-daily = 7
    keep-weekly = 4
    keep-monthly = 12
    after-backup = true
```

- **repository**: 백업이 저장될 공통 저장소 경로 (`/mnt/nas/backup`)
- **password-file**: restic 저장소 암호화에 사용할 패스워드 파일 경로 (`/root/.restic-password`)
- **retention**: 보존 정책
  - `keep-daily = 7`: 최근 7일간의 백업 보존
  - `keep-weekly = 4`: 최근 4주간의 주간 백업 보존
  - `keep-monthly = 12`: 최근 12개월간의 월간 백업 보존
  - `after-backup = true`: 백업 완료 후 자동으로 forget(정리) 실행

---

## documents 프로필

```toml
[documents]
  inherit = "base"

  [documents.backup]
    source = ["/srv/documents"]
```

- **inherit = "base"**: `base` 프로필의 모든 설정(저장소, 패스워드, retention)을 상속
- **source**: `/srv/documents` 디렉터리를 백업 소스로 지정

---

## photos 프로필

```toml
[photos]
  inherit = "base"

  [photos.backup]
    source = ["/srv/photos"]
    exclude = ["*.tmp"]
```

- **inherit = "base"**: `base` 프로필의 모든 설정을 상속
- **source**: `/srv/photos` 디렉터리를 백업 소스로 지정
- **exclude**: `*.tmp` 패턴에 해당하는 임시 파일은 백업에서 제외

---

## 사용 방법

```bash
# documents 프로필로 백업 실행
resticprofile -n documents backup

# photos 프로필로 백업 실행
resticprofile -n photos backup

# 각 프로필의 retention 정책 수동 실행
resticprofile -n documents forget
resticprofile -n photos forget
```

`after-backup = true` 설정으로 인해 백업 시 retention 정리가 자동으로 수행됩니다.
