# profiles.toml 설명

## 구성 개요

이 설정 파일은 resticprofile의 프로필 상속 기능을 활용하여 세 개의 프로필로 구성됩니다.

## base 프로필

공통 설정을 담는 기본 프로필입니다:
- **repository**: `/mnt/nas/backup` — 모든 백업이 저장될 NAS 경로
- **password-file**: `/root/.restic-password` — 저장소 암호화 키 파일
- **retention** 정책:
  - `keep-daily = 7` — 최근 7일치 일별 스냅샷 보존
  - `keep-weekly = 4` — 최근 4주치 주별 스냅샷 보존
  - `keep-monthly = 12` — 최근 12개월치 월별 스냅샷 보존
  - `after-backup = true` — 백업 완료 후 자동으로 forget(정리) 실행

## documents 프로필

`inherit = "base"`로 base의 모든 설정을 상속받습니다:
- **backup.source**: `/srv/documents` — 백업할 소스 경로

## photos 프로필

`inherit = "base"`로 base의 모든 설정을 상속받습니다:
- **backup.source**: `/srv/photos` — 백업할 소스 경로
- **backup.exclude**: `["*.tmp"]` — `.tmp` 확장자 파일 제외

## 사용법

```bash
# documents 백업 실행
resticprofile --name documents backup

# photos 백업 실행
resticprofile --name photos backup

# 저장소 초기화 (최초 1회)
resticprofile --name documents init
resticprofile --name photos init

# 효과적인 설정 확인
resticprofile --name documents show
resticprofile --name photos show
```
