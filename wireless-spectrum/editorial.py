"""Report wording for the wireless-spectrum dashboard: chart titles and notes, tiles, verdict, method and caveats.

Numbers in the charts come from the research data points (workflow_result.json); the few charts built from
hand-entered points cite the finding they come from. The verdict text quotes the forecasts it is built on.
"""
import re

DOMAIN_LABEL = {"demand": "Demand", "capacity": "Capacity", "supply": "Supply and rules", "prices": "Prices and deals", "satellite": "Satellites",
                "economics": "Carrier economics", "investables": "Listed exposure", "precedents": "Precedents", "global": "Outside the US"}
DROP_ALIASES = {"EV", "IPO", "ETF", "beam", "Beam", "uplink", "Uplink", "downlink", "Downlink", "screen", "Screen", "pipeline", "Pipeline"}
DEAL_SKIP = {"EchoStar paired AWS-3 (Verizon talks; no deal)", "SpaceX buys Tristar unpaired AWS-3 licenses", "FCC Auction 115 (upper C-band)"}
DEAL_RENAME = {"SpaceX buys Grain 800 MHz (Reuters 2026-10-08)": "SpaceX agrees to buy Grain's 800 MHz (8 Oct 2026)"}
PLAYER_SKIP = {"EchoStar (spectrum seller)", "Space42 (Thuraya)", "Lynk Global / Omnispace"}
PLAYER_STAGE = {"Starlink Mobile (Direct to Cell)": "In service", "T-Mobile T-Satellite": "In service", "AST SpaceMobile": "Testing",
                "Globalstar (being acquired by Amazon)": "In service", "Amazon Leo (D2D)": "Planned", "Iridium NTN Direct (being acquired by Rocket Lab)": "In service",
                "Viasat / Inmarsat": "Planned", "Skylo": "In service"}

FORECAST_SOURCES = {
    "q_ucb_price": "https://www.fierce-network.com/wireless/upper-c-band-auction-gets-april-27-start-date | https://www.lightreading.com/5g/c-band-bidding-wraps-at-$809",
    "q_ucb_proceeds": "https://www.fierce-network.com/wireless/upper-c-band-auction-gets-april-27-start-date",
    "q_traffic_2030": "https://www.benton.org/headlines/ctia-2026-annual-survey-highlights | https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/mobile-traffic-forecast",
    "q_traffic_2035": "https://www.benton.org/headlines/ctia-2026-annual-survey-highlights",
    "q_ai_share": "https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/genai-data-traffic-today-june-2025 | https://www.nokia.com/about-us/news/releases/2026/11/04/nokia-global-network-traffic-report-forecasts-ai-will-drive-nearly-half-of-global-traffic-in-2035/",
    "q_new_mhz_2030": "https://www.wiley.law/alert-One-Big-Beautiful-Bill-Act-Passes-Restoring-FCC-Auction-Authority-and-Establishing-Spectrum-Pipeline",
    "q_new_mhz_2035": "https://www.wiley.law/alert-One-Big-Beautiful-Bill-Act-Passes-Restoring-FCC-Auction-Authority-and-Establishing-Spectrum-Pipeline",
    "q_spacex_mhz": "https://www.fcc.gov/document/order-granting-spacex-echostar-applications | https://www.lightreading.com/5g/spacex-s-bid-for-grain-s-lowband-spectrum-takes-a-step-forward",
    "q_service_rev": "https://lightreading.com/wireless/inflation-mostly-skipped-the-wireless-bill",
    "q_cable_lines": "https://finviz.com/news/418256/charter-announces-third-quarter-2026-results-and-launches-new-operating-model",
    "q_rev_per_gb": "https://lightreading.com/wireless/inflation-mostly-skipped-the-wireless-bill",
}


def rnd(v):
    if v is None:
        return None
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    if abs(v) >= 100:
        return round(v)
    if abs(v) >= 10:
        return round(v, 1)
    return round(v, 2)


def _x(order):
    return order


# ------------------------------------------------------------------ charts
def _licensed(F, pts):
    """Replace the researcher's projections with our forecast central estimates."""
    fc = {x["id"]: x for x in (F.get("chief") or {}).get("forecasts", [])}
    base = [p for p in pts if p["x"] in ("2014", "2017", "2025")]
    for p in base:
        p["series"] = "Licensed"
    out = list(base)
    out.append(dict(series="Projection: our central forecast", x="2027", y=1155 + 160, note="Adds the 160 MHz upper C-band auction scheduled for April 2027."))
    for q, yr in (("q_new_mhz_2030", "2030"), ("q_new_mhz_2035", "2035")):
        if q in fc:
            v = round(1155 + fc[q]["p50"])
            out.append(dict(series="Projection: our central forecast", x=yr, y=v, note="1,155 MHz today plus our central forecast of %d MHz of new auctions (80%% range %d-%d)." % (fc[q]["p50"], fc[q]["p10"], fc[q]["p90"])))
    return out


def _swap(pts):
    return [dict(series=p["x"], x=p["series"], y=p["y"], note=p.get("note")) for p in pts]


CTIA = "https://www.benton.org/headlines/ctia-2026-annual-survey-highlights"
AI_X = {"GenAI share of mobile traffic, measured Apr 2025 (Ericsson)": "Gen AI share of traffic, 2025", "Typical mobile uplink share today (Ericsson)": "Uplink share of all traffic today",
        "Uplink share of GenAI app traffic (Ericsson)": "Uplink share of gen AI traffic", "Uplink share, text LLM traffic (Ookla est.)": "Uplink share, text chatbots",
        "Uplink share, voice/agentic AI (Ookla est.)": "Uplink share, voice and agents", "US urban uplink share 2031, medium GenAI (Ericsson ETR)": "US urban uplink share, 2031 scenario",
        "Uplink share in highest-AI cells 2035 (Nokia)": "Uplink in busiest AI cells, 2035", "AI share of all network traffic 2035 (Nokia)": "AI share of all traffic, 2035 (Nokia)",
        "AI share of broadband traffic 2034 (CTIA)": "AI share of broadband, 2034 (CTIA)"}
