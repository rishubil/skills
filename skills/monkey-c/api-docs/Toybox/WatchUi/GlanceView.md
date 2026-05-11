---
title: Toybox.WatchUi.GlanceView
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/GlanceView.html
---

## Class: Toybox.WatchUi.GlanceView

## Overview

The class that represents a glance view which can be used to display the widget preview content in a restricted drawing context (dc) among other widgets.

Glance view behaves mostly like a regular WatchUi.View, e.g. user can load layout and update view using [View.onLayout()](View.md#onLayout-instance_function) and [View.onUpdate()](View.md#onUpdate-instance_function), however, the `dc` object passed in those calls will be bounded by glance area rather than a full screen `dc`.

GlanceView doesn't support [WatchUi.Layer](Layer.md) or other View APIs that are associated with layering system, such as [View.addLayer()](View.md#addLayer-instance_function) [View.removeLayer()](View.md#removeLayer-instance_function), [View.insertLayer()](View.md#insertLayer-instance_function), [View.clearLayers()](View.md#clearLayers-instance_function)

The widget that's running in the glance mode are prohibited from using page control functionality, as there is only one view allowed during said mode.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.

## Instance Method Details

### initialize()

Constructor
