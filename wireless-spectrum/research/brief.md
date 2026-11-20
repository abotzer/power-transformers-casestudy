# Wireless spectrum research digest (prepared 2026-11-19)

## demand

Bottom line. Demand for licensed mobile capacity is still growing at double-digit rates. In the US it is slowing, not speeding up, and the 'AI beyond the data center' story does not yet show up in measured traffic. Since 2021 the biggest new user of US licensed capacity has been fixed wireless access (FWA): home broadband sold at a low price per gigabyte. The forecasts that show AI driving a step change are scenario models. They come mostly from equipment vendors (Ericsson, Nokia) and the carrier trade group (CTIA), and all three benefit from a spectrum-scarcity story. Revenue per GB keeps falling about 20% a year. On demand evidence alone, the thesis is plausible for 2030-2035, mainly through uplink, but the data through 2026 does not support it.

1. Growth rate and direction
US: CTIA counted 159.3 trillion MB (159.3 EB) in 2025, up 20%. That follows +38% (2022), +36% (2023) and +32% (2024). It is the slowest year since 2020 (+14%), and the 12-point drop is the sharpest slowdown in the series.

Global: Ericsson puts mobile network traffic at 203 EB/month at end-2025 including FWA (146 EB/month excluding it). Q2 2026 passed 220 EB/month, up 23% y/y, slightly faster than the ~20-21% of 2024-25, led by India and North America. Its June 2026 forecast is 515 EB/month by 2031 (17% CAGR), with yearly growth falling to 14% in 2031. The November 2026 edition is due 30 November.

Ericsson's forecasts have tended to run high:
- In 2017-18 it expected North American smartphones to average 48 GB/month in 2023. Its 2024 edition put 2023 at 26 GB. The current edition shows 21 GB for 2024 and 25 GB for 2025, with a forecast of 52 GB by 2031.
- It cut its Q3 2023 global estimate from over 140 to about 130 EB/month.
- Its 2030 forecast fell from 473 EB/month (Nov 2024 edition) to 430 (Jun 2025 edition).

Comparable mature markets settle near 20%: UK traffic grew 18% in 2025 (Ofcom), and Switzerland slowed from about 100% (2018) to 20-25% (2024).

2. FWA absorbs most new capacity
Per Ericsson, FWA was 28% of global mobile network traffic at end-2025 and rises to about 187 EB/month (about 36%) by 2031. A typical FWA line uses about 500 GB/month, against about 25 GB for a smartphone.

US subscriber bases:
- T-Mobile: 8.45M at end-2025.
- Verizon: about 5.7M at end-2025, and about 6.37M in Q3 2026 per a secondary source.
- AT&T: 2.94M fixed wireless connections in Q3 2026, including business lines.

Our cross-check: about 326M phones (54% of about 603M connections) × 25 GB × 12 months ≈ 98 EB. That leaves about 61 EB, roughly 39% of CTIA's total, for FWA and other devices. This fits about 14M average FWA lines using about 375 GB/month. Separately, analyst Dean Bubley estimated FWA made up about 90% of the 2023 increase.

So much of the US 'mobile data boom' is home broadband running on licensed spectrum. FWA growth is now slowing: Verizon added 159K in Q3 2026 versus 261K a year earlier, and New Street expected 3.6M industry adds in 2026 versus 3.8M in 2025. New Street puts Big 3 headroom at about 32M subscribers. This cuts both ways. It shows licensed spectrum can be sold as a substitute for fiber, but it also shows carriers have spare capacity today and sell it cheaply. That is not a sign of scarcity.

3. Licensed spectrum vs Wi-Fi
Opensignal found 82-89% of US smartphone data went over Wi-Fi in 2024. Many AI devices will also use unlicensed or local spectrum:
- Smart glasses connect through the phone.
- Factory and warehouse robots run on Wi-Fi or private 5G, and robot makers recommend private 5G for industrial sites.
- Counterpoint expects about 50,000 humanoid robot shipments in 2026.

Licensed wide-area spectrum matters mainly for outdoor, moving 'physical AI': robotaxis, delivery robots and drones.

