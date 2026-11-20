"""Build the wireless-spectrum dashboard datasets from the research, verification, forecasting and synthesis results.

Usage: python3 -I build_spectrum.py <research dir> <out dir>
Reads, from <research dir>:
  workflow_result.json  nine research domains (findings, chart data points, records)
  verification.json     independent re-checks of the 102 key claims
  forecasts.json        five forecasting lenses, their aggregate and the chief forecaster's final numbers and scenarios
  map.json              market map nodes and flows
  glossary.json         glossary terms
  synthesis.json        key findings, key numbers, watchlist and the curated list of listed companies and funds
Report wording that is not data (verdict, method, caveats, tiles, chart titles and notes) lives in editorial.py.
Writes one JSON file per dataset into <out dir> and dashboard/layer_titles.json.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editorial as E  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
POPS = 335e6


def clean(t):
    t = str(t if t is not None else "").replace("**", "").replace("&amp;", "&")
    t = re.sub(r"(^|\n)\s*[-*]\s+", r"\1• ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def https(u):
    u = str(u or "").strip()
    return u if u.startswith("https://") else ""


def slug(s, n=40):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:n]


def numf(v):
    """First number in a value ('$23.0B' -> 23.0, '~0.94 (x)' -> 0.94, '<0.01' -> 0.01); None if there is none."""
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    m = re.search(r"-?\d[\d,]*\.?\d*", str(v))
    if not m:
        return None
    try:
        return float(m.group(0).replace(",", ""))
    except ValueError:
        return None


def write(out, name, rows):
    with open(os.path.join(out, name + ".json"), "w") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print("%-20s %d" % (name, len(rows)))


def load(path, default=None):
    return json.load(open(path)) if os.path.exists(path) else default


def sources(*urls):
    seen = []
    for u in urls:
        for x in (u if isinstance(u, list) else [u]):
            x = https(x)
            if x and x not in seen:
                seen.append(x)
    return " | ".join(seen)


# ---------------------------------------------------------------- findings and verification
def build_findings(R, V):
    verdict = {v["id"]: v for v in V.get("verdicts", [])}
    label = {"confirmed": "Confirmed", "corrected": "Corrected", "refuted": "Refuted", "unverified": "Not independently checked"}
    rows = []
    for dom, r in R.items():
        for f in r.get("findings", []):
            fid = dom + ":" + f["id"]
            v = verdict.get(fid)
            claim, value, url = clean(f.get("claim")), clean(f.get("value")), https(f.get("source_url"))
            status = ""
            if v:
                status = label.get(v["verdict"], "")
                if v["verdict"] == "corrected":
                    claim = clean(v.get("corrected_claim")) or claim
                    value = clean(v.get("corrected_value")) or value
                if v.get("note"):
                    status += ": " + clean(v["note"])
            elif not f.get("key"):
                status = ""
            if v and v["verdict"] == "refuted":
                continue
            rows.append(dict(id=fid, domain=E.DOMAIN_LABEL.get(dom, dom), claim=claim, value=value, as_of=clean(f.get("as_of")),
                             source_name=clean(f.get("source_name")), source_url=url, confidence=f.get("confidence", ""), status=status))
    return rows


# ---------------------------------------------------------------- charts
def build_charts(R, F):
    meta, data = [], []

    def dp(domain, chart):
        return [p for p in R[domain].get("datapoints", []) if p.get("chart") == chart]

    for spec in E.CHARTS:
        pts = []
        if "build" in spec:
            pts = spec["build"](R)
        elif "points" in spec:
            pts = [dict(series=s, x=x, y=y, note=n) for s, x, y, n in spec["points"]]
        else:
            src = dp(spec["domain"], spec["from"])
            for p in src:
                if spec.get("keep") and not spec["keep"](p):
                    continue
                q = dict(series=spec.get("series_map", {}).get(p["series"], p["series"]), x=spec.get("x_map", {}).get(p["x"], p["x"]),
                         y=p["y"], note=clean(p.get("note")))
                pts.append(q)
        if spec.get("build_after"):
            pts = spec["build_after"](pts)
        for p in pts:
            if p["x"] in spec.get("overrides", {}):
                p["y"] = spec["overrides"][p["x"]]
        if spec.get("from_forecast"):
            pts = spec["from_forecast"](F, pts)
        if spec.get("swap"):
            pts = [dict(series=p["x"], x=p["series"], y=p["y"], note=p.get("note")) for p in pts]
        if "x_order" in spec:
            order = spec["x_order"]
            pts = [p for p in pts if p["x"] in order]
            pts.sort(key=lambda p: (order.index(p["x"]), p["series"]))
        cid = spec["id"]
        m = dict(id=cid, group=spec["group"], order=spec["order"], title=spec["title"], note=spec["note"], kind=spec["kind"], fmt=spec["fmt"],
                 source_url=spec["source_url"], confidence=spec["confidence"])
        for k in ("log_x", "x_fmt", "x_title", "height", "wide", "highlight"):
            if k in spec:
                m[k] = spec[k]
        meta.append(m)
        for i, p in enumerate(pts):
            row = dict(id="%s-%02d" % (cid, i), chart_id=cid, order=i, series=p["series"], x=str(p["x"]), y=p["y"])
            if p.get("label"):
                row["label"] = p["label"]
            if p.get("note"):
                row["note"] = p["note"]
            data.append(row)
    return meta, data


# ---------------------------------------------------------------- deals (auctions and private sales)
def build_deals(R):
    rows = []
    for r in R["prices"].get("records", []):
        name = clean(r.get("name"))
        if name in E.DEAL_SKIP:
            continue
        kind = "Auction" if r.get("kind") == "auction" else "Private sale"
        date = clean(r.get("date"))
        m = re.match(r"(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", date)
        sort_date = "-".join([m.group(1), m.group(2) or "06", m.group(3) or "15"]) if m else "9999"
        price = numf(r.get("price_usd_b"))
        ppm = numf(r.get("usd_per_mhz_pop"))
        if ppm is not None and ("n/a" in str(r.get("usd_per_mhz_pop")) or ppm > 20):
            ppm = None
        raw_price = clean(r.get("price_usd_b"))

        def fmt_b(v):
            return "$%gM" % round(v * 1000, 1) if v < 0.1 else "$%gB" % round(v, 2)
        if price is None:
            label = raw_price
        elif re.match(r"~?\d[\d.]*\s*[-–]\s*\d", raw_price):
            label = "$" + re.match(r"~?([\d.]+\s*[-–]\s*[\d.]+)", raw_price).group(1).replace(" ", "") + "B"
        elif raw_price.startswith("~"):
            label = "~" + fmt_b(price)
        else:
            label = fmt_b(price)
        rows.append(dict(id=slug(name, 48), kind=kind, name=E.DEAL_RENAME.get(name, name), date=date.split(" (")[0], sort_date=sort_date,
                         buyer=clean(r.get("buyer")), seller=clean(r.get("seller")), band=clean(r.get("band")), band_class=clean(r.get("band_class")),
                         mhz=clean(r.get("mhz")), price_usd_b=price, price_label=label, usd_per_mhz_pop=round(ppm, 3) if ppm is not None else None,
                         status=clean(r.get("status")), notes=clean(r.get("notes")), source_url=https(r.get("source_url"))))
    return rows


# ---------------------------------------------------------------- pipeline and rules
def build_pipeline(R):
    rows = []
    for i, r in enumerate(R["supply"].get("records", [])):
        if r.get("kind") not in ("pipeline", "rule"):
            continue
        rows.append(dict(id=slug(r.get("entity", "") + "-" + r.get("band", ""), 48), order=i, kind="Pipeline" if r["kind"] == "pipeline" else "Rule",
                         band=clean(r.get("band")) + (" (" + clean(r.get("entity")) + ")" if r["kind"] == "rule" else ""),
                         mhz=clean(r.get("mhz")), timing=clean(r.get("timing")), status=clean(r.get("status")), notes=clean(r.get("notes")),
                         source_url=https(r.get("source_url"))))
    return rows


# ---------------------------------------------------------------- precedents
def build_precedents(R):
    rows = []
    for i, r in enumerate(R["precedents"].get("records", [])):
        o = str(r.get("outcome", ""))
        outcome = "Won" if o.startswith("Won") else "Lost" if o.startswith("Lost") else "Mixed"
        rows.append(dict(id=slug(r.get("name"), 48), order=i, name=clean(r.get("name")), period=clean(r.get("period")), holder=clean(r.get("holder")),
                         spectrum=clean(r.get("spectrum")), cost_basis=clean(r.get("cost_basis")), outcome_value=clean(r.get("outcome_value")),
                         multiple="" if clean(r.get("multiple")).startswith("n/a") else clean(r.get("multiple")), outcome=outcome,
                         years=clean(r.get("years_held")), lesson=clean(r.get("lesson")), sources=sources(r.get("source_url"))))
    return rows


# ---------------------------------------------------------------- direct-to-device players
def build_players(R):
    rows = []
    for i, r in enumerate(R["satellite"].get("records", [])):
        name = clean(r.get("name"))
        if name in E.PLAYER_SKIP:
            continue
        st = clean(r.get("service_status"))
        stage = "In service" if re.search(r"[Cc]ommercial|[Pp]owers|since", st) and not re.search(r"planned|targeted before", st) else "Testing" if re.search(r"target|[Ii]ntermittent|trial|beta", st) else "Planned"
        rows.append(dict(id=slug(name, 40), order=i, name=name, owner=clean(r.get("owner_or_ticker")), stage=E.PLAYER_STAGE.get(name, stage),
                         spectrum=clean(r.get("spectrum")) + (" (" + clean(r.get("mhz")) + " MHz)" if r.get("mhz") and not re.search(r"MHz", str(r.get("spectrum"))) else ""),
                         partners=clean(r.get("partners")), satellites=clean(r.get("satellites")), status=st, capacity=clean(r.get("capacity_notes")),
                         value=clean(r.get("funding_or_value")), sources=sources(r.get("source_url"))))
    return rows


# ---------------------------------------------------------------- forecasts, panel, probabilities, scenarios
def build_forecasts(Fq, F):
    chief = F.get("chief") or {}
    cf = {x["id"]: x for x in chief.get("forecasts", [])}
    cp = {x["id"]: x for x in chief.get("probabilities", [])}
    agg_p = {x["id"]: x for x in (F.get("aggregate") or {}).get("probabilities", [])}
    lens_name = {p["lens"]: p.get("lens_name", p["lens"]) for p in F.get("panel", [])}
    forecasts, probs, panel = [], [], []
    for i, q in enumerate(Fq):
        if q["kind"] == "quantile":
            c = cf.get(q["id"], {})
            forecasts.append(dict(id=q["id"], group=q["group"], order=i, headline=q.get("headline", ""), short=q["short"], question=q["question"],
                                  unit=q["unit"], fmt=q["fmt"], current=q.get("current"), current_label=q.get("current_label", ""),
                                  p10=E.rnd(c.get("p10")), p50=E.rnd(c.get("p50")), p90=E.rnd(c.get("p90")), horizon=q["horizon"], log=q.get("log", ""),
                                  rationale=clean(c.get("rationale")), drivers_up=clean(c.get("drivers_up")), drivers_down=clean(c.get("drivers_down")),
                                  base_rate=clean(c.get("base_rate")), signposts=clean(c.get("signposts")), sources=E.FORECAST_SOURCES.get(q["id"], "")))
        else:
            c, a = cp.get(q["id"], {}), agg_p.get(q["id"], {})
            probs.append(dict(id=q["id"], order=i, group=q["group"], question=q["question"], horizon=q["horizon"], probability=int(round(c.get("probability"))) if c.get("probability") is not None else None,
                              low=a.get("low"), high=a.get("high"), rationale=clean(c.get("rationale")), resolution=q.get("resolution", ""),
                              signposts=clean(c.get("signposts"))))
    for p in F.get("panel", []):
        for f in p.get("forecasts", []):
            panel.append(dict(id=p["lens"] + ":" + f["id"], forecast_id=f["id"], lens=lens_name[p["lens"]], p10=E.rnd(f.get("p10")), p50=E.rnd(f.get("p50")),
                              p90=E.rnd(f.get("p90")), note=clean(f.get("rationale"))))
        for b in p.get("probabilities", []):
            panel.append(dict(id=p["lens"] + ":" + b["id"], forecast_id=b["id"], lens=lens_name[p["lens"]], p10=None, p50=int(round(b["probability"])),
                              p90=None, note=clean(b.get("rationale"))))
    scen = []
    for i, s in enumerate(chief.get("scenarios", [])):
        scen.append(dict(id=s["id"], order=i, name=clean(s["name"]), probability=s["probability"], tagline=clean(s["tagline"]), summary=clean(s["summary"]),
                         spectrum_prices=clean(s["spectrum_prices"]), carriers=clean(s["carriers"]), satellites=clean(s["satellites"]),
                         investors=clean(s["investors"]), signposts=clean(s["signposts"])))
    return forecasts, probs, panel, scen


# ---------------------------------------------------------------- market map
def build_map(M):
    net = M["network"]
    nodes = []
    for n in net["nodes"]:
        nodes.append(dict(id=n["id"], name=clean(n["name"]), layer=n["layer"], group=clean(n["group"]), group_order=n.get("group_order"),
                          kind=n["kind"], description=clean(n["description"]), size_label=clean(n.get("size_label")), ownership=clean(n.get("ownership")),
                          source_url=https(n.get("source_url"))))
    ids = {n["id"] for n in nodes}
    edges = []
    for i, e in enumerate(net["edges"]):
        if e["source"] not in ids or e["target"] not in ids or e["source"] == e["target"]:
            print("  dropped edge", e["id"], e["source"], e["target"])
            continue
        edges.append(dict(id=e["id"] if e.get("id") else "e%d" % i, source=e["source"], target=e["target"], product=clean(e["product"]),
                          value_low_usd_m=e["value_low_usd_m"], value_high_usd_m=e["value_high_usd_m"], value_label=clean(e["value_label"]),
                          estimated=e["estimated"], kind=e["kind"], basis=clean(e["basis"]), source_url=https(e.get("source_url"))))
    ids_used = {e["source"] for e in edges} | {e["target"] for e in edges}
    nodes = [n for n in nodes if n["id"] in ids_used]
    return nodes, edges, net.get("layer_titles")


def build_universe(U):
    rows = []
    for u in U:
        u = dict(u)
        full = clean(u.get("spectrum_pct_ev"))
        short = re.split(r"\s*[(;,]|\s+on\s", full)[0].strip()
        u["spectrum_basis"] = full if full != short else ""
        u["spectrum_pct_ev"] = short
        mc, r1 = clean(u.get("market_cap_label")), clean(u.get("return_1y"))
        notes = []
        if mc:
            notes.append("market cap " + mc)
        if r1:
            notes.append("return " + r1)
        u["market_note"] = "; ".join(notes)
        u["market_cap_label"] = re.sub(r"\s*\(.*?\)", "", mc).strip()
        u["return_1y"] = re.sub(r"\s*\(.*?\)", "", r1).strip()
        for k in ("holdings", "benefits_if", "loses_if", "risks", "scenario_view"):
            u[k] = clean(u.get(k))
        u["website"] = https(u.get("website"))
        u["sources"] = sources([x.strip() for x in str(u.get("sources", "")).split("|")])
        rows.append(u)
    return rows


def build_glossary(G):
    rows, seen = [], set()
    for t in G["terms"]:
        if t["id"] in seen or t["id"] in E.GLOSSARY_SKIP:
            continue
        seen.add(t["id"])
        aliases = [a.strip() for a in str(t.get("aliases", "")).split("|") if a.strip() and a.strip() not in E.DROP_ALIASES]
        rows.append(dict(id=t["id"], term=clean(t["term"]), aliases=" | ".join(aliases), case_sensitive=bool(t.get("case_sensitive")),
                         category=t["category"], definition=clean(t["definition"])))
    return rows


def main(src, out):
    os.makedirs(out, exist_ok=True)
    R = load(os.path.join(src, "workflow_result.json"))["research"]
    V = load(os.path.join(src, "verification.json"), {})
    F = load(os.path.join(src, "forecasts.json"), {})
    Fq = load(os.path.join(src, "forecast_questions.json"), [])
    M = load(os.path.join(src, "map.json"), None)
    G = load(os.path.join(src, "glossary.json"))
    S = load(os.path.join(src, "synthesis.json"), {})

    write(out, "findings", build_findings(R, V))
    meta, data = build_charts(R, F)
    write(out, "chart_meta", meta)
    write(out, "charts", data)
    write(out, "deals", build_deals(R))
    write(out, "pipeline", build_pipeline(R))
    write(out, "precedents", build_precedents(R))
    write(out, "d2d_players", build_players(R))
    fc, pr, pn, sc = build_forecasts(Fq, F)
    write(out, "forecasts", fc)
    write(out, "probabilities", pr)
    write(out, "forecast_panel", pn)
    write(out, "scenarios", sc)
    if M:
        nodes, edges, titles = build_map(M)
        write(out, "value_chain_nodes", nodes)
        write(out, "value_chain_edges", edges)
        if titles and len(titles) == 7:
            json.dump(titles, open(os.path.join(HERE, "dashboard", "layer_titles.json"), "w"))
    write(out, "glossary", build_glossary(G))
    write(out, "figures", E.figures())
    write(out, "plan", E.plan(fc, pr, sc))
    write(out, "key_findings", S.get("key_findings", []))
    write(out, "key_numbers", S.get("key_numbers", []))
    write(out, "watchlist", S.get("watchlist", []))
    write(out, "universe", build_universe(S.get("universe", [])))
    apply_edits(out)


def apply_edits(out):
    """Apply editorial.EDITS (text replacements) and editorial.SETS (field values) to the written datasets."""
    cache = {}

    def rows(name):
        if name not in cache:
            cache[name] = json.load(open(os.path.join(out, name + ".json")))
        return cache[name]

    def row(name, rid):
        r = next((x for x in rows(name) if x.get("id") == rid), None)
        assert r is not None, (name, rid)
        return r
    for name, rid, field, old, new in E.EDITS:
        r = row(name, rid)
        assert old in str(r.get(field, "")), ("edit text not found", name, rid, field, old[:60])
        r[field] = r[field].replace(old, new)
    for name, rid, field, value in E.SETS:
        row(name, rid)[field] = value
    for name, data in cache.items():
        write(out, name, data)


if __name__ == "__main__":
    main(*sys.argv[1:3])
