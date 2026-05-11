---
title: Toybox.Time
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Time.html
---

## Module: Toybox.Time

## Overview

The Time module provides functionality for dealing with times and dates.

There are two main concepts used by Monkey C when working with time: the [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) and [Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html). A Moment is a single point in time, while a Duration is a span of time. Moments and Durations can be used together for time calculations in the following ways:

```
Expression           Method               Result    Notes
---------------------------------------------------------------------------
Moment + Moment      -                    -         Invalid
Moment + Duration    Moment.add()         Moment    A later Moment
Moment - Moment      Moment.subtract()    Duration  The span between Moments
Moment - Duration    Moment.subtract()    Moment    An earlier Moment

Duration + Duration  Duration.add()       Duration  A longer Duration
Duration + Moment    Duration.add()       Moment    A later Moment
Duration - Duration  Duration.subtract()  Duration  A shorter Duration
Duration - Moment    -                    -         Invalid
```

Dates and times are generally represented in UTC time from the UNIX epoch, with the exception of the [Gregorian Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian.html#moment-instance_function), which are created relative to the current local time.

Date and time formatting in Monkey C is relatively open-ended, providing some formatting constants for short, medium, and long formatting (long and medium formatting are currently equivalent).

```
Constant          Seconds  Minutes  Hours  Day of Week  Day  Month  Year
---------------------------------------------------------------------------
FORMAT_SHORT   |  0        0        0      4            1    3      2017
FORMAT_MEDIUM  |  0        0        0      Wed          1    Mar    2017
FORMAT_LONG    |  0        0        0      Wed          1    Mar    2017
```

## See Also:

- [UTC Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)
- [UNIX Time](https://en.wikipedia.org/wiki/Unix_time)

## Modules Under Namespace

**Modules:** [Time.Gregorian](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian.html)

## Classes Under Namespace

**Classes:** [Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html), [LocalMoment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/LocalMoment.html), [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html), [RealTimeClockNotValidException](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/RealTimeClockNotValidException.html)

## Constant Summary

### DateFormat

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| FORMAT\_SHORT | 0 | API Level 1.0.0 | Short formatting is a numerical representation of date/time. |
| FORMAT\_MEDIUM | 1 | API Level 1.0.0 | Medium formatting is a mix of Numbers and Strings depending on which function is called. If formatted as a String, the result is an abbreviated form of the time or date. |
| FORMAT\_LONG | 2 | API Level 1.0.0 | Long formatting is a mix of Numbers and Strings depending on which function is called. If formatted as a String, the result is an abbreviated form of the time or date. |

### CurrentTime

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CURRENT\_TIME\_DEFAULT | 0 | API Level 3.0.10 | The default system clock, which may be user-modified. |
| CURRENT\_TIME\_GPS | 1 | API Level 3.0.10 | The clock time based on your current GPS location if a GPS signal is available. |
| CURRENT\_TIME\_RTC | 2 | API Level 3.0.10 | The system's real-time clock that cannot be overridden by user settings, and can only be updated by trusted sources such as GPS. |

## Instance Method Summary

- [**getCurrentTime**](#getCurrentTime-instance_function "getCurrentTime (Instance Function)") (options as {:currentTimeType as [Time.CurrentTime](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time.html#CurrentTime-module) }) as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html)
	Get a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) for the current time based on the specified source.
- [**now**](#now-instance_function "now (Instance Function)") () as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html)
	Get a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) for the current time.
- [**today**](#today-instance_function "today (Instance Function)") () as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html)
	Get a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) for midnight today.
