---
name: commit
description: >
  Create git commits following Conventional Commits format with a mandatory body
  that explains *why* the change was made. Use when you need to stage and commit
  changes with a well-structured, informative commit message.
---

<!-- Based on https://github.com/mitsuhiko/agent-stuff/tree/main/skills/commit -->

## Format

```
<type>(<scope>): <summary>

<body>
```

- **type** (required): `feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `perf`
- **scope** (optional): short noun in parentheses
- **summary** (required): imperative mood, ≤ 72 chars, no trailing period
- **body** (required): see Body guidelines below

Do NOT include breaking-change markers, footers, or sign-off lines.

## Body guidelines

The body is **mandatory**. Follow the principles from
[Write good commit messages](https://blog.jgc.org/2013/07/write-good-commit-messages.html)
by John Graham-Cumming:

- Explain **why** the change was made, not just what changed — the diff already
  shows what.
- Use words like "because", "as", or "so that" to make the reasoning explicit.
- Include relevant context: what problem existed, what you verified, how to
  reproduce if applicable, and any notable implementation decisions.
- Write for a future reader (including yourself months from now) who needs to
  understand how the code evolved.
- Commit messages are tied to a specific diff and never go out of date — use
  that to your advantage by capturing reasoning that would otherwise be lost.

Wrap body lines at 72 characters.

## Language

Default to English, but if `git log` shows that recent commits are written in
another language (e.g. Korean, Japanese), match that language for both the
subject and the body. Consistency with the project's existing history matters
more than personal preference — a repository whose log is in Korean should
keep getting Korean commit messages.

## Process

1. Check if the user specified particular files or a scope for the commit.
2. Run `git status` and `git diff` (staged + unstaged) to review changes.
3. Scan recent commits (`git log --oneline -10`, plus a full message or two
   via `git log -n 3`) to match the project's conventions **and language**.
4. If it is ambiguous which files should be staged, ask the user before
   proceeding.
5. Stage the intended files and create the commit — do **not** push.

File-specific arguments constrain which changes get staged; stage everything
only when the user explicitly asks for it.

## Examples

Both examples below are taken directly from
[John Graham-Cumming's blog post](https://blog.jgc.org/2013/07/write-good-commit-messages.html)
(obscured details in the originals are shown as `XXX`). They illustrate the
level of detail to aim for in the body.

Subject lines have been rewritten to follow the Conventional Commits format
defined above; the bodies are unchanged from the original blog post.

### Example 1 — a one-line Makefile fix

```
fix(make): sort the output of $(wildcard), unsorted in GNU Make 3.82+

The Makefile was relying on the output of $(wildcard) to be sorted. This is
important because the XXXXXXXXXXXX rules have files that are numbered and
must be handled in order. The XXXXXXX relies on this order to build the rules
in the correct order (and set the order attributes in the JSON files). This
worked with GNU Make 3.81

In GNU Make 3.82 the code that globs has been changed to add the GLOB_NOSORT
option and so the output of $(wildcard) is no longer ordered and the build
would break. For example,

   make clean-out && make

would fail because the XXXXXXXXXXXXXXXX (which is used for the XXXXX action)
which appears in XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX would not have been
parsed before the XXXXX action was used in some other XXXXX file. That would
generate a fatal error.

The solution is simple: wrap the $(wildcard) in $(sort). The actual change
uses a $(foreach) loop because it's necessary to keep the directories in the
order specified in the Makefile and the files within the directory are sorted
by the $(sort $(wildcard ...)). The directory order is important because
XXXXXXXXXXXX must be processed before the other rule directories because it
contains XXXXXXXXXXXXXXXXXXXXXXXXXXX which sets the XXXXXXXXXX thresholds.
```

The first line gives a brief summary. The body explains *why* the change was
made (a behaviour change in GNU Make 3.82), *what actually broke*,
*how to reproduce* the failure, and *why the specific fix is shaped the way
it is* — none of which is recoverable from the diff alone.

### Example 2 — adding signal handling

```
feat: handle SIGABRT and force a panic

It can be useful to crash XXXXXXX via a signal to get a stack trace of every
running goroutine. To make this reliable have added handling of SIGABRT.

If you do,

   kill -ABRT

A panic is generated with message "panic: SIGABRT called" followed by
a stack trace of every goroutine.
```

Even a small feature gets a body that documents the *motivation* (need to
inspect goroutine stacks on demand) and *how to use the new behaviour*, so a
future reader does not have to reverse-engineer either from the code.
