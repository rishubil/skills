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

Create `.claude/skills/landing-protocol/` if it does not exist, then write
`.claude/skills/landing-protocol/SKILL.md` using the template below.

Fill in `<PLACEHOLDERS>` based on the analysis results.

---

```markdown
---
name: landing-protocol
description: "Work completion landing protocol. Defines the mandatory wrap-up procedure after finishing any task. Execute this skill when the user says landing, /land, or similar."
---

# Landing Protocol

> **This protocol is modeled after an aircraft landing checklist.**
> Just as a pilot cannot skip a single item on the landing checklist — regardless of experience, weather, or time pressure — **every step in this protocol is absolutely mandatory and must never be skipped, abbreviated, or reinterpreted.**

## Non-Negotiable Rules

1. **This protocol requires explicit user invocation.** The user must explicitly say "landing", "/land", or similar to start this protocol. If the AI agent initiates this protocol on its own (e.g. because it judged that "work is done"), it must immediately halt and report: "Landing protocol requires explicit user invocation. Awaiting your instruction." Do not proceed with any steps.
2. **No step may be skipped.** There are no exceptions. Even if a step "seems unnecessary" or "obviously passes", it must still be executed and its result verified.
3. **No step may be reordered.** Steps must be executed in the exact sequence defined below.
4. **No step may be abbreviated.** Each step must be performed in full as described. Reading a file path is not the same as reading the diff. Glancing at output is not the same as verifying it.
5. **Failure halts the protocol.** If any step fails, stop immediately and report to the user. Do not attempt to continue with subsequent steps.
6. **Self-judgment is not a substitute for execution.** You must run the commands, read the output, and verify the results. "I already know this passes" is never acceptable.

## Abort Landing

If the user instructs to abort (e.g. "abort landing", "stop landing", "cancel landing"):
1. Use TaskList to check the current landing Task list
2. Use TaskUpdate to set all landing-related Tasks to `deleted`
3. Terminate the landing protocol immediately

**Do not resume landing work on your own until explicitly instructed to land again.**

---

**At the start, register ALL steps below with TaskCreate.** Then use TaskUpdate to mark each step `in_progress` when starting and `completed` immediately on finishing. **Every registered task must reach either `completed` or trigger a protocol halt — no task may be silently dropped or left unresolved.**

Tasks to register (each with TaskCreate):

```
Landing Protocol — Step 1: Invocation check
Landing Protocol — Step 2: Work completion check
Landing Protocol — Step 2.1: Review git changes
Landing Protocol — Step 2.2: Inspect key changes in modified files
Landing Protocol — Step 2.3: Identify any missing work
<OPTIONAL: Landing Protocol — Step 3: License check>
<OPTIONAL: Landing Protocol — Step 4: Test coverage check>
<OPTIONAL: Landing Protocol — Step 4.1: Unit test check for new/modified features>
<OPTIONAL: Landing Protocol — Step 4.1a: Code coverage verification>
<OPTIONAL: Landing Protocol — Step 5: Lint / Format / Type Check>
<OPTIONAL: Landing Protocol — Step 5.1: Format check>
<OPTIONAL: Landing Protocol — Step 5.2: Lint check>
<OPTIONAL: Landing Protocol — Step 5.3: Type check>
Landing Protocol — Step 6: Run tests
Landing Protocol — Step 6.1: Run tests
<OPTIONAL: Landing Protocol — Step 7: Documentation update>
<OPTIONAL: Landing Protocol — Step 7.1: Review CHANGELOG.md update>
Landing Protocol — Step 8: Prepare commit
Landing Protocol — Step 9: Await commit confirmation
```

(Remove the `<OPTIONAL: ...>` lines for steps that are not included in this
generated protocol. Keep only the tasks that correspond to included steps.)

## Step 1: Invocation Check ⛔ MANDATORY

Verify that the user explicitly requested the landing protocol.

Scan the conversation for an explicit user invocation such as "landing", "/land", "land", or similar. **The invocation must come from the user's message, not from the AI agent's own decision.**

- **If explicit user invocation is found**: record which message triggered it and proceed to Step 2.
- **If no explicit user invocation is found**: halt immediately and report:
  > "Landing protocol requires explicit user invocation. Awaiting your instruction."
  Do not proceed with any subsequent steps.

## Step 2: Work Completion Check ⛔ MANDATORY

Inspect the list of modified files and their changes via git.

```bash
git status && git diff HEAD
```

- Check that all planned modifications are complete
    - **Do not glance at paths and assume "looks modified" — read the actual diff**
    - Accurate answers require reading the actual changes
- **If work is missing**: cancel the landing protocol and complete the work first

<!-- INCLUDE STEP 3 ONLY IF A LICENSE CHECK TOOL/SCRIPT WAS DETECTED -->
## Step 3: License Check ⛔ MANDATORY

**Conditional execution**: only run the license check if `<DEPENDENCY_FILE>` changed. If it did not change, explicitly mark this step as completed with the reason "<DEPENDENCY_FILE> unchanged" — do not silently skip it.

```bash
<LICENSE_CHECK_COMMAND>
```

- If blocked packages appear: find an alternative or stop the protocol and report to the user
- If unknown packages appear: verify the license manually
- If the command exits with a non-zero code: stop the protocol and report to the user
<!-- END STEP 3 -->

<!-- INCLUDE STEP 4 ONLY IF A TEST FRAMEWORK WAS DETECTED -->
## Step 4: Test Coverage Check ⛔ MANDATORY

- New features must have unit tests
- Bug fixes must have a test that reproduces the bug

<!-- INCLUDE STEP 4.1a ONLY IF COVERAGE TOOL WAS DETECTED -->
### Step 4.1a: Code coverage verification ⛔ MANDATORY

All new or modified code **must** be covered by tests unless there is an unavoidable reason (e.g. platform-specific paths that cannot be exercised in CI). Run the coverage tool on changed files and verify:

```bash
<COVERAGE_COMMAND>
```

1. Check the "Missing" column for every file you touched
2. New code with missing coverage → write a test for it
3. If coverage is impossible, document the reason in the commit message

**Exemptions** (mark as completed with reason):
- Pure CI/config changes — no executable code
- Unreachable defensive branches
- Platform-specific code that cannot run in the test environment
<!-- END STEP 4.1a -->

### Test Locations

| Type | Location |
|------|----------|
| Unit / integration tests | `<TEST_DIR>` |

- **Failure condition**: if writing tests is impossible → stop the protocol and report to the user
<!-- END STEP 4 -->

<!-- INCLUDE STEP 5 ONLY IF ANY LINT/FORMAT/TYPE TOOL WAS DETECTED -->
## Step 5: Lint / Format / Type Check ⛔ MANDATORY

<!-- INCLUDE STEP 5.1 ONLY IF A FORMATTER WAS DETECTED -->
```bash
<FORMAT_CHECK_COMMAND>
```

If errors found, auto-fix:

```bash
<FORMAT_FIX_COMMAND>
```
<!-- END STEP 5.1 -->

<!-- INCLUDE STEP 5.2 ONLY IF A LINTER WAS DETECTED -->
```bash
<LINT_CHECK_COMMAND>
```

If errors found, auto-fix:

```bash
<LINT_FIX_COMMAND>
```

For errors that cannot be auto-fixed, attempt to fix manually.

**Failure condition**: if unfixable errors remain → stop the protocol and report to the user
<!-- END STEP 5.2 -->

<!-- INCLUDE STEP 5.3 ONLY IF A TYPE CHECKER WAS DETECTED -->
### Step 5.3: Type Check ⛔ MANDATORY

```bash
<TYPE_CHECK_COMMAND>
```

If type errors are found, attempt to fix them manually.

**Failure condition**: if unfixable type errors remain → stop the protocol and report to the user
<!-- END STEP 5.3 -->

<!-- END STEP 5 -->

## Step 6: Run Tests ⛔ MANDATORY

```bash
<TEST_COMMAND>
```

- If errors found, attempt to fix
- After fixing, **go back to Step 5** and re-run
- **Failure condition**: if errors cannot be resolved → stop the protocol and report to the user

<!-- INCLUDE STEP 7 ONLY IF CHANGELOG.md EXISTS -->
## Step 7: Documentation Update ⛔ MANDATORY

**Review CHANGELOG.md**:

- Add an entry to `CHANGELOG.md` for user-facing feature additions, changes, or bug fixes
- May be omitted for internal refactoring or test-only additions
- Follow the existing format in CHANGELOG.md
<!-- END STEP 7 -->

## Step 8: Prepare Commit ⛔ MANDATORY

```bash
git status
git diff
```

- Check for unstaged relevant files and `git add` them
- Final review of all changes
- Draft a commit message (focus on the reason for the change, in English)
- Use conventional commits format: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, etc.

## Step 9: Await Commit Confirmation ⛔ MANDATORY

Use the **AskUserQuestion** tool to propose the commit message and ask whether to commit. Do not run `git commit` until the user confirms via AskUserQuestion.

```bash
git commit -m "$(cat <<'EOF'
<commit message>
EOF
)"
git status
```

---

## Failure Report Format

```
🚨 Landing Protocol Failed — Step N: <step name>

Cause: <specific error details>

Required actions:
- <action 1>
- <action 2>
```
```

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
