# Where this stood on the night of 6 November 2026

Live at https://henryo124.github.io/the-chair/ — the version is printed at the
foot of the front page and in `version.txt`, and the page offers to reload
itself when it is behind.

## What is playable

Five games. **Quiz** (672 questions), **Picture Guess** (80 subjects),
**True or False** (172 statements), **Smart Ten** (8 sets, one question and ten
candidates of which some are true), and **Name the Artist**. All of them run in
Finnish, Swedish and English, and the deck is dealt evenly across the six
topics so a thin category gets as many questions as a fat one.

**The Chair**, the original game, is built but off the menu: `const SHELVED={chair:1}`
in `src/index.html`. It waits for its videos. Deleting that one entry brings it
back with its engine, its catalogue and its blocking rules intact.

## Running it

    python3 tools/bundle.py     # src/*.js + src/index.html -> index.html, version.txt
    bash tests/run.sh           # twelve suites, all green as of 00:22

A scheduled task runs the suites every morning at 10:23 Helsinki time and
reports; it does not fix anything.

## What is half-finished

- **The payload split.** `/tmp/perf/patch.py` and a replacement `tools/bundle.py`
  were measured and delivered but not applied: a guest's wait on a slow
  connection goes from 8.5 s to 1.9 s, and the bytes they download from 384 KB
  to 166 KB. Read the patch before running it. If `/tmp` is gone, the work is
  gone with it and would have to be done again — it is the largest single
  improvement still outstanding.
- **Smart Ten content.** 8 sets in the game, 50 more being written.
- **Pictures.** 91 of 672 quiz questions have one, all in the first 120 rows.
  Two picture jobs were in flight.
- **The category balance.** History 134 against Sport 74; 63 arts and 66 sport
  questions were being written to bring every category to 140.

## Decided, so as not to relitigate

Henry hosts on GitHub Pages and accepts its ten-minute cache, mitigated by the
version check and by `?v=` on the invitation link. Pictures come from Wikimedia
Commons with author and licence recorded. Questions are written by one agent and
checked by another against fetched sources, never from memory. Nothing reaches
the page without the test suites passing.
