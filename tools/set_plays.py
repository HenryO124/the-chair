#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write the list of records a person has heard and approved into the page.

records.html hands back {"Artist | First single": 1, ...}. Those keys are
videoKey(a) — the act and its debut single, which is what the game plays — and
the game will only deal a record that has either a saved video or a key in
here. So this is the gate, and it is opened by a person, not by a machine.

Merges by default: a second pass adds to the first rather than replacing it,
because the page is gone through in sittings. --replace throws the old set away.

    python3 tools/set_plays.py takes.json
    python3 tools/set_plays.py takes.json --replace
    cat takes.json | python3 tools/set_plays.py -
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "src", "index.html")
HEAD = "/* ---- playable: generated, do not edit by hand ---- */"
FOOT = "/* ---- end playable ---- */"


def die(msg):
    print("set_plays.py: " + msg)
    sys.exit(1)


def catalogue(src):
    """Every [artist, ..., first single, ...] row, as the page holds them."""
    m = re.search(r"(?m)^(?:var|const)\s+CATALOG\s*=\s*\[", src)
    if not m:
        die("no CATALOG in the page")
    i = src.index("[", m.start())
    d = 0
    for j in range(i, len(src)):
        if src[j] == "[":
            d += 1
        elif src[j] == "]":
            d -= 1
            if d == 0:
                break
    text = re.sub(r",\s*\]$", "]", src[i:j + 1])
    return json.loads(text)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    replace = "--replace" in sys.argv
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)

    raw = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    try:
        taken = json.loads(raw)
    except Exception as e:
        die("that is not JSON: %s" % e)
    if not isinstance(taken, dict):
        die("expected an object of keys, got %s" % type(taken).__name__)

    src = open(PAGE, encoding="utf-8").read()
    rows = catalogue(src)
    known = set("%s | %s" % (r[0], r[5]) for r in rows)

    # A key that matches no record is not a near miss to be fixed up quietly:
    # it would sit in the gate forever opening nothing. Say which ones.
    stray = sorted(k for k in taken if k not in known)
    good = sorted(k for k in taken if k in known)

    i = src.find(HEAD)
    j = src.find(FOOT)
    if i < 0 or j < 0:
        die("the page has no playable block to write into")
    old = {}
    m = re.search(r"PLAYS\s*=\s*(\{.*?\})\s*;", src[i:j], re.S)
    if m:
        try:
            old = json.loads(m.group(1))
        except Exception:
            old = {}

    merged = {} if replace else dict(old)
    for k in good:
        merged[k] = 1

    body = (HEAD + "\nvar PLAYS=" + json.dumps(merged, ensure_ascii=False, sort_keys=True)
            + ";\n" + FOOT)
    src = src[:i] + body + src[j + len(FOOT):]
    open(PAGE, "w", encoding="utf-8").write(src)

    # What this actually changes on the night: how many records can be dealt.
    saved = set()
    ms = re.search(r"(?m)^(?:var|const)\s+SEEDVIDEOS\s*=\s*(\{.*?\})\s*;\s*\n", src, re.S)
    if ms:
        try:
            saved = set(json.loads(ms.group(1)).keys())
        except Exception:
            saved = set()
    playable = set(merged) | saved

    print("%d key(s) given, %d matched a record" % (len(taken), len(good)))
    if stray:
        print("\n%d key(s) matched nothing in the catalogue:" % len(stray))
        for k in stray:
            print("   ? " + k)
        print("   (these were left out — check the spelling against the catalogue)")
    if not replace and old:
        print("\nmerged with the %d already there -> %d in the gate" % (len(old), len(merged)))
    print("\nName the Artist can now deal %d of %d records%s."
          % (len(playable & known), len(known),
             " (%d of them from a saved video)" % len(saved & known) if saved else ""))


if __name__ == "__main__":
    main()
