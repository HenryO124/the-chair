# Tests

    bash tests/run.sh            # everything
    bash tests/run.sh qrflow tf  # just these

Most suites drive the page in jsdom with a fake MQTT broker standing in for the
real one, often with two or three pages at once — a television and its phones.
Those read `src/index.html`, the unbundled source: in the built file the real
mqtt library is inlined and overwrites the fake broker, and every phone then
fails to join, which looks exactly like a bug and is not one.

`fold.js` is different: it drives the built `index.html` in Chromium and
measures where things land on a phone screen.

| suite | what would break if it failed |
|---|---|
| `qrthis`/`qrflow` | the QR and invitation on menu 2, the settings on the waiting page, a picture reaching a phone |
| `home2` | the front page: filters, the list of open rooms, joining by code, the name chip |
| `settings` | the language picker, and the lobby picker agreeing with it |
| `tf` | True or False: two answers, the run that pays more, the quiz left alone |
| `cap2` | eight phones fitting in a room of eight, Back not shutting the room, phones told when it closes |
| `again` | one party, several games, same code, same phones |
| `bank` | 672 questions in three languages, every row playable |
| `leak` | a Picture Guess painting not following the room into another game |
| `tap2` | the answer buttons surviving a stage message — a lost tap is a lost round |
| `shelf` | the shelved game staying off the menu, the other four playable |
| `fold` | the answers sitting above the fold on a small phone |
