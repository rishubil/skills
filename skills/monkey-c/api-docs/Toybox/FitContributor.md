---
title: Toybox.FitContributor
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor.html
---

## Module: Toybox.FitContributor

## Overview

The FitContributor module allows Applications and Data Fields to record [Field](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html) data into FIT files on the device's file system during an activity. This is useful for recording data that is not already calculated by the device, which can be synced to a service like Garmin Connect.

There are three FitContributor message types available:

MESG\_TYPE\_SESSION

Session data is written once per recording session at the end of the recording, and is used for data that pertains to the entire session (e.g. average speed).

MESG\_TYPE\_LAP

Lap data is written once for every lap in the session, and used for data that pertains to each lap (e.g. average lap speed).

MESG\_TYPE\_RECORD

Depending on the device, record data is written once per second or when new data is available (Smart Recording), but is never written faster than once per second. This message type is used for instantaneous values (e.g. current speed).

Data type constants are also available for use with the [createField()](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording/Session.html#createField-instance_function) method.

## See Also:

- [Session.createField()](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityRecording/Session.html#createField-instance_function)
- [Learn more about the FIT format](http://www.thisisant.com/resources/fit)

## Classes Under Namespace

**Classes:** [Field](https://developer.garmin.com/connect-iq/api-docs/Toybox/FitContributor/Field.html)

## Constant Summary

### MessageType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MESG\_TYPE\_SESSION | 18 | API Level 1.3.0 | The message type for session messages. |
| MESG\_TYPE\_LAP | 19 | API Level 1.3.0 | The message type for lap messages. |
| MESG\_TYPE\_RECORD | 20 | API Level 1.3.0 | The message type for record messages. |

### DataType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DATA\_TYPE\_SINT8 | 1 | API Level 1.3.0 |  |
| DATA\_TYPE\_UINT8 | 2 | API Level 1.3.0 |  |
| DATA\_TYPE\_SINT16 | 3 | API Level 1.3.0 |  |
| DATA\_TYPE\_UINT16 | 4 | API Level 1.3.0 |  |
| DATA\_TYPE\_SINT32 | 5 | API Level 1.3.0 |  |
| DATA\_TYPE\_UINT32 | 6 | API Level 1.3.0 |  |
| DATA\_TYPE\_STRING | 7 | API Level 1.3.0 |  |
| DATA\_TYPE\_FLOAT | 8 | API Level 1.3.0 |  |
| DATA\_TYPE\_DOUBLE | 9 | API Level 1.3.0 |  |
