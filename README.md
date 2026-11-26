[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Fawulana/u-azazex-one-line-one-chill-6d4d5488-entry/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/Fawulana/u-azazex-one-line-one-chill-6d4d5488-entry/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

# One Line, One Chill

A single sentence of horror, written by a program, judged head to head
against other one-line frights on how frightening, vivid and original it is.

## The line

> I watched the feed from my bed as, at 3:17 in the morning, a man wearing
> my face and my coat stood waiting on my porch, smiled straight into the
> doorbell camera, and mouthed: let me in.

The scare is built from ordinary, specific things — a doorbell camera feed,
a timestamp, the narrator's own coat — so the impossible part lands without
any announcement. The man outside is never explained and never gets in
during the line; the dread is what he is still doing out there, patiently,
wearing the narrator's face better than a stranger should be able to. The
sentence holds its one quiet request back to the very end, so the last
three words are the blow: he is not breaking in, he is asking — and he
expects to be obeyed.

## How the program works

`main.py` (Python 3, standard library only) holds the line as a fixed
constant and writes it, UTF-8 encoded, to `/output/entry.txt`, creating
`/output` first if needed. It takes no input, uses no randomness and no
network, so every run produces byte-identical output — one sentence, well
under the competition's 200-character gate.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```
