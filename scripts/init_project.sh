#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <new-project-dir>" >&2
  exit 1
fi

TARGET="$1"
mkdir -p "$TARGET"

# 使用 rsync 排除目标目录，避免循环嵌套
if command -v rsync &>/dev/null; then
  rsync -av --exclude="$(basename "$TARGET")" . "$TARGET/"
else
  # 降级方案：手动复制，跳过目标目录
  for item in .* *; do
    [ "$item" = "." ] && continue
    [ "$item" = ".." ] && continue
    [ "$item" = "$(basename "$TARGET")" ] && continue
    [ -e "$item" ] && cp -R "$item" "$TARGET/"
  done
fi
echo "Initialized project at $TARGET"
