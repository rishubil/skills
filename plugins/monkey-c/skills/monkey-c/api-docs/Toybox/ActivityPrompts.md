---
title: Toybox.ActivityPrompts
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html
---

## Module: Toybox.ActivityPrompts

## Overview

The ActivityPrompts module allows a data field to handle audio output during an activity.

Using this module will cause to all activity prompts during an activity to no longer play through the device or any connected devices such as headphones. The user must select the data field as the activity prompt handler in the device menus.

Prompts will be passed to [ActivityPromptDelegate.onPrompt()](ActivityPrompts/ActivityPromptDelegate.md#onPrompt-instance_function) when they are to be played. If more than one prompt is passed to `ActivityPromptDelegate::onPrompt()`, they are meant to be played together uninterrupted.

## Classes Under Namespace

**Classes:** [ActivityPrompt](ActivityPrompts/ActivityPrompt.md), [ActivityPromptDelegate](ActivityPrompts/ActivityPromptDelegate.md)

## Typedef Summary

- [**ActivityPromptContextValue**](#ActivityPromptContextValue-named_type "ActivityPromptContextValue (Named Type)") as [Lang.Boolean](Lang/Boolean.md) or [Lang.Number](Lang/Number.md) or [Lang.Double](Lang/Double.md) or [Lang.String](Lang/String.md) or [Lang.Dictionary](Lang/Dictionary.md) < [Lang.String](Lang/String.md), [ActivityPrompts.ActivityPromptContextValue](ActivityPrompts.md#ActivityPromptContextValue-named_type) > or [Lang.Array](Lang/Array.md) < [ActivityPrompts.ActivityPromptContextValue](ActivityPrompts.md#ActivityPromptContextValue-named_type) > or **Null**

## Instance Method Summary

- [**registerActivityPromptsListener**](#registerActivityPromptsListener-instance_function "registerActivityPromptsListener (Instance Function)") (delegate as [ActivityPrompts.ActivityPromptDelegate](ActivityPrompts/ActivityPromptDelegate.md), options as [Lang.Dictionary](Lang/Dictionary.md) or **Null**) as [Lang.Boolean](Lang/Boolean.md)
- [**setActivityPromptTextLanguage**](#setActivityPromptTextLanguage-instance_function "setActivityPromptTextLanguage (Instance Function)") (languages as [System.Language](System.md#Language-module)) as [Lang.Boolean](Lang/Boolean.md)
	Set the language for [ActivityPrompt.text](ActivityPrompts/ActivityPrompt.md#text-var).
- [**unregisterActivityPromptsListener**](#unregisterActivityPromptsListener-instance_function "unregisterActivityPromptsListener (Instance Function)") () as **Void**
	Unregister as the activity prompt output handler.
