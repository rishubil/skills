# resticprofile 홈 디렉토리 백업 설정 설명

## 구성 개요

`profiles.toml` 파일은 resticprofile을 사용하여 홈 디렉토리를 자동 백업하는 설정입니다.

## 주요 설정 항목

### `[global]`
- `priority = "low"` — 백업 프로세스가 시스템 작업을 방해하지 않도록 낮은 우선순위로 실행합니다.

### `["home-backup"]` (프로파일)
- `repository = "/mnt/backup/home"` — 백업 저장소 경로
- `password-file = "/etc/restic/password"` — 저장소 암호화에 사용할 패스워드 파일 경로
- `initialize = true` — 저장소가 존재하지 않으면 자동으로 초기화합니다.

### `[home-backup.backup]`
- `source = ["/home"]` — `/home` 디렉토리 전체를 백업 대상으로 지정
- `exclude = ["**/.cache", "**/node_modules"]` — `.cache` 폴더와 `node_modules` 디렉토리를 백업에서 제외
- `schedule = "*-*-* 02:00:00"` — 매일 새벽 2시에 자동 백업 실행 (systemd 캘린더 표현식)
- `schedule-permission = "system"` — 시스템 권한으로 실행 (root로 `resticprofile schedule` 필요)
- `schedule-lock-mode = "default"` — 잠금이 걸려 있을 경우 대기 후 실패 처리
- `schedule-lock-wait = "30m"` — 잠금 대기 최대 시간 30분

### `[home-backup.retention]`
- `keep-daily = 7` — 최근 7일치 일별 스냅샷 보존
- `keep-weekly = 4` — 최근 4주치 주별 스냅샷 보존
- `after-backup = true` — 백업 완료 후 자동으로 보존 정책 적용 (나머지 스냅샷 삭제)
- `prune = true` — forget 실행 후 unreferenced 데이터를 자동으로 정리(prune)

## 스케줄 등록 방법

설정 완료 후 root 권한으로 아래 명령어를 실행하여 systemd 타이머를 등록합니다:

```bash
sudo resticprofile --name home-backup schedule
```

등록된 스케줄 상태 확인:

```bash
sudo resticprofile --name home-backup status
```

저장소 초기화 (최초 1회):

```bash
sudo resticprofile --name home-backup init
```
