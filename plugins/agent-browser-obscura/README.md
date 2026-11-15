# agent-browser-obscura

A Claude Code skill for browser tasks with [agent-browser](https://github.com/vercel-labs/agent-browser) on the [Obscura](https://github.com/h4ckf0r0day/obscura) headless engine, with stealth on, falling back to Chrome only when Obscura cannot do the job. It replaces the upstream `agent-browser` skill, so this one plugin is all you need.

## What it does

The skill (`agent-browser-obscura`) tells Claude to:

- **Load the version-matched guide** with `agent-browser skills get core` (and its references or the specialized skills such as `electron`, `slack`, `dogfood`) instead of relying on a copy that goes stale — the same approach as the upstream skill, whose triggers it also covers.
- **Check the setup** once per task (agent-browser 0.39.0+ and `obscura` on `PATH`) and use Chrome, telling you once, when it is missing.
- **Pin one deterministic named session** per worktree (`agent-browser session id --scope worktree --prefix agent-temp`), never the shared default session, and keep one browser in it.
- **Write every command** as `AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser --session <name> --engine obscura …`, because any command can be the one that launches the browser (first use, after the one-hour idle timeout, after a `close`), and a launch without these parts silently gives Chrome without stealth.
- **Fall back to Chrome** inside the same session (`--engine chrome` on every command) for headed mode, profiles, saved state, extensions, CJK text in screenshots, WebGL/WebGPU, and pages Obscura renders empty — but not for bot walls, where headless Chrome does worse.
- Handle `localhost` (`OBSCURA_ALLOW_PRIVATE_NETWORK=1`), locale-sensitive pages (`OBSCURA_TIMEZONE`), tracker blocking, `NO_PROXY`, one-shot reads with `obscura fetch --dump markdown`, and the quirks you will see.

### Why Obscura by default

Measured on Linux with agent-browser 0.43.0 and Obscura 0.2.7 (stealth build). The figures are the summed PSS of the browser processes.

| Page | Chrome (headless) | Obscura |
|---|---|---|
| example.com | 312 MB, 17 processes | 50 MB, 1 process |
| Content-heavy pages | 410–566 MB | 199–244 MB |
| Four tabs | 786 MB | 541 MB |

Bot walls: some sites that blocked headless Chrome served Obscura with stealth. Some sites blocked both.

## Installation

Requirements:

1. agent-browser 0.39.0 or later: `npm install -g agent-browser@latest`, then `agent-browser install` for the Chrome fallback.
2. The Obscura binary on `PATH`. Download the archive for your platform from the [releases page](https://github.com/h4ckf0r0day/obscura/releases) — the `-stealth` builds add TLS impersonation and tracker blocking — and keep `obscura-worker` next to `obscura`:

   ```bash
   curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-linux-stealth.tar.gz
   tar xzf obscura-x86_64-linux-stealth.tar.gz
   install -m 755 obscura obscura-worker ~/.local/bin/
   ```

Then install the plugin, and uninstall the upstream `agent-browser` plugin if you have it, so the two skills do not compete:

```
/plugin marketplace add rishubil/skills
/plugin install agent-browser-obscura@rishubil-skills
```

## Usage

Ask Claude for a browser task as usual ("open this page and check the login flow"). The commands it runs look like this:

```bash
agent-browser session id --scope worktree --prefix agent-temp   # agent-temp-5e934c5df6e6
AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser --session agent-temp-5e934c5df6e6 --engine obscura open https://example.com
agent-browser --session agent-temp-5e934c5df6e6 session info   # shows "Engine: obscura"
```

To skip permission prompts for these commands, allow both forms in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(agent-browser:*)",
      "Bash(AGENT_BROWSER_OBSCURA_STEALTH=1 agent-browser:*)"
    ]
  }
}
```

## Source

- [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — the upstream `agent-browser` skill (`skills/agent-browser/SKILL.md`), whose triggers and "load the guide from the CLI" approach this skill adopts, and the experimental `--engine obscura` option (0.39.0+, [engine page](https://agent-browser.dev/engines/obscura)).
- [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) — the engine; its `skills/obscura/SKILL.md` and docs are the source for the stealth, fingerprint, tracker-blocking, `fetch --dump`, and limitation notes. This plugin does not bundle Obscura.

Both are Apache-2.0. See [`skills/agent-browser-obscura/NOTICE.md`](skills/agent-browser-obscura/NOTICE.md).
