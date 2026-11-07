#!/bin/bash
# Put the site back to an earlier version. For the night something breaks and
# the person who has to fix it is holding a drink in a room full of people.
#
#   bash tools/rollback.sh            what versions are there, newest first
#   bash tools/rollback.sh 16:18      go back to that one
#   bash tools/rollback.sh --last     go back one version
#
# It does not rewrite history: it puts the old files back as a new commit, so
# nothing is lost and you can roll forward again the same way.
cd "$(dirname "$0")/.."
set -o pipefail

list(){
  echo "Versions on this site, newest first:"
  echo
  # dedup on the whole version string: they are all from the same day, so
  # keying on the first word would collapse the lot into one
  git log --format='%h' -60 -- version.txt | while read -r h; do
    v=$(git show "$h:version.txt" 2>/dev/null | tr -d '\n')
    [ -n "$v" ] && printf '%s\t%s\n' "$v" "$h"
  done | awk -F'\t' '!seen[$1]++{printf "  %-14s %s\n",$1,$2}'
  echo
  echo "Now live: $(cat version.txt)"
}

pick(){                       # the commit whose version.txt holds $1
  git log --format='%h' -60 -- version.txt | while read -r h; do
    v=$(git show "$h:version.txt" 2>/dev/null | tr -d '\n')
    case "$v" in *"$1"*) echo "$h"; return;; esac
  done | head -1
}

case "${1:-}" in
  ""|-l|--list) list; exit 0;;
  --last)
    now=$(cat version.txt)
    target=$(git log --format='%h' -60 -- version.txt | while read -r h; do
      v=$(git show "$h:version.txt" 2>/dev/null | tr -d '\n')
      [ -n "$v" ] && [ "$v" != "$now" ] && { echo "$h"; break; }
    done | head -1);;
  *) target=$(pick "$*");;   # accepts 16:43 or "07.11. 16:43"
esac

if [ -z "${target:-}" ]; then
  echo "No version matching '${1}'. Run it with no arguments to see the list."; exit 1
fi

was=$(cat version.txt)
now=$(git show "$target:version.txt" | tr -d '\n')
echo "Putting the site back:  $was  ->  $now   ($target)"

# the files a visitor actually loads, plus the source they are built from
for f in index.html banks.js lib-mqtt.js lib-qr.js version.txt src/index.html; do
  git show "$target:$f" > "$f" 2>/dev/null || echo "  (no $f in that version — left as it is)"
done

git add -A
git commit -q -m "Back to $now

Rolled back from $was. Nothing is lost: $was is still in the history and
tools/rollback.sh can go forward to it again."
echo
if git push -q 2>/dev/null; then
  echo "Done. The site reads $now within a minute or two."
else
  echo "The files here are back to $now, but sending them out failed."
  echo "The site is still showing $was until this works:"
  echo
  echo "    git -C \"$PWD\" push"
  echo
  echo "If it keeps failing you are offline. Nothing is lost — the rollback"
  echo "is committed here and will go out the moment a push succeeds."
fi
echo "To go the other way:  bash tools/rollback.sh \"$was\""
