"""Editorial layer applied over the research output by build_infra.py.

The report is written as an independent reference on the industry: it does not quote or grade the
thesis materials it was commissioned alongside. Pushbacks appear as findings and as "figures that
should be revalidated"; recommendations are phrased as suggestions.
"""

HEADLINE = ("Utility infrastructure maintenance is a large market funded through regulated rates, and a well-trodden roll-up category "
            "with moderate margins. Crews and equipment are largely specific to each utility type, and margins change little with scale, "
            "which favors starting with one founder-owned gas distribution maintenance platform at about 6-8x EBITDA and adding units over time.")

# "Our verdict": each section is rendered with a bold subtitle
VERDICT = [
    ("The market",
     "Outsourced maintenance across gas, power and water is about $44-81B a year (est.), paid for through utility rates. "
     "Maintenance and replacement demand is supported by:\n"
     "• investor-owned electric capex of ~$208B in 2025\n"
     "• gas utility construction capex of $49.1B in 2023\n"
     "• federally mandated gas inspection cycles\n"
     "• 50-55% of distribution transformers older than 33 years\n"
     "• water mains replaced on a ~125-year cycle\n"
     "• nuclear plants licensed to 80 years\n"
     "Population growth (+0.5%) and headline load growth add less: they mostly fund new construction."),
    ("The category",
     "Maintenance roll-ups are a proven model. Shermco (~$1.6B to Blackstone), Pike (>$5B EV reported), USIC, Osmose and Azuria/Inframark "
     "were profitable sponsor exits. Multi-unit platforms have a weaker record: no one has built a scaled gas + power + water maintenance "
     "platform, the closest attempts failed (Williams, Orbital), and Artera, the largest gas roll-up, is highly leveraged. "
     "At least 26 sponsor-backed platforms compete for the same add-ons."),
    ("Figures that should be revalidated",
     "• Scaled players: public data shows 15-20 companies with revenue around or above $1B, plus 26 sponsor-backed platforms, though fewer than 10 in each sub-segment.\n"
     "• Shared crews and equipment: only ~15-27% of field headcount can move between power and gas or water (est.). Gas and water share more, at ~53%.\n"
     "• Margins at scale: maintenance contracts earn about 8-10% EBITDA at most sizes. Scale mainly lifts the valuation multiple.\n"
     "• Provider count: 18,877 utility-system construction firms (Census 2017), down from 25,227 in 2012. The maintenance-focused pool is much smaller.\n"
     "• Asset age: NREL's transformer data, PHMSA's pipe inventory and the Utah State water main survey are stronger sources than grid-wide age estimates."),
    ("A path the evidence favors",
     "• Start with one founder-owned gas distribution maintenance platform at ~6-8x EBITDA.\n"
     "• Add water underground work in the same metros.\n"
     "• Consider T&D later, as a separate operating company.\n"
     "• Approach power generation, if at all, through testing or inspection add-ons.\n"
     "A 9-11% margin and cash yield are a sounder underwriting basis than multiple expansion."),
]

