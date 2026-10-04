#!/usr/bin/env bash
# SessionStart hook: print the plugin's session context to stdout (Claude Code
# adds plain stdout as context), point at the project glossary, and start the
# one-time background install of the Korean morphology analyzer.

set -o errexit
set -o nounset
set -o pipefail

ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
CONTEXT_FILE="${ROOT}/hooks/session-context.md"
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"

if [[ ! -f "$CONTEXT_FILE" ]]; then
    exit 0
fi

cat "$CONTEXT_FILE"
echo

# Same discovery order as scripts/ste-lint.py.
glossary=""
for candidate in GLOSSARY.md docs/GLOSSARY.md docs/glossary.md; do
    if [[ -f "${PROJECT_DIR}/${candidate}" ]]; then
        glossary="$candidate"
        break
    fi
done

if [[ -n "$glossary" ]]; then
    echo "Project glossary: ${glossary}. Use its term pairs in Korean and English prose. Add a pair when a document you translate between English and Korean introduces a new term."
else
    echo "No project glossary yet. Create GLOSSARY.md at the project root only when you translate a project document between English and Korean, or write a new one in both languages. Do not create one for chat replies, rewrites of pasted text, or polishing an existing document; suggest it in one line instead."
fi

# Install kiwipiepy into the plugin data dir once. The installer runs fully
# detached so this hook returns immediately, and nothing here may fail the
# session.
launch_install() {
    mkdir -p "$DATA_DIR" || return 0
    if command -v setsid >/dev/null 2>&1; then
        setsid nohup "${ROOT}/scripts/install-deps.sh" \
            >"${DATA_DIR}/install.log" 2>&1 </dev/null &
    else
        nohup "${ROOT}/scripts/install-deps.sh" \
            >"${DATA_DIR}/install.log" 2>&1 </dev/null &
    fi
    disown 2>/dev/null || true
}

if [[ "${STE100_KOREAN_NO_INSTALL:-}" != "1" && -n "$DATA_DIR" \
    && -f "${ROOT}/requirements.txt" ]] \
    && ! cmp -s "${ROOT}/requirements.txt" "${DATA_DIR}/requirements.installed" 2>/dev/null; then
    launch_install >/dev/null 2>&1 || true
    echo "Korean morphology analyzer (kiwipiepy) is installing in the background; until it finishes, ste-lint uses uv run or the regex fallback."
fi

exit 0
