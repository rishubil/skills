---
title: Toybox.WatchUi.GlanceView
source: https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/GlanceView.html
---

## Class: Toybox.WatchUi.GlanceView

## Overview

The class that represents a glance view which can be used to display the widget preview content in a restricted drawing context (dc) among other widgets.

Glance view behaves mostly like a regular WatchUi.View, e.g. user can load layout and update view using [View.onLayout()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onLayout-instance_function) and [View.onUpdate()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#onUpdate-instance_function), however, the `dc` object passed in those calls will be bounded by glance area rather than a full screen `dc`.

GlanceView doesn't support [WatchUi.Layer](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/Layer.html) or other View APIs that are associated with layering system, such as [View.addLayer()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#addLayer-instance_function) [View.removeLayer()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#removeLayer-instance_function), [View.insertLayer()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#insertLayer-instance_function), [View.clearLayers()](https://developer.garmin.com/connect-iq/api-docs/Toybox/WatchUi/View.html#clearLayers-instance_function)

The widget that's running in the glance mode are prohibited from using page control functionality, as there is only one view allowed during said mode.

## Instance Method Summary

- [**initialize**](#initialize-instance_function "initialize (Instance Function)") ()
	Constructor.

## Instance Method Details

### initialize()

Constructor
