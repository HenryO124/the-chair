# -*- coding: utf-8 -*-
"""Build /home/claude/the-chair/batch_s10_a.json from the data_*.py tables.

Swedish is a recorded debt: the Finnish string is copied into the Swedish slot
everywhere (question, explanation and every candidate).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from data_history import HISTORY
from data_geography import GEOGRAPHY
from data_science import SCIENCE

OUT = "/home/claude/the-chair/batch_s10_a.json"
SRC = "/home/claude/the-chair/src/index.html"

CATS = [("History", HISTORY), ("Geography", GEOGRAPHY), ("Science", SCIENCE)]


def build():
    rows = []
    for cat, sets in CATS:
        for q_en, q_fi, e_en, e_fi, cands in sets:
            cc = [[c_en, c_fi, c_fi, int(b)] for c_en, c_fi, b in cands]
            rows.append([cat, q_en, q_fi, q_fi, e_en, e_fi, e_fi, cc])
    return rows


def existing_questions():
    s = open(SRC, encoding="utf-8").read()
    m = re.search(r"var S10BANK\s*=\s*(\[.*?\]);", s, re.S)
    bank = json.loads(re.sub(r",\s*\]", "]", m.group(1)))
    return bank


def norm(q):
    q = q.lower()
    q = re.sub(r"[^a-z0-9 ]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()
    stop = {"which", "of", "these", "are", "were", "was", "is", "the", "a", "an",
            "in", "on", "at", "by", "to", "from", "their", "its", "has", "have",
            "had", "that", "did", "do", "does", "and", "or", "as", "for", "with",
            "year", "years", "than", "more", "only", "all", "been", "be", "men",
            "people", "things", "country", "countries", "city", "cities"}
    return frozenset(w for w in q.split() if w not in stop)


def validate(rows, bank):
    errs = []
    seen_q = {}
    bank_q = [(r[0], r[1], norm(r[1])) for r in bank]

    for i, r in enumerate(rows):
        tag = "row %d [%s] %r" % (i, r[0], r[1][:60])
        if len(r) != 8:
            errs.append("%s: has %d fields, not 8" % (tag, len(r)))
            continue
        cat, q_en, q_fi, q_sv, e_en, e_fi, e_sv, cands = r
        if cat not in ("History", "Geography", "Science"):
            errs.append("%s: bad category %r" % (tag, cat))
        for name, v in (("q_en", q_en), ("q_fi", q_fi), ("q_sv", q_sv),
                        ("e_en", e_en), ("e_fi", e_fi), ("e_sv", e_sv)):
            if not isinstance(v, str) or not v.strip():
                errs.append("%s: empty %s" % (tag, name))
        if q_fi != q_sv or e_fi != e_sv:
            errs.append("%s: Swedish slot is not the Finnish string" % tag)
        if q_fi == q_en:
            errs.append("%s: Finnish question equals the English" % tag)
        if e_fi == e_en:
            errs.append("%s: Finnish explanation equals the English" % tag)
        if len(q_en) > 110:
            errs.append("%s: EN question is %d chars" % (tag, len(q_en)))
        if len(q_fi) > 110:
            errs.append("%s: FI question is %d chars" % (tag, len(q_fi)))
        if len(cands) != 10:
            errs.append("%s: %d candidates, not 10" % (tag, len(cands)))
        belongs = 0
        labels = set()
        for c in cands:
            if len(c) != 4:
                errs.append("%s: candidate %r has %d fields" % (tag, c, len(c)))
                continue
            c_en, c_fi, c_sv, b = c
            if not all(isinstance(x, str) and x.strip() for x in (c_en, c_fi, c_sv)):
                errs.append("%s: empty candidate text in %r" % (tag, c))
            if c_fi != c_sv:
                errs.append("%s: candidate Swedish slot wrong: %r" % (tag, c))
            if b not in (0, 1):
                errs.append("%s: candidate flag %r is not 0 or 1" % (tag, b))
            belongs += b
            if c_en in labels:
                errs.append("%s: duplicate candidate %r" % (tag, c_en))
            labels.add(c_en)
        if not (4 <= belongs <= 6):
            errs.append("%s: %d candidates belong (need 4-6)" % (tag, belongs))

        key = q_en.strip().lower()
        if key in seen_q:
            errs.append("%s: duplicates own row %d" % (tag, seen_q[key]))
        seen_q[key] = i

        n = norm(q_en)
        for bcat, bq, bn in bank_q:
            if bcat != cat or not n or not bn:
                continue
            inter = len(n & bn)
            if inter >= max(2, min(len(n), len(bn))) and inter == len(n) == len(bn):
                errs.append("%s: same as existing bank question %r" % (tag, bq))
        for j in range(i):
            if rows[j][0] != cat:
                continue
            m2 = norm(rows[j][1])
            if m2 and m2 == n:
                errs.append("%s: same wording as own row %d" % (tag, j))
    return errs


def near_bank(rows, bank):
    """Report the closest existing bank question for each new row, for eyeballing."""
    out = []
    for r in rows:
        n = norm(r[1])
        best, score = None, 0.0
        for b in bank:
            if b[0] != r[0]:
                continue
            m = norm(b[1])
            if not m or not n:
                continue
            j = len(n & m) / float(len(n | m))
            if j > score:
                best, score = b[1], j
        if score >= 0.6:
            out.append((round(score, 2), r[0], r[1], best))
    return sorted(out, reverse=True)


if __name__ == "__main__":
    rows = build()
    bank = existing_questions()
    errs = validate(rows, bank)
    from collections import Counter
    print("rows:", len(rows), dict(Counter(r[0] for r in rows)))
    if errs:
        print("\n%d PROBLEMS:" % len(errs))
        for e in errs:
            print(" -", e)
    else:
        print("validation clean")
    near = near_bank(rows, bank)
    if near:
        print("\nclose to existing bank questions (eyeball these):")
        for sc, cat, q, b in near:
            print("  %.2f [%s] %s\n        vs %s" % (sc, cat, q, b))
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print("\nwrote", OUT)
