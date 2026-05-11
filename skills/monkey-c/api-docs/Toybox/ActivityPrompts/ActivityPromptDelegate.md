---
title: Toybox.ActivityPrompts.ActivityPromptDelegate
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPromptDelegate.html
---

## Class: Toybox.ActivityPrompts.ActivityPromptDelegate

## Overview

Delegate used by the system to notify the app about activity prompts

Registered using [ActivityPrompts.registerActivityPromptListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html#registerActivityPromptsListener-instance_function) to allow an app to get notified when an activity prompt should be played.

## Instance Method Summary

- [**onAudioOutputChange**](#onAudioOutputChange-instance_function "onAudioOutputChange (Instance Function)") (selectedHandler as [Lang.Boolean](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Boolean.html)) as **Void**
	Called by the system if [ActivityPrompts.registerActivityPromptListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html#registerActivityPromptsListener-instance_function) has been called and the user has changed the activity prompt output provider.
- [**onPrompt**](#onPrompt-instance_function "onPrompt (Instance Function)") (prompts as [Lang.Array](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Array.html) < [ActivityPrompts.ActivityPrompt](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts/ActivityPrompt.html) >, priority as [Lang.Number](https://developer.garmin.com/connect-iq/api-docs/Toybox/Lang/Number.html)) as **Void**
	Called by the system when an activity prompt is to be played.

## Instance Method Details

### onAudioOutputChange(selectedHandler as Lang.Boolean) as Void

Called by the system if [ActivityPrompts.registerActivityPromptListener()](https://developer.garmin.com/connect-iq/api-docs/Toybox/ActivityPrompts.html#registerActivityPromptsListener-instance_function) has been called and the user has changed the activity prompt output provider.

### onPrompt(prompts as Lang.Array<ActivityPrompts.ActivityPrompt>, priority as Lang.Number) as Void

Called by the system when an activity prompt is to be played
