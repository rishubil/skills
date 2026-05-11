---
title: Toybox.AntPlus
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus.html
---

## Module: Toybox.AntPlus

## Overview

## See Also:

- [Toybox.Ant](Ant.md)
- [ANT Basics](https://www.thisisant.com/developer/ant/ant-basics/#104_tab)
- [ANT Downloads & Resources (ANT+ Device Profiles)](https://www.thisisant.com/developer/resources/downloads/)

## Classes Under Namespace

**Classes:** [AntPlusNotAllowedException](AntPlus/AntPlusNotAllowedException.md), [BatteryStatus](AntPlus/BatteryStatus.md), [BikeCadence](AntPlus/BikeCadence.md), [BikeCadenceInfo](AntPlus/BikeCadenceInfo.md), [BikeCadenceListener](AntPlus/BikeCadenceListener.md), [BikeLight](AntPlus/BikeLight.md), [BikePower](AntPlus/BikePower.md), [BikePowerListener](AntPlus/BikePowerListener.md), [BikeRadar](AntPlus/BikeRadar.md), [BikeRadarListener](AntPlus/BikeRadarListener.md), [BikeSpeed](AntPlus/BikeSpeed.md), [BikeSpeedCadence](AntPlus/BikeSpeedCadence.md), [BikeSpeedCadenceInfo](AntPlus/BikeSpeedCadenceInfo.md), [BikeSpeedCadenceListener](AntPlus/BikeSpeedCadenceListener.md), [BikeSpeedInfo](AntPlus/BikeSpeedInfo.md), [BikeSpeedListener](AntPlus/BikeSpeedListener.md), [CalculatedCadence](AntPlus/CalculatedCadence.md), [CalculatedPower](AntPlus/CalculatedPower.md), [CalculatedWheelDistance](AntPlus/CalculatedWheelDistance.md), [CalculatedWheelSpeed](AntPlus/CalculatedWheelSpeed.md), [CommonData](AntPlus/CommonData.md), [DerailleurStatus](AntPlus/DerailleurStatus.md), [Device](AntPlus/Device.md), [DeviceListener](AntPlus/DeviceListener.md), [DeviceState](AntPlus/DeviceState.md), [FitnessEquipment](AntPlus/FitnessEquipment.md), [FitnessEquipmentData](AntPlus/FitnessEquipmentData.md), [FitnessEquipmentListener](AntPlus/FitnessEquipmentListener.md), [FitnessEquipmentMode](AntPlus/FitnessEquipmentMode.md), [LightNetwork](AntPlus/LightNetwork.md), [LightNetworkListener](AntPlus/LightNetworkListener.md), [ManufacturerInfo](AntPlus/ManufacturerInfo.md), [PedalPowerBalance](AntPlus/PedalPowerBalance.md), [ProductInfo](AntPlus/ProductInfo.md), [RadarTarget](AntPlus/RadarTarget.md), [ResistanceSettings](AntPlus/ResistanceSettings.md), [RunningDynamics](AntPlus/RunningDynamics.md), [RunningDynamicsData](AntPlus/RunningDynamicsData.md), [RunningDynamicsListener](AntPlus/RunningDynamicsListener.md), [SensorPosition](AntPlus/SensorPosition.md), [Shifting](AntPlus/Shifting.md), [ShiftingListener](AntPlus/ShiftingListener.md), [ShiftingStatus](AntPlus/ShiftingStatus.md), [SimulationSettings](AntPlus/SimulationSettings.md), [TargetPowerSettings](AntPlus/TargetPowerSettings.md), [TorqueEffectivenessPedalSmoothness](AntPlus/TorqueEffectivenessPedalSmoothness.md), [UserSettings](AntPlus/UserSettings.md)

## Constant Summary

### Constant Variables

| Type | Name | Value | Since | Description |
| --- | --- | --- | --- | --- |
| Type | FRONT\_GEAR\_INVALID | 7 | API Level 3.1.0 | Invalid front gear index |
| Type | INVALID\_CADENCE | \-1 | API Level 3.0.0 |  |
| Type | INVALID\_SPEED | \-1 | API Level 3.0.0 | Represents an invalid speed value |
| Type | MAX\_GEARS\_INVALID | 0 | API Level 3.1.0 | Invalid max gears value |
| Type | REAR\_GEAR\_INVALID | 31 | API Level 3.1.0 | Invalid rear gear index |

### BatteryStatusValue

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BATT\_STATUS\_NEW | 1 | API Level 2.2.0 |  |
| BATT\_STATUS\_GOOD | 2 | API Level 2.2.0 |  |
| BATT\_STATUS\_OK | 3 | API Level 2.2.0 |  |
| BATT\_STATUS\_LOW | 4 | API Level 2.2.0 |  |
| BATT\_STATUS\_CRITICAL | 5 | API Level 2.2.0 |  |
| BATT\_STATUS\_INVALID | 7 | API Level 2.2.0 |  |
| BATT\_STATUS\_CNT | 8 | API Level 2.2.0 |  |

### MessageSendStatus

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MESSAGE\_SENT\_SUCCESS | 0 | API Level 3.1.0 | Message sent successfully |
| MESSAGE\_SENT\_FAILED | 1 | API Level 3.1.0 | Message sent failed |
| MESSAGE\_SENT\_COUNT | 2 | API Level 3.1.0 |  |

### MessageType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| MESSAGE\_TYPE\_MANUFACTURER | 0 | API Level 3.1.0 | Manufacturer specific message sent |
| MESSAGE\_TYPE\_PAGE\_REQUEST | 1 | API Level 3.1.0 | Page request sent |
| MESSAGE\_TYPE\_COUNT | 2 | API Level 3.1.0 |  |

### DeviceCurrentState

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| DEVICE\_STATE\_DEAD | 0 | API Level 2.2.0 | Device is not usable (not paired or disabled) |
| DEVICE\_STATE\_CLOSED | 1 | API Level 2.2.0 | Device's channel is closed |
| DEVICE\_STATE\_TRACKING | 3 | API Level 2.2.0 | Device's channel is open and tracking |
| DEVICE\_STATE\_CNT | 4 | API Level 2.2.0 |  |

### LightNetworkState

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LIGHT\_NETWORK\_STATE\_NOT\_FORMED | 0 | API Level 2.2.0 | Light network is not yet formed |
| LIGHT\_NETWORK\_STATE\_FORMING | 1 | API Level 2.2.0 | Light network is forming |
| LIGHT\_NETWORK\_STATE\_FORMED | 2 | API Level 2.2.0 | Light network is formed |

### LightNetworkMode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LIGHT\_NETWORK\_MODE\_INDIVIDUAL | 0 | API Level 2.2.0 | Light modes are set by the user |
| LIGHT\_NETWORK\_MODE\_AUTO | 1 | API Level 2.2.0 | Light modes are automatically set based on ambient light (or time of day if there is no ambient light sensor available) |
| LIGHT\_NETWORK\_MODE\_HIGH\_VIS | 2 | API Level 2.2.0 | Light modes are automatically placed in their highest-visibility mode |

### LightMode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LIGHT\_MODE\_OFF | 0 | API Level 2.2.0 |  |
| LIGHT\_MODE\_ST\_81\_100 | 1 | API Level 2.2.0 | Steady beam 81-100% intensity |
| LIGHT\_MODE\_ST\_61\_80 | 2 | API Level 2.2.0 | Steady beam 61-80% intensity |
| LIGHT\_MODE\_ST\_41\_60 | 3 | API Level 2.2.0 | Steady beam 41-60% intensity |
| LIGHT\_MODE\_ST\_21\_40 | 4 | API Level 2.2.0 | Steady beam 21-40% intensity |
| LIGHT\_MODE\_ST\_0\_20 | 5 | API Level 2.2.0 | Steady beam 0-20% intensity |
| LIGHT\_MODE\_SLOW\_FLASH | 6 | API Level 2.2.0 | Slow flash mode |
| LIGHT\_MODE\_FAST\_FLASH | 7 | API Level 2.2.0 | Fast flash mode |
| LIGHT\_MODE\_RANDOM\_FLASH | 8 | API Level 2.2.0 | Randomly timed flash mode |
| LIGHT\_MODE\_AUTO | 9 | API Level 2.2.0 |  |
| LIGHT\_MODE\_SIGNAL\_LEFT\_SC | 10 | API Level 2.2.0 | Turn signal left self-cancelling |
| LIGHT\_MODE\_SIGNAL\_LEFT | 11 | API Level 2.2.0 | Turn signal left |
| LIGHT\_MODE\_SIGNAL\_RIGHT\_SC | 12 | API Level 2.2.0 | Turn signal right self-cancelling |
| LIGHT\_MODE\_SIGNAL\_RIGHT | 13 | API Level 2.2.0 | Turn signal right |
| LIGHT\_MODE\_HAZARD | 14 | API Level 2.2.0 | Hazard - right and left signals flash |
| LIGHT\_MODE\_CUSTOM\_5 | 59 | API Level 2.2.0 | Custom mode (manufacturer-defined) |
| LIGHT\_MODE\_CUSTOM\_4 | 60 | API Level 2.2.0 | Custom mode (manufacturer-defined) |
| LIGHT\_MODE\_CUSTOM\_3 | 61 | API Level 2.2.0 | Custom mode (manufacturer-defined) |
| LIGHT\_MODE\_CUSTOM\_2 | 62 | API Level 2.2.0 | Custom mode (manufacturer-defined) |
| LIGHT\_MODE\_CUSTOM\_1 | 63 | API Level 2.2.0 | Custom mode (manufacturer-defined) |

### LightType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| LIGHT\_TYPE\_HEADLIGHT | 0 | API Level 2.2.0 | Headlight light type |
| LIGHT\_TYPE\_TAILLIGHT | 2 | API Level 2.2.0 | Taillight light type |
| LIGHT\_TYPE\_SIGNAL\_CONFIG | 3 | API Level 2.2.0 | Configurable signal light type |
| LIGHT\_TYPE\_SIGNAL\_LEFT | 4 | API Level 2.2.0 | Left turn signal light type |
| LIGHT\_TYPE\_SIGNAL\_RIGHT | 5 | API Level 2.2.0 | Right turn signal light type |
| LIGHT\_TYPE\_OTHER | 7 | API Level 2.2.0 | Undefined light type |

### BikePowerSensorType

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BIKE\_POWER\_SENSOR\_TYPE\_NONE | 0 | API Level 2.2.0 | None |
| BIKE\_POWER\_SENSOR\_TYPE\_POWER\_ONLY | 1 | API Level 2.2.0 | Power output directly in Watts |
| BIKE\_POWER\_SENSOR\_TYPE\_WHEEL\_TORQUE | 2 | API Level 2.2.0 | Power output from torque on rear wheel |
| BIKE\_POWER\_SENSOR\_TYPE\_CRANK\_TORQUE | 3 | API Level 2.2.0 | Power output from torque at crank |
| BIKE\_POWER\_SENSOR\_TYPE\_CRANK\_TORQUE\_FREQUENCY | 4 | API Level 2.2.0 | Power output from torque frequency at crank |
| BIKE\_POWER\_SENSOR\_TYPE\_CNT | 5 | API Level 2.2.0 |  |

### ThreatLevel

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| THREAT\_LEVEL\_NO\_THREAT | 0 | API Level 3.0.0 | No threat |
| THREAT\_LEVEL\_VEHICLE\_APPROACHING | 1 | API Level 3.0.0 | Vehicle is approaching |
| THREAT\_LEVEL\_VEHICLE\_FAST\_APPROACHING | 2 | API Level 3.0.0 | Vehicle is approaching fast |

### ThreatSide

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| THREAT\_SIDE\_NO\_SIDE | 0 | API Level 3.0.0 | Threat not on right or left |
| THREAT\_SIDE\_RIGHT | 1 | API Level 3.0.0 | Threat is on the right side |
| THREAT\_SIDE\_LEFT | 2 | API Level 3.0.0 | Threat is on the left side |

### TrainerMode

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| TRAINER\_MODE\_BASIC\_RESISTANCE | 0 | API Level 2.4.0 | Basic resistance fitness equipment training mode In this mode the user may set the percentage of maximum resistance on the equipment |
| TRAINER\_MODE\_TARGET\_POWER | 1 | API Level 2.4.0 | Target power fitness equipment training mode In this mode the user may set the target wattage output of the equipment |
| TRAINER\_MODE\_SIMULATION | 2 | API Level 2.4.0 | Simulation fitness equipment training mode In this mode the user may set various fields to adjust resistance |

### TrainerValue

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| TRAINER\_MODE | 7 | API Level 2.4.0 | The training mode the fitness equipment is currently in. See TRAINER\_MODE\_\* enum for values |
| TRAINER\_RESISTANCE | 8 | API Level 2.4.0 | Basic resistance value of the fitness equipment. Percent of max resistance 0 - 100 input range, unit 0.5%. |
| TRAINER\_TARGET\_POWER | 9 | API Level 2.4.0 | Target power setting of the fitness equipment. 0 - 4000W input range, unit 0.25W. |
| TRAINER\_SLOPE | 10 | API Level 2.4.0 | The simulated Slope/Grade setting of simulation training mode. -200% - 200% input range, unit 0.01%. |
| TRAINER\_SURFACE | 11 | API Level 2.4.0 | The simulated surface resistance coefficient setting of simulation training mode. 0 - 0.0127 input range, 5x10^-5 scale. Default value is set to 0xFF. |
| TRAINER\_WIND\_COEFF | 12 | API Level 2.4.0 | The simulated wind resistance coefficient setting of simulation training mode. 0.0 - 1.86 kg/m input range, 0.01 scale. Wind Resistance Coefficient \[kg/m\] = Frontal Surface Area \[m2\] x Drag Coefficient x Air Density \[kg/m3\] Default value is set to 0xFF. |
| TRAINER\_WIND\_SPEED | 13 | API Level 2.4.0 | The simulated wind speed setting of simulation training mode. -127 - +127 km/hr input range, (+)Head wind (-)Tail wind. 1 km/hr units. Simulated Wind Speed (km/h) = Raw Wind Speed Value – 127 km/h Default value is set to 0xFF. |
| TRAINER\_WIND\_DRAFT\_FACTOR | 14 | API Level 2.4.0 | The simulated wind drafting scale factor setting of simulation training mode. 0 - 1.0 input range, 0.01 scale. A draft factor of 0 removes all wind resistance, and 1.0 indicates no drafting effects. |
| TRAINER\_USER\_WEIGHT | 15 | API Level 2.4.0 | The user weight setting of simulation training mode. 0 - 655.34 kg input range, unit 0.01kg. |
| TRAINER\_BIKE\_WEIGHT | 16 | API Level 2.4.0 | The bike weight setting of simulation training mode. 0 - 50kg input range, unit 0.05kg |
| TRAINER\_WHEEL\_DIAMETER | 17 | API Level 2.4.0 | The wheel diameter setting of the fitness equipment. 0 - 2.54m input range, unit 0.01m |
| TRAINER\_GEAR\_RATIO | 18 | API Level 2.4.0 | The gear ratio setting of the fitness equipment. 0.03 - 7.65 input range, unit 0.03. gear ratio = value \* 0.03 |

### BodyLocation

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| BODY\_LOCATION\_LEFT\_LEG | 0 | API Level 2.4.0 | Left leg body location |
| BODY\_LOCATION\_RIGHT\_LEG | 1 | API Level 2.4.0 | Right leg body location |
| BODY\_LOCATION\_TORSO\_FRONT | 17 | API Level 2.4.0 | Front torso body location |
| BODY\_LOCATION\_WAIST\_MID\_BACK | 36 | API Level 2.4.0 | Waist, mid back body location |
| BODY\_LOCATION\_WAIST\_FRONT | 37 | API Level 2.4.0 | Waist, front body location |
| BODY\_LOCATION\_WAIST\_LEFT | 38 | API Level 2.4.0 | Waist, left body location |
| BODY\_LOCATION\_WAIST\_RIGHT | 39 | API Level 2.4.0 | Waist, right body location |

### SensorOrientation

| Name | Value | Since | Description |
| --- | --- | --- | --- |
| SENSOR\_ORIENTATION\_RIGHT\_SIDE\_UP | 0 | API Level 2.4.0 | Right side up sensor orientation |
| SENSOR\_ORIENTATION\_UPSIDE\_DOWN | 1 | API Level 2.4.0 | Upside down sensor orientation |
