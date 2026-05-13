# resticprofile 홈 디렉토리 백업 설정 설명

## 파일 구조

`profiles.toml`은 resticprofile v1 형식으로 작성되었으며, `default` 프로파일 하나를 정의합니다.

## 주요 설정

| 항목 | 값 | 설명 |
|------|-----|------|
| `repository` | `/mnt/backup/home` | 백업이 저장될 restic 저장소 경로 |
| `password-file` | `/etc/restic/password` | 저장소 암호화 패스워드 파일 |
| `initialize` | `true` | 저장소가 없으면 자동으로 초기화 |

## backup 섹션

- **source**: `~/` — 현재 사용자의 홈 디렉토리 전체를 백업
- **exclude**: `.cache`와 `node_modules` 디렉토리를 모든 하위 경로에서 제외(`**` 글로브 패턴 사용)
- **schedule**: `02:00` — 매일 새벽 2시에 백업 실행
- **schedule-permission**: `system` — systemd 타이머로 등록(루트 권한 필요)

## forget 섹션

- **keep-daily**: `7` — 최근 7일치 일별 스냅샷 유지
- **keep-weekly**: `4` — 최근 4주치 주별 스냅샷 유지
- **prune**: `true` — forget 실행 시 불필요한 데이터도 함께 정리
- **schedule**: `02:30` — 백업 직후인 새벽 2시 30분에 정리 실행

## 사용 방법

```bash
# 스케줄 등록 (systemd 타이머 생성)
resticprofile schedule --all

# 즉시 백업 실행 (테스트)
resticprofile backup

# 즉시 forget/prune 실행 (테스트)
resticprofile forget
```

## 주의 사항

- `schedule-permission = "system"`을 사용하면 systemd 시스템 타이머로 등록되어 루트 권한이 필요합니다. 사용자 단위 타이머를 원하면 `"user"`로 변경하세요.
- `/etc/restic/password` 파일은 사전에 생성되어 있어야 하며, 읽기 권한이 적절히 설정되어야 합니다.
- 저장소 첫 사용 시 `resticprofile init`으로 초기화하거나, `initialize = true` 설정으로 자동 초기화할 수 있습니다.
