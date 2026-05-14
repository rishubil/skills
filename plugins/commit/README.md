# commit

A Claude Code plugin that enforces [Conventional Commits](https://www.conventionalcommits.org/) format with a mandatory body explaining *why* the change was made.

## What it does

When triggered, this skill stages the relevant files and creates a commit with a well-structured message following this format:

```
<type>(<scope>): <summary>

<body>
```

The body is **required** — it must explain the reasoning behind the change, not just what changed. The diff already shows what; the commit message must capture *why*.

## Commit types

| Type | When to use |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `refactor` | Code refactoring without behavior change |
| `chore` | Maintenance tasks |
| `test` | Adding or updating tests |
| `perf` | Performance improvement |

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install commit@rishubil-skills
```

## Usage

Mention "commit" or "create a commit" in your message. The skill will:

1. Check which files to stage (asks if ambiguous)
2. Run `git status` and `git diff` to review changes
3. Scan recent commits to match the project's conventions and language
4. Stage the intended files and create the commit — does **not** push

## Language

Defaults to English. If recent commits in `git log` are in another language (e.g. Korean, Japanese), the skill matches that language for consistency.
