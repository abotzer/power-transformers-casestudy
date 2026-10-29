# Weekly Monitoring Runbook

Each weekly run follows this checklist so reports stay comparable from week to week.

## 1. Scope

North American (US, Canada, Mexico) electricity transformers: large and medium power transformers, GSUs, distribution (pole, pad-mount, dry-type), mobile substations, solid-state transformers, and their inputs (GOES, cores, copper, insulation, bushings, test capacity).

## 2. Window

Cover the 7 days ending on the run date. Also pick up anything dated in the previous 7 days that the last run missed, and mark it "late catch".

## 3. Sweep (searches to run each week)

Use web search in "extended" mode for anything time-sensitive. Run the searches in parallel batches.

**Supply and capacity**
- `transformer manufacturing plant announced <month year>` and `transformer factory expansion jobs <month year>`
- Company sweeps: Hitachi Energy, GE Vernova / Prolec GE, Siemens Energy, HD Hyundai Electric, Hyosung HICO, LS Electric, Mitsubishi Electric Power Products, Virginia Transformer, Pennsylvania Transformer / Niagara (Quanta), Delta Star, Howard Industries, ERMCO, Central Moloney, Eaton, Forgent (MGM/VanTran), JST Power Equipment, Giga Energy, Hammond Power Solutions, WEG, Cleveland-Cliffs
- State economic-development press releases (governor offices), which often break plant news first

**Prices and lead times**
- BLS producer price releases (monthly, mid-month): WPU117409, WPU11740999, PCU335311335311
- Wood Mackenzie, NREL/DOE, NIAC, CoBank, NRECA, APPA lead-time and price notes
- Copper (COMEX/LME) and GOES pricing

**Demand**
- EEI and S&P/RRA capex updates; utility earnings in reporting season
- ERCOT STEP / PUCT, PJM RTEP/TEAC, MISO, SPP 765 kV and transmission awards
- Hyperscaler and data-center power-equipment orders (Korean exchange disclosures carry many of these)

**Trade and policy**
- DOE rulemaking under EO 14420/14421 (docket DOE-HQ-2026-1123), the DPA Title III awards from Presidential Determination 2026-10, and DOE distribution-transformer efficiency (EERE-2026-BT-STD-0133)
- Section 232 (metals, derivatives, Annex III changes), Section 301 forced-labor tariffs, Section 122 refund litigation, USMCA annual review
- CBP CSMS notices on HTS 8504

**Deals and capital**
- `transformer acquisition <month year>`, `transformer manufacturer private equity`, `remanufactured transformer acquisition`, `mobile substation acquisition`
- Solid-state transformer funding rounds; IPO and follow-on filings (SEC EDGAR)
- Status checks on pending deals listed in `data/deals.csv` (Status = Signed / Pending)

**Fulton Asset Management**
- `"Fulton Asset Management"`, `"Imperial Group" Chicago acquisition`, `"Ashland Capital Partners" acquisition` (Fulton's usual co-sponsor), and press on the portfolio companies (Metaltec, Mayco, Stainless Foundry, Panther Metalflow, AFCO, Setna iO, Transend, ZYCI)
- Deals and plant news among the targets named in the Fulton plays (value-chain section of the dashboard)

**New entrants**
- Indian, Turkish, Vietnamese and other non-covered-country suppliers entering North America (JVs, distributors, plants)

## 4. Update procedure

1. Add new rows to `data/capacity_expansions.csv`, `data/deals.csv` and `data/indicators.csv`. Change the status or value on existing rows when something moves. Never delete history; add a new dated indicator row instead.
2. Edit `market-map.md` sections 1–9 where facts changed, and update the "Baseline as of" date.
3. Write `weekly/<YYYY-MM-DD>.md` using the template below.
4. Refresh the dashboard at https://claude.ai/artifact/HPfiJXoEzG2ZwVXuMkAWYb:
   - Update the rows in `dashboard/build_data.py`, including `report_window`, `events` (move last week's items to "Last six weeks"), `takeaways` and `watchlist`.
   - Run `python3 -I dashboard/build_data.py <out_dir>`, then `python3 -I dashboard/build_deep.py deep-dive/research/round2_synthesis.json deep-dive/research/round2_research.json <out_dir>`. The second script writes the deep-dive datasets (segments, scorecard, plant status, utility price points, margins, demand in units, monthly PPI) and also `takeaways.json` and `watchlist.json`. To change takeaways or the watchlist in a weekly run, edit `build_deep.py`.
   - Upload each changed JSON file as an asset on that artifact.
   - Update `url`, `name` and `updated` on the matching `datasets/<id>` document.
   - Edit `files/index.html` (source in `dashboard/index.html`) only when the layout itself needs to change.
   - The value-chain graph, the Fulton section and the glossary come from `value-chain/research/workflow_result.json`. After editing that file (a new flow, a changed estimate, a new Fulton deal, a new term), run `python3 -I value-chain/build_value_chain.py value-chain/research/workflow_result.json <out_dir> value-chain`, then upload `value_chain_nodes`, `value_chain_edges`, `fulton_plan`, `fulton_portfolio`, `fulton_plays` and `glossary` the same way. When a new acronym appears in the weekly text, add it to the glossary so the page underlines it.
4c. Rebuild the public site: copy changed dataset JSON into `transformer-market/site-data/`, then run `python3 -I tools/build_catalog.py . site` from the repo root. Pushing `site/` redeploys it through `.github/workflows/pages.yml`.
5. Commit with the message `weekly: transformer market update <YYYY-MM-DD>` and push to the working branch.

## 4b. Deep-dive follow-ups each week

- Re-check the plants in `deep-dive/research/round2_synthesis.json` → `plant_status` that are `at_risk`, `slipped` or `unverified`. Look for groundbreakings, stormwater notices, county minutes and job posts, and update their verdicts.
- Add new utility purchase records (council or board approvals with price and lead time) to the price-points list.
- Track the deep dive's walk-away thresholds: DOE's EO 14421 rules (~Dec 24-27), bid lead times under 20 weeks for 3-phase pad-mounts or under 52 weeks for substation units, gross margins at Forgent and Hammond, and transformer PPI growth under 3% YoY.

## 5. Weekly report template

```
# NA Transformer Market Weekly: <date range>
## TL;DR (3–5 bullets, each with the "so what")
## What changed this week (table: date | event + links | category | significance High/Med/Low)
## What it implies (for someone building or investing in transformer manufacturing)
## What it means for Fulton (portfolio exposure, plays, triggers hit)
## Scorecard (metric | value | change vs last week | 6–12 mo direction)
## Watchlist (dated catalysts)
## Confidence & gaps
```

## 6. Significance rubric

- **High**: changes NA supply by ≥5% in a segment, changes tariff or ban scope, a deal >$500M or one that sets a valuation benchmark, or a lead-time or price series breaking its trend.
- **Medium**: a new plant <$200M, a new entrant, a notable order (≥$100M), input-supply changes.
- **Low**: context, non-NA events, restated news.

## 7. Source hygiene

- Tag each claim [P] primary, [S] secondary or [W] weak.
- Prefer primary sources: company press releases, SEC/SEDAR filings, Federal Register, BLS, governors' offices.
- When sources conflict, show both and say which one you trust more.
- Do not repeat a number without a link.
