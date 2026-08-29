# discord-notify

A Claude Code plugin that lets the agent ping you on Discord — through an
incoming webhook — when something actually needs your attention away from the
terminal.

## What it does

The terminal is only useful when someone is looking at it. This skill covers
the other case: you walked away, and a long build finished, a deploy broke, or
the agent hit a decision it should not make on its own.

When triggered, the skill:

1. **Checks that a notification is authorized.** It sends only when you asked
   to be notified — right now, or as a standing request earlier in the session
   ("build 깨지면 알려줘"), or via project config. Otherwise it offers in the
   terminal instead of pushing an unsolicited message into your channel.
2. **Decides whether the ping is worth it** — is the work terminal or blocked,
   are you plausibly away, is this the whole story rather than a progress tick.
3. **Writes a message that survives being read on a phone** — a title, one to
   three lines with the actual outcome or error, a footer naming the project,
   and a colour that carries the result at a glance (green / red / yellow).
4. **Sends it once** via the bundled `discord-notify.sh` script, and never
   retries a failed send.

### The no-spam policy

A Discord notification interrupts a person, possibly in a channel other people
can read. The skill treats that as expensive, and holds these lines:

- No notification without your request — standing or immediate.
- At most one per agent turn, one per event, a handful per session.
- Never progress updates, heartbeats, or anything already visible in the
  terminal.
- Never retried, because a duplicate ping is worse than a missed one.
- Never secrets, tokens, `.env` contents, or long log dumps.

Two guarantees are enforced by the script rather than by judgment: **mentions
are always suppressed** (a message containing `@everyone` cannot ping anyone),
and the script **refuses to POST to any non-Discord host**, so a misconfigured
variable cannot leak message content elsewhere.

## Setup

Create an incoming webhook for the channel you want pinged (Discord → Server
Settings → Integrations → Webhooks → New Webhook → Copy Webhook URL), then make
it available to the script in either way:

```bash
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
```

or store it in 1Password as an item named **`Discord Webhook URL`** with the URL
in the password field — the script falls back to `op` when the environment
variable is unset.

Requires `curl` and `jq`.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install discord-notify@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install discord-notify@rishubil-skills --scope project
```

## Usage

Trigger phrases include:

- "이 마이그레이션 돌려놓고 끝나면 디스코드로 알려줘"
- "ping me on Discord when the deploy is done"
- "빌드 깨지면 디스코드로 알려줘" (a standing request for the rest of the session)
- "let me know on Discord if the test suite fails"

You can also make it a project-wide default by putting the rule in your
`CLAUDE.md` — for example: *"When a build or deploy fails, notify me on
Discord."*

The script is usable on its own too:

```bash
plugins/discord-notify/skills/discord-notify/scripts/discord-notify.sh \
  --title "Deploy finished" --color green --footer "myapp · prod" \
  "staging is live — 42 tests passed, took 6m12s"
```

## Scripts

| Path | Purpose |
|---|---|
| `skills/discord-notify/scripts/discord-notify.sh` | Posts a message to a Discord incoming webhook via `curl` + `jq`. Sends a rich embed by default (`--title` / `--color` / `--footer`) or a plain message with `--plain`; body comes from the arguments or stdin, with literal `\n` converted to real newlines and every field clipped to Discord's limits (title 256, description 4000, footer 2048, plain content 1900) — with the description shrunk further when a long title or footer would push the embed past Discord's 6000-character total. Resolves the webhook URL from `--webhook`, then `DISCORD_WEBHOOK_URL`, then 1Password (`op item get "Discord Webhook URL"`) — never accepts it inline in a message. Always sets `allowed_mentions.parse: []` so `@everyone`/`@here` in a body cannot ping anyone, rejects any non-Discord webhook host before sending, and never retries. `--dry-run` prints the JSON payload without contacting Discord. Distinct exit codes separate a usage error (1) from a Discord rate limit (3), a rejected request (4), and an unreachable API (5). Requires `curl`, `jq`, and a webhook URL. |
