# self-kill-guard

A Claude Code plugin that blocks Bash commands which would kill the shell
running them — or Claude Code itself — before they run, and reminds the model
to re-check kill code it writes into files (see
[Write-time reminder](#write-time-reminder)).

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
`pkill` inside an argument (an `echo`, a commit message, a quoted string) is
not a `pkill` call and is never flagged. A prefix like `sudo pkill ...` or
`xargs pkill ...` still counts as command position, so those are still caught.
Which words really are command invocations is decided by a real shell
parser, see [How invocations are found](#how-invocations-are-found). So
`cd /tmp` + newline + `pkill -f x`, `if true; then pkill -f x; fi`, `! pkill -f
x`, `( pkill -f x )` and `echo $(pkill -f x)` are all caught, while `echo then
pkill -f x` and a heredoc that is only data are not.

Name matching has an asymmetry worth knowing, because it's the reason the
guard catches more than a naive reader would expect: `pkill`/`pgrep` do a
**partial** regex search against the process name unless `-x`/`--exact` is
given (so `pkill nod` really does hit `node` — this is documented pkill(1)
behaviour, not a guess), while `killall` matches the name **exactly** by
default and only becomes a regex search with `-r`/`--regexp`. `pidof` always
matches a literal program name exactly. Each shape carries its own default in
the code specifically so this asymmetry isn't "corrected" into a bug later.

## How invocations are found

The structural question (is `pkill`/`pgrep`/`killall`/`pidof`/`ps | grep |
kill`/`kill $(pgrep ...)` actually *run*, and with which argv) is answered by
[tree-sitter-bash](https://github.com/tree-sitter/tree-sitter-bash):

1. The command is parsed into an AST and flattened into one simple command per
   `;`-separated segment, with `|` between pipeline stages. Words are
   unquoted (`'a b'`, `"a b"` and `\x` all become their value); expansions
   (`$VAR`, `$(...)`) stay textual, so an unresolvable pattern still produces
   an **ask**. Comments and heredoc *data* never reach the matcher.
2. Everything that executes is found: `$(...)`, backticks, `<(...)`,
   subshells, `{ }`, `if`/`for`/`while`/`case` bodies, `!`, `&&`/`||`, and
   `$(...)` inside an unquoted heredoc body.
3. Code hidden in strings is parsed recursively (depth cap 5) when the
   receiving command is a shell interpreter: `bash|sh|zsh|dash|ksh -c '...'`,
   `eval ...`, and a heredoc or here-string (`<<`, `<<<`) fed to a shell,
   including `cat <<EOF | bash`. The interpreter may be given by path
   (`/bin/bash`) or sit behind prefixes (`sudo -E`, `env A=1`, `timeout 5`,
   `xargs`). Past the depth cap the text goes to the shlex heuristic.
4. Text tree-sitter cannot parse (an `ERROR` node: zsh-only syntax such as the
   glob qualifier in `ls **/*(.om[1]) && pkill -f x`, broken quoting) is handed
   to the shlex heuristic **for just that text** (fail closed), so it can
   never silently hide a `pkill`; the rest of the command still gets exact
   treatment.
5. The shape detection (`pkill`, `pgrep ... | kill`, `ps | grep | kill`,
   `killall`, ...) and the pattern matching run on this flattened form. The
   **self-match** test always uses the *original* command text, because that
   is what is in the running shell's cmdline.

If tree-sitter is not available (plain `python3`, dependencies not installed yet, no `uv`)
or `SELF_KILL_GUARD_PARSER=shlex` is set, the older **shlex heuristic** is
used for the whole command. It treats newlines, `if/then/do/{/!` and `(`/`)`
as command boundaries, blanks quote characters in heredoc bodies, and drops
comments, but it is only a heuristic and has known false positives and misses:

- `echo then pkill -f x` is denied (reserved words are accepted loosely).
- A heredoc body line starting with `pkill -f x` is denied even when it is
  only data (it cannot know whether the receiver is a shell).
- `echo ';' pkill -f x` is denied.
- It does not look inside quotes: `bash -c 'pkill -f x'`, `eval '...'`,
  `"$(pkill -f x)"` and `` `pkill -f x` `` are **missed**.

`--check` prints `parser=tree-sitter` or `parser=shlex` on the verdict line.

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

Static parsing cannot decide everything. These stay undecidable (the guard
passes or asks, as before):

- **Aliases and shell functions.** `alias k=pkill` then `k -f x`, or a function
  wrapping `pkill`, is not resolved (a function *body* is still scanned).
- **Commands built from variables.** `cmd=pkill; $cmd -f x` and `$PKILL -f x`
  have no literal command name.
- **Computed `eval`/`-c` strings.** Only literal arguments are parsed;
  `eval "$script"` or `bash -c "$(generate)"` cannot be inspected.
- **Text piped into a shell.** `echo 'pkill -f x' | bash` is not parsed (a
  *heredoc* piped into a shell is).
- **Scripts run from files.** `bash script.sh` is not read.
- **Patterns from variables or substitutions** are reported as **ask**, never
  resolved.

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

## Write-time reminder

The guard above only sees Bash commands. An agent can also *write* a script
(or any other file) that contains `pkill -f ...`, `pgrep ... | xargs kill`,
`ps | grep | kill`, `killall` or `pidof` and that kills its own shell, or
Claude Code, when it is run later. Whether that happens depends on how the
file is executed, which cannot be judged statically, so this part **never
blocks**. It adds a reminder to the model's context and leaves the decision to
the model.

**Triggers.** A `PostToolUse` hook on `Write`, `Edit` and `NotebookEdit`
(`scripts/write-reminder-hook.sh`) scans the text that was just written, line
by line, in **all file types** (including Markdown), for the words `pkill`,
`pgrep`, `killall`, `pidof` (word boundaries), a `ps ... | ... grep ... | ...
kill` chain, and `kill ... $(pgrep ...)` / backticks. `Write` scans `content`,
`Edit` scans `new_string` (never `old_string`), and for `NotebookEdit` every
string value of `tool_input` except the path fields is scanned (the content
field name is not documented).

**Heredocs in Bash.** With tree-sitter, a heredoc body that is only data
(`cat > x.sh <<'EOF'` ... `EOF`, or a here-string into a non-shell) is not
analysed as commands. When the Bash verdict is a plain pass and such a body
contains the same kill words, the `PreToolUse` hook adds the same reminder
(`additionalContext`, never a `permissionDecision`, so the normal permission
prompt is untouched). In shlex fallback mode heredoc bodies are already treated
as commands, so no reminder is added. `--check` prints it as a `--- REMIND ---`
section after a `PASS` first line.

**Message.** The model sees the file (or "this Bash command"), up to 10
matching lines (line number plus text trimmed to 160 characters, then "and N
more"), and a short checklist:

- a `-f` pattern matches full command lines, so it must not match the shell or
  command line that will run the file (including its arguments and the Bash
  tool command that invokes it) or Claude Code and its ancestors;
- run `pgrep -af PATTERN` first and kill the literal PIDs;
- the bracket trick (`myservic[e]`) hides a pattern from its own text;
- in tests and cleanup code, record PIDs (`$!`, pid files) and kill by PID or
  process group instead of by pattern;
- `killall NAME`, `pkill NAME` and `pidof NAME` match process names, and
  `node`, `bash`, `sh`, `zsh`, `python`, `claude` are dangerous;
- patternless kills (`kill -1`, `kill 0`, `pkill -u $USER`) are never safe.

It ends with the path of this README and states that it is a reminder, not an
error: if the code is already safe, nothing needs to change.

**Line numbers.** `Write` reports line numbers in `content`. For `Edit` the
hook reads the file from disk after the edit and locates `new_string`; if it is
found exactly once, absolute line numbers are reported, otherwise the numbers
are relative to the edited fragment and the message says so.

**De-duplication.** Within one session the same (file path, stripped line
text) is reported once; if only already-reported lines match, nothing is
printed. Bash heredocs use the fixed key `<bash-heredoc>`. State lives in
`${CLAUDE_PLUGIN_DATA:-${XDG_CACHE_HOME:-~/.cache}/self-kill-guard}` as
`reminded-*.json`, files older than 7 days are deleted, and any state error is
ignored (the reminder is then simply shown).

**Limitations.** It is a nudge, not a guarantee.

- `Edit` sees only the new fragment, not the rest of the file.
- Files changed through Bash (`sed -i`, `python`, `tee`, ...) are not seen,
  and heredoc detection covers only what tree-sitter classifies as data.
- Matching is by words, so it also fires for harmless mentions (comments,
  documentation) and for a safe `pgrep -af`; it cannot tell safe from unsafe.
- A `ps | grep | kill` chain split over several lines is not recognised as a
  chain (the individual `pgrep`/`pkill` words still are).
- Any error exits 0 without output, so a broken hook is silent.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `SELF_KILL_GUARD_DISABLE` | — | Set to `1` to disable the guard entirely (exit 0, no output, on every call); also disables the reminders |
| `CLAUDE_PLUGIN_DATA` | set by Claude Code | Directory for the reminders' per-session de-duplication state (falls back to `${XDG_CACHE_HOME:-~/.cache}/self-kill-guard`) |
| `SELF_KILL_GUARD_PARSER` | tree-sitter if importable | Set to `shlex` to force the shlex heuristic (used by the tests) |
| `SELF_KILL_GUARD_UV_TIMEOUT` | `7` | Seconds the wrapper lets the cached-environment `uv run --offline` take (when `timeout` exists) before it falls back to `python3` |
| `SELF_KILL_GUARD_NO_WARMUP` | — | Set to `1` to never spawn the background dependency warm-up (used by the tests) |

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

## Tests

```bash
bash plugins/self-kill-guard/tests/self-kill-guard-test.sh
```

Runs the hook's `--check` mode over a fixed list of commands (newline and
reserved-word boundaries, continuations, comments, quoting, heredocs, nested
`$(...)`/backticks/subshells, `bash -c`/`eval`, zsh-only syntax, and the
existing pass/deny behaviour) **twice**: once with tree-sitter (the default) and
once with `SELF_KILL_GUARD_PARSER=shlex`. A case may expect different verdicts
per mode where the heuristic legitimately differs (for example `echo then pkill
-f myworker` is PASS with tree-sitter, DENY with shlex), and each case also
asserts that the `parser=` reported by `--check` is the mode under test. Finally
it runs the `.sh` wrapper with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR` and
asserts it still emits exactly one deny decision through the `python3` fallback.
A last test starts from an empty uv cache with the warm-up enabled: the first
call must still deny quickly through the fallback and leave a stamp file, and
once the background install finished (polled for up to 20 s; skipped with a
`skip` line if there is no network) a later call must report
`parser=tree-sitter`.
The heredoc case (`cat > x.sh <<'EOF'` with kill code) expects PASS with
tree-sitter and DENY with shlex. Further sections cover the reminders: `--check`
prints a `--- REMIND ---` section for a data heredoc but not for a plain `pkill
-f`; in hook mode through the `.sh` wrapper the output is valid JSON with
`hookEventName: "PreToolUse"`, `additionalContext` and no `permissionDecision`;
and `write-reminder-hook.sh` is fed `Write`, `Edit` and `NotebookEdit` payloads
(line numbers, README path, de-duplication per session, no output for clean
text or malformed JSON, a `.md` file, the 10-line cap, pruning of old state).
They use temporary directories for `CLAUDE_PLUGIN_DATA` and the edited files.
It exits nonzero if any verdict differs. The verdict also depends on the
caller's ancestor processes' command lines, so do not run it from a command line
that itself contains the test token `myworker`.

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
| `PostToolUse` | `Write\|Edit\|NotebookEdit` | `scripts/write-reminder-hook.sh` (timeout 5s) |

## Scripts

| Path | Purpose |
|---|---|
| `scripts/self-kill-guard-hook.sh` | Dispatcher. Buffers the hook's stdin, tries `uv run --offline --script` (cached environment only, bounded by `timeout`, 7s, when available), and if uv is missing or fails (dependencies not cached, timeout) starts a throttled detached background warm-up (`uv run --script ... --help`) and replays the same input through `python3` / `python` (3.x), which uses the shlex heuristic. Output is emitted exactly once; `--check`/`--help` pass through. If no Python 3 exists at all it fails open: prints a note to stderr and exits 0 rather than breaking every Bash call. |
| `scripts/write-reminder-hook.sh` | Dispatcher for the write-time reminder: runs `write-reminder-hook.py` with `python3` (`python` 3.x, then `uv run --offline --no-project --script` as a last resort). Fails open: any problem prints nothing and exits 0. |
| `scripts/write-reminder-hook.py` | PostToolUse hook for `Write`/`Edit`/`NotebookEdit`: scans the written text for kill-by-pattern lines and prints a non-blocking `additionalContext` reminder. Stdlib only, no subprocesses. |
| `scripts/kill_reminder.py` | Shared stdlib module: kill-line detection, per-session de-duplication state, the checklist message. Imported by both hook scripts. |
| `scripts/self-kill-guard-hook.py` | Hook logic: finds real invocations of `pkill`/`pgrep`/`ps \| grep`/`killall`/`pidof` (tree-sitter-bash AST, shlex fallback), extracts the pattern operand, tests it against the command's own text, ancestor process command lines, the shell wrapper's fixed strings, and protected process names, and emits a `deny`/`ask` decision as `hookSpecificOutput` JSON (or, for a data heredoc that writes kill code, a non-blocking `additionalContext` reminder). Also serves `--check` and `--help`. Declares its dependencies as PEP 723 metadata. |
| `tests/self-kill-guard-test.sh` | Regression tests: feeds fixed commands to the hook's `--check` mode in both parser modes, compares the DENY/ASK/PASS verdict and the reported parser, and checks the wrapper's offline fallback. |

## Runtime requirements

- One of [`uv`](https://docs.astral.sh/uv/) (preferred), `python3`, or
  `python` at version 3.x.
- With `uv`, two pinned dependencies are installed on first use from the
  script's inline metadata (MIT licensed, prebuilt wheels for Linux, macOS and
  Windows, Python >= 3.10): `tree-sitter==0.26.1` and
  `tree-sitter-bash==0.25.1`. Measured cost: about 13 ms to import per hook
  call, about 0.65 s for the very first install (cold uv cache, done in the background, not on the hook's critical path), and about 4 MB
  in the uv cache. Parsing a command takes microseconds.
- Hook latency does not depend on the network. The wrapper only ever runs
  `uv run --offline --script`, which uses the already cached environment (about
  40-130 ms per call end to end, measured). If that fails (dependencies not
  cached yet, or any uv error), the wrapper starts a **detached background
  warm-up** (`uv run --script ... --help`, online, stdin/stdout/stderr on
  `/dev/null`, never waited for) and answers **that call** with the `python3`
  shlex heuristic. The first call(s) after a fresh install, or after the uv
  cache was cleared, therefore use the less precise parser until the warm-up
  finishes (about a second with network). The warm-up is throttled by
  `${XDG_CACHE_HOME:-~/.cache}/self-kill-guard/warmup.stamp` (at most one
  attempt per 10 minutes, so an air-gapped machine retries rarely), and while
  one is running (`warmup.running`, which holds uv's cache lock) calls skip uv
  and go straight to the fallback instead of blocking on the lock. Set
  `SELF_KILL_GUARD_NO_WARMUP=1` to disable spawning; failure to create the
  stamp never breaks the hook.
- Without `uv` the wrapper uses `python3` and the shlex heuristic described
  above: less precise, but the guard stays on.
- `ps`, for ancestor process detection. This is what lets the guard
  recognize `pkill node` / `killall node` / `pkill -f claude` as hitting
  Claude Code's own process tree. It is optional in the sense that the guard
  degrades gracefully (empty ancestor list) if `ps` is missing or fails; the
  command-text check, which is the dominant and most reliable case, does not
  depend on it at all.