# Key findings: research id (q in the synthesis) -> topic, tag, order and rewritten text
FINDINGS = {
    6: dict(id="economics", order=1, topic="Market size and platform economics", tag="Mixed",
            summary=("Outsourced maintenance across gas, power and water is about $44-81B a year (est.): T&D $20-35B, gas $12-20B, water $8-18B "
                     "and power generation $4-8B. A founder-owned platform of about $50M revenue, built to about $150M through add-ons, would "
                     "typically earn a 9-11% EBITDA margin. Scale adds little margin on its own (roughly 0-1 point); its main benefit is a higher "
                     "valuation multiple, which a permanent-capital owner realizes only through a sale or recapitalization.")),
    3: dict(id="age", order=2, topic="How old the infrastructure is", tag="Favorable",
            summary=("Much of it is old, and the age can be measured. Most of the US transmission grid dates from the 1960s-70s, some lines go back "
                     "to the 1920s, and 50-55% of distribution transformers are older than 33 years. At today's replacement pace, the old stock takes "
                     "about 17-22 years to clear for transformers and 11-16 years for cast-iron gas mains, and water mains are on a ~125-year cycle. "
                     "Maintenance extends asset life and is itself recurring revenue, so aging is a slow, funded driver rather than a sudden wave.")),
    5: dict(id="demand", order=3, topic="What is driving demand", tag="Mixed",
            summary=("The drivers most tied to maintenance are replacement capex that utilities recover through their rates, mandated gas safety "
                     "cycles and asset life extension, especially nuclear licenses to 80 years. Population growth has slowed to 0.5%. Electricity use "
                     "was flat for years as products became more efficient and is now rising again, mostly from data centers; that growth largely "
                     "funds new construction. Headwinds include a withdrawn federal leak-detection rule, the end of supplemental federal water "
                     "funding and litigation over the lead-pipe rule.")),
    7: dict(id="structure", order=4, topic="Providers and scaled players", tag="Watch",
            summary=("The provider base is large and shrinking. The Census counted 18,877 utility-system construction firms in 2017, down from 25,227 "
                     "in 2012, though the maintenance-focused pool is much smaller (for example, ~240 members of the gas distribution contractors' "
                     "association). At the top, 15-20 companies have revenue around or above $1B, usually fewer than 10 per sub-segment, and none "
                     "spans gas, power and water at scale.")),
    1: dict(id="precedents", order=5, topic="Roll-ups that worked and roll-ups that struggled", tag="Mixed",
            summary=("Utility maintenance roll-ups have been built many times, with profitable exits such as Shermco (~$1.6B to Blackstone), Pike "
                     "(>$5B reported), USIC, Osmose and Azuria. Multi-unit platforms have a weaker record: the closest attempts failed or are highly "
                     "leveraged, and no one has built a scaled gas + power + water maintenance platform. The field is crowded, with at least 26 "
                     "sponsor-backed platforms plus the public consolidators.")),
    2: dict(id="sharing", order=6, topic="Sharing crews and equipment across units", tag="Watch",
            summary=("Crews and equipment move readily within a unit, partly between gas and water, and rarely between gas or water and power. Only "
                     "about 15-27% of field headcount (est.) can move between power and gas or water, and those are the easiest roles to hire. Gas "
                     "and water overlap more, at about 53% of headcount and 65% of fleet value. The larger synergies are route density, purchasing, "
                     "insurance and back office.")),
    4: dict(id="candidates", order=7, topic="The candidate pool", tag="Mixed",
            summary=("Trade rosters (DCA, NETA, NASSCO, AWWA) and ownership records yield 147 private companies, of which 21 are platform-grade "
                     "(gas 9, water 4, T&D 3, power generation 5). Nine of those look independent, six of them in gas. Setting aside Day & Zimmermann, "
                     "which is unlikely to sell, about 8 names may be worth approaching, most of them gas regionals whose size still needs checking.")),
}

