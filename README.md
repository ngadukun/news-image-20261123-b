# THE WORLD TODAY — Monday, 23 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/ngadukun/news-image-20261123-b/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/ngadukun/news-image-20261123-b/reward.svg)](https://make.fun/bounty/news-image-20261123)

A one-image newspaper front page summing up the world news of **Monday
23 November 2026**, built for the make.fun bounty
[news-image-20261123](https://make.fun/bounty/news-image-20261123).

## The entry

- `main.py` — the entry program (Python 3.13, standard library only).
  It copies `entry.png` to `/output/entry.png`, byte for byte, on every
  run. Outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in
  for `/output`:

  ```
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
  ```

- `entry.png` — the front page itself: 1000 × 1024 px PNG, ~203 KB.
- `render.py` — the program that drew the front page with Pillow
  (layout, typography and story text all live there). Run it to
  regenerate `entry.png`:

  ```
  python3 render.py
  ```

## The day's stories, and where they were reported

Compiled on 23 November 2026 from wire and newsroom reporting:

- **COP31 talks collapse without a deal** — AFP via NAMPA, 23 Nov 2026:
  Australian PM Anthony Albanese attributes the failure to "difficult
  geopolitical times"; the contentious deal collapsed over fossil fuels
  as the summit in Türkiye stretched into record overtime, and
  Türkiye's final draft did not mention the words "fossil fuels"
  (also The Daily Jagran and Observer Voice headline roundups, 23 Nov).
- **Russian strikes kill 12 in the Kyiv region** — AFP, Dymer dateline,
  23 Nov 2026 (death toll updated from 11 to 12 during the day);
  Zelensky: Russia fired 165 missiles, ~2,700 drones and ~1,460 glide
  bombs in a week, and US Patriot delays are "difficult to understand"
  (The Kyiv Independent, 21–22 Nov developments, via Europe Says).
- **Iran strike wounds two in Bahrain** — AFP via NAMPA, 22 Nov 2026:
  Saudi Arabia condemns the "criminal" attacks; the Saudi-led
  coalition intercepted a Houthi missile in its western region.
- **Tech sell-off pushes Wall Street into correction** — BBC reporting
  via PAN: S&P 500 −3.7% and Dow −1.9% close in correction territory,
  Nasdaq −5.3%; Anthropic −8.5% back toward its $83 IPO price, Nvidia
  −13.7% (Friday's close); The Guardian: Nasdaq erases its 2026 gains,
  Asian markets' worst week since 2020.
- **Dozens missing in Indonesian factory fire** — Reuters, Jakarta,
  22 Nov 2026: police removed 24 body bags from the PT Fonusa Agung
  Mulia candy factory in Cikande, Serang, Banten; the search for the
  missing resumes Monday; victims unidentifiable, DNA testing may take
  two to three weeks (also AFP via NAMPA; The Business Standard).
- **ICJ: Myanmar committed genocide** — Human Rights Watch and FIDH on
  the International Court of Justice judgment of 19 Nov 2026 (nine
  votes to six; reparations ordered); Myanmar's government calls ASEAN
  criticism "unfair and imbalanced" (headline roundups, 23 Nov).
- **Sport** — India post a record 720/9 declared in the Wellington Test
  against New Zealand; Anupama defends her IBSF World Women's Snooker
  Championship title (Observer Voice / The Daily Jagran, 23 Nov).
- **Briefs** — South Korea's education minister quits over an AI
  exam-cheating scandal (AFP); Mexico captures "El Chapo Isidro", the
  cartel boss on the FBI's most-wanted list, 11 killed in firefights;
  Brazil's ex-president Bolsonaro "stable" in intensive care (AFP);
  Nepal PM Balendra Shah's state visit to India and talks with PM Modi.

## License

MIT — see `LICENSE`.
