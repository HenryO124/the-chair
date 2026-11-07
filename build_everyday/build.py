#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the Everyday batch into the two JSON files the importer takes."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import part1, part2, part3, part4  # noqa: E402

# Written, then cut on the owner's rule: a question earns its place only if the
# reveal makes somebody say "I didn't know that". These were correct and sourced
# but hard-and-forgettable, or the same shape asked once too often.
CUT = {
    # knots: obscure without a payoff in the answer
    "Which bowline is tied for wet conditions where other knots slip or jam?",
    "Which friction hitch is the tree climber's own?",
    "Which knot joins the two ends of a length of climbing webbing?",
    "Which hitch is used for heavy towing and for making fast to a bollard?",
    # cheeses: the which-country shape, asked past the point of interest
    "Mahón-Menorca is the protected cheese of which country?",
    "Cabrales and Picón Bejes-Tresviso are blue cheeses of which country?",
    "Bovški sir, Mohant, Nanoški sir and Tolminc are the protected cheeses of which country?",
    "Telemea de Ibănești and Telemea de Sibiu are the protected cheeses of which country?",
    "Džiugas and Liliputas are protected cheeses of which country?",
    "Olomoucké tvarůžky is a protected cheese of which country?",
    # currencies: name-the-currency with nothing behind it
    "What is the currency of Laos?",
    "What is the currency of Myanmar?",
    "What is the currency of Georgia?",
    "What is the currency of Albania?",
    "What is the currency of Paraguay?",
    # a bare synonym, and a coffee nobody will ever meet
    "The gudgeon pin in an engine is also called what?",
    "What is a caffè tobio?",
    # a bare date and a degree length: nothing behind either reveal
    "Since when has Finland had free universal daycare?",
    "How long does a bachelor's degree take at a Finnish university of applied sciences?",
}

ALL = part1.ROWS + part2.ROWS + part3.ROWS + part4.ROWS
ROWS = [r for r in ALL if r[0] not in CUT]
missed = CUT - set(r[0] for r in ALL)
if missed:
    print("warning: cut list did not match %d row(s): %s" % (len(missed), missed))
print("%d written, %d cut, %d kept" % (len(ALL), len(ALL) - len(ROWS), len(ROWS)))

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
