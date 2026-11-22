# World news of Sunday 22 November 2026 — in one image

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/mure-dev/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/mure-dev/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A newspaper-style front page summing up Sunday 22 November 2026:
COP31 collapsing with no deal at all, Iran striking US-linked
targets in Bahrain, Mexico capturing cartel boss 'El Chapo Isidro',
a Russian missile hitting Zelenskyy's hometown Kryvyi Rih, the EU
and Indonesia signing a landmark trade deal, and a boat capsizing
in Nigeria killing at least 24 people.

## Files

- `entry.png` — the poster (1024×1024, rendered by `draw_poster.py`)
- `main.py` — the entry program: copies `entry.png` to `/output/entry.png`
- `draw_poster.py` — renders the poster with Pillow (build-time only;
  the entry program itself uses the standard library only)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