# Edits applied to the research bodies of the findings: (q, old, new); old must occur exactly once
BODY_EDITS = [
    (1, "Yes. Without the branding, this is a utility-infrastructure maintenance (MRO) roll-up, and the playbook has been run many times. The record validates the category, but not the three-unit design.",
        "The utility-infrastructure maintenance (MRO) roll-up playbook has been run many times. The record supports focused, single-niche platforms more than multi-unit ones."),
    (1, ", which is in effect FAM's gas unit at scale.", ", the largest gas distribution maintenance roll-up."),
    (1, "FAM's permanent, low-leverage capital is a genuine edge.", "Permanent, low-leverage capital is a genuine edge here."),
    (1, " are the usual killers (Williams), which matches the deck's own avoid list.", " are the usual causes of failure (Williams)."),
    (1, "FAM will bid against all of them for add-ons.", "A new platform would bid against all of them for add-ons."),
    (2, "Mostly no across units, yes within a unit, and partly between gas and water. Public labor data",
        "Crews and equipment move readily within a unit, partly between gas and water, and rarely between gas or water and power. Public labor data"),
    (2, "Implication: build gas and water as one underground-pipe platform, and run T&D and power-gen as separate operating companies. Underwrite purchasing, overhead and density, not crew flex.",
        "Implication: gas and water fit together as one underground-pipe platform, while T&D and power generation work better as separate operating companies. Purchasing, overhead and density are more reliable synergies than crew flex."),
    (3, "Yes, and routine maintenance is why the thesis works, not a rebuttal of it. Maintenance stretches asset life, and that maintenance is the revenue. The deck, however, uses the weakest numbers available.",
        "Routine maintenance keeps old assets in service, and that maintenance is the revenue. The age of the installed base can be measured from federal and utility data."),
    (3, "Is there a US power line over 50 years old? Yes, many:", "Power lines over 50 years old are common:"),
    (3, "Reporting on PG&E's records dates the line to 1921 (see the update below).",
        "Reporting on PG&E's records dates the line to 1921, and a 2017 PG&E presentation put the average age of its ~50,000 transmission towers at 68 years, "
        "the oldest built before 1910 (GV Wire / KQED, citing the Wall Street Journal).\n"
        "• In Pennsylvania, PPL is rebuilding 230 kV lines from the mid-1920s and 1930s under a 'Vintage Conductor' program (PA PUC filing)."),
    (3, "Quantified like lead times, as years to clear the old stock at today's replacement pace:", "Years to clear the old stock at today's replacement pace:"),
    (3, "Verdict: aging is real, measurable and funded through rate trackers, but it is slow and regional, not a shock. Replace the deck's 70%-of-the-grid figure with NREL's transformer data, and source the gas and water claims to PHMSA and Utah State.",
        "In sum: aging is real, measurable and funded through rate trackers, but it is slow and regional. NREL's transformer data, PHMSA's pipe inventory and the Utah State water main survey are the most defensible sources; grid-wide age percentages should be revalidated before use."),
    (5, "Not as written. The deck leans on drivers that mostly fund new construction, which FAM excludes, and on population, which is barely growing. A stronger why-now exists.",
        "Drivers that fund new construction and drivers that fund maintenance point in different directions."),
    (5, "Population: drop it.", "Population: a weak driver."),
    (5, "Power demand: the instinct is right for homes and wrong for the total.", "Power demand: falling per home, rising in total."),
    (5, "What should anchor the why-now:", "The drivers most tied to maintenance:"),
    (5, "Headwinds the deck omits:", "Headwinds:"),
    (5, "Utilities earn a return on capex but not on O&M, so FAM should target the replacement programs utilities capitalize.",
        "Utilities earn a return on capital spending but not on O&M, so the replacement programs they capitalize are the most durable source of work."),
    (6, "The deck has no TAM and no margin case. The market is big enough; the margin story is not.",
        "The market is large; margins are moderate and change little with scale."),
    (6, "A $500M holdco would hold ~1%.", "A $500M platform would hold ~1%."),
    (6, "Underwrite 9-11% at steady state.", "A 9-11% steady-state margin is a reasonable underwriting case."),
    (6, "unless FAM recapitalizes or sells", "unless the owner recapitalizes or sells"),
    (6, "Expectation: buy a ~$50M founder-owned platform at ~6-8x, build it to ~$150M through add-ons, and earn 9-11%. $500M is a long-horizon outcome, not a plan.",
        "A realistic path: a ~$50M founder-owned platform bought at ~6-8x, built to ~$150M through add-ons, earning 9-11%. $500M is a long-horizon outcome."),
    (7, "The deck's '20,000+ providers' is roughly right but measures the wrong thing. Its '<10 meaningful scaled players' is false.\n\n",
        "The total firm count is large, but the pool relevant to maintenance platforms is much smaller, and the number of scaled players is larger than often assumed.\n\n"),
    (7, "so don't cite them", "so they are not relied on here"),
    (7, "By sub-segment, the deck's framing fits better:", "By sub-segment, the field is thinner:"),
    (7, "Defensible rewrite: '~19,000 utility-system contractors (Census 2017), mostly small; 15-20 players with revenue around or above $1B; fewer than 10 in each sub-segment; none spanning gas, power and water at scale.'",
        "In short: ~19,000 utility-system contractors (Census 2017), mostly small; 15-20 players with revenue around or above $1B; fewer than 10 in each sub-segment; none spanning gas, power and water at scale."),
]

