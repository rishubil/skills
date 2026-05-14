---
name: landing-protocol-creator
description: >
  Analyze the current project's tech stack and generate a project-specific
  landing-protocol skill at .claude/skills/landing-protocol/SKILL.md.
  Use when the user asks to create, generate, or set up a landing protocol
  for the current project.
  Trigger phrases: "create landing protocol", "generate landing protocol",
  "set up landing protocol", "/landing-protocol-creator".
---

# Landing Protocol Creator

Generate a project-specific `landing-protocol` skill tailored to the current
project's tech stack and tooling. The output is written to
`.claude/skills/landing-protocol/SKILL.md`.

## Step 1: Analyze the Project

Run the following checks to detect the tech stack and available tooling.

### Detect language / build system

Check for these files (use `ls` or `test -f`):

| File | Implies |
|------|---------|
| `pyproject.toml` or `setup.py` or `setup.cfg` | Python |
| `uv.lock` | Python + uv |
| `package.json` | Node.js |
| `Cargo.toml` | Rust |
| `go.mod` | Go |
| `Makefile` | Make-based build |

### Common checks (all projects)

- **Source directory**: does `src/` exist? If not, is there a named package
  directory (e.g. same name as the project)?
- **Test directory**: does `tests/` or `test/` exist?
- **CHANGELOG**: does `CHANGELOG.md` (or `CHANGELOG`) exist?
- **License check automation**: look for any of the following:
  - Shell scripts in `scripts/` whose name contains "license"
  - A Makefile target named `license` or `check-license`
  - For Python: `pip-licenses`, `licensecheck`, or `reuse` listed in
    `pyproject.toml` dependencies or dev-dependencies

### Python-specific checks

Read `pyproject.toml` and look for:

| Section | Implies |
|---------|---------|
| `[tool.ruff]` | ruff (format + lint) |
| `[tool.mypy]` | mypy type checker |
| `[tool.pyright]` | pyright type checker |
| `[tool.pytest.ini_options]` or pytest in deps | pytest |
| `ty` in dev dependencies | ty type checker |
| `pytest-xdist` in deps | parallel test execution (`-n auto`) |
| `pytest-cov` in deps | coverage support |

Also check whether `uv run` should be used as the runner prefix (if `uv.lock`
exists or `[tool.uv]` is present).

### Node.js-specific checks

Read `package.json`:
- `scripts.test` → test command
- `scripts.lint` → lint command
- `scripts.format` → format command
- `scripts.typecheck` → type check command
- devDependencies: `typescript`, `eslint`, `prettier`, `biome`, etc.

### Rust-specific checks

- Test: `cargo test`
- Format: `cargo fmt --check` / `cargo fmt`
- Lint: `cargo clippy`
- Type check: n/a (covered by compiler)

### Go-specific checks

- Test: `go test ./...`
- Format: `gofmt -l .` / `gofmt -w .`
- Lint: `golangci-lint run` (if present)
- Type check: n/a (covered by compiler)

## Step 2: Determine What to Include

Based on the analysis, decide which sections to include in the generated
landing protocol. **Omit sections entirely** when the corresponding tool is
not detected — do not leave placeholders or "N/A" notes.

| Section | Include when |
|---------|-------------|
| Step 3: License check | A license-check script or tool was detected |
| Step 4.1a: Coverage | `pytest-cov` (or equivalent) detected |
| Step 5.1: Format check | A formatter was detected (ruff, prettier, gofmt, etc.) |
| Step 5.2: Lint check | A linter was detected (ruff, eslint, clippy, etc.) |
| Step 5.3: Type check | A type checker was detected (ty, mypy, tsc, pyright) |
| Step 6.1: Tests | A test framework was detected |
| Step 7: CHANGELOG | `CHANGELOG.md` exists |

Steps 1, 2, 8, and 9 are always included regardless of stack.

## Step 3: Generate the SKILL.md

Read the template file `landing-protocol.template.md` located in the same
directory as this `SKILL.md`. Use it as the base for the generated protocol.

Create `.claude/skills/landing-protocol/` if it does not exist, then write
`.claude/skills/landing-protocol/SKILL.md` by applying the following
transformations to the template:

1. **Replace all `<PLACEHOLDERS>`** with the values determined in Step 2.
2. **Remove conditional blocks** that do not apply:
   - Each optional section is wrapped in `<!-- IF:flag -->` … `<!-- END:flag -->` markers.
   - Remove the entire block (including the markers) for any flag that is not active.
   - Keep the block content (removing only the markers) for active flags.
3. **Remove all remaining HTML comment markers** from the output — they are
   instructions for the generator, not content for the user.

### Conditional flags

| Flag | Active when |
|------|-------------|
| `license_check` | A license-check script or tool was detected |
| `test_framework` | A test framework was detected |
| `coverage` | A coverage tool was detected (`pytest-cov` or equivalent) |
| `lint_format_type` | Any of: formatter, linter, or type checker was detected |
| `formatter` | A formatter was detected (ruff, prettier, gofmt, etc.) |
| `linter` | A linter was detected (ruff, eslint, clippy, etc.) |
| `type_checker` | A type checker was detected (ty, mypy, tsc, pyright) |
| `changelog` | `CHANGELOG.md` exists in the project root |

---

## Placeholder Reference

When writing the generated SKILL.md, replace these placeholders:

| Placeholder | Example (Python/uv/ruff/ty/pytest) |
|-------------|-------------------------------------|
| `<DEPENDENCY_FILE>` | `pyproject.toml` / `package.json` / `Cargo.toml` |
| `<LICENSE_CHECK_COMMAND>` | `uv run pip-licenses --format=plain-vertical` |
| `<COVERAGE_COMMAND>` | `uv run pytest <TEST_DIR>/ -n auto --cov --cov-report=term-missing` |
| `<TEST_DIR>` | `tests` or `test` |
| `<FORMAT_CHECK_COMMAND>` | `uv run ruff format --check src/ tests/` |
| `<FORMAT_FIX_COMMAND>` | `uv run ruff format src/ tests/` |
| `<LINT_CHECK_COMMAND>` | `uv run ruff check src/ tests/` |
| `<LINT_FIX_COMMAND>` | `uv run ruff check --fix src/ tests/` |
| `<TYPE_CHECK_COMMAND>` | `uv run ty check src/ tests/` |
| `<TEST_COMMAND>` | `uv run pytest tests/ -n auto -v` |

Remove the HTML comment markers (`<!-- ... -->`) and their content from the
final output — they are instructions for you, not content for the user.

## Step 4: Report to the User

After writing the file, report:

- What tech stack was detected
- Which steps were included and which were omitted (and why)
- The path of the generated file: `.claude/skills/landing-protocol/SKILL.md`
