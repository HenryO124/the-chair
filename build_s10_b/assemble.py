# -*- coding: utf-8 -*-
"""Assemble and validate /home/claude/the-chair/batch_s10_b.json."""
import io, json, re, sys, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)

import part_arts, part_sport, part_everyday, part_extra

ROWS = part_arts.ROWS + part_sport.ROWS + part_everyday.ROWS + part_extra.ROWS

# ---- existing bank questions, for duplicate checking
src = io.open(os.path.join(ROOT, 'src', 'index.html'), encoding='utf-8').read()
m = re.search(r'var S10BANK\s*=\s*(\[.*?\]);', src, re.S)
bank = json.loads(re.sub(r',\s*\]', ']', m.group(1)))


def norm(q):
    q = q.lower()
    q = re.sub(r'[^a-z0-9äöå ]', ' ', q)
    q = re.sub(r'\b(which|of|these|the|a|an|in|is|are|do|did|that|have|has)\b', ' ', q)
    return ' '.join(sorted(set(q.split())))


bank_q = {norm(r[1]): r[1] for r in bank}

errs = []
seen = {}
for i, r in enumerate(ROWS):
    tag = 'row %d (%s)' % (i, r[1][:60])
    if len(r) != 8:
        errs.append('%s: %d fields' % (tag, len(r)))
        continue
    for k in range(7):
        if not isinstance(r[k], str) or not r[k].strip():
            errs.append('%s: field %d empty' % (tag, k))
    if r[0] not in ('Arts & culture', 'Sport', 'Everyday'):
        errs.append('%s: bad category %r' % (tag, r[0]))
    if len(r[1]) > 110:
        errs.append('%s: question EN %d chars' % (tag, len(r[1])))
    if len(r[2]) > 110:
        errs.append('%s: question FI %d chars' % (tag, len(r[2])))
    if r[1] == r[2]:
        errs.append('%s: FI question equals EN' % tag)
    if r[2] != r[3]:
        errs.append('%s: SV question not equal to FI' % tag)
    if r[4] == r[5]:
        errs.append('%s: FI explanation equals EN' % tag)
    if r[5] != r[6]:
        errs.append('%s: SV explanation not equal to FI' % tag)
    cands = r[7]
    if not isinstance(cands, list) or len(cands) != 10:
        errs.append('%s: %s candidates' % (tag, len(cands)))
        continue
    n = 0
    cset = set()
    for c in cands:
        if len(c) != 4:
            errs.append('%s: candidate %r has %d fields' % (tag, c, len(c)))
            continue
        if not all(isinstance(x, str) and x.strip() for x in c[:3]):
            errs.append('%s: candidate %r has an empty string' % (tag, c))
        if c[1] != c[2]:
            errs.append('%s: candidate SV != FI: %r' % (tag, c))
        if c[3] not in (0, 1):
            errs.append('%s: candidate flag %r' % (tag, c[3]))
        n += c[3]
        if c[0] in cset:
            errs.append('%s: duplicate candidate %r' % (tag, c[0]))
        cset.add(c[0])
    if not 4 <= n <= 6:
        errs.append('%s: %d belong' % (tag, n))
    k = norm(r[1])
    if k in bank_q:
        errs.append('%s: duplicates existing bank question %r' % (tag, bank_q[k]))
    if k in seen:
        errs.append('%s: duplicates own row %r' % (tag, seen[k]))
    seen[k] = r[1]

print('rows:', len(ROWS))
print('spread:', dict(Counter(r[0] for r in ROWS)))
print('belong distribution:', dict(Counter(sum(c[3] for c in r[7]) for r in ROWS)))
print('max question length:', max(max(len(r[1]), len(r[2])) for r in ROWS))
if errs:
    print('\n%d PROBLEM(S):' % len(errs))
    for e in errs:
        print(' -', e)
    sys.exit(1)

out = os.path.join(ROOT, 'batch_s10_b.json')
io.open(out, 'w', encoding='utf-8').write(
    json.dumps(ROWS, ensure_ascii=False, indent=1))
print('\nwrote', out)
