---
title: Toybox.Position
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html
---

## Module: Toybox.Position

## Overview

## Classes Under Namespace

**Classes:** [Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Info.html), [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html)

## Constant Summary

### Constellation

**This has been deprecated**

This enum may be removed after System 10.

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONSTELLATION\_GPS | 0 | API Level 3.2.0 | Use the GPS satellite constellation |
| CONSTELLATION\_GLONASS | 1 | API Level 3.2.0 | Use the GLONASS satellite constellation |
| CONSTELLATION\_GALILEO | 2 | API Level 3.2.0 | Use the GALILEO satellite constellation |

### Configuration

Configuration values for known GNSS configurations

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| CONFIGURATION\_GPS | 1 | API Level 3.3.6 | GPS L1 |
| CONFIGURATION\_GPS\_GLONASS | 2 | API Level 3.3.6 | GPS L1 and GLONASS |
| CONFIGURATION\_GPS\_GALILEO | 3 | API Level 3.3.6 | GPS L1 and GALILEO L1 |
| CONFIGURATION\_GPS\_BEIDOU | 4 | API Level 3.3.6 | GPS L1 and BEIDOU L1 |
| CONFIGURATION\_GPS\_GLONASS\_GALILEO\_BEIDOU\_L1 | 5 | API Level 3.3.6 | GPS L1, GLONASS, GALILEO L1, BEIDOU L1  This option is supported by System 6 devices like fenix7 and edge1040 |
| CONFIGURATION\_GPS\_GLONASS\_GALILEO\_BEIDOU\_L1\_L5 | 6 | API Level 3.3.6 | GPS L1, GPS L5, GLONASS, GALILEO L1A, GALILEO L5, BEIDOU L1, BEIDOU L5  Referred to as Multi-GNSS Multi-band on Edge 1040.  This option is supported by System 6 devices like fenix7 and edge1040 |
| CONFIGURATION\_SAT\_IQ | 255 | API Level 3.3.6 | AutoGNSS (SatIQ™) |

### CoordinateFormat

| Name | Value | Since | Description | See Also |
| --- | --- | --- | --- | --- |
| GEO\_DEG | 0 | API Level 1.0.0 | The decimal degree format: ddd.dddddd (e.g. 38.278652) | - [Decimal Degrees](https://en.wikipedia.org/wiki/Decimal_degrees) |
| GEO\_DM | 1 | API Level 1.0.0 | The degrees/decimal minutes format: dddmm.mmm (e.g 38 27.865') |  |
| GEO\_DMS | 2 | API Level 1.0.0 | degrees/minutes/seconds (DMS) format: ddd mm ss (e.g. 38 27' 8") |  |
| GEO\_MGRS | 3 | API Level 1.0.0 | Military Grid Reference System, or MGRS (e.g. 4QFJ12345678) | - [Military Grid Reference System](https://en.wikipedia.org/wiki/Military_Grid_Reference_System) |

### Quality

| Name | Value | Since | Description | See Also |
| --- | --- | --- | --- | --- |
| QUALITY\_NOT\_AVAILABLE | 0 | API Level 1.0.0 | GPS is not available |  |
| QUALITY\_LAST\_KNOWN | 1 | API Level 1.0.0 | The Location is based on the last known GPS fix. |  |
| QUALITY\_POOR | 2 | API Level 1.0.0 | The Location was calculated with a poor GPS fix. Only a 2-D GPS fix is available, likely due to a limited number of tracked satellites. |  |
| QUALITY\_USABLE | 3 | API Level 1.0.0 | The Location was calculated with a usable GPS fix. A 3-D GPS fix is available, with marginal HDOP (horizontal dilution of precision) | - [Dilution of Precision](https://en.wikipedia.org/wiki/Dilution_of_precision_\(navigation\)) |
| QUALITY\_GOOD | 4 | API Level 1.0.0 | The Location was calculated with a good GPS fix. A 3-D GPS fix is available, with good-to-excellent HDOP (horizontal dilution of precision). | - [Dilution of Precision](https://en.wikipedia.org/wiki/Dilution_of_precision_\(navigation\)) |

### LocationAcquisitionType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LOCATION\_ONE\_SHOT | 0 | API Level 1.0.0 | Enables a one-time Location acquisition |
| LOCATION\_CONTINUOUS | 1 | API Level 1.0.0 | Enables continuous Location tracking |
| LOCATION\_DISABLE | 2 | API Level 1.0.0 | Disables Location tracking |

### PositioningMode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| POSITIONING\_MODE\_NORMAL | 0 | API Level 3.2.0 | Standard positioning mode used by default for fitness activities |
| POSITIONING\_MODE\_AVIATION | 1 | API Level 3.2.0 | Enable special mode for aviation use-cases that require support for higher altitudes. |

## Instance Method Summary

- [**createBoundingBox**](#createBoundingBox-instance_function "createBoundingBox (Instance Function)") (locations as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) >) as \[ [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html), [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) \] or **Null**
	Create a bounding box from an array of [Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html) objects.
- [**enableLocationEvents**](#enableLocationEvents-instance_function "enableLocationEvents (Instance Function)") (options as {:acquisitionType as [Position.LocationAcquisitionType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#LocationAcquisitionType-module),:constellations as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [Position.Constellation](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#Constellation-module) >,:configuration as [Position.Configuration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#Configuration-module),:mode as [Position.PositioningMode](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#PositioningMode-module) } or [Position.LocationAcquisitionType](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#LocationAcquisitionType-module), listener as **Null** or [Lang.Method](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Method.html) (loc as [Position.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Info.html)) as **Void**) as **Void**
	Request a Location event.
- [**getInfo**](#getInfo-instance_function "getInfo (Instance Function)") () as [Position.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Info.html)
	Get the current [Position.Info](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Info.html).
- [**hasConfigurationSupport**](#hasConfigurationSupport-instance_function "hasConfigurationSupport (Instance Function)") (config as [Position.Configuration](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#Configuration-module)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Determines if the device supports a requested GPS configuration.
- [**parse**](#parse-instance_function "parse (Instance Function)") (string as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), format as [Position.CoordinateFormat](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position.html#CoordinateFormat-module)) as [Position.Location](https://developer.garmin.com/connect-iq/api-docs/Toybox/Position/Location.html)
	Convert a String to a Location object.

## Instance Method Details

### createBoundingBox(locations as Lang.Array<Position.Location>) as \[ Position.Location, Position.Location \] or Null

### enableLocationEvents(options as {:acquisitionType as Position.LocationAcquisitionType,:constellations as Lang.Array<Position.Constellation>,:configuration as Position.Configuration,:mode as Position.PositioningMode } or Position.LocationAcquisitionType, listener as Null or Lang.Method(loc as Position.Info) as Void) as Void

Note:

Passing an options [Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) is only supported with ConnectIQ 3.2.0 and later.

Note:

Passing the `:configuration` option is only supported with ConnectIQ 3.3.6 or later.

Note:

Multitasking: Location events will be disabled when app enters inacitve state, and re-enabled when is active again. These state changes are denoted by calls to AppBase.onActive() and AppBase.onInactive().
