---
name: discord-notify
description: >
  Send a short notification to the user's Discord channel through an incoming
  webhook when something genuinely needs their attention away from the terminal
  — long-running work finished, you are blocked and cannot proceed, or a
  build/deploy/test run failed. Use this whenever the user asks to be pinged,
  notified, messaged, or DM'd on Discord ("ping me when the deploy is done",
  "let me know on Discord if it breaks", "작업 끝나면 디스코드로 알려줘"), and
  whenever a standing notification request they made earlier in the session
  comes due. This skill is deliberately conservative: it exists to send a small
  number of high-value pings, never a stream of progress updates.
---

# Notify the user on Discord

The terminal is only useful when someone is looking at it. This skill covers
the other case: the user walked away, and something happened that they would
want to know about now rather than in twenty minutes.

That framing sets the whole bar. A Discord notification interrupts a person —
possibly on their phone, possibly in a channel other people can read. It is
worth spending when it saves them from staring at a finished job, or from
waiting on a run that died five minutes in. It is worth nothing when it tells
them what they can already see on the screen in front of them.

## Prerequisites

- A Discord **incoming webhook URL** for the channel the user wants pinged.
  The script resolves it in this order: the `--webhook` option, the
  `DISCORD_WEBHOOK_URL` environment variable, then the 1Password CLI
  (`op item get "Discord Webhook URL"`, field: password). You never pass the
  URL yourself — let the script find it.
- `curl` and `jq` on PATH.

If nothing resolves, the script fails with a clear message. Relay it: the user
needs to export `DISCORD_WEBHOOK_URL` or store the webhook in 1Password. Do not
ask them to paste the URL into the chat — it is a credential, and anyone
holding it can post to that channel.

## The rule that prevents spam: notifications are authorized, not assumed

**Send only when the user has asked to be notified.** Their request is what
makes the ping welcome; without it you are pushing an unsolicited message into
a channel on their behalf. The request can be:

- **Immediate** — "run the migration and ping me on Discord when it's done."
- **Standing, from earlier in the session** — "from now on tell me on Discord
  whenever a build fails." Honour it until they say otherwise, but only for the
  events they named.
- **Configured** — the project's `CLAUDE.md` or their user config says to
  notify on certain events.

If none of those apply and you still think something warrants a ping — a
two-hour job just finished and they have been silent since starting it, a
deploy is failing in a way that costs money — **offer instead of sending**:
"이건 디스코드로 알려드릴까요?" one line in the terminal. If they are away they
will see it when they return, which is exactly where the information belonged
anyway. If they say yes, that is your authorization, and it usually becomes a
standing one for the rest of the session.

This single rule does most of the anti-spam work, because unrequested pings are
where spam actually comes from. The rest of the guidance below is about not
abusing an authorization once you have it.

## When a ping is worth sending

Within an authorization, weigh three things:

1. **Is the user away?** If they sent you a message a moment ago, they are at
   the keyboard and your terminal reply already reached them. A notification on
   top of it is pure duplication. Pings are for work that ran while nobody was
   watching.
2. **Is it terminal or actionable?** The work is finished, or it is stuck and
   needs a human decision, or it failed. Something that changes what the user
   does next. "Step 3 of 7 complete" changes nothing.
3. **Is it the whole story?** If five things finished, that is one notification
   listing five lines, not five notifications. Wait until you actually know the
   outcome instead of narrating your way to it.

Good reasons to send:

- A long build, test suite, migration, deploy, or batch job finished — success
  or failure.
- You are blocked and cannot continue without the user: a decision, a
  credential, a permission they have to grant, an ambiguity you should not
  guess at.
- Something broke in a way that keeps costing something while it stays broken.

Never send:

- Progress updates, heartbeats, "still working on it", "starting now".
- Anything the user can see in the terminal in the same breath.
- Routine successes that were the obvious expected outcome of a short command.
- A second message repeating a notification you already sent, reworded.
- Secrets, tokens, API keys, `.env` contents, or customer data. Assume other
  people can read the channel.
- Long logs or file dumps. Send the two lines that matter and let the user come
  back to the terminal for the rest.

## Self-imposed limits

There is no rate limiter in the script — restraint is yours to exercise, so
hold these lines deliberately:

- **At most one notification per turn.** If you are about to send a second one,
  the two belong in a single message.
- **One notification per event.** Not one when it starts and one when it ends;
  just the end.
