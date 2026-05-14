---
title: Using Monkey C from the Command Line
source: https://developer.garmin.com/connect-iq/reference-guides/monkey-c-command-line-setup/
---

Before getting started with the installation on Mac or Windows, you'll need version 11 or higher of the Oracle Java™ Runtime Environment installed. Once that's done, continue on to your platform's installation instructions.

## OS X Installation

1. [Install the Connect IQ SDK Manager](https://developer.garmin.com/connect-iq/connect-iq-basics/getting-started/), download the SDK, and set the active SDK.
2. Point your `PATH` to the active Connect IQ bin directory in the Terminal. To temporarily add it to a single local shell instance:
```bash
$ export PATH=$PATH:\`cat $HOME/Library/Application\ Support/Garmin/ConnectIQ/current-sdk.cfg\`/bin
```

For a more persistent addition, open `.bash_profile` in a text editor:

```bash
$ touch ~/.bash_profile
$ open ~/.bash_profile
```

Then add the line below to the file and save the changes:

```bash
export PATH=$PATH:\`cat $HOME/Library/Application\ Support/Garmin/ConnectIQ/current-sdk.cfg\`/bin
```

## Windows Installation

1. [Install the Connect IQ SDK Manager](https://developer.garmin.com/connect-iq/connect-iq-basics/getting-started/), download the SDK, and set the active SDK.
2. Point your `PATH` to the active Connect IQ bin directory in the command prompt:
```bash
> for /f usebackq %i in (%APPDATA%\Garmin\ConnectIQ\current-sdk.cfg) do set CIQ_HOME=%~pi
> set PATH=%PATH%;%CIQ_HOME%\bin
```

## Linux Installation

1. [Install the Connect IQ SDK Manager](https://developer.garmin.com/connect-iq/connect-iq-basics/getting-started/), download the SDK, and set the active SDK.
2. Point your `PATH` to the active Connect IQ bin directory in the command prompt:
```bash
$ export PATH=$PATH:\`cat $HOME/.Garmin/ConnectIQ/current-sdk.cfg\`/bin
```

For a more persistent addition, open `.bash_profile` in a text editor:

```bash
$ touch ~/.bash_profile
$ nano ~/.bash_profile
```

Then add the line below to the file and save the changes: CTRL-X

```bash
export PATH=$PATH:\`cat $HOME/.Garmin/ConnectIQ/current-sdk.cfg\`/bin
```

## Basic Commands

After installation, three new shell commands are available: `connectiq`, `monkeyc`, and `monkeydo`.

- `connectiq` launches the Connect IQ simulator, which can be used to run and test apps on your computer before running them on your device. In the simulator, your app will only have access to those APIs that are available on the currently simulated device. For example, an API only available in Connect IQ v2.2.x or higher, such as `PersistedContent`, will not be available on devices that run earlier versions of Connect IQ.
- `monkeyc` calls the Monkey C compiler. The compiler can take code from multiple files and link them together into a single Connect IQ executable (a PRG file). The usage is:
```bash
> monkeyc [-d <arg>] [-f <arg>] [-o <arg>] [-y <arg>]
```

| Argument | Definition |
| --- | --- |
| `-d <arg>` | Target device |
| `-f <arg>` | Jungle files |
| `-o <arg>` | Output file to create |
| `-y <arg>` | to sign builds with |

**Note:** For more information on all the command line options, refer to the [Compiler Options](../overview/compiler-options.md) section in the Monkey C guide.

- `monkeydo` runs a Connect IQ executable in the simulator. You must have previously started the simulator with `connectiq`. The usage is:
```bash
monkeydo [executable] [device_id] [-n] [-t | -t test_name]
```

| Argument | Definition |
| --- | --- |
| `executable` | A Connect IQ executable (PRG) to run |
| `device_id` | The device to simulate (e.g. "fenix5plus") |
| `-n` | Runs the app in sensor native pairing mode |
| `-t` | Execute Run No Evil unit tests. Supply an optional test method or class name to only run that test or set of tests. |

Here is an example of a basic build and run cycle from the command line:

```bash
// Launch the simulator:
> connectiq

// Compile the executable:
> monkeyc -d fenix5plus -f /path/to/monkey.jungle -o project_name.prg -y /path/to/Dev_Key

// Run in the simulator
> monkeydo myApp.prg fenix5plus
```

**Note:** For more information on the `-f` option and the Jungle build framework, see the [Overriding Resources](jungle-reference.md#jungle-reference-guide) section of this guide.

## Generating a Key Using OpenSSL

If you're working from the command line you can generate a RSA key using [OpenSSL](https://www.openssl.org/). The following command will generate a valid signing key.

```bash
> openssl genrsa -out developer_key.pem 4096
> openssl pkcs8 -topk8 -inform PEM -outform DER -in developer_key.pem -out developer_key.der -nocrypt
```

This developer key, `developer_key.der`, is passed to the compiler using the `-y` command line option.
