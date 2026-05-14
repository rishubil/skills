---
title: Toybox.Time.Gregorian
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian.html
---

## Module: Toybox.Time.Gregorian

## Overview

## See Also:

- [The Gregorian Calendar](https://en.wikipedia.org/wiki/Gregorian_calendar)

## Classes Under Namespace

**Classes:** [Info](Gregorian/Info.md)

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | SECONDS\_PER\_DAY | 86400 | API Level 1.0.0 | The number of seconds in one day |
| Type | SECONDS\_PER\_HOUR | 3600 | API Level 1.0.0 | The number of seconds in one hour |
| Type | SECONDS\_PER\_MINUTE | 60 | API Level 1.0.0 | The number of seconds in one minute |
| Type | SECONDS\_PER\_YEAR | 31557600 | API Level 1.0.0 | The number of seconds in one year |

### DayOfWeek

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DAY\_SUNDAY | 1 | API Level 3.0.0 | Sunday |
| DAY\_MONDAY | 2 | API Level 3.0.0 | Monday |
| DAY\_TUESDAY | 3 | API Level 3.0.0 | Tuesday |
| DAY\_WEDNESDAY | 4 | API Level 3.0.0 | Wednesday |
| DAY\_THURSDAY | 5 | API Level 3.0.0 | Thursday |
| DAY\_FRIDAY | 6 | API Level 3.0.0 | Friday |
| DAY\_SATURDAY | 7 | API Level 3.0.0 | Saturday |

### Month

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MONTH\_JANUARY | 1 | API Level 3.0.0 | January |
| MONTH\_FEBRUARY | 2 | API Level 3.0.0 | February |
| MONTH\_MARCH | 3 | API Level 3.0.0 | March |
| MONTH\_APRIL | 4 | API Level 3.0.0 | April |
| MONTH\_MAY | 5 | API Level 3.0.0 | May |
| MONTH\_JUNE | 6 | API Level 3.0.0 | June |
| MONTH\_JULY | 7 | API Level 3.0.0 | July |
| MONTH\_AUGUST | 8 | API Level 3.0.0 | August |
| MONTH\_SEPTEMBER | 9 | API Level 3.0.0 | September |
| MONTH\_OCTOBER | 10 | API Level 3.0.0 | October |
| MONTH\_NOVEMBER | 11 | API Level 3.0.0 | November |
| MONTH\_DECEMBER | 12 | API Level 3.0.0 | December |

## Instance Method Summary

- [**duration**](#duration-instance_function "duration (Instance Function)") (options as {:years as [Lang.Number](../Lang/Number.md),:days as [Lang.Number](../Lang/Number.md),:hours as [Lang.Number](../Lang/Number.md),:minutes as [Lang.Number](../Lang/Number.md),:seconds as [Lang.Number](../Lang/Number.md) }) as [Time.Duration](Duration.md)
	Create a [Duration](Duration.md) from a Dictionary of options.
- [**info**](#info-instance_function "info (Instance Function)") (moment as [Time.Moment](Moment.md) or [Time.LocalMoment](LocalMoment.md), format as [Time.DateFormat](../Time.md#DateFormat-module)) as [Gregorian.Info](Gregorian/Info.md)
	Get [Info](Gregorian/Info.md) for a [Moment](Moment.md) in local time.
- [**localMoment**](#localMoment-instance_function "localMoment (Instance Function)") (location as [Position.Location](../Position/Location.md), moment as [Time.Moment](Moment.md)) as [Time.LocalMoment](LocalMoment.md) or **Null**
	Create a LocalMoment from a Moment and a Location.
- [**moment**](#moment-instance_function "moment (Instance Function)") (options as {:year as [Lang.Number](../Lang/Number.md),:month as [Lang.Number](../Lang/Number.md) or [Lang.Symbol](../Lang/Symbol.md),:day as [Lang.Number](../Lang/Number.md),:hour as [Lang.Number](../Lang/Number.md),:minute as [Lang.Number](../Lang/Number.md),:second as [Lang.Number](../Lang/Number.md) }) as [Time.Moment](Moment.md)
	Create a [Moment](Moment.md) from a Dictionary of options.
- [**utcInfo**](#utcInfo-instance_function "utcInfo (Instance Function)") (moment as [Time.Moment](Moment.md), format as [Time.DateFormat](../Time.md#DateFormat-module)) as [Gregorian.Info](Gregorian/Info.md)
	Get [Info](Gregorian/Info.md) for a [Moment](Moment.md) in UTC time.

## Instance Method Details

### duration(options as {:years as Lang.Number,:days as Lang.Number,:hours as Lang.Number,:minutes as Lang.Number,:seconds as Lang.Number }) as Time.Duration

### info(moment as Time.Moment or Time.LocalMoment, format as Time.DateFormat) as Gregorian.Info

### localMoment(location as Position.Location, moment as Time.Moment) as Time.LocalMoment or Null

### moment(options as {:year as Lang.Number,:month as Lang.Number or Lang.Symbol,:day as Lang.Number,:hour as Lang.Number,:minute as Lang.Number,:second as Lang.Number }) as Time.Moment

Create a [Moment](Moment.md) from a Dictionary of options.

```
Each option value is assumed to be in the UTC time zone.
```

Unlike [Moment.initialize()](Moment.md#initialize-instance_function), which is based on the UNIX epoch, a Moment created with Gregorian.moment() is based on [today()](../Time.md#today-instance_function). The result is determined by taking the result of [today()](../Time.md#today-instance_function) and overlaying the options provided.

### utcInfo(moment as Time.Moment, format as Time.DateFormat) as Gregorian.Info

Get [Info](Gregorian/Info.md) for a [Moment](Moment.md) in UTC time.

```
Info
```