- **A handful per session, not a stream.** If you have already sent three and
  are reaching for a fourth, that is a signal that you are narrating rather than
  reporting. Stop and ask the user whether they still want these.
- **Never retry a failed send.** The script does not retry either, on purpose —
  a duplicate ping is worse than a missed one. Report the failure in the
  terminal and move on.

## The script

Everything goes through the bundled script:

```
<path-to-this-skill>/scripts/discord-notify.sh
```

Run it with `--help` for the full list. The common shape:

```bash
discord-notify.sh --title "Deploy finished" --color green "staging is live — 42 tests passed, took 6m12s"
```

| Need | Option |
| --- | --- |
| Headline | `--title "Build failed"` (clipped at 256 chars) |
| Colour by outcome | `--color green\|red\|yellow\|blue\|orange\|gray` or `#RRGGBB` |
| Small context line | `--footer "myproject · main"` |
| Override the webhook's display name | `--username "claude-code"` |
| Plain message, no embed box | `--plain` |
| Check the payload without sending | `--dry-run` |

The body is the first positional argument, or stdin if you pipe into it:

```bash
make test 2>&1 | tail -20 | discord-notify.sh --title "Tests failed" --color red
```

Literal `\n` in the body becomes a real newline, so multi-line summaries are
easy to pass as one argument.

Two things the script enforces for you: mentions are always suppressed (a body
containing `@everyone` will not ping anyone), and it refuses to POST to
anything that is not a Discord webhook host, so a misconfigured variable cannot
leak the message elsewhere.

### Exit codes

| Code | Meaning | What to do |
| --- | --- | --- |
| 0 | Sent | Mention it briefly in the terminal. |
| 1 | Bad usage or missing config | Fix the invocation, or relay the config problem to the user. |
| 3 | Discord rate-limited you (429) | **Do not retry.** You are sending far too often — say so in the terminal and stop notifying. |
| 4 | Discord rejected the request | Read the message; usually a malformed payload or a dead webhook. Report it, do not retry. |
| 5 | Could not reach Discord | Network problem. Report it in the terminal. Do not retry. |

## Writing the message

The user is reading this on a phone, out of context, minutes or hours later.
Two things have to survive that: **which project** and **what now**.

- **Title**: what happened, in a few words. "Deploy failed", "Migration
  finished", "Needs your decision".
- **Body**: the outcome and the next action, in one to three short lines. If
  something failed, include the actual error line, not "an error occurred".
- **Footer**: the project or directory name, so a user with three sessions open
  knows which one this is.
- **Colour** carries the outcome at a glance: green for success, red for
  failure, yellow for needs-attention/blocked, blue for neutral info.
- Write in the language the user has been speaking.

Keep it short. The notification's job is to get them to the terminal, not to
replace it.

## Examples

**Example 1 — requested completion ping**

User: "이 마이그레이션 돌려놓고 끝나면 디스코드로 알려줘" → run it → when it
finishes:

```bash
discord-notify.sh --title "마이그레이션 완료" --color green \
  --footer "myapp · staging" \
  "3개 테이블 마이그레이션 성공, 12분 소요.\n다운타임 없었습니다."
```

**Example 2 — failure under a standing request**

User earlier: "빌드 깨지면 알려줘." The build breaks:

```bash
discord-notify.sh --title "빌드 실패" --color red --footer "myapp · main" \
  "tsc: src/api/client.ts:88 — Property 'retries' does not exist on type 'Config'.\n커밋 4a1f2b 이후 처음 실패."
```

One message, with the real error in it. Not one saying "빌드가 실패했어요" and a
second one with the details.

**Example 3 — blocked, needs a decision**

Mid-way through authorized long work, you hit a fork you should not guess at:

```bash
discord-notify.sh --title "결정이 필요합니다" --color yellow --footer "myapp" \
  "prod DB 스키마가 예상과 다릅니다. 마이그레이션을 중단하고 대기 중입니다.\n롤백할까요, 아니면 스키마에 맞춰 조정할까요?"
```

**Example 4 — no authorization yet**

A 40-minute test run you started finishes; the user never asked to be pinged.
Do not send. Say in the terminal: "테스트가 끝났습니다 (전부 통과). 앞으로 이런
건 디스코드로 알려드릴까요?" — and if they say yes, treat it as standing
authorization from then on.
