#!/usr/bin/env python3
"""What the page is known to contain, counted straight out of it.

A deploy that makes any of these numbers go down is almost always an accident:
a stale copy written over the repo, a merge that dropped a block, a bad patch.
That exact thing happened on 7 November and went unnoticed for hours, because
nothing was watching. Now something is.

    python3 tools/facts.py            # print the counts
    python3 tools/facts.py --check    # compare against tools/facts.json, fail on a drop
    python3 tools/facts.py --save     # record the current counts as the new floor
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'index.html')
STORE = os.path.join(ROOT, 'tools', 'facts.json')


def count_rows(block):
    """Top-level entries in a JS array literal, counted by bracket depth."""
    depth, n, instr, esc = 0, 0, None, False
    for ch in block:
        if instr:
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == instr:
                instr = None
            continue
        if ch in '"\'':
            instr = ch
        elif ch in '[{':
            depth += 1
            if depth == 2:
                n += 1
        elif ch in ']}':
            depth -= 1
    return n


def facts():
    s = open(SRC, encoding='utf-8').read()
    out = {'page_bytes': len(s)}
    for name in ('TRIVIA', 'TRIVIA_FI', 'TRIVIA_SV', 'TFBANK', 'S10BANK',
                 'CATALOG', 'PICTURES'):
        m = re.search(r'\b(?:var|const|let) %s\s*=\s*(\[.*?\]);\s*$' % name, s, re.M | re.S)
        out[name] = count_rows(m.group(1)) if m else 0
    # QIMG is an object keyed by row, and is merged in two places
    out['QIMG'] = len(re.findall(r'"\d+"\s*:\s*\{"u"', s))
    out['tests'] = len(open(os.path.join(ROOT, 'tests', 'run.sh'),
                            encoding='utf-8').read().split('ALL="')[1].split('"')[0].split())
    return out


def main():
    now = facts()
    mode = sys.argv[1] if len(sys.argv) > 1 else ''

    if mode == '--save':
        json.dump(now, open(STORE, 'w'), indent=1, sort_keys=True)
        print('recorded:', ', '.join('%s %d' % kv for kv in sorted(now.items())))
        return 0

    if mode != '--check':
        for k in sorted(now):
            print('%-10s %d' % (k, now[k]))
        return 0

    if not os.path.exists(STORE):
        json.dump(now, open(STORE, 'w'), indent=1, sort_keys=True)
        print('no record yet — the current page is now the floor')
        return 0

    was = json.load(open(STORE))
    # a page may shrink a little from honest tidying; a lost block is not little
    slack = {'page_bytes': 0.04}
    lost = []
    for k, old in sorted(was.items()):
        new = now.get(k, 0)
        floor = old * (1 - slack.get(k, 0))
        if new < floor:
            lost.append('%s %d -> %d' % (k, old, new))
    if lost:
        print('REFUSING TO DEPLOY: the page lost content it had before')
        for line in lost:
            print('  ' + line)
        print('If this is deliberate, run: python3 tools/facts.py --save')
        return 1

    grew = ['%s %d -> %d' % (k, was[k], now[k])
            for k in sorted(was) if now.get(k, 0) > was[k]]
    json.dump(now, open(STORE, 'w'), indent=1, sort_keys=True)
    print('content check ok' + ('  (' + ', '.join(grew) + ')' if grew else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
