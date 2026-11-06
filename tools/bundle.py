# The working copy is split in three (so the test suites load in seconds).
# What gets deployed is a single self-contained file: this script inlines the
# two libraries and stamps the build time into the page.
import os, datetime

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
src  = os.path.join(root, 'src', 'index.html')
out  = os.path.join(root, 'index.html')

s = open(src, encoding='utf-8').read()

for tag, fn in [('<script src="lib-mqtt.js"></script>', 'lib-mqtt.js'),
                ('<script src="lib-qr.js"></script>',   'lib-qr.js')]:
    assert tag in s, 'missing in src/index.html: ' + tag
    body = open(os.path.join(root, 'src', fn), encoding='utf-8').read()
    assert '</script' not in body.lower(), fn + ' would close the script tag early'
    s = s.replace(tag, '<script>\n' + body + '\n</script>', 1)

stamp = datetime.datetime.now().strftime('%d.%m. %H:%M')
s = s.replace('__BUILD__', stamp)

open(out, 'w', encoding='utf-8').write(s)
# the page asks this file whether it is still the newest one in the room
open(os.path.join(root, 'version.txt'), 'w', encoding='utf-8').write(stamp + '\n')
print('bundled %d bytes, version %s -> %s' % (len(s), stamp, out))
