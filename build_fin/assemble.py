# -*- coding: utf-8 -*-
"""Collect every chunk file in this directory and write the two batch files.

Each chunk exposes ROWS, a list of 13-field rows:
    [category, q_en, c_en, w1_en, w2_en, w3_en, expl_en,
               q_fi, c_fi, w1_fi, w2_fi, w3_fi, expl_fi]
"""
import importlib, json, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

CATS = ["History", "Geography", "Science", "Arts & culture", "Sport", "Everyday"]

def main():
    names = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "c*.py")))
    en, fi, bad = [], [], []
    from collections import Counter
    cnt = Counter()
    for n in names:
        mod = importlib.import_module(n)
        for i, r in enumerate(mod.ROWS):
            if len(r) != 13:
                bad.append("%s row %d: %d fields" % (n, i + 1, len(r))); continue
            if r[0] not in CATS:
                bad.append("%s row %d: bad category %r" % (n, i + 1, r[0]))
            cnt[r[0]] += 1
            en.append([r[0]] + r[1:7])
            fi.append([r[0]] + r[7:13])
        print("%-34s %4d" % (n, len(mod.ROWS)))
    if bad:
        print("\n".join(bad)); sys.exit(1)
    json.dump(en, open(os.path.join(OUT, "batch_fin_en.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(fi, open(os.path.join(OUT, "batch_fin_fi.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\ntotal %d" % len(en))
    for c in CATS:
        print("  %-14s %d" % (c, cnt[c]))

main()