4. Is AI visible in traffic?
Not in volume. Ericsson measured GenAI apps at 0.06% of mobile traffic in April 2025 (21 apps on one operator's network). Uplink was 26% of that traffic, against about 10% for mobile traffic overall. Ericsson says uplink grew faster than downlink at 43 of 55 operators, but Ookla found the uplink share flat or falling since 2023 in more than half of 22 markets.

Physical AI is still small:
- Waymo ran about 4,000 robotaxis in September 2026. At about 20 GB/day per vehicle (AT&T's network CTO), that is about 0.03 EB/yr, or about 0.02% of 2025 US traffic. Even 1M robotaxis would add about 7.3 EB/yr, about 4.6% of the 2025 total.
- Meta sold more than 7M glasses in 2025. IDC sees display-less glasses at 13.6M units in 2026 and 27.3M by 2030, and growth cooled to about 35% in Q2 2026.
- Connected-car cellular traffic grows from 1.8 EB/yr (2023) to 13.5 EB/yr (2029) per Analysys Mason, under 1% of global mobile traffic.
- T-Mobile's Starlink-based T-Satellite service was 0.0002% of T-Mobile's network usage.

The forecasts:
- Ericsson: AI could make 2031 uplink 3x (medium adoption) to 5x (high) the 2025 level. Its Technology Review models US urban uplink share rising from 10% to 14% by 2031.
- Nokia (November 2026): about 3,789 EB/month across all networks by 2035, 44% of it AI-driven. Agentic AI traffic reaches 160x its 2026 level and physical AI 105x, but uplink reaches 24% only in the cells with the most AI use.
- CTIA: about 4x US demand by 2032. That implies about 22% a year, faster than 2025's 20%.

A simple check on scale: uplink is about 10% of traffic, so tripling it adds only about 20% to total volume over six years. The stronger pro-thesis argument is physics, not volume. Handset uplink is power-limited, so uplink-heavy AI uses a disproportionate share of spectrum and favors low- and mid-band coverage.

5. Revenue per GB
Service revenue per GB fell from $412 (2010) to $4.50 (2020) and $1.48 (2025), about -20% a year since 2020. CTIA reports price per MB fell 21% in 2025, and service revenue per connection was $33.14/month versus $49.26 in 2007. Analysys Mason sees North American service revenue roughly flat to 2030. Secondary reports say the wireless CPI rose 5.9% month-on-month in August 2026 after carrier price increases; this is not verified against BLS tables. Verizon trimmed 2026 capex to $16.0-16.5B from $17.0B, and T-Mobile guided about $10B. Neither looks like an operator short of capacity.

What supports the thesis:
- Traffic still compounds at 15-20%.
- Global growth ticked up to 23% in mid-2026.
- AI traffic is uplink-heavy (26-50% uplink against 10%), and uplink is the binding constraint.
- FWA shows licensed spectrum can be sold as broadband.
- Robotaxis need wide-area coverage.

What undercuts it:
- US growth is slowing.
- Measured AI traffic is 0.06%.
- Most device data rides Wi-Fi.
- Vendor forecasts have overshot.
- The main absorber of capacity is cheap FWA.
- Revenue per GB falls about 20% a year while revenue stays flat.
- Carriers are trimming capex.
- Satellite direct-to-phone traffic is negligible so far.

6. Projections (P50, with P10-P90 range)

| Metric | 2028 | 2030 | 2035 |
|---|---|---|---|
| US traffic (EB/yr) | 250 (220-300) | 320 (255-440) | 520 (325-930) |
| Global traffic incl. FWA (EB/month) | 315 (285-360) | 420 (355-525) | 700 (500-1,100) |
| US uplink share | 11% | 12.5% | 15% |
| AI share of mobile traffic (narrow definition) | 1.5% | 4% | 15% |
| US revenue per GB | $0.98 | $0.78 | $0.52 |

CTIA's 4x-by-2032 path (about 640 EB) sits above our 2032 P90 (about 590). The AI-share ranges are very wide. Our judgment: about a 15% chance US growth goes back above 25% in any year from 2027 to 2030, and about a 15% chance AI traffic tops 10% of US mobile traffic by 2030.

Watch: Ericsson's November 2026 report, any new measured AI traffic share, CTIA's 2027 growth rate, uplink share in Ookla and Opensignal data, FWA net adds and throttling, robotaxi fleet counts, and the BLS wireless CPI.

### Key findings
- [S] US mobile data growth slowed to 20% in 2025 from 32% in 2024 and about 36% in 2023.: +20% y/y (2025) vs +32% (2024), ~+36% (2023) (CY2025; Broadband Breakfast (CTIA survey coverage), https://broadbandbreakfast.com/wireless-data-use-up-20-percent-last-year-ctia-finds/)
- [S] Analyst Dean Bubley estimated that about 90% of the added US 'mobile' traffic in 2023 came from fixed wireless access, which CTIA does not report separately.: ~90% of the 2023 increment (~26 trillion MB) (Oct 2024; RCR Wireless Analyst Angle (Dean Bubley), https://www.rcrwireless.com/20241014/5g/us-mobile-data-traffic-stats-need-careful-scrutiny-analyst-angle)
- [S] US industry service revenue divided by traffic fell from $412/GB in 2010 to $4.50/GB in 2020 and $1.48/GB in 2025.: $412 (2010), $4.50 (2020), $1.48 (2025) per GB; ~-20%/yr 2020-25 (CY2025; Light Reading (from CTIA survey data), https://lightreading.com/wireless/inflation-mostly-skipped-the-wireless-bill)
- [P] Global mobile network data traffic including FWA exceeded 220 EB/month in Q2 2026, up 23% y/y, mainly driven by India and North America.: >220 EB/month; +23% y/y; ~+6% q/q (Q2 2026; Ericsson Mobility Report, mobile traffic update, https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/mobile-traffic-update)
- [P] Ericsson forecasts 515 EB/month of global mobile network traffic by end-2031 including FWA (CAGR ~17%), with yearly growth slowing to 14% in 2031; 328 EB/month excluding FWA.: 515 EB/month (2031, incl. FWA); 328 EB/month excl. FWA (Jun 2026 forecast; Ericsson Mobility Report, mobile traffic forecast, https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/mobile-traffic-forecast)
- [S] FWA was 28% of global mobile network data traffic at end-2025 and is forecast to grow more than 3x to about 187 EB/month by end-2031 (~36% of total).: 28% (2025); ~187 EB/month (2031) (Jun 2026; Fierce Network (Ericsson Mobility Report June 2026), https://www.fierce-network.com/broadband/ericsson-predicts-more-fwa-uplink-traffic-network-demand-transforms)
- [P] North American smartphones averaged about 25 GB/month of cellular data at end-2025 (21 GB in 2024), forecast to reach 52 GB by 2031.: 21 GB (2024), 25 GB (2025), 52 GB (2031F); 13% CAGR (Jun 2026 edition; Ericsson Mobility Report key figures, https://www.ericsson.com/en/reports-and-papers/mobility-report/key-figures)
- [P] Ericsson measured GenAI apps at 0.06% of mobile network traffic (21 apps, one operator, April 2025); 26% of that traffic was uplink versus about 10% for mobile traffic overall.: 0.06% of mobile traffic; 26% uplink share (Apr 2025 (published Jun 2025); Ericsson Mobility Report article: GenAI data traffic today, https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/genai-data-traffic-today-june-2025)
- [P] Ericsson scenario modeling suggests additional AI traffic could make 2031 uplink volumes 3x (medium adoption) to 5x (high adoption) the 2025 level, while networks remain downlink-dominated.: 3x (medium) to 5x (high) uplink, 2031 vs 2025 (Jun 2026; Ericsson press release, Mobility Report June 2026, https://www.ericsson.com/en/press-releases/2026/6/ericsson-mobility-report-5g-subscriptions-top-three-billion-as-uplink-gains-momentum)
- [P] Nokia projects total network traffic (all networks) of about 3,789 EB/month by 2035, nearly 4x 2026 levels, with 44% driven by AI.: ~3,789 EB/month (2035); AI 44% (4 Nov 2026; Nokia press release, Global Network Traffic Report, https://www.nokia.com/about-us/news/releases/2026/11/04/nokia-global-network-traffic-report-forecasts-ai-will-drive-nearly-half-of-global-traffic-in-2035/)
- [S] Opensignal found that most US smartphone data travels over Wi-Fi, 82-89% depending on operator, with Xfinity Mobile highest at 89% and T-Mobile users lowest.: 82-89% of smartphone data on Wi-Fi (Oct 2024; Opensignal, https://insights.opensignal.com/2024/10/31/wi-fi-drives-smartphone-data-consumption-in-the-us-but-trends-vary-across-operators)
- [P] T-Mobile ended 2025 with 8.45 million 5G broadband customers after 1.9 million 5G broadband net additions in 2025 (495K in Q4).: 8.45M; +1.9M in 2025 (31 Dec 2025; T-Mobile Q4 2025 earnings release, https://www.t-mobile.com/news/business/t-mobile-q4-2025-earnings)

### Forecast seeds
- How much data will US wireless networks carry per year on the CTIA Annual Survey basis (includes FWA)? [trillion MB per year (= EB/yr)] now 159.3 (2025); history: 1.47 (2012), 9.65 (2015), 37.1 (2019), 53.4 (2021), 73.7 (2022), 100.1 (2023), 132 (2024), 159.3 (2025). Growth +38% (2022), +36% (2023), +32% (2024), +20% (2025).; up: FWA base growing toward 25-30M lines; per-phone use 25 -> 52 GB/month (Ericsson NA forecast); higher-resolution video; uplink-heavy AI (glasses, agents, cameras) if multimodal use scales; robotaxi fleets; new mid-band capacity making FWA cheaper; satellite-terrestrial roaming.; down: FWA net adds already slowing (Verizon 159K in Q3 2026 vs 261K); fiber overbuild by the same carriers; 82-89% of smartphone data on Wi-Fi; phone base saturated; codec efficiency; carriers deprioritizing FWA to protect mobile; CTIA methodology changes.; base rate: Mature markets settle at high-teens to ~20% growth: UK +18% (2025), Switzerland 20-25% (2024); Ericsson global CAGR 17%, slowing to 14% by 2031. US growth fell 12 points in one year. CTIA's own 4x-by-2032 path implies ~22% CAGR.; suggested P10/P50/P90 2028: 220 | 2030: 255 | 2035: 325 / 2028: 250 | 2030: 320 | 2035: 520 / 2028: 300 | 2030: 440 | 2035: 930 (2028 / 2030 / 2035)
- What will global mobile network data traffic including FWA be at year-end (Ericsson basis)? [EB per month] now 203 (end-2025); >220 (Q2 2026); history: ~130 (Q3 2023, revised), 157 (Q3 2024), 203 (Q4 2025), 210 (Q1 2026), >220 (Q2 2026); y/y growth ~20-23%.; up: India and emerging-market smartphone use; FWA connections 185M -> 350M by 2031; AI uplink scenarios (3-5x uplink by 2031); 5G standalone; video.; down: History of downward revisions (2030 forecast cut from 473 to 430 between Nov 2024 and Jun 2025 editions); market maturity; Wi-Fi offload; video compression.; base rate: Ericsson 17% CAGR 2025-2031 (515 EB/month in 2031); ABI 23% CAGR 2025-2030; Nokia 2023 report 22-25% CAGR for end-user traffic on all networks.; suggested P10/P50/P90 2028: 285 | 2030: 355 | 2035: 500 / 2028: 315 | 2030: 420 | 2035: 700 / 2028: 360 | 2030: 525 | 2035: 1,100 (2028 / 2030 / 2035)
- How many US fixed wireless access subscribers will T-Mobile, Verizon and AT&T have combined? [million subscribers] now ~15.6 (end-2025, reported/derived); ~19 (Q3 2026, Whitesail estimate); history: ~4.1 (2022), ~7.9 (2023), ~11.7 (2024), ~15.6 (2025); industry adds ~3.8M in 2025.; up: T-Mobile 15M target by 2030 (ahead of schedule); Verizon 'well beyond' 8-9M by 2028; mmWave 1-Gig FWA; new spectrum; cable price increases; steady AT&T adds.; down: Disconnects rising with the base; same carriers prioritizing fiber; capacity pulled back for mobile/AI if demand rises; satellite broadband competition; network congestion signs (Ookla FWA speeds dipped in 2025).; base rate: New Street: adds 3.8M (2025) -> 3.6M (2026); Big 3 capacity ~32M. Product S-curves typically flatten as 50-70% of capacity is used.; suggested P10/P50/P90 2028: 21 | 2030: 22 | 2035: 18 / 2028: 25 | 2030: 29 | 2035: 32 / 2028: 29 | 2030: 36 | 2035: 45 (2028 / 2030 / 2035)
- What share of global mobile network data traffic will FWA account for? [% of total mobile network traffic] now 28% (end-2025); history: Ericsson: 28% at end-2025; forecast ~187 of 515 EB/month (~36%) in 2031. Nokia: FWA >1/3 of consumer cellular traffic by 2035.; up: FWA lines use ~20x a smartphone (500 vs 25 GB/month); emerging-market FWA growth (Asia-Pacific 50% of connections by 2031); new mid-band spectrum.; down: Fiber build-outs; operators prioritizing mobile when AI uplink demand rises; FWA net adds slowing in the US.; base rate: Ericsson and Nokia both project a mid-30s percent share by 2031-2035.; suggested P10/P50/P90 2028: 29% | 2030: 30% | 2035: 28% / 2028: 32% | 2030: 35% | 2035: 37% / 2028: 34% | 2030: 39% | 2035: 45% (2028 / 2030 / 2035)
- What share of US mobile network traffic will be uplink? [% of total mobile traffic (volume)] now ~10% (Ericsson baseline); history: Roughly 90:10 downlink:uplink for years. GenAI app traffic was 26% uplink (2025). Ookla: uplink share flat or declining since 2023 in more than half of 22 markets.; up: Multimodal AI assistants; smart glasses (~8 bytes up per byte down); robotaxi and camera uploads; agentic AI near 50/50; creator video.; down: Downlink video growth; FWA (downlink-heavy, ~20% of US urban traffic); on-device inference reducing uploads; uploads moved onto Wi-Fi.; base rate: Ericsson ETR medium GenAI: 10% -> 14% (US urban, 2031); Nokia: 24% only in highest-AI cells by 2035; Ericsson: tripling uplink by 2031 in medium scenario.; suggested P10/P50/P90 2028: 10% | 2030: 10% | 2035: 11% / 2028: 11% | 2030: 12.5% | 2035: 15% / 2028: 13% | 2030: 16% | 2035: 22% (2028 / 2030 / 2035)
- What share of mobile network traffic will be directly attributable to AI apps, agents and AI devices (narrow definition, not AI-recommended video)? [% of mobile network traffic] now 0.06% (Apr 2025, Ericsson, 21 GenAI apps); history: No newer operator measurement found; Counterpoint (Jun 2026) still cites 0.06%.; up: Voice/vision assistants on phones; AI glasses (7M+ sold in 2025, IDC 27M display-less by 2030); robotaxis; agentic AI (Nokia 160x by 2035); physical AI (Nokia 105x).; down: Text-based AI is light; on-device models; AI features absorbed into existing apps and not counted separately; Wi-Fi offload; robots indoors on Wi-Fi/private 5G.; base rate: Broad-definition forecasts: Nokia 44% of all network traffic by 2035; CTIA ~1/3 of broadband by 2034. Historical analog: video took over a decade to reach ~75% of mobile traffic (end-2025).; suggested P10/P50/P90 2028: 0.3% | 2030: 0.8% | 2035: 4% / 2028: 1.5% | 2030: 4% | 2035: 15% / 2028: 5% | 2030: 12% | 2035: 35% (2028 / 2030 / 2035)
- What will US wireless service revenue per GB of traffic be (CTIA service revenue / CTIA traffic)? [US$ per GB (nominal)] now $1.48 (2025); history: $412 (2010), $4.50 (2020), $1.48 (2025): about -20% per year 2020-2025. Price per MB -21% in 2025; revenue per connection $33.14/month.; up: Carrier price increases (Aug 2026 CPI +5.9% m/m, unverified); slower traffic growth; premium tiers for AI/slicing/satellite; less competition.; down: Continued traffic growth; low-price FWA gigabytes; cable MVNO competition; satellite texting/data bundled free; flat service revenue (Analysys Mason ~+0.6% 2024-2030).; base rate: -20%/yr (2020-2025). Our P50 assumes revenue +1.5%/yr and the P50 traffic path.; suggested P10/P50/P90 2028: $0.78 | 2030: $0.53 | 2035: $0.25 / 2028: $0.98 | 2030: $0.78 | 2035: $0.52 / 2028: $1.17 | 2030: $1.07 | 2035: $0.97 (2028 / 2030 / 2035)
- What share of US licensed mobile traffic will come from robotaxis/autonomous vehicles? [% of US mobile traffic] now ~0.02% (Waymo ~4,000 vehicles x ~20 GB/day vs 159.3 EB in 2025); history: Waymo fleet ~3,000 (Mar 2026) -> ~4,000 (Sep 2026); ~500K paid rides/week; target 1M weekly rides by end-2026.; up: Fleet scaling (Waymo, Tesla, Zoox); more cameras and remote-assist video uplink; real-time map updates; regulation requiring telemetry.; down: Bulk data offloaded at depots over Wi-Fi/fiber; on-vehicle compression; slower city approvals; safety incidents.; base rate: Even 1M robotaxis at 20 GB/day = ~7.3 EB/yr, ~4.6% of 2025 traffic. Our P50 assumes ~25K vehicles (2028), ~60K (2030), ~400K (2035).; suggested P10/P50/P90 2028: 0.02% | 2030: 0.04% | 2035: 0.1% / 2028: 0.06% | 2030: 0.15% | 2035: 0.6% / 2028: 0.2% | 2030: 0.6% | 2035: 3% (2028 / 2030 / 2035)

### Gaps
Method limits: WebFetch could not reach primary pages. lightreading.com and telecoms.com failed to resolve, which happens when a host is outside this session's allowed network domains. Per instructions I stopped trying further hosts, so every figure comes from search-result extracts of primary and secondary pages, not full documents. Allowing those hosts in the session's network settings would let them be read directly. I did not open the CTIA survey PDF, Ericsson report PDFs, the Nokia 2026 report, the Ookla report or carrier 8-Ks.

Not yet published: Ericsson's November 2026 Mobility Report (due 30 Nov 2026, adds a 2032 horizon).

Unconfirmed or conflicting:
- T-Mobile stopped disclosing FWA counts in 2026, so no Q3 2026 base exists.
- Verizon's Q3 2026 FWA base (6.37M) comes from one secondary source.
- AT&T's consumer Internet Air base is unclear (2.94M all fixed wireless incl. business vs a 2.23M figure from one outlet).
- AT&T's end-2025 base is derived, not reported.
- BLS August 2026 wireless CPI (+5.9% m/m) was not checked against BLS tables.
- Opensignal Wi-Fi share data for 2025-26 not found; latest is Oct 2024.
- Waymo does not disclose per-vehicle cellular usage; the 20 GB/day figure is an AT&T executive's estimate.
- No operator-measured AI traffic share newer than April 2025 found.
- Nokia 2026 mobile-specific CAGR not found.
- Cisco VNI has been discontinued and was not used.
- GSMA licensed cellular IoT 2030 figure only from an older edition.
- Ericsson North America GB/smartphone history was restated between editions (26 GB for 2023 in the 2024 edition vs 21 GB for 2024 in the 2026 edition).
- Earlier Ericsson forecast vintages (466/473/430 EB) come from press coverage.
- CTIA's series mixes survey editions (2015 and 2017 anomalies) and does not separate FWA.
- The FWA share of US traffic (~35-45%) and the Q3 2026 Big 3 FWA total (~19M) are Whitesail estimates from reported inputs, not published figures.
- US wireless service revenue is $235B per Light Reading/CTIA, but other trackers range $255-326B.
- The Ookla 'uplink share flat or declining' finding comes via secondary coverage.

## capacity

Short answer: spectrum is the cheapest way to add capacity at cell sites carriers already own, and in the 5G era it did more of the work than the long-run history suggests. But the 2025-2026 evidence does not show a binding US capacity shortage, and new mid-band supply is about to rise by statute. For licensed spectrum to become significantly more valuable per MHz-pop, US traffic growth would have to re-accelerate well above the 13-20% range it has settled into. That is not my base case.

**How capacity has been added**
The usual reading of Cooper's law splits a roughly million-fold gain since the late 1950s into three parts (arXiv 1908.06035; the factors are approximate):
- cell densification, about 1,600x;
- more spectrum, about 30x;
- better modulation and coding, 10x or less.

The 5G era looks different. From 2018 to 2025 US mobile traffic rose about 5.6x, from roughly 28.6 to 159.3 trillion MB (CTIA). Over the same period:
- Licensed sub-6 GHz spectrum in use rose about 1.6x by my estimate: C-band, 3.45 GHz, CBRS licensed blocks (PALs), 600 MHz and T-Mobile's 2.5 GHz.
- Outdoor site counts rose about 1.3x: 349,344 in CTIA's 2018 count against about 453,000 macro sites plus outdoor small cells in WIA's end-2025 count. The two counts define sites differently.
- The remaining ~2.7x came from efficiency and from running networks more heavily loaded.

A measurement study of the three US carriers found that mid-band 5G (NR) was only marginally more efficient than LTE per stream: 1.9-2.3 bit/s/Hz/stream, with T-Mobile's n41 at 3.14 because of its denser grid. The study attributed most throughput gains to wider channels. This is the strongest technical point for the thesis: in practice, wide contiguous mid-band blocks did most of the capacity work in 5G.

**Efficiency and 6G**
Within existing spectrum, 5G-Advanced adds incremental gains:
- Nokia cites 20-40% higher spectral efficiency from more antenna ports.
- Nokia also cites up to 40% more uplink capacity from eight-stream uplink.
- A T-Mobile trial of an improved multi-user MIMO method (zero-forcing) reported +60% over the legacy version.

On timing, 3GPP approved the Release 21 timeline in June 2026, with the final specification freeze (ASN.1) in March 2029. Ericsson expects the first commercial 6G systems in 2030.

6G's capacity case rests mostly on new spectrum rather than better bits per Hz:
- Ericsson's simulation says 200 MHz at 7 GHz on an existing macro grid roughly triples downlink capacity.
- Nokia's coverage modelling and a 2026 study using live-network data are less favourable: they point to denser grids and higher energy use.
- Nokia's target of 50 bps/Hz average, against about 10 for 5G, assumes extreme MIMO and 400 MHz channels. It is an ambition, not a measurement.

The candidate bands under WRC-27 agenda item 1.7 are 4.4-4.8, 7.125-8.4 and 14.8-15.35 GHz. NTIA's study of 7.125-7.4 GHz is due December 10, 2026. The 2025 budget law (OBBBA) bars auctions of 7.4-8.4 GHz and 3.1-3.45 GHz. So the 2030-2035 capacity path depends heavily on whether about 275 MHz or more at 7 GHz is cleared. That would be a supply event: it adds to the stock of licensed spectrum rather than making existing holdings scarcer.

**How credible are the shortfall claims?**
The industry studies:
- Brattle, commissioned by CTIA, projects a deficit of about 400 MHz by 2027 and about 1,400 MHz by 2032.
- GSMA says dense urban areas need 2-3 GHz of mid-band by 2035-2040.
- CTIA and Accenture (2026) say up to a third of AI traffic demand in dense areas could go unmet.

These forecasts have a poor record. The FCC's 2010 staff paper projected a deficit of about 275-300 MHz by 2014. Carriers absorbed the growth with LTE, cell splitting, Wi-Fi and later auctions, with no visible failure.

Current market data point to headroom rather than scarcity:
- US traffic growth slowed from 35% in 2023 to 32% in 2024 and 20% in 2025.
- Real prices for unlimited plans fell more than 10% in 2025, and the price per MB fell 21%.
- The combined median download speed of AT&T, Verizon and T-Mobile reached 334 Mbps in H1 2026, up 74% in two years (RootMetrics).
- Industry capex has been flat at about $29-30B for 2023-2025, down from $39B in 2022.
- Verizon's C-band build is about 90% complete, and its fixed-wireless (FWA) targets assume no extra capital.
- T-Mobile guides capex of about $10B, roughly 13% of service revenue. AT&T lowered its long-term capital outlook.
- Verizon's 1,741 MHz of mmWave carries little traffic: OpenSignal found capable phones on it about 0.5% of the time.

A truly scarce input does not usually see the unit price of its output fall while its buyers cut capex. Carriers do not disclose utilization; the last chart Verizon published (around 2020) said it had more unused capacity than five years earlier.

The evidence on the other side is what carriers pay:
- AT&T agreed to pay about $23B for EchoStar spectrum.
- Verizon spent $4.38B on licenses in the first nine months of 2026.
- The AWS-3 re-auction raised $3.57B, slightly above Dish's original price, with SpaceX among the winners.
- Analysts put the April 2027 upper C-band auction at $30-75B.
- The 2021 lower C-band auction raised about $81B against forecasts of $40-52B.

Prices per unit are not clearly rising, though. $30-75B for 160 MHz works out to about $0.56-1.40 per MHz-pop, against roughly $0.9 for lower C-band.

**Wi-Fi and fixed wireless**
Wi-Fi carried 82-89% of US smartphone data in 2024 (Opensignal). The US kept all 1,200 MHz at 6 GHz for unlicensed use and widened outdoor use with geofenced variable-power rules, effective April 27, 2026. The UK, by contrast, is splitting upper 6 GHz between Wi-Fi and mobile. Wi-Fi is the largest capacity lever by volume, and consumers and cable operators pay for it. Unlimited plans cut the share of time on Wi-Fi in 2017-18, and faster 5G may erode it further, but most phone use happens at home.

The counterweight is fixed wireless (FWA). It has accounted for virtually all US home broadband growth for four years and now has more than 17M connections. FWA is the main new load on licensed mid-band, but carriers choose how much of it to sell. Today's FWA sales signal spare capacity, and the ability to stop selling gives carriers a pressure valve later.

**What spectrum is worth**
The economic value of spectrum is capped by the cost of the next-cheapest capacity. The FCC's 2010 paper estimated a build using only new cell sites at $174B, against $54B with 275 MHz of new spectrum: about $120B of avoided cost. Through 2035 three forces hold down that avoided cost:
- efficiency gains that arrive with normal equipment refresh (20-40%);
- slower demand: Ericsson projects data per smartphone in North America growing 13% a year to 2031;
- rising supply: the 800 MHz statutory pipeline, 160 MHz of upper C-band, and possibly 7 GHz.

The cap is highest in dense urban cores. Traffic density there is about nine times other urban areas (GSMA), and adding sites is hardest. Spectrum and towers are complements (Peha), so a MHz is worth most to whoever owns the site grid. That points to a narrow pool of buyers, which matches the Goldman banker's view.

**Satellites and AI**
Estimates of Starlink's capacity run from 4 to 55 Mbps per km². By my estimate, a 100 MHz terrestrial mid-band layer on an urban macro grid delivers roughly 5-7 Gbps per km² (500 m site spacing, three sectors, about 5 bps/Hz). Satellites therefore cannot relieve capacity in dense areas. Satellite spectrum is valuable for coverage, and a SpaceX terrestrial play would need its own site grid.

On AI:
- Generative AI is under 1% of traffic today.
- GSMA Intelligence projects direct AI traffic at 5-20% of mobile traffic by 2030.
- Ericsson models AI tripling uplink traffic by 2031, on networks built for roughly 10:1 download-to-upload.
- Critics note that most AI agent traffic runs server-to-server, not over the radio.
- On-device inference cuts round trips, but camera and video capture add uplink.

Uplink is limited by phone transmit power as much as by MHz. Part of the fix is therefore 5G-Advanced uplink improvements and denser grids, not just more spectrum.

**Probabilities (my estimates)**
- US traffic grows faster than 20% a year over 2025-2030: about 15%.
- A visible capacity crunch by 2030, meaning per-GB price increases or capex intensity back above the 2022 peak: about 20%.
- First US commercial 6G by end-2030: about 60%.
- Upper C-band gross proceeds above $50B: about 35%.
- Licensed 7 GHz mobile service live in the US by 2032: about 40%.

**Net assessment**
Supporting the thesis:
- Mid-band spectrum is the cheapest capacity at existing sites.
- 6G capacity depends on new spectrum.
- Demand concentrates where satellites cannot help.
- Carriers and SpaceX keep buying.

Undercutting it:
- Demand growth is slowing.
- Price per MB is falling and capex is flat.
- Wi-Fi carries most smartphone data.
- Supply is rising by statute, and efficiency keeps compounding.
- Past shortage forecasts failed.

My central case for 2030 is flat to modestly higher prices per MHz-pop for contiguous mid-band TDD blocks next to the incumbents' existing holdings. I do not expect a broad re-rating of spectrum as an asset class.

### Key findings
- [S] US wireless networks carried 159.3 trillion MB in 2025, up 20% year on year, down from 32% growth in 2024 and 35% in 2023.: 159.3 trillion MB; +20% YoY (vs +32% 2024, +35% 2023) (2025 (CTIA survey released 2026-09-09); IEEE ComSoc Techblog summarizing CTIA 2026 Annual Survey, https://techblog.comsoc.org/2026/09/10/ctia-americans-used-more-wireless-data-in-2025-than-in-the-entire-4g-decade-but-growth-slowed-from-2023-2024/)
- [S] Real prices for typical US unlimited plans fell more than 10% in 2025 and the price per megabyte fell 21%, which is hard to square with binding capacity scarcity.: >10% real price decline; -21% price per MB (2025; IEEE ComSoc Techblog summarizing CTIA 2026 Annual Survey, https://techblog.comsoc.org/2026/09/10/ctia-americans-used-more-wireless-data-in-2025-than-in-the-entire-4g-decade-but-growth-slowed-from-2023-2024/)
- [P] Ericsson projects North American data use per active smartphone rising from 25 GB per month in 2025 to 52 GB in 2031, a 13% CAGR.: 25 -> 52 GB/month; 13% CAGR (2026-06 forecast; Ericsson Mobility Report June 2026, https://www.ericsson.com/49ce36/assets/local/reports-papers/mobility-report/documents/2026/ericsson-mobility-report-june-2026.pdf)
- [S] A common reading of Cooper's law attributes the roughly million-fold wireless capacity gain over about 60 years to densification (~1,600x), more spectrum (~30x) and communication theory (no more than ~10x).: 1,600x / 30x / <=10x (2019 paper; arXiv 1908.06035, PHY Research Is Sick but Curable, https://arxiv.org/pdf/1908.06035)
- [P] The FCC's 2010 staff paper projected a spectrum deficit of about 275 MHz (roughly 300 MHz in FCC framing) by 2014 and estimated that meeting demand with cell sites alone would cost $174B versus $54B with additional spectrum.: 275 MHz deficit by 2014; $174B vs $54B (2010-10; FCC staff technical paper (archived) / Computerworld, https://www.computerworld.com/article/1540380/fcc-projects-275mhz-spectrum-deficit-by-2014.html)
- [S] A Brattle Group study for CTIA projects a US licensed spectrum deficit of nearly 400 MHz by 2027 and about 1,400 MHz by 2032, normalized to full-power licensed spectrum with 1-2 GHz propagation.: ~400 MHz (2027); ~1,400 MHz (2032) (2023-04; Brattle Group, https://www.brattle.com/insights-events/publications/current-spectrum-allocation-is-not-sufficient-for-meeting-the-future-demand-for-wireless-broadband-in-the-us-according-to-a-new-brattle-report)
- [S] The 2025 budget law restored FCC auction authority through September 30, 2034, set an 800 MHz spectrum pipeline, required at least 100 MHz of upper C-band auctioned by July 2027, and excluded 3.1-3.45 GHz and 7.4-8.4 GHz from auction.: 800 MHz pipeline; >=300 MHz auctioned by 2034 (2025-07; Wiley Rein client alert, https://www.wiley.law/alert-One-Big-Beautiful-Bill-Act-Passes-Restoring-FCC-Auction-Authority-and-Establishing-Spectrum-Pipeline)
- [P] The FCC adopted rules on July 22, 2026 to auction 160 MHz of upper C-band (3.98-4.14 GHz) as Auction 115, with bidding set to start April 27, 2027, creating a 440 MHz contiguous C-band range (3.70-4.14 GHz).: 160 MHz; bidding 2027-04-27 (2026-07-22; FCC (DOC-423286A1) / Fierce Network, https://www.fierce-network.com/wireless/upper-c-band-auction-gets-april-27-start-date)
- [P] 3GPP approved the Release 21 (first 6G specifications) timeline in June 2026 with stage 3 freeze in December 2028 and ASN.1 freeze in March 2029; Ericsson expects first commercial 6G systems in 2030.: Spec freeze 2029-03; commercial ~2030 (2026-06; Ericsson blog, 6G standardization key milestones, https://www.ericsson.com/en/blog/2026/6/6g-standardization-key-milestones-and-ran-decisions)
- [S] A real-world measurement study of AT&T, T-Mobile and Verizon found 5G NR mid-band per-stream spectral efficiency only marginally above LTE (1.9-2.3 bit/s/Hz/stream; T-Mobile n41 3.14 due to denser deployment), with throughput gains coming mainly from wider channels.: 1.9-2.3 bit/s/Hz/stream; n41 3.14 (2023-12 paper; arXiv 2312.00957, https://arxiv.org/pdf/2312.00957)
- [S] Opensignal found 82-89% of US smartphone data traffic was carried over Wi-Fi across carriers, highest for Xfinity Mobile at 89% and 86% for AT&T users.: 82-89% of smartphone data (2024-10; Opensignal, https://insights.opensignal.com/2024/10/31/wi-fi-drives-smartphone-data-consumption-in-the-us-but-trends-vary-across-operators)
- [S] US wireless capex per CTIA was $27.4B in 2018, peaked at $39B in 2022, fell to $30B in 2023 and $29B in 2024, and was nearly $30B in 2025, while traffic kept growing.: $27.4B (2018) -> $39B (2022) -> ~$30B (2025) (2018-2025; CTIA Annual Surveys (via PR Newswire, Benton), https://www.benton.org/headlines/ctia-2026-annual-survey-highlights)

### Forecast seeds
- US annual wireless data traffic (CTIA basis) [trillion MB per year] now 159.3 (2025); history: 2018 ~28.6 (recalled); 2022 73.7; 2023 100.1 (+36%); 2024 ~132 (+32%); 2025 159.3 (+20%); up: FWA growth, multimodal AI and uplink video, higher video quality, connected robots/vehicles/wearables on cellular, 5G standalone services; down: Smartphone usage saturation, better video codecs, Wi-Fi offload, on-device AI, FWA saturation; base rate: Ericsson NA per-smartphone 13% CAGR 2025-31; global growth fell from >80% to ~20% over seven years; CTIA claims 4x by 2032 (~22% CAGR); suggested P10/P50/P90 2028: 215 / 2030: 255 / 2035: 350 / 2028: 240 / 2030: 300 / 2035: 480 / 2028: 280 / 2030: 380 / 2035: 750 (2030 (2028 and 2035 shown))
- US wireless network capex (CTIA basis, nominal) [$B per year] now ~30 (2025); history: 2018 27.4; 2019 29.1; 2020 30; 2021 35; 2022 39 (peak); 2023 30; 2024 29; 2025 ~30; up: Upper C-band build 2028-30, 6G 7 GHz overlays from ~2030, uplink densification, inflation; down: Capital-light strategies, AT&T lowered long-term capex, fiber priority, RAN price competition, slowing traffic; base rate: 5G cycle: +42% from 2018 to 2022 peak then -25% by 2024; suggested P10/P50/P90 2028: 25 / 2030: 26 / 2035: 27 / 2028: 29 / 2030: 32 / 2035: 34 / 2028: 34 / 2030: 40 / 2035: 45 (2030)
- Global wireless capital intensity (Dell'Oro basis) [% of wireless revenue] now Not confirmed; implied ~13-15% in 2026; history: 5G peak ~18% (2020-22); Sept 2025 forecast 12-13% by 2029; April 2026 forecast ~11% by 2029; up: 6G cycle start 2030-31, AI-RAN and uplink investment; down: Revenue growth from FWA and pricing, vendor price pressure, slower traffic; base rate: Capex intensity has fallen after each generation peak; suggested P10/P50/P90 2030: 9.0 / 2035: 9.0 / 2030: 11.5 / 2035: 12.0 / 2030: 14.0 / 2035: 16.0 (2030)
- Share of US smartphone data carried over Wi-Fi [% of smartphone data] now 82-89 (2024); history: Time on Wi-Fi 43-54% by carrier in Q1 2017, falling into 2018 with unlimited plans; data share 82-89% in 2024; up: Wi-Fi 7 and full 1,200 MHz at 6 GHz, outdoor GVP devices, cable MVNO growth with Wi-Fi-first designs; down: 5G medians above 300 Mbps, unlimited plans, satellite D2D, carrier pricing that favors cellular; base rate: Unlimited-plan wave cut Wi-Fi time share by ~2-6 points in a year; suggested P10/P50/P90 2030: 72 / 2035: 68 / 2030: 81 / 2035: 78 / 2030: 88 / 2035: 88 (2030)
- Additional licensed mid-band spectrum in US commercial service versus 2025 [MHz (cumulative)] now 0 (baseline ~1,150 MHz licensed sub-6 GHz, Whitesail est.); history: 2018-2025 added C-band 280, 3.45 GHz 100, CBRS PAL 70, 600 MHz 70 into service; up: 800 MHz statutory pipeline; upper C-band 160 MHz auction April 2027; NTIA 7.125-7.4 GHz; possible 4.4-4.8 GHz; down: DoD resistance, FAA altimeter constraints, satellite incumbents, Wi-Fi lobby, presidential withdrawal power; base rate: Lower C-band took ~4-5 years from 2018 rulemaking to large-scale service; suggested P10/P50/P90 2028: 0 / 2030: 160 / 2035: 300 / 2028: 80 / 2030: 200 / 2035: 600 / 2028: 160 / 2030: 400 / 2035: 900 (2035)
- Year of first commercial standards-based 6G service in the US [calendar year] now Not launched; Release 21 ASN.1 freeze March 2029; history: LTE: spec 2008 to US launch Dec 2010; 5G NR: spec 2018 to US launch April 2019; up: US policy push for 6G leadership, 7 GHz identification, competitive pressure; down: Lack of new spectrum, weak carrier ROI, flat capex; base rate: 0.5-2 years from spec freeze to first commercial launch; suggested P10/P50/P90 2029 / 2030 / 2032 (2032)
- Upper C-band (Auction 115) gross proceeds [$B] now Analyst range $30-75B (TD Cowen); Carr $30-60B; history: Lower C-band 2021 ~$81B for 280 MHz (~$0.9/MHz-pop) vs forecasts $40-52B; AWS-3 re-auction 2026 $3.57B; up: Contiguous 440 MHz super-band, SpaceX or other new bidders, AT&T and Verizon mid-band needs; down: Altimeter constraints, carrier leverage (Verizon net debt $123.7B), recent EchoStar purchases, slowing traffic, more pipeline supply; base rate: Lower C-band beat consensus by ~55-100%; suggested P10/P50/P90 22 / 40 / 65 (2027)
- Direct AI-related share of global mobile data traffic [% of mobile data traffic] now <1% (GenAI); history: Negligible before 2024; up: Multimodal assistants, camera-based agents, AR glasses, robotics telemetry; down: On-device inference, server-to-server agent traffic not on radio, compression; base rate: GSMA Intelligence 5-20% by 2030; suggested P10/P50/P90 2030: 2 / 2035: 4 / 2030: 6 / 2035: 12 / 2030: 15 / 2035: 25 (2030)

### Gaps
1) WebFetch was blocked for nearly all hosts in this session (ericsson.com, lightreading.com, telecoms.com, techblog.comsoc.org and others failed to resolve). Every figure here therefore comes from search-result excerpts, not from reading the primary documents (Ericsson PDFs, FCC orders, CTIA PDFs, the Brattle report). Those hosts need to be allowed to check page-level details.
2) The 2018 US traffic figure (~28.6 trillion MB) is from memory, not re-checked. The licensed sub-6 GHz spectrum totals (~716 MHz in 2018, ~1,150 MHz in 2025) are my own estimates. The 2018-2025 lever breakdown depends on both.
3) No current carrier disclosures of network utilization or capacity headroom were found. The latest is Verizon's chart from around 2020. The mmWave usage figure (0.5%) is about 2021-22.
4) No sourced spectral-efficiency figure for 3G (HSPA), so 3G is left out of that chart. ITU IMT-Advanced, IMT-2020 and IMT-2030 numeric targets were not confirmed. The 6G figures are vendor targets.
5) No Wi-Fi offload share for 2025 or 2026. The 2017-18 figures measure time on Wi-Fi; the 2024 figures measure share of data. They are not comparable.
6) CTIA's 2025 total cell-site count was not found. The WIA and CTIA site definitions differ.
7) No current US wireless-only capex-as-%-of-revenue series was found; carrier capex guidance includes fiber. Dell'Oro's 5G-peak figure (~18%) is inferred from its forecast wording.
8) Paywalled analysis was not accessible: New Street, MoffettNathanson, TD Cowen and Tim Farrar notes on spectrum value versus the cost of densification. Minimum opening bids for upper C-band were also not found.
9) Ericsson's November 2026 Mobility Report launches November 30, 2026; I used the June 2026 edition.
10) No source quantifies the bandwidth saved by on-device AI. Mobile Experts' uplink-overload claim and the full conclusion of the RCR uplink critique were not reviewed.
11) The Reuters 2026-10-08 story could not be opened. Search results point to SpaceX buying Grain Management's nationwide 800 MHz holdings (up to 14 MHz paired, price not disclosed), but this is unconfirmed.
12) The 3.45 GHz auction proceeds (~$22.5B) and the lower C-band $/MHz-pop figure are my recall or calculation, not re-verified this session.

## satellite

Summary. In November 2026, satellite direct-to-device (D2D) has a large user base but little revenue. It has already changed the US spectrum market in one specific way. SpaceX was valued at about $1.77T at its June 2026 IPO, and it is now the most aggressive buyer of terrestrial-capable spectrum in the country. That supports one part of the thesis: convergence brings new bidders with deep pockets. Two things undercut the other part. The physics says D2D cannot carry dense urban traffic. And the market reacted to each SpaceX spectrum step by selling carrier stocks. Convergence is adding a competitor and a coverage layer. It does not ease scarcity where the incumbents earn their money.

Where D2D stands. SpaceX's first-generation Direct to Cell fleet has about 650 satellites. It runs on about 5 MHz of partner spectrum (in the US, T-Mobile's PCS G block) and carries texts, some app data and limited voice. SpaceX reported about 7.4M monthly unique devices in about 30 countries at March 31, 2026. Management cited about 22M Starlink Mobile monthly users in Q3 2026, up 37% on Q2, but that metric is defined differently from the March figure. D2D revenue is not disclosed. In Q3 2026 connectivity revenue was $5.25B out of $14.6B total, so D2D is a small, unreported slice of a company whose value comes from broadband, launch and AI.

SpaceX's spectrum build:
- **EchoStar bands.** On May 12, 2026 the FCC approved the transfer of EchoStar's AWS-4 (about 40 MHz), H-block (10 MHz) and unpaired AWS-3 (15 MHz). Waivers allow terrestrial, satellite or hybrid use, and the order adds performance obligations.
- **EchoStar price and closing.** The AWS-4/H-block price is $17B: up to $8.5B in cash and $8.5B in SpaceX stock. EchoStar expects closing around November 30, 2027.
- **Grain 800 MHz.** On October 8, 2026 SpaceX agreed to buy Grain Management's nationwide 800 MHz portfolio (546 licences, up to 14 MHz). The FCC has only accepted the filing. The reported ~$8B price (WSJ) is unconfirmed. Grain bought the same licences from T-Mobile in August 2026 for $2.9B cash plus 600 MHz spectrum.
- **Why 800 MHz.** SpaceX says it needs the band because its 2 GHz holdings do not reach indoors.

SpaceX's next-generation plans:
- **Constellation.** The FCC authorized up to 15,000 next-generation D2D satellites in October 2026. Launches start in 2027, and expanded service is targeted for the end of 2027.
- **Capacity claims.** About 20x per-satellite throughput, more than 100x system capacity, and about 150 Mbps per user. These are company targets.
- **Strategy.** SpaceX partners with carriers abroad but is confrontational in the US. Shotwell said SpaceX wants to be a full mobile telco. T-Mobile said on its Q3 call it does not want to lease capacity to SpaceX. Bloomberg reported SpaceX is seeking access to at least 80,000 US cell sites; TD Cowen puts a terrestrial build above $80B.

AST SpaceMobile:
- **Fleet.** 12 BlueBirds are operating. The target of about 45 has slipped to mid-2027, and launch contracts cover more than 100 satellites over 2027-2028.
- **Financials.** Q3 2026 revenue was $42.3M, mostly gateways and government work. FY2026 guidance is $150-200M, and cash is $3.2B.
- **Service.** Intermittent nationwide US service is targeted before year-end 2026.
- **Spectrum.** Up to 45 MHz of Ligado L-band in North America (about $550M plus at least $80M a year); Inmarsat disputes these rights outside North America. Also 60 MHz of S-band priority rights bought for $64.5M.
- **Valuation.** Market cap was $24.6-37.9B in June-July 2026, against revenue guidance under $200M. Investors are paying for the option on execution.

Consolidation:
- **Amazon and Globalstar.** Amazon is buying Globalstar (about $11-11.5B; FCC approval October 27, 2026; closing in 2027). That brings about 25 MHz of MSS spectrum and the Apple relationship: Apple holds 20%, and 85% of capacity is committed to Apple.
- **Amazon Leo.** Amazon has applied for up to 5,105 D2D satellites for service around 2028.
- **Rocket Lab and Iridium.** Rocket Lab is buying Iridium at $54 a share (enterprise value about $8.0B; closing mid-2027). Iridium's NTN Direct goes commercial in Q4 2026 with Deutsche Telekom IoT.

Within about 18 months, nearly every Western satellite-spectrum asset with D2D potential has been bought or tied up by a large, vertically integrated space company.

Physics. These are Whitesail order-of-magnitude estimates, not published measurements:
- **Gen-1 D2D:** about 5-10 Mbps per beam over several hundred km2, or roughly 0.01-0.03 Mbps/km2.
- **Next-gen targets:** perhaps 1-6 Mbps/km2.
- **Terrestrial:** dense urban macro is about 1,500-9,000 Mbps/km2, small-cell layers 10,000+, and rural macro about 5-30.

A single next-gen satellite may carry hundreds of Gbps, but that is spread over a field of view of hundreds of thousands of km2. It cannot reuse spectrum as tightly as towers 0.5-2 km apart. So satellites can come within about one order of magnitude of rural terrestrial capacity, but stay about three orders below urban. That is why SpaceX itself is buying 800 MHz and looking for towers. Demand from AI devices concentrates where people and vehicles are, and that demand will be met on the ground, mostly by existing licence holders.

Regulation:
- **Repurposing satellite spectrum.** The FCC is willing to repurpose satellite spectrum for flexible terrestrial or hybrid use (the EchoStar waivers). That adds usable supply.
- **SCS framework.** It lets satellites reuse carriers' terrestrial spectrum under emission limits. Existing licences do double duty, which is the opposite of new scarcity.
- **Not checked this session:** 2026 decisions on emission limits and EPFD (satellite power limits); the EU 2 GHz MSS licence renewal (licences expire 2027); WRC-27 agenda item 1.13 on D2D in mobile bands.
- **Concentration rules.** The Goldman point holds. The buyer pool is small (SpaceX, Amazon, AT&T, Verizon, T-Mobile, a few intermediaries such as Grain, and AST), and the FCC spectrum screen limits concentration.

Supports the thesis:
- **Prices are rising.** SpaceX paid about $1.00/MHz-pop for AWS-4/H-block, a band EchoStar could not use for over a decade. If the $8B is right, it paid about $1.68/MHz-pop for 800 MHz that changed hands two months earlier at about $0.61 in cash (plus a 600 MHz swap).
- **Satellite assets have been repriced.** Globalstar at about $11B and Iridium at about $8B; AST pays about $80M a year for L-band.
- **Low-band is the scarce input.** SpaceX's own move into 800 MHz confirms it.
- **Coverage demand from machines is real.** Examples: the Toyota and Deutsche Telekom IoT work on NTN Direct.

Undercuts the thesis:
- **Carrier stocks fell on each SpaceX spectrum step.** After the August 2026 earnings and after the October 2026 Grain deal (one report says T-Mobile fell 7.7%; another says 13%). Markets read convergence as competition, which is the banker's point.
- **D2D cannot serve urban demand.** Its per-km2 capacity is the constraint above.
- **Revenue is small.** SpaceX does not disclose it, and AST's is mostly non-subscriber.
- **Regulators are adding supply** through flexible-use waivers and sharing.
- **Buyer demand may fade.** Once SpaceX completes about 79 MHz of owned US spectrum, its incremental appetite may fall.
- **Execution risk is high:** AST's slips, the New Glenn failure in May 2026, and Starship's cadence.

Probabilistic view (Whitesail judgment):

2028:
- About 85% that the EchoStar transfer closes by end-2027.
- Next-gen SpaceX D2D is in early deployment (P50 about 1,000-1,500 satellites).
- Starlink Mobile monthly users: P50 about 70M.
- AST: P50 about 80 satellites.
- Global D2D revenue: P50 about $2.5B.
- About 55% that SpaceX sells US retail mobile service under its own brand on its own spectrum.

2030:
- D2D satellites: P50 about 3,500.
- Revenue: P10/P50/P90 of $2B/$6B/$15B.
- About 65% that at least one more US spectrum deal above $5B is driven by a satellite operator (Ligado, remaining AWS-3, or a cable or regional holder).
- About 30% that SpaceX runs at least 30,000 active terrestrial sites.

2035:
- About 80% that D2D is a standard feature of most new phones.
- About 85% that D2D carries under 2% of developed-market mobile data.
- Revenue: P50 about $15B.
- About 20% that SpaceX is a top-four US operator by subscribers.

Investability. There is no clean passive way to own scarce spectrum through D2D:
- **ASTS** is a high-beta bet on execution.
- **SPCX** is dominated by AI, broadband and launch.
- **GSAT and IRDM** are now merger-arbitrage positions with capped upside.
- **EchoStar (SATS)** has turned its spectrum into cash plus SpaceX stock.
- **Viasat** holds contested L-band and S-band rights.
- **The US carriers** bear the competitive risk.

The evidence supports "spectrum is being repriced by new strategic buyers." It does not support "incumbent holders will capture that value through pricing."

### Key findings
- [P] Starlink describes its first-generation Direct to Cell fleet as more than 650 satellites in low Earth orbit.: 650+ satellites (2026; Starlink (company site), https://www.starlink.com/direct-to-cell)
- [S] Starlink Mobile reached about 22 million monthly users in Q3 2026, up 37% from Q2, per COO remarks on the earnings webcast; mobile revenue was not disclosed.: 22 million monthly users (Q3 2026 (reported 2026-10-20); Payload Space, https://payloadspace.com/spacexs-ai-revenue-leads-q3-earnings/)
- [W] SpaceX priced its IPO on June 11, 2026 at $135 per share, raising about $75 billion at a valuation of about $1.77 trillion, and began trading on Nasdaq as SPCX on June 12.: $135/share; ~$75B raised; ~$1.77T (2026-06-12; Wikipedia (Initial public offering of SpaceX), https://en.wikipedia.org/wiki/Initial_public_offering_of_SpaceX)
- [S] SpaceX said its next-generation Starlink Mobile system will operate in 65 MHz of spectrum bought from EchoStar, versus the 5 MHz the current system uses.: 65 MHz vs 5 MHz (2026-08-05; Via Satellite, https://www.satellitetoday.com/finance/2026/08/05/spacex-outlines-starlink-mobile-plans-in-first-earnings-report/)
- [P] The FCC approved the transfer of EchoStar's AWS-4 (about 40 MHz), H-block (10 MHz) and unpaired AWS-3 (15 MHz) licences to SpaceX with waivers for terrestrial, space and hybrid use plus new performance obligations.: ~65 MHz (2026-05-12; FCC Order Granting SpaceX-EchoStar Applications, https://www.fcc.gov/document/order-granting-spacex-echostar-applications)
- [P] The SpaceX purchase of EchoStar's AWS-4 and H-block licences is priced at about $17 billion: up to $8.5 billion in cash and $8.5 billion in SpaceX stock valued at signing.: $17B (2025-09-08; EchoStar Form 8-K exhibit (SEC), https://www.sec.gov/Archives/edgar/data/1415404/000141540425000041/tmb-20250907xex99d1.htm)
- [S] SpaceX agreed to buy Grain Management's nationwide 800 MHz portfolio of 546 licences covering up to 14 MHz; the FCC has accepted the applications for filing, which is not a grant.: up to 14 MHz; 546 licences (2026-10-08 (filing accepted late Oct 2026); Light Reading, https://www.lightreading.com/5g/spacex-s-bid-for-grain-s-lowband-spectrum-takes-a-step-forward)
- [S] SpaceX targets about 20x per-satellite throughput for next-generation mobile satellites versus first generation, more than 100x system capacity, and about 150 Mbps per user.: 20x per satellite; >100x system; 150 Mbps/user target (2026-02-25; SatNews, https://satnews.com/2026/02/25/spacex-unveils-150mbps-performance-target-for-upgraded-direct-to-cell-starlink/)
- [P] AST SpaceMobile's Q3 2026 investor slides list 12 BlueBirds (1-6 and 8-13) as unfolded and operating in orbit.: 12 satellites (2026-11-09; AST SpaceMobile Form 8-K exhibit 99.2 (SEC), https://www.sec.gov/Archives/edgar/data/0001780312/000119312526453758/asts-ex99_2.htm)
- [P] AST reported Q3 2026 revenue of $42.3 million (mainly gateways and government milestones), reaffirmed 2026 revenue guidance of $150-200 million, and held about $3.2 billion of cash.: $42.3M Q3; $150-200M FY; $3.2B cash (2026-11-09; AST SpaceMobile press release (Nasdaq), https://www.nasdaq.com/press-release/ast-spacemobile-provides-business-update-and-third-quarter-2026-results-2026-11-09)
- [P] Globalstar agreed to be acquired by Amazon at an implied equity value of about $11 billion; Amazon will continue supporting iPhone and Apple Watch satellite features.: ~$11B (2026-04-14; Globalstar Form 8-K exhibit (SEC), https://www.sec.gov/Archives/edgar/data/1366868/000114036126014528/ef20070409_ex99-2.htm)
- [P] Rocket Lab agreed to acquire Iridium for $54 per share in cash and stock, an enterprise value of about $8.0 billion, with closing expected in mid-2027.: $54/share; EV ~$8.0B (2026-06-29; Rocket Lab / Iridium press release (Nasdaq), https://www.nasdaq.com/press-release/rocket-lab-acquire-iridium-historic-deal-creating-fully-vertically-integrated-space-0)

### Forecast seeds
- How many smartphone-direct D2D-capable LEO satellites (all operators) will be in orbit at end-2030? [satellites] now ~660 (SpaceX ~650 Gen-1 + AST 12), Nov 2026; history: ~0 before 2024; SpaceX >600 by Feb 2026; AST 5 (2024) to 12 (Nov 2026); AST 45-by-end-2026 goal slipped to mid-2027; up: SpaceX authorized for 15,000 next-gen satellites with launches from 2027; AST >100 under contract for 2027-2028 and 6/month production; Amazon applied for 5,105; down: Starship cadence; New Glenn failure (May 2026) and AST slips; Gen-1 deorbits; capital intensity; interference limits; base rate: Large LEO constellations have typically deployed at roughly 30-60% of announced schedules (AST's 2026 target slipped about 6-9 months); suggested P10/P50/P90 1,500 / 3,500 / 7,000 (2030)
- Starlink Mobile monthly users worldwide at end-2028 [million monthly users] now ~22 million (Q3 2026); history: 7.4M monthly unique devices (Mar 2026); 22M monthly users (Q3 2026, +37% QoQ; different definition); up: Next-gen service end-2027; more MNO partners abroad; more handsets supported; possible US retail launch; down: Metric redefinition; US carrier conflict could end the T-Mobile partnership; users are mostly incidental (in coverage gaps); base rate: Starlink broadband consumer subscribers grew to 13.6M by Q3 2026 at roughly 50-70% a year; suggested P10/P50/P90 35 / 70 / 150 (2028)
- Global D2D satellite-to-phone service revenue (wholesale plus retail, all operators) in 2030 [USD billions per year] now Well under $1B in 2026 (Whitesail estimate; SpaceX undisclosed; AST guides $150-200M, mostly non-subscriber); history: Effectively zero before 2024; T-Satellite paid add-on from Jul 2025; Apple-Globalstar service funded by Apple; up: Next-gen broadband-class D2D (SpaceX 2027, Amazon 2028, AST 2027-2028); IoT/auto/wearable connectivity; carrier wholesale deals; government contracts; down: Bundling into existing plans at near-zero price; low willingness to pay outside emergencies; competition among 3-4 constellations; base rate: Whole legacy MSS industry is a few $B a year (Iridium alone $0.87B in 2025); suggested P10/P50/P90 2 / 6 / 15 (2030)
- Median implied price ($/MHz-pop) of US low/mid-band spectrum transactions with a satellite-operator buyer, 2027-2030 [USD per MHz-pop] now ~$1.00 (EchoStar AWS-4/H to SpaceX); ~$1.68 if the reported $8B Grain 800 MHz price is correct; history: T-Mobile to Grain 800 MHz at ~$0.61 cash (Aug 2026, plus 600 MHz); AT&T-EchoStar ~$1.35 (3.45 GHz + 600 MHz); up: SpaceX and Amazon balance sheets; low-band scarcity for indoor coverage; flexible-use waivers turning MSS into hybrid spectrum; down: Few buyers; FCC spectrum screen; new auction supply; SpaceX near its portfolio target; incumbents reluctant to sell to a competitor; base rate: US auctions 2014-2022 cleared roughly $0.8-2.7/MHz-pop (prior knowledge, not reverified this session); suggested P10/P50/P90 0.6 / 1.1 / 2.0 (2030)
- MHz of US licensed spectrum owned or long-term controlled (not leased from MNOs) by satellite D2D operators at end-2030 [MHz] now ~163 MHz incl. pending (SpaceX 65+14+5 regional, AST ~45 L-band, Globalstar/Amazon ~25, Iridium ~9); history: Before 2025, satellite operators held only MSS bands (Globalstar, Iridium, Ligado, EchoStar AWS-4 unused); 2025-2026 SpaceX added ~80 MHz; up: Possible Ligado/other MSS or AWS-3 purchases; FCC reallocation of MSS bands to flexible use; Amazon adding terrestrial spectrum; down: Closings fail (EchoStar due ~Nov 2027; Grain pending); FCC concentration limits; AST's L-band rights contested; base rate: Two large satellite-buyer spectrum transactions in 2025-2026 (EchoStar, Grain) plus two operator takeovers (Globalstar, Iridium); suggested P10/P50/P90 150 / 200 / 300 (2030)
- AST SpaceMobile BlueBird satellites in orbit at end-2028 [satellites] now 12 (Nov 2026); history: 5 Block 1 (Sep 2024); 12 operating by Nov 2026; 45 target moved from 2026 to mid-2027; up: >100 satellites under launch contracts for 2027-2028; 6/month production target; $3.2B cash; down: Launch availability (SpaceX scheduling, New Glenn reliability); Blacklift not before late 2028; funding needs; base rate: AST has delivered roughly half of its stated near-term launch targets on time; suggested P10/P50/P90 40 / 80 / 115 (2028)
- Starlink Mobile US standalone retail subscribers (on SpaceX-owned spectrum, not via a carrier partner) at end-2030 [million subscribers] now 0; history: No standalone US service; SpaceX says it intends to become a full mobile telco; reportedly seeking >=80,000 US cell sites; up: EchoStar spectrum close (~Nov 2027) with flexible-use rights; 800 MHz for indoor coverage; tower leases; bundling with Starlink broadband (13.6M consumer subs globally); down: Urban capacity requires a terrestrial build (TD Cowen >$80B); carriers refuse roaming/wholesale; handset and device support; regulatory performance obligations; base rate: US new entrants have grown slowly: Dish/Boost took years to reach mid-single-digit millions, largely from acquired bases; cable MVNOs took about 7 years to reach ~20M lines (prior knowledge, not reverified); suggested P10/P50/P90 0.3 / 3 / 12 (2030)

### Gaps
The research was cut short:
- **Searches:** Only 21 searches completed, below the 25 required. The shared web-search limit for this turn was used up before the Viasat/Space42 (Equatys), Lynk/Omnispace/SES and Skylo searches ran.
- **Page fetches:** Direct fetching failed for reuters.com, lightreading.com and telecomtv.com, and per the session's network guidance no other sites were tried. All facts therefore come from search-result summaries; no primary filing was opened directly. SEC, FCC and company-release items are tagged P only where the summary quoted the filing.
- **Reuters article:** The 2026-10-08 Reuters story could not be read. Its date matches the SpaceX-Grain 800 MHz deal, which is assumed to be its subject.

Not confirmed:
- **Deal terms:** The ~$8B Grain price (WSJ-reported), the price of the unpaired AWS-3 piece of the EchoStar deal (~$2.6B in prior reporting), and whether SpaceX acquired EchoStar's global or EU 2 GHz MSS rights.
- **Market data:** AST's November 2026 market cap; Starlink Mobile revenue; the 22M Q3 user figure appears only in secondary reports of earnings-call remarks.
- **Operator details:** T-Satellite subscriber or usage numbers for 2026; Globalstar's satellite count; Iridium's exact MHz (~8.7 MHz is from memory).
- **Other players:** Status of Equatys (Viasat-Space42), the Lynk-Omnispace merger and SES role, Skylo's current partners, and Vodafone/Rakuten partnership terms with AST. These are carried from prior knowledge and flagged in the records; Space42, Skylo and Lynk records link to company homepages that were not opened this session.
- **Regulation:** 2026 FCC actions on out-of-band emission limits and EPFD (beyond a headline that the FCC approved D2D/sharing frameworks on 2026-05-12, content not read); the EU 2 GHz MSS licence renewal process for 2027; the status of WRC-27 agenda item 1.13.

Not retrieved:
- **Capacity analyses:** Independent beam-capacity work (e.g., Tim Farrar, academic papers). All per-km2 capacity figures are Whitesail order-of-magnitude estimates. In the capacity chart, the Light Reading pages linked to terrestrial rows give context only; they are not the source of those numbers.
- **Market forecasts:** Third-party D2D subscriber and revenue forecasts (ABI, NSR, Analysys Mason, Quilty and others). The d2d_market chart therefore pairs company actuals with Whitesail forecasts.

Conflicting figures:
- **T-Mobile share drop on 2026-10-09:** one report says 7.7% to $146.54, another says 13%. Not reconciled.
- **Globalstar deal value:** $10.8B to $11.57B across sources.
- **AST satellites in orbit:** 12 per the Q3 slides, 13 per an August article.

## economics

Short answer. Through November 2026, owning spectrum has not by itself produced shareholder returns for US carriers. Their stocks have moved on pricing, share shifts and perceived competitive threats. The largest spectrum-linked gains went to a seller with more than one bidder (EchoStar, about +375% in 2025), not to holders of licenses already deployed. The Goldman banker's view fits the 2024-2026 evidence, with two qualifications set out below.

1. Demand grew, but revenue did not keep pace. CTIA reports US mobile data use of 159.3 trillion MB in 2025, up 20% (slower than the prior two years). Over the same year the wireless service price index fell 4.1% and price per GB fell 21%. Light Reading, citing CTIA, puts 2025 industry service revenue at about $235B, up 69% since 2007. That is about 3% a year in nominal terms, roughly flat after inflation, over a period when traffic rose by orders of magnitude. Carriers sell capacity at falling unit prices. CTIA projects data demand to roughly quadruple by 2032, with AI-related traffic growing about three times faster than other traffic. For the thesis to work for incumbents, that demand would have to break the pattern of the last two decades. Nothing in the 2026 results shows AI devices moving service revenue yet.

2. Q3 2026: growth came from taking share, not from raising prices. Verizon added 406k postpaid phones (44k a year earlier), its best third quarter in five years, and raised 2026 guidance to 1.1-1.2M. But postpaid ARPA fell 1.9% to $168.08, so the growth was bought with promotions and lower prices. CEO Dan Schulman has said the earlier price-led strategy cost about 2.25M net adds, and he pledged no increases "without corresponding value." Verizon still raised its top plan $5 for new customers in May 2026. AT&T added 379k (405k a year earlier), held churn at 0.92%, and grew wireless service revenue 5.0% to $17.8B. T-Mobile stopped disclosing phone net adds. Its postpaid account adds fell 31% to 274k and account churn rose 12 bps to 1.09%. Still, its ARPA rose 4% to $155.73 and postpaid service revenue rose 9%. T-Mobile is the one carrier showing pricing power.

Cable keeps taking share. Charter added 508k mobile lines pro forma (13.5M total, including Cox) and Comcast added 368k (about 10.6M). The two cable companies' roughly 876k lines exceeded AT&T's and Verizon's combined phone adds (785k). About half of Comcast's postpaid connects were free lines. This is a promotional market, not one where scarce spectrum lets carriers raise prices.

3. Returns came from lower capex and higher free cash flow. After the 5G peak, industry network investment was about $30B in 2025 (CTIA). Verizon guides 2026 capex to $16.0-16.5B. T-Mobile expects about $10.0B, and its Q3 cash capex was down 14%. Charter's Q3 capex fell 11.2%. Free cash flow rose: T-Mobile guides adjusted FCF of $18.7-18.8B, and AT&T generated $5.0B in Q3. Shareholder value in this sector is mostly dividends and buybacks funded by FCF (Verizon yields about 6.1%). Spectrum shows up mainly as a cost to be recovered: AT&T paid $23B for EchoStar's 50 MHz, a deal that closed on July 28, 2026.

4. Market structure after EchoStar. The FCC approved EchoStar's sales on May 12, 2026, with a $2.4B escrow condition. The US went from four facilities-based carriers to three, and Boost now runs as a hybrid MVNO on AT&T. Alongside the three carriers are cable MVNOs with about 24M lines and SpaceX as a growing spectrum holder. SpaceX is buying AWS-4/H-block spectrum from EchoStar for about $17B, with closing reportedly expected around late 2027. It is also buying up to 14 MHz of paired 800 MHz spectrum from Grain Management, reportedly for about $8B and pending FCC approval. The FCC has approved 15,000 Gen2 satellites. Normally a move from four networks to three supports pricing. Here cable, and the prospect of SpaceX, have offset that.

5. SpaceX is a credible bidder, an unproven operator, and a large factor in carrier stock prices. In its favor:
- Q2 2026 revenue of $7.8B, about double a year earlier
- 12M Starlink subscribers and 7.4M monthly unique direct-to-cell devices
- public stock it can use to pay for deals
- a stated intent to compete with the major US carriers
- reported talks to use about 80,000 cell sites

Against it:
- Satellites have limited capacity indoors and in dense areas. T-Mobile says more than 70% of traffic is indoors.
- Its key spectrum deals have not closed.
- Starlink ARPU fell 22%, and the company still posts losses.
- T-Mobile has ruled out an MVNO deal.

DISH is the reference case: an entrant with plenty of spectrum that never scaled, and that captured value by selling its licenses.

The market treats SpaceX's spectrum purchases as bad for incumbents. Carriers fell 4-5% on the September 2025 EchoStar deal, and 2-4% after hours when SpaceX outlined its mobile plans in August 2026. On October 9, 2026 they fell 9.8% (AT&T), 8.8% (Verizon) and 13.3% (T-Mobile, its worst day as a public company). That is the opposite of what the thesis predicts for license holders. Verizon was still up about 14% for 2026 by mid-November, while T-Mobile was down about 22% by late October.

6. Valuation. Our own estimates, which are not sourced and carry low confidence, put EV/EBITDA at about 6.5-7.5x and license book value at about 38-47% of enterprise value. At those multiples, the market pays no premium for spectrum over what the carriers paid for it. The value is real but hard to unlock: turning it into cash means selling to a small, regulated set of buyers or raising prices.

7. Scoring the banker's view.
- "Buyers are not broad and control is regulated": supported. In 2025-26 the buyers were AT&T, SpaceX, Grain (an intermediary) and a few smaller in-market deals, all under FCC conditions.
- "Telcos see no value unless they can raise prices": supported for Verizon (ARPA down 1.9%, its price-hike strategy reversed) and for the industry (service price index down 4.1%). T-Mobile is the exception, with ARPA up 4%.
- "Competition goes the other way": supported by cable's adds, free-line promotions, T-Mobile's higher churn and the stock reactions to SpaceX.

Two qualifications:
- License holders can capture value when an outside bidder appears. EchoStar went from near-bankruptcy to the best shareholder return in the Fortune 500. The 800 MHz licenses reportedly moved from T-Mobile to Grain to SpaceX for about $8B, roughly $1.7 per MHz-pop if 14 MHz is the total width. So incumbents can sell non-core licenses at a premium.
- Fewer networks, plus SpaceX's need for land-based infrastructure, create options for wholesale deals, tower leases or M&A. MoffettNathanson argued T-Mobile could benefit, and Morgan Stanley called the Grain deal constructive for tower companies.

8. Probabilistic view (our judgment). For 2030 we weight three states:
- Grind (about 50%): service revenue grows 2-3% a year to roughly $255-270B, multiples stay at 6-7.5x, cable reaches 33-37M lines, and SpaceX has fewer than 3M direct US subscribers.
- Price pressure (about 30%): SpaceX and cable push ARPA down, service revenue is flat in nominal terms, and multiples fall to 5-6x.
- Convergence premium (about 20%): spectrum scarcity is turned into cash through sales or M&A (for example, SpaceX or a hyperscaler buys a carrier or a large spectrum block), and incumbents re-rate to 8x or more.

For 2028 the ranges are narrower and the grind case is more likely (about 60%), because the SpaceX deals close in 2027 at the earliest and building a network takes years. By 2035 the ranges are wide. A 6G and upper C-band capex cycle starting around 2030 would weigh on free cash flow in every state.

For a passive investor, the evidence says AT&T, Verizon and T-Mobile are cash-flow and dividend holdings with spectrum carried at cost, not a way to own rising spectrum value. Exposure to that theme has come through sellers in contested sales and possibly tower companies, and those gains were event-driven and volatile. AST SpaceMobile, for example, rose 244% in 2025 and was down about 55% in 2026 by mid-November.

### Key findings
- [S] SpaceX agreed to buy up to 14 MHz of paired nationwide 800 MHz low-band spectrum from Grain Management, subject to FCC approval; the WSJ put the price at about $8B in cash.: up to 14 MHz paired; ~$8B reported (2026-10-08; Reuters (syndicated by The Star), https://www.thestar.com.my/tech/tech-news/2026/10/09/spacex-takes-aim-at-us-wireless-carriers-with-spectrum-acquisition)
- [S] On the first trading day after the SpaceX-Grain spectrum deal, AT&T, Verizon and T-Mobile shares closed down 9.8%, 8.8% and 13.3%.: T -9.8%, VZ -8.8%, TMUS -13.3% (2026-10-09; Axios, https://www.axios.com/2026/10/09/spacex-elon-musk-spectrum)
- [S] AT&T closed its $23B purchase of EchoStar's 30 MHz of 3.45 GHz and 20 MHz of 600 MHz spectrum, and Boost continues on a hybrid MVNO with AT&T.: $23B for 50 MHz (2026-07-28; Broadband Breakfast, https://broadbandbreakfast.com/echostar-at-t-close-23-billion-spectrum-sale/)
- [P] Verizon added 406,000 postpaid phones in Q3 2026 versus 44,000 a year earlier, its strongest third quarter in five years.: 406k (vs 44k) (Q3 2026; Verizon earnings release (via Finviz), https://finviz.com/news/407554/verizon-delivers-another-record-breaking-quarter-with-3q-2026-results-driven-by-strong-postpaid-phone-and-account-additions)
- [P] Verizon postpaid ARPA fell 1.9% year over year to $168.08 even as phone net adds surged.: $168.08 (vs $171.27) (Q3 2026; Verizon earnings release (via Finviz), https://finviz.com/news/407554/verizon-delivers-another-record-breaking-quarter-with-3q-2026-results-driven-by-strong-postpaid-phone-and-account-additions)
- [P] AT&T wireless service revenue grew 5.0% year over year to $17.76B in Q3 2026, from $16.93B.: $17.76B (+5.0%) (Q3 2026; AT&T Form 8-K Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/0000732717/000073271726000370/t-3q2026exhibit991.htm)
- [S] T-Mobile no longer discloses postpaid phone net adds; postpaid net account additions were 274,000 in Q3 2026, down 31% year over year.: 274k accounts (-31%) (Q3 2026; Fierce Network, https://www.fierce-network.com/wireless/t-mobile-raises-profit-adds-274k-accounts-q3)
- [P] Charter added 508,000 mobile lines pro forma in Q3 2026 (440,000 legacy Charter plus 68,000 Cox), reaching 13.5M lines, up 1.8M over twelve months.: 508k; 13.5M lines (Q3 2026; Charter earnings release (via Finviz), https://finviz.com/news/418256/charter-announces-third-quarter-2026-results-and-launches-new-operating-model)
- [S] Comcast added 368,000 wireless lines in Q3 2026, down from 414,000 a year earlier and below the 399,000 consensus, for about 10.6M lines.: 368k; ~10.6M lines (Q3 2026; Light Reading, https://lightreading.com/cable-technology/comcast-drops-more-broadband-subs-as-restructuring-and-layoffs-loom)
- [P] Wireless service prices fell 4.1% from 2024 to 2025 and price per GB used fell 21%.: -4.1% price; -21% per GB (2025; CTIA 2026 Annual Survey (via Benton), https://www.benton.org/headlines/ctia-2026-annual-survey-highlights)
- [S] US wireless industry service revenue rose 69% between 2007 and 2025 to about $235B, roughly 3% a year nominal.: $235B (2025) (2025; Light Reading (citing CTIA), https://lightreading.com/wireless/inflation-mostly-skipped-the-wireless-bill)
- [S] EchoStar went from near-bankruptcy to the best shareholder return in the Fortune 500 on the back of its spectrum sales to SpaceX and AT&T.: #1 Fortune 500 shareholder return (2026-06-04; Fortune, https://fortune.com/2026/06/04/echostar-stock-elon-musk-spacex-spectrum-bankruptcy-to-best-shareholder-return-fortune-500/)

### Forecast seeds
- Combined Charter + Comcast mobile lines at year-end 2030 [million lines] now ~24.1M (Q3 2026: Charter 13.5M incl. Cox, Comcast ~10.6M); history: Charter +1.8M and Comcast +1.6M over the 12 months to Q3 2026; Q3 2026 adds 876k combined (508k Charter pro forma, 368k Comcast) vs ~896k a year earlier on a legacy basis; Comcast adds falling (368k vs 414k); up: Free-line promotions (~50% of Comcast connects); bundling to defend broadband against fiber and FWA; Cox footprint added to Charter; MVNO cost model; CBRS offload; possible alternative wholesale hosts (including SpaceX); down: Shrinking broadband base caps attach (Comcast -144k, Charter -233k broadband in Q3 2026); free-line roll-off churn; carrier retaliation on price; MVNO terms with Verizon; base rate: Linear ~3.4M/yr gives ~38M by end-2030; adds decaying ~10%/yr gives ~33M. Implied path: 2028 P50 ~30M; 2035 P50 ~42M (wide range); suggested P10/P50/P90 30 / 35 / 40 (2030)
- US wireless industry service revenue (CTIA basis) in 2030 [$B nominal] now ~$235B (2025); history: ~$139B in 2007 (derived) to ~$235B in 2025, ~3.0% nominal CAGR (about flat in real terms); service price index -4.1% and price per GB -21% in 2025; AT&T wireless service +5.0% and T-Mobile service +6% in Q3 2026; up: Data demand ~4x by 2032 with AI traffic growing faster (CTIA); connected devices and IoT lines; FWA; 4-to-3 facilities consolidation; T-Mobile-style ARPA growth (+4%); down: Falling price per GB; cable MVNO and SpaceX competition; Verizon ARPA -1.9%; saturated phone base; free-line promotions; base rate: 2007-2025 nominal CAGR ~3.0%; 2.0-2.5% gives $259-266B in 2030. Implied path: 2028 P50 ~$250B; 2035 P50 ~$290B; suggested P10/P50/P90 245 / 262 / 282 (2030)
- Average EV/EBITDA of AT&T, Verizon and T-Mobile at end-2030 [x (EV / forward adj. EBITDA)] now ~6.9x (Whitesail estimate Nov 2026: T ~6.7x, VZ ~6.7x, TMUS ~7.4x); history: T-Mobile de-rated from a premium: -9% YTD by Sep 2026 and ~-22% by late Oct after -13.3% on Oct 9; Verizon +29% YTD by Sep, +14% by mid-Nov; up: Spectrum monetized through sales or M&A; SpaceX or hyperscaler bid for a carrier; rational 3-network pricing; FCF growth (T-Mobile guide $18.7-18.8B); down: SpaceX entry and price pressure; cable share gains; 6G capex cycle around 2030; higher rates; base rate: US incumbent telcos have mostly traded at about 6-8x EV/EBITDA; scenario weights 50% grind (6-7.5x), 30% price pressure (5-6x), 20% convergence premium (8x+); suggested P10/P50/P90 5.5 / 6.8 / 8.3 (2030)
- US wireless industry network capex (CTIA basis) in 2030 [$B per year] now ~$30B (2025); history: Verizon 2026 capex guide $16.0-16.5B (consolidated); T-Mobile ~$10.0B in 2026 with Q3 cash capex -14% YoY; Charter Q3 2026 capex -11.2%; up: 6G builds from ~2030 (T-Mobile CTO); upper C-band and other new spectrum deployment; densification for AI uplink traffic; any SpaceX terrestrial build; down: Post-5G harvest mode; network sharing; fiber prioritized over wireless; satellite offload in rural areas; base rate: Past generations: capex peaked early in each cycle then fell 20-30%; a 6G ramp would likely start 2029-2031, so 2030 sits near the trough-to-ramp turn. 2028 P50 ~$29B; 2035 P50 ~$34B; suggested P10/P50/P90 25 / 31 / 40 (2030)
- SpaceX/Starlink Mobile paying direct US mobile subscribers at end-2030 (excluding carrier-billed satellite add-ons) [million subscribers] now ~0 direct US retail mobile subscribers; 7.4M monthly unique D2C devices globally; 12M Starlink broadband subscribers (Q2 2026); history: EchoStar AWS-4/H-block (~$17B) pending, expected ~2027; Grain 800 MHz (~$8B) pending FCC; 15,000 Gen2 satellites approved; reported talks on ~80k cell sites; T-Mobile refused an MVNO; up: Low-band plus 2 GHz spectrum; IPO capital; tower leasing; bundling with Starlink broadband; regulatory goodwill; down: Satellite capacity limits indoors and in dense areas (>70% of traffic indoors); deal closings and FCC approvals; handset support for new bands; Starlink ARPU -22%; incumbents refuse wholesale access; base rate: DISH/Boost: about 7M subscribers ~5 years after entering as 4th carrier, never scaled, exited by selling spectrum; cable MVNOs: ~24M lines in ~8 years on incumbent networks. Implied 2028 P50 ~0.5M; 2035 P50 ~8M; suggested P10/P50/P90 0.3 / 2.5 / 10 (2030)
- Postpaid ARPA YoY growth, simple average of Verizon and T-Mobile, full-year 2028 [% YoY] now +1.05% (Q3 2026: T-Mobile +4.0%, Verizon -1.9%); history: T-Mobile ARPA guide raised to ~3.5% for 2026; Verizon ARPA fell from $171.27 to $168.08 while phone adds rose ninefold; CTIA service price index -4.1% in 2025; up: Premium plan mix, fees and bundles; 3-network structure; slower promotions if share gains fade; down: Cable free lines; SpaceX entry; Verizon's no-price-hike pledge; device subsidies; base rate: Industry service revenue ~3% nominal CAGR since 2007 with line growth ~1-2%/yr implies ARPU growth around 0-2%/yr; suggested P10/P50/P90 -2.0 / 1.0 / 3.0 (2028)
- Average monthly postpaid phone churn of AT&T and Verizon in Q3 2030 [% per month] now 0.93% (Q3 2026: AT&T 0.92%, Verizon 0.94%); history: AT&T flat YoY; Verizon -4 bps YoY after 0.97% in Q1 2026; T-Mobile account churn 1.09% (+12 bps); up: SpaceX entry; cable promotions; switching incentives; price increases; down: Convergence bundles with fiber (AT&T 442k fiber adds); multi-year device financing locks; fewer facilities-based rivals; base rate: US big-carrier postpaid phone churn has mostly been in a ~0.8-1.0% range since the mid-2010s; suggested P10/P50/P90 0.82 / 0.95 / 1.15 (2030)

### Gaps
Research limits: the shared web search budget ran out after 21 searches, short of the 25 target. WebFetch failed for sec.gov and verizon.com because those hosts are not in this session's allowed network list, so I stopped fetching. As a result, no primary filing or release was opened directly. Figures tagged P come from search-engine summaries of company releases, 8-Ks and CTIA material, and should be checked against the documents.

Not confirmed:
- AT&T postpaid phone ARPU for Q3 2026 or any year.
- T-Mobile postpaid phone net adds and phone ARPU (no longer disclosed in 2026). Verizon reports only ARPA.
- Annual 2022-2025 carrier capex, ARPU and net adds by carrier, so the size of the post-5G capex decline from its peak is not quantified from sources.
- Industry Q3 2026 total adds by source, including Boost subscriber losses after the MVNO transition.
- AT&T and EchoStar 2026 year-to-date returns as of November, and the S&P 500 November YTD.

Approximations:
- 2024 total returns for T, VZ and TMUS rely on recalled year-end prices plus dividends.
- 2025 returns for VZ and TMUS are derived from 2026 YTD figures.
- EV/EBITDA and spectrum book value as a share of EV are Whitesail estimates that use recalled 10-K license balances (AT&T ~$127B, Verizon ~$156B, T-Mobile ~$97B at end-2024) and estimated net debt. Treat them as roughly plus or minus 0.7x and plus or minus 5 points.

Uncertain deal details:
- The $8B Grain price comes from the WSJ via Axios and was not officially disclosed.
- Whether 14 MHz is the total width or per direction is unclear, so the implied ~$1.7/MHz-pop assumes 2x7 MHz.
- The structure of the T-Mobile-to-Grain transfer (reported as an August 2026 swap) is unclear.
- The SpaceX-EchoStar closing timing (~2027) comes from secondary reporting.
- The $235B 2025 service revenue figure comes from Light Reading citing CTIA. I could not confirm which Light Reading article carries it or read the CTIA report directly.

No data was found on AI, robotics or IoT connected-device line growth or revenue in carrier results, so the AI-demand part of the thesis cannot be measured from carrier financials yet. The 2028/2030/2035 scenario weights are analyst judgment, not model outputs.

## investables

Bottom line. Licensed spectrum has large value that can be realized, and SpaceX now buys it repeatedly. But the 2025-2026 deals do not yet show a scarcity premium, and no public security gives clean, liquid exposure to spectrum values. The large US carriers own most of the asset. They are also its main buyers, so their equity tracks pricing power, not license values. The purest listed plays are small and pay off mainly through a sale. EchoStar, the best-known "spectrum stock", is now mainly a claim on SpaceX equity.

What the 2025-2026 deals show. EchoStar turned its licenses into about $43B of announced consideration.
- AT&T closed its ~$23B purchase on July 28, 2026: 30 MHz of 3.45 GHz plus 20 MHz of 600 MHz. EchoStar netted ~$20.25B, and AT&T put $2.4B into an FCC-mandated trust for shutting down the Dish 5G network.
- SpaceX agreed in September 2025 to buy the AWS-4 and H-block licenses for $17B ($8.5B cash, $8.5B stock). It later added up to 15 MHz of unpaired AWS-3 for $2.6B in stock.
- EchoStar's stock consideration is fixed at about 261.8M SpaceX shares at $42.40 each. The FCC approved the transfers in May 2026. The SpaceX licenses sit in a trust, and that closing is expected in 2027.
- On October 8, 2026, SpaceX agreed to buy up to 14 MHz of paired nationwide 800 MHz from Grain Management, to add in-building coverage. Grain had bought that spectrum from T-Mobile in August, reportedly for $2.9B cash plus 600 MHz spectrum (one weak source).

Implied prices, on my arithmetic with 335M US pops:
- AT&T paid about $1.37/MHz-pop blended.
- SpaceX paid about $1.01 for AWS-4/H-block and about $0.52 for unpaired AWS-3.
- Grain paid about $0.62 in cash for 800 MHz.

For comparison, past auctions (from memory, not re-verified here): AWS-3 in 2015 about $2.2, 600 MHz in 2017 about $0.9, C-band in 2021 about $0.9 before clearing payments, 3.45 GHz in 2022 about $0.7. The recent deals sit inside that range, at the high end for mid-band, not above it.

The universe, from purest to least pure.
- High purity, small size: Anterix (ATEX, 900 MHz broadband, ~6 MHz), NextNav (NN, lower 900 MHz, ~8 MHz), Globalstar (GSAT, ~25 MHz of satellite L/S-band with terrestrial Band 53 rights, anchored by Apple) and Array Digital Infrastructure (AD, the spectrum and towers left after the UScellular sale, partly sold to AT&T and Verizon). These pay off mainly through a sale, and with only four or five possible buyers, that is a constraint.
- EchoStar (now ECHO; it changed from SATS on June 24, 2026): at SpaceX's November 18 close of $143.50, the 261.8M shares are worth ~$37.6B. Adding $8.5B of pending SpaceX cash and $13.44B of cash on hand, less ~$9.7-9.8B of debt, gives a gross look-through value of ~$50B. That is before taxes and wind-down costs (one unverified report puts cash use at $5-7B). Its market value has been reported near $34B (weak, undated source), which implies a discount of roughly 30%. UBS valued the stake at ~$39B. The stock now trades on SpaceX's price, closing risk, taxes and governance, not on spectrum.
- Big-3 carriers (T, VZ, TMUS): on pre-2026 balance sheets plus known deals, FCC licenses are about 45-47% of enterprise value (EV) at AT&T and Verizon and about 29% at T-Mobile. These are rough book-value figures, not re-verified this session. The carriers own most of the valuable bands, but scarcity raises what they pay for capacity about as much as it raises their asset values.
- Satellite: AST SpaceMobile (L-band rights via Ligado, S-band rights, partner carriers' low-band), Iridium and Viasat (satellite L-band). Their value depends on FCC rules for terrestrial and direct-to-device use, and SpaceX's buildout competes with them directly.
- SpaceX (SPCX): it listed on June 12, 2026 after pricing at $135 and is now worth ~$1.9T. Its ~$20-23B of spectrum purchases is about 1% of that. Owning SPCX is a bet on Starlink, launch and xAI, not on spectrum. Alphabet's SpaceX stake is an even more diluted version.
- Cable and towers: low exposure. Comcast and Charter hold modest 600 MHz and CBRS positions and resell Verizon's network (MVNOs). The tower companies hold no licensed spectrum, but they gain if scarce spectrum forces carriers to add sites.
- Funds: none isolates spectrum. IYZ and XTL are mostly carriers plus some small spectrum names. UFO and ARKX hold satellite names. XOVR and DXYZ hold SpaceX, and now that SPCX trades directly, paying those funds' premium for access makes less sense.

Evidence that supports the thesis:
1. SpaceX is paying for spectrum that works on the ground: ~$19.6B to EchoStar, then 800 MHz from Grain, plus reported small regional AWS-3 purchases. Satellites alone do not deliver dense-area capacity or indoor coverage, and the Grain deal was explicitly for in-building coverage.
2. AT&T paid $23B for 3.45 GHz spectrum it was already leasing, so owned capacity is worth a premium to carriers.
3. Spectrum that is sitting unused can be sold at scale. Fortune ranked EchoStar's shareholder return the best in the Fortune 500.
4. Regulators are allowing satellite and terrestrial networks to converge. The FCC approved large license transfers and reportedly 15,000 next-generation Starlink Mobile satellites (weak source).

Evidence that undercuts it:
1. No scarcity premium is visible yet. The 2025-2026 prices sit within past auction ranges.
2. Spectrum is illiquid and allocated by regulators. EchoStar sold under FCC pressure, two of its subsidiaries filed for bankruptcy during the closing delay, the AT&T deal took 11 months to close, and the SpaceX deal will take more than 15.
3. Supply is rising. The 2025 budget law restored FCC auction authority and requires large new auctions, including upper C-band (from memory, not re-verified). Satellite bands and spectrum sharing also add usable capacity.
4. Competition hurts carrier equity. A SpaceX mobile network with its own spectrum would be a fourth national competitor. The Goldman banker's point holds: spectrum can gain value while carrier stocks lose pricing power.
5. The available stocks are either volatile or tiny. SPCX has traded between ~$108 and $192.50 since June. A 1.3B-share lockup release on October 22 cut 9% in one day, and the main 180-day lockup ends December 8. Anterix is a sub-$1B stock.

Probabilistic view (my judgment, not market-implied):
- By 2028:
  - SpaceX-EchoStar closes: ~85%.
  - An upper C-band auction concludes: ~60%. Gross proceeds P10/P50/P90: $12B/$30B/$55B.
  - At least one of Anterix, NextNav or Globalstar is acquired or sells its core spectrum: ~45%.
- By 2030:
  - SpaceX controls at least 100 MHz (national equivalent) of US spectrum usable on the ground: ~45%.
  - The Big-3 carriers beat the S&P 500 over 2026-2030: ~35%.
  - Big-3 FCC license book value: P50 ~$445B, versus ~$410B now (estimated).
- By 2035:
  - Nominal mid-band deal prices reach at least 1.5x the 2025-2026 level of ~$1.0-1.4/MHz-pop: ~25%.
  - Operators that started in satellite own at least 20% of US mobile spectrum value: ~20%.

Answer to Jason's question. There is no clean passive vehicle. The closest options are:
- An equal-weight basket of the small pure plays (ATEX, NN, GSAT, AD). Exposure is high, but the basket is concentrated, illiquid and depends on sales happening.
- ECHO, as a claim on SpaceX shares bought at a discount, with closing and tax risk.
- Carrier ETFs (IYZ, XTL). Spectrum is a large share of carrier assets, but returns depend on pricing.

If convergence mainly adds competition, the gains are more likely to show up in sellers' and SpaceX's equity than in the incumbent carriers'.

Data caveat: the shared web-search budget ran out after 9 searches, and primary sites (SEC, FCC, Light Reading, Reuters) could not be fetched. Figures for companies other than EchoStar, SpaceX and AT&T are rough estimates from pre-2026 data and must be verified before use.

### Key findings
- [S] SpaceX agreed to buy a nationwide 800 MHz low-band portfolio from Grain Management to add in-building coverage to its 2 GHz spectrum; terms were undisclosed and FCC approval is pending.: up to 14 MHz paired, nationwide (2026-10-08; Light Reading, https://www.lightreading.com/satellite/spacex-feuls-mobile-ambition-with-another-helping-of-spectrum)
- [S] SpaceX agreed to buy EchoStar's AWS-4 and H-block licenses for about $17B, half in cash and half in SpaceX stock.: $17B ($8.5B cash + $8.5B stock) (2025-09-08; TechCrunch, https://techcrunch.com/2025/09/08/spacex-strikes-17b-deal-to-buy-echostars-spectrum-for-starlinks-direct-to-phone-service/)
- [P] EchoStar's stock consideration from SpaceX is fixed at about 261.8 million SpaceX Class A shares valued at $42.40 per share after SpaceX's 5-for-1 split.: 261.8M shares at $42.40 (~$11.1B at deal price) (2026-09-30; EchoStar Form 10-Q Q3 2026 (via search snippet), https://www.sec.gov/Archives/edgar/data/0001415404/000110465926121675/sats-20260930x10q.htm)
- [S] The SpaceX purchase of EchoStar spectrum was described as timed to close in 2027.: $19.6B; expected close 2027 (2026-07-29; Broadband Breakfast, https://broadbandbreakfast.com/echostar-at-t-close-23-billion-spectrum-sale/)
- [P] AT&T closed its acquisition of EchoStar's nationwide 3.45 GHz (30 MHz) and 600 MHz (20 MHz) licenses.: ~$23B; 50 MHz (2026-07-28; AT&T newsroom, https://about.att.com/story/2026/echostar-spectrum.html)
- [S] EchoStar's share of the AT&T payment was about $20.25B, and AT&T put another $2.4B into an FCC-mandated trust for decommissioning the Dish Wireless 5G network.: $20.25B to EchoStar; $2.4B to trust (2026-07; Broadband Breakfast, https://broadbandbreakfast.com/echostar-at-t-close-23-billion-spectrum-sale/)
- [W] EchoStar held cash and cash equivalents of $13.44B at September 30, 2026.: $13.44B (2026-09-30; Yahoo Finance (Simply Wall St), https://finance.yahoo.com/markets/stocks/articles/did-profit-rebound-just-shift-131337751.html)
- [S] UBS valued EchoStar's SpaceX stake at about $39B ($110 per EchoStar share) at the then-current SpaceX price, and at $55B ($156 per share) at its $210 SpaceX target; it rated EchoStar Buy with a $150 target.: $39B ($110/share); $55B at $210 SPCX (2026 post-IPO (exact date unconfirmed); Proactive Investors, https://www.proactiveinvestors.co.uk/companies/news/1098238/echostar-shares-rise-as-ubs-says-spacex-stake-makes-stock-undervalued-1098238.html)
- [S] SpaceX priced its IPO at $135 per share and listed on Nasdaq as SPCX, raising $75B in the base offering and $85.7B including the over-allotment.: $135/share; $75B base, $85.7B total (2026-06-11; CNBC, https://www.cnbc.com/2026/06/11/spacex-raises-75-billion-in-record-setting-ipo-ahead-of-nasdaq-debut.html)
- [W] SpaceX closed at $143.50 on November 18, 2026, about 6% above its IPO price.: $143.50/share (~$1.9T implied) (2026-11-18; Yahoo Finance (Motley Fool), https://finance.yahoo.com/markets/stocks/articles/spacex-stock-buy-now-184600694.html)

### Forecast seeds
- SpaceX (SPCX) equity market value [US$ trillion] now ~1.9 (2026-11-18 close $143.50; share count inferred); history: Dec 2025 secondary-market basis ~0.8 (Citi assumption); IPO 2026-06-11 ~1.77 at $135; first-day close ~2.1; Jun-15 close $192.50 (~2.5, calc.); Aug 2026 low ~$108 (~1.4); up: Starlink subscriber growth; direct-to-device revenue on owned spectrum; launch cadence; xAI monetization; down: AI capex; Dec 8 lockup supply; FCC/antitrust limits; competition (Kuiper, AST); key-person and governance risk; base rate: Mega-cap IPOs (Facebook 2012, Aramco 2019, Arm 2023) went from roughly flat to 2-3x over three years; dispersion is wide; suggested P10/P50/P90 0.9 / 2.2 / 4.5 (2030)
- Nominal price of nationwide US mid-band spectrum in secondary deals and auctions [$/MHz-pop] now ~1.0-1.4 (2025-26 EchoStar deals, calc. at 335M pops); history: AWS-3 2015 ~2.19; 600 MHz 2017 ~0.91; C-band 2021 ~0.89 before clearing; 3.45 GHz 2022 ~0.68 (training data); unpaired AWS-3 to SpaceX ~0.52; Grain 800 MHz ~0.62 (cash portion); up: AI-device traffic growth; SpaceX and carriers bidding against each other; little new mid-band below 4 GHz; down: Mandated 800 MHz auction pipeline; spectral-efficiency gains; satellite and shared bands; high interest rates; base rate: Mid-band prices fell from ~$2.2 (2015) to ~$0.7-0.9 (2021-22) as more mid-band supply came to market; suggested P10/P50/P90 0.5 / 1.0 / 1.9 (2030)
- Gross proceeds of the upper C-band (3.98-4.2 GHz) FCC auction [US$ billion] now Not yet held (statutory deadline ~July 2027 under the 2025 budget law; training data, not re-verified); history: C-band 2021: $81.1B for 280 MHz; 3.45 GHz 2022: $22.5B for 100 MHz; up: AT&T/Verizon capacity needs; SpaceX as a new bidder; up to 180 MHz offered; down: Altimeter and satellite protections cut usable MHz to ~100; carrier balance sheets stretched after the EchoStar deals; few bidders; base rate: 2021-22 mid-band auctions cleared at ~$0.68-0.89/MHz-pop; suggested P10/P50/P90 12 / 30 / 55 (2028)
- EchoStar market-value discount to gross look-through value (SpaceX consideration + cash - debt) [%] now ~30% (rough; market value from a weak, undated source); history: June 2026: New Street said the market priced the stake at $86/share vs ~$159 fair value; UBS stake value ~$39B (2026); up: SPCX falls (the discount widens with the share-price risk); tax leakage; litigation from bankrupt subsidiaries; closing delays; down: Spectrum Acquisition Closing in 2027; distribution of SpaceX shares to holders; buybacks; base rate: Listed holding-company discounts are typically 10-40%; suggested P10/P50/P90 5 / 20 / 40 (2028)
- Combined FCC license book value of AT&T, Verizon and T-Mobile [US$ billion] now ~410 (est.: T ~151, VZ ~157, TMUS ~101); history: ~383 at end-2024 (training data); +$23B AT&T-EchoStar in 2026; UScellular spectrum deals 2025-26; up: Upper C-band auction; AWS-3 re-auction; further secondary purchases; down: Sales or swaps to SpaceX or Grain; impairments; leasing instead of buying; base rate: Grew from ~$270B (2020) to ~$383B (2024) on the C-band and 3.45 GHz auctions (training data); suggested P10/P50/P90 405 / 445 / 500 (2030)
- US spectrum usable on the ground that SpaceX owns or controls (national-equivalent MHz) [MHz] now ~0 closed; ~65 pending from EchoStar (AWS-4 40 + H-block 10 + AWS-3 15) plus up to 14 pending from Grain (800 MHz), ~79 in total; history: 2022-2025: relied on its T-Mobile partnership for PCS G-block access (training data); Sept 2025 EchoStar deal; Oct 2026 Grain deal; up: Globalstar or other satellite-band purchases; upper C-band bids; more secondary deals; down: FCC aggregation limits; carrier opposition; AI-capex competition for capital; base rate: Dish built a ~100-MHz-class national position over about a decade (2008-2021); suggested P10/P50/P90 65 / 100 / 160 (2030)
- How many of ATEX, NN, GSAT, AD and IRDM are acquired or sell their core spectrum [count (of 5)] now 0 fully (AD partly, via agreed sales to AT&T and Verizon); history: 2018-2026 exits of US spectrum holders: Straight Path (to VZ 2018), Shentel wireless (to TMUS 2021), UScellular (2025), EchoStar (2025-26); up: SpaceX, AST and carrier demand; FCC rule changes that unlock terrestrial use; down: Only four or five buyers; regulatory holds; Apple control rights at GSAT; base rate: Roughly one notable US spectrum-holder exit every 1-2 years; suggested P10/P50/P90 1 / 2 / 4 (2030)

### Gaps
Tool limits: the shared web-search budget ran out after 9 successful searches (the brief asked for at least 25). WebFetch could not reach sec.gov, docs.fcc.gov or lightreading.com (DNS blocked) or reuters.com (refused), so no primary page was read directly. 10-Q facts come from search snippets.

Not verified for Nov 2026:
- Market caps, EVs, 1-year and 2025-2026 returns for T, VZ, TMUS, ASTS, GSAT, IRDM, VSAT, ATEX, NN, AD, TDS, CMCSA, CHTR, AMT, CCI, SBAC, GOOGL, RCI, TU, BCE, and every ETF (NXTG, IYZ, VOX, XTL, UFO, ARKX, XOVR, DXYZ). Their record and scatter values are rough estimates from pre-2026 data. Their source_url fields are company or issuer landing pages that were not fetched.
- The returns_1y chart has only SpaceX since-IPO points. Q3 2026 carrier earnings were not checked. Carrier spectrum book values are FY2024 figures plus known deals.

EchoStar:
- ECHO share price and the ~$34B market value (weak, undated source).
- Residual licenses and their carrying values.
- Whether the $8.5B SpaceX cash was already received (the 10-Q snippet says the $17B is payable at the second closing).
- The difference between Seller Notes ($9.821B) and total debt ($9.67B).
- The tax and wind-down estimate.

SpaceX:
- Exact share count, so market cap is $1.88-1.95T depending on the basis.
- The price SpaceX is paying Grain (undisclosed).
- The $2.9B T-Mobile-to-Grain price (single weak source).
- FCC approval of 15,000 satellites and the Tristar AWS-3 purchase (weak sources).
- Details of the xAI combination.
- Alphabet's SpaceX stake percentage.

Deal and regulatory status not checked: Globalstar sale exploration, AST/Ligado L-band closing, Anterix strategic review, Array-AT&T/Verizon spectrum closings, Charter-Cox, Verizon-Frontier, the 2025 budget law's auction mandates and upper C-band timing, AWS-3 re-auction results, Canadian carriers' spectrum book values, and ETF holdings and SpaceX weights.

Auction benchmark $/MHz-pop figures are from training data and were not re-verified. No hard data was gathered on AI-device wireless demand.

## precedents

Scope and caveat. This domain reviews 26 spectrum bets from 1996 to 2026. The session's shared web-search budget ran out after 17 queries, and page fetches failed on every host tried. Source-checked through search results: Dish/EchoStar, NextWave, Clearwire, LightSquared/Ligado, Straight Path and SpaceX's 2026 purchases. Prior knowledge only, flagged as such: European 3G, C-band, the mmWave auctions, Globalstar, Iridium, Anterix, Metricom, India and Canada.

1. What the record shows

Results are widely spread and skewed toward losses. Of 26 cases:
- 6 clearly made money for the holder.
- 12 lost most of the capital (or, where a government was selling, most spectrum went unsold).
- 8 were mixed or are still pending.

Counting only pure-play holders (16 cases): 3 won, 8 lost, 5 mixed. For a holder who bought at the market price, the typical result after financing and carrying costs was between breaking even and a loss. The wins show large gains are possible, but they are the minority.

2. The most relevant case: Dish/EchoStar, 2008-2026

- **What went in.** By mid-2023 Dish had put more than $30B into licences, including more than $10B through designated entities (small bidders it financed). Its books carried the licences at $37.5B including capitalized interest.
- **What it sold:**
  - 3.45 GHz and 600 MHz to AT&T for about $23B. The deal closed on 2026-07-28, and $2.4B went into an FCC trust to pay Dish's obligations.
  - AWS-4 and H-block to SpaceX for about $17B: half cash, half SpaceX stock, plus about $2B of interest support.
  - Unpaired AWS-3 to SpaceX for about $2.6B in stock.
- **Overall return.** Headline proceeds of about $42.6B are about 1.4x the cash cost. Over a weighted holding of roughly ten years, that is about 3.5-4% a year. Against the $37.5B basis that includes capitalized interest, it is about 1.1x.
- **The best piece.** Dish bought the 2 GHz licences out of the TerreStar and DBSD bankruptcies for about $2.86B and added H-block for $1.67B. Together they sold for $17B: about 3.8x over 13-14 years, or about 10-11% a year. Two things made this happen: the FCC let the band be used for terrestrial service in 2012, and a satellite direct-to-device buyer eventually appeared.
- **The other pieces.** The 600 MHz and 3.45 GHz licences returned about 1.7x. The unpaired AWS-3 was reported to sell about 73% below book value (weak source).
- **The stock.** EchoStar shares rose about 430% from January 2025 to June 2026, the best return in the Fortune 500.
- **The circumstances.** Even so, the subsidiaries Dish DBS and Dish Wireless filed for Chapter 11 on 2026-06-30. The sales happened under FCC scrutiny of Dish's network build-out and with debt coming due. This was a forced seller meeting two strategic buyers, not a patient owner collecting a scarcity premium.

3. Other US precedents

- **NextWave.**
  - First round: it bid $4.74B for C-block PCS licences in 1996, paid $500M down, and went bankrupt in 1998. It kept the licences only by winning a court fight with the FCC. In 2004-05 it sold them for about $5.4B and paid creditors in full. That is about 1.1x the original bid after nine years.
  - Second round: its successor spent on WiMAX and WCS spectrum. AT&T bought it in 2012 for up to $600M, almost all of which went to creditors; shareholders got $25-50M.
- **Clearwire.**
  - Backers put in $3.2B in 2008. Intel took a $950M charge, and Google lost 94% on its $500M.
  - Sprint bought out the remaining shareholders in 2013 at $5 a share, roughly 0.25x the 2008 entry price.
  - The same 2.5 GHz spectrum later became T-Mobile's main 5G capacity band after the 2020 merger (prior knowledge). The large operator captured the value, not the people who held the spectrum first.
- **LightSquared/Ligado.**
  - Harbinger put about $3B into L-band spectrum. The FCC gave conditional approval for terrestrial use in 2011, then froze it in 2012 over interference with GPS.
  - LightSquared went bankrupt, and Harbinger's main fund lost 47% in 2011.
  - Its successor, Ligado, went bankrupt again in 2025. It leased up to 40 MHz to AST SpaceMobile for $550M in cash, mostly passed through to Inmarsat, plus at least $80M a year. That set against about $8.6B of debt (weak source).
- **Straight Path.**
  - This is the clean holder win. A Verizon-AT&T bidding war in 2017 produced a price of $3.1B ($184 a share, all stock). The FCC took 20% of proceeds, and penalty payments totalled about $614M.
  - The buyer then held millimetre-wave spectrum that the 2020 auctions priced below a cent per MHz-pop (prior knowledge).

4. Outside the US (prior knowledge)

- The UK's 2000 3G auction raised £22.5B and Germany's about €50.8B.
- Two German winners walked away from licences that cost about €8.4B each.
- Later auctions raised about a tenth of those sums for more spectrum: £2.3B in the UK in 2013 and €4.4B in Germany in 2010.
- India's 2024 auction sold only about 12% of the spectrum value it offered at reserve prices.
- Canada's 3800 MHz auction raised C$2.16B, against C$8.9B for 3500 MHz.

5. When spectrum bets paid and when they failed

Bets paid in two situations:
- **The regulator widened what the spectrum could be used for.** Examples: AWS-4; C-band, where satellite incumbents received about $9.7B in accelerated relocation payments; and the 2017 broadcast incentive auction.
- **Two or more strategic buyers had a deadline.** Examples: Straight Path in 2017 and EchoStar in 2025.

Bets failed for five reasons:
- **Interference with an entrenched incumbent:** LightSquared and GPS, and the WCS band.
- **Technology shifts:** WiMAX, Metricom, and the short range of millimetre-wave.
- **Too much supply:** the mmWave auctions, India in 2024, Canada's 3800 MHz auction, and the 2.5 GHz auction of leftover licences.
- **Paying the peak price:** European 3G and NextWave's bids.
- **Carrying costs:** Dish's roughly $7.5B of capitalized interest and Ligado's debt.

**Timing.** Wins took 4-14 years, and the biggest took more than 13. Losses usually became clear within 2-5 years.

**Who captured the value:**
- Treasuries, through auctions and the FCC's 20% of Straight Path's sale.
- Operators that bought from distressed holders: AT&T (NextWave), T-Mobile (2.5 GHz), Dish (TerreStar).
- Incumbents whose existing licences were upgraded by regulators.
- Nimble intermediaries. Grain reportedly bought T-Mobile's 800 MHz in August 2026 and agreed in October to sell it to SpaceX.

Pure equity holders made money mainly when a regulatory upgrade coincided with a buyer who had few alternatives.

6. What supports the thesis

- **More buyers.** SpaceX has agreed to buy about 65 MHz of mid-band from EchoStar (FCC-approved May 2026), the Tristar AWS-3 licences, and up to 14 MHz of 800 MHz from Grain. Musk called the 800 MHz deal the last piece needed for indoor coverage. Historically, a second motivated bidder was the best single predictor of a good exit.
- **Higher prices.** Prices in the 2025-26 private sales were about $1.0-1.4 per MHz-pop, above the 3.45 GHz auction's roughly $0.68 (auction figure from prior knowledge).
- **A template.** AWS-4 is the model for how satellite and terrestrial convergence can create value.

7. What undercuts it

- **Modest returns even at best.** The best recent case returned single digits a year across the whole programme, and it took FCC pressure to force a sale.
- **Satellite buyers have paid little for awkward spectrum:** Ligado's L-band and the unpaired AWS-3.
- **Others take much of the upside.** A large share went to regulators, operators and creditors.
- **New supply keeps arriving** as regulators repurpose bands.
- **Spectrum has not given carriers pricing power.** Carrier share prices after large spectrum purchases (Verizon after C-band, prior knowledge) suggest spectrum is a cost of doing business.

8. Implications for 2028-2035

Based on these cases, a new pure-play spectrum position bought at market has roughly a 25-35% chance of returning more than 1.5x by 2030. It has roughly a 25-30% chance of ending below 0.5x.

What drives outcomes is FCC rule changes, interference rulings and how many motivated bidders there are, more than total demand for data.

Passive exposure through carriers has historically captured little of the scarcity value. Listed pure plays are few, and each depends on one company's situation:
- EchoStar now trades largely as a proxy for SpaceX.
- Globalstar is tied to Apple.
- Anterix depends on a narrow pool of utility buyers.

### Key findings
- [P] AT&T closed its purchase of about 30 MHz of nationwide 3.45 GHz and about 20 MHz of nationwide 600 MHz spectrum from EchoStar.: ~$23B for ~50 MHz (2026-07-28; AT&T newsroom, https://about.att.com/story/2026/echostar-spectrum.html)
- [S] SpaceX agreed to buy EchoStar's AWS-4 and H-block licences for about $17B (up to $8.5B cash and $8.5B SpaceX stock), and to fund about $2B of EchoStar debt interest through November 2027.: ~$17B (+~$2B interest) (2025-09-08; Fierce Network, https://www.fierce-network.com/wireless/spacex-scoops-echostar-spectrum-17b)
- [S] EchoStar's share price rose about 430% from the start of 2025 to June 2026, including nearly 375% in 2025, the top shareholder return in the Fortune 500.: +430% (2026-06-04; Fortune, https://fortune.com/2026/06/04/echostar-stock-elon-musk-spacex-spectrum-bankruptcy-to-best-shareholder-return-fortune-500/)
- [P] Dish stated it had invested more than $30B in wireless spectrum licences, including more than $10B in noncontrolling investments in designated entities.: >$30B (2023-06-30; DISH Network 10-Q (SEC XBRL note), https://www.sec.gov/Archives/edgar/data/1001082/000155837023013759/R16.htm)
- [P] Dish paid total consideration of about $2.86B for the DBSD North America and TerreStar assets, whose 40 MHz of 2 GHz licences the FCC transferred in March 2012.: ~$2.86B (2012-03; DISH Network 10-K (SEC XBRL note), https://www.sec.gov/Archives/edgar/data/1001082/000155837019003904/R16.htm)
- [S] SpaceX agreed to buy Grain Management's nationwide 800 MHz portfolio of up to 14 MHz paired, to give Starlink Mobile indoor reach; terms were not disclosed and FCC approval is pending.: up to 14 MHz paired; price undisclosed (2026-10-08; TelecomTV, https://www.telecomtv.com/content/access-evolution/spectrum-deal-advances-starlink-s-major-mobile-carrier-plan-56431/amp/)
- [P] After winning its fight with the FCC, NextWave sold its PCS business to Verizon Wireless for about $3.0B, following earlier licence sales of over $2.3B (Cingular $1.4B, Verizon New York $930M, MetroPCS $43.5M), and paid creditors in full.: ~$5.4B total (2005-04; NextWave Wireless Form S-4 (SEC), https://www.sec.gov/Archives/edgar/data/0001374993/000114420406038702/v052905_s-4.htm)
- [S] Sprint raised its offer for the roughly 50% of Clearwire it did not own to $5 per share, valuing Clearwire at about $14B, after Dish bid $4.40; Dish then withdrew.: $5.00/share; ~$14B valuation (2013-06; Engadget, https://www.engadget.com/2013/06/20/sprint-clearwire-buyout-offer/)
- [S] Harbinger had put about $3B into LightSquared; its main hedge fund lost 47% in 2011 after marking down its LightSquared stake by 59%.: ~$3B invested; -47% fund return (2012-02-03; Bloomberg, https://www.bloomberg.com/news/articles/2012-02-03/falcone-s-harbinger-capital-lost-47-last-year-on-lightsquared-venture-bet)
- [P] AST SpaceMobile's deal for Ligado's L-band pays $550M in cash ($420M on 2025-10-31, $100M on 2026-03-31, $15M at closing), mostly passed to Inmarsat, plus at least $80M a year in usage payments for up to 40 MHz.: $550M + >=$80M/yr (2026-06-30; AST SpaceMobile 10-Q (SEC), https://www.sec.gov/Archives/edgar/data/0001780312/000119312526342550/asts-20260630.htm)
- [S] Verizon agreed to buy Straight Path and its 39 GHz and 28 GHz licences for about $3.1B ($184 per share, all stock), beating AT&T, whose April offer was reported at $1.25B to $1.6B.: $3.1B (2017-05; CBS News, https://www.cbsnews.com/news/verizon-to-buy-straight-path-for-3-1-billion)

### Forecast seeds
- Gross price in the next major US mid-band auction (upper C-band 3.98-4.2 GHz or similar) [$/MHz-pop] now No such auction yet; last mid-band auctions ~ $0.68-0.73 (3.45 GHz, 2022) and ~ $0.94 (C-band, 2021) (prior knowledge); history: AWS-3 2015 ~ $2.2 (paired, unverified); CBRS PAL 2020 ~ $0.22; C-band 2021 ~ $0.94; 3.45 GHz 2022 ~ $0.68-0.73; 2.5 GHz 2022 a few cents; 37/39/47 GHz 2020 ~ $0.007; up: SpaceX and other D2D players bidding; private-sale comparables of ~$1.0-1.4/MHz-pop in 2025-26; growth in AI device traffic; down: Altimeter/aviation power limits on upper C-band; carrier leverage after the EchoStar deals; a statutory supply pipeline; only three or four bidders; base rate: The three most recent US mid-band auctions averaged ~$0.6/MHz-pop; second tranches of similar bands usually price lower (Canada 3800 vs 3500 ~0.24x); suggested P10/P50/P90 0.15 / 0.45 / 1.0 (2028)
- Implied price of the largest US private sale of nationwide low/mid-band spectrum in the year [$/MHz-pop] now ~1.39 (AT&T-EchoStar, $23B for ~50 MHz); ~1.03 (SpaceX AWS-4/H-block, $17B for 50 MHz); history: Clearwire 2013 (~$14B whole company); Straight Path 2017 mmWave ~ $0.01-0.02 (estimate); EchoStar unpaired AWS-3 2025 ~ $0.5; up: More satellite buyers (SpaceX, AST, Apple-linked Globalstar); FCC tolerance of SpaceX holdings; scarce nationwide blocks; down: FCC auctions adding supply; spectrum caps on carriers; no forced sellers left after EchoStar; base rate: Two nationwide private sales above $1/MHz-pop in 2025 after essentially none from 2013 to 2024 (count not fully verified); suggested P10/P50/P90 0.4 / 1.0 / 1.8 (2030)
- Cumulative number of announced US spectrum-only transactions of $5B or more, 2027-2030 [count] now 2 announced in 2025 (AT&T-EchoStar $23B; SpaceX-EchoStar $17B); history: No spectrum-only private deal of $5B or more found for 2013-2024 (Straight Path $3.1B; Clearwire minority buyout ~$3.8B were the largest); count not fully verified; up: SpaceX's appetite for low-band indoor coverage; cable or new-entrant consolidation; sales of remaining EchoStar licences; down: Few large nationwide holdings left outside the big three carriers; FCC competition review; auctions as an alternative supply route; base rate: ~0.2 per year before 2025; 2 in 2025; suggested P10/P50/P90 0 / 1 / 4 (2030)
- Value of EchoStar's SpaceX equity stake received for spectrum [$B] now ~$11.1B at deal values (Fortune, June 2026); history: $8.5B stock (Sept 2025) + $2.6B stock (Nov 2025); reported IPO targets of $1.5-2.0T vs Morningstar ~ $780B; up: A SpaceX IPO at or above target; Starlink Mobile subscriber growth; down: Dilution from the xAI combination; IPO delay; a lower valuation such as Morningstar's; base rate: Stock consideration in spectrum deals has swung widely (Straight Path holders took Verizon stock; Clearwire backers lost 75% or more); suggested P10/P50/P90 7 / 16 / 32 (2028)
- Realized multiple (sale value / capital invested) for a pure-play spectrum position bought at market in 2026 [x] now Recent reference: Dish/EchoStar ~1.4x cash (~1.1x incl. capitalized interest) over ~10 years; history: TerreStar/DBSD ~3.8x; 600 MHz/3.45 GHz ~1.7x; NextWave ~1.1x of bid; Clearwire ~0.25x; Ligado ~0.06x; LightSquared ~0x; UK/German 3G ~0.1x proxy; up: An FCC upgrade of allowed use; two or more motivated bidders with deadlines; satellite-terrestrial convergence demand; down: Interference vetoes; new supply; carrying and financing costs; buyer discipline in a three-carrier market; base rate: Of 16 pure-play holder cases reviewed, ~3 won, ~8 lost, ~5 mixed; median below 1x after carry; suggested P10/P50/P90 0.1 / 0.8 / 2.5 (2035)
- Share of a basket of US non-carrier spectrum holders (EchoStar's remaining licences, Globalstar, Anterix, the Ligado/L-band rights, Grain's other holdings) sold to or merged with a strategic buyer [% of 5 holders] now 0 of 5 complete; Grain's 800 MHz sale to SpaceX pending FCC approval; history: Most historical pure-play holders ended in a sale to an operator, often after bankruptcy (NextWave twice, Clearwire, Straight Path, TerreStar, DBSD, EchoStar); up: SpaceX's repeated buying; AST/Apple-linked demand; FCC approvals arriving faster (SpaceX-EchoStar approved in ~8 months); down: Narrow buyer pool; regulatory caps; interference disputes (L-band); price disagreements; base rate: Roughly 8 of 12 historical pure-play holders were eventually sold, typically over 5-15 years; suggested P10/P50/P90 20 / 40 / 80 (2030)

### Gaps
Tool limits: the shared web-search budget ran out after 17 successful queries, short of the 25 requested. WebFetch failed with DNS errors on every host tried (lightreading.com, about.att.com, ir.echostar.com, fortune.com, fierce-network.com, docs.fcc.gov). Facts therefore rest on search-result summaries of the cited pages, not full-page reads.

Not verified in this session (stated from prior knowledge and flagged in the records):
- European 3G proceeds, write-downs and FX conversions
- US mmWave auction totals (101/102/103) and the status of returned or unused licences
- C-band accelerated relocation payments (~$9.7B) and the split between SES and Intelsat
- Verizon's C-band spend and its share price since 2021
- Globalstar's Apple terms and any 2025-26 sale process
- Iridium's 1999-2000 figures
- Anterix's 2014 cost basis and current status
- ICO/Pendrell history
- Metricom's capital raised and asset sale price
- India's 2024 auction figures
- Canada's 3500/3800 MHz auction totals
- 600 MHz incentive auction payouts
- Clearwire's ~$20 2008 entry price
- The T-Mobile 2.5 GHz outcome

Not confirmed at all:
- Straight Path's spin-off value, so its holder multiple is unquantified
- Harbinger's residual recovery
- The basis of the $9.8B AWS-3 book value
- The MHz amount in the unpaired AWS-3 sale
- Whether the SpaceX-EchoStar deal formally closed (FCC approved 2026-05-12; Satnews called it finalized in June 2026)
- The SpaceX IPO status and price
- EchoStar's current share price and long-run 2008-2026 total shareholder return
- The status of EchoStar's remaining licences (paired AWS-3, 700 MHz E-block, CBRS, others)
- The Grain-SpaceX price and the Grain-T-Mobile terms
- Any FCC re-auction of returned AWS-3 licences

Estimates: the Verizon/Straight Path mark-to-market (~0.4x) and the Ligado multiple are my own calculations with stated assumptions.

## global

Short answer: outside the US, licensed mobile spectrum is getting cheaper per unit, a lot of it now goes unsold or is handed out on non-cash terms, and the policy trend favours renewals and obligations over auctions designed to raise the most money. Operators' total spectrum bills are still rising, because they hold much more spectrum than a decade ago. The non-US evidence does not show licensed spectrum broadly gaining value. It shows two things: the US is a price outlier, and the scarcity that does exist sits in satellite-usable bands where governments decide who gets them.

1. Is spectrum getting more or less expensive?
Less expensive per unit, more expensive in total. GSMA's 2025 study (about 250 operators in roughly 100 countries) finds that operator revenue per MHz fell by about 60-67% between 2014 and 2023. Over the same period operators added about 80% more spectrum, so cumulative spectrum costs rose to about 7% of revenue, 63% above 2014. In Europe, revenue per MHz fell 54% and spectrum costs roughly tripled to about 8% of recurring revenue. GSMA lobbies for lower prices, so its claim that prices are too high is not neutral. Still, the auction data point the same way.

Analysys Mason averages 49 national 3.3-3.9 GHz auctions from 2018 to 2024 at €0.067/MHz-pop, normalised to a 20-year term. Italy's 2018 auction (about $0.42/MHz-pop for 3.7 GHz) was the high point. Later results were lower:
- Germany 2019: about $0.19
- UK 2018: about $0.15
- France 2020: about $0.15
- Spain: about $0.06
- Finland 2018: about $0.04

Canada gives the cleanest same-buyer comparison. Rogers says it paid C$3.38/MHz-pop for 3500 MHz in 2021 and C$0.32 for 3800 MHz in 2023, about 90% less. The 3800 MHz auction raised C$2.16bn, against C$8.91bn for 3500 MHz.

Capacity spectrum has become close to free. Ofcom's October 2025 mmWave award sold all 5.4 GHz offered for £39m. That is about US$0.00014/MHz-pop, which is my calculation. Each new block of capacity spectrum has sold for less than the one before.

2. The US is the outlier
FCC Auction 107 (C-band) cleared at about $0.94/MHz-pop on bids alone ($80.9bn). That is roughly 13 times the European 3.5 GHz average. Auction 110 (3.45 GHz) cleared at about $0.67.

The two are not strictly comparable. Licence terms and renewal expectations differ, the exchange rates come from different dates, and US clearing costs sit on top of the bids.

Even so, the gap points to US-specific conditions: three national bidders competing hard, higher revenue per user, and spectrum shortages at the time. Other markets show what usually happens when more mid-band supply arrives: prices fall. That does not predict rising US prices once the planned upper C-band and other pipeline bands come to auction.

3. Unsold spectrum
India is the starkest case:
- 2022: 51,236 MHz sold out of 72,098 MHz offered (29% unsold) for about US$19bn.
- June 2024: only about 141 MHz sold out of roughly 10,523 MHz (98.7% unsold by MHz, 88% by reserve value), raising about US$1.35bn.
- February 2026: TRAI recommended offering all 11,790 MHz available, worth about ₹2.1trn (about US$23bn) at reserve prices. Press reports put the reserve-price cuts at 20-40%, with a 35% cap on how much spectrum one operator can hold.

When a large market leaves most of its inventory unsold at reserve, reserve prices are above what operators will pay. That runs directly against a scarcity story. The UK mmWave award did sell out, but only at a nominal price. I could not verify unsold shares for auctions in Southeast Asia, Latin America or Africa in this pass.

4. Is policy moving away from auctions designed to maximise revenue?
Yes, in the cases I could verify:
- **Germany:** in March 2025 BNetzA extended 800/1800/2600 MHz rights by five years instead of auctioning them. It plans a competitive award around 2029, and the extension came with conditions, including continued 2600 MHz access for 1&1.
- **Brazil:** the 2021 auction (R$47.2bn, about US$8.5bn) turned at least 90% of the spectrum's economic value into investment obligations.
- **India:** the regulator is cutting reserve prices.
- **Europe-wide:** GSMA is pushing automatic low-cost renewals, which it says could save operators up to €30bn of the €104bn they would otherwise pay in 2025-2035.

Regulators are trading cash for coverage, competition and sovereignty. Fewer rights change hands at prices set in an open market, and cheaper renewals lower incumbents' future costs. That modestly helps operator cash flow, but it is not the same as spectrum gaining market value.

5. Satellite direct-to-device (D2D) and satellite-band (MSS) policy abroad
The EU 2 GHz MSS band (2x30 MHz) is the clearest live contest. The incumbents' 18-year authorisations expire in May 2027. On 27 May 2026 the Commission proposed a single EU-level selection with 20-year rights. Press reports say the band would be split into three equal blocks, two of them for European operators; I have not checked that against the regulation text.

This proposal supports both sides of the thesis. Satellite-usable spectrum is scarce and contested. But how much any one company can control is capped by politics: under the reported design, a non-European entrant such as SpaceX could get at most one third. That matches the Goldman banker's point about limits on who can hold how much. In the UK, Ofcom proposed letting the incumbents (Viasat and EchoStar) keep 2 GHz MSS access for 3-5 years.

At ITU level, WRC-27 agenda item 1.13 studies whether satellites can use bands now assigned to terrestrial mobile (roughly 694 MHz to 2.7 GHz) to connect directly to phones. The decision comes in late 2027; I did not re-verify the text in this pass. Outside the US, D2D so far mostly runs through partnerships in which operators lend their terrestrial spectrum to a satellite partner. That gives licensees a role, not a windfall. I could not verify Ofcom's D2D authorisation decision or what the 8 October 2026 Reuters article on SpaceX says.

6. Who captures the value
Spectrum costs are rising as a share of revenue while revenue per MHz falls. That means value has gone to treasuries and consumers, not operators. Industry studies widely put European telco returns at or below their cost of capital, but I could not re-verify a current ROIC figure in this pass.

Abroad, the banker's point holds: operators pay more in total and cannot raise prices. More spectrum and more competition have pushed returns down, not up.

What supports the thesis:
- Demand keeps rising. Holdings are up about 80% since 2014, and GSMA says each European operator needs at least 2 GHz of mid-band by 2030 and possibly 3 GHz by 2035.
- Total spectrum spending is still rising.
- Satellite-usable MSS bands are few, contested and treated as strategic.

What undercuts it:
- Prices per MHz-pop are falling across mid-band and mmWave.
- Large shares of offered spectrum go unsold.
- Regulators are shifting toward extensions, obligations and lower reserve prices.
- Politics caps who can control satellite bands.
- The next mid-band supply (6-8 GHz) is likely to be worth less per MHz. Analysys Mason says operators may value it only in high-traffic areas, and existing users of the band will create exclusion zones.

Probabilistic view (my estimates):
- **2028:** about 80% that new European mid-band auctions average at or below €0.10/MHz-pop. About 70% that India's next auction leaves most of the MHz offered unsold.
- **2030:** about 60% that most major European licence expiries due between 2025 and 2032 are handled by renewal or extension rather than open auction. About 65% that at least one of the three EU 2 GHz MSS blocks goes to a European-controlled operator. About 35% that a non-European constellation operator holds an EU-level block.
- **2035:** the global spectrum cost share settles at 5-9% of revenue. Prices per MHz-pop keep falling in real terms in most markets.

The scenario where spectrum broadly becomes far more valuable outside the US is a low-probability tail, about 10-15%. It would need sustained traffic growth that outpaces new supply and a return to auctions designed to raise money. The more likely place for a value premium is narrow: satellite-capable bands and US spectrum.

### Key findings
- [S] GSMA's 2025 Global Spectrum Pricing study found cumulative spectrum costs equal about 7% of mobile operator revenues, 63% higher than in 2014.: 7% of revenue (+63% vs 2014) (2023 data, published May 2025; GSMA press release, Global Spectrum Pricing, https://www.gsma.com/newsroom/press-release/gsma-calls-for-governments-to-prioritise-affordable-spectrum-costs-to-support-global-digital-growth/)
- [S] GSMA reports that average operator revenue per MHz of spectrum fell between 2014 and 2023, and says the fall has not been fully reflected in spectrum prices.: -60% (press release) to -67% (full report) (2014-2023; GSMA, Global Spectrum Pricing (May 2025), https://www.gsma.com/connectivity-for-good/spectrum/wp-content/uploads/2025/05/Global-Spectrum-Pricing.pdf)
- [S] Analysys Mason calculates that 49 national 3.3-3.9 GHz auctions held in 2018-2024 averaged EUR0.067/MHz/pop, normalised to a 20-year licence term.: EUR0.067/MHz/pop (~US$0.07) (June 2025; Analysys Mason, New thinking on spectrum valuation for upper mid-band, https://www.analysysmason.com/consulting/articles/spectrum-valuation-uppermid/)
- [S] FCC Auction 107 (C-band, 3.7-3.98 GHz) drew $80.92bn in gross bids, a nationwide average of about $0.94/MHz-pop and the highest of any mid-band auction worldwide.: $80.92bn; ~$0.942/MHz-pop (Jan-Feb 2021; Light Reading (FCC figures; BitPath average), https://www.lightreading.com/5g/c-band-bidding-wraps-at-$8091b-/d/d-id/766706)
- [P] Ofcom's October 2025 mmWave award, the largest it has run, sold all 5.4 GHz offered at 26 GHz and 40 GHz to EE, O2 and VodafoneThree for GBP13m each, GBP39m in total.: GBP39m for 5,400 MHz (~US$0.00014/MHz-pop, derived) (24 Oct 2025; Ofcom, spectrum auction final results, https://www.ofcom.org.uk/spectrum/spectrum-awards/ofcom-spectrum-auction-final-results-announced)
- [P] On 24 March 2025 Germany's BNetzA extended the 800 MHz, 1800 MHz and 2600 MHz rights that were due to expire at end-2025 by five years instead of auctioning them, and plans a competitive award around 2029 together with bands expiring in 2033.: 5-year interim extension (24 Mar 2025; Bundesnetzagentur press release, https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/EN/2025/20250324_frequenzen.html)
- [S] India's June 2024 auction sold only about 141 MHz of the roughly 10,523 MHz offered (1.34%), raising INR11,340 crore, against a reserve value of INR96,318 crore for everything offered.: ~US$1.35bn; 98.7% unsold by MHz; 88% unsold by reserve value (June 2024; Developing Telecoms, https://www.developingtelecoms.com/telecom-business/telecom-regulation/16916-india-s-second-5g-spectrum-auction-fizzles-at-us-1-35b.html)
- [W] Operators reported 3800 MHz prices of C$0.32/MHz-pop (Rogers, C$475m for an average 40.5 MHz) and C$0.24/MHz-pop (Telus), about 90% below Rogers' own 2021 3500 MHz price.: C$0.24-0.32/MHz-pop (Nov 2023; TelecomTalk (citing company releases), https://telecomtalk.info/canada-concludes-3800mhz-spectrum-auction-awarding-4099licences/901670/)
- [P] Anatel's 2021 design turned at least 90% of the spectrum's economic value into investment obligations rather than cash, with 20-year licences.: >=90% of value as obligations (2021 (presented 2023); Anatel presentation at ITU, https://www.itu.int/en/ITU-D/Regulatory-Market/Documents/Events2023/IPEC-23/Presentations/Session3_Edgar-Souza_Anatel.pdf)
- [S] On 27 May 2026 the European Commission proposed a regulation for a single EU-level selection for the 2 GHz MSS band; reports say it splits the band into three equal blocks, two of them for European players, and Council documents reference 20-year rights.: 3 blocks; 2/3 to European players (reported); 20-year term (27 May 2026; Greenberg Traurig, https://www.gtlaw.com/ar/insights/2026/6/eu-commission-proposes-new-authorization-regime-for-mobile-satellite-services)
- [S] On the reported figures, US C-band bids cleared at about 13 times the 2018-2024 European 3.3-3.9 GHz average per MHz-pop. Licence terms differ, so the comparison is not exact.: ~13x ($0.942 vs ~$0.072) (2021 vs 2018-2024; Whitesail calculation from Light Reading and Analysys Mason figures, https://www.analysysmason.com/consulting/articles/spectrum-valuation-uppermid/)

### Forecast seeds
- Average price in new European mid-band (3.3-4.2 GHz and 6 GHz) awards, 20-year normalised [EUR/MHz-pop] now 0.067 (2018-2024 average of 49 auctions); history: Italy 2018 ~US$0.42 peak; Germany 2019 ~0.19; UK 2018 and France 2020 ~0.15; Spain ~0.06; Finland ~0.04; up: Traffic growth, GSMA-stated need of 2-3 GHz mid-band per operator, scarce contiguous blocks, more consolidation leaving fewer but stronger bidders; down: Revenue per MHz down 54% in Europe, upper mid-band valued only in hotspots, exclusion zones, renewals instead of auctions, weak telco returns; base rate: Every major mid-band tranche outside the US since 2018 has cleared below Italy 2018; Canada fell about 90% from 2021 to 2023; suggested P10/P50/P90 0.015 / 0.04 / 0.09 (2030)
- Global cumulative spectrum cost as a share of mobile operator revenue (GSMA basis) [% of revenue] now 7% (2023); history: ~4.3% in 2014 (derived), 7% in 2023; Europe ~8% in 2025; up: Continued purchases of new bands, renewals at legacy prices, flat revenue; down: Low-cost renewals and extensions, reserve-price cuts (India), obligation-based awards (Brazil), revenue growth from fixed-wireless and IoT; base rate: Rose about 0.3 percentage points a year over 2014-2023; suggested P10/P50/P90 5.5 / 7.5 / 9.5 (2030)
- Share of offered MHz left unsold in India's next multi-band auction [% of offered MHz] now 98.7% (2024); history: 28.9% unsold in 2022; 98.7% in 2024; TRAI proposes offering all 11,790 MHz with lower reserve prices; up: Only three private bidders, Vodafone Idea's weak balance sheet, large 600 MHz and 6 GHz inventory, operators already holding enough 5G spectrum; down: Reserve cuts of 20-40%, renewal of expiring licences forcing purchases, satellite operators possibly bidding; base rate: India has left a majority of offered MHz unsold in most recent rounds; 2022 was the exception; suggested P10/P50/P90 45 / 75 / 92 (2027)
- Share of major EU/UK mobile licence expiries (2025-2035) handled by renewal or extension rather than open competitive auction [% of expiring licences by MHz] now Germany 2025 extension is the main verified example; history: Germany extended 800/1800/2600 MHz in 2025; GSMA is lobbying for automatic low-cost renewals; EU-level MSS uses a policy-based selection; up: Political focus on investment and coverage, the Digital Networks Act agenda (not verified here), weak operator returns; down: Treasury revenue needs, new-entrant complaints, competition law, the planned German competitive award around 2029; base rate: Historically most EU 2G/3G licence expiries were re-auctioned; the trend since 2023 favours extensions; suggested P10/P50/P90 30 / 55 / 80 (2032)
- Number of the three EU 2 GHz MSS blocks awarded to a non-European-controlled operator (e.g., SpaceX/Starlink, AST) [blocks (0-3)] now 0 (incumbents' rights run to May 2027); history: Two 18-year EU authorisations since 2009; May 2026 Commission proposal reportedly reserves two of three blocks for European players; up: Starlink's D2D scale and D2D demand from member states, a weak field of European bidders; down: Sovereignty preference, IRIS2 politics, legislative changes that tighten eligibility; base rate: EU selections in 2009 went to two operators linked to Europe (Inmarsat and Solaris); suggested P10/P50/P90 0 / 1 / 1 (2028)
- US mid-band price premium over the European 3.5 GHz average (price of the next large US mid-band auction divided by the Europe average) [multiple (x)] now ~13x (C-band 2021); history: C-band $0.94, 3.45 GHz $0.67 vs Europe ~$0.07; up: US revenue per user, three-way national bidding, SpaceX or cable as new bidders; down: Large statutory US pipeline adding supply, operator balance sheets, falling revenue per MHz, satellite substitution in rural areas; base rate: The US premium narrowed from Auction 107 to Auction 110 within one year; suggested P10/P50/P90 3 / 6 / 12 (2028)
- Proceeds of India's next multi-band auction [US$bn] now 1.35 (2024); history: ~US$19bn in 2022; US$1.35bn in 2024; ~US$23bn reserve value for all 11,790 MHz proposed; up: Renewal-driven purchases, 600 MHz demand, lower reserve prices clearing more volume; down: Operator leverage, three-player market, already ample 5G holdings; base rate: Two most recent auctions: one large (2022), one very small (2024); suggested P10/P50/P90 1 / 4 / 12 (2027)

### Gaps
The research ran under tool limits. The shared web-search budget ran out after 16 searches that returned results (the brief asked for at least 25). WebFetch could not reach any page tried (gsma.com, ofcom.org.uk, bundesnetzagentur.de, digital-strategy.ec.europa.eu, wikipedia.org, reuters.com): each host either failed to resolve (outside the session's allowed network domains) or was unavailable to the fetch tool, so primary documents were not read in full. Most figures come from search snippets and headlines.

Not confirmed in this pass:
(1) The content of the Reuters 8 Oct 2026 article on SpaceX acquiring spectrum.
(2) Ofcom's direct-to-device authorisation decision and any UK operator D2D launches.
(3) The ITU WRC-27 agenda item 1.13 text and the status of studies. It is described from background knowledge only.
(4) Japan and China administrative assignments, Australia (ACMA renewals and auctions), and Saudi/Gulf auctions. No verified data, so they are excluded from the records.
(5) Current European telco ROIC versus WACC. Not verified; it is referred to only as widely reported.
(6) The EU Digital Networks Act's licence-duration and renewal provisions.
(7) GSMA's own $/MHz-pop series by band and year. The GSMA 2025 reports were not readable, and the GSMA Intelligence note on falling mid-band prices is paywalled.
(8) France 2020 total proceeds, the UK 2021 band split, Germany 2019 MHz totals, and Italy's 3.7 GHz portion. Only per-MHz-pop estimates or headlines were captured.
(9) Auction-wide average $/MHz-pop for Canada 3500 and 3800 MHz. Operator-reported figures are used instead, and the cited analyst average of C$1.83 could not be attributed to a source.
(10) The cash portion of Brazil's 2021 proceeds.
(11) The Germany 2025 extension fee, reported at under EUR800m by one secondary source only, and its coverage obligations.
(12) Unsold shares for US auctions and for recent auctions in Southeast Asia, Latin America, Africa and the Middle East.
(13) The DoT decision and date for India's next auction, and the size of the reserve-price cut (reports range from 20% to 40%).
(14) Details of the EU 2 GHz MSS proposal: the two-thirds European allocation comes from a French press source, and the 20-year term from a Council document excerpt.
(15) The GSA 700 MHz average of $0.269/MHz-pop, which comes from an ambiguous snippet.

Currency conversions use approximate rates at the time of each auction. Comparisons of $/MHz-pop across countries are not like-for-like, because licence terms, renewal expectations, obligations and clearing costs differ.
