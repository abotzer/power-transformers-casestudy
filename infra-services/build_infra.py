"""Build the infra-services dashboard datasets from the research workflow results.

Usage: python3 -I build_infra.py <research/workflow_result.json> <out_dir> <research/candidates_round2.json>
Writes one JSON file per dataset (figures, plan, key_findings, key_numbers, charts, chart_meta, platforms, scaled,
pl, synergies, candidates, unit_ranking, findings, watchlist, glossary, value_chain_nodes, value_chain_edges)
plus dashboard/layer_titles.json (column titles for the page).
Chart rows are curated here from the research tables; every chart row carries its source in chart_meta.
Report wording (findings, verdict, recommended actions, the prospective platform) comes from editorial.py.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editorial as E  # noqa: E402

ID_BRACKETS = re.compile(r"\s*\[(?:[a-z0-9]+(?:-[a-z0-9]+)+)(?:,\s*[a-z0-9]+(?:-[a-z0-9]+)*)*\]")
DROP_ALIASES = {"EO", "CT", "CC", "shelter", "fluids", "platform", "Platform", "outage", "Outage", "backlog", "Backlog",
                "organic", "Organic", "add-on", "Add-on", "roll-up", "Roll-up"}


def clean(t):
    t = str(t or "").replace("**", "").replace("&amp;", "&")
    t = ID_BRACKETS.sub("", t)
    t = re.sub(r"(^|\n)\s*-\s+", r"\1• ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def https(u):
    u = str(u or "").strip()
    return u if u.startswith("https://") or u.startswith("http://") else ""


def slug(s, n=40):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:n]


def write(out, name, rows):
    with open(os.path.join(out, name + ".json"), "w") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print(name, len(rows))


def apply_round2(out, cands):
    """Bring the candidate finding, its numbers and the unit ranking in line with the round-2 candidate list."""
    def load(name):
        return json.load(open(os.path.join(out, name + ".json")))

    units = ["gas", "water", "T&D", "power-gen"]
    plat = [c for c in cands if c["grade"] == "Platform"]
    ind = [c for c in plat if c["c_independent"] == "yes"]
    n = {u: sum(1 for c in cands if c["unit"] == u) for u in units}
    p = {u: sum(1 for c in plat if c["unit"] == u) for u in units}
    i = {u: [c["name"] for c in ind if c["unit"] == u] for u in units}
    leads = sum(1 for c in cands if c["grade"] == "Lead")
    # the prose in editorial.py names these companies, so stop the build if the list changes
    assert len(cands) == 147 and [p[u] for u in units] == [9, 4, 3, 5] and [len(i[u]) for u in units] == [6, 1, 1, 1] and leads == 38, (len(cands), p, i, leads)
    by_unit = "gas %d, water %d, T&D %d, power generation %d" % tuple(p[u] for u in units)

    kf = load("key_findings")
    f = next(x for x in kf if x["id"] == "candidates")
    f["body"] = E.CANDIDATE_BODY.format(gas_n=n["gas"], gas_p=p["gas"], water_n=n["water"], water_p=p["water"], td_n=n["T&D"], td_p=p["T&D"],
                                        pg_n=n["power-gen"], pg_p=p["power-gen"], leads=leads)
    f["sources"] = " | ".join(["https://directory.dcaweb.org/", "https://heathus.com", "https://rhwhite.com", "https://www.driverpipeline.com", "https://pttg.com", "https://tomberlinpole.com"]
                              + [u for u in f["sources"].split(" | ") if u])
    write(out, "key_findings", kf)
    kn = [x for x in load("key_numbers") if x["finding"] != "candidates" or not any(k in x["label"] for k in ("screened", "Platform-grade", "Realistic"))]
    new = [dict(label="Private companies listed after the roster check", value="%d (%d without a verified website)" % (len(cands), leads), source_url="https://directory.dcaweb.org/"),
           dict(label="Platform-grade candidates by unit", value="%d (%s)" % (len(plat), by_unit), source_url="https://directory.dcaweb.org/"),
           dict(label="Platform-grade and independent", value="%d (%d in gas)" % (len(ind), len(i["gas"])), source_url="https://heathus.com"),
           dict(label="Names that may be worth approaching now", value="~%d, mostly gas regionals (size unchecked)" % (len(ind) - 1), source_url="https://rhwhite.com")]
    rest = [x for x in kn if x["finding"] == "candidates"]
    kn = [x for x in kn if x["finding"] != "candidates"]
    for k, x in enumerate(new + [dict(label=r["label"], value=r["value"], source_url=r["source_url"]) for r in rest]):
        kn.append(dict(id="candidates-n%02d" % k, finding="candidates", order=k, label=x["label"], value=x["value"], source_url=x["source_url"]))
    write(out, "key_numbers", kn)

    rank = load("unit_ranking")
    cand_text = {
        "Natural gas": "%d listed; %d platform-grade, 6 of them independent: Heath Consultants, R.H. White, Driver Pipeline, Larrett Energy, Banks Gas Services, Diversified Utility Services. J.F. Kiely is family-led (control unconfirmed). Sponsor-owned: Sparus (Ridgemont), Artera (CD&R). Danella has a safety flag." % (n["gas"], p["gas"]),
        "Water": "%d listed; %d platform-grade: Pittsburg Tank & Tower (Johnston family), Carylon (ownership unconfirmed), Maguire Iron (ownership unknown), USG (sponsored). Nine names depend on low-bid work." % (n["water"], p["water"]),
        "T&D": "%d listed; %d platform-grade: Pike (TPG) and Osmose (EQT), both sponsor-owned, and Tomberlin Pole Treatment (family, add-on scale). Davis H. Elliot (ESOP) fits but is unverified. Vegetation managers score 3." % (n["T&D"], p["T&D"]),
        "Power-generation": "%d listed; %d platform-grade. Only Day & Zimmermann is confirmed independent, and it is unlikely to sell; Structural Integrity Associates is employee-owned. Shermco, RESA Power and Allied Power Group are sponsor-owned." % (n["power-gen"], p["power-gen"]),
    }
    for r in rank:
        key = next(k for k in cand_text if r["unit"].startswith(k))
        r["candidates"] = cand_text[key]
        r["why"] = (r["why"].replace("\u2022 It has the most independent platform-grade candidates.", "\u2022 It has the second-largest candidate list, clustered in tank asset management and sewer cleaning.")
                    .replace("\u2022 No independent platform-grade candidate was found.", "\u2022 The only independent platform-grade candidate, Tomberlin Pole Treatment, is add-on scale."))
    write(out, "unit_ranking", rank)


def apply_text_edits(out):
    """Plain wording fixes in datasets that come straight from the research (see editorial.TEXT_EDITS)."""
    cache = {}
    for name, rid, field, old, new in E.TEXT_EDITS:
        rows = cache.setdefault(name, json.load(open(os.path.join(out, name + ".json"))))
        r = next(x for x in rows if x["id"] == rid)
        assert r[field].count(old) == 1, (name, rid, field, old[:50])
        r[field] = r[field].replace(old, new)
    for name, rows in cache.items():
        write(out, name, rows)


def main(src, out, round2=None):
    r = json.load(open(src))
    R, S = r["research"], r["synthesis"]
    os.makedirs(out, exist_ok=True)

    # ---------- key findings (the research answers, reworded as independent findings in editorial.py) ----------
    bodies = {a["q"]: clean(a["answer"]) for a in S["answers"]}
    bodies[3] = bodies[3].replace("A secondary source dates the line to 1921; confirm that against the Butte County DA report before citing it.",
                                  "Reporting on PG&E's records dates the line to 1921 (see the update below).")
    for q, old, new in E.BODY_EDITS:
        assert bodies[q].count(old) == 1, (q, old[:60])
        bodies[q] = bodies[q].replace(old, new)
    kf, kn = [], []
    for a in S["answers"]:
        f = E.FINDINGS[a["q"]]
        srcs = list(a.get("source_urls") or [])
        nums = list(a["key_numbers"])
        if a["q"] == 3:
            srcs += ["https://gvwire.com/2019/07/11/report-pge-ignored-repairs-on-aging-power-lines/", "https://www.kqed.org/news/11760156/report-pge-knew-about-extensive-power-line",
                     "https://www.puc.pa.gov/pcdocs/1118448.pdf"]
            nums = [dict(label="Caribou-Palermo line (Camp Fire) in service since", value="1921", source_url="https://gvwire.com/2019/07/11/report-pge-ignored-repairs-on-aging-power-lines/"),
                    dict(label="PG&E transmission towers, average age (2017)", value="68 yrs", source_url="https://gvwire.com/2019/07/11/report-pge-ignored-repairs-on-aging-power-lines/")] + nums
        kf.append(dict(id=f["id"], order=f["order"], topic=f["topic"], tag=f["tag"], summary=f["summary"], body=bodies[a["q"]],
                       sources=" | ".join(u for u in srcs if https(u))))
        for i, k in enumerate(nums):
            kn.append(dict(id=f"{f['id']}-n{i:02d}", finding=f["id"], order=i, label=clean(k["label"]), value=clean(k["value"]), source_url=https(k.get("source_url"))))
    write(out, "key_findings", sorted(kf, key=lambda x: x["order"]))
    write(out, "key_numbers", kn)
    for old in ("answers", "answer_numbers", "deck_claims"):
        if os.path.exists(os.path.join(out, old + ".json")):
            os.remove(os.path.join(out, old + ".json"))

    # ---------- plan ----------
    P = S["fam_plan"]
    plan = [dict(id="headline", kind="headline", order=0, heading="Headline", body=E.HEADLINE)]
    for i, (h, b) in enumerate(E.VERDICT):
        plan.append(dict(id=f"verdict{i}", kind="verdict", order=1 + i, heading=h, body=b))
    plan += [dict(id="first_unit", kind="first_unit", order=8, heading=E.FIRST_UNIT[0], body=E.FIRST_UNIT[1]),
             dict(id="rationale", kind="rationale", order=9, heading="Why", body=E.RATIONALE)]
    for i, x in enumerate(E.STEPS):
        plan.append(dict(id=f"step{i:02d}", kind="step", order=10 + i, heading=f"Step {i + 1}", body=x))
    for i, (h, b) in enumerate(E.PROFILE):
        plan.append(dict(id=f"profile{i}", kind="profile", order=30 + i, heading=h, body=b))
    for i, (h, b) in enumerate(E.FULTON_LINKS):
        plan.append(dict(id=f"vi{i:02d}", kind="vi", order=40 + i, heading=h, body=b))
    for i, x in enumerate(P["risks"]):
        rid = f"risk{i:02d}"
        plan.append(dict(id=rid, kind="risk", order=80 + i, heading=clean(x["risk"]), body=E.RISK_BODIES[rid]))
    for i, x in enumerate(P["signals"]):
        plan.append(dict(id=f"sig{i:02d}", kind="signal", order=100 + i, heading=clean(x["signal"]), body=clean(x["meaning"])))
    plan.append(dict(id="caveats", kind="caveat", order=200, heading="Caveats", body=E.CAVEATS))
    write(out, "plan", plan)

    # ---------- unit ranking ----------
    write(out, "unit_ranking", [dict(id=f"u{u['rank']}", rank=u["rank"], unit=clean(u["unit"]), attractiveness=u["attractiveness"], why=clean(u["why"]),
                                     tam=clean(u.get("tam")), mro_share=clean(u.get("mro_share")), margin_range=clean(u.get("margin_range")),
                                     fragmentation=clean(u.get("fragmentation")), competition=clean(u.get("competition")), candidates=clean(u.get("candidates")))
                                for u in S["unit_ranking"]])

    # ---------- watchlist ----------
    write(out, "watchlist", [dict(id=f"w{i:02d}", sort_date=w["sort_date"], when=clean(w["when"]), item=clean(w["item"]), why=clean(w["why"]))
                             for i, w in enumerate(sorted(S["watchlist"], key=lambda w: w["sort_date"]))])

    # ---------- platforms (precedents) ----------
    orank = {"thriving": 0, "solid": 1, "mixed": 2, "struggling": 3, "failed/restructured": 4, "exited": 5}
    write(out, "platforms", [dict(id=slug(p["name"], 30), name=clean(p["name"]), website=https(p.get("website")), type=p["type"], sponsor=clean(p.get("sponsor_or_ticker")),
                                  units=", ".join(p["units"]), model=p["model"], year=clean(p.get("formed_or_platform_year")), revenue=clean(p.get("revenue_latest")),
                                  margin=clean(p.get("ebitda_margin")), acquisitions=clean(p.get("acquisitions")), outcome=p["outcome"], outcome_rank=orank.get(p["outcome"], 9),
                                  evidence=clean(p["outcome_evidence"]), lesson=clean(p["lesson"]), sources=" | ".join(u for u in p["source_urls"] if https(u)))
                             for p in R["precedents"]["platforms"]])

    # ---------- scaled players ----------
    t = [t for t in R["fragmentation"]["tables"] if t["title"].startswith("Scaled US")][0]
    scaled = []
    for i, row in enumerate(t["rows"]):
        company, rev, util, fy, tier, units, own, web, conf = (row + [""] * 9)[:9]
        m = re.match(r"[~>]?\s*([\d.]+)", rev.replace(",", ""))
        revb = round(float(m.group(1)) / 1000, 2) if m else None
        scaled.append(dict(id=f"s{i:02d}", company=company, revenue_label=(rev + (" ($M, " + fy + ")" if rev and rev[0].isdigit() or rev.startswith("~") or rev.startswith(">") else "")).strip(),
                           revenue_usd_b=revb, units=units.replace("2b", "T&D").replace("2a", "power-gen").replace("1", "gas").replace("3", "water"),
                           ownership=own, website=https(web), note=util, confidence=conf))
    scaled.append(dict(id="s90", company="Badger Infrastructure Solutions", revenue_label="831.7 ($M, FY2025)", revenue_usd_b=0.83, units="gas, T&D, water (hydro-excavation)",
                       ownership="Public (TSX: BDGI)", website="https://www.badgerinc.com", note="Owns a self-built hydrovac fleet; 23.8% adj. EBITDA margin", confidence="P"))
    write(out, "scaled", scaled)

    # ---------- P&L and synergies ----------
    t = [t for t in R["tam_economics"]["tables"] if t["title"].startswith("Illustrative platform P&L")][0]
    bridge = {"Revenue": "Organic growth plus add-ons", "Gross profit before D&A": "Crew productivity, mix of specialty work, pricing on MSAs",
              "Operating SG&A (branch + business-unit)": "Branch overhead spread over more revenue", "Holdco cost (safety, finance, HR, ERP, M&A)": "Added once there are several companies",
              "Adjusted EBITDA": "Net of the above; comps at scale earn 8-10%", "Fleet net capex (estimate)": "Owned fleet at 3-4% of revenue",
              "Implied value at entry/exit multiple": "Multiples rise with scale; a permanent owner only realizes this by recapitalizing"}
    pl = []
    for i, row in enumerate(t["rows"]):
        line, a, ap, b, bp, c, cp = (row + [""] * 7)[:7]
        f = lambda v, p: (("$" + v + "M") if v and v[0].isdigit() else v) + (f" ({p}%)" if p and p not in ("100.0",) and p[0].isdigit() else "")
        pl.append(dict(id=f"pl{i}", order=i, line=line, s50=f(a, ap), s150=f(b, bp), s500=f(c, cp), drivers=bridge.get(line, "")))
    write(out, "pl", pl)
    t = [t for t in R["synergies"]["tables"] if t["title"].startswith("Synergy verdict")][0]
    vmap = {"Real (largest)": "Real", "Real": "Real", "Real but bounded": "Real", "Real where co-located": "Real", "Partial": "Partial", "Overstated": "Overstated"}
    write(out, "synergies", [dict(id=f"y{i}", order=i, lever=row[0], verdict=vmap.get(row[1], row[1]), quant=(row[2] + " bps of revenue" if row[2][:1].isdigit() or row[2].startswith("<") or row[2].startswith("~") else row[2]),
                                  evidence=row[3]) for i, row in enumerate(t["rows"])])

    # ---------- findings (all research findings + verification status) ----------
    status = {(v["domain"], v["id"]): v for v in r["verified"]["verdicts"]}
    findings = []
    for dom, res in R.items():
        for f in res["findings"]:
            v = status.get((dom, f["id"]))
            findings.append(dict(id=f"{dom}:{f['id']}"[:60], domain=dom.replace("_", " ").replace("cand ", "candidates: "), claim=clean(f["claim"]), value=clean(f.get("value")),
                                 as_of=clean(f.get("as_of")), source_name=clean(f.get("source_name")), source_url=https(f["source_url"]), confidence=f["confidence"],
                                 status=(v["status"] + (": " + clean(v.get("corrected_value")) if v and v.get("corrected_value") else "")) if v else ""))
    findings += [dict(id="check:caribou-1921", domain="asset age", claim="PG&E's Caribou-Palermo 115 kV line, whose worn hook started the 2018 Camp Fire, went into service in 1921; PG&E's ~50,000 transmission towers averaged 68 years old in 2017, the oldest pre-1910",
                      value="1921; 68 yrs", as_of="2019 reporting", source_name="GV Wire / KQED (citing WSJ and PG&E)", source_url="https://gvwire.com/2019/07/11/report-pge-ignored-repairs-on-aging-power-lines/", confidence="S", status="confirmed"),
                 dict(id="check:ppl-vintage", domain="asset age", claim="PPL Electric is rebuilding 230 kV lines dating from the mid-1920s to the 1930s under its Vintage Conductor program", value="~80-100 yrs",
                      as_of="PA PUC filing", source_name="Pennsylvania PUC filing", source_url="https://www.puc.pa.gov/pcdocs/1118448.pdf", confidence="P", status="confirmed")]
    write(out, "findings", findings)

    # ---------- candidates ----------
    cands = json.load(open(round2))["candidates"]
    rows = []
    seen = set()
    for c in cands:
        cid = slug(c.get("id") or c["name"], 30)
        while cid in seen:
            cid += "-x"
        seen.add(cid)
        cr = c.get("criteria") or {}
        fit = int(c.get("fit_score") or 0)
        web = https(c.get("website"))
        rec, avoid = cr.get("recurring_maintenance", "unknown"), cr.get("avoids_low_bid_fixed_price", "unknown")
        if not web:
            grade = "Lead"
        elif fit >= 4 and rec in ("yes", "partial") and avoid != "no":
            grade = "Platform"
        elif fit >= 3 or c.get("platform_or_addon") == "add-on":
            grade = "Add-on"
        else:
            grade = "Watch"
        hq = clean(c.get("hq"))
        hq_short = re.sub(r"\s*\([^)]*\)?", "", re.split(r";| per | - ", hq or "")[0]).strip(" ,.") if hq else ""
        rows.append(dict(id=cid, name=clean(c["name"]), website=web, hq=hq, hq_short=hq_short if 2 < len(hq_short) <= 40 and not re.match(r"(?i)not |unknown", hq_short) else "", unit=c["unit"], ownership=clean(c.get("ownership")), services=clean(c.get("services")),
                         customers=clean(c.get("customers")), size_hint=clean(c.get("size_hint")), recurring_evidence=clean(c.get("recurring_evidence")), red_flags=clean(c.get("red_flags")),
                         fit_score=fit, grade=grade, c_recurring=rec, c_customer=cr.get("large_regional_national_customer", "unknown"),
                         c_specialized=cr.get("specialized_labor_equipment", "unknown"), c_avoid=avoid, c_independent=cr.get("independent_available", "unknown"),
                         sources=" | ".join(u for u in (c.get("source_urls") or []) if https(u))))
    write(out, "candidates", rows)
    apply_round2(out, rows)

    # ---------- charts ----------
    meta, data = [], []

    def chart(cid, group, order, title, note, kind, fmt, source_url, conf, points, **kw):
        meta.append(dict(id=cid, group=group, order=order, title=title, note=note, kind=kind, fmt=fmt, source_url=source_url, confidence=conf, **kw))
        for i, p in enumerate(points):
            series, x, y = p[0], p[1], p[2]
            row = dict(id=f"{cid}-{i:02d}", chart_id=cid, order=i, series=series, x=x, y=y)
            if len(p) > 3 and p[3] is not None:
                row["label"] = p[3]
            if len(p) > 4 and p[4] is not None:
                row["note"] = p[4]
            if len(p) > 5 and p[5] is not None:
                row["y2"] = p[5]
            data.append(row)

    PHMSA_CI = "https://www.phmsa.dot.gov/data-and-statistics/pipeline-replacement/cast-and-wrought-iron-inventory"
    chart("ci_mains", "aging", 1, "Cast and wrought iron gas mains still in service",
          "Miles left in US gas distribution systems. The pace has slowed as the easiest miles were replaced; at ~1,000–1,500 miles a year the rest takes ~11–16 years.",
          "line", "int", PHMSA_CI, "P", [("Miles", "2013", 33619, None, "Congressional testimony citing PHMSA"), ("Miles", "2015", 27771, None, "PHMSA via Pipeline & Gas Journal"),
                                          ("Miles", "2021", 18314, None, "Federal Register, PHMSA leak rule"), ("Miles", "2022", 17010, None, "PHMSA via Pipeline & Gas Journal"),
                                          ("Miles", "2023", 16337, None, "PHMSA data cited in research")])
    chart("ci_states", "aging", 2, "Where the cast iron is left", "Cast and wrought iron gas mains by state, end of 2022. The Northeast and Michigan hold most of what remains.",
          "hbar", "int", PHMSA_CI, "P",
          [("Miles", "New Jersey", 2904), ("Miles", "New York", 2481), ("Miles", "Massachusetts", 2413), ("Miles", "Pennsylvania", 2259), ("Miles", "Michigan", 1616)])
    chart("power_age", "aging", 3, "Power assets: age against design life", "Years. Old does not mean failing: maintained wood poles outlive their book life, which is why inspection is recurring work.",
          "bar", "int", "https://www.eia.gov/todayinenergy/detail.php?id=50658", "P",
          [("Age", "Coal units", 45, "45 yrs", "Average age of operating coal units (EIA)"), ("Design or book life", "Coal units", 50, "~50", "Average retirement age"),
           ("Age", "Transformers", 39, "38–40", "Large power transformers, average age in 2014 (DOE)"), ("Design or book life", "Transformers", 40, "~40", "Large power transformer design life"),
           ("Age", "Wood poles", 75, "70–80+", "Maintained service life (NAWPC)"), ("Design or book life", "Wood poles", 35, "35", "Depreciation life")])
    chart("backlog_years", "aging", 4, "Years to clear the old stock at today's pace", "Derived from the backlog and the current replacement rate. Water mains are replaced on a ~125-year cycle while the average main fails at ~53 years, so that backlog grows.",
          "hbar", "int", "https://nrel.gov/docs/fy25osti/92076.pdf", "S",
          [("Years", "Cast iron gas mains", 13, "~11–16 yrs", "Cast and wrought iron gas mains"), ("Years", "Bare steel gas mains", 18, "~15–20 yrs"),
           ("Years", "Old transformers", 20, "~17–22 yrs", "Distribution transformers over 33 years old"), ("Years", "Lead service lines", 10, "~10 yrs", "If the Lead and Copper Rule Improvements hold"),
           ("Years", "Water mains", 125, "~125-yr cycle", "Full replacement cycle at today's pace")])
    chart("dwinsa", "aging", 5, "Drinking water: the $625B twenty-year need", "EPA's seventh needs survey, by category ($B over 20 years). Two-thirds is pipe in the ground.",
          "hbar", "usd_b", "https://asdwa.org/2023/09/07/epa-sends-7th-drinking-water-infrastructure-needs-report-to-congress", "P",
          [("$B", "Distribution and transmission", 420.8), ("$B", "Treatment", 106.4), ("$B", "Storage, source and other", 97.8)])
    chart("lsl", "aging", 6, "Lead service lines left", "Millions of lines. The 2025 count from utilities' actual inventories is less than half the 2023 model.",
          "hbar", "dec1", "https://www.epa.gov/system/files/documents/2025-11/fact-sheet-2025-7th-dwinsa-update.pdf", "P",
          [("Millions", "EPA model (2023)", 9.2, "9.2M"), ("Millions", "Utility inventories (2025)", 4.0, "~4.0M")])
    chart("water_breaks", "aging", 7, "Water mains: age and condition", "Miles of US and Canadian water main (Utah State University 2023 survey).",
          "hbar", "k", "https://www.asce.org/publications-and-news/civil-engineering-source/civil-engineering-magazine/article/2024/04/breaking-water-mains-present-us-canada-with-%24452b-problem", "S",
          [("Miles", "Over 50 years old", 770000, "~770k mi", "About 33% of all mains"), ("Miles", "Past useful life", 452000, "~452k mi", "Unfunded; about $452B to replace")])

    EIA = "https://www.eia.gov/outlooks/steo/archives/oct26.pdf"
    chart("elec_use", "demand", 1, "US electricity use is rising again", "Billion kWh. Retail sales (EIA Monthly Energy Review) and total end-use consumption including direct use (EIA STEO, Oct 2026). Use was roughly flat from 2015 to 2021 as efficiency offset growth.",
          "line", "int", EIA, "P",
          [("Retail sales", "2021", 3806), ("Retail sales", "2022", 3927), ("Retail sales", "2023", 3861), ("Retail sales", "2024", 3975),
           ("Total consumption", "2024", 4097), ("Total consumption", "2025", 4195), ("Total consumption", "2026F", 4288), ("Total consumption", "2027F", 4356)])
    chart("dc_use", "demand", 2, "Data centers are the swing factor", "TWh a year (LBNL for DOE, Dec 2024). The 2028 range is 6.7–12% of US electricity.",
          "bar", "int", "https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers", "P",
          [("TWh", "2014", 58), ("TWh", "2023", 176, "176 (4.4%)"), ("TWh", "2028 low", 325, "325 (6.7%)"), ("TWh", "2028 high", 580, "580 (12%)")])
    chart("eei_capex", "demand", 3, "Investor-owned utility capital spending", "$B a year (EEI). Replacement and hardening are a large share, and utilities recover it through their rates.",
          "bar", "dec1", "https://www.eei.org/News/news/All/electric-companies-to-invest-nearly-$208b-in-2025-to-strengthen-grid-and-drive-economic-growth", "P",
          [("$B", "2020", 139.8), ("$B", "2024", 178.2), ("$B", "2025E", 207.9), ("$B", "2025–29", 220, "~220+", "Average a year, 2025–29 plan")], fmt_unit="$B")
    chart("additions", "demand", 4, "New capacity additions: solar and batteries lead", "GW of utility-scale capacity (EIA). New plants bring operations and maintenance work, much of it kept by OEMs or owners.",
          "bar", "dec1", "https://www.eia.gov/todayinenergy/detail.php?id=67205", "P",
          [("2025 actual", "Solar", 27.2), ("2026 planned", "Solar", 43.4), ("2025 actual", "Batteries", 15, "~15"), ("2026 planned", "Batteries", 24.3),
           ("2025 actual", "All types", 53), ("2026 planned", "All types", 86)])
    chart("loadfc", "demand", 5, "Forecasts of five-year peak-load growth keep rising", "GW of added US peak demand forecast over five years, by report year (Grid Strategies). The 2024 figure is the headline; on FERC's basis it was 64–66 GW.",
          "bar", "int", "https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf", "S",
          [("GW", "2022", 24), ("GW", "2023", 38), ("GW", "2024", 128), ("GW", "2025", 166)])
    HEAT_OVERRIDE = {"Sun Belt": ("Some", 1), "SMRs": ("Later", 1), "PFAS": ("Treatment", 2)}
    dmap = {"Strong": 3, "Moderate": 2, "Partial": 2, "Indirect": 1, "Low": 1, "Neutral": 0, "Negative": 0, "Negligible": 0, "Yes": 3}
    t = [t for t in R["demand"]["tables"] if t["title"].startswith("Why-now driver scorecard")][0]
    pts = []
    for row in t["rows"]:
        drv, _, mag, mro, con, verdict = (row + [""] * 6)[:6]
        for col, txt in (("Maintenance and repair", mro), ("New construction", con)):
            key = next((k for k in dmap if txt.startswith(k)), None)
            lbl, val = next(((l, v) for k, (l, v) in HEAT_OVERRIDE.items() if txt.startswith(k)), (key, dmap.get(key, 1)))
            pts.append((drv, col, val, lbl or "Some", txt + " · " + verdict))
    chart("drivers", "demand", 6, "Who benefits from each why-now driver", "Darker means a stronger benefit. Most demand growth funds new construction; the drivers that favor maintenance are replacement capex, gas safety work, lead lines and nuclear life extension.",
          "heat", "int", "https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf", "S", pts, wide="Yes")

    chart("firms", "competition", 1, "How many utility-system construction firms are there?", "US firms in NAICS 2371 (Economic Census via NUCA). The count includes new construction and telecom, so the pool doing utility maintenance is smaller.",
          "bar", "int", "https://nuca.com/wp-content/uploads/2026/03/Fact-Sheet2026.pdf", "S", [("Firms", "2012", 25227), ("Firms", "2017", 18877)])
    chart("estabs", "competition", 2, "Establishments by sub-industry", "Business locations by NAICS code from secondary compilations of Census data; directional only (W). Water and sewer line work is the most fragmented.",
          "hbar", "int", "https://plainbizbench.com/industry/237130/", "W",
          [("Establishments", "Water and sewer", 10818, None, "NAICS 237110 water and sewer line construction"), ("Establishments", "Power and comms lines", 7112, None, "NAICS 237130 power and communication line construction"), ("Establishments", "Oil and gas pipelines", 2172, None, "NAICS 237120 oil and gas pipeline construction")])
    chart("scaled_rev", "competition", 3, "The scaled players by revenue", "$B, latest fiscal year. Fifteen to twenty companies operate at or near $1B, well above the deck's 'fewer than ten'.",
          "hbar", "usd_b", "https://www.sec.gov/Archives/edgar/data/1050915/000119312526058069/d101511dex991.htm", "P",
          [("Revenue", s_["company"], s_["revenue_usd_b"], None) for s_ in sorted([x for x in scaled if x["revenue_usd_b"]], key=lambda x: -x["revenue_usd_b"])], height=420)
    crowd = [t for t in R["precedents"]["tables"] if t["title"].startswith("Crowding map")][0]
    chart("crowding", "competition", 4, "Scaled consolidators already in each unit", "Named public and sponsor-backed consolidators per sub-segment (examples, not a census).",
          "hbar", "int", "https://www.sec.gov/Archives/edgar/data/1981599/000198159926000017/centuriholdingsincex-991xq.htm", "S",
          [("Count", lbl, int(row[3]), None, row[1]) for lbl, row in zip(["Natural gas", "Power generation", "T&D", "Water"], crowd["rows"])])
    chart("exits", "competition", 5, "Exits, recaps and failures", "Disclosed or reported deal values ($M, log scale). Specialists sold for the most; diversified roll-ups failed.",
          "hbar", "usd_m", "https://www.blackstone.com/news/press/blackstone-announces-agreement-to-acquire-shermco-for-approximately-1-6-billion/", "S",
          [("Exit", "Pike, 2025", 5000, ">$5,000M", "Reported value including debt"), ("Exit", "Shermco, 2025", 1600, "~$1,600M", "Blackstone acquisition"), ("Exit", "IEA, 2022", 1100, "~$1,100M", "Sold to MasTec"),
           ("Exit", "Aegion, 2021", 963, None, "Take-private"), ("Platform formed", "Artera, 2020", 850, None, "Artera buys Miller Pipeline and Minnesota Limited"), ("Exit", "Utility Service Co, 2008", 220, None, "Sale of the water-tank maintenance business"),
           ("Exit", "Vortex, 2023", 160, "~$160M", "Unconfirmed"), ("Failure", "Williams Industrial, 2023", 60, None, "Asset sale after restructuring")], log_x="Yes")
    outc = {}
    for p in R["precedents"]["platforms"]:
        outc[p["outcome"]] = outc.get(p["outcome"], 0) + 1
    chart("outcomes", "competition", 6, "How the precedent platforms turned out", "Count of the platforms profiled in this report, by outcome.",
          "hbar", "int", "https://www.sec.gov/Archives/edgar/data/1981599/000198159926000017/centuriholdingsincex-991xq.htm", "S",
          [("Platforms", lbl, outc.get(k, 0)) for k, lbl in [("thriving", "Thriving"), ("solid", "Solid"), ("mixed", "Mixed"), ("struggling", "Struggling"), ("failed/restructured", "Failed"), ("exited", "Exited")] if outc.get(k)])

    chart("tam", "economics", 1, "Addressable outsourced maintenance market by unit", "$B a year, low to high estimate. Hover for the basis: utility spend pools multiplied by the share contractors capture.",
          "range", "usd_b", "https://www.aga.org/safety", "S",
          [("TAM", "T&D and electrical", 20, "$20–35B", "Distribution capex $50.9B + transmission $32.6B + O&M; replacement share x contractor share", 35),
           ("TAM", "Natural gas", 12, "$12–20B", "AGA ~$33–37B a year of safety spend x 35–55% contractor share", 20),
           ("TAM", "Water and wastewater", 8, "$8–18B", "20–30% of ~$45–55B capex plus 2–4% of O&M", 18),
           ("TAM", "Power generation maintenance", 4, "$4–8B", "~$13B plant maintenance (EIA $/MWh x generation) x 30–60% outsourced", 8)])
    chart("comps", "economics", 2, "Margins do not rise with size", "Adjusted EBITDA margin against revenue (FY2025, log scale). Margin follows service mix and owned specialty equipment, not scale.",
          "scatter", "pct1", "https://www.sec.gov/Archives/edgar/data/1050915/000119312526058069/d101511dex991.htm", "P",
          [("MRO-heavy", 0.72, 12.6, "Mistras"), ("MRO-heavy", 0.90, 6.8, "Team"), ("MRO-heavy", 2.98, 8.3, "Centuri"), ("Mixed or specialty", 0.41, 4.2, "ESOA"),
           ("Mixed or specialty", 0.83, 23.8, "Badger"), ("Construction-heavy", 7.71, 6.9, "Primoris"), ("Construction-heavy", 14.3, 8.0, "MasTec"), ("Construction-heavy", 28.48, 10.1, "Quanta")],
          log_x="Yes", x_fmt="usd_b", x_title="Revenue, $B (log)", height=320)
    chart("swings", "economics", 3, "Even maintenance-heavy margins swing with execution", "Gross or segment margin, FY2024 against FY2025 (%).",
          "bar", "pct1", "https://investor.myrgroup.com/node/16096", "P",
          [("FY2024", "MYR gross", 8.6), ("FY2025", "MYR gross", 11.6), ("FY2024", "Centuri base gross", 6.9), ("FY2025", "Centuri base gross", 8.0),
           ("FY2024", "MasTec Pipeline", 18.3), ("FY2025", "MasTec Pipeline", 14.9), ("FY2024", "Primoris Utilities", 10.6), ("FY2025", "Primoris Utilities", 11.5)])
    chart("bridge", "economics", 4, "EBITDA margin from $50M to $500M of revenue", "Percentage points, estimate. Overhead leverage and purchasing roughly cancel the cost of a holding company and integration: about +0.3 points net.",
          "hbar", "dec1", "https://www.businesswire.com/news/home/20260225110463/en", "S",
          [("pts", "Holdco and standalone costs", -1.2), ("pts", "Integration, mix and wage alignment", -0.7), ("pts", "Materials and equipment purchasing", 0.4),
           ("pts", "Equipment utilization", 0.4), ("pts", "Insurance, EMR and benefits pooling", 0.4), ("pts", "Overhead leverage", 1.0)])
    chart("multiples", "economics", 5, "What these businesses sell for", "EV/EBITDA. Small private deals trade at 6–8x; scaled utility-services companies at 11–16x. Lower-middle-market figures cover all industries (W).",
          "hbar", "dec1", "https://capitalpad.com/lower-middle-market-ebitda-multiples/", "W",
          [("x", "Private deals, $10–25M EV", 6.4), ("x", "Private deals, $25–50M EV", 6.8), ("x", "Private deals, $50–100M EV", 8.3),
           ("x", "Centuri at IPO (est.)", 11.5, "~11–12x"), ("x", "Engineering and services sector, 2025", 13.2), ("x", "Public utility-services peers, median", 15.2)])

    def heat_from(table_title, domain, cid, title, note, src):
        t = [t for t in R["synergies"]["tables"] if t["title"].startswith(table_title)][0]
        cols = ["Gas", "Water", "T&D", "Power-gen"]
        pts = []
        for row in t["rows"]:
            for j, col in enumerate(cols):
                v = row[j + 1]
                if row[0] == col:
                    continue
                m = re.findall(r"\d+", v)
                val = int(m[-1]) if m else None
                pts.append((row[0], col, val, f"{val}%" if val is not None else "", ("raw / movable: " + v + "%") if "/" in v else None))
        chart(cid, "synergies", 1 if cid == "people" else 2, title, note, "heat", "pct", src, "S", pts, x_order="Gas|Water|T&D|Power-gen", y_order="Gas|Water|T&D|Power-gen")
    heat_from("Workforce overlap matrix", "synergies", "people", "Field headcount that can move between units",
              "Share of each unit's field workforce in occupations that can work in the other unit (estimate built on BLS occupation data). Gas and water are the only real pair.", "https://www.bls.gov/oes/2023/may/naics4_237100.htm")
    heat_from("Equipment overlap matrix", "synergies", "fleet", "Fleet value usable by the other unit",
              "Share of fleet value (estimate). Trucks and excavators move; bucket trucks, CCTV and lining rigs, leak-survey and NDE gear do not.", "https://protips.vermeer.com/underground/2026/09/07/potholing-best-practices-daylighting-buried-utilities-with-a-vacuum-excavator/")
    t = [t for t in R["synergies"]["tables"] if t["title"].startswith("Estimated field-workforce mix")][0]
    groups = {"Laborers, operators and drivers": [0, 1, 2], "Pipe trades and welders": [3], "Lineworkers": [4], "Electricians and testers": [5],
              "Plant crafts and NDE": [6], "Water specialists": [7], "Supervisors and other": [8, 9]}
    units = [("Gas", 1), ("Water", 2), ("T&D", 3), ("Power-gen", 4)]
    pts = []
    for g, idx in groups.items():
        for u, col in units:
            pts.append((g, u, sum(float(t["rows"][i][col]) for i in idx)))
    chart("mix", "synergies", 3, "What each unit's field workforce does", "Share of field headcount by occupation group (%, estimate on BLS anchors). Lineworkers, plant crafts and water specialists are not interchangeable.",
          "stack", "pct", "https://www.bls.gov/oes/2023/may/naics4_237100.htm", "S", pts)
    chart("syn_bps", "synergies", 4, "What each synergy is worth", "Basis points of revenue, low to high (estimate). Density inside a unit is worth the most; crews flexing across units is worth the least.",
          "range", "int", "https://www.sec.gov/Archives/edgar/data/1981599/000198159925000008/ctri-20241229.htm", "S",
          [("bps", "Density and wallet share in one unit", 100, "100–300", None, 300), ("bps", "Purchasing", 50, "50–150", None, 150), ("bps", "Back office, safety, records", 50, "50–100", None, 100),
           ("bps", "Insurance and benefits", 30, "30–100", None, 100), ("bps", "Shared fleet shops", 20, "20–50", None, 50), ("bps", "Crews flexing across units", 0, "<50", None, 50),
           ("bps", "Specialized assets across units", 0, "~0", None, 2)])

    # candidate counts (from the candidate rows themselves)
    pts = []
    for u, lbl in [("gas", "Natural gas"), ("power-gen", "Power generation"), ("T&D", "T&D"), ("water", "Water")]:
        us = [c for c in rows if c["unit"] == u]
        pts += [("Listed", lbl, len(us)), ("Platform-grade", lbl, sum(1 for c in us if c["grade"] == "Platform")),
                ("Platform-grade and independent", lbl, sum(1 for c in us if c["grade"] == "Platform" and c["c_independent"] == "yes")),
                ("Sponsor or strategic owned", lbl, sum(1 for c in us if c["c_independent"] == "no"))]
    chart("cand_counts", "candidates", 1, "Candidates by unit", "Counts from the candidate list below. Platform-grade means fit 4 or 5, recurring maintenance and not dependent on low bids; independent means confirmed as not owned by a sponsor or strategic.",
          "bar", "int", "https://directory.dcaweb.org/", "S", pts, wide="Yes")
    write(out, "chart_meta", meta)
    write(out, "charts", data)

    # ---------- tiles ----------
    figs = [
        ("report_window", "header", 0, "Prepared Oct 29, 2026 · federal data, filings, dockets and trade sources", "", "", "", "", "", ""),
        ("ci_left", "market", 1, "Cast iron gas mains still in service (2023)", 16337, "mi", "", "Down 63% since 2005; ~1,000–1,500 miles replaced a year", PHMSA_CI, "P"),
        ("pre1970", "market", 2, "Gas distribution pipe installed before 1970", 28, "%", "", "PHMSA (2021); the deck's 25% is close", "https://primis-meetings.phmsa.dot.gov/archive/Agenda_9_PAC_Pipeline_Industry_Performance_10202021.pdf", "P"),
        ("dt_old", "market", 3, "Distribution transformers older than 33 years", "50–55", "%", "", "Of 60–80 million units; replacements plus additions run 2.5–3% a year", "https://nrel.gov/docs/fy25osti/92076.pdf", "P"),
        ("towers", "market", 4, "PG&E transmission towers, average age (2017)", 68, "yrs", "", "The Camp Fire line dates to 1921; the oldest towers predate 1910", "https://gvwire.com/2019/07/11/report-pge-ignored-repairs-on-aging-power-lines/", "S"),
        ("breaks", "market", 5, "Water main breaks a year (US and Canada)", "~260k", "", "", "11.1 per 100 miles; ~$2.6B of repairs", "https://www.asce.org/publications-and-news/civil-engineering-source/civil-engineering-magazine/article/2024/04/breaking-water-mains-present-us-canada-with-%24452b-problem", "S"),
        ("lsl", "market", 6, "Lead service lines left", "~4.0", "M", "", "EPA's 2025 count, down from a 9.2M model", "https://www.epa.gov/system/files/documents/2025-11/fact-sheet-2025-7th-dwinsa-update.pdf", "P"),
        ("elec", "market", 7, "US electricity use, 2027 forecast", 4356, "BkWh", "", "Record 4,195 in 2025 (EIA STEO, Oct 2026)", EIA, "P"),
        ("pop", "market", 8, "US population growth, 2025", 0.5, "%", "", "Slowest since 2021; net migration fell from 2.7M to 1.3M", "https://census.gov/newsroom/press-releases/2026/population-growth-slows.html", "P"),
        ("capex", "market", 9, "Investor-owned utility capex, 2025", 207.9, "B", "$", "From $139.8B in 2020; >$1.1T planned for 2025–29", "https://www.eei.org/News/news/All/electric-companies-to-invest-nearly-$208b-in-2025-to-strengthen-grid-and-drive-economic-growth", "P"),
        ("firms", "market", 10, "Utility-system construction firms (2017)", 18877, "", "", "25,227 in 2012; includes new construction and telecom", "https://nuca.com/wp-content/uploads/2026/03/Fact-Sheet2026.pdf", "S"),
    ]
    write(out, "figures", [dict(id=f[0], tab=f[1], order=f[2], label=f[3], value=f[4], unit=f[5], prefix=f[6], note=f[7], source_url=f[8], confidence=f[9]) for f in figs])

    # ---------- glossary ----------
    gl, gids, taken = [], set(), set()
    for t_ in r["glossary"]["terms"]:
        gid = slug(t_.get("id") or t_["term"])
        if gid in gids:
            continue
        gids.add(gid)
        aliases = []
        for a in [t_["term"].split(" (")[0]] + list(t_.get("aliases") or []):
            a = str(a).strip()
            key = a if t_.get("case_sensitive") else a.lower()
            if len(a) > 1 and a not in aliases and a not in DROP_ALIASES and key not in taken:
                aliases.append(a)
                taken.add(key)
        gl.append(dict(id=gid, term=t_["term"].strip(), aliases=" | ".join(aliases), case_sensitive=bool(t_.get("case_sensitive")), category=t_["category"], definition=clean(t_["definition"])))
    gl.sort(key=lambda x: x["term"].lower())
    write(out, "glossary", gl)

    # ---------- value chain ----------
    net = r["network"]
    groups = net.get("builder_groups") or []
    nodes, seen_n = [], set()
    for n in net["nodes"]:
        if n["id"] in seen_n:
            continue
        seen_n.add(n["id"])
        g = n.get("group") or ""
        nodes.append(dict(id=n["id"], name=clean(n["name"]), layer=n["layer"], group=g, group_order=groups.index(g) if n["layer"] == "B" and g in groups else None,
                          kind=n.get("kind", "company"), description=clean(n.get("description")), size_label=clean(n.get("size_label")), ownership=clean(n.get("ownership")),
                          source_url=https(n.get("source_url"))))
    nodes.append(dict(E.PROSPECT_NODE))
    net_edges = [e for e in net["edges"] if e.get("kind") != "fulton_opportunity"]
    for k, (src_, tgt, prod, lo, hi, basis, url) in enumerate(E.PROSPECT_EDGES):
        net_edges.append(dict(id=f"p{k:02d}", source=src_, target=tgt, product=prod, value_low_usd_m=lo, value_high_usd_m=hi,
                              value_label="$%s-%sM/yr (est.)" % (lo, hi), estimated=True, kind="prospect", basis=basis, source_url=url))
    for k, (src_, tgt, prod, lo, hi, basis) in enumerate(E.FULTON_EDGES):
        net_edges.append(dict(id=f"fs{k:02d}", source=src_, target=tgt, product=prod, value_low_usd_m=lo, value_high_usd_m=hi,
                              value_label="$%s-%sM/yr (est.)" % (lo, hi), estimated=True, kind="fulton_synergy", basis=basis, source_url=""))
    ids = {n["id"] for n in nodes}
    edges, eids = [], set()
    for i, e in enumerate(net_edges):
        if e["source"] not in ids or e["target"] not in ids or e["source"] == e["target"]:
            continue
        eid = e.get("id") or f"e{i:03d}"
        while eid in eids:
            eid += "x"
        eids.add(eid)
        edges.append(dict(id=eid, source=e["source"], target=e["target"], product=clean(e["product"]), value_low_usd_m=e.get("value_low_usd_m"), value_high_usd_m=e.get("value_high_usd_m"),
                          value_label=clean(e.get("value_label")), estimated="Yes" if e.get("estimated", True) else "No", kind=e.get("kind", "flow"), basis=clean(e.get("basis")), source_url=https(e.get("source_url"))))
    used = {e["source"] for e in edges} | {e["target"] for e in edges}
    nodes = [n for n in nodes if n["id"] in used]
    write(out, "value_chain_nodes", nodes)
    write(out, "value_chain_edges", edges)
    with open(os.path.join(os.path.dirname(os.path.abspath(src)), "..", "dashboard", "layer_titles.json"), "w") as f:
        json.dump(net["layer_titles"], f)
    apply_text_edits(out)


if __name__ == "__main__":
    main(*sys.argv[1:4])