CANDIDATE_BODY = (
    "Platform criteria used in this screen: recurring maintenance work, large regional or national utility customers, specialized labor and "
    "equipment, little dependence on low-bid or fixed-price work, and availability (not owned by a sponsor or a larger company). Candidates come "
    "from DCA, NETA, NASSCO and AWWA member lists, company websites, ownership records and trade press.\n\n"
    "By unit:\n"
    "• Gas: {gas_n} listed, {gas_p} platform-grade. Six look independent: Heath Consultants (third-generation family, Houston), R.H. White "
    "(White family, ~500-600 staff, Massachusetts), Driver Pipeline and Larrett Energy Services (Texas; Larrett was formed by Scott Driver, so the "
    "two may be related), Banks Gas Services (founder-owned, Pittsburgh) and Diversified Utility Services (Atlanta). J.F. Kiely is family-led, but "
    "family control is not confirmed. Sparus (Ridgemont) and Artera (CD&R) are sponsor-owned. Danella would need a safety review: OSHA has "
    "investigated it six times since 2017 over trench work (NBC10). Q3 Contracting is owned by Primoris and is not available.\n"
    "• Water: {water_n} listed, {water_p} platform-grade. Pittsburg Tank & Tower (Johnston family) is independent; Carylon's ownership is "
    "unconfirmed, Maguire Iron's is unknown, and USG Water is sponsor-owned. Independent water firms cluster in tank asset-management contracts "
    "and annual sewer cleaning and CCTV programs. Nine names depend on low-bid work.\n"
    "• T&D: {td_n} listed, {td_p} platform-grade. Pike (TPG) and Osmose (EQT) are sponsor-owned; Tomberlin Pole Treatment (family) is "
    "independent but add-on scale. Davis H. Elliot (ESOP) fits, but its website was not verified. Vegetation managers (Asplundh, Davey, Lewis, "
    "Wright) score lower because the work is thin-margin and re-bid.\n"
    "• Power generation: {pg_n} listed, {pg_p} platform-grade. Day & Zimmermann is the only confirmed independent and is unlikely to sell; "
    "Structural Integrity Associates is employee-owned; Shermco, RESA Power and Allied Power Group are sponsor-owned.\n"
    "• {leads} more names are leads without a verified website.\n\n"
    "Why the independent pool is modest:\n"
    "• 26 sponsor-backed platforms already hold many of the scaled assets.\n"
    "• Much line, lead-pipe and meter work is bought by low bid.\n"
    "• Web sources under-represent founder-owned $10-50M firms, which is where a first platform would most likely come from.\n\n"
    "The gas universe is bounded: the Distribution Contractors Association has ~240 member companies, including suppliers. State utility "
    "commission filings and utility contractor prequalification lists would add names that web sources miss. A fit score of 3 with mostly "
    "unknown fields means not yet diligenced, not weak.")

