#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
# ]
# ///
"""
PreToolUse hook: detects direct `gh` invocations for read-only commands
and suggests using the gh-readonly.sh wrapper instead.

Write commands (gh issue create, gh pr create, gh pr merge, etc.) are
left alone; those require explicit user permission and should use `gh`
directly.
"""

import json
import os
import re
import sys

# Read-only subcommand patterns (mirrors scripts/gh-readonly.sh allowlist)
READONLY_PATTERNS: dict[str, set[str] | None] = {
    # None means the top-level command itself is readonly
    "status": None,
    "completion": None,
    "browse": None,
    "auth": {"status", "token"},
    "gist": {"list", "ls", "view"},
    "issue": {"list", "ls", "status", "view", "develop"},
    "org": {"list", "ls"},
    "pr": {"list", "ls", "status", "checks", "diff", "view"},
    "project": {"field-list", "item-list", "list", "ls", "view"},
    "release": {"list", "view", "download"},
    "repo": {"list", "view", "gitignore", "license", "autolink", "deploy-key"},
    "cache": {"list", "ls"},
    "run": {"list", "view", "watch", "download"},
    "workflow": {"list", "ls", "view"},
    "alias": {"list"},
    "attestation": {"download", "trusted-root"},
    "config": {"get", "list"},
    "extension": {"list", "search"},
    "gpg-key": {"list"},
    "label": {"list"},
    "preview": {"prompter"},
    "ruleset": {"check", "list", "view"},
    "secret": {"list"},
    "ssh-key": {"list"},
    "variable": {"get", "list"},
    "search": {"code", "commits", "issues", "prs", "repos"},
}

# HTTP methods that are NOT read-only
WRITE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}

data = json.load(sys.stdin)
command: str = data.get("tool_input", {}).get("command", "")

# Already using the wrapper → pass
if "gh-readonly.sh" in command:
    sys.exit(0)

# Find direct `gh` invocations (first command or after && ; | ||)
gh_match = re.search(
    r"(?:^|&&|\|\||;|\|)\s*gh\s+(\S+)(?:\s+(\S+))?", command
)
if not gh_match:
    sys.exit(0)

subcmd = gh_match.group(1)
subsub = gh_match.group(2) or ""

# Special handling for `gh api`: check HTTP method
if subcmd == "api":
    method_match = re.search(r"(?:-X|--method)\s+(\S+)", command)
    if method_match and method_match.group(1).upper() in WRITE_METHODS:
        # Explicit write method — let it through (needs permission)
        sys.exit(0)
    # No method flag (default GET) or explicit GET → readonly
    is_readonly = True
else:
    # Check if this is a readonly command
    is_readonly = False
    if subcmd in READONLY_PATTERNS:
        allowed_subs = READONLY_PATTERNS[subcmd]
        if allowed_subs is None or subsub in allowed_subs:
            is_readonly = True

if not is_readonly:
    # Not a readonly command — let it through (needs explicit permission)
    sys.exit(0)

plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
wrapper = f"{plugin_root}/scripts/gh-readonly.sh" if plugin_root else "gh-readonly.sh"

print(
    f"Hint: `gh {subcmd}` is a read-only command. Use"
    f" `{wrapper}` instead of `gh` directly.\n"
    f"  Example: {wrapper} {subcmd} {subsub}".rstrip(),
    file=sys.stderr,
)
sys.exit(2)
