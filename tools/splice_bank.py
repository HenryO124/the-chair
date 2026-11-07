#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append rows to one of the page's generated banks, and refuse what would spoil it.

The quiz has its own importer because it is three parallel arrays. These banks
are one array each, every row carrying all three languages, so one tool does
all of them:

    FINGERS   [tone, en, fi, sv]
    NEAR      [cat, qEn, qFi, qSv, number, explEn, explFi, explSv]
    S10BANK   [cat, qEn, qFi, qSv, explEn, explFi, explSv, [[en,fi,sv,0|1] x10]]

It checks shape, emptiness, the category against the six, the 110-character
television limit, that the Finnish is not simply the English, that nothing in
the batch repeats itself, and that nothing repeats what is already in the page.
It reports; it never quietly drops a row.

    python3 tools/splice_bank.py NEAR batch_near.json --dry
    python3 tools/splice_bank.py NEAR batch_near.json
"""
import json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "src", "index.html")
CATS = ["History", "Geography", "Science", "Arts & culture", "Sport", "Everyday"]
MAXQ = 110

BANKS = {
    "FINGERS": dict(head="/* ---- point the finger: generated, do not edit by hand ---- */",
                    foot="/* ---- end point the finger ---- */",
                    width=4, qi=1, fi=2, sv=3, cat=None, tones=["warm","silly","sharp","daft"]),
    "NEAR":    dict(head="/* ---- closest wins: generated, do not edit by hand ---- */",
                    foot="/* ---- end closest wins ---- */",
                    width=8, qi=1, fi=2, sv=3, cat=0, num=4),
    "S10BANK": dict(head="/* ---- smart ten: generated, do not edit by hand ---- */",
                    foot="/* ---- end smart ten ---- */",
                    width=8, qi=1, fi=2, sv=3, cat=0, ten=7),
}


def die(msg):
    print("splice_bank.py: " + msg); sys.exit(1)


def fold(s):
    s = unicodedata.normalize("NFKD", str(s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def read_bank(src, spec):
    i = src.find(spec["head"])
    j = src.find(spec["foot"], i)
    if i < 0 or j < 0:
        die("the page has no block for this bank")
    m = re.search(r"(?:var|const|let)\s+\w+\s*=\s*(\[.*?\]);", src[i:j], re.S)
    if not m:
        die("could not read the array out of its block")
    return i, j + len(spec["foot"]), json.loads(re.sub(r",\s*\]", "]", m.group(1)))


def check(rows, spec, name, existing):
    bad = []
    seen = {fold(r[spec["qi"]]): -1 for r in existing}
    seen.update({fold(r[spec["fi"]]): -1 for r in existing})
    for n, r in enumerate(rows, 1):
        tag = "row %d (%s)" % (n, str(r[spec["qi"]] if len(r) > spec["qi"] else "?")[:46])
        if not isinstance(r, list) or len(r) != spec["width"]:
            bad.append("%s: %d fields, expected %d" % (tag, len(r), spec["width"])); continue
        for k, v in enumerate(r):
            if k == spec.get("ten") or k == spec.get("num"):
                continue
            if not str(v or "").strip():
                bad.append("%s: field %d is empty" % (tag, k))
        if spec["cat"] is not None and r[spec["cat"]] not in CATS:
            bad.append("%s: category %r is not one of the six" % (tag, r[spec["cat"]]))
        if spec.get("tones") and r[0] not in spec["tones"]:
            bad.append("%s: tone %r is not one of %s" % (tag, r[0], ", ".join(spec["tones"])))
        if len(str(r[spec["qi"]])) > MAXQ or len(str(r[spec["fi"]])) > MAXQ:
            bad.append("%s: the question is over %d characters" % (tag, MAXQ))
        if fold(r[spec["qi"]]) == fold(r[spec["fi"]]):
            bad.append("%s: the Finnish is the English" % tag)
        if "num" in spec and not isinstance(r[spec["num"]], (int, float)):
            bad.append("%s: the answer %r is not a number" % (tag, r[spec["num"]]))
        if "ten" in spec:
            ten = r[spec["ten"]]
            if not isinstance(ten, list) or len(ten) != 10:
                bad.append("%s: %s candidates, expected exactly 10"
                           % (tag, len(ten) if isinstance(ten, list) else "?"))
            else:
                if any(not isinstance(c, list) or len(c) != 4 for c in ten):
                    bad.append("%s: a candidate is not [en, fi, sv, 0 or 1]" % tag)
                else:
                    right = sum(1 for c in ten if c[3] == 1)
                    if not 1 <= right <= 9:
                        bad.append("%s: %d of the ten belong — the game needs some of each"
                                   % (tag, right))
                    if len(set(fold(c[0]) for c in ten)) != 10:
                        bad.append("%s: a candidate appears twice" % tag)
        for key in (fold(r[spec["qi"]]), fold(r[spec["fi"]])):
            if key in seen:
                where = "already in the page" if seen[key] < 0 else "the same as row %d" % seen[key]
                bad.append("%s: %s" % (tag, where))
                break
        seen[fold(r[spec["qi"]])] = n
        seen[fold(r[spec["fi"]])] = n
    return bad


def main():
    argv = sys.argv[1:]
    dry = "--dry" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2 or args[0] not in BANKS:
        print(__doc__); sys.exit(2)
    name, path = args
    spec = BANKS[name]
    rows = json.load(open(path, encoding="utf-8"))
    if not isinstance(rows, list) or not rows:
        die("that file is not a non-empty array")

    src = open(PAGE, encoding="utf-8").read()
    i, j, have = read_bank(src, spec)

    bad = check(rows, spec, name, have)
    if bad:
        print("REFUSED — %d problem(s):" % len(bad))
        for b in bad[:40]:
            print("  x " + b)
        if len(bad) > 40:
            print("  ... and %d more" % (len(bad) - 40))
        print("\nNothing was written.")
        sys.exit(1)
    print("ok  %d rows, shape and languages clean, nothing repeated" % len(rows))

    out = have + [list(r) for r in rows]
    if dry:
        print("dry run: %s would go %d -> %d" % (name, len(have), len(out)))
        return
    body = (spec["head"] + "\nvar " + name + "="
            + json.dumps(out, ensure_ascii=False) + ";\n" + spec["foot"])
    open(PAGE, "w", encoding="utf-8").write(src[:i] + body + src[j:])
    print("%s  %d -> %d" % (name, len(have), len(out)))


if __name__ == "__main__":
    main()
