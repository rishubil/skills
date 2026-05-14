#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi
cd "$(dirname "$0")"
cat <<'EOF'
Instruction: MANDATORY SKILL ACTIVATION SEQUENCE
Step 1 - Assessment (must be included in your response):
For each skill in <available_skills>, state its status in this format:
[skill name] - YES/NO - [reason]
Step 2 - Activation (execute immediately after Step 1):
- If any skill is judged YES → call the Skill(skill-name) tool for each one right now.
- If none are YES → state "No skills needed" and proceed.
Step 3 - Implementation:
Only begin actual implementation after Step 2 is fully complete.
Important: You MUST call the Skill() tool in Step 2. Do not skip it and jump to implementation.
If you do not actually activate skills in Step 2, the assessment in Step 1 is worthless.
Correct execution example:
- research: NO - not a research task
- svelte5-runes: YES - reactive state management ($state) needed
- sveltekit-structure: YES - route creation needed
[Then immediately call Skill() tools:]
> Skill(svelte5-runes)
> Skill(sveltekit-structure)
[Only then begin actual implementation]
EOF
exit 0