# Recommended action items (plan steps), in order
STEPS = [
    "Nov 2026: Consider focusing the first unit on gas distribution maintenance, with entry screens such as ~6-8x EBITDA; at least two utility MSA customers; most revenue from MSA or unit-rate maintenance rather than fixed-price or one-off low-bid work; a clean OSHA and EMR record; and leverage well below the levels that strained Artera.",
    "Nov-Dec 2026: It may help to build a primary-source list of 40-60 founder- or family-owned gas contractors with $20-100M of revenue, drawing on the DCA directory (~240 members), state PUC filings on utility replacement programs (NJ, NY, MA, PA and MI hold the most remaining cast iron) and utility contractor prequalification lists.",
    "Dec 2026: The independent gas regionals look like natural first conversations: Heath Consultants, R.H. White, Driver Pipeline and Larrett Energy, Banks Gas Services and Diversified Utility Services, and J.F. Kiely once family control is confirmed. Checking each one's size beforehand would save time. Danella would merit a safety review first, and sponsor auctions priced above the screen may be worth passing over.",
    "Q1 2027: Diligence could focus on MSA terms and renewal dates, customer tenure, revenue mix by work type, PHMSA operator-qualification records, union status (UA/DCA vs non-union), and equipment ownership and fleet age. A reasonable milestone is one letter of intent by the end of Q1 2027 for a ~$50M-revenue platform (illustratively ~$5.5M EBITDA, ~$37-46M EV at 6.8-8.3x).",
    "2027: First add-ons could sit inside the platform's existing utility territories: leak survey, cathodic protection and regulator-station maintenance (all mandated under 49 CFR 192), plus hydro-excavation. These build density (est. 100-300 bps) and a larger share of each utility's spend.",
    "2027: A lean shared-services layer for safety, operator-qualification records, insurance and fleet purchasing would likely cost ~1-2% of revenue; a temporary margin dip around $150M of revenue is common.",
    "2027, after the D.C. Circuit rules on LCRI: Water underground work in the same metros is a natural second step, ideally taking lead service lines only under negotiated or unit-rate programs. Sewer cleaning and CCTV, and tank asset management (Carylon, Pittsburg Tank & Tower or Maguire, after ownership checks), are related options.",
    "Nov 2026-2027: Links with Fulton's companies could start as small pilots: Imperial quoting buybacks of meter brass, service-line and cable scrap; Transend quoting pipe freight; Panther quoting fittings. Committing capex only against purchase orders keeps the downside small.",
    "2028 and later: T&D could be revisited as a separate operating company if a lower-middle-market distribution-maintenance or substation-testing firm becomes available within the screen. Power generation looks best approached through NETA testing or NDE add-ons.",
    "Review points: a go or no-go on the target list in Jan 2027, a decision on the first platform in mid-2027, and a yearly re-underwriting against the watchlist and signals.",
]

FIRST_UNIT = ("A possible starting point", "Natural gas distribution maintenance, built as an underground-utility platform that later adds water and wastewater work in the same metros")
RATIONALE = (
    "Gas distribution maintenance is the only unit that combines four advantages:\n"
    "1. Recurring work that is mandated on a calendar (49 CFR 192 leak surveys, cathodic protection, regulator inspections), plus replacement programs funded through state rate trackers.\n"
    "2. A bounded target universe (~240 DCA members) that still includes founder-owned regional firms not held by sponsors.\n"
    "3. The one sizable cross-unit synergy: gas shares crews and fleet with water underground work (~53% of movable headcount, ~65% of fleet value, est.).\n"
    "4. The most direct links to Fulton's metals, fittings and freight businesses.\n\n"
    "It also carries the clearest caution: Artera, the largest gas roll-up, is highly leveraged, and Centuri earns 8.3%. Buying small, at ~6-8x, "
    "with low leverage and no forced exit is the natural edge for permanent capital.\n\n"
    "T&D is larger but heavily consolidated. Power generation is smaller and dominated by equipment makers' service arms.")

RISK_BODIES = {
    "risk00": "Favoring founder- and family-owned firms at ~6-8x, passing on auctions priced above the screen, and building the pipeline from primary rosters rather than banker books.",
    "risk01": "Underwriting 9-11% steady-state margins and cash yield, giving little credit for cross-unit crew flex, and keeping shared costs to ~1-2% of revenue.",
    "risk02": "Permanent capital with modest leverage (Centuri deleveraged to 2.5x), staggered maturities, and a preference for several small deals over one large one.",
    "risk03": "Capping fixed-price and low-bid revenue in the platform criteria, favoring add-ons whose work is MSA or unit-rate, and reporting job-level margins from day one.",
    "risk04": "At least two utility MSAs at entry, diligence on renewal dates and tenure, and growth with existing customers before new geographies.",
    "risk05": "Leaning toward bare steel, vintage plastic, service lines and mandated compliance work, which run into the 2040s.",
    "risk06": "A base case built on existing state rate-tracker programs, with federal rules and federal money treated as upside.",
    "risk07": "Screening OSHA history and EMR, and centralizing operator-qualification records and the safety program. Repeat trench citations are a reason to pass.",
    "risk08": "Mapping union status for each target, not assuming crews can move between units or regions, and budgeting ~0.7 pts for wage harmonization.",
    "risk09": "Favoring replacement programs that utilities capitalize and earn a return on over O&M work they expense.",
}

