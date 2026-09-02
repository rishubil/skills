# unslop

## What it does

Edits text to strip the patterns that mark it as AI-generated, then puts a human
voice back in. The skill carries a checklist of 31 tells grouped into content,
language, style, communication artifacts, filler, jargon, and plain speech, plus
a short "adding soul" section for the other half of the job: removing patterns
without adding voice just produces sterile writing.

Use it on prose you or an agent just wrote — docs, READMEs, PR descriptions,
commit messages, release notes, blog posts, replies.

The skill sets `disable-model-invocation: true`, so Claude will not load it on
its own. Invoke it with `/unslop`. Remove that line from `SKILL.md` if you want
Claude to reach for it automatically.

## Installation

```
/plugin marketplace add rishubil/skills
/plugin install unslop@rishubil-skills
```

## Usage

```
/unslop
```

```
/unslop clean up the README section I just wrote
```

```
can we unslop and tighten the new changes?
```

## Source

`skills/unslop/SKILL.md` is a **verbatim copy** of the `unslop` skill from the
`pstack` plugin in Cursor's official plugin repository.

- Original: https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md
- Project: [cursor/plugins](https://github.com/cursor/plugins) — `pstack` plugin
- Author: (c) 2026 Lauren Tan
- License: [MIT](https://github.com/cursor/plugins/blob/main/pstack/LICENSE)

The file is redistributed here under its original MIT License, not under this
repository's license. See [`skills/unslop/NOTICE.md`](./skills/unslop/NOTICE.md)
for the full notice and license text.
