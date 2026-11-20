"""Verdict, method and caveats for the wireless-spectrum report.

The text quotes the final forecasts (forecasts.json via build_spectrum.py), so the numbers in the verdict always match
the Projections tab. Facts quoted without a forecast come from the verified findings.
"""


def plan(fc, pr, sc, f, p, rng, money):
    ucb, mid, traffic, ai, newmhz, spxmhz = (f(fc, k) for k in ("q_ucb_price", "q_midband_2030", "q_traffic_2030", "q_ai_share", "q_new_mhz_2030", "q_spacex_mhz"))
    rev, rpgb, ev = f(fc, "q_service_rev"), f(fc, "q_rev_per_gb"), f(fc, "q_ev_ebitda")
    above, retail, sale, beat, reaccel, crunch, techbuy, spxucb = (p(pr, k).get("probability") for k in (
        "b_ucb_above", "b_spacex_retail", "b_pureplay_sale", "b_carriers_beat", "b_reaccel", "b_crunch", "b_tech_buys_carrier", "b_spacex_ucb"))
    growth = ((traffic.get("p50") or 0) / 159.3) ** (1 / 5) - 1 if traffic.get("p50") else None
    scen = "; ".join("%s %s%%" % (s["name"], s["probability"]) for s in sc)

    rows = [dict(id="headline", kind="headline", order=0, heading="Headline", body=(
        "The thesis is half right. Low-band and satellite-capable spectrum is scarce, and SpaceX has become a deep-pocketed buyer that pushed private prices up in 2025-26. "
        "But licensed spectrum as a whole is unlikely to become significantly more valuable by 2030: traffic growth is slowing, AI is still a sliver of traffic, and a statutory pipeline adds about a third more mid-band. "
        "We expect the 2027 upper C-band auction to clear near %s per MHz-pop, below 2021's $0.94, and we see no clean passive way to own the theme." % money(ucb.get("p50"), "usd2")))]

    V = [
        ("Where the thesis is right",
         "Some spectrum is scarce, and convergence has brought a new buyer:\n"
         "• Low-band spectrum (under 1 GHz) carries signals indoors and nothing new is coming. SpaceX agreed to pay a reported $1.73 per MHz-pop for 800 MHz licences that changed hands at about $0.78 two months earlier.\n"
         "• SpaceX accounts for about $28B, roughly half, of 2025-26 US private spectrum deal value, and Amazon is paying about $11.6B for Globalstar.\n"
         "• Satellites cannot carry city traffic: a next-generation satellite targets about a thousandth of the capacity per square kilometre of an urban network. That is why SpaceX is buying terrestrial-grade spectrum and looking for towers, the convergence Jason described.\n"
         "• Sellers facing two motivated buyers captured large gains. EchoStar's shares rose about 430% from January 2025 to June 2026, and leftover AWS-3 licences fetched $2.53 per MHz-pop in June 2026."),
        ("Where it breaks",
         "The broad claim that licensed rights become significantly more valuable runs into six problems:\n"
         "• Demand is slowing. US traffic grew 20%% in 2025 after 32%% in 2024. Generative AI was 0.06%% of mobile traffic in Ericsson's measurement, and Wi-Fi carries 82-89%% of US smartphone data.\n"
         "• Capacity has substitutes. More cells, better radios and Wi-Fi add capacity; capital spending has been flat near $30B since 2023 while speeds rose 74%% in two years.\n"
         "• Supply is rising by law. The 2025 budget law created an 800 MHz pipeline; we expect about %s of new spectrum auctioned by 2030.\n"
         "• Owners do not capture it. AT&T, Verizon and T-Mobile carry about $411B of licences at cost, 41-50%% of their enterprise value, and their shares fell 9-13%% the day SpaceX bought the 800 MHz licences. Corey's point holds: without pricing power, more valuable spectrum in a competitor's hands hurts incumbents.\n"
         "• Buyers are few and regulated. The three carriers took 96-99%% of recent auction dollars, and FCC screens and conditions limit who can hold how much.\n"
         "• History is unkind. Of 26 past spectrum bets we reviewed, 6 clearly paid off and 12 lost most of their capital." % money(newmhz.get("p50"), "mhz")),
        ("What our forecasts say",
         "Central estimates with 80%% ranges, from five independent forecasting lenses:\n"
         "• Upper C-band auction price (2027): %s. Chance it clears above 2021's $0.94: %s%%.\n"
         "• Median mid-band price in 2029-30 deals: %s, against $1.0-1.4 in the 2025-26 private sales.\n"
         "• US mobile traffic in 2030: %s, about %s%% a year.\n"
         "• AI share of mobile traffic in 2030: %s.\n"
         "• Spectrum SpaceX owns at end-2030: %s. Chance SpaceX sells its own US phone plan by 2028: %s%%.\n"
         "• US wireless service revenue in 2030: %s; revenue per GB %s.\n"
         "• Chance an equal-weight basket of AT&T, Verizon and T-Mobile beats the S&P 500 through 2030: %s%%.\n"
         "Scenarios for 2030: %s." % (rng(ucb), above, rng(mid), rng(traffic), round(growth * 100) if growth is not None else "?", rng(ai), rng(spxmhz), retail,
                                      rng(rev), rng(rpgb), beat, scen)),
        ("Ways to get exposure",
         "No listed security gives clean, passive exposure to spectrum values. The options trade off purity against liquidity:\n"
         "• US carriers (T, VZ, TMUS) own most of the spectrum, but their returns follow pricing and competition, and the market already values their licences at about cost.\n"
         "• Small spectrum holders (Anterix, NextNav, Array, EchoStar's remaining licences) are the purest exposure. They pay off through a sale to a handful of buyers, so the exposure is event-driven and illiquid. We put the chance that at least one sells by 2028 at %s%%.\n"
         "• EchoStar is now mostly a claim on SpaceX shares and cash from its spectrum sales.\n"
         "• SpaceX (SPCX) is the most active buyer, but spectrum is about 1%% of its value.\n"
         "• Globalstar and Iridium are being acquired, which caps their upside; AST SpaceMobile is a high-risk bet on execution.\n"
         "• Tower companies hold no spectrum but gain if scarcity forces more sites or SpaceX leases them.\n"
         "• No fund isolates spectrum; telecom ETFs such as IYZ and XTL are mostly carriers.\n"
         "If convergence plays out, the evidence points to gains for sellers and for the buyer rather than for incumbent carriers. That is an event-driven exposure, not a passive one." % sale),
        ("What would change our view",
         "Signposts that would move us toward the thesis, with our current odds:\n"
         "• The upper C-band auction clears above $0.94 per MHz-pop (%s%%), or SpaceX wins licences in it (%s%%).\n"
         "• US traffic growth returns above 25%% in any year to 2030 (%s%%), or revenue per GB rises for a year (%s%%), either of which would signal a real capacity crunch.\n"
         "• A technology company agrees to buy a US carrier or a cable company's mobile business by 2030 (%s%%).\n"
         "• The FCC pipeline slips: a delayed 2.7 GHz auction or a stalled 7 GHz band would tighten mid-band supply.\n"
         "The dated events are on the Projections tab." % (above, spxucb, reaccel, crunch, techbuy)),
    ]
    for i, (h, b) in enumerate(V):
        rows.append(dict(id="verdict%d" % i, kind="verdict", order=i + 1, heading=h, body=b))

    M = [
        ("Research", "Nine researchers each covered one part of the market: demand, substitutes for spectrum, supply and rules, prices and deals, satellites, carrier economics, listed exposure, past spectrum bets and markets outside the US. They gathered 379 findings, each with a source link and a tag: P for regulators, filings and official statistics, S for reputable press and analysts, W for directional sources. Our environment could not open some primary sites (SEC, FCC, Reuters) directly, so those facts rest on search extracts of the documents."),
        ("Independent check", "Separate fact-checkers re-searched the 102 key claims with differently worded searches. 92 were confirmed, 5 were corrected (the corrections are applied), 5 could not be confirmed independently, and none was refuted. Each finding's check result is in the Appendix."),
        ("Forecasts", "We wrote 32 questions with resolution criteria: 18 quantities and 14 yes-or-no events. Five forecasting lenses answered every question independently: a reference-class lens, a bottom-up model, an advocate for the thesis, a skeptic, and a policy and market-structure lens. We take the median central estimate, the average 10th and 90th percentiles and, for yes-or-no questions, the geometric mean of the odds. A chief forecaster then checked the numbers for consistency and wrote the four scenarios."),
        ("How to read the ranges", "Each range is an 80% interval: we expect the outcome to fall outside it about one time in five. The ticks on each forecast show where each lens put its central estimate. The lenses agreed closely, partly because they worked from the same research, so read the ranges as a careful judgment rather than the output of a statistical model."),
    ]
    for i, (h, b) in enumerate(M):
        rows.append(dict(id="method%d" % i, kind="method", order=i + 1, heading=h, body=b))

    C = [
        "This report is an independent market reference prepared for Fulton Asset Management. It is not investment advice or a recommendation to buy or sell any security. ",
        "Market data (market capitalisations and returns) come from public sources dated October-November 2026 and should be refreshed before any decision. ",
        "Holdings by company, the share of value that is spectrum, capacity per square kilometre and several precedent returns are Whitesail estimates and are labelled as such. ",
        "Deal prices per MHz-pop depend on the population and bandwidth assumed; we use about 335 million people unless a source states otherwise. The ~$8B SpaceX-Grain price is a press report, not a disclosed figure. ",
        "Forecasts are judgments made on 20 November 2026 and will be wrong in places; the signposts say what would change them.",
    ]
    for i, b in enumerate(C):
        rows.append(dict(id="caveat%d" % i, kind="caveat", order=i + 1, heading="", body=b))
    return rows
