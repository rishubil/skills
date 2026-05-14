---
title: Toybox.AntPlus.FitnessEquipment
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/AntPlus/FitnessEquipment.html
---

## Class: Toybox.AntPlus.FitnessEquipment

## Overview

Represents a Fitness Equipment Device instance.

## Instance Method Summary

- [**controlEquipment**](#controlEquipment-instance_function "controlEquipment (Instance Function)") (setting as [AntPlus.TrainerValue](../AntPlus.md#TrainerValue-module), data as [Lang.Float](../Lang/Float.md) or [AntPlus.TrainerMode](../AntPlus.md#TrainerMode-module)) as **Void**
	Control the fitness Equipment Note: Setting a value related to a specific training mode will cause the fitness equipment to change to that mode.
- [**getEquipmentData**](#getEquipmentData-instance_function "getEquipmentData (Instance Function)") () as [AntPlus.FitnessEquipmentData](FitnessEquipmentData.md)
	Get the current training data from the FE.
- [**getResistanceSettings**](#getResistanceSettings-instance_function "getResistanceSettings (Instance Function)") () as [AntPlus.ResistanceSettings](ResistanceSettings.md)
	Get the resistance percentage setting of the fitness equipment for basic resistance training mode.
- [**getSimulationSettings**](#getSimulationSettings-instance_function "getSimulationSettings (Instance Function)") () as [AntPlus.SimulationSettings](SimulationSettings.md)
	Get the wind and track resistance simulation settings.
- [**getTargetPowerSettings**](#getTargetPowerSettings-instance_function "getTargetPowerSettings (Instance Function)") () as [AntPlus.TargetPowerSettings](TargetPowerSettings.md)
	Get the target power setting of the fitness equipment for target power training mode.
- [**getTrainerMode**](#getTrainerMode-instance_function "getTrainerMode (Instance Function)") () as [AntPlus.FitnessEquipmentMode](FitnessEquipmentMode.md)
	Get the current training mode and supported modes of the fitness equipment.
- [**getUserSettings**](#getUserSettings-instance_function "getUserSettings (Instance Function)") () as [AntPlus.UserSettings](UserSettings.md)
	Get the user configuration settings of the fitness equipment for simulation training mode.
- [**initialize**](#initialize-instance_function "initialize (Instance Function)") (listener as [AntPlus.FitnessEquipmentListener](FitnessEquipmentListener.md) or **Null**)
	Constructor.
- [**setTrainerMode**](#setTrainerMode-instance_function "setTrainerMode (Instance Function)") (mode as [AntPlus.TrainerMode](../AntPlus.md#TrainerMode-module)) as **Void**
	Set the trainer mode.

## Instance Method Details

### controlEquipment(setting as AntPlus.TrainerValue, data as Lang.Float or AntPlus.TrainerMode) as Void

Control the fitness Equipment Note: Setting a value related to a specific training mode will cause the fitness equipment to change to that mode. For example, controlEquipment(TRAINER\_TARGET\_POWER, 100) will set the fitness equipment to target power mode with target power set to 100W if such mode is supported. Values out of range will be set to within the nearest range boundary value.

### getEquipmentData() as AntPlus.FitnessEquipmentData

Get the current training data from the FE

### getResistanceSettings() as AntPlus.ResistanceSettings

Get the resistance percentage setting of the fitness equipment for basic resistance training mode. You should set resistance values and be in basic resistance training mode before calling this method, otherwise `null` or default values may be returned.

### getSimulationSettings() as AntPlus.SimulationSettings

Get the wind and track resistance simulation settings. You should set wind and track settings, as well as be in simulation training mode before calling this method or `null` or default values may be returned.

### getTargetPowerSettings() as AntPlus.TargetPowerSettings

Get the target power setting of the fitness equipment for target power training mode. You should set the target power and be in target power training mode before calling this method, otherwise `null` or default values may be returned.

### getTrainerMode() as AntPlus.FitnessEquipmentMode

Get the current training mode and supported modes of the fitness equipment

### getUserSettings() as AntPlus.UserSettings

Get the user configuration settings of the fitness equipment for simulation training mode. You should set user settings values and be in simulation mode before calling this method, otherwise `null` or default values may be returned.

### initialize(listener as AntPlus.FitnessEquipmentListener or Null)

Constructor

### setTrainerMode(mode as AntPlus.TrainerMode) as Void

Set the trainer mode. You should check the capable modes of the fitness equipment, as the command will be ignored by the fitness equipment if the mode is not supported.
