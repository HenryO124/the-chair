#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the Everyday batch into the two JSON files the importer takes."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import part1, part2, part3, part4  # noqa: E402

ROWS = part1.ROWS + part2.ROWS + part3.ROWS + part4.ROWS
CAT = "Everyday"
MAXQ = 110

en, fi, problems = [], [], []
seen_en, seen_fi = {}, {}

for i, r in enumerate(ROWS, 1):
    if len(r) != 12:
        problems.append("row %d has %d fields, expected 12" % (i, len(r)))
        continue
    qe, ce, w1e, w2e, w3e, xe, qf, cf, w1f, w2f, w3f, xf = r
    en.append([CAT, qe, ce, w1e, w2e, w3e, xe])
    fi.append([CAT, qf, cf, w1f, w2f, w3f, xf])
    for name, q, answers, expl in (("en", qe, (ce, w1e, w2e, w3e), xe),
                                   ("fi", qf, (cf, w1f, w2f, w3f), xf)):
        if len(q) > MAXQ:
            problems.append("row %d %s: question %d chars - %s" % (i, name, len(q), q))
        if len(set(a.strip().lower() for a in answers)) != 4:
            problems.append("row %d %s: repeated answer" % (i, name))
        if not expl.strip():
            problems.append("row %d %s: empty explanation" % (i, name))
    if qe.strip().lower() == qf.strip().lower():
        problems.append("row %d: fi question is the English one" % i)
    if xe.strip().lower() == xf.strip().lower():
        problems.append("row %d: fi explanation is the English one" % i)
    for d, q in ((seen_en, qe), (seen_fi, qf)):
        k = q.strip().lower()
        if k in d:
            problems.append("row %d duplicates row %d: %s" % (i, d[k], q))
        d[k] = i

# answers identical to English with fewer than 4 capitalised -> importer refuses
for i, (e, f) in enumerate(zip(en, fi), 1):
    same = [x.strip().lower() for x in e[2:6]] == [x.strip().lower() for x in f[2:6]]
    proper = sum(1 for x in f[2:6] if x[:1].isupper())
    if same and proper < 4:
        problems.append("row %d: fi answers equal the English ones, only %d capitalised: %s"
                        % (i, proper, f[2:6]))

print("%d rows assembled" % len(en))
if problems:
    print("\n%d problem(s):" % len(problems))
    for p in problems:
        print("  x " + p)
else:
    print("local checks clean")

out = os.path.join(HERE, "..")
json.dump(en, open(os.path.join(out, "batch_everyday_en.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
json.dump(fi, open(os.path.join(out, "batch_everyday_fi.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote batch_everyday_en.json and batch_everyday_fi.json")
