# self-kill-guard

A Claude Code plugin that blocks Bash commands which would kill the shell
running them — or Claude Code itself — before they run.

## What it does

Claude Code runs every Bash tool call as a fresh
`/bin/zsh -c '<preamble> && <the entire command text>'` process, so that
shell's own `/proc/<pid>/cmdline` contains the full command text. `pkill -f
uvicorn` matches by *full command line*, not just the process name — so it
matches its own shell first (the pattern `uvicorn` is sitting right there in
the command it was typed into) and kills it before the intended target is
ever reached. There is no error to read, because the process that would have
reported the result is the one that died.

This was verified directly on this machine: `pgrep -af SOMETOKEN` matches the
very shell running the command that contains `SOMETOKEN`, confirming that any
`pkill -f`/`pgrep -f`/`ps | grep` chain built from a token present in its own
invocation is self-targeting.

This plugin adds a `PreToolUse` hook on the `Bash` tool that catches this
class of mistake — and the related one of killing Claude Code's own process
tree — before the command runs.

## What it catches

| Shape | Checked against |
| --- | --- |
| `pkill PATTERN` | Full command line if `-f`/`--full` is present, otherwise process name |
| `pgrep PATTERN \| ... kill` or `kill $(pgrep PATTERN)` / `` kill `pgrep PATTERN` `` | Same as `pkill`, since it feeds a kill either way |
| `ps ... \| grep PATTERN \| ... \| kill` | Full command line (what `ps` would list) |
| `pkill NAME` / `killall NAME` | Process name only — `killall` has no `-f` on either psmisc or BSD |

In every case the check is the same question: does `PATTERN` actually match
the command's own text, an ancestor process's command line (Claude Code, its
node runtime, other ancestors of this session, ...), the shell wrapper's
fixed strings (`shell-snapshots`, `NO_EXTENDED_GLOB`, ...), or a protected
process name (`zsh`, `bash`, `node`, `claude`, ...)? If none of those match,
nothing is blocked.

Only tokens in **command position** are treated as an invocation — the word
`pkill` inside an argument (an `echo`, a commit message, a heredoc) is not a
`pkill` call and is never flagged. A prefix like `sudo pkill ...` or
`xargs pkill ...` still counts as command position, so those are still caught.

Name matching has an asymmetry worth knowing, because it's the reason the
guard catches more than a naive reader would expect: `pkill`/`pgrep` do a
**partial** regex search against the process name unless `-x`/`--exact` is
given (so `pkill nod` really does hit `node` — this is documented pkill(1)
behaviour, not a guess), while `killall` matches the name **exactly** by
default and only becomes a regex search with `-r`/`--regexp`. `pidof` always
matches a literal program name exactly. Each shape carries its own default in
the code specifically so this asymmetry isn't "corrected" into a bug later.

## What it lets through

This is not a blacklist of `pkill -f` / `killall` — it is a match test, and a
pattern that provably does not hit anything at risk is let through:

- **`pgrep -af foo`** on its own — never flagged. This is the recommended
  first step, and it is completely safe by itself; only a `pgrep`/`pidof`
  whose output visibly feeds a `kill` (a pipe, or `$(...)`/`` `...` ``) is
  checked.
- **`kill 123 456`** — literal PIDs never match anything by pattern.
- **`pkill -f 'uvicor[n]'`** — the classic bracket trick. The regex
  `uvicor[n]` only matches the literal substring `uvicorn`, and the command's
  own text contains `uvicor[n]` (with a `[` and `]` in it), not `uvicorn` — so
  it does not self-match.
- **Any pattern that genuinely does not occur** in the command text, in an
  ancestor process's command line, or in a protected process name.
- **The word `pkill` (or `pgrep`, `killall`, `grep`) appearing as an
  argument** — inside an `echo`, a commit message, a heredoc, any quoted
  string — is not treated as an invocation at all. Only a token in command
  position (the actual command being run, optionally behind `sudo`, `xargs`,
  `env FOO=bar`, and the like) counts.
- **`pkill -x nod`** — `-x`/`--exact` requires the process name to match
  exactly, and `nod` is not `node`.
- **`killall nod`** — `killall` is exact by default (no `-x` needed, and it
  has no `-f`), so a substring like `nod` does not match `node`.

## Known limitations

The guard reasons about the **pattern operand** a command would search with.
Commands that take this session down *without* a pattern fall outside that
model and are **not** blocked:

| Command | Why it is missed |
| --- | --- |
| `pkill -u $USER`, `killall -u $USER` | `-u` consumes its value and leaves no pattern operand, so there is nothing to test — yet it kills every process of that user, Claude Code included |
| `kill -9 -1` | Signals every process the user can signal; no pattern is involved |
| `kill -9 $PPID` | Targets a PID, not a pattern. In a Bash tool call the shell's parent *is* the Claude Code process |
| `pkill -t <tty>`, `pkill -P <pid>` | Selects by terminal or parent PID; whether that set covers this session cannot be decided from the command text |

These are genuine gaps in something called a self-kill guard, so they are
named here rather than left for someone to find the hard way. Denying `-u`
when its value is the *current* user, and denying the `kill -1` / `kill 0`
whole-group forms, would be a reasonable extension. `-t` and `-P` probably
cannot be judged without guessing, which is why nothing is attempted there.

## Decisions

- **deny** — an invocation self-matches a protected target. Reported as exit
  0 with `permissionDecision: "deny"` in the hook's stdout JSON, not exit 2.
  Exit 2's reason is delivered as raw stderr and cannot be structured or
  overridden; exit 0 + JSON lets Claude Code render a proper decision and
  reason.
- **ask** — the pattern comes from a variable or command substitution
  (`$VAR`, `` `cmd` ``) that cannot be resolved ahead of time, so its safety
  cannot be verified.
- **silent pass** — nothing is printed and the command proceeds untouched.

A bug in this guard must never block every Bash call in the session: the
whole analysis is wrapped in a `try`/`except` that exits 0 with no output on
any unexpected error.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `SELF_KILL_GUARD_DISABLE` | — | Set to `1` to disable the guard entirely (exit 0, no output, on every call) |

## Testing it

Use `--check` to evaluate a command string directly without going through
the hook payload. It never blocks anything for real — it only prints the
verdict and the JSON that would be emitted, and always exits 0:

```bash
./scripts/self-kill-guard-hook.sh --check 'pkill -f uvicorn'
```

Never actually run a `pkill -f`/`pgrep -f ... | xargs kill` command to test
this plugin — pass it as a quoted argument to `--check` instead, or it may
kill the shell you are testing from.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install self-kill-guard@rishubil-skills
```

