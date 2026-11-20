"""Verdict, method and caveats for the wireless-spectrum report.

The text quotes the final forecasts and scenarios (forecasts.json via build_spectrum.py), so the numbers in the
verdict always match the Projections tab. Facts quoted without a forecast come from the checked findings.
Revised after the independent review: like-for-like auction prices, pending deals described as agreed, EchoStar's
SpaceX shares shown at deal and market value, a fairer precedent base rate, and the strongest arguments for the thesis.
"""


def plan(fc, pr, sc, f, p, rng, money):
    ucb, mid, traffic, ai, newmhz, spxmhz = (f(fc, k) for k in ("q_ucb_price", "q_midband_2030", "q_traffic_2030", "q_ai_share", "q_new_mhz_2030", "q_spacex_mhz"))
    rev, rpgb, proceeds = f(fc, "q_service_rev"), f(fc, "q_rev_per_gb"), f(fc, "q_ucb_proceeds")
    above, retail, sale, beat, reaccel, crunch, techbuy, spxucb = (p(pr, k).get("probability") for k in (
        "b_ucb_above", "b_spacex_retail", "b_pureplay_sale", "b_carriers_beat", "b_reaccel", "b_crunch", "b_tech_buys_carrier", "b_spacex_ucb"))
    growth = ((traffic.get("p50") or 0) / 159.3) ** (1 / 5) - 1 if traffic.get("p50") else 0
    S = {s["name"]: s["probability"] for s in sc}
    scar, fourth = S.get("Scarcity premium", 0), S.get("SpaceX fourth force", 0)
    scen = "; ".join("%s %s%%" % (s["name"], s["probability"]) for s in sc)
    p50 = money(ucb.get("p50"), "usd2")
    spx_more = round((spxmhz.get("p50") or 79) - 79)

    rows = [dict(id="headline", kind="headline", order=0, heading="Headline", body=(
        "The thesis is half right. Low-band and satellite-capable spectrum is getting scarcer and SpaceX is paying up, "
        "but we put only %s%% on licensed spectrum as a whole re-rating by 2030, and no listed security gives clean exposure." % scar))]

    SHORT = [
        ("Right about",
         "• Low-band is scarce. SpaceX agreed to pay 2.2x what Grain paid for the same 800 MHz licences two months earlier.\n"
         "• SpaceX is a deep-pocketed new buyer, with about $28B of deals agreed.\n"
         "• Satellites can't serve cities, so convergence needs ground spectrum."),
        ("Wrong about",
         "• Demand growth is slowing. US traffic still rises, but by 20%% in 2025 against 32%% in 2024, and AI is 0.06%% of traffic.\n"
         "• Supply is rising. We expect about %s of new spectrum auctioned by 2030.\n"
         "• Owners don't capture it. Carrier stocks fell 9-13%% on SpaceX's 800 MHz deal.\n"
         "• Past pure plays mostly failed. Of 16, 8 lost money and 3 clearly won." % money(newmhz.get("p50"), "mhz")),
        ("Our odds",
         "• Upper C-band (2027): %s per MHz-pop, below 2021's $0.87.\n"
         "• Scarcity premium by 2030: %s%%. SpaceX as a fourth force: %s%%.\n"
         "• Carriers beat the S&P 500 through 2030: %s%%." % (p50, scar, fourth, beat)),
        ("Ways in",
         "• No clean passive vehicle exists.\n"
         "• The purest are small holders (Anterix, NextNav, Array), which pay off only through a sale.\n"
         "• Convergence gains go to sellers and SpaceX more than to carriers."),
    ]
    for i, (h, b) in enumerate(SHORT):
        rows.append(dict(id="verdict%d" % i, kind="verdict", order=i + 1, heading=h, body=b))

    V = [
        ("Where the thesis is right",
         "Some spectrum is scarce, AI strains the uplink, and convergence has brought a new buyer:\n"
         "• Low-band spectrum (under 1 GHz) carries signals indoors, and nothing new is coming. SpaceX agreed to pay a reported $1.73 per MHz-pop for 800 MHz licences that changed hands at about $0.78 two months earlier.\n"
         "• SpaceX accounts for about $28B, roughly half, of 2025-26 US private spectrum deal value, and Amazon is paying about $11.6B for Globalstar. SpaceX's IPO raised $75B ($85.7B with the over-allotment) and it pays partly in its own stock, so it could fund the whole upper C-band auction at our %s central estimate. Its appetite, not its balance sheet, limits further buying.\n"
         "• Satellites cannot carry city traffic. By our order-of-magnitude estimate, next-generation satellite-to-phone service reaches about 1-6 Mbps per square kilometre, roughly a thousandth of a dense urban network's 1,500-9,000. That is why SpaceX is buying ground-grade spectrum and looking for towers, the convergence the thesis describes.\n"
         "• AI strains the uplink first. Generative AI traffic was 26%% uplink against about 10%% for all traffic, phones transmit with limited power, and networks are built for roughly 10:1 download-to-upload. Ericsson models AI lifting 2031 uplink to 3-5x the 2025 level, which favours low- and mid-band coverage spectrum. Tripling uplink adds only about 20%% to total traffic, so the pressure falls on particular bands and busy cells more than on total volume.\n"
         "• Sellers facing two motivated buyers captured large gains. EchoStar's shares rose about 430%% from a near-distressed level in January 2025 to June 2026 as AT&T and SpaceX split its licences, though over 2008-2026 Dish's licence spending returned about 1.4x cash cost at deal values. Small paired lots also still clear high at auction: leftover AWS-3 licences fetched $2.53 per MHz-pop in June 2026, almost all from Verizon." % money(proceeds.get("p50"), "usd_b")),
        ("Where it breaks",
         "The broader reading, that licensed spectrum as a whole becomes significantly more valuable by 2030, runs into seven problems:\n"
         "• Demand is slowing. US traffic grew 20%% in 2025 after 32%% in 2024. Generative AI apps were 0.06%% of traffic on the one operator network Ericsson measured in April 2025, and Wi-Fi carries 82-89%% of US smartphone data. The devices the thesis names add little licensed traffic so far. Waymo's roughly 4,000 robotaxis use about 0.02%% of US mobile traffic, and glasses and most robots ride a phone or Wi-Fi.\n"
         "• Capacity has substitutes. Wi-Fi carries most phone data, and denser cells and 5G-Advanced radios (20-40%% more bits per hertz) add capacity without new licences. Networks also have room today. Capital spending has been flat near $30B since 2023 while speeds rose 74%% in two years, though much of that gain came from C-band and 3.45 GHz spectrum bought in 2021-22.\n"
         "• Supply is rising by law. The 2025 budget law created an 800 MHz pipeline, and we expect about %s of new spectrum auctioned by 2030.\n"
         "• SpaceX may be nearly done buying. Musk called the Grain 800 MHz licences the last critical piece for complete US phone coverage. We expect SpaceX to own about %s at end-2030, about %d MHz more than it has already agreed to buy.\n"
         "• Owners rarely capture it. AT&T, Verizon and T-Mobile carry about $411B of licences at cost (T-Mobile's $100B is from its filing; AT&T's $149B and Verizon's $161B could not be independently confirmed), 41-50%% of their enterprise value. Their shares fell 9-13%% the day after SpaceX agreed to buy Grain's 800 MHz licences. The pricing-power objection holds: carriers see stock value from spectrum only if they can raise prices, and competition, now including SpaceX, works against that.\n"
         "• Buyers are few and regulated. The three carriers took 96%% of 2021 C-band dollars and about 99%% of the 2026 AWS-3 re-auction. The last outside bidder of size, Dish (about a third of 3.45 GHz in 2022), has sold out, and FCC screens and conditions limit who can hold how much.\n"
         "• History is unkind to pure plays. Of 16 companies whose main asset was spectrum, 3 clearly won, 8 lost and 5 were mixed. The sample is small and hand-picked." % (money(newmhz.get("p50"), "mhz"), money(spxmhz.get("p50"), "mhz"), spx_more)),
        ("What our forecasts say",
         "Central estimates with 80%% ranges, from five forecasting lenses that worked from the same research:\n"
         "• Upper C-band auction price (2027): %s, against 2021's $0.87 on the same basis ($0.94 as originally reported). Chance gross bids exceed $0.94: %s%%; chance they beat 2021's $0.87 like-for-like: about 37%%. With about $0.30 of clearing and altimeter costs on top, the all-in price is roughly level with 2021's (about $1.01 including its clearing payments).\n"
         "• Low- and mid-band deal price in 2029-30 (FCC auctions plus private sales above $1B): %s, against a median near $1.20 on the same basis in 2025-26. Most of the fall comes from new FCC auctions (2.7 GHz and others, at about $0.3-0.8) entering the mix; we expect private low-band and paired sales to hold at $1.2-2.5.\n"
         "• US mobile traffic in 2030: %s, about %.1f%% a year.\n"
         "• AI share of mobile traffic in 2030, on a narrow definition like Ericsson's (assistants, agents and AI devices, not AI-recommended video): %s. Broad-definition forecasts run higher, such as GSMA's 5-20%%.\n"
         "• Spectrum SpaceX owns at end-2030: %s. Chance SpaceX sells its own US phone plan by 2028: %s%%.\n"
         "• US wireless service revenue in 2030: %s; revenue per GB %s.\n"
         "• Chance an equal-weight basket of AT&T, Verizon and T-Mobile beats the S&P 500 through 2030: %s%%.\n"
         "Scenarios for 2030: %s. The thesis holds in about %s%% of them: %s%% where existing holders gain (Scarcity premium) and %s%% where SpaceX and sellers gain (SpaceX fourth force). The demand case is stronger for 2030-2035, mainly through AI uplink." % (
             rng(ucb), above, rng(mid), rng(traffic), growth * 100, rng(ai), rng(spxmhz), retail, rng(rev), rng(rpgb), beat, scen, scar + fourth, scar, fourth)),
        ("Ways to get exposure",
         "No listed security gives clean, passive exposure to spectrum values. The options trade purity against liquidity:\n"
         "• US carriers (T, VZ, TMUS) own most of the spectrum. Their licences sit on the books at cost, equal to 41-50%% of enterprise value, and higher spectrum prices reach earnings only if they sell. Their returns follow pricing and competition.\n"
         "• Small spectrum holders (Anterix, NextNav, Array) are the purest listed exposure; EchoStar's remaining licences come only through ECHO stock. These holdings pay off through a sale to a handful of buyers, so the exposure is event-driven and illiquid. We put %s%% on at least one of the four selling by 2028, but most of that is EchoStar's promise to the FCC to sell its remaining licences by September 2028. For Anterix, NextNav or Array the chance is roughly one in three, and a sale does not guarantee a premium.\n"
         "• EchoStar is now mostly a claim on SpaceX shares (about $36B at the 13 November close) and cash from its spectrum sales. At about $28.6B it trades well below that look-through value, before taxes and wind-down costs.\n"
         "• SpaceX (SPCX) is the most active buyer, but spectrum is about 1.5%% of its value.\n"
         "• Globalstar and Iridium are being acquired at fixed prices, which caps their upside. AST SpaceMobile is a high-risk bet on execution.\n"
         "• Tower companies hold no spectrum but gain if scarcity forces more sites or SpaceX leases them.\n"
         "• No fund isolates spectrum. IYZ is led by the large carriers; XTL gives equal weight to carriers, equipment makers and small spectrum and satellite names.\n"
         "If convergence plays out, the evidence points to gains for sellers and for SpaceX as buyer, while incumbent carriers lose ground. Those gains come through deals, so the exposure is event-driven." % sale),
        ("What would change our view",
         "Signposts that would move us toward the thesis, with our current odds:\n"
         "• The upper C-band auction's gross bids exceed $0.94 per MHz-pop (%s%%), or SpaceX wins meaningful blocks in it, not just rural licences (part of our %s%% for any win).\n"
         "• US traffic growth returns above 25%% in any year to 2030 (%s%%), or carriers raise real prices while rationing fixed wireless for capacity. A rise in revenue per GB (%s%%) would point the same way, unless it comes from a change in CTIA's method.\n"
         "• A technology company agrees to buy a US carrier or a cable company's mobile business by 2030 (%s%%).\n"
         "• The FCC pipeline slips beyond our central case. A 2.7 GHz auction that misses 2028 would tighten mid-band supply before 2030; a stalled 7 GHz band is already our central case.\n"
         "The dated events are on the Projections tab." % (above, spxucb, reaccel, crunch, techbuy)),
    ]
    for i, (h, b) in enumerate(V):
        rows.append(dict(id="detail%d" % i, kind="verdict_detail", order=i + 1, heading=h, body=b))

    M = [
        ("Research", "Nine researchers each covered one part of the market: demand, substitutes for spectrum, supply and rules, prices and deals, satellites, carrier economics, listed exposure, past spectrum bets and markets outside the US. They gathered 379 findings, each with a source link and a tag: P for regulators, filings and official statistics, S for reputable press and analysts, W for directional sources. Our environment could not open some primary sites (SEC, FCC, Reuters) directly, so those facts rest on search extracts of the documents."),
        ("Independent check", "Separate fact-checkers re-searched the 102 key claims with differently worded searches. 92 were confirmed, 5 were corrected (the corrections are applied), 5 could not be confirmed independently, and none was refuted. Each finding's check result is in the Appendix. A second review read the finished report for accuracy, reasoning and clarity, and its corrections are applied."),
        ("Forecasts", "We wrote 32 questions with resolution criteria: 18 quantities and 14 yes-or-no events. Five forecasting lenses answered every question separately: a reference-class lens, a bottom-up model, an advocate for the thesis, a skeptic, and a policy and market-structure lens. We take the median central estimate, the average 10th and 90th percentiles and, for yes-or-no questions, the geometric mean of the odds. A chief forecaster then checked the numbers for consistency and wrote the four scenarios."),
        ("How to read the ranges", "Each range is an 80% interval, so we expect the outcome to fall outside it about one time in five. The ticks on each forecast show where each lens put its central estimate. The lenses agreed closely, partly because they worked from the same research, so treat the ranges as careful judgments; no statistical model produced them. On the variables that matter most for the thesis, the panel sat below the research team's own medians: AI share of traffic 1.5% against 4%, satellite-to-phone revenue $4.8B against $6B, SpaceX direct US lines 1M against 3M, and 6G by 2030 49% against 60%. The panel leaned on slowing measured data and vendors' record of overshooting. At 3M SpaceX lines, the SpaceX fourth force scenario would be close to even odds."),
    ]
    for i, (h, b) in enumerate(M):
        rows.append(dict(id="method%d" % i, kind="method", order=i + 1, heading=h, body=b))

    C = [
        "This report is an independent market reference prepared for Fulton Asset Management. It is not investment advice or a recommendation to buy or sell any security. ",
        "Market data (market capitalisations and returns) come from public sources dated October-November 2026 and should be refreshed before any decision. ",
        "Holdings by company, the share of value that is spectrum, capacity per square kilometre and several precedent returns are Whitesail estimates and are labelled as such. ",
        "Deal prices per MHz-pop depend on the population and bandwidth assumed; we use about 335 million people unless a source states otherwise, so 2021's C-band price is $0.87 on our basis and $0.94 as originally reported. The ~$8B SpaceX-Grain price is a press report, not a disclosed figure. ",
        "Risks to these forecasts. Interest rates: spectrum is a long-lived asset, and higher rates cut auction budgets and carrier multiples, while lower rates do the reverse. Policy: a change in FCC leadership after the 2028 election, political friction around SpaceX approvals, Defense Department resistance or litigation could slow the pipeline, which would tighten supply, or change ownership limits. Technology: an on-time 6G standard raises demand for 7 GHz but also adds supply, while Wi-Fi 7 on 6 GHz and on-device AI keep moving traffic off licensed networks. Each could shift the scenario weights by several points. ",
        "Forecasts are judgments made on 20 November 2026 and will be wrong in places; the signposts say what would change them.",
    ]
    for i, b in enumerate(C):
        rows.append(dict(id="caveat%d" % i, kind="caveat", order=i + 1, heading="", body=b))
    return rows
