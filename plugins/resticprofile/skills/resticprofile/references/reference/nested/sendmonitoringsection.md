---
title: SendMonitoringSection :: resticprofile
source: https://creativeprojects.github.io/resticprofile/reference/nested/sendmonitoringsection/
---

## SendMonitoringSection

#### Nested SendMonitoringSection

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| **body** | `string` |  | Request body, overrides “body-template” |
| **body-template** | `string` |  | Path to a file containing the request body (go template). See [configuration/http\_hooks/#body-template](https://creativeprojects.github.io/resticprofile/configuration/http_hooks/#body-template) |
| **headers** | one or more nested *[SendMonitoringHeader](https://creativeprojects.github.io/resticprofile/reference/nested/sendmonitoringheader/index.html)* |  | Additional HTTP headers to send with the request |
| **method** | `string` | `GET` | HTTP method of the request. Is one of `GET`, `DELETE`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, `PUT`, `TRACE` |
| **skip-tls-verification** | `true` / `false` | `false` | Enables insecure TLS (without verification), see also “global.ca-certificates” |
| **url** | `uri` |  | URL of the target to send to |