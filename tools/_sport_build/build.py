# -*- coding: utf-8 -*-
import importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.abspath(os.path.join(HERE, "..", ".."))
rows = []
for name in ("b01", "b02", "b03", "b04", "b05"):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    rows += mod.Q
    print("%s: %d" % (name, len(mod.Q)))
en = [r[0] for r in rows]; fi = [r[1] for r in rows]
json.dump(en, open(os.path.join(OUT, "batch_sport_en.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
json.dump(fi, open(os.path.join(OUT, "batch_sport_fi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("total %d" % len(rows))
