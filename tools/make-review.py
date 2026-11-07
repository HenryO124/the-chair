#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the picture review page from whatever the picture maker has produced.

The maker refuses a candidate the moment anything looks wrong, which is right
for a machine working alone and wrong as a final answer: most of its refusals
are guesses from a file name. This turns them back into a question a person can
answer in a second, newest refusals first, with the picture actually on screen.
"""
import json, os, sys, html

SRC = sys.argv[1] if len(sys.argv) > 1 else '/tmp/picmore2'
OUT = '/home/claude/the-chair/review-pictures.html'

def load(name):
    p = os.path.join(SRC, name)
    if not os.path.exists(p): return []
    try:
        d = json.load(open(p, encoding='utf-8'))
    except Exception as e:
        print('could not read %s: %s' % (name, e)); return []
    return d if isinstance(d, list) else list(d.values())

rejected = load('rejected.json')
accepted = load('candidates.json')

# A machine is right about these and a person cannot help: no picture to look at,
# or a licence that is not ours to use.
HOPELESS = ('mediatype is', 'not a still photograph', 'GFDL', 'licence', 'license',
            'no image', 'no file', 'missing')
def worth_asking(r):
    why = str(r.get('why') or r.get('reason') or '')
    return not any(h.lower() in why.lower() for h in HOPELESS)

ask = [r for r in rejected if worth_asking(r)]

def url_of(r):
    for k in ('url', 'image', 'img', 'src'):
        if r.get(k): return r[k]
    f = r.get('file') or ''
    if not f: return ''
    return 'https://commons.wikimedia.org/wiki/Special:FilePath/' + f.replace(' ', '_') + '?width=1000'

# Put the refusals a person is most likely to overturn first, and show only a
# few pictures of any one subject: forty photographs of Sibelius is one answer,
# not forty, and the next person in the list is worth more than his eleventh
# portrait.
# What a person can actually overturn. A photograph rejected for its shape or
# a few missing pixels may still be a fine round; a funeral, a grave or a
# statue is not a photograph of the person at all, however the machine phrased
# it, and putting those first wasted the first minute of the owner's time.
NEVER = ('funeral', 'grave', 'cemetery', 'memorial', 'monument', 'statue',
         'plaque', 'stamp', 'banknote', 'coin', 'bust', 'painting of',
         'congress', 'conference', 'parade', 'crowd')
def hopeless_subject(r):
    hay = (str(r.get('why') or r.get('reason') or '') + ' ' + str(r.get('file') or '')).lower()
    return any(w in hay for w in NEVER)

def value(r):
    why = str(r.get('why') or r.get('reason') or '').lower()
    if 'not landscape' in why:   return 0   # a television can letterbox a portrait
    if 'too small' in why:       return 1   # borderline, and the owner can see it
    if 'more than one person' in why: return 2
    return 3

# One picture is one question, so one picture per subject is all there is to
# decide. Sixty-four people, sixty-four calls.
PER_SUBJECT = 1
# A television cannot use a picture that is not there. Whatever the reason
# given, if the long side is under 800 pixels the answer is no and there is
# nothing to ask.
import re as _re
def big_enough(r):
    m = _re.search(r'(\d{2,5})\s*[x\u00d7]\s*(\d{2,5})', str(r.get('why') or ''))
    if not m: return True
    return max(int(m.group(1)), int(m.group(2))) >= 800
ask = [r for r in ask if not hopeless_subject(r) and big_enough(r)]
ask.sort(key=value)
seen_subject = {}
kept = []
for r in ask:
    sub = r.get('subject') or r.get('name') or '?'
    n = seen_subject.get(sub, 0)
    if n >= PER_SUBJECT: continue
    seen_subject[sub] = n + 1
    kept.append(r)
ask = kept

rows = []
for r in ask:
    rows.append({
        'subject': r.get('subject') or r.get('name') or '?',
        'topic':   r.get('topic') or '',
        'why':     r.get('why') or r.get('reason') or '',
        'file':    r.get('file') or '',
        'url':     url_of(r),
    })

print('%d refusals, %d worth asking about, %d shown (at most %d a subject, %d subjects)'
      % (len(rejected), len(ask), len(rows), PER_SUBJECT, len(seen_subject)))
print('%d already accepted' % len(accepted))

DATA = json.dumps(rows, ensure_ascii=False)
page = open('/home/claude/the-chair/tools/review.tpl.html', encoding='utf-8').read()
open(OUT, 'w', encoding='utf-8').write(page.replace('/*__DATA__*/[]', DATA))
print('wrote ' + OUT)
