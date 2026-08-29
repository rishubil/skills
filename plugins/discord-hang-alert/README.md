# discord-hang-alert

A Claude Code plugin that pings you on Discord when a session is **blocked
waiting for you** — so a session never sits hung while you are away from the
terminal.

## What it does

Claude Code stops and waits whenever it needs a human: a tool needs your
approval, a subagent needs input, an MCP server opens an elicitation dialog.
If you have stepped away, that wait costs you the whole time until you happen
to look back at the terminal.

This plugin registers a `Notification` hook that fires on exactly those
blocking events and sends one short Discord webhook message:

> **Waiting for your permission**
> Claude Code is blocked and cannot continue until you respond.
> Project: `myapp`
> `/home/you/work/myapp · a1b2c3d4`

**This is not a progress reporter.** It fires only when the session is
genuinely stuck on you. Completion notices, progress updates, and idle
notifications are deliberately out of scope — if you want the agent to tell
you when work *finishes*, use the separate `discord-notify` plugin.

### Which events trigger it

The hook matches these `notification_type` values:

| Type | Meaning |
| --- | --- |
| `permission_prompt` | A tool call is waiting for your approval |
| `agent_needs_input` | A subagent needs input from you |
| `elicitation_dialog` | An MCP server is asking for input |
| `elicitation_url_dialog` | An MCP server is asking you to open a URL |

Deliberately **excluded**: `idle_prompt` (fires while you are simply reading
the terminal) and `agent_completed` (that is a completion notice, and it would
fire on every turn).

## Setup

Create an incoming webhook for the channel you want pinged (Discord → Server
Settings → Integrations → Webhooks → New Webhook → Copy Webhook URL), then
make it available in any one of these ways:

```bash
export DISCORD_HANG_ALERT_WEBHOOK_URL="https://discord.com/api/webhooks/..."
```

or reuse the shared `DISCORD_WEBHOOK_URL` variable, or write the URL into a
file — useful because a hook only sees the environment Claude Code itself was
launched with:

```bash
mkdir -p ~/.config/discord-hang-alert
printf '%s\n' "https://discord.com/api/webhooks/..." > ~/.config/discord-hang-alert/webhook
chmod 600 ~/.config/discord-hang-alert/webhook
```

Until a webhook resolves, the plugin is completely inert — it logs
`no webhook configured` and does nothing.

Requires `curl` and `jq`.

### Verify your setup

```bash
~/.claude/plugins/.../discord-hang-alert/scripts/discord-hang-alert-hook.sh --self-test
```

It prints the state directory, the cooldown, which config source won, and the
webhook **host** (never the full URL), then sends one test notification and
reports the result.

## Safety and anti-spam

A hook fires automatically with no model in the loop, so the limits are
mechanical rather than advisory:

- **Cooldown per session** — at most one notification per session every
  `DISCORD_HANG_ALERT_COOLDOWN` seconds (default 300). The timestamp is
  recorded only after a *successful* send, so a failed send never starts a
  cooldown that swallows the next real alert.
- **No retries** — a duplicate ping is worse than a missed one.
- **No session content ever leaves the machine.** The message carries only the
  notification type and the working directory. The hook never reads the
  transcript and never includes tool arguments, code, or output.
- **Mentions are always suppressed** (`allowed_mentions.parse: []`).
- **Non-Discord webhook hosts are refused** before any request is made, and
  the URL is never written to a log — only its host, for diagnosis.
- **It can never break your session.** Claude Code ignores a `Notification`
  hook's exit code and stderr entirely, and every failure path in the script
  logs and exits 0. `curl` is capped at 5 seconds and the hook at 10.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `DISCORD_HANG_ALERT_WEBHOOK_URL` | — | Webhook URL (highest priority) |
| `DISCORD_WEBHOOK_URL` | — | Webhook URL, shared with `discord-notify` |
| `DISCORD_HANG_ALERT_COOLDOWN` | `300` | Seconds between alerts for one session |
| `DISCORD_HANG_ALERT_USERNAME` | `Claude Code` | Webhook display name |
| `DISCORD_HANG_ALERT_DISABLE` | — | Set to `1` to turn the hook off entirely |
| `DISCORD_HANG_ALERT_DEBUG` | — | Set to `1` to dump the raw hook payload (see below) |

Config file locations, consulted only when the environment variables are unset:
`${CLAUDE_PLUGIN_DATA}/webhook`, then
`${XDG_CONFIG_HOME:-~/.config}/discord-hang-alert/webhook`.

## Troubleshooting

Claude Code discards a `Notification` hook's stderr, so **the log file is the
only debugging surface**:

```bash
tail -20 "${XDG_STATE_HOME:-$HOME/.local/state}/discord-hang-alert/hang-alert.log"
```

(When the plugin is installed, the state directory is `${CLAUDE_PLUGIN_DATA}`
instead — `--self-test` prints the resolved path.)

Every invocation appends one line: `sent (permission_prompt) session=a1b2c3d4`,
`suppressed (cooldown, 240s remaining)`, `no webhook configured`,
`unparseable payload`, or `send failed: HTTP 401 ...`.

### On the undocumented payload

Claude Code's public hooks documentation specifies the `Notification` hook's
matcher values but **not** its stdin JSON schema. The script therefore reads
every field defensively (`.notification_type // .notificationType // empty`,
`cwd` falling back to `$PWD`) and degrades to a generic title rather than
failing when a field is missing or renamed.

If a Claude Code update changes the payload, set `DISCORD_HANG_ALERT_DEBUG=1`
and inspect the captured raw payload:

```bash
cat "<state dir>/last-payload.json"
```

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install discord-hang-alert@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install discord-hang-alert@rishubil-skills --scope project
```

## Hooks

| Event | Matcher | Script |
|---|---|---|
| `Notification` | `permission_prompt\|agent_needs_input\|elicitation_dialog\|elicitation_url_dialog` | `scripts/discord-hang-alert-hook.sh` (timeout 10s) |

## Scripts

| Path | Purpose |
|---|---|
| `scripts/discord-hang-alert-hook.sh` | Reads the `Notification` hook payload from stdin, maps the notification type to a human-readable title, and posts a single yellow Discord embed naming the situation and the project directory. Resolves the webhook from `DISCORD_HANG_ALERT_WEBHOOK_URL`, `DISCORD_WEBHOOK_URL`, `${CLAUDE_PLUGIN_DATA}/webhook`, or `~/.config/discord-hang-alert/webhook`; refuses non-Discord hosts; always sets `allowed_mentions.parse: []`; enforces a per-session cooldown recorded only after a successful send; never retries; and exits 0 on every path so it can never break a session. `--self-test` verifies the setup and sends a test message; `--help` documents every option. Requires `curl` and `jq`. |
