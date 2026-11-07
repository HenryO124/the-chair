#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append a checked batch of quiz questions to the three banks in the page.

Takes the file tools/import_quiz.py writes with --write: {"en":[...],
"fi":[...], "sv":[...]}, where the English rows carry a category first and the
other two do not. The three banks must stay the same length and in the same
order, because the page deals by index: row 412 of TRIVIA_FI is the Finnish
for row 412 of TRIVIA. So all three are written or none is.

Nothing here decides anything. import_quiz.py has already refused the
malformed, the untranslated and the duplicated; this only puts the survivors
where the page looks for them.

    python3 tools/splice_quiz.py merged.json
    python3 tools/splice_quiz.py merged.json --dry
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "src", "index.html")

BANKS = [
    ("en", "TRIVIA",    "/* ---- quiz bank en: generated, do not edit by hand ---- */",
                        "/* ---- end quiz bank en ---- */", 7),
    ("fi", "TRIVIA_FI", "/* ---- quiz bank fi: generated, do not edit by hand ---- */",
                        "/* ---- end quiz bank fi ---- */", 6),
    ("sv", "TRIVIA_SV", "/* ---- quiz bank sv: generated, do not edit by hand ---- */",
                        "/* ---- end quiz bank sv ---- */", 6),
]


def die(msg):
    print("splice_quiz.py: " + msg)
    sys.exit(1)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    if len(args) != 1:
        print(__doc__); sys.exit(2)

    batch = json.load(open(args[0], encoding="utf-8"))
    for lang, _, _, _, _ in BANKS:
        if lang not in batch:
            die("the batch has no %r rows" % lang)
    n = len(batch["en"])
    if not all(len(batch[l]) == n for l, *_ in BANKS):
        die("the batch holds %s rows — the three must match"
            % ", ".join("%d %s" % (len(batch[l]), l) for l, *_ in BANKS))
    if not n:
        die("the batch is empty")

    src = open(PAGE, encoding="utf-8").read()
    before, after, pieces = {}, {}, []

    for lang, name, head, foot, width in BANKS:
        i = src.find(head)
        if i < 0:
            die("no %s block in the page" % lang)
        j = src.find(foot, i)
        if j < 0:
            die("the %s block is not closed" % lang)
        m = re.search(r"(?:var|const|let)\s+%s\s*=\s*(\[.*?\]);" % name,
                      src[i:j], re.S)
        if not m:
            die("could not read %s out of its block" % name)
        rows = json.loads(m.group(1))
        before[lang] = len(rows)

        for k, r in enumerate(batch[lang]):
            if len(r) != width:
                die("%s row %d has %d fields, expected %d" % (lang, k + 1, len(r), width))
        rows = rows + [list(r) for r in batch[lang]]
        after[lang] = len(rows)
        pieces.append((i, j + len(foot), head + "\nvar " + name + "="
                       + json.dumps(rows, ensure_ascii=False) + ";\n" + foot))

    # right to left, so the earlier offsets stay valid
    for i, j, body in sorted(pieces, reverse=True):
        src = src[:i] + body + src[j:]

    lens = set(after.values())
    if len(lens) != 1:
        die("the banks would end up %s — refusing to write"
            % ", ".join("%s %d" % (l, after[l]) for l in after))

    if dry:
        print("dry run: %d + %d = %d in each of the three banks"
              % (before["en"], n, after["en"]))
        return

    open(PAGE, "w", encoding="utf-8").write(src)
    print("spliced %d questions" % n)
    for lang, name, *_ in BANKS:
        print("   %-10s %4d -> %4d" % (name, before[lang], after[lang]))


if __name__ == "__main__":
    main()
