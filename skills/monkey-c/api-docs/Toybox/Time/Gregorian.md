---
title: Toybox.Time.Gregorian
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian.html
---

## Module: Toybox.Time.Gregorian

## Overview

## See Also:

- [The Gregorian Calendar](https://en.wikipedia.org/wiki/Gregorian_calendar)

## Classes Under Namespace

**Classes:** [Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian/Info.html)

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

- [**duration**](#duration-instance_function "duration (Instance Function)") (options as {:years as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:days as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:hours as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:minutes as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:seconds as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) }) as [Time.Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html)
	Create a [Duration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Duration.html) from a Dictionary of options.
- [**info**](#info-instance_function "info (Instance Function)") (moment as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) or [Time.LocalMoment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/LocalMoment.html), format as [Time.DateFormat](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time.html#DateFormat-module)) as [Gregorian.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian/Info.html)
	Get [Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian/Info.html) for a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) in local time.
- [**localMoment**](#localMoment-instance_function "localMoment (Instance Function)") (location as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html), moment as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html)) as [Time.LocalMoment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/LocalMoment.html) or **Null**
	Create a LocalMoment from a Moment and a Location.
- [**moment**](#moment-instance_function "moment (Instance Function)") (options as {:year as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:month as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Symbol](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Symbol.html),:day as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:hour as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:minute as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html),:second as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) }) as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html)
	Create a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) from a Dictionary of options.
- [**utcInfo**](#utcInfo-instance_function "utcInfo (Instance Function)") (moment as [Time.Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html), format as [Time.DateFormat](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time.html#DateFormat-module)) as [Gregorian.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian/Info.html)
	Get [Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian/Info.html) for a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) in UTC time.

## Instance Method Details

### duration(options as {:years as Lang.Number,:days as Lang.Number,:hours as Lang.Number,:minutes as Lang.Number,:seconds as Lang.Number }) as Time.Duration

### info(moment as Time.Moment or Time.LocalMoment, format as Time.DateFormat) as Gregorian.Info

### localMoment(location as Position.Location, moment as Time.Moment) as Time.LocalMoment or Null

### moment(options as {:year as Lang.Number,:month as Lang.Number or Lang.Symbol,:day as Lang.Number,:hour as Lang.Number,:minute as Lang.Number,:second as Lang.Number }) as Time.Moment

Create a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) from a Dictionary of options.

```
Each option value is assumed to be in the UTC time zone.
```

Unlike [Moment.initialize()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html#initialize-instance_function), which is based on the UNIX epoch, a Moment created with Gregorian.moment() is based on [today()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time.html#today-instance_function). The result is determined by taking the result of [today()](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time.html#today-instance_function) and overlaying the options provided.

### utcInfo(moment as Time.Moment, format as Time.DateFormat) as Gregorian.Info

Get [Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Gregorian/Info.html) for a [Moment](https://developer.garmin.com/connect-iq/api-docs/Toybox/Time/Moment.html) in UTC time.

```
Info
```
