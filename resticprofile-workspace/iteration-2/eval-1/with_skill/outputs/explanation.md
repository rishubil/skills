# resticprofile 홈 디렉토리 백업 설정 설명

## 생성된 파일: `profiles.toml`

### 전체 구조

```
[global]           → resticprofile 전역 설정
["home-backup"]    → 홈 디렉토리 백업 프로파일
  [home-backup.backup]      → 백업 대상 및 스케줄
  [home-backup.retention]   → 보존 정책
```

---

### 각 섹션 설명

#### `[global]`

```toml
priority = "low"
```

resticprofile 프로세스를 낮은 우선순위로 실행하여 시스템 리소스에 미치는 영향을 최소화합니다.

---

#### `["home-backup"]` (프로파일 루트)

```toml
repository    = "/mnt/backup/home"
password-file = "/etc/restic/password"
initialize    = true
```

- **`repository`**: 백업 데이터를 저장할 restic 저장소 경로입니다.
- **`password-file`**: 저장소 암호화 키가 담긴 파일 경로입니다.
- **`initialize = true`**: 저장소가 아직 초기화되지 않았을 경우 자동으로 `restic init`을 실행합니다. 처음 설정 시 별도로 초기화 명령을 실행할 필요가 없습니다.

---

#### `[home-backup.backup]` (백업 설정)

```toml
source  = ["/home"]
exclude = ["**/.cache", "**/node_modules"]
schedule            = "*-*-* 02:00:00"
schedule-permission = "system"
```

- **`source`**: `/home` 전체를 백업 대상으로 지정합니다.
- **`exclude`**: 백업에서 제외할 패턴입니다.
  - `**/.cache` — 모든 경로의 `.cache` 폴더 제외
  - `**/node_modules` — 모든 경로의 `node_modules` 폴더 제외
  - `**` 패턴은 중첩된 경로에도 적용됩니다.
- **`schedule = "*-*-* 02:00:00"`**: systemd OnCalendar 표현식으로 매일 새벽 2시에 실행합니다.
- **`schedule-permission = "system"`**: 시스템 스케줄러(systemd system timer)로 등록합니다. `resticprofile schedule` 명령을 루트 권한으로 실행해야 합니다.

> **주의**: `exclude`는 반드시 `[home-backup.backup]` 안에 위치해야 합니다. 프로파일 루트(`["home-backup"]`)에 놓으면 무시됩니다.

---

#### `[home-backup.retention]` (보존 정책)

```toml
keep-daily   = 7
keep-weekly  = 4
after-backup = true
```

- **`keep-daily = 7`**: 최근 7일 동안의 일별 스냅샷을 유지합니다.
- **`keep-weekly = 4`**: 최근 4주 동안의 주별 스냅샷을 유지합니다.
- **`after-backup = true`**: 백업이 완료된 직후 자동으로 `restic forget`을 실행하여 보존 정책에 맞지 않는 오래된 스냅샷을 정리합니다. 별도의 forget 스케줄을 설정할 필요가 없습니다.

---

## 사용 방법

### 1. 스케줄 등록 (최초 1회, 루트 권한 필요)

```bash
sudo resticprofile --name home-backup schedule
```

### 2. 스케줄 상태 확인

```bash
sudo resticprofile --name home-backup status
```

### 3. 즉시 수동 백업 실행

```bash
sudo resticprofile --name home-backup backup
```

### 4. 스냅샷 목록 확인

```bash
sudo resticprofile --name home-backup snapshots
```

### 5. 설정 확인

```bash
resticprofile --name home-backup show
```

### 6. 스케줄 해제

```bash
sudo resticprofile --name home-backup unschedule
```

---

## 보존 정책 동작 예시

`after-backup = true`로 설정되어 있으므로 매일 새벽 2시 백업 후 다음 규칙이 적용됩니다:

| 보존 규칙 | 설정값 | 설명 |
|-----------|--------|------|
| `keep-daily` | 7 | 오늘부터 최근 7일간의 일별 최신 스냅샷 유지 |
| `keep-weekly` | 4 | 최근 4주간의 주별 대표 스냅샷 유지 |
| 그 외 | — | 위 규칙에 해당하지 않는 오래된 스냅샷은 삭제 |

> 실제 데이터 삭제(prune)는 `restic forget --prune` 또는 별도 `resticprofile prune` 실행이 필요합니다. `after-backup`은 `forget`만 실행하며, `prune`은 필요 시 별도로 예약하거나 수동 실행합니다.