CAVEATS = (
    "Many central figures are analyst estimates, not reported data:\n"
    "• the market size by unit ($44-81B)\n"
    "• the labor and fleet overlap matrices\n"
    "• synergy basis points\n"
    "• the illustrative P&L and margin bridge\n"
    "• the flows shown for the prospective platform on the market map\n"
    "• the size of the platform-quality universe\n"
    "• the pre-tax cash yield\n\n"
    "Items that are unverified or weakly sourced:\n"
    "• The 1921 build date of PG&E's Caribou-Palermo line (press reporting on PG&E records).\n"
    "• MIT's 8,000 mi/yr transmission build rate (excluded) and the ~90% replacement share of transmission spend.\n"
    "• Artera's current rating (a Dec 2025 S&P action was not confirmed).\n"
    "• Pike's >$5B value (press-reported).\n"
    "• Asplundh's revenue and Day & Zimmermann's current revenue.\n"
    "• The current owners of USG Water Solutions, Carylon, Pittsburg Tank & Tower and Maguire Iron.\n"
    "• The PJM +41% wholesale price figure.\n\n"
    "Six-digit NAICS firm counts conflict across aggregators and were not used. The share of gas mains over 50 years old rests on 2021 PHMSA data and should be re-pulled.\n\n"
    "The candidate list over-represents sponsor-owned and web-visible firms. Founder-owned $10-50M businesses need primary rosters (DCA, NETA, NASSCO, AWWA, state PUC lists). "
    "Lower-middle-market multiples are all-industry (GF Data), not utility-specific.\n\n"
    "Not researched here: state gas-transition policy and long-run gas demand.\n\n"
    "Out of scope: sponsor economics and any specific live deal process.")

# The prospective platform, as it would sit in the market (Analysis for Fulton tab)
PROFILE = [
    ("Profile", "A founder- or family-owned gas distribution maintenance contractor with about $50M of revenue and a 9-11% EBITDA margin (est.), "
                "working under MSAs with two to four gas utilities in one region. Typical work: main and service replacement, leak survey and repair, "
                "meter and regulator work, and cathodic protection."),
    ("Who it would sell to", "Gas distribution utilities (LDCs) under multi-year MSAs and unit-rate programs, about $30-40M a year (est.); transmission "
                             "pipeline operators for integrity digs, $2-5M; and, in a second phase, water utilities in the same metros, $5-10M. "
                             "The utilities recover this spending through state rate trackers paid by households and businesses."),
    ("Who it would buy from", "Field crews (pipelayers, operators, laborers, CDL drivers; UA/DCA or merit shop), about $16-20M a year in wages; paving, "
                              "restoration and traffic-control subcontractors, $3-6M; insurance and surety, $1.5-2.5M; equipment rental, $1-2.5M; "
                              "materials the utility does not furnish, from distributors such as Core & Main, $1-3M; vacuum excavators and drills from "
                              "makers such as Vermeer; and hydro-excavation subcontractors such as Badger (all est.)."),
    ("Who it would compete with for work", "Centuri, Artera (Miller Pipeline, Minnesota Limited) and Energy Services of America at scale; Quanta and "
                                           "MasTec units on larger programs; and regional independents in each territory. Utilities re-bid MSAs every "
                                           "three to five years, so safety record and unit prices decide renewals."),
    ("Who it would compete with for deals", "Sponsor-backed platforms buying gas and underground add-ons, including Sparus (Ridgemont), Delphi "
                                            "Infrastructure (MPE), USIC and Pro-Vac, plus public consolidators. Founder-owned firms sold off-market "
                                            "tend to price at ~6-8x EBITDA; auctions run higher."),
    ("Add-on paths", "Inside its territories: leak survey, cathodic protection, regulator-station maintenance and hydro-excavation. In the same metros: "
                     "water main and service work, sewer cleaning and CCTV, and tank asset management."),
]

