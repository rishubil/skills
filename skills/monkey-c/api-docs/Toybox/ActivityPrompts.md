---
title: Toybox.ActivityPrompts
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html
---

## Module: Toybox.ActivityPrompts

## Overview

The ActivityPrompts module allows a data field to handle audio output during an activity.

Using this module will cause to all activity prompts during an activity to no longer play through the device or any connected devices such as headphones. The user must select the data field as the activity prompt handler in the device menus.

Prompts will be passed to [ActivityPromptDelegate.onPrompt()](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPromptDelegate.html#onPrompt-instance_function) when they are to be played. If more than one prompt is passed to `ActivityPromptDelegate::onPrompt()`, they are meant to be played together uninterrupted.

## Classes Under Namespace

**Classes:** [ActivityPrompt](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPrompt.html), [ActivityPromptDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPromptDelegate.html)

## Typedef Summary

- [**ActivityPromptContextValue**](#ActivityPromptContextValue-named_type "ActivityPromptContextValue (Named Type)") as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html) or [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html) or [Lang.Double](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Double.html) or [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), [ActivityPrompts.ActivityPromptContextValue](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html#ActivityPromptContextValue-named_type) > or [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [ActivityPrompts.ActivityPromptContextValue](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html#ActivityPromptContextValue-named_type) > or **Null**

## Instance Method Summary

- [**registerActivityPromptsListener**](#registerActivityPromptsListener-instance_function "registerActivityPromptsListener (Instance Function)") (delegate as [ActivityPrompts.ActivityPromptDelegate](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPromptDelegate.html), options as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) or **Null**) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
- [**setActivityPromptTextLanguage**](#setActivityPromptTextLanguage-instance_function "setActivityPromptTextLanguage (Instance Function)") (languages as [System.Language](https://developer.garmin.com/connect-iq/api-docs/Toybox/System.html#Language-module)) as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)
	Set the language for [ActivityPrompt.text](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPrompt.html#text-var).
- [**unregisterActivityPromptsListener**](#unregisterActivityPromptsListener-instance_function "unregisterActivityPromptsListener (Instance Function)") () as **Void**
	Unregister as the activity prompt output handler.
