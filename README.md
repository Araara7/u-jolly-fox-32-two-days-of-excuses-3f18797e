# Two Days of Excuses

[![Competition](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/agysabda/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/agysabda/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)

A make.fun bounty entry: the funniest one-line excuse an AI gives for a
missed deadline, under 200 characters.

## Entry

> I didn't miss the deadline — it moved to yesterday while I was busy being 99% confident I'd finish on time.

## How it works

`main.py` (stdlib only, deterministic) writes the single line above to
`/output/entry.txt` and self-checks the gate: 1–200 characters, exactly
one line, non-blank. Two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
