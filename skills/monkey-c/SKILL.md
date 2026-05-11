---
name: monkey-c
description: Garmin Connect IQ 플랫폼을 위한 Monkey C 언어 전문 스킬. Garmin 스마트워치·웨어러블 앱(Watch Face, Device App, Widget, Data Field 등)을 개발하거나, Monkey C 코드 작성·디버깅·리팩터링이 필요할 때 사용하세요.
---

# Monkey C 개발 가이드

> 참고: https://developer.garmin.com/connect-iq/monkey-c/

Monkey C는 Garmin이 Connect IQ 플랫폼용으로 만든 객체지향 언어입니다. Java·JavaScript·Python·Ruby의 문법을 혼합하여 설계되었으며, 동적 타이핑과 덕 타이핑을 지원합니다.

## 앱 타입

| 타입 | 설명 |
|------|------|
| **Watch Face** | 시계 화면 커스터마이징 |
| **Device App** | 디바이스 자원에 완전 접근하는 풀 앱 |
| **Widget** | 메인 캐러셀의 정보 카드 |
| **Data Field** | 활동 화면의 커스텀 측정 항목 표시 |
| **Audio Content Provider** | 서드파티 오디오 서비스 연동 |

## 언어 핵심 규칙

### 변수 & 상수
```monkey-c
var count = 0;          // 변수
const MAX = 100;        // 상수
```

### 클래스 & 상속
```monkey-c
using Toybox.Application as App;

class MyApp extends App.AppBase {
    function initialize() {
        AppBase.initialize();
    }

    function getInitialView() {
        return [new MyView(), new MyDelegate()];
    }
}
```

### 함수
```monkey-c
function add(a, b) {
    return a + b;
}
```

### 제어 구조
```monkey-c
// if/else
if (value > 0) {
    // ...
} else if (value == 0) {
    // ...
} else {
    // ...
}

// for
for (var i = 0; i < 10; i++) {
    // ...
}

// while
while (condition) {
    // ...
}

// switch
switch (value) {
    case 1:
        break;
    default:
        break;
}
```

### 모듈 임포트
```monkey-c
using Toybox.WatchUi as Ui;
using Toybox.Graphics as Gfx;
using Toybox.System as Sys;
using Toybox.Activity as Act;
```

## Toybox 표준 라이브러리 주요 모듈

| 모듈 | 용도 |
|------|------|
| `Toybox.Application` | 앱 생명주기 관리 |
| `Toybox.WatchUi` | UI 뷰·델리게이트·메뉴 |
| `Toybox.Graphics` | 그래픽 그리기 (drawText, drawLine 등) |
| `Toybox.System` | 시스템 정보, println 디버그 출력 |
| `Toybox.Activity` | 현재 활동 데이터 |
| `Toybox.ActivityMonitor` | 걸음 수, 칼로리 등 일상 활동 |
| `Toybox.Sensor` | 심박수, 고도, 기압 등 센서 |
| `Toybox.SensorHistory` | 센서 이력 데이터 |
| `Toybox.Communications` | BLE, HTTP 요청 |
| `Toybox.Ant` / `Toybox.AntPlus` | ANT+ 연결 |
| `Toybox.Time` | 날짜·시간 처리 |
| `Toybox.Position` | GPS 위치 정보 |
| `Toybox.Math` | 수학 함수 |
| `Toybox.Lang` | 기본 타입·컬렉션 |
| `Toybox.StringUtil` | 문자열 유틸리티 |
| `Toybox.Cryptography` | 암호화 |
| `Toybox.Timer` | 타이머 |

## Watch Face 기본 구조

```monkey-c
using Toybox.WatchUi as Ui;
using Toybox.Graphics as Gfx;
using Toybox.System as Sys;

class MyWatchFaceView extends Ui.WatchFace {
    function initialize() {
        WatchFace.initialize();
    }

    function onLayout(dc) {
        // 레이아웃 초기화
    }

    function onUpdate(dc) {
        // 화면 갱신 (매 초 또는 분마다 호출)
        var clockTime = Sys.getClockTime();
        var hour = clockTime.hour;
        var min = clockTime.min;

        dc.setColor(Gfx.COLOR_BLACK, Gfx.COLOR_BLACK);
        dc.clear();

        dc.setColor(Gfx.COLOR_WHITE, Gfx.COLOR_TRANSPARENT);
        dc.drawText(
            dc.getWidth() / 2,
            dc.getHeight() / 2,
            Gfx.FONT_LARGE,
            hour.format("%02d") + ":" + min.format("%02d"),
            Gfx.TEXT_JUSTIFY_CENTER | Gfx.TEXT_JUSTIFY_VCENTER
        );
    }
}
```

## 베스트 프랙티스

- **메모리 절약**: Garmin 기기는 RAM이 수십~수백 KB로 제한되어 있음. 큰 배열이나 불필요한 객체 생성을 피할 것.
- **배터리 효율**: `onUpdate()`에서 무거운 연산을 하지 말고 결과를 캐시할 것.
- **null 체크**: 동적 타이핑이므로 센서 데이터나 외부 값은 반드시 null 체크 후 사용.
- **퍼미션 선언**: Communications, Sensor 등 특수 기능은 `manifest.xml`에 퍼미션을 명시해야 함.
- **디버그 출력**: `Sys.println("msg")` 사용. 릴리즈 전 제거 권장.

## 개발 환경

- **VS Code**: 공식 Monkey C 확장 설치 (자동완성, 구문 강조, 실시간 오류, 코드 폴딩)
- **Connect IQ SDK**: Garmin Developer 포털에서 다운로드
- **시뮬레이터**: SDK에 포함된 기기 시뮬레이터로 실제 기기 없이 테스트 가능

## 참고 자료

- [Monkey C 언어 레퍼런스](https://developer.garmin.com/connect-iq/reference-guides/monkey-c-reference/)
- [Connect IQ 개요](https://developer.garmin.com/connect-iq/overview/)
- [API 문서 (Toybox)](https://developer.garmin.com/connect-iq/api-docs/)
