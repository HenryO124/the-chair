# The working copy is split in three (so the test suites load in seconds).
#
# What gets deployed used to be a single self-contained file. It is now one
# HTML file plus three files beside it, because a guest who opens an
# invitation link needs the join form and nothing else: not the record
# catalogue, not three quiz banks, not the picture tables, not the QR
# generator. Those now travel separately and the page fetches them when
# something actually asks.
#
#   index.html    the page: shell, styles, logic
#   lib-mqtt.js   the party library, fetched after the document is parsed
#   lib-qr.js     the lobby QR, fetched the first time a QR is drawn
#   banks.js      the catalogue and the question banks, fetched by the host
#
# src/index.html is NOT split: every bank stays where it is, between the
# markers the generator scripts look for, so src/index.html still runs on its
# own as one complete page and tools that rewrite the banks keep working.
# The cutting happens here, on the way out.
import os, re, datetime, shutil, sys

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
srcd = os.path.join(root, 'src')
out  = os.path.join(root, 'index.html')

s = open(os.path.join(srcd, 'index.html'), encoding='utf-8').read()
orig_len = len(s)

def die(msg):
    print('bundle.py: ' + msg)
    sys.exit(1)

# ---------------------------------------------------------------------------
# 1. The two libraries stop being inlined. They become siblings, and the page
#    loads them itself through chunkLoad(), so the tags go away entirely.
for tag, fn in [('<script src="lib-mqtt.js"></script>', 'lib-mqtt.js'),
                ('<script src="lib-qr.js"></script>',   'lib-qr.js')]:
    if tag not in s:
        die('missing in src/index.html: ' + tag)
    s = s.replace(tag, '<!-- ' + fn + ' is fetched by chunkLoad() when wanted -->', 1)
    shutil.copyfile(os.path.join(srcd, fn), os.path.join(root, fn))

if 'function chunkLoad(' not in s:
    die('src/index.html has no chunkLoad() — apply the payload-split patch first')

# ---------------------------------------------------------------------------
# 2. Cut the data out into banks.js.
#
# Five of the blocks sit between generated-code markers; cut those whole, so
# whatever the generators put inside travels with them. CATALOG and
# SEEDVIDEOS have no markers, so they are found by their declaration.
MARKED = [
    ('quiz bank en',  '/* ---- quiz bank en: generated, do not edit by hand ---- */',
                      '/* ---- end quiz bank en ---- */'),
    ('quiz bank fi',  '/* ---- quiz bank fi: generated, do not edit by hand ---- */',
                      '/* ---- end quiz bank fi ---- */'),
    ('quiz bank sv',  '/* ---- quiz bank sv: generated, do not edit by hand ---- */',
                      '/* ---- end quiz bank sv ---- */'),
    ('pictures',      '/* ---- pictures: generated, do not edit by hand ---- */',
                      '/* ---- end pictures ---- */'),
    ('true or false', '/* ---- true or false: generated, do not edit by hand ---- */',
                      '/* ---- end true or false ---- */'),
]

# every global the chunk is allowed to define; the page declares each as an
# empty placeholder so a function body can mention one before it arrives
PLACEHOLDERS = [
    ('CATALOG',    '[]'),
    ('SEEDVIDEOS', '{}'),
    ('TRIVIA',     '[]'),
    ('TRIVIA_FI',  '[]'),
    ('TRIVIA_SV',  '[]'),
    ('QIMG',       '{}'),
    ('PICTURES',   '[]'),
    ('PICASK',     '{en:{}}'),
    ('PICCAT',     '{en:{}}'),
    ('TFBANK',     '[]'),
]
NAMES = [n for n, _ in PLACEHOLDERS]

chunks = []

def undeclare(text):
    """const TRIVIA=[...]  ->  TRIVIA=[...]   (the page declares them instead)"""
    for n in NAMES:
        text = re.sub(r'(?m)^(?:var|const|let)\s+(' + n + r')\s*=', r'\1=', text)
    return text

for label, head, foot in MARKED:
    i = s.find(head)
    if i < 0:
        die('marker missing: ' + head)
    j = s.find(foot, i)
    if j < 0:
        die('closing marker missing: ' + foot)
    j += len(foot)
    chunks.append('/* ---- ' + label + ' ---- */\n' + undeclare(s[i:j]).strip())
    s = s[:i] + s[j:]

