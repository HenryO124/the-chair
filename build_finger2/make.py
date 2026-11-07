# -*- coding: utf-8 -*-
"""Build batch_finger2.json and look hard for near-duplicates."""
import json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rows import ALL

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "src", "index.html")
OUT = os.path.join(HERE, "..", "batch_finger2.json")

src = open(PAGE, encoding="utf-8").read()
m = re.search(r"var FINGERS\s*=\s*(\[.*?\]);", src, re.S)
have = json.loads(re.sub(r",\s*\]", "]", m.group(1)))

STOP = set("""who whom whose would will who's the a an and or to of in on at for with
is are was were be been being do does did have has had you your yours they them their
that this these those it its as if so but not no nor by from up down out off over
their one else somebody anybody everybody nobody most best first last longest
kuka kenet kenelle kene kenen keneen ja tai se on ei joka jonka jossa joka kun
kuin mikä mitä jotta vaikka ihan ja aina koko oma omaa oman olisi ole""".split())

def toks(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return set(w for w in re.findall(r"[a-z0-9]+", s) if w not in STOP and len(w) > 2)

def jac(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / float(len(a | b))

rows = [[t, en, fi, fi] for (t, en, fi) in ALL]

bad = []
for i, r in enumerate(rows):
    if len(r) != 4 or any(not str(x).strip() for x in r):
        bad.append("row %d: shape/empty" % i)
    if r[0] not in ("warm", "silly", "sharp", "daft"):
        bad.append("row %d: tone %r" % (i, r[0]))
    if len(r[1]) > 110 or len(r[2]) > 110:
        bad.append("row %d: too long (%d en / %d fi) %s" % (i, len(r[1]), len(r[2]), r[1]))
    if r[1].strip().lower() == r[2].strip().lower():
        bad.append("row %d: fi == en" % i)

# near-duplicate scan: mine vs existing, and mine vs mine
pairs = []
mine_en = [toks(r[1]) for r in rows]
mine_fi = [toks(r[2]) for r in rows]
ex_en = [toks(r[1]) for r in have]
ex_fi = [toks(r[2]) for r in have]

TH = 0.42
for i, r in enumerate(rows):
    for j, h in enumerate(have):
        s = max(jac(mine_en[i], ex_en[j]), jac(mine_fi[i], ex_fi[j]))
        if s >= TH:
            pairs.append((round(s, 2), "EXISTING", r[1], h[1], r[2], h[2]))
for i in range(len(rows)):
    for j in range(i + 1, len(rows)):
        s = max(jac(mine_en[i], mine_en[j]), jac(mine_fi[i], mine_fi[j]))
        if s >= TH:
            pairs.append((round(s, 2), "MINE", rows[i][1], rows[j][1], rows[i][2], rows[j][2]))

pairs.sort(reverse=True)
if bad:
    print("PROBLEMS:")
    for b in bad:
        print("  x", b)
print("\n%d near-duplicate pairs at >= %.2f" % (len(pairs), TH))
for p in pairs:
    print("  %.2f %-8s %s" % (p[0], p[1], p[2]))
    print("                   %s" % p[3])
    print("           fi      %s" % p[4])
    print("                   %s" % p[5])

from collections import Counter
print("\ntones:", Counter(r[0] for r in rows), "total", len(rows))
json.dump(rows, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", OUT)
