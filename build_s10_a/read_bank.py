import json, re, sys
s = open('/home/claude/the-chair/src/index.html', encoding='utf-8').read()
m = re.search(r'var S10BANK\s*=\s*(\[.*?\]);', s, re.S)
raw = m.group(1)
rows = json.loads(re.sub(r',\s*\]', ']', raw))
print("total", len(rows))
from collections import Counter
print(Counter(r[0] for r in rows))
for r in rows:
    if r[0] in ('History','Geography','Science'):
        print(r[0], "|", r[1])