# How Fulton's companies could work with the prospective platform (replaces the industry-wide portfolio links)
FULTON_LINKS = [
    ("Imperial Group", "Buys the platform's meter brass, steel service-line and cable scrap; small direct volumes (~$0.05-0.3M a year, est.). The larger "
                       "opening is an introduction to the platform's utility customers, whose replacement programs generate $10-45M a year of gas scrap and "
                       "$30-80M of lead and brass from water work (addressable market, est.)."),
    ("Transend Logistics", "Moves pipe and materials from distributor yards to the platform's job sites (~$0.2-0.6M a year, est.), and could quote the "
                           "pipe makers that supply the platform's utility customers."),
    ("Panther Metalflow", "Machined brass and steel fittings and meter-set components, sold through the platform's distributors or specified on its jobs "
                          "(~$0.05-0.3M a year, est.). Most major materials are furnished by the utilities."),
    ("AFCO Industries", "Aluminum compartments and toolboxes for the platform's truck bodies, through upfitters (~$0.05-0.1M a year, est.)."),
    ("Stainless Foundry & Engineering", "Occasional specialty castings for regulator-station and valve rebuilds; not sized."),
    ("Metaltec", "No clear link found."),
]

PROSPECT_NODE = dict(
    id="prospect", name="New gas platform", layer="B", group="Prospective", group_order=-1, kind="prospect",
    description=("A founder-owned gas distribution maintenance contractor of about $50M revenue, as a first platform that later adds water "
                 "underground work in the same metros. The flows shown are estimates for a company of that size, not a specific target."),
    size_label="~$50M revenue; 9-11% EBITDA (est.)", ownership="Founder- or family-owned at entry", source_url="https://directory.dcaweb.org/")

# (source, target, product, low $M, high $M, basis, source_url)
PROSPECT_EDGES = [
    ("field-labor", "prospect", "Field crews: pipelayers, operators, laborers and CDL drivers (UA/DCA or merit shop)", 16, 20,
     "~35-40% of revenue in field wages and benefits for MSA maintenance work (est.).", "https://www.bls.gov/oes/2023/may/naics4_237100.htm"),
    ("restoration", "prospect", "Paving, restoration and traffic-control subcontracts", 3, 6, "~6-12% of revenue on main and service replacement jobs (est.).", ""),
    ("insurance", "prospect", "General liability, auto, workers' comp and surety", 1.5, 2.5, "~3-5% of revenue (est.).", ""),
    ("united-rentals", "prospect", "Excavators, trench shoring and traffic equipment rental", 1, 2.5, "Peak and specialty equipment rented rather than owned (est.).", ""),
    ("core-main", "prospect", "PE pipe, fittings and meter-set materials the utility does not furnish", 1, 3,
     "Many gas utilities furnish the major materials, so contractor-bought materials are a small share (est.).", ""),
    ("vermeer", "prospect", "Vacuum excavators and compact directional drills", 0.5, 1.5, "Fleet replacement capex (est.).", ""),
    ("badger-infra", "prospect", "Hydro-excavation subcontracts for locating and daylighting", 0.5, 1.5, "Used where the platform has no own vac trucks (est.).", ""),
    ("prospect", "other-gas-ldcs", "Main and service replacement, leak survey and repair, meter and regulator work under MSAs", 30, 40,
     "Most of a ~$50M platform's revenue comes from two to four gas utility MSAs (est.).", "https://directory.dcaweb.org/"),
    ("prospect", "pipeline-operators", "Integrity digs and anomaly repair for transmission pipelines", 2, 5, "Adjacent work for gas distribution contractors (est.).", ""),
    ("prospect", "municipal-water", "Water main, service and sewer work in the same metros (second phase)", 5, 10, "After the gas platform is established (est.).", ""),
]
FULTON_EDGES = [
    ("fulton-imperial", "prospect", "Scrap buyback: meter brass, steel service-line and cable scrap from replacement jobs (Imperial pays the platform)", 0.05, 0.3,
     "Small direct volumes; the larger opening is the platform's utility customers (est.)."),
    ("fulton-transend", "prospect", "Freight of pipe and materials to job sites", 0.2, 0.6, "Platform's own material moves (est.)."),
    ("fulton-panther", "prospect", "Machined fittings and meter-set components", 0.05, 0.3, "Through distributors or specified on jobs (est.)."),
    ("fulton-afco", "prospect", "Aluminum compartments and toolboxes for truck bodies (via upfitters)", 0.05, 0.1, "About a tenth of the fleet replaced each year (est.)."),
]