CHARTS = [
    # ---- demand
    dict(id="us_traffic", group="demand", order=1, domain="demand", **{"from": "us_traffic"}, kind="line", fmt="dec1",
         title="US mobile data traffic", source_url=CTIA, confidence="S",
         note="Exabytes (trillion megabytes) a year, from CTIA's annual survey. The series includes fixed wireless home internet. Survey editions changed in 2015 and 2017, so the early years are approximate."),
    dict(id="us_traffic_growth", group="demand", order=2, domain="demand", **{"from": "us_traffic_growth"}, kind="bar", fmt="pct",
         keep=lambda p: p["x"] >= "2019", overrides={"2025": 20}, title="Traffic growth is slowing", source_url=CTIA, confidence="S",
         note="Year-on-year growth in US mobile data traffic (CTIA). 2025's 20% was the slowest year since 2020 and the sharpest one-year slowdown in the series."),
    dict(id="global_traffic", group="demand", order=3, domain="demand", **{"from": "global_traffic"}, kind="bar", fmt="int",
         keep=lambda p: p["series"] in ("Actual", "Forecast"), x_map={"2031": "2031F"},
         title="Global mobile traffic, actual and forecast", source_url="https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/mobile-traffic-forecast", confidence="P",
         note="Exabytes a month including fixed wireless (Ericsson). The June 2026 forecast of 515 EB a month in 2031 implies 17% a year, slowing to 14%. Ericsson cut its 2030 forecast from 473 to 430 between its November 2024 and June 2025 editions."),
    dict(id="forecast_overshoot", group="demand", order=4, kind="bar", fmt="int", title="Usage forecasts have run high",
         points=[("Forecast at the time", "2022 (forecast made in 2018)", 26, "Ericsson 2018 edition"), ("What happened", "2022 (forecast made in 2018)", 19, "Later Ericsson edition"),
                 ("Forecast at the time", "2023 (forecast made in 2017)", 48, "Ericsson 2017 edition"), ("What happened", "2023 (forecast made in 2017)", 26, "Ericsson 2024 edition")],
         source_url="https://www.ericsson.com/en/reports-and-papers/mobility-report/key-figures", confidence="S",
         note="North American smartphone data use, GB a month (Ericsson Mobility Report editions). Forecasts made in 2017-18 were roughly double what happened. The current edition expects 52 GB by 2031, up from 25 GB in 2025."),
    dict(id="fwa_subs", group="demand", order=5, domain="demand", **{"from": "fwa_subs"}, kind="line", fmt="dec1",
         x_map={"YE2022": "2022", "YE2023": "2023", "YE2024": "2024", "YE2025": "2025"}, x_order=["2022", "2023", "2024", "2025"],
         title="Fixed wireless home internet subscribers", source_url="https://www.t-mobile.com/news/business/t-mobile-q4-2025-earnings", confidence="P",
         note="Millions at year end. Fixed wireless sells spare mobile capacity as home broadband and took most of the growth in US traffic. Additions are now slowing: Verizon added 159K in Q3 2026 against 261K a year earlier."),
    dict(id="ai_traffic", group="demand", order=6, domain="demand", **{"from": "ai_traffic_scenarios"}, kind="hbar", fmt="pctx",
         keep=lambda p: p["series"] == "Share (%)", series_map={"Share (%)": "Share"}, x_map=AI_X,
         title="AI traffic today is tiny, but upload-heavy", source_url="https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/genai-data-traffic-today-june-2025", confidence="S",
         note="Percent, measured and forecast. Ericsson measured generative AI apps at 0.06% of mobile traffic in April 2025, but 26% of that traffic was uplink against about 10% for mobile overall. The 2031-2035 figures are scenarios from vendors and the industry body, who benefit from a scarcity story."),
    # ---- capacity
    dict(id="capacity_levers", group="capacity", order=1, domain="capacity", **{"from": "capacity_levers"}, kind="hbar", fmt="x",
         keep=lambda p: p["series"].startswith("US 2018"), series_map={"US 2018-2025 (Whitesail estimate)": "Multiple"},
         title="How the US carried 5.6 times more traffic, 2018-2025", source_url="https://techblog.comsoc.org/2026/09/10/ctia-americans-used-more-wireless-data-in-2025-than-in-the-entire-4g-decade-but-growth-slowed-from-2023-2024/", confidence="S",
         note="Multiples, Whitesail estimate from CTIA and WIA counts. Licensed spectrum in use grew about 1.6x and outdoor sites about 1.3x; the remaining 2.7x came from better technology and fuller networks. Over sixty years, more cells did far more of the work than more spectrum (Cooper's law)."),
    dict(id="spectrum_need", group="capacity", order=2, domain="capacity", **{"from": "spectrum_need_estimates"}, kind="hbar", fmt="int",
         series_map={"Claimed need or deficit": "Claimed need or shortfall", "Statutory or planned supply": "Planned supply"},
         title="Claimed spectrum shortfalls against planned supply", source_url="https://www.brattle.com/insights-events/publications/current-spectrum-allocation-is-not-sufficient-for-meeting-the-future-demand-for-wireless-broadband-in-the-us-according-to-a-new-brattle-report", confidence="S",
         note="MHz. Industry studies have forecast large shortfalls before: the FCC's 2010 paper projected a 275 MHz deficit by 2014, and carriers absorbed the growth without visible strain. GSMA's figures are total mid-band per country, not additional spectrum."),
    dict(id="spectral_efficiency", group="capacity", order=3, domain="capacity", **{"from": "spectral_efficiency"}, kind="hbar", fmt="dec1",
         title="Bits per hertz by technology generation", source_url="https://arxiv.org/pdf/2312.00957", confidence="S",
         note="Downlink bits per second per hertz per cell. Typical and target values from vendors and textbooks; the two measured US figures are per stream. 6G's 50 is a vendor ambition, not a measurement."),
    dict(id="capex", group="capacity", order=4, domain="capacity", **{"from": "capex_intensity"}, kind="line", fmt="usd_b",
         keep=lambda p: p["series"].startswith("US wireless capex"), series_map={"US wireless capex, CTIA ($B)": "Capital spending"},
         title="US wireless capital spending", source_url=CTIA, confidence="S",
         note="$B a year (CTIA), excluding spectrum purchases. Spending peaked at $39B in 2022 with the mid-band 5G build and has been flat near $30B since, while traffic kept growing."),
    # ---- supply
    dict(id="holdings", group="supply", order=1, domain="supply", **{"from": "holdings_by_holder"}, kind="stack", fmt="int", height=280, wide="Yes",
         keep=lambda p: p["series"] in ("Low-band", "Mid-band"),
         x_map={"EchoStar (remainder)": "EchoStar (rest)"}, x_order=["T-Mobile", "AT&T", "Verizon", "SpaceX (pending)", "EchoStar (rest)", "Comcast", "Array (TDS)", "Charter"],
         title="Who holds US low- and mid-band spectrum", source_url="https://www.fcc.gov/document/order-granting-spacex-echostar-applications", confidence="S",
         note="Nationwide average MHz, weighted by population (Whitesail estimates from filings and TD Cowen totals). SpaceX's 79 MHz (77 MHz population-weighted, because Grain's up-to-14 MHz of 800 MHz averages about 12 MHz nationally) is pending the EchoStar and Grain closings. AT&T, Verizon and T-Mobile also hold 600-1,700 MHz each of millimetre wave, which carries little traffic."),
    dict(id="pipeline", group="supply", order=2, domain="supply", **{"from": "pipeline"}, kind="hbar", fmt="int",
         series_map={"Excluded by statute": "Excluded by the 2025 law", "Terrestrial pipeline": "In the pipeline or under study"},
         title="What the federal pipeline holds", source_url="https://www.wiley.law/alert-One-Big-Beautiful-Bill-Act-Passes-Restoring-FCC-Auction-Authority-and-Establishing-Spectrum-Pipeline", confidence="S",
         note="MHz by band. Upper C-band is scheduled for April 2027 and 2.7 GHz is targeted for 2028; 7 GHz and 4.4-4.94 GHz are studies. The 2025 law excludes 3.1-3.45 GHz and 7.4-8.4 GHz, 1,350 MHz in all."),
    dict(id="licensed_total", group="supply", order=3, domain="supply", **{"from": "us_licensed_total"}, kind="bar", fmt="int",
         keep=lambda p: p["series"].startswith("Sub-6"), from_forecast=_licensed,
         title="Licensed sub-6 GHz mobile spectrum in the US", source_url="https://www.fcc.gov/document/order-granting-spacex-echostar-applications", confidence="S",
         note="MHz, derived from the FCC's spectrum screen (set at about one third of suitable spectrum). The projections add our central forecasts of new FCC auctions."),
    dict(id="midband_peers", group="supply", order=4, domain="supply", **{"from": "midband_peers"}, kind="hbar", fmt="int",
         keep=lambda p: p["series"].startswith("PolicyTracker"), series_map={"PolicyTracker: assigned 1-7 GHz": "MHz assigned"},
         title="Mid-band assigned to operators by country", source_url="https://policytracker.com/blog/spectrum-auctions-resume-and-", confidence="S",
         note="MHz of 1-7 GHz spectrum assigned to mobile operators (PolicyTracker). Industry-funded studies that count only 3 GHz and above show a larger US gap. The upper C-band auction adds 160 MHz."),
    # ---- prices
    dict(id="auction_prices", group="prices", order=1, domain="prices", **{"from": "auction_prices"}, kind="hbar", fmt="usdp", log_x="Yes", height=380,
         keep=lambda p: "clearing" not in p["series"], series_map={"low-band": "Low-band", "mid-band": "Mid-band", "high-band (mmWave)": "Millimetre wave"},
         title="FCC auction prices per MHz-pop", source_url="https://www.lightreading.com/5g/c-band-bidding-wraps-at-$809", confidence="S",
         note="Gross bids divided by MHz and population, log scale. Mid-band peaked with AWS-3 in 2015; the large C-band and 3.45 GHz blocks sold for less per unit; millimetre wave sold for about a cent. Leftover AWS-3 licences fetched $2.53 in the June 2026 re-auction."),
    dict(id="deal_prices", group="prices", order=2, domain="prices", **{"from": "deal_prices"}, kind="hbar", fmt="usd2", height=360,
         keep=lambda p: p["series"] != "analyst mark", series_map={"low-band": "Low-band", "mid-band": "Mid-band", "MSS/2 GHz": "Satellite-capable 2 GHz"},
         title="Private spectrum sales per MHz-pop", source_url="https://www.lightreading.com/5g/spacex-s-bid-for-grain-s-lowband-spectrum-takes-a-step-forward", confidence="S",
         note="Implied prices of private sales, 2022-2026 (analyst estimates or Whitesail calculations from deal value, MHz and population). T-Mobile sold its 800 MHz licences to Grain for about $0.78; SpaceX agreed two months later to buy them at a reported $1.73."),
    dict(id="auction_proceeds", group="prices", order=3, domain="prices", **{"from": "auction_proceeds"}, kind="hbar", fmt="usd_b", height=380,
         series_map={"gross proceeds": "Gross proceeds"}, title="FCC auction proceeds", source_url="https://www.fcc.gov/auction/103", confidence="P",
         note="$B of gross bids. The 2021 C-band auction raised more than any auction before it, against pre-auction forecasts of $40-52B."),
    dict(id="license_book", group="prices", order=4, domain="prices", **{"from": "license_book"}, kind="bar", fmt="usd_b",
         keep=lambda p: p["series"].startswith("FCC licenses book") and p["x"] in ("AT&T", "Verizon", "T-Mobile"),
         series_map={"FCC licenses book value, Dec 31 2025": "End 2025", "FCC licenses book value, Sep 30 2026": "Sep 2026"},
         title="Spectrum on carrier balance sheets", source_url="https://www.sec.gov/Archives/edgar/data/0000732717/000073271726000370/t-3q2026exhibit991.htm", confidence="P",
         note="FCC licence book value at historical cost, $B. About $411B across the three, roughly 41-50% of each carrier's enterprise value at late-October 2026 prices. T-Mobile's figure is from its filing; AT&T's and Verizon's could not be independently confirmed. Book value is what was paid and does not show what the market would pay for the spectrum today."),
    # ---- global
    dict(id="global_prices", group="global", order=1, domain="global", **{"from": "global_prices"}, kind="hbar", fmt="usdp", log_x="Yes", height=420,
         series_map={"Mid-band auction price": "Mid-band", "mmWave (contrast)": "Millimetre wave"},
         title="Mid-band auction prices around the world", source_url="https://www.analysysmason.com/consulting/articles/spectrum-v", confidence="S",
         note="$ per MHz-pop, log scale. US prices are many times Europe's, where 49 auctions of 3.3-3.9 GHz averaged about 7 cents. Canada's second mid-band tranche sold for about a tenth of the first."),
    dict(id="unsold", group="global", order=2, domain="global", **{"from": "unsold_share"}, kind="hbar", fmt="pct",
         series_map={"Unsold share of offered spectrum": "Share of MHz unsold", "Unsold share by reserve value": "Share of reserve value unsold"},
         title="Spectrum that went unsold", source_url="https://www.developingtelecoms.com/telecom-business/telecom-", confidence="S",
         note="Share of the spectrum offered that found no buyer. India's 2024 auction sold about 1% of the MHz on offer at reserve prices. The UK's 2025 millimetre-wave award sold out, for a token £39m."),
    dict(id="rev_per_mhz", group="global", order=3, domain="global", **{"from": "price_trend"}, kind="bar", fmt="int",
         keep=lambda p: "revenue per MHz index" in p["series"], series_map={"Global revenue per MHz index (GSMA, 2014=100)": "Global", "Europe revenue per MHz index (GSMA, 2014=100)": "Europe"},
         x_map={"2023": "2023-24", "2024": "2023-24"},
         title="Operator revenue per MHz has fallen", source_url="https://www.gsma.com/newsroom/press-release/gsma-calls-for-g", confidence="S",
         note="Index, 2014 = 100 (GSMA, which lobbies for lower spectrum prices). Operators added about 80% more spectrum since 2014 while revenue per MHz fell 54-60%."),
    # ---- precedents
    dict(id="precedent_multiples", group="precedents", order=1, domain="precedents", **{"from": "precedent_multiples"}, kind="hbar", fmt="x2", log_x="Yes", height=440, wide="Yes",
         keep=lambda p: p["y"] > 0, series_map={"Won": "Paid off", "Mixed": "Mixed", "Lost": "Failed or lost"},
         title="What past spectrum bets returned", source_url="https://www.sec.gov/Archives/edgar/data/1001082/000155837023013759/R16.htm", confidence="S",
         note="Sale value divided by cost, log scale (filings and press; several are Whitesail estimates). Dish's SpaceX sales use the $42.40 deal price for the SpaceX shares; marked at the 13 November 2026 close, the Dish programme is about 2.3x cash cost. Bets paid off when a regulator widened what the band could be used for, or when two buyers competed against a deadline."),
    dict(id="euro_3g", group="precedents", order=2, domain="precedents", **{"from": "euro_3g"}, kind="bar", fmt="usd_b",
         title="Europe's 2000 3G auctions and what followed", source_url="https://en.wikipedia.org/wiki/Spectrum_auction", confidence="W",
         note="$B. The UK and Germany raised about $79B in 2000; later auctions of more spectrum raised a tenth as much, and two German winners walked away from licences that cost about €8.4B each."),
    # ---- satellite
    dict(id="d2d_capacity", group="satellite", order=1, domain="satellite", **{"from": "d2d_capacity"}, kind="hbar", fmt="numx", log_x="Yes", wide="Yes",
         keep=lambda p: p["series"].startswith("Capacity density"), series_map={"Capacity density (Mbps per km2, Whitesail estimate)": "Mbps per km²"},
         title="Capacity per square kilometre: satellites against towers", source_url="https://satnews.com/2026/02/25/spacex-unveils-150mbps-performance-target-for-upgraded-direct-to-cell-starlink/", confidence="W",
         note="Mbps per km², Whitesail order-of-magnitude estimates on a log scale. By our estimates, even next-generation satellites reach about a thousandth of a dense urban network (roughly 1/250 to 1/9,000), which is why SpaceX is buying low-band spectrum and looking for tower sites."),
    dict(id="d2d_spectrum", group="satellite", order=2, domain="satellite", **{"from": "d2d_spectrum"}, kind="hbar", fmt="dec1",
         series_map={"Owned or long-term controlled, incl. pending (MHz)": "Owned or controlled, incl. pending", "Partner MNO spectrum in use today (MHz)": "Borrowed from a carrier today"},
         title="Spectrum held by satellite-to-phone operators", source_url="https://www.fcc.gov/document/order-granting-spacex-echostar-applications", confidence="S",
         note="MHz owned or long-term controlled, including pending deals. SpaceX's 79 MHz is pending; AST's includes L-band rights disputed outside North America and S-band priority rights."),
    dict(id="d2d_satellites", group="satellite", order=3, domain="satellite", **{"from": "d2d_satellites"}, kind="hbar", fmt="int", log_x="Yes",
         keep=lambda p: p["y"] > 0, series_map={"D2D-capable satellites in orbit (latest)": "In orbit", "Authorized, applied or targeted": "Authorized, applied for or targeted"},
         title="Satellites that can reach ordinary phones", source_url="https://www.starlink.com/direct-to-cell", confidence="S",
         note="Satellites in orbit now against those authorized or targeted, log scale. SpaceX is authorized for up to 15,000 next-generation direct-to-cell satellites, with launches from 2027."),
    # ---- invest
    dict(id="exposure", group="invest", order=1, kind="hbar", fmt="pctx", height=460, wide="Yes",
         points=[("Spectrum holders", "EchoStar (ECHO)", 34, "Remaining licences at book ($8.45B) against EV; most of the rest is SpaceX shares and cash from its spectrum sales"),
                 ("Spectrum holders", "Anterix (ATEX)", 95, "900 MHz licences are nearly the whole company"),
                 ("Spectrum holders", "NextNav (NN)", 85, "Lower 900 MHz licences; value depends on an FCC petition"),
                 ("Satellite", "Globalstar (GSAT)", 50, "Being acquired by Amazon at a fixed $90 a share, so spectrum prices matter only if the deal breaks"),
                 ("US carriers", "Verizon (VZ)", 50, "Licence book value / EV, late Oct 2026"),
                 ("US carriers", "AT&T (T)", 49, "Licence book value / EV, late Oct 2026"),
                 ("US carriers", "T-Mobile (TMUS)", 41, "Licence book value / EV, late Oct 2026"),
                 ("Spectrum holders", "Array (AD)", 40, "Retained spectrum and pending sale proceeds"),
                 ("Satellite", "Viasat (VSAT)", 25, "L-band, very rough"),
                 ("Satellite", "Iridium (IRDM)", 15, "L-band, very rough; being acquired by Rocket Lab"),
                 ("Satellite", "AST SpaceMobile (ASTS)", 4, "On book value; the market implies more"),
                 ("Satellite", "SpaceX (SPCX)", 1.5, "~$27.6B of agreed spectrum deals in a ~$1.85T company"),
                 ("Cable", "Comcast (CMCSA)", 1.1, "600 MHz and CBRS licences"),
                 ("Cable", "Charter (CHTR)", 0.4, "CBRS licences")],
         title="How much of each company's value is spectrum", source_url="https://www.sec.gov/Archives/edgar/data/0000732717/000073271726000370/t-3q2026exhibit991.htm", confidence="W",
         note="Rough Whitesail estimates: licence book value, or an estimate of the spectrum's market value, divided by enterprise value. Carriers use reported book values; the others are directional only. EchoStar's licences are now a third of its value; most of the rest is SpaceX shares and cash from its sales. A high share is not the same as upside: these companies gain mainly when they sell."),
    # ---- economics
    dict(id="carrier_shock", group="economics", order=1, kind="hbar", fmt="pct1",
         points=[("Change", "AT&T", -9.8, "Close 9 Oct 2026"), ("Change", "Verizon", -8.8, "Close 9 Oct 2026"), ("Change", "T-Mobile", -13.3, "T-Mobile's worst day as a public company")],
         title="Carrier stocks the day after SpaceX agreed to buy 800 MHz", source_url="https://www.axios.com/2026/10/09/spacex-elon-musk-spectrum", confidence="S",
         note="Share price change on 9 October 2026, the day after SpaceX agreed to buy Grain's 800 MHz licences, which still need FCC approval (Axios). The market treated a new spectrum owner as a competitor more than as proof that the carriers' own spectrum had become more valuable."),
    dict(id="net_adds", group="economics", order=2, domain="economics", **{"from": "net_adds"}, kind="bar", fmt="int", swap=True,
         keep=lambda p: p["x"] in ("Q3 2025", "Q3 2026") and "pro forma" not in p["series"],
         series_map={"AT&T postpaid phones": "AT&T", "Verizon postpaid phones": "Verizon", "T-Mobile postpaid accounts (phones not disclosed)": "T-Mobile (accounts)",
                     "Charter mobile lines (legacy Charter)": "Charter (excl. Cox)", "Comcast mobile lines": "Comcast"},
         title="Who is adding mobile customers", source_url="https://finviz.com/news/418256/charter-announces-third-quarter-2026-results-and-launches-new-operating-model", confidence="P",
         note="Thousands of net additions, Q3 2025 against Q3 2026. Charter and Comcast added more lines than AT&T and Verizon added phones; about half of Comcast's new connections were free lines. T-Mobile reports accounts, not phones."),
    dict(id="arpa", group="economics", order=3, domain="economics", **{"from": "arpu"}, kind="bar", fmt="usd", swap=True,
         keep=lambda p: "postpaid" in p["series"], series_map={"Verizon postpaid ARPA": "Verizon", "T-Mobile postpaid ARPA": "T-Mobile"},
         title="Revenue per postpaid account", source_url="https://finviz.com/news/407554/verizon-delivers-another-record-breaking-quarter-with-3q-2026-results-driven-by-strong-postpaid-phone-and-account-additions", confidence="P",
         note="$ a month, Q3 2025 against Q3 2026. Verizon's fell 1.9% as it bought share with promotions; T-Mobile's rose 4%, the one carrier showing pricing power."),
    dict(id="rev_per_gb", group="economics", order=4, kind="hbar", fmt="usd2", log_x="Yes",
         points=[("Revenue per GB", "2010", 412, "CTIA service revenue / traffic"), ("Revenue per GB", "2020", 4.5, "CTIA service revenue / traffic"), ("Revenue per GB", "2025", 1.48, "CTIA service revenue / traffic")],
         title="Revenue per gigabyte keeps falling", source_url="https://lightreading.com/wireless/inflation-mostly-skipped-the-wireless-bill", confidence="S",
         note="US wireless service revenue divided by traffic, $ per GB, log scale (Light Reading from CTIA data). It has fallen about 20% a year since 2020 while total service revenue grew about 3% a year."),
]
for _c in CHARTS:
    if "from" not in _c and "points" not in _c:
        raise SystemExit("chart without data: " + _c["id"])
    if "x_map" in _c and "keep" in _c and "x_order" not in _c:
        pass


