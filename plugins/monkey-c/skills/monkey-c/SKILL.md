---
name: monkey-c
description: Specialist skill for Monkey C on the Garmin Connect IQ platform. Use when developing Garmin smartwatch or wearable apps (Watch Face, Device App, Widget, Data Field, etc.) or when writing, debugging, or refactoring Monkey C code.
---

# Monkey C Development Guide

> Reference: https://developer.garmin.com/connect-iq/monkey-c/

Monkey C is an object-oriented language created by Garmin for the Connect IQ platform. It blends syntax from Java, JavaScript, Python, and Ruby, and supports dynamic typing and duck typing.

## App Types

| Type | Description |
|------|-------------|
| **Watch Face** | Customize the watch display |
| **Device App** | Full app with complete access to device resources |
| **Widget** | Information card in the main carousel |
| **Data Field** | Custom metric display on the activity screen |
| **Audio Content Provider** | Integration with third-party audio services |

## Core Language Rules

### Variables & Constants
```monkey-c
var count = 0;          // variable
const MAX = 100;        // constant
```

### Classes & Inheritance
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

### Functions
```monkey-c
function add(a, b) {
    return a + b;
}
```

### Control Structures
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

### Module Imports
```monkey-c
using Toybox.WatchUi as Ui;
using Toybox.Graphics as Gfx;
using Toybox.System as Sys;
using Toybox.Activity as Act;
```

## Key Toybox Standard Library Modules

| Module | Purpose |
|--------|---------|
| `Toybox.Application` | App lifecycle management |
| `Toybox.WatchUi` | UI views, delegates, and menus |
| `Toybox.Graphics` | Drawing graphics (drawText, drawLine, etc.) |
| `Toybox.System` | System info, println debug output |
| `Toybox.Activity` | Current activity data |
| `Toybox.ActivityMonitor` | Daily activity: steps, calories, etc. |
| `Toybox.Sensor` | Sensors: heart rate, altitude, barometer, etc. |
| `Toybox.SensorHistory` | Historical sensor data |
| `Toybox.Communications` | BLE, HTTP requests |
| `Toybox.Ant` / `Toybox.AntPlus` | ANT+ connectivity |
| `Toybox.Time` | Date and time handling |
| `Toybox.Position` | GPS location |
| `Toybox.Math` | Math functions |
| `Toybox.Lang` | Basic types and collections |
| `Toybox.StringUtil` | String utilities |
| `Toybox.Cryptography` | Cryptography |
| `Toybox.Timer` | Timers |

## Watch Face Basic Structure

```monkey-c
using Toybox.WatchUi as Ui;
using Toybox.Graphics as Gfx;
using Toybox.System as Sys;

class MyWatchFaceView extends Ui.WatchFace {
    function initialize() {
        WatchFace.initialize();
    }

    function onLayout(dc) {
        // initialize layout
    }

    function onUpdate(dc) {
        // screen refresh (called every second or minute)
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

## Best Practices

- **Conserve memory**: Garmin devices have limited RAM (tens to hundreds of KB). Avoid large arrays and unnecessary object creation.
- **Battery efficiency**: Don't perform heavy computation in `onUpdate()` — cache results instead.
- **Null checks**: Due to dynamic typing, always null-check sensor data and external values before use.
- **Declare permissions**: Special features like Communications and Sensor must be declared in `manifest.xml`.
- **Debug output**: Use `Sys.println("msg")`. Remove before releasing.

## Development Environment

- **VS Code**: Install the official Monkey C extension (autocomplete, syntax highlighting, real-time errors, code folding)
- **Connect IQ SDK**: Download from the Garmin Developer portal
- **Simulator**: The SDK includes a device simulator for testing without a physical device

## Local Documentation (use first)

This skill directory contains official documentation saved as local markdown files. When writing code or looking up APIs, **always consult the local docs below first**. Do not open external URLs or guess — Read the local files for accurate information.

### overview/ — Monkey C Language Guide

| File | Contents |
|------|----------|
| [overview/monkey-c.md](overview/monkey-c.md) | Basic syntax overview |
| [overview/monkey-types.md](overview/monkey-types.md) | Data types in detail |
| [overview/objects-and-memory.md](overview/objects-and-memory.md) | Object and memory model |
| [overview/functions.md](overview/functions.md) | Defining and calling functions |
| [overview/containers.md](overview/containers.md) | Array and Dictionary |
| [overview/exceptions-and-errors.md](overview/exceptions-and-errors.md) | Exception handling |
| [overview/annotations.md](overview/annotations.md) | Annotations |
| [overview/compiler-options.md](overview/compiler-options.md) | Compiler options |
| [overview/coding-conventions.md](overview/coding-conventions.md) | Coding conventions |

### references/ — Reference Guides

| File | Contents |
|------|----------|
| [references/monkey-c-reference.md](references/monkey-c-reference.md) | Full Monkey C language reference |
| [references/jungle-reference.md](references/jungle-reference.md) | Jungle build configuration language |
| [references/monkey-c-command-line-setup.md](references/monkey-c-command-line-setup.md) | CLI build and simulator |
| [references/visual-studio-code-extension.md](references/visual-studio-code-extension.md) | VS Code extension usage |
| [references/monkey-motion-reference.md](references/monkey-motion-reference.md) | Animation conversion tool |
| [references/monkey-graph-reference.md](references/monkey-graph-reference.md) | FIT data visualization tool |

### api-docs/ — Toybox API Reference (330 files)

Structured as `api-docs/Toybox/<Module>.md` or `api-docs/Toybox/<Module>/<Class>.md`.
When looking up a specific class or method, Read the file at the corresponding path directly.

Key entry points:
- [api-docs/index.md](api-docs/index.md) — Full Toybox namespace listing
- [api-docs/class_list.md](api-docs/class_list.md) — Class and module index
- [api-docs/method_list.md](api-docs/method_list.md) — Full method listing

Commonly used modules:
- `api-docs/Toybox/WatchUi.md`, `api-docs/Toybox/WatchUi/View.md`
- `api-docs/Toybox/Graphics.md`, `api-docs/Toybox/Graphics/Dc.md`
- `api-docs/Toybox/Application/AppBase.md`
- `api-docs/Toybox/System.md`, `api-docs/Toybox/Sensor.md`