def stmt_end(text, start):
    """Offset just past the `;` that ends the statement beginning at start.

    Counts bracket depth and steps over strings, template literals, regex-ish
    character classes and comments, so a declaration that ends in something
    like `].filter(a=>a[3]>0);` is found correctly rather than guessed at from
    the shape of a line. Guessing is what ate three declarations the first
    time this ran.
    """
    i, n = start, len(text)
    depth = 0
    while i < n:
        c = text[i]
        if c in '"\'`':                            # a string: skip to its close
            q, i = c, i + 1
            while i < n:
                if text[i] == '\\':
                    i += 2; continue
                if text[i] == q:
                    i += 1; break
                i += 1
            continue
        if c == '/' and i + 1 < n and text[i+1] == '/':
            nl = text.find('\n', i)
            i = n if nl < 0 else nl + 1
            continue
        if c == '/' and i + 1 < n and text[i+1] == '*':
            e = text.find('*/', i + 2)
            i = n if e < 0 else e + 2
            continue
        if c in '([{':
            depth += 1
        elif c in ')]}':
            depth -= 1
            if depth < 0:
                die('bracket depth went negative while reading from offset %d' % start)
        elif c == ';' and depth == 0:
            return i + 1
        i += 1
    die('never found the end of the statement starting at offset %d' % start)


def cut_decl(name):
    """Lift `const NAME = <whatever> ;` out of the page."""
    global s
    hits = list(re.finditer(r'(?m)^(?:var|const|let)\s+' + name + r'\s*=', s))
    if len(hits) != 1:
        die('expected exactly one declaration of %s, found %d' % (name, len(hits)))
    start = hits[0].start()
    end = stmt_end(s, start)
    if end < len(s) and s[end:end+1] == '\n':
        end += 1
    body = s[start:end]
    if name not in body.split('=')[0]:
        die('cut the wrong thing for ' + name)
    chunks.append('/* ---- ' + name + ' ---- */\n' + undeclare(body).strip())
    s = s[:start] + s[end:]


cut_decl('CATALOG')
cut_decl('SEEDVIDEOS')

# The placeholders go at the very top of the app script, which is the one
# holding the loader. var hoists, so this is before any call can read one.
decl = ('/* ---- the deferred data, declared empty until banks.js lands ---- */\n'
        'var ' + ', '.join(n + '=' + v for n, v in PLACEHOLDERS) + ';\n')
loader_at = s.find('function chunkLoad(')
if loader_at < 0:
    die('lost track of the loader')
open_tag = s.rfind('<script>', 0, loader_at)
if open_tag < 0:
    die('could not find the script tag that holds the app')
at = open_tag + len('<script>')
s = s[:at] + '\n' + decl + s[at:]

# Nothing may be left declaring these in the page: a second declaration
# alongside the placeholder is a syntax error for const/let and a silent
# overwrite for var. The placeholder line itself is the one allowed match.
decl_at = s.find(decl)
decl_end = decl_at + len(decl)
for n in NAMES:
    for stray in re.finditer(r'(?m)^(?:var|const|let)\s+' + n + r'\s*=', s):
        if not (decl_at <= stray.start() < decl_end):
            die('%s is still declared in the page at offset %d' % (n, stray.start()))

banks = ('/* The Chair — the catalogue and the question banks.\n'
         '   Generated by tools/bundle.py out of src/index.html. The page\n'
         '   declares each of these empty and fetches this file when a host\n'
         '   needs it; a guest joining from a phone never asks for it. */\n\n'
         + '\n\n'.join(chunks) + '\n')

if '</script' in banks.lower():
    die('banks.js contains a closing script tag')

# ---------------------------------------------------------------------------
# 3. Stamp the build, and stamp it into the chunk URLs too. _headers is a
#    Netlify file and GitHub Pages ignores it, so a plain banks.js can be
#    served from cache for ten minutes: long enough to pair a fresh
#    index.html with last build's questions. The query string makes that
#    impossible.
stamp = datetime.datetime.now().strftime('%d.%m. %H:%M')
ver = re.sub(r'[^0-9]', '', stamp)

n_sub = 0
for fn in ('lib-mqtt.js', 'lib-qr.js', 'banks.js'):
    s, k = re.subn(r"'" + re.escape(fn) + r"'", "'" + fn + "?v=" + ver + "'", s)
    n_sub += k
if n_sub < 3:
    die('expected the loader to name all three chunks, found %d' % n_sub)

if '__BUILD__' not in s:
    die('no __BUILD__ placeholder in src/index.html')
s = s.replace('__BUILD__', stamp)

# ---------------------------------------------------------------------------
# 4. Write everything out.
open(out, 'w', encoding='utf-8').write(s)
open(os.path.join(root, 'banks.js'), 'w', encoding='utf-8').write(banks)
open(os.path.join(root, 'version.txt'), 'w', encoding='utf-8').write(stamp + '\n')

mq = os.path.getsize(os.path.join(root, 'lib-mqtt.js'))
qr = os.path.getsize(os.path.join(root, 'lib-qr.js'))
print('bundled version %s' % stamp)
print('  index.html   %7d bytes   (was %d as one file)' % (len(s), orig_len))
print('  banks.js     %7d bytes   host only' % len(banks))
print('  lib-mqtt.js  %7d bytes   after the document' % mq)
print('  lib-qr.js    %7d bytes   first QR only' % qr)
print('  a guest is sent index.html + lib-mqtt.js = %d bytes before gzip' % (len(s) + mq))
