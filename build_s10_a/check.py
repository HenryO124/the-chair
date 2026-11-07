# -*- coding: utf-8 -*-
import json, re, sys
from collections import Counter

rows = json.load(open('/home/claude/the-chair/batch_s10_a.json', encoding='utf-8'))
src = open('/home/claude/the-chair/src/index.html', encoding='utf-8').read()
bank = json.loads(re.sub(r',\s*\]', ']', re.search(r'var S10BANK\s*=\s*(\[.*?\]);', src, re.S).group(1)))
bank_en = {r[1].strip().lower() for r in bank}
bank_fi = {r[2].strip().lower() for r in bank}

bad = []
qlen = []
for i, r in enumerate(rows):
    t = 'row %d' % i
    assert isinstance(r, list)
    if len(r) != 8: bad.append(t + ' not 8 fields')
    cat, qe, qf, qs, ee, ef, es, cands = r
    if cat not in ('History','Geography','Science'): bad.append(t+' cat')
    for n, v in (('qe',qe),('qf',qf),('qs',qs),('ee',ee),('ef',ef),('es',es)):
        if not isinstance(v, str) or not v.strip(): bad.append('%s empty %s' % (t,n))
    if qf != qs: bad.append(t+' sv question != fi')
    if ef != es: bad.append(t+' sv expl != fi')
    if qf == qe: bad.append(t+' fi question == en')
    if ef == ee: bad.append(t+' fi expl == en')
    qlen.append(max(len(qe), len(qf)))
    if len(qe) > 110 or len(qf) > 110: bad.append('%s question too long (%d/%d)' % (t,len(qe),len(qf)))
    if len(cands) != 10: bad.append('%s %d candidates' % (t,len(cands)))
    b = 0
    for c in cands:
        if len(c) != 4: bad.append('%s cand %r fields' % (t,c)); continue
        ce, cf, cs, fl = c
        if not all(isinstance(x,str) and x.strip() for x in (ce,cf,cs)): bad.append('%s cand empty %r'%(t,c))
        if cf != cs: bad.append('%s cand sv != fi %r'%(t,c))
        if fl not in (0,1): bad.append('%s cand flag %r'%(t,fl))
        b += fl
    if not 4 <= b <= 6: bad.append('%s belongs=%d' % (t,b))
    if qe.strip().lower() in bank_en: bad.append(t+' EN question already in bank')
    if qf.strip().lower() in bank_fi: bad.append(t+' FI question already in bank')

qe_all = [r[1].strip().lower() for r in rows]
qf_all = [r[2].strip().lower() for r in rows]
for k,v in Counter(qe_all).items():
    if v>1: bad.append('duplicate EN question in batch: %r' % k)
for k,v in Counter(qf_all).items():
    if v>1: bad.append('duplicate FI question in batch: %r' % k)

print('rows', len(rows), dict(Counter(r[0] for r in rows)))
print('belongs distribution', dict(Counter(sum(c[3] for c in r[7]) for r in rows)))
print('max question length', max(qlen), '| mean', round(sum(qlen)/len(qlen),1))
print('non-ascii present in FI fields:', any(any(ord(ch)>127 for ch in r[2]) for r in rows))
print('PROBLEMS:', len(bad))
for x in bad: print('  -', x)
