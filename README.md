# The Chair

A party-play platform for a room full of people and their phones. One host screen,
everyone else joins from their own device.

Two games so far:

- **The Chair** — a blind audition. A record plays, the coaches' chairs are facing
  away, and each coach decides whether to turn. Teams fill up; the night ends when
  every chair is taken.
- **Name the Artist** — the record plays behind a closed curtain and four names
  appear on every phone. The curtain lifts once everyone has answered.

## Playing it

Open the deployed page on the screen everyone can see, create a game, and share the
room code or the QR. Everyone else opens the same address on their phone and takes a
chair. No accounts, no installs.

The devices talk to each other over a public MQTT broker, so they only need to be on
the internet — not on the same wifi.

## Layout

| Path | What it is |
| --- | --- |
| `index.html` | **The deployed page.** One self-contained file. Generated — don't edit it. |
| `src/index.html` | The real source. Loads the two libraries as separate files. |
| `src/lib-mqtt.js` | mqtt.js 5.3.4, for the party layer. |
| `src/lib-qr.js` | qrcode-generator 1.4.4, for the lobby QR. |
| `src/videos.json` | The act catalogue: `"Artist \| Track": "youtube-id"`. |
| `tools/bundle.py` | Inlines the libraries and stamps the build time. |
| `_headers` | Tells the host not to cache the page, so phones get the newest build. |

The split exists for speed: the test suites load `src/index.html` in a couple of
seconds, where a single 500 kB file took minutes.

## Building

```bash
python3 tools/bundle.py
```

That rewrites `index.html` from `src/`. Commit both. Anything pushed to `main` goes
live by itself.

## Videos

Nothing is downloaded or re-hosted. The page embeds YouTube's own player, which is
the route YouTube provides: ads run and views count, so rights holders are paid as
normal. Fine for a private party. Charging admission or playing it in a venue is
public performance and needs the usual licences.

Clips that turn out wrong or blocked can be flagged in the app; a flagged video
never reaches the stage again.
