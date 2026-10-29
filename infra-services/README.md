# Critical utility infrastructure services

Tests Fulton's maintenance-led holding-company thesis (natural gas, power generation, T&D/electrical and water) against public and government data: precedent roll-ups, asset age, demand drivers, fragmentation, market size and margins, cross-unit synergies and platform candidates.

- Interactive dashboard: https://claude.ai/artifact/Qr6MHQ1uWuHrpDkx2gfpJn
- Plain-text answers to the seven questions and the candidate list: [`report.md`](report.md)

## Layout

| Path | What it is |
|---|---|
| `research/workflow_result.json` | Research output: nine research domains, claim checks, consolidated tables, market map, glossary and synthesis |
| `research/candidates_round2.json` | Second candidate pass: website and ownership checks plus new gas, water and T&D names |
| `build_infra.py` | Turns the research into the dashboard datasets in `site-data/` |
| `build_report_md.py` | Writes `report.md` from the datasets |
| `site-data/` | The 18 datasets the dashboard reads |
| `dashboard/` | Page source: `body.html`, `infra.css`, `infra.js`, `layer_titles.json`, `datasets.json` (dataset titles) and `compose_page.py` |

## Rebuild

```
cd infra-services
python3 -I build_infra.py research/workflow_result.json site-data research/candidates_round2.json
python3 -I build_report_md.py site-data report.md
cd dashboard && python3 -I compose_page.py ../../transformer-market/dashboard/index.html layer_titles.json index.html
cd ../.. && python3 -I tools/build_catalog.py . site
```

`compose_page.py` reuses the transformer page's styles, Whitesail header, tables, market-map graph, glossary pop-ups, watchlist timeline and tabs, so both reports share one layout.
