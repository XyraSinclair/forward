#!/bin/sh
# Install Drive Forward skills into a project (or user-wide with --user).
set -eu

here="$(cd "$(dirname "$0")" && pwd)"

case "${1:-}" in
  --user)
    dest="$HOME/.claude/skills"
    ;;
  "")
    echo "usage: $0 <target-repo> | --user" >&2
    exit 2
    ;;
  *)
    target="$1"
    [ -d "$target" ] || { echo "error: $target is not a directory" >&2; exit 1; }
    dest="$target/.claude/skills"
    ;;
esac

mkdir -p "$dest"
for skill in "$here"/skills/*/; do
  name="$(basename "$skill")"
  mkdir -p "$dest/$name"
  cp "$skill/SKILL.md" "$dest/$name/SKILL.md"
  echo "installed $name -> $dest/$name"
done

# Ship the principles alongside; the forward skill reads them.
cp "$here/PRINCIPLES.md" "$dest/forward/PRINCIPLES.md"
echo "installed PRINCIPLES.md -> $dest/forward/"
echo "done. run /forward inside a Claude Code session in your project."
