# resticprofile S3 백업 설정 설명

## 파일 구조

`profiles.toml` 파일은 resticprofile의 TOML 형식 설정 파일입니다.

---

## 주요 섹션 설명

### `[global]`
- `scheduler = "systemd"`: systemd를 스케줄러로 사용하도록 지정합니다.

### `[default]`
- `repository`: S3 버킷 경로를 지정합니다. restic의 S3 형식(`s3:<endpoint>/<bucket>`)을 따릅니다.
- `password-file`: restic 저장소 암호화 비밀번호 파일 경로입니다. 실제 경로로 변경해야 합니다.

### `[default.env]`
AWS 자격증명을 환경변수로 주입합니다. resticprofile의 템플릿 문법(`.Env.<VAR>`)을 사용하여 시스템 환경변수에서 값을 읽어옵니다.

- `AWS_ACCESS_KEY_ID`: AWS 액세스 키 ID
- `AWS_SECRET_ACCESS_KEY`: AWS 시크릿 액세스 키

실행 전에 셸 또는 systemd 서비스 환경에 해당 변수가 설정되어 있어야 합니다.

### `[default.backup]`
- `source`: 백업 대상 디렉토리 목록 (`/var/www`, `/etc`)
- `schedule`: systemd 달력 형식으로 매주 일요일 오전 3시를 지정합니다 (`Sun *-*-* 03:00:00`)
- `schedule-permission = "system"`: 시스템 권한(root)으로 systemd 유닛을 생성합니다
- `schedule-log`: 스케줄 실행 로그 파일 경로

### 훅(Hooks)

#### `run-after` (백업 성공 시)
백업이 성공적으로 완료된 후 healthchecks.io에 성공 신호를 보냅니다:
```
curl -fsS --retry 3 https://hc-ping.com/${HC_UUID}
```

#### `run-after-fail` (백업 실패 시)
백업이 실패했을 때 healthchecks.io에 실패 신호를 보냅니다:
```
curl -fsS --retry 3 https://hc-ping.com/${HC_UUID}/fail
```

`${HC_UUID}`는 healthchecks.io에서 발급받은 고유 UUID로, 환경변수로 설정하거나 직접 URL에 삽입해야 합니다.

---

## 사용 전 준비사항

1. **restic 저장소 비밀번호** 파일 생성:
   ```bash
   echo "your-strong-password" > /etc/resticprofile/password
   chmod 600 /etc/resticprofile/password
   ```

2. **AWS 자격증명 환경변수 설정** (systemd 서비스에서 사용할 경우):
   `/etc/resticprofile/environment` 파일을 만들고 systemd 서비스에 `EnvironmentFile=` 지시자로 연결하거나, systemd drop-in 파일로 설정합니다.

3. **healthchecks.io UUID 설정**:
   - [healthchecks.io](https://healthchecks.io)에서 체크를 생성하고 UUID를 확인합니다.
   - `${HC_UUID}` 부분을 실제 UUID로 교체하거나, 환경변수 `HC_UUID`를 설정합니다.

4. **로그 디렉토리 생성**:
   ```bash
   mkdir -p /var/log/resticprofile
   ```

5. **restic S3 저장소 초기화** (최초 1회):
   ```bash
   AWS_ACCESS_KEY_ID=<key> AWS_SECRET_ACCESS_KEY=<secret> \
     resticprofile backup --dry-run
   # 또는
   resticprofile -n default init
   ```

6. **systemd 유닛 설치**:
   ```bash
   resticprofile schedule --all
   systemctl daemon-reload
   systemctl enable --now resticprofile-backup@default.timer
   ```

---

## 스케줄 확인

```bash
systemctl list-timers | grep resticprofile
```