# ------------------------------------------------------------------ tiles
def figures():
    F = [
        ("report_window", "header", 0, "Prepared 20 Nov 2026 · regulators, filings, auction records and industry data, with five-lens probabilistic forecasts", "", "", "", "", "", ""),
        ("traffic", "demand", 1, "US mobile data carried in 2025", 159, "EB", "", "Up 20%, after +32% in 2024: the slowest growth since 2020", CTIA, "S"),
        ("ai_share", "demand", 2, "Share of mobile traffic from generative AI apps", "0.06", "%", "", "Ericsson measurement, April 2025; 26% of it uplink", "https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/genai-data-traffic-today-june-2025", "P"),
        ("wifi", "demand", 3, "Share of US smartphone data that goes over Wi-Fi", "82-89", "%", "", "Opensignal, 2024, by carrier", "https://insights.opensignal.com/2024/10/31/wi-fi-drives-smartphone-data-consumption-in-the-us-but-trends-vary-across-operators", "S"),
        ("rpgb", "demand", 4, "Service revenue per GB of traffic, 2025", "1.48", "", "$", "About -20% a year since 2020", "https://lightreading.com/wireless/inflation-mostly-skipped-the-wireless-bill", "S"),
        ("sub6", "supply", 1, "Licensed sub-6 GHz mobile spectrum in the US", 1155, "MHz", "", "Implied by the FCC's 385 MHz screen; low-band about 204 MHz", "https://www.fcc.gov/document/order-granting-spacex-echostar-applications", "S"),
        ("big3", "supply", 2, "Share of 2021 C-band auction dollars won by AT&T, Verizon and T-Mobile", 96, "%", "", "$78.2B of $81.2B; in the 2026 AWS-3 re-auction they took about 99%", "https://www.lightreading.com/5g/c-band-bidding-wraps-at-$809", "S"),
        ("ucb", "supply", 3, "Upper C-band auction, bidding from 27 Apr 2027", 160, "MHz", "", "3.98-4.14 GHz; analysts expect $30-75B", "https://www.fierce-network.com/wireless/upper-c-band-auction-gets-april-27-start-date", "P"),
        ("pipeline", "supply", 4, "Federal pipeline set by the 2025 law", 800, "MHz", "", "At least 300 MHz must be auctioned by 2034", "https://www.wiley.law/alert-One-Big-Beautiful-Bill-Act-Passes-Restoring-FCC-Auction-Authority-and-Establishing-Spectrum-Pipeline", "S"),
        ("cband", "prices", 1, "Lower C-band auction, 2021, per MHz-pop", "0.94", "", "$", "$81.2B of bids for 280 MHz", "https://www.lightreading.com/5g/c-band-bidding-wraps-at-$809", "S"),
        ("echo_att", "prices", 2, "AT&T's purchase of EchoStar spectrum, closed Jul 2026", "22.65", "B", "$", "About $1.40 per MHz-pop for 3.45 GHz and 600 MHz", "https://about.att.com/story/2026/echostar-spectrum.html", "P"),
        ("grain", "prices", 3, "SpaceX's reported price for Grain's 800 MHz", "~8", "B", "$", "About $1.73 per MHz-pop; Grain paid $3.6B two months earlier", "https://www.axios.com/2026/10/09/spacex-elon-musk-spectrum", "S"),
        ("aws3", "prices", 4, "AWS-3 re-auction, June 2026, average per MHz-pop", "2.53", "", "$", "$3.57B; Verizon took about 88%", "https://www.fierce-network.com/wireless/upper-c-band-auction-gets-april-27-start-date", "S"),
        ("d2c_sats", "satellite", 1, "SpaceX direct-to-cell satellites in orbit", 650, "", "", "First generation; up to 15,000 next-generation authorized", "https://www.starlink.com/direct-to-cell", "P"),
        ("users", "satellite", 2, "Starlink Mobile monthly users, Q3 2026", 22, "M", "", "Mostly incidental use in coverage gaps; revenue not disclosed", "https://payloadspace.com/spacexs-ai-revenue-leads-q3-earnings/", "S"),
        ("spx_mhz", "satellite", 3, "Spectrum SpaceX has agreed to buy", 79, "MHz", "", "65 MHz from EchoStar (closing 2027), up to 14 MHz of 800 MHz from Grain", "https://www.fcc.gov/document/order-granting-spacex-echostar-applications", "P"),
        ("ast", "satellite", 4, "AST SpaceMobile satellites operating", 12, "", "", "About 45 targeted by mid-2027; Q3 revenue $42.3M", "https://www.sec.gov/Archives/edgar/data/0001780312/000119312526453758/asts-ex99_2.htm", "P"),
    ]
    out = []
    for fid, tab, order, label, value, unit, prefix, note, url, conf in F:
        out.append(dict(id=fid, tab=tab, order=order, label=label, value=value, unit=unit, prefix=prefix, note=note, source_url=url, confidence=conf))
    return out


