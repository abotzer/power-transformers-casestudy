# Whitesail Labs market reports

Source-linked market research reports prepared for Fulton Asset Management. The public site's home page (`site/index.html`) is a catalog of the reports below. Each report has an interactive market map, tabs for the market evidence, the analysis for Fulton and an appendix, plus pop-up definitions of technical terms.

| Report | What it covers | Where |
|---|---|---|
| **North American power transformers** | Supply, capacity, lead times, prices, trade and policy, deals, the value chain from electrical steel to data centers, and how Fulton can profit from the build-out. Updated weekly | [`transformer-market/`](transformer-market/) · [dashboard](https://claude.ai/artifact/HPfiJXoEzG2ZwVXuMkAWYb) |
| **Critical utility infrastructure services** | Tests the maintenance-led holding-company thesis across natural gas, power and water: precedent platforms, asset age, demand drivers, fragmentation, TAM and margins, cross-unit synergies and platform candidates | [`infra-services/`](infra-services/) |

## Repository layout

| Path | What it is |
|---|---|
| `reports.json` | The report catalog (title, summary, page and data folders) |
| `tools/build_catalog.py` | Builds the public site: the catalog home page plus one folder per report |
| `tools/build_site.py` | Turns one dashboard page and its datasets into a standalone static page |
| `site/` | The built public site, deployed by `.github/workflows/pages.yml` |
| `shared/brand/` | Whitesail Labs logo |
| `transformer-market/` | Transformer report: market map, weekly reports, deep dive, CSV trackers, dashboard source, runbook |
| `infra-services/` | Utility infrastructure services report: research, dashboard source and datasets |
