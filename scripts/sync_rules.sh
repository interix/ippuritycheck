#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <target-project-dir>" >&2
  exit 1
fi

TARGET="$1"
mkdir -p "$TARGET/rules"
cp -R rules/* "$TARGET/rules/"
cp CLAUDE.md "$TARGET/CLAUDE.md"
echo "Synced CLAUDE.md and rules/ to $TARGET"
