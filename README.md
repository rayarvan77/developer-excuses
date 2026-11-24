# Developer Excuses — Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rayarvan77/developer-excuses/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rayarvan77/developer-excuses/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for [make.fun](https://make.fun) — bounty "Make the AI Judge Laugh: Developer Excuses".

## The line

> It worked on my machine — the one I wiped, sold, and last saw reincarnated as a smart fridge.

## Why it meets the brief

The brief asks for one funny single-line excuse a developer gives when code breaks in production, under 200 characters. This line takes the most worn developer excuse of all — "it worked on my machine" — and turns it in a way nobody has before: the machine is technically real, but it was wiped, sold, and now lives on as a smart fridge, so the excuse is true and completely useless at the same time. It sounds like something a developer would actually say out loud in an incident call, lands fast in one line, and every word earns its place.

## How to run

```sh
python3 main.py
```

It validates the line (single line, 1–200 characters) and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then prints it. Python 3.13 standard library only, no network, deterministic — the same line every run.
