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
<!-- OPTIONAL: Landing Protocol — Step 3: License check -->
<!-- OPTIONAL: Landing Protocol — Step 4: Test coverage check -->
<!-- OPTIONAL: Landing Protocol — Step 4.1: Unit test check for new/modified features -->
<!-- OPTIONAL: Landing Protocol — Step 4.1a: Code coverage verification -->
<!-- OPTIONAL: Landing Protocol — Step 5: Lint / Format / Type Check -->
<!-- OPTIONAL: Landing Protocol — Step 5.1: Format check -->
<!-- OPTIONAL: Landing Protocol — Step 5.2: Lint check -->
<!-- OPTIONAL: Landing Protocol — Step 5.3: Type check -->
Landing Protocol — Step 6: Run tests
Landing Protocol — Step 6.1: Run tests
<!-- OPTIONAL: Landing Protocol — Step 7: Documentation update -->
<!-- OPTIONAL: Landing Protocol — Step 7.1: Review CHANGELOG.md update -->
Landing Protocol — Step 8: Prepare commit
Landing Protocol — Step 9: Await commit confirmation
```

(Remove the `<!-- OPTIONAL: ... -->` lines for steps that are not included in this generated protocol. Keep only the tasks that correspond to included steps.)

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

<!-- IF:license_check -->
## Step 3: License Check ⛔ MANDATORY

**Conditional execution**: only run the license check if `<DEPENDENCY_FILE>` changed. If it did not change, explicitly mark this step as completed with the reason "<DEPENDENCY_FILE> unchanged" — do not silently skip it.

```bash
<LICENSE_CHECK_COMMAND>
```

- If blocked packages appear: find an alternative or stop the protocol and report to the user
- If unknown packages appear: verify the license manually
- If the command exits with a non-zero code: stop the protocol and report to the user
<!-- END:license_check -->

<!-- IF:test_framework -->
## Step 4: Test Coverage Check ⛔ MANDATORY

- New features must have unit tests
- Bug fixes must have a test that reproduces the bug

<!-- IF:coverage -->
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
<!-- END:coverage -->

### Test Locations

| Type | Location |
|------|----------|
| Unit / integration tests | `<TEST_DIR>` |

- **Failure condition**: if writing tests is impossible → stop the protocol and report to the user
<!-- END:test_framework -->

<!-- IF:lint_format_type -->
## Step 5: Lint / Format / Type Check ⛔ MANDATORY

<!-- IF:formatter -->
```bash
<FORMAT_CHECK_COMMAND>
```

If errors found, auto-fix:

```bash
<FORMAT_FIX_COMMAND>
```
<!-- END:formatter -->

<!-- IF:linter -->
```bash
<LINT_CHECK_COMMAND>
```

If errors found, auto-fix:

```bash
<LINT_FIX_COMMAND>
```

For errors that cannot be auto-fixed, attempt to fix manually.

**Failure condition**: if unfixable errors remain → stop the protocol and report to the user
<!-- END:linter -->

<!-- IF:type_checker -->
### Step 5.3: Type Check ⛔ MANDATORY

```bash
<TYPE_CHECK_COMMAND>
```

If type errors are found, attempt to fix them manually.

**Failure condition**: if unfixable type errors remain → stop the protocol and report to the user
<!-- END:type_checker -->

<!-- END:lint_format_type -->

## Step 6: Run Tests ⛔ MANDATORY

```bash
<TEST_COMMAND>
```

- If errors found, attempt to fix
- After fixing, **go back to Step 5** and re-run
- **Failure condition**: if errors cannot be resolved → stop the protocol and report to the user

<!-- IF:changelog -->
## Step 7: Documentation Update ⛔ MANDATORY

**Review CHANGELOG.md**:

- Add an entry to `CHANGELOG.md` for user-facing feature additions, changes, or bug fixes
- May be omitted for internal refactoring or test-only additions
- Follow the existing format in CHANGELOG.md
<!-- END:changelog -->

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
