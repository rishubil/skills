#!/usr/bin/env bash
# Source: https://scottspence.com/posts/how-to-make-claude-code-skills-activate-reliably
set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi
cd "$(dirname "$0")"
cat <<'EOF'
Instruction: Skill activation check
Step 1 - Assessment (must be included in your response):
For each skill in the available-skills list (the skills the Skill tool can load), state its status in this format:
[skill name] - YES/NO - [reason]
Step 2 - Activation (execute immediately after Step 1):
- If any skill is judged YES → call the Skill(skill-name) tool for each one right now.
- If none are YES → state "No skills needed" and proceed.
Step 3 - Implementation:
Only begin actual implementation after Step 2 is fully complete.
A YES only takes effect once its Skill() call is made, because the assessment alone loads none of the skill's instructions.
EOF
exit 0
