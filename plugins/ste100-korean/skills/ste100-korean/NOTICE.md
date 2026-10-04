# NOTICE — ste100-korean skill

This skill is an adaptation of four MIT-licensed projects. The adapted files are
redistributed under the MIT License. The upstream copyright notices and license
text are reproduced below, as the MIT License requires.

## 1. danyuchn/asd-ste100-skill

- **Source:** https://github.com/danyuchn/asd-ste100-skill (commit `32511c6`)
- **Copyright:** (c) 2026 Dustin Yuchen Teng
- **License:** MIT License
- **Retrieved:** 2026-10-04
- **What this skill adapts:** the overall structure of `SKILL.md` (modes, process,
  output format, boundaries, the modality rule), `references/english.md`, the
  English examples in `examples/before-after.md`, and the English rules,
  Markdown handling, and command-line interface of `scripts/ste-lint.py`.

## 2. beamonic/ste-ko

- **Source:** https://github.com/beamonic/ste-ko (commit `fd351fe`)
- **Copyright:** (c) 2026 Beamonic
- **License:** MIT License
- **Retrieved:** 2026-10-04
- **What this skill adapts:** several Korean rule ideas in `references/korean-*.md`
  (single-tilde ranges, the modifier-clause limit, the connective-chain limit,
  slashes and nested parentheses, guess vs. fact), and the regex
  stem-expansion technique in `scripts/ste-lint.py`. Rule text and examples
  were written anew for this skill.

## 3. Turtle-Hwan/im-ai-copyeditor

- **Source:** https://github.com/Turtle-Hwan/im-ai-copyeditor (commit `393cf27`)
- **Copyright:** (c) 2026 Turtle-Hwan
- **License:** MIT License
- **Retrieved:** 2026-10-04
- **What this skill adapts:** Korean rule ideas from its sentence, AI-tell,
  style, and spelling rulebooks, in `references/korean-wording.md` and `references/korean-style.md` (K30-K38 and parts
  of K16-K19), and the corresponding regex rules in `scripts/ste-lint.py`
  (`ko-plain-word`, `ko-ai-tell`, `ko-middle-dot`, `ko-dash`,
  `ko-genitive-chain`, `ko-honorific-object`, and part of
  `ko-translationese`). Rule text and examples were written anew for this
  skill. No scripts were copied.

## 4. cursor/plugins — pstack `unslop` skill

- **Source:** https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md (main as of 2026-10-04)
- **Copyright:** (c) 2026 Lauren Tan
- **License:** MIT License — https://github.com/cursor/plugins/blob/main/pstack/LICENSE
- **Retrieved:** 2026-10-04
- **What this skill adapts:** English rule ideas in `references/english.md`
  ("AI tells and plain words"), parts of core rules 7, 12, and 15 in
  `SKILL.md`, and the advisory English rules `ai-vocabulary`,
  `filler-phrase`, `plain-word`, `fancy-is`, `chatbot-phrase`, `em-dash`,
  `curly-quote`, `arrow-speak`, `title-case-heading`, and `inline-header` in
  `scripts/ste-lint.py`. Rule text was written anew for this skill.

## ASD-STE100

This skill does not contain the ASD-STE100 rule text or its approved-word
dictionary. ASD-STE100 is (c) ASD, the AeroSpace and Defence Industries
Association of Europe. See `references/sources.md`.

## License text

All four upstream projects use the same MIT License text, with these copyright lines:

- Copyright (c) 2026 Dustin Yuchen Teng
- Copyright (c) 2026 Beamonic
- Copyright (c) 2026 Turtle-Hwan
- Copyright (c) 2026 Lauren Tan

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
