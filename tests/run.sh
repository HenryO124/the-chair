#!/bin/bash
# Every suite, against the repo as it stands. Usage: bash tests/run.sh [name ...]
# The fake-broker suites read src/index.html (unbundled, so the injected broker
# survives); the visual ones read the built index.html.
cd "$(dirname "$0")/.."
ROOT=$(pwd); export CHAIR_ROOT=$ROOT

node -e 'require("jsdom")' 2>/dev/null || { echo "installing jsdom…"; npm install --silent jsdom >/dev/null 2>&1; }

ALL="qrflow home2 settings tf s10 count dress route cap2 again bank leak tap2 shelf fold pub look host name night turn reach seal words finger onescreen near uilang again2 lobby artist gamelists gametables grid lobby3 sofa2 monday"
# The suites that drive a real browser. Everything else is jsdom and quick.
BROWSER="fold reach onescreen grid sofa2"
# bash tests/run.sh --fast  -> jsdom only, for while you are working
if [ "$1" = "--fast" ]; then
  shift
  for b in $BROWSER; do ALL="${ALL// $b/}"; ALL="${ALL//$b /}"; done
fi
LIST="${*:-$ALL}"

# They do not touch each other, so run them at once rather than in a queue:
# a suite you wait three minutes for is a suite you stop running.
JOBS="${CHAIR_JOBS:-8}"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
run_one(){
  local t=$1
  local out rc
  out=$(timeout 300 node "tests/$t.js" 2>&1); rc=$?
  printf '%s\n' "$out" | grep -v 'Not implemented' > "$TMP/$t.out"
  echo $rc > "$TMP/$t.rc"
}
n=0
for t in $LIST; do
  run_one "$t" &
  n=$((n+1))
  if [ $((n % JOBS)) -eq 0 ]; then wait; fi
done
wait

pass=0; fail=0; failed=""
for t in $LIST; do
  rc=$(cat "$TMP/$t.rc" 2>/dev/null || echo 1)
  if [ "$rc" = "0" ]; then
    pass=$((pass+1)); echo "  ✓ $t"
  else
    fail=$((fail+1)); failed="$failed $t"
    echo "  ✗ $t"; sed 's/^/      /' "$TMP/$t.out" 2>/dev/null
  fi
done
echo
echo "$pass passed, $fail failed${failed:+ —$failed}"
exit $([ $fail -eq 0 ] && echo 0 || echo 1)