# ------------------------------------------------------------------ verdict, method, caveats
def _f(fc, fid):
    return next((x for x in fc if x["id"] == fid), {})


def _p(pr, pid):
    return next((x for x in pr if x["id"] == pid), {})


def money(v, fmt):
    if v is None:
        return "?"
    if fmt == "usd2":
        return "$%.2f" % v
    if fmt == "usd_b":
        return "$%sB" % (("%.0f" % v) if v >= 10 else ("%.1f" % v))
    if fmt == "mhz":
        return "%d MHz" % round(v)
    if fmt == "eb":
        return "%d EB" % round(v)
    if fmt in ("pct1", "pct"):
        return ("%.1f%%" % v) if v < 10 else ("%d%%" % round(v))
    if fmt == "x":
        return "%.1fx" % v
    if fmt in ("m", "m1"):
        return ("%.1fM" % v) if v < 10 else ("%dM" % round(v))
    return str(v)


def rng(f):
    return "%s (80%% range %s to %s)" % (money(f.get("p50"), f.get("fmt")), money(f.get("p10"), f.get("fmt")), money(f.get("p90"), f.get("fmt")))


def plan(fc, pr, sc):
    import verdict as V  # noqa: E402  (written after the forecasts are in)
    return V.plan(fc, pr, sc, _f, _p, rng, money)