Or install into a specific project's `.claude/settings.json` from the command line:

```bash
claude plugin marketplace add rishubil/skills --scope project
claude plugin install self-kill-guard@rishubil-skills --scope project
```

## Hooks

| Event | Matcher | Script |
|---|---|---|
| `PreToolUse` | `Bash` | `scripts/self-kill-guard-hook.sh` (timeout 10s) |

## Scripts

| Path | Purpose |
|---|---|
| `scripts/self-kill-guard-hook.sh` | Dispatcher: tries `uv`, then `python3`, then `python` (3.x). If none is found it fails open — prints a note to stderr and exits 0 rather than breaking every Bash call for the rest of the session. |
| `scripts/self-kill-guard-hook.py` | Hook logic: extracts the pattern operand from `pkill`/`pgrep`/`ps \| grep`/`killall` invocations, tests it against the command's own text, ancestor process command lines, the shell wrapper's fixed strings, and protected process names, and emits a `deny`/`ask` decision as `hookSpecificOutput` JSON. Also serves `--check` and `--help`. |

## Runtime requirements

- One of [`uv`](https://docs.astral.sh/uv/) (preferred), `python3`, or
  `python` at version 3.x.
- `ps`, for ancestor process detection — this is what lets the guard
  recognize `pkill node` / `killall node` / `pkill -f claude` as hitting
  Claude Code's own process tree. It is optional in the sense that the guard
  degrades gracefully (empty ancestor list) if `ps` is missing or fails; the
  command-text check, which is the dominant and most reliable case, does not
  depend on it at all.
