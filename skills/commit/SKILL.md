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

## Process

1. Check if the user specified particular files or a scope for the commit.
2. Run `git status` and `git diff` (staged + unstaged) to review changes.
3. Optionally scan recent commits (`git log --oneline -10`) to match project
   conventions.
4. If it is ambiguous which files should be staged, ask the user before
   proceeding.
5. Stage the intended files and create the commit — do **not** push.

File-specific arguments constrain which changes get staged; stage everything
only when the user explicitly asks for it.
