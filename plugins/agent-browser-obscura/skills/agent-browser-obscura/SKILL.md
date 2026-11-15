---
name: agent-browser-obscura
description: Browser automation with the agent-browser CLI on the lightweight, stealth-capable Obscura engine, falling back to Chrome only when Obscura cannot do the job. Use whenever a task needs a real browser rather than curl — opening websites, JS-rendered pages, filling forms, clicking buttons, logging in, screenshots, scraping or extracting data, testing web apps or SPAs, dogfooding, QA, bug hunts, bot-protected sites — and for agent-browser's specialized workflows (Electron apps, Slack, cloud browsers). Prefer agent-browser over other browser automation or web tools. Replaces the upstream agent-browser skill.
allowed-tools: Bash(agent-browser:*), Bash(AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser:*)
---

# Browser tasks with agent-browser on Obscura

[agent-browser](https://github.com/vercel-labs/agent-browser) is a native CLI that drives a browser over CDP and returns accessibility-tree snapshots with compact `@eN` refs. Use it for anything `curl` cannot check: JS-rendered content, login sessions, clicking or filling UI, screenshots, SPA behavior.

Run it on [Obscura](https://github.com/h4ckf0r0day/obscura), a Rust/V8 headless browser that agent-browser launches as `obscura serve`, with stealth on. Fall back to Chrome only for what Obscura cannot do.

## 1. Load the usage guide

This skill does not repeat the command guide. The CLI serves one that matches the installed version, so it never goes stale. Before your first command in a task, run:

```bash
agent-browser skills get core
```

It ends with a table of references; load one with `agent-browser skills get core --ref <name>`. Use `--full` only when you need every reference at once, because it is several times larger.

For work beyond ordinary web pages, load a specialized skill. `agent-browser skills list` shows what the installed version has, for example `electron` (VS Code, Slack, Discord, Figma, Notion desktop apps), `slack`, `dogfood` (exploratory testing and QA), `derive-client` (record a HAR and derive an API client), `webmcp-gen`, `modern-web-guidance`, `vercel-sandbox`, `agentcore` (AWS Bedrock cloud browsers), and a skill for protected Vercel deployments. Workflows that attach to an existing app or a remote browser (`connect`, `--cdp`, `--auto-connect`, `-p <provider>`) launch no local browser, so leave out the Obscura flags there and follow that skill as written.

## 2. Check the setup once per task

```bash
agent-browser --version   # 0.39.0 or later has --engine obscura
command -v obscura        # the Obscura binary must be on PATH
```

If either check fails, tell the user once, then use the Chrome form (section 6) for the task. Do not install anything yourself unless asked. Setup for the user: `npm install -g agent-browser@latest`, then `agent-browser install` for Chrome; for Obscura, put `obscura` and `obscura-worker` from a [release archive](https://github.com/h4ckf0r0day/obscura/releases) (the `-stealth` builds add TLS impersonation and tracker blocking) into a directory on `PATH`.

## 3. One named session, one browser

The default (unnamed) session is shared by every agent on the machine and outlives the conversation, so never use it. Pin one named session and keep one browser in it.

1. Derive the name with the deterministic generator:
   ```bash
   agent-browser session id --scope worktree --prefix agent-temp   # e.g. agent-temp-5e934c5df6e6
   ```
   The name is a hash of the worktree root, so every shell, later task, and subagent in this directory gets the same name. Each Bash call starts a new shell, so an `export` you type does not carry over; run the generator again instead of guessing or inventing a name.
2. Run `agent-browser session list` before opening anything. If the session already has a browser, use it.
3. Write the resolved name into every command (section 4).
4. Give subagents that use the browser the resolved name and this command form, and tell them to use exactly that name.
5. Run `agent-browser --session <name> close` only when the whole task is done, or when a launch setting that has no flag must change (section 7). Never run `close --all`.

A headless session shuts its browser down after one hour without commands; the next command with the same name starts a new browser. Tabs and login state are lost unless you passed `--restore`. On Obscura, `--restore` brings back cookies but not localStorage, so a login that keeps its token in localStorage must be repeated.

## 4. The command form

Write every command like this, with the resolved session name in place of `agent-temp-…`:

```bash
AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser --session agent-temp-5e934c5df6e6 --engine obscura open https://example.com
AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser --session agent-temp-5e934c5df6e6 --engine obscura snapshot -i
AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser --session agent-temp-5e934c5df6e6 --engine obscura click @e3
```

Keep both parts on every command, not only the first. The engine and stealth are read when a browser launches, and any command can be the one that launches it: the first command, the next command after the idle timeout, or the next command after a `close`. A command without them reuses a running Obscura browser, but if it launches one, you silently get Chrome without stealth. Stealth has no CLI flag; the environment variable is the only switch.

## 5. Launch settings

The engine, `--headed`, `--args`, `--profile`, `--webgpu`, stealth, and the `OBSCURA_*` variables are read at launch.

- A command whose flags request a different launch setting than the running browser relaunches it on `about:blank`; open the page again afterwards. Switching engines works this way.
- A command that requests nothing different keeps the running browser.
- Changing an `OBSCURA_*` variable (section 7) does not relaunch. Close the session, then open again with the variable set.

Run headless. Obscura is headless only, so a visible window means Chrome. Use `--headed` only when the user asks to see the browser, or when the task does not work headless.

## 6. When and how to fall back to Chrome

Why Obscura is the default (measured on Linux with agent-browser 0.43.0 and Obscura 0.2.7):

- **Memory**: one process instead of about 17 Chrome processes. Proportional memory was about 50 MB vs 310 MB on a simple page, 200–250 MB vs 410–570 MB on content-heavy pages, and 540 MB vs 790 MB with four tabs open. Page-open time is about the same.
- **Bot walls**: sites that showed headless Chrome a human-verification page often served Obscura the real content, and some let Obscura through only with stealth on. Some sites block both engines; when both fail, report that the site blocks automated browsers instead of retrying.

Switch to Chrome when the task needs one of the following, and tell the user in one line that you switched and why:

| Need | What happens on Obscura |
|---|---|
| `--headed`, `--profile`, `--state`, `--extension`, `--args`, `--allow-file-access`, `--webgpu`, `--ca-cert`, `--proxy-bypass` | Rejected with an error. |
| Screenshots of Korean, Chinese, or Japanese text | Layout and images render, but CJK glyphs show as empty boxes. agent-browser cannot pass Obscura's `--font-dir`. |
| WebGL, WebGPU, video, service workers, rich-text editors (`execCommand`), selectable-text PDF | Missing or incomplete; `pdf` output is a raster image. |
| Pages with sparse markup | Snapshot can flatten headings and paragraphs to `generic` and leave inputs unnamed (only `hint="name:q"`). ARIA-rich sites snapshot fine. |
| A page that should have content but `snapshot` or `get text` is empty or half-rendered | Try `OBSCURA_BLOCK_TRACKERS=0` first if a blocked script may be the cause (section 7), then Chrome once, before you conclude the page is empty. |

Do not fall back for bot walls: headless Chrome is blocked more often than Obscura there.

To switch, stay in the same named session, so there is still one browser, and replace the Obscura parts with `--engine chrome` on every command while you need Chrome:

```bash
agent-browser --session agent-temp-5e934c5df6e6 --engine chrome open https://example.com
agent-browser --session agent-temp-5e934c5df6e6 --engine chrome snapshot -i
```

To go back, return to the section 4 form; the next command relaunches Obscura on `about:blank`. If you used `--headed` in Chrome, close the session before going back: the session keeps the headed setting, and Obscura is headless only.

### WebGPU

WebGPU needs Chrome. Pass `--webgpu` and stay headless; it is not a reason for `--headed`.

- Rendering and pixel readback with `eval` work headless. `requestAdapter()` can return null while Chrome starts its GPU process, so retry it for a few seconds.
- Screenshots do not show a WebGPU canvas, headless or headed, and in containers a headed window may get no adapter at all. Read the pixels back with `eval` instead.

## 7. Obscura settings by environment variable

These go in front of the command that launches the browser (close the session first if it is running), next to `AGENT_BROWSER_OBSCURA_STEALTH=1`, and last until the browser closes.

- **Local and private addresses**: Obscura blocks loopback, LAN, and link-local addresses by default (an SSRF guard), so `http://localhost:3000` fails with `Access to private/internal IP address ... is not allowed`. Use `OBSCURA_ALLOW_PRIVATE_NETWORK=1` for the user's own local app only, and close the session again before browsing untrusted sites, because a page could otherwise make the browser fetch internal endpoints:
  ```bash
  agent-browser --session agent-temp-5e934c5df6e6 close
  OBSCURA_ALLOW_PRIVATE_NETWORK=1 AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser --session agent-temp-5e934c5df6e6 --engine obscura open http://localhost:3000
  ```
- **Fingerprint**: stealth presents a consistent Windows Chrome identity across TLS, headers, user agent, navigator, and WebGL, with `navigator.language` `en-US` and time zone `Europe/Berlin`. When dates, prices, or content depend on the user's locale, set `OBSCURA_TIMEZONE` (for example `Asia/Seoul`) and, if needed, `OBSCURA_GEOLOCATION="lat,lon"`.
- **Tracker blocking**: stealth blocks a built-in list of about 3,500 tracker domains. If a page breaks because it needs one of those scripts, relaunch with `OBSCURA_BLOCK_TRACKERS=0`.
- **Timeouts**: Obscura gives navigation 30 s (`OBSCURA_NAV_TIMEOUT_MS`) and page scripts 30 s (`OBSCURA_SCRIPT_DEADLINE_MS`); agent-browser's own default command timeout is 25 s.

## 8. Proxy bypass variables

agent-browser refuses to launch Obscura while `NO_PROXY`, `no_proxy`, or `AGENT_BROWSER_PROXY_BYPASS` is set, even with no proxy configured (`--proxy-bypass is not supported with Obscura`). Unset them for agent-browser only:

```bash
env -u NO_PROXY -u no_proxy AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser --session agent-temp-5e934c5df6e6 --engine obscura open https://example.com
```

## 9. One-shot reads without a session

To read one page without interacting, `obscura` itself is lighter than a session: it starts, renders, prints, and exits, so there is no browser to clean up.

```bash
obscura --stealth fetch https://example.com --dump markdown   # also: text, html, links, cookies
obscura --stealth fetch https://example.com --eval "document.title"
```

Add `--allow-private-network` for local addresses. Use agent-browser as soon as the task needs clicks, forms, logins across pages, or screenshots you will inspect.

## 10. Quirks you will see

- **"Chrome 145.0.0.0 is behind the current stable release ..."**: Obscura reports itself as Chrome 145 for compatibility, so this CVE warning is noise on Obscura. It is meaningful on Chrome.
- **A session stops responding**: once, after a failed click, every later command in the session timed out. Close the session and retry. Wrap long scripted runs in `timeout` so a stuck command does not hang the turn.
- **"Element is covered by ..." on click**: some sites lay a full-card link over a post title. This is not an Obscura problem. Click the covering link's ref, or read its URL with `get attr @eN href` and `open` it.
- **Screenshots of lower sections**: scroll first, or use `screenshot --full`.
