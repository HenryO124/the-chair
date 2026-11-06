# Raw content, as the writers left it

These are the working files the content and picture agents produced. The game
does not read them: everything in here has already been merged into
`src/index.html`, or is waiting to be. They are kept because the agents run in
a scratch directory that does not survive a session, and losing a night of
verified questions to a cleaned-up container would be a bad way to lose it.

| folder | what is in it |
|---|---|
| `cm/` | quiz questions, their fact-checker verdicts, and the merge and insert scripts |
| `tf/` | the True or False statements |
| `s10/` | the Smart Ten sets |
| `pg2/` | Picture Guess subjects and their Commons images |
| `qimg2/` | pictures for the quiz rows added on 6 November |
| `curator/` | the picture curator's image-first batches |

`cm/insert_bank.py` rewrites the three quiz arrays in `src/index.html` between
its markers and can be run again without the file drifting. Run `merge_bank.py`
and `validate_bank.py` before it; the validator exits non-zero if anything is
wrong, and it is worth believing.