# Plain replacements in other datasets: (dataset, record id, field, old, new)
TEXT_EDITS = [
    ("candidates", "jf-kiely", "recurring_evidence", " (gas plus water in the same metros, as the thesis wants)", " (gas plus water in the same metros)"),
    ("candidates", "utility-line-services", "recurring_evidence", "fits the thesis", "fits the gas-plus-water platform model"),
    ("candidates", "structural-integrity", "red_flags", "(thesis wants field-first)", "(a field-first platform is a better fit)"),
    ("chart_meta", "drivers", "title", "why-now driver", "demand driver"),
    ("chart_meta", "scaled_rev", "note", "Fifteen to twenty companies operate at or near $1B, well above the deck's 'fewer than ten'.",
     "Fifteen to twenty companies operate at or near $1B, though fewer than ten in any one sub-segment."),
    ("figures", "pre1970", "note", "PHMSA (2021); the deck's 25% is close", "PHMSA (2021)"),
    ("findings", "demand:epa-dwinsa", "claim", "(deck claim verified; not re-fetched this run)", "(verified)"),
    ("findings", "cand_gas:danella-osha", "claim", "This conflicts with the thesis's 'strong safety record' criterion pending diligence.",
     "This is a safety-record concern pending diligence."),
    ("platforms", "badger-infrastructure-solution", "lesson", "It supports the thesis's integrated-manufacturing idea within one niche.",
     "It shows the value of owning and building the equipment base within one niche."),
    ("platforms", "williams-industrial-services-g", "lesson", "This is exactly the thesis's 'avoid' list.", "These are the usual risks to screen out."),
    ("unit_ranking", "u2", "why", "the closest match in the whole thesis to", "the closest match in this report to"),
    ("unit_ranking", "u4", "why", "The precedents are the worst in the thesis:", "The precedents are the weakest of the four units:"),
    ("value_chain_edges", "e90", "basis", "outside thesis TAM", "outside the core maintenance market"),
    ("value_chain_nodes", "centuri", "description", "Closest public analogue to the thesis:", "Closest public analogue to a gas maintenance platform:"),
    ("value_chain_nodes", "pipeline-operators", "description", "adjacent to, not inside, the thesis TAM", "adjacent to, not inside, the core maintenance market"),
    ("value_chain_nodes", "dc-ci-owners", "description", "Outside the thesis TAM.", "Outside the core maintenance market."),
    ("watchlist", "w12", "why", "to finalize the deck's mains-over-50-years statistic", "to update the share of mains over 50 years old"),
    ("unit_ranking", "u1", "why", "Artera, the same unit at scale, is distressed.", "Artera, the largest gas roll-up, is highly leveraged (rated CCC+ in 2022)."),
    ("watchlist", "w11", "why", "Sets the prices FAM will face", "Sets the prices a buyer will face"),
    ("platforms", "vortex-companies", "lesson", "that FAM's water unit would bid against", "that a new water platform would bid against"),
    ("platforms", "utility-service-co-usg-water-s", "lesson", "It is a template for FAM's water unit.", "It is a template for a water maintenance unit."),
    ("value_chain_nodes", "esoa", "description", "a scale reference for a FAM platform", "a scale reference for a new platform"),
    ("value_chain_nodes", "regional-gas", "description", "The pool FAM would buy from.", "The pool a new platform would buy from."),
    ("findings", "precedents:crowding-count", "claim", "across FAM's four target sub-segments", "across the four sub-segments covered here"),
    ("findings", "fragmentation:est-platform-universe", "claim", "meeting FAM's platform criteria", "meeting the platform criteria used here"),
]
