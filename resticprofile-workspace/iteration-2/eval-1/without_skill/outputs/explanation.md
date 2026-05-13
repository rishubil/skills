# resticprofile 홈 디렉토리 백업 설정 설명

## 파일 구조

`profiles.toml` 파일은 resticprofile의 설정 파일로, TOML 형식으로 작성되었습니다.

## 주요 설정 항목

### `[default]` 프로파일

- **`repository`**: 백업 저장소 경로를 `/mnt/backup/home`으로 지정합니다.
- **`password-file`**: 저장소 암호화에 사용할 패스워드 파일 경로를 `/etc/restic/password`로 지정합니다.
- **`initialize = true`**: 저장소가 없을 경우 자동으로 초기화합니다.

### `[default.backup]` 섹션

- **`source`**: 백업 대상을 홈 디렉토리(`~/`)로 지정합니다.
- **`exclude`**: 백업에서 제외할 경로를 지정합니다.
  - `~/.cache`: 홈 디렉토리의 `.cache` 폴더 제외
  - `**/node_modules`: 모든 경로의 `node_modules` 폴더 제외
- **`schedule`**: 매일 새벽 2시(`02:00`)에 자동 백업을 실행합니다.
- **`schedule-permission`**: 시스템 레벨(root)로 스케줄을 등록합니다.
- **`schedule-log`**: 백업 로그를 `/var/log/resticprofile-backup.log`에 기록합니다.

### `[default.forget]` 섹션

- **`keep-daily = 7`**: 최근 7일치 일별 백업을 유지합니다.
- **`keep-weekly = 4`**: 최근 4주치 주별 백업을 유지합니다.
- **`prune = true`**: forget 실행 시 실제로 사용하지 않는 데이터도 정리(prune)합니다.
- **`schedule`**: 매일 새벽 2시 30분(`02:30`)에 자동으로 오래된 백업을 정리합니다.
- **`schedule-log`**: forget 로그를 `/var/log/resticprofile-forget.log`에 기록합니다.

## 사용 방법

### 스케줄 등록

```bash
# 백업 스케줄 등록
sudo resticprofile schedule --all

# 또는 개별 등록
sudo resticprofile backup.schedule
sudo resticprofile forget.schedule
```

### 수동 실행

```bash
# 즉시 백업 실행
resticprofile backup

# 즉시 정리 실행
resticprofile forget
```

### 스케줄 상태 확인

```bash
resticprofile status
```

## 주의 사항

- 패스워드 파일(`/etc/restic/password`)은 미리 생성되어 있어야 합니다.
- `schedule-permission = "system"`은 systemd 또는 launchd를 통해 root 권한으로 스케줄을 등록합니다. 홈 디렉토리 전체를 백업할 때 권한 문제가 없도록 하기 위함입니다.
- 저장소가 없는 경우 `initialize = true` 설정 덕분에 첫 실행 시 자동으로 초기화됩니다.
- forget과 backup 스케줄을 30분 간격으로 분리하여 backup이 완료된 후 forget이 실행되도록 했습니다.
