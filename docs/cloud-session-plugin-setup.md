# Claude Code Web — Cloud Session Plugin Setup

How to have plugins automatically installed whenever a new Claude Code web session starts.

## Background

In the current Claude Code web environment, `/plugin marketplace add <github-repo>` cannot be used to add marketplaces directly. The workaround is to include a setup script in the cloud environment configuration. The script downloads marketplace repositories from GitHub as ZIP archives, extracts them to a local path, registers those paths as marketplaces, and then installs the desired plugins.

`rename_marketplace` is needed because some marketplace repositories (e.g. `anthropics/claude-plugins-official`) have an official-sounding name in their `marketplace.json`. Registering a marketplace under that same name from a third-party account can be rejected by an impersonation guard. Overwriting the `name` field with a neutral value such as `local-mirror` avoids this.

## Setup

Open the cloud environment settings in Claude Code web and paste the script below into the setup script field.

```bash
#!/usr/bin/env bash
set -euo pipefail

DEBIAN_FRONTEND=noninteractive apt-get update -qq && apt-get install -y -q gh jq

MARKETPLACE_BASE="$HOME/.claude/plugins/local-marketplaces"
mkdir -p "$MARKETPLACE_BASE"

get_default_branch() {
    local branch
    branch=$(curl -sSL "https://api.github.com/repos/$1" 2>/dev/null \
        | jq -r '.default_branch // empty' 2>/dev/null || true)
    echo "${branch:-main}"
}

# rename_marketplace <dir> <new_name>
rename_marketplace() {
    local dir="$1" new_name="$2"
    local manifest="$dir/.claude-plugin/marketplace.json"
    if [[ -f "$manifest" ]]; then
        local tmp
        tmp=$(mktemp)
        jq --arg n "$new_name" '.name = $n' "$manifest" > "$tmp" && mv "$tmp" "$manifest"
        echo "[rename] marketplace.json name -> $new_name"
    else
        echo "[rename] WARN: manifest not found at $manifest" >&2
    fi
}

# add_marketplace <dir_name> <repo> [manifest_name_override]
add_marketplace() {
    local name="$1" repo="$2" rename_to="${3:-}"
    local branch
    branch=$(get_default_branch "$repo")
    echo "[$name] default branch: $branch"

    local tmp_zip tmp_dir
    tmp_zip=$(mktemp /tmp/mktmp-XXXXXX.zip)
    tmp_dir=$(mktemp -d /tmp/mktmp-XXXXXX)

    curl -fsSL "https://github.com/$repo/archive/refs/heads/$branch.zip" -o "$tmp_zip"
    unzip -q "$tmp_zip" -d "$tmp_dir"
    rm "$tmp_zip"

    rm -rf "$MARKETPLACE_BASE/$name"
    mv "$tmp_dir/${repo##*/}-$branch" "$MARKETPLACE_BASE/$name"
    rm -rf "$tmp_dir"

    if [[ -n "$rename_to" ]]; then
        rename_marketplace "$MARKETPLACE_BASE/$name" "$rename_to"
    fi

    claude plugin marketplace add "$MARKETPLACE_BASE/$name"
    echo "[$name] added"
}

# -- Register marketplaces --------------------------------------------------
add_marketplace "rishubil-skills"  "rishubil/skills"
add_marketplace "local-mirror"     "anthropics/claude-plugins-official" "local-mirror"
add_marketplace "karpathy-skills"  "multica-ai/andrej-karpathy-skills"

# -- Install plugins --------------------------------------------------------
claude plugins install shell-script@rishubil-skills
claude plugins install commit@rishubil-skills
claude plugins install plan-review@rishubil-skills
claude plugins install fetch-docs@rishubil-skills
npm install -g agent-browser defuddle   # required by fetch-docs
claude plugins install skill-eval-hook@rishubil-skills
claude plugins install ascii-diagram@rishubil-skills
claude plugins install andrej-karpathy-skills@karpathy-skills
claude plugins install skill-creator@local-mirror
```

## Customization

### Adding a marketplace

```bash
add_marketplace "<local-folder-name>" "<owner>/<repo>"
# Use a third argument to override the name when impersonation may be an issue
add_marketplace "my-mirror" "<owner>/<official-repo>" "my-mirror"
```

### Adding or removing plugins

Add or remove `claude plugins install` lines. The `@<marketplace>` suffix must match the first argument passed to `add_marketplace` (or the third argument when a rename is used).

## Notes

- The setup script runs once when the cloud environment is (re)built, not on every session start. Plugin state persists across sessions until the environment is rebuilt.
- If a GitHub ZIP download fails, the entire script aborts due to `set -euo pipefail`. Add `--retry 3` to the `curl` invocation if flaky network conditions are a concern.
- `apt-get install gh jq` assumes a Debian/Ubuntu-based container image. Update this line if the Claude Code web runtime changes.
