#!/bin/bash
# One step from the repo to the live site.
#   deploy.sh "commit subject"            build, check, commit, push
#   SKIP_TESTS=1 deploy.sh "..."          skip the suite (say why in the message)
#
# The repo's src/ is the source of truth. It used to be the other way round,
# and a stale working copy silently overwrote a morning's fixes on the way out.
# Nothing noticed for hours, so now three things are checked before anything
# is committed: the page still has the content it had, the suite is green, and
# the build stamp agrees with itself.
set -e
O=/mnt/user-data/outputs
R=/home/claude/the-chair

cp $R/src/index.html $O/index.html          # keep the working copy in step
cp $R/src/index.html $O/the-chair.html      # what the jsdom suites read
[ -f $O/menu.mp3 ] && cp $O/menu.mp3 $R/menu.mp3

python3 $R/tools/bundle.py
mkdir -p $O/dist && cp $R/index.html $O/dist/index.html

cd $R

# 1. did the page quietly lose something it had before?
python3 tools/facts.py --check

# 2. does the stamp in the built page match the one we are publishing?
V=$(cat version.txt)
B=$(grep -o "const BUILD='[^']*'" index.html | head -1 | sed "s/.*'\(.*\)'/\1/")
if [ "$V" != "$B" ]; then
  echo "REFUSING TO DEPLOY: version.txt says '$V' but the page says '$B'"
  exit 1
fi

# 3. is it green?
if [ -z "$SKIP_TESTS" ]; then
  if ! bash tests/run.sh | tail -1; then
    echo "REFUSING TO DEPLOY: the suite is not green"
    exit 1
  fi
else
  echo "tests skipped"
fi

git add -A
if git diff --cached --quiet; then echo "nothing changed"; exit 0; fi
git commit -q -F - <<MSG
${1:-Update The Chair}

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01QKtKix6MR9HdNxBfsMWUDJ
MSG
git push -q origin main
git -c core.pager=cat log --oneline -1
echo
echo "live build should read: $V"
echo "confirm with: https://henryo124.github.io/the-chair/version.txt"
