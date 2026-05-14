---
title: Toybox.AntPlus.DerailleurStatus
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/DerailleurStatus.html
---

## Class: Toybox.AntPlus.DerailleurStatus

## Overview

Class that stores current status information about a connected derailleur

## Instance Member Summary

- [**gearIndex**](#gearIndex-var "gearIndex (Var)") as [Lang.Number](../Lang/Number.md)
	Current gear index (for front derailleur 0 - 6, [Toybox::AntPlus::FRONT\_GEAR\_INVALID](../AntPlus.md#FRONT_GEAR_INVALID-const) = Unknown gear index / Error) (for rear derailleur 0 - 30, [Toybox::AntPlus::REAR\_GEAR\_INVALID](../AntPlus.md#REAR_GEAR_INVALID-const) = Unknown gear index / Error).
- [**gearMax**](#gearMax-var "gearMax (Var)") as [Lang.Number](../Lang/Number.md)
	Number of gears installed (1 - 7, [Toybox::AntPlus::MAX\_GEARS\_INVALID](../AntPlus.md#MAX_GEARS_INVALID-const) = Unknown gear count / Error) (1 - 31, [Toybox::AntPlus::MAX\_GEARS\_INVALID](../AntPlus.md#MAX_GEARS_INVALID-const) = Unknown gear count / Error).
- [**gearSize**](#gearSize-var "gearSize (Var)") as [Lang.Number](../Lang/Number.md)
	Current gear size (number of teeth, 0 - 255).
- [**invalidInboardShiftCount**](#invalidInboardShiftCount-var "invalidInboardShiftCount (Var)") as [Lang.Number](../Lang/Number.md)
	Number of invalid inboard shifts (0 - 255).
- [**invalidOutboardShiftCount**](#invalidOutboardShiftCount-var "invalidOutboardShiftCount (Var)") as [Lang.Number](../Lang/Number.md)
	Number of invalid outboard shifts (0 - 255).
- [**shiftFailureCount**](#shiftFailureCount-var "shiftFailureCount (Var)") as [Lang.Number](../Lang/Number.md)
	Number of shift failures (0 - 255).

## Instance Attribute Details

### var gearIndex as Lang.Number

Current gear index (for front derailleur 0 - 6, [Toybox::AntPlus::FRONT\_GEAR\_INVALID](../AntPlus.md#FRONT_GEAR_INVALID-const) = Unknown gear index / Error) (for rear derailleur 0 - 30, [Toybox::AntPlus::REAR\_GEAR\_INVALID](../AntPlus.md#REAR_GEAR_INVALID-const) = Unknown gear index / Error)

### var gearMax as Lang.Number

Number of gears installed (1 - 7, [Toybox::AntPlus::MAX\_GEARS\_INVALID](../AntPlus.md#MAX_GEARS_INVALID-const) = Unknown gear count / Error) (1 - 31, [Toybox::AntPlus::MAX\_GEARS\_INVALID](../AntPlus.md#MAX_GEARS_INVALID-const) = Unknown gear count / Error)

### var gearSize as Lang.Number

Current gear size (number of teeth, 0 - 255)

### var invalidInboardShiftCount as Lang.Number

Number of invalid inboard shifts (0 - 255)

### var invalidOutboardShiftCount as Lang.Number

Number of invalid outboard shifts (0 - 255)

### var shiftFailureCount as Lang.Number

Number of shift failures (0 - 255)
