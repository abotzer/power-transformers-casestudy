# Wireless spectrum

An independent market reference on US wireless spectrum, prepared for Fulton Asset Management in response to Jason Kozin's thesis that licensed spectrum becomes significantly more valuable as AI devices and satellite-terrestrial convergence raise demand. It covers demand, substitutes for spectrum, supply and FCC rules, auction and private-sale prices, satellite direct-to-device service, who captures the value, past spectrum bets, markets outside the US and listed ways to get exposure, with probabilistic projections to 2027-2035 (18 quantity forecasts with 80% ranges, 14 event probabilities and four scenarios for 2030).

- Plain-text version (verdict, scenarios, forecasts, key findings, exposure list, signposts): [`report.md`](report.md)

## Layout

| Path | What it is |
|---|---|
| `research/workflow_result.json` | Research output: nine domains with sourced findings, chart data points, records and forecast seeds |
| `research/brief.md` | Digest of the research used by the later stages; `merge_research.py` builds both files from the workflow runs |
| `research/key_claims.json`, `research/verification.json` | The 102 key claims and their independent re-checks |
| `research/forecast_questions.json` | The 32 forecast questions with resolution criteria |
| `research/forecasts.json` | Five forecasting lenses, their aggregate and the chief forecaster's final numbers and scenarios |
| `research/map.json`, `research/glossary.json`, `research/synthesis.json` | Market map, glossary, key findings, watchlist and the listed-exposure list |
| `editorial.py`, `verdict.py` | Report wording: chart titles and notes, tiles, verdict, method and caveats (the verdict quotes the final forecasts) |
| `build_spectrum.py` | Turns the research into the dashboard datasets in `site-data/` |
| `build_report_md.py` | Writes `report.md` from the datasets |
| `site-data/` | The 20 datasets the dashboard reads |
| `dashboard/` | Page source: `body.html`, `spectrum.css`, `spectrum.js`, `layer_titles.json`, `datasets.json` (dataset titles) and `compose_page.py` |

## Rebuild

```
cd wireless-spectrum
python3 -I build_spectrum.py research site-data
python3 -I build_report_md.py site-data report.md
cd dashboard && python3 -I compose_page.py ../../transformer-market/dashboard/index.html ../../infra-services/dashboard layer_titles.json index.html
cd ../.. && python3 -I tools/build_catalog.py . site
```

`compose_page.py` reuses the transformer page's styles, header, tables, market-map graph, glossary pop-ups, watchlist timeline and tabs, and the infra report's verdict box, key-findings pane, tiles and chart engine, so all reports share one layout. This report adds forecast range strips, event probabilities, scenarios and the exposure board.
