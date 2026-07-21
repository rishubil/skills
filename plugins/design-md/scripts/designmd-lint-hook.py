#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
# ]
# ///
"""
PostToolUse hook: validates DESIGN.md files with `designmd lint` after Write/Edit.

Runs `npx -y -p @google/design.md designmd lint <file>` on any file whose
basename matches DESIGN.md (or a DESIGN-*.md / DESIGN.*.md variant) and:
- blocks with the lint errors when the CLI reports at least one error finding
- surfaces warnings as additional context (advisory, non-blocking)
- surfaces best-effort diagnostics when the CLI itself can't be run or parsed

Always exits 0: this hook informs, it never hard-fails the session.
"""

import json
import os
import re
import shutil
import subprocess
import sys

DESIGN_MD_RE = re.compile(r"^DESIGN([-.][^/]*)?\.md$", re.IGNORECASE)
LINT_CMD_HINT = "npx -y -p @google/design.md designmd lint {path}"


def emit(payload):
    print(json.dumps(payload))
    sys.exit(0)


def context_payload(system_message, additional_context):
    """Non-blocking informational payload: shown to the user and to Claude."""
    return {
        "systemMessage": system_message,
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": additional_context,
        },
    }


def additional_context_only(additional_context):
    """Non-blocking payload visible only to Claude (no systemMessage)."""
    return {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": additional_context,
        }
    }


def block_payload(reason):
    return {"decision": "block", "reason": reason}


def format_finding(finding):
    severity = finding.get("severity", "info")
    message = finding.get("message", "")
    path = finding.get("path")
    if path:
        return f"- [{severity}] {path}: {message}"
    return f"- [{severity}] {message}"


try:
    data = json.load(sys.stdin)
except (json.JSONDecodeError, UnicodeDecodeError):
    sys.exit(0)

if data.get("tool_name") not in ("Write", "Edit"):
    sys.exit(0)

file_path = data.get("tool_input", {}).get("file_path", "")
basename = os.path.basename(file_path)
if not DESIGN_MD_RE.match(basename):
    sys.exit(0)

if not os.path.isfile(file_path):
    sys.exit(0)

if shutil.which("npx") is None:
    emit(
        context_payload(
            "designmd-lint-hook: 'npx' not found, could not validate "
            f"{basename}.",
            f"`npx` was not found in PATH, so {file_path} could not be "
            "validated against the DESIGN.md spec. Install Node.js/npx, "
            "or manually review the file against the DESIGN.md spec "
            "before continuing.",
        )
    )

cmd = ["npx", "-y", "-p", "@google/design.md", "designmd", "lint", file_path]
try:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=100)
except subprocess.TimeoutExpired:
    emit(
        context_payload(
            f"designmd-lint-hook: lint of {basename} timed out.",
            f"`designmd lint` timed out after 100s while validating "
            f"{file_path}. Manually review the file against the "
            "DESIGN.md spec, or re-run "
            f"`{LINT_CMD_HINT.format(path=file_path)}` later.",
        )
    )
except OSError as exc:
    emit(
        context_payload(
            f"designmd-lint-hook: could not run lint for {basename}.",
            f"Failed to launch `npx` to validate {file_path}: {exc}. "
            "Manually review the file against the DESIGN.md spec.",
        )
    )

try:
    report = json.loads(result.stdout)
except json.JSONDecodeError:
    stderr_excerpt = result.stderr[:500]
    emit(
        context_payload(
            f"designmd-lint-hook: could not parse lint output for {basename}.",
            f"`designmd lint` produced output that could not be parsed as "
            f"JSON for {file_path}. stderr (truncated): {stderr_excerpt!r}. "
            "Manually review the file against the DESIGN.md spec, or "
            f"re-run `{LINT_CMD_HINT.format(path=file_path)}` to inspect it "
            "directly.",
        )
    )

if "error" in report:
    emit(
        context_payload(
            f"designmd-lint-hook: could not lint {basename}.",
            f"`designmd lint` could not process {file_path}: "
            f"{report.get('message', report['error'])}. Manually review "
            "the file against the DESIGN.md spec.",
        )
    )

findings = report.get("findings", [])
errors = [f for f in findings if f.get("severity") == "error"]
warnings = [f for f in findings if f.get("severity") == "warning"]

if errors:
    lines = [
        f"{basename} failed `designmd lint` with {len(errors)} error(s). "
        "Fix them before continuing:"
    ]
    lines.extend(format_finding(f) for f in errors)
    if warnings:
        lines.append("Warnings (not blocking):")
        lines.extend(format_finding(f) for f in warnings)
    lines.append(
        "Re-run "
        f"`{LINT_CMD_HINT.format(path=file_path)}` after fixing."
    )
    emit(block_payload("\n".join(lines)))

if warnings:
    lines = [
        f"`designmd lint` found {len(warnings)} warning(s) in {basename} "
        "(advisory, e.g. contrast, orphaned tokens, section order). "
        "Fix them unless there is a deliberate reason not to:"
    ]
    lines.extend(format_finding(f) for f in warnings)
    emit(additional_context_only("\n".join(lines)))

sys.exit(0)
