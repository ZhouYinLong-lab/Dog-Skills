#!/usr/bin/env bash
# Record dbskill plugin marketplace demo GIF
# Usage: ./scripts/record-demo.sh
# Output: demo.gif in repo root
#
# Auto-detects marketplace repo: uses upstream (dontbesilent2025/dbskill) if its
# default branch has .claude-plugin/marketplace.json, otherwise falls back to
# origin fork. After upstream PR merge, re-running this script will automatically
# produce a demo pointing at the canonical repo.
#
# Prerequisites: brew install charmbracelet/tap/vhs gifsicle

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TAPE_TEMPLATE="$SCRIPT_DIR/demo.tape"
TAPE_RENDERED="/tmp/demo_rendered.tape"
OUTPUT_GIF="$REPO_DIR/demo.gif"

for cmd in vhs gifsicle; do
  if ! command -v "$cmd" &>/dev/null; then
    echo "Error: $cmd not found."
    echo "Install: brew install charmbracelet/tap/vhs gifsicle"
    exit 1
  fi
done

# Extract owner/repo from a git remote URL (strips .git suffix and host prefix)
parse_remote() {
  git -C "$REPO_DIR" remote get-url "$1" 2>/dev/null \
    | sed 's|.*github.com[:/]||; s|\.git$||'
}

# Detect marketplace repo: prefer upstream if it has marketplace.json, else origin
detect_marketplace_repo() {
  local upstream origin
  upstream=$(parse_remote upstream) || true
  origin=$(parse_remote origin) || true

  if [[ -n "$upstream" ]] && gh api "repos/$upstream/contents/.claude-plugin/marketplace.json" &>/dev/null; then
    echo "$upstream"
    return
  fi
  if [[ -n "$origin" ]]; then
    echo "$origin"
    return
  fi
  echo "dontbesilent2025/dbskill"
}

# Remove previously installed demo plugins (safe to call when nothing is installed)
cleanup_plugins() {
  claude plugin uninstall dbs-diagnosis@dontbesilent-skills 2>/dev/null || true
  claude plugin uninstall dbs@dontbesilent-skills 2>/dev/null || true
  claude plugin marketplace remove dontbesilent-skills 2>/dev/null || true
}

MARKETPLACE_REPO=$(detect_marketplace_repo)
# Sanitize: keep only characters valid in a GitHub owner/repo slug to prevent
# a maliciously crafted remote URL from corrupting the sed substitution.
MARKETPLACE_REPO=$(printf '%s' "$MARKETPLACE_REPO" | tr -dc 'A-Za-z0-9/_.-')
echo "Using marketplace repo: $MARKETPLACE_REPO"

# Render tape template: replace MARKETPLACE_REPO placeholder with detected repo
sed "s|MARKETPLACE_REPO|$MARKETPLACE_REPO|g" "$TAPE_TEMPLATE" > "$TAPE_RENDERED"

echo "Cleaning previous plugin state..."
cleanup_plugins

echo "Recording demo..."
rm -f "$OUTPUT_GIF"
(cd "$REPO_DIR" && vhs "$TAPE_RENDERED")

echo "Speeding up 2x..."
cp "$OUTPUT_GIF" /tmp/demo_raw.gif
gifsicle -d2 /tmp/demo_raw.gif "#0-" > "$OUTPUT_GIF"

echo "Cleaning up..."
cleanup_plugins
rm -f /tmp/demo_raw.gif "$TAPE_RENDERED" /tmp/cw.sh

SIZE=$(du -sh "$OUTPUT_GIF" | awk '{print $1}')
echo "Done: $OUTPUT_GIF ($SIZE)"
