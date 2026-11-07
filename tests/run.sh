#!/bin/bash
# Every suite, against the repo as it stands. Usage: bash tests/run.sh [name ...]
# The fake-broker suites read src/index.html (unbundled, so the injected broker
# survives); the visual ones read the built index.html.
cd "$(dirname "$0")/.."
ROOT=$(pwd); export CHAIR_ROOT=$ROOT

node -e 'require("jsdom")' 2>/dev/null || { echo "installing jsdom…"; npm install --silent jsdom >/dev/null 2>&1; }

ALL="qrflow home2 settings tf s10 count dress route cap2 again bank leak tap2 shelf fold pub look host name night turn reach seal words"
LIST="${*:-$ALL}"
pass=0; fail=0; failed=""
for t in $LIST; do
  out=$(timeout 300 node "tests/$t.js" 2>&1); rc=$?
  out=$(printf '%s\n' "$out" | grep -v 'Not implemented')
  if [ $rc -eq 0 ]; then
    pass=$((pass+1)); echo "  ✓ $t"
  else
    fail=$((fail+1)); failed="$failed $t"
    echo "  ✗ $t"; echo "$out" | sed 's/^/      /'
  fi
done
echo
echo "$pass passed, $fail failed${failed:+ —$failed}"
exit $([ $fail -eq 0 ] && echo 0 || echo 1)
