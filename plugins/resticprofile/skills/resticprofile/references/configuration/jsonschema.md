---
title: JSON schema :: resticprofile
source: https://creativeprojects.github.io/resticprofile/configuration/jsonschema/
---

## JSON schema

JSON, YAML and TOML configuration files can benefit from a JSON schema that describes the config structure depending on the selected *restic* and configuration file version.

## Schema URL

**[https://creativeprojects.github.io/resticprofile/jsonschema/config.json](https://creativeprojects.github.io/resticprofile/jsonschema/config.json)**

This schema detects config and restic version and redirects to the corresponding [versioned URL](https://creativeprojects.github.io/resticprofile/configuration/jsonschema/index.html#versioned-urls). Detection requires full support for JSON Schema Draft 7. Use a versioned URL where not supported (e.g. TOML).

## Usage (vscode)

To use a schema with **vscode**, begin your config files with:

```toml
#:schema https://creativeprojects.github.io/resticprofile/jsonschema/config-2.json

version = "2"
```

```yaml
# yaml-language-server: $schema=https://creativeprojects.github.io/resticprofile/jsonschema/config.json

version: "2"
```

```json
{
    "$schema": "https://creativeprojects.github.io/resticprofile/jsonschema/config.json",
    "version": "2"
}
```

Info

YAML & TOML validation with JSON schema is not supported out of the box. Additional extensions are required, such as ‘redhat.vscode-yaml’ for YAML and ’tamasfe.even-better-toml’ for TOML in Visual Studio Code.

**Example**

![](https://creativeprojects.github.io/resticprofile/configuration/jsonschema/jsonschema-vsc.gif)

**Extension**: `redhat.vscode-yaml`

## Versioned URLs

The following versioned schemas are referenced from `config.json`. Which URL is selected depends on config and restic version. You may use the URLs directly if you need a self-contained schema file or to enforce a certain version of configuration format and/or restic flags

JSON schema URLs for **any** *restic* version:

- Config V1: [https://creativeprojects.github.io/resticprofile/jsonschema/config-1.json](https://creativeprojects.github.io/resticprofile/jsonschema/config-1.json)
- Config V2: [https://creativeprojects.github.io/resticprofile/jsonschema/config-2.json](https://creativeprojects.github.io/resticprofile/jsonschema/config-2.json)

These universal schemas contain all flags and commands of all known *restic* versions and may allow to set flags that are not supported by a particular *restic* version. Descriptions and deprecation markers indicate what is supported and what should no longer be used.

JSON schema URLs for a **specific** *restic* version (list of [available URLs](https://creativeprojects.github.io/resticprofile/reference/json-schema/index.html)):

- `.../config-1-restic-{MAJOR}-{MINOR}.json`
- `.../config-2-restic-{MAJOR}-{MINOR}.json`

These schemas contain only flags and commands of a specific *restic* version. The schema will validate a config only when flags are used that the selected *restic* version supports according to its manual pages.

Tip

As an alternative to URLs, schemas can be generated locally with: `resticprofile generate --json-schema [--version RESTIC_VERSION] [global|v1|v2]`