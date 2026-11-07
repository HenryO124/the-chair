#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Import a batch of quiz questions, and refuse the ones that would spoil a night.

Takes three files in the agreed shape — one per language, each row

    [category, question, correct, wrong1, wrong2, wrong3, explanation]

with the correct answer always first — and turns them into the rows this page
actually holds. Everything it refuses, it refuses out loud, with the row and
the reason, so the batch can be fixed rather than guessed at.

The part that matters is the last check. A quiz does not fail because one
question is wrong; it fails because the same fact comes round again in
different words and the room notices. That check runs against the whole
existing bank, in all three languages at once, and it never deletes anything:
a near miss is reported for a person to settle.

    python3 tools/import_quiz.py batch_en.txt batch_fi.txt batch_sv.txt
    python3 tools/import_quiz.py batch_en.txt batch_fi.txt       # fi only, sv = fi
    python3 tools/import_quiz.py ... --write out.json     # once it is clean
"""
import json, re, sys, unicodedata, os

CATS = ["History","Geography","Science","Arts & culture","Sport","Everyday"]
MAXQ = 110          # a question has to fit a television
PAGE = os.path.join(os.path.dirname(__file__), "..", "src", "index.html")

# ---------------------------------------------------------------- normalising
_STOP = set("""a an the of in on at to for and or is are was were did do does
what which who whom whose when where why how many much year years was been
mika mikä mitkä minä missä milloin kuka kuinka monta vuonna oli ovat on ja tai
vilket vilken vilka vem när hur många ar var och eller""".split())

def fold(s):
    s = unicodedata.normalize("NFKD", str(s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", " ", s)

def words(s):
    return [w for w in fold(s).split() if w and w not in _STOP]

def stem(w):
    # crude, deliberately: enough to tie berliinin/berlin/berlins together
    return w[:6] if len(w) > 6 else w

def content(s):
    return set(stem(w) for w in words(s) if len(w) > 2)

# ---------------------------------------------------------------- the checks
def check_batch(en, fi, sv):
    bad = []
    if not (len(en) == len(fi) == len(sv)):
        bad.append("the three files hold %d, %d and %d rows — they must match"
                   % (len(en), len(fi), len(sv)))
        return bad
    seen = {}
    for i, (e, f, s) in enumerate(zip(en, fi, sv)):
        tag = "row %d (%s)" % (i + 1, str(e[1])[:48] if len(e) > 1 else "?")
        for name, r in (("en", e), ("fi", f), ("sv", s)):
            if len(r) != 7:
                bad.append("%s: %s has %d fields, expected 7" % (tag, name, len(r))); continue
            if any(not str(x or "").strip() for x in r):
                bad.append("%s: %s has an empty field" % (tag, name))
            if len(set(fold(x) for x in r[2:6])) != 4:
                bad.append("%s: %s repeats an answer among the four" % (tag, name))
            if len(str(r[1])) > MAXQ:
                bad.append("%s: %s question is %d characters, over %d"
                           % (tag, name, len(str(r[1])), MAXQ))
        if len(e) == 7 and e[0] not in CATS:
            bad.append("%s: category %r is not one of %s" % (tag, e[0], ", ".join(CATS)))
        # A translated question with English answers under it is the failure that
        # looks like success: the batch reads as three languages and the room
        # sees English on the television. Proper nouns are exempt — Vltava is
        # Vltava in every language — so only prose is required to differ.
        for name, r in (("Finnish", f), ("Swedish", s)):
            if len(e) != 7 or len(r) != 7:
                continue
            if fold(e[1]) == fold(r[1]):
                bad.append("%s: the %s question is the English one" % (tag, name))
            if fold(e[6]) == fold(r[6]) and len(str(e[6]).split()) > 2:
                bad.append("%s: the %s explanation is the English one: %r"
                           % (tag, name, str(r[6])[:60]))
            proper = sum(1 for x in r[2:6] if str(x)[:1].isupper())
            if [fold(x) for x in e[2:6]] == [fold(x) for x in r[2:6]] and proper < 4:
                bad.append("%s: the %s answers are the English ones" % (tag, name))
        if len(e) == 7:
            k = fold(e[1])
            if k in seen:
                bad.append("%s: the same question as row %d" % (tag, seen[k] + 1))
            seen[k] = i
    return bad

def load_bank():
    """Every question already in the page, as (question, correct) per language."""
    src = open(PAGE, encoding="utf-8").read()
    out = []
    for name in ("TRIVIA", "TRIVIA_FI", "TRIVIA_SV"):
        m = re.search(r"var %s\s*=\s*(\[.*?\]);\s*\n" % name, src, re.S)
        if not m:
            print("could not find %s in the page" % name); sys.exit(1)
        rows = json.loads(m.group(1))
        off = 1 if name == "TRIVIA" else 0        # only the English row has a category
        out.append([(r[0 + off], r[1 + off]) for r in rows])
    return list(zip(*out))                        # one tuple of three per question

def same_fact(a, b):
    """Two questions, each (question, correct). Do they settle the same thing?"""
    qa, ca = a; qb, cb = b
    if fold(qa) == fold(qb):
        return "word for word"
    wa, wb = content(qa), content(qb)
    if not wa or not wb:
        return None
    share = len(wa & wb) / max(1, min(len(wa), len(wb)))
    if fold(ca) == fold(cb) and len(wa & wb) >= 2:
        return "same answer (%s) and %d words in common" % (str(ca)[:24], len(wa & wb))
    if share >= 0.8:
        return "%d%% of the words in common" % round(share * 100)
    return None

def check_against_page(en, fi, sv):
    bank = load_bank()
    hits = []
    for i, (e, f, s) in enumerate(zip(en, fi, sv)):
        if len(e) != 7:
            continue
        mine = [(e[1], e[2]), (f[1], f[2]), (s[1], s[2])]
        for j, old in enumerate(bank):
            for k in range(3):
                why = same_fact(mine[k], old[k])
                if why:
                    hits.append((i + 1, e[1], j, old[0][0] if k == 0 else old[k][0], why))
                    break
    return hits

# ---------------------------------------------------------------- the output
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = None
    if "--write" in sys.argv:
        write = sys.argv[sys.argv.index("--write") + 1]
    if len(args) == 2:
        # Finnish only, by the owner's decision for now. The Swedish bank has to
        # hold the same number of rows as the other two or the page deals a round
        # it cannot label, so it gets the Finnish text. That is a debt, not a
        # translation, and it is printed as one every single run.
        en, fi = [json.load(open(p, encoding="utf-8")) for p in args]
        sv = [list(r) for r in fi]
        print("note  two files given: the Swedish bank gets the Finnish text for")
        print("      these %d rows. They are playable in fi and en, and read as" % len(fi))
        print("      Finnish on a Swedish television until someone translates them.")
    elif len(args) == 3:
        en, fi, sv = [json.load(open(p, encoding="utf-8")) for p in args]
    else:
        print(__doc__); sys.exit(2)

    bad = check_batch(en, fi, sv)
    if bad:
        print("REFUSED — %d problem(s) in the batch itself:" % len(bad))
        for b in bad: print("  x " + b)
        print("\nNothing was imported. Fix these and run it again.")
        sys.exit(1)
    print("ok  %d questions, three languages, shape and answers clean" % len(en))

    hits = check_against_page(en, fi, sv)
    if hits:
        # One question can match the bank more than once, so count the questions
        # and not the lines: the difference is what is actually importable, and
        # reading it off the lines gets the subtraction wrong.
        rows = sorted(set(h[0] for h in hits))
        print("\n%d match(es) against the bank, behind %d of your %d questions."
              % (len(hits), len(rows), len(en)))
        print("Drop all of them and %d remain importable." % (len(en) - len(rows)))
        print("These are NOT thrown away — read them and decide:\n")
        for n, q, j, old, why in hits[:40]:
            print("  row %d  %s" % (n, q[:70]))
            print("     bank #%d  %s" % (j, str(old)[:70]))
            print("     -> %s\n" % why)
        if len(hits) > 40: print("  ... and %d more" % (len(hits) - 40))
    else:
        print("ok  nothing here is already in the bank, in any language")

    rows = {"en": en, "fi": [r[1:] for r in fi], "sv": [r[1:] for r in sv]}
    if write:
        json.dump(rows, open(write, "w", encoding="utf-8"), ensure_ascii=False)
        print("\nwrote %s — %d rows ready to splice" % (write, len(en)))
    else:
        print("\nAdd --write out.json once you are happy with the overlaps above.")

if __name__ == "__main__":
    main()
