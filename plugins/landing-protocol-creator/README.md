# landing-protocol-creator

A Claude Code plugin that analyzes the current project's tech stack and generates a project-specific `landing-protocol` skill at `.claude/skills/landing-protocol/SKILL.md`.

## What it does

A landing protocol is a mandatory work-completion checklist — modeled after an aircraft landing checklist — that Claude runs before committing. It covers git diff review, license checks, test coverage, lint/format/type checks, running tests, CHANGELOG updates, and commit preparation.

Because each project uses different tools (pytest vs jest, ruff vs eslint, ty vs tsc, etc.), a one-size-fits-all landing protocol does not work well. This skill inspects the project's configuration files and generates a protocol that includes only the steps and commands that actually apply to this project.

Steps that are not relevant to the project are omitted entirely — not left as placeholders.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install landing-protocol-creator@rishubil-skills
```

## Usage

In any project directory, ask Claude to create a landing protocol:

- "create a landing protocol for this project"
- "generate a landing protocol"
- "set up a landing protocol"

Claude will:

1. Detect the language and build system (`pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, etc.)
2. Identify the test framework, linter, formatter, and type checker in use
3. Check for a CHANGELOG and license-check automation
4. Write `.claude/skills/landing-protocol/SKILL.md` with project-specific commands and only the applicable steps
5. Report what was detected and what was included or omitted

The generated skill becomes a local project skill. Once it exists, Claude will automatically follow it whenever the user says "landing" or "/land".