# ------------------------------------------------------------------ review edits
# Corrections from the independent review (accuracy, reasoning, usefulness), applied after the datasets are built.
# Each edit names the dataset, row id and field and must find its old text, so a changed upstream text stops the build.
EDITS = [
    # key findings
    ("key_findings", "demand", "summary", "Ericsson measured generative AI apps at 0.06% of mobile traffic", "Ericsson measured generative AI apps at 0.06% of one operator's mobile traffic"),
    ("key_findings", "demand", "body", "that is roughly 0.02% of 2025 US traffic (Whitesail calculation).\n",
     "that is roughly 0.02% of 2025 US traffic (Whitesail calculation).\n• Even 1M robotaxis at that rate would add about 7.3 EB a year, about 4.6% of 2025 US traffic. Licensed wide-area spectrum matters most for outdoor, moving machines such as robotaxis, delivery robots and drones. Smart glasses connect through the phone, and factory robots mostly use Wi-Fi or private 5G. Meta sold more than 7M smart glasses in 2025, and IDC expects 27M display-less units by 2030.\n"),
    ("key_findings", "demand", "body", "We put about a 15% chance", "We put about a 14% chance"),
    ("key_findings", "capacity", "summary", "while median speeds rose 74% in two years to 334 Mbps.", "while median speeds rose 74% in two years to 334 Mbps, helped by C-band and 3.45 GHz spectrum bought in 2021-22."),
    ("key_findings", "capacity", "body", "reached 334 Mbps in H1 2026, up 74% in two years.", "reached 334 Mbps in H1 2026, up 74% in two years. Much of that came from C-band and 3.45 GHz spectrum bought in 2021-22, so it shows spare capacity today."),
    ("key_findings", "capacity", "body", "A scarce input rarely sees its output price fall while buyers cut capex. We put about a 20% chance on a visible US capacity crunch by 2030. Our central case is flat to modestly higher prices for wide mid-band blocks next to carriers' existing holdings, with no broad re-rating of spectrum.",
     "If spectrum were short, carriers would be raising prices and spending more on their networks. Instead, price per GB is falling and capex is flat. We put 7% on revenue per GB rising in any year to 2030 and 14% on a year of traffic growth above 25%, our two tests for a capacity crunch. Our central case has upper C-band bids slightly below 2021's like-for-like price, with no broad re-rating of spectrum."),
    ("key_findings", "supply", "summary", "We estimate about 395 MHz of new licensed spectrum auctioned by 2030 and about 700 MHz by 2035, roughly 60% more than today's base of about 1,155 MHz.",
     "We estimate about 370 MHz of new licensed spectrum auctioned by 2030 and about 640 MHz by 2035, roughly 55% more than today's base of about 1,155 MHz."),
    ("key_findings", "supply", "body", "Our P50 is about 395 MHz of new licensed spectrum auctioned by 2030 and about 700 MHz by 2035.", "Our central estimate is about 370 MHz of new licensed spectrum auctioned by 2030 and about 640 MHz by 2035."),
    ("key_findings", "supply", "body", "about a third by 2030 and about 60% by 2035", "about a third by 2030 and about 55% by 2035"),
    ("key_findings", "prices", "summary", "about 2.8x Grain's cash cost two months earlier", "about 2.2x the $3.6B in cash and licences Grain paid two months earlier"),
    ("key_findings", "prices", "body", "and $2.6B in stock for unpaired AWS-3, about $0.52.", "and $2.6B in stock for unpaired AWS-3, about $0.52, both payable at the closing targeted for 30 November 2027."),
    ("key_findings", "prices", "body", "• AWS-3 (2015) raised $44.9B at about $2.7 per MHz-pop, the US peak.", "• AWS-3 (2015) raised $44.9B; the paired blocks averaged about $2.7 per MHz-pop (about $2.2 across all 65 MHz), the US peak."),
    ("key_findings", "prices", "body", "• 3.45 GHz (2022) raised $22.5B at about $0.74.", "• 3.45 GHz (2022) raised $22.5B at about $0.74 as reported (about $0.67 on today's 335M population)."),
    ("key_findings", "prices", "body", "• EchoStar sold at large premiums to its cost.", "• EchoStar sold to AT&T, and agreed to sell to SpaceX, at large premiums to its cost."),
    ("key_findings", "prices", "body", "and it now says its spectrum puzzle is complete.", "and Musk called the 800 MHz licences the last critical piece for complete US phone coverage, though an urban service would still need more mid-band capacity."),
    ("key_findings", "prices", "body", "Our P50 for upper C-band is about $42B, or about $0.80 per MHz-pop.", "Our central estimate for upper C-band is about $41B, or about $0.77 per MHz-pop (80% range $0.42-1.35)."),
    ("key_findings", "satellite", "body", "• Convergence has brought a new bidder with deep pockets.", "• Convergence has brought a new bidder with deep pockets. SpaceX's IPO raised $75B ($85.7B with the over-allotment), and it can pay partly in its own stock."),
    ("key_findings", "satellite", "body", "• SpaceX paid about $1.03 per MHz-pop for AWS-4 and H-block, a band EchoStar could not use for over a decade.",
     "• SpaceX agreed to pay about $1.03 per MHz-pop for AWS-4 and H-block, a band EchoStar could not use for over a decade, payable at the closing targeted for 30 November 2027."),
    ("key_findings", "satellite", "body", "Analyst estimates put Starlink's broadband capacity at 4-55 Mbps per square km.",
     "Analyst estimates put Starlink's broadband capacity at 4-55 Mbps per square km, and we estimate next-generation satellite-to-phone capacity at about 1-6 Mbps."),
    ("key_findings", "capture", "body", "about 430% from January 2025 to June 2026", "about 430% from a near-distressed level in January 2025 to June 2026"),
    ("key_findings", "capture", "body", "It sold under FCC pressure to two strategic buyers.", "It sold to AT&T, and agreed to sell to SpaceX, under FCC pressure."),
    ("key_findings", "capture", "body", "Higher resale prices reach carrier earnings only when carriers sell, and they rarely do.",
     "Higher resale prices reach carrier earnings mainly when carriers sell, as T-Mobile will through its 50% share of Grain's gain on the resale to SpaceX, and they rarely sell."),
    ("key_findings", "capture", "body", "For 2030 we weight a grind case at about 50% and price pressure from SpaceX and cable at about 30%. We put about 20% on a convergence premium, where spectrum is sold or bought through M&A and carriers re-rate to 8x EBITDA or more.",
     "Our 2030 scenarios put 39% on a steady grind, 24% on a supply wave that lowers prices, 23% on SpaceX becoming a fourth national force and 14% on a scarcity premium. Only the scarcity premium lifts carriers to about 7.5-8.5x EBITDA."),
    ("key_findings", "history", "headline", "Most past spectrum bets lost money; the wins needed a rule change plus two motivated buyers.",
     "Pure-play spectrum holders lost more often than they won; the wins needed a rule change or two motivated buyers."),
    ("key_findings", "history", "summary", "Of 26 spectrum bets from 1996 to 2026 that we reviewed, 6 clearly made money, 12 lost most of the capital and 8 were mixed or pending. Dish/EchoStar, the most relevant case, turned more than $30B of licence spending into about $42.6B of sales, about 1.4x cash cost over roughly ten years.",
     "Of 16 companies whose main asset was spectrum, 3 clearly won, 8 lost and 5 were mixed. Dish/EchoStar, the most relevant case, turned more than $30B of licence spending into about $42.6B of sales at deal values, about 1.4x cash cost over roughly ten years. With the 261.8M SpaceX shares it is due marked at the 13 November close instead of the $42.40 deal price, proceeds are about $68B, about 2.3x."),
    ("key_findings", "history", "body", "Of 26 spectrum bets from 1996 to 2026, 6 clearly made money, 12 lost most of the capital and 8 were mixed or pending. Among the 16 pure-play holders, 3 won, 8 lost and 5 were mixed.",
     "We reviewed 26 cases from 1996 to 2026. They include government auctions and separate pieces of the Dish programme, so treat the tally as a rough guide. 6 clearly made money, 12 lost most of the capital or, where a government was selling, left most spectrum unsold, and 8 were mixed or pending. Among the 16 companies whose main asset was spectrum, 3 won, 8 lost and 5 were mixed."),
    ("key_findings", "history", "body", "• It sold 3.45 GHz and 600 MHz to AT&T for about $23B, AWS-4 and H-block to SpaceX for about $17B, and unpaired AWS-3 to SpaceX for about $2.6B in stock.",
     "• It sold 3.45 GHz and 600 MHz to AT&T for about $23B (closed July 2026) and agreed to sell AWS-4 and H-block to SpaceX for about $17B and unpaired AWS-3 for about $2.6B in stock (closing targeted for November 2027)."),
    ("key_findings", "history", "body", "Against the $37.5B book basis, the multiple is about 1.1x.",
     "Against the $37.5B book basis, the multiple is about 1.1x. These use the $42.40 deal price for the 261.8M SpaceX shares; marked at the 13 November close of $139.11, proceeds are about $68B, about 2.3x cash cost."),
    ("key_findings", "history", "body", "They sold for $17B, about 3.8x over 13-14 years.", "They sold for $17B at deal value, about 3.8x over 13-14 years, and more with the SpaceX shares marked to market."),
    ("key_findings", "investing", "summary", "fell 9-13% after SpaceX's 800 MHz deal.", "fell 9-13% after SpaceX agreed to buy Grain's 800 MHz."),
    ("key_findings", "investing", "body", "We put about 35% on them beating the S&P 500 over 2026-2030.", "We put about 36% on them beating the S&P 500 from November 2026 to the end of 2030."),
    ("key_findings", "investing", "body", "EchoStar sold its licences for about $42.6B of announced consideration. It is due 261.8M SpaceX shares, valued at $42.40 each at the deal price, plus $8.5B of cash at the final closing, targeted for November 2027.",
     "EchoStar sold or agreed to sell its main licences for about $42.6B at deal values. It is due 261.8M SpaceX shares, fixed at $42.40 each when the deal was signed (about $11.1B) and worth about $36B at SpaceX's $139.11 close on 13 November, plus $8.5B of cash at the final closing, targeted for November 2027."),
    ("key_findings", "investing", "body", "Its roughly $20-23B of spectrum purchases is about 1% of its value.",
     "Its roughly $27.6B of agreed spectrum purchases ($19.6B from EchoStar and a reported ~$8B for Grain's 800 MHz) is about 1.5% of its value."),
    ("key_findings", "investing", "body", "IYZ and XTL hold mostly carriers.", "IYZ is led by the large carriers; XTL gives equal weight to carriers, equipment makers and small spectrum and satellite names. We did not verify either fund's holdings."),
    ("key_findings", "investing", "body", "The closest options are an equal-weight basket of the small pure plays, ECHO as a discounted claim on SpaceX shares, or carrier funds. The basket depends on sale timing, ECHO on SpaceX's share price, and carrier funds on carrier pricing.",
     "The listed names closest to the theme are the small pure plays, ECHO and the carrier funds. The pure plays depend on sale timing, ECHO on SpaceX's share price, and the carrier funds on carrier pricing."),
    # scenarios
    ("scenarios", "s1", "summary", "Defined as: SpaceX bills fewer than 3M US mobile lines directly at end-2030, and the median 2029-30 deal price is $0.60-1.40 per MHz-pop.",
     "Defined as: no satellite owner (SpaceX or another) bills 3M or more US mobile lines directly at end-2030, and the median 2029-30 deal price is at least $0.60 but below $1.40 per MHz-pop."),
    ("scenarios", "s1", "carriers", "Revenue grows 2-3% a year and multiples stay at about 6-7.5x. Returns come from dividends and buybacks, not from spectrum value.", "Revenue grows 2.5-3.5% a year and multiples stay at about 6.5-7.5x. Returns come from dividends and buybacks."),
    ("scenarios", "s1", "satellites", "SpaceX is a coverage layer and a buyer, not a price-setter.", "SpaceX adds coverage and bids for spectrum, but carriers still set prices."),
    ("scenarios", "s1", "investors", "Carrier stocks are income holdings, not a spectrum bet.", "Carrier stocks behave as income holdings."),
    ("scenarios", "s2", "summary", "Defined as: SpaceX bills fewer than 3M US lines directly at end-2030, and the median 2029-30 deal price is below $0.60 per MHz-pop.",
     "Defined as: no satellite owner (SpaceX or another) bills 3M or more US mobile lines directly at end-2030, and the median 2029-30 deal price is below $0.60 per MHz-pop."),
    ("scenarios", "s2", "carriers", "keep revenue growth near 1-2%. Multiples sit around 6-7x.", "keep revenue growth near 1.5-2.5%. Multiples sit around 6.5-7x."),
    ("scenarios", "s3", "tagline", "Convergence creates a new national rival, and value moves from carriers to SpaceX and sellers.", "SpaceX becomes a retail entrant and a deep-pocketed bidder, and value moves from carriers to SpaceX and sellers."),
    ("scenarios", "s3", "summary", "directly at end-2030, whatever the price level.",
     "directly at end-2030, whatever the price level. That is under 1% of US mobile connections, so the damage to carriers here comes mainly from SpaceX's low prices and its bidding for spectrum and towers, not from its market share."),
    ("scenarios", "s3", "investors", "Spectrum exposure works best through the buyer and the sellers: SpaceX itself, EchoStar's SpaceX stake, or pure plays sold into a bidding contest. Incumbent carriers fund the shift rather than benefit from it.",
     "In this world the gains go to SpaceX, to EchoStar through its SpaceX shares, and to pure plays sold into a bidding contest. Incumbent carriers pay for the shift."),
    ("scenarios", "s3", "spectrum_prices", "Two tiers: low-band", "Prices split into two tiers. Low-band"),
    ("scenarios", "s4", "summary", "Defined as: SpaceX bills fewer than 3M US lines directly at end-2030, and the median 2029-30 deal price is $1.40 per MHz-pop or more.",
     "Defined as: no satellite owner (SpaceX or another) bills 3M or more US mobile lines directly at end-2030, and the median 2029-30 deal price is $1.40 per MHz-pop or more."),
    ("scenarios", "s4", "summary", "($55-72B)", "($54-72B)"),
    ("scenarios", "s4", "satellites", "Satellite owners gain as deep-pocketed buyers, but SpaceX stays mainly a wholesale coverage partner rather than a retail rival.",
     "Owners of satellite spectrum gain because deep-pocketed buyers compete for their bands. SpaceX stays mainly a wholesale coverage partner to carriers."),
    ("scenarios", "s4", "investors", "Even here, gains arrive through sales and auctions rather than steady earnings growth.", "Even here, gains come mostly through sales and auctions, and earnings grow slowly."),
    # watchlist
    ("watchlist", "w18", "why", "beat the lower C-band price and resolve that forecast Yes,", "resolve that forecast Yes (about $46.6B would already match 2021's $0.87 on the same population basis),"),
    ("watchlist", "w22", "item", "the step at which SpaceX pays about $20B including up to $11B in SpaceX stock.",
     "the step at which SpaceX pays $8.5B in cash and delivers 261.8M SpaceX shares (about $11.1B at the $42.40 deal price, about $36B at the 13 November close)."),
    # universe
    ("universe", "echo", "holdings", "Sold its main spectrum for about $43B of announced value.", "Sold or agreed to sell its main spectrum for about $43B at deal values."),
    ("universe", "rci", "holdings", "also holds 600 MHz and AWS.", "also holds 600 MHz and AWS. Canadian licences have little link to US prices."),
    ("universe", "tu", "holdings", "It also holds 600 MHz and AWS.", "It also holds 600 MHz and AWS. Canadian licences have little link to US prices."),
    ("universe", "bce", "holdings", "It also holds 600 MHz and AWS.", "It also holds 600 MHz and AWS. Canadian licences have little link to US prices."),
    # forecasts and probabilities
    ("forecasts", "q_midband_2030", "rationale", "below today's $1.40 AT&T-EchoStar benchmark", "below the $1.40 AT&T paid EchoStar for a mix of 3.45 GHz and 600 MHz"),
    ("forecasts", "q_midband_2030", "base_rate", "2025-26 private sales ran $0.52-2.53 with a median near $1.20.", "2025-26 deals (private sales plus the AWS-3 re-auction) ran $0.52-2.53 with a median near $1.20 (private sales alone about $1.03)."),
    ("forecasts", "q_ucb_price", "rationale", "close to the 3.45 GHz auction's $0.70.", "close to the 3.45 GHz auction's $0.67 on that basis."),
    ("forecasts", "q_ucb_price", "base_rate", "cleared $0.70-0.87 per MHz-pop on 335M pops", "cleared $0.67-0.87 per MHz-pop on 335M pops"),
    ("probabilities", "b_ucb_2027", "rationale", "so a normal auction closes around August-September 2027. That leaves about four months of slack.", "so a normal auction closes in July 2027. That leaves about five months of slack."),
    # deals and precedents
    ("deals", "fcc-auction-110-3-45-ghz", "notes", "DISH 3.45 GHz later sold to AT&T", "DISH 3.45 GHz later sold to AT&T. About $0.74 at ~305M pops as reported; $0.67 at 335M."),
    ("precedents", "india-2024-spectrum-auction", "cost_basis", "96,317", "96,238"),
    ("charts", "unsold-02", "note", "INR96,318", "INR96,238"),
]
SETS = [
    ("key_findings", "supply", "tag", "Mixed"),
    ("universe", "gsat", "exposure_grade", "Low"),
    ("universe", "gsat", "spectrum_pct_ev", "Capped by the $90 deal"),
    ("universe", "gsat", "spectrum_basis", "Spectrum is most of the $90-a-share Amazon deal value (very rough; Amazon is paying about 40x 2026 sales), but holders receive a fixed price, so spectrum prices matter only if the deal breaks."),
    ("universe", "rci", "exposure_grade", "Low"),
    ("universe", "tu", "exposure_grade", "Low"),
    ("universe", "bce", "exposure_grade", "Low"),
    ("universe", "spcx", "spectrum_pct_ev", "~1.5%"),
    ("universe", "spcx", "spectrum_basis", "~1.5% (about $27.6B of agreed spectrum deals against about $1.85T)"),
    ("universe", "xovr", "spectrum_basis", "Low (via SpaceX, where spectrum is about 1.5% of value)"),
    ("universe", "dxyz", "spectrum_basis", "Low (via SpaceX, where spectrum is about 1.5% of value)"),
    ("watchlist", "w07", "when", "Late Jan to mid-Feb 2027"),
    ("watchlist", "w18", "when", "July 2027 (bidding usually ends 10-13 weeks after the 27 April start; statutory date 4 July 2027)"),
    ("watchlist", "w18", "sort_date", "2027-07-15"),
    ("deals", "amazon-acquires-globalstar", "status", "FCC approved 2026-10-27; closing expected 2027"),
    ("deals", "amazon-acquires-globalstar", "mhz", "~25 (L-band and S-band; ~36.7 if Band 53 is counted separately)"),
    ("precedents", "india-2024-spectrum-auction", "outcome", "Mixed"),
]
