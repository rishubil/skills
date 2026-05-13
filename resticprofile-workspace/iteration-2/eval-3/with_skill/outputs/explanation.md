# resticprofile S3 백업 설정 설명

## 구성 개요

`profiles.toml`은 AWS S3 버킷(`s3:s3.amazonaws.com/mycompany-backup`)을 저장소로 사용하는 단일 프로파일 `mycompany-backup`을 정의합니다.

---

## 섹션별 설명

### `[global]`

resticprofile 전체에 적용되는 설정입니다.

- `priority = "low"` — 백업 프로세스가 다른 작업에 영향을 주지 않도록 낮은 우선순위로 실행합니다.
- `ionice = true` — I/O 우선순위도 낮게 설정합니다.

---

### `["mycompany-backup"]` (프로파일 루트)

- `repository` — restic이 스냅샷을 저장할 S3 경로입니다.
- `password-file` — 리포지토리 암호화 키가 저장된 파일 경로입니다. 이 파일을 사전에 생성해 두어야 합니다 (예: `openssl rand -base64 32 > /etc/restic/password`).
- `initialize = true` — 리포지토리가 아직 초기화되지 않은 경우 첫 실행 시 자동으로 `restic init`을 수행합니다.

---

### `["mycompany-backup".env]` (환경변수)

AWS 자격증명을 환경변수에서 읽어 restic에 전달합니다.

```toml
AWS_ACCESS_KEY_ID     = "{{ .Env.AWS_ACCESS_KEY_ID }}"
AWS_SECRET_ACCESS_KEY = "{{ .Env.AWS_SECRET_ACCESS_KEY }}"
```

**중요:** resticprofile의 `env` 섹션은 Go 템플릿 문법(`{{ .Env.VAR }}`)을 사용합니다. 셸 문법(`${VAR}`)은 동작하지 않습니다.

실제 자격증명은 resticprofile 프로세스가 실행되는 환경에 설정되어 있어야 합니다. systemd를 사용하는 경우 `EnvironmentFile` 지시문으로 별도 파일에서 불러올 수 있습니다.

예시 (`/etc/resticprofile/aws-credentials`):
```
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
```

systemd 서비스 파일에 다음 줄을 추가합니다:
```ini
EnvironmentFile=/etc/resticprofile/aws-credentials
```

resticprofile이 자동 생성하는 systemd 유닛 파일을 수정하거나, `/etc/systemd/system/resticprofile-mycompany-backup@backup.service.d/override.conf`를 드롭인으로 추가하면 됩니다.

---

### `["mycompany-backup".backup]` (백업 설정)

- `source` — 백업할 경로 목록: `/var/www`와 `/etc`.
- `schedule = "Sun *-*-* 03:00:00"` — 매주 일요일 오전 3시에 실행 (systemd OnCalendar 형식).
- `schedule-permission = "system"` — systemd **시스템** 유닛으로 등록합니다. `resticprofile schedule`을 **root**로 실행해야 합니다.
- `schedule-lock-wait = "30m"` — 이미 백업이 실행 중인 경우 최대 30분 대기 후 시작합니다.

#### healthchecks.io 훅

`<YOUR-UUID>` 자리에 healthchecks.io에서 발급받은 실제 Check UUID를 입력하세요.

| 훅 | 시점 | 역할 |
|---|---|---|
| `run-before` | 백업 시작 전 | `…/start` 엔드포인트로 "시작" 신호 전송 |
| `run-after` | 백업 성공 후 | 기본 엔드포인트로 "완료(성공)" 신호 전송 |
| `run-after-fail` | 백업 실패 시 | `…/fail` 엔드포인트로 "실패" 신호 전송 |

---

### `["mycompany-backup".retention]` (보존 정책)

- `after-backup = true` — 매 백업 직후 `restic forget`을 자동 실행합니다. 별도의 scheduled forget이 필요 없습니다.
- 보존 정책: 주간 8개, 월간 12개, 연간 3개.

---

### `["mycompany-backup".check]` (정합성 검사)

- `schedule = "monthly"` — 매월 리포지토리 정합성 검사를 수행합니다.

---

## systemd 스케줄 등록 방법

설정 완료 후 root 권한으로 다음 명령을 실행합니다:

```bash
# 스케줄 등록 (systemd 유닛 파일 생성 및 활성화)
resticprofile --name mycompany-backup schedule

# 등록된 스케줄 상태 확인
resticprofile --name mycompany-backup status

# systemd 유닛 상태 직접 확인
systemctl status resticprofile-mycompany-backup@backup.timer
```

스케줄을 제거하려면:
```bash
resticprofile --name mycompany-backup unschedule
```

---

## 초기 설정 체크리스트

1. `/etc/restic/password` 파일 생성 (리포지토리 암호)
2. AWS 자격증명을 환경변수 또는 EnvironmentFile로 준비
3. `resticprofile --name mycompany-backup init` 으로 리포지토리 초기화 (또는 `initialize = true`로 자동 처리)
4. healthchecks.io에서 Check를 생성하고 UUID를 profiles.toml의 `<YOUR-UUID>` 위치에 입력
5. `resticprofile --name mycompany-backup schedule` 으로 systemd 타이머 등록
