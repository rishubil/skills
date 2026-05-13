# profiles.toml 설명

## 구성 개요

이 설정 파일은 resticprofile을 사용하여 `/var/www`와 `/etc` 디렉터리를 AWS S3 버킷(`s3:s3.amazonaws.com/mycompany-backup`)에 매주 일요일 오전 3시에 백업합니다.

## 주요 설정 항목

### 저장소 및 인증

- **repository**: `s3:s3.amazonaws.com/mycompany-backup` — AWS S3를 restic 저장소로 사용합니다.
- **password-file**: `/etc/resticprofile/password` — restic 저장소 암호화 비밀번호 파일 경로입니다. 이 파일을 미리 생성해야 합니다.
- **initialize = true**: 저장소가 없으면 자동으로 초기화합니다.

### AWS 자격증명 (환경변수)

`[mycompany.env]` 섹션에서 환경변수를 참조합니다:

```toml
[mycompany.env]
  AWS_ACCESS_KEY_ID = "${AWS_ACCESS_KEY_ID}"
  AWS_SECRET_ACCESS_KEY = "${AWS_SECRET_ACCESS_KEY}"
```

실행 전 다음과 같이 환경변수를 설정해야 합니다:

```bash
export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
```

또는 systemd 서비스 override 파일(`/etc/systemd/system/resticprofile-backup@mycompany.service.d/override.conf`)에서 설정할 수 있습니다:

```ini
[Service]
Environment="AWS_ACCESS_KEY_ID=your-access-key-id"
Environment="AWS_SECRET_ACCESS_KEY=your-secret-access-key"
```

### 백업 스케줄

```toml
schedule = "Sun *-*-* 03:00:00"
schedule-permission = "system"
```

- `Sun *-*-* 03:00:00`: 매주 일요일 오전 3시 (systemd OnCalendar 형식)
- `schedule-permission = "system"`: systemd 시스템 서비스로 등록 (root 권한 필요)
- `schedule-after-network-online = true`: 네트워크 연결 후 실행 보장
- `schedule-lock-wait = "30m"`: 락 대기 최대 30분

### healthchecks.io 알림 훅

```toml
run-after = [
  "curl -fsS -m 10 --retry 3 'https://hc-ping.com/YOUR-UUID-HERE'"
]
run-after-fail = [
  "curl -fsS -m 10 --retry 3 'https://hc-ping.com/YOUR-UUID-HERE/fail'"
]
```

- **run-after**: 백업 성공 시 healthchecks.io에 성공 ping을 보냅니다.
- **run-after-fail**: 백업 실패 시 `/fail` 엔드포인트로 실패를 알립니다.
- `YOUR-UUID-HERE`를 실제 healthchecks.io 체크 UUID로 교체해야 합니다.

### 보존 정책 (retention)

- 일별 7개, 주별 8개, 월별 12개, 연별 2개 스냅샷 보관
- `after-backup = true`: 백업 직후 자동으로 forget 실행

## systemd 스케줄 등록 방법

```bash
# root 권한으로 실행
resticprofile --name mycompany schedule

# 상태 확인
resticprofile --name mycompany status

# 수동 실행 테스트
resticprofile --name mycompany backup
```

## 사전 준비 사항

1. resticprofile 및 restic 설치
2. 비밀번호 파일 생성: `echo "your-strong-password" > /etc/resticprofile/password && chmod 600 /etc/resticprofile/password`
3. `YOUR-UUID-HERE`를 실제 healthchecks.io UUID로 교체
4. AWS 자격증명 설정 (환경변수 또는 systemd override)
5. `resticprofile --name mycompany init`으로 저장소 초기화 (또는 `initialize = true`가 자동 처리)
