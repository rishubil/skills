---
title: Toybox.ActivityPrompts.ActivityPrompt
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPrompt.html
---

## Class: Toybox.ActivityPrompts.ActivityPrompt

## Overview

Informtion about the activity prompt.

Created by the system and passed to [ActivityPromptDelegate.onPrompt()](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPromptDelegate.html#onPrompt-instance_function) when an activity prompt is to be played.

## Instance Member Summary

- [**context**](#context-var "context (Var)") as [Lang.Dictionary](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Dictionary.html) < [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html), [ActivityPrompts.ActivityPromptContextValue](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html#ActivityPromptContextValue-named_type) >
	Data for the prompt.
- [**templateName**](#templateName-var "templateName (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html)
	The prompt identifier.
- [**text**](#text-var "text (Var)") as [Lang.String](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/String.html) or **Null**
	The text-to-speech text to be spoken.

## Instance Attribute Details

### var context as Lang.Dictionary<Lang.String, ActivityPrompts.ActivityPromptContextValue>

Data for the prompt. The usage of this depends on the value of [ActivityPrompt.templateName](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPrompt.html#templateName-var).

### var templateName as Lang.String

The prompt identifier.

### var text as Lang.String or Null

The text-to-speech text to be spoken.
