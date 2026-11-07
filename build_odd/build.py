#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble batch_odd_en.json and batch_odd_fi.json from the data modules."""
import json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

import data_geo_hist, data_sci_arts, data_sport_every

ROWS = data_geo_hist.ROWS + data_sci_arts.ROWS + data_sport_every.ROWS

DROP = set(int(x) for x in sys.argv[1:] if x.isdigit())

en, fi, bad = [], [], []
for i, (cat, e, f) in enumerate(ROWS, 1):
    if i in DROP:
        continue
    if len(e) != 6 or len(f) != 6:
        bad.append("row %d: %d/%d fields" % (i, len(e), len(f))); continue
    for name, r in (("en", e), ("fi", f)):
        if len(r[0]) > 110:
            bad.append("row %d %s: question %d chars -- %s" % (i, name, len(r[0]), r[0]))
        if len(set(x.strip().lower() for x in r[1:5])) != 4:
            bad.append("row %d %s: repeated answer" % (i, name))
        if any(not str(x).strip() for x in r):
            bad.append("row %d %s: empty field" % (i, name))
    if e[0] == f[0]:
        bad.append("row %d: Finnish question is the English one" % i)
    if e[5] == f[5]:
        bad.append("row %d: Finnish explanation is the English one" % i)
    en.append([cat] + list(e))
    fi.append([cat] + list(f))

if bad:
    print("PROBLEMS:")
    for b in bad:
        print("  x " + b)
    sys.exit(1)

json.dump(en, open(os.path.join(OUT, "batch_odd_en.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=0)
json.dump(fi, open(os.path.join(OUT, "batch_odd_fi.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=0)
print("wrote %d rows" % len(en))
for k, v in collections.Counter(r[0] for r in en).most_common():
    print("  %-16s %d" % (k, v))
