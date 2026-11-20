"""Write report.md: verdict, projections (scenarios, forecasts, event probabilities), key findings and the exposure list, from the site datasets.

Usage: python3 -I build_report_md.py site-data report.md
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from editorial import money  # noqa: E402


def load(d, name):
    return json.load(open(os.path.join(d, name + ".json")))


def link(text, url):
    return "[%s](%s)" % (text.replace("[", "(").replace("]", ")"), url) if url else text


def cell(s):
    return str(s if s is not None else "").replace("|", "/").replace("\n", " ")


def bullets(t):
    return str(t or "").replace("• ", "- ")


def main(d, out):
    plan = sorted(load(d, "plan"), key=lambda r: r["order"])
    findings = sorted(load(d, "key_findings"), key=lambda r: r["order"])
    nums = load(d, "key_numbers")
    fc = load(d, "forecasts")
    pr = sorted(load(d, "probabilities"), key=lambda r: r["order"])
    sc = sorted(load(d, "scenarios"), key=lambda r: r["order"])
    uni = load(d, "universe")
    watch = sorted(load(d, "watchlist"), key=lambda r: r["sort_date"])
    head = next((p for p in plan if p["kind"] == "headline"), None)
    L = ["# Wireless spectrum: market reference and probabilistic outlook", ""]
    if head:
        L += ["**%s**" % head["body"], ""]
    L += ["Prepared for Fulton Asset Management by Whitesail Labs, November 2026. The interactive report has the charts, market map, forecast panel and full source list; this file holds the text. It is a market reference, not investment advice.", "",
          "Units: a MHz-pop is one megahertz of bandwidth covering one person, so a nationwide 10 MHz licence is about 3.35 billion MHz-pops, and prices per MHz-pop let bands of different width and reach be compared. An exabyte (EB) is a billion gigabytes. Uplink is data sent from a device to the network.", ""]
    L += ["## Our verdict", ""]
    for p in [p for p in plan if p["kind"] == "verdict"]:
        L += ["**%s**" % p["heading"], "", bullets(p["body"]).replace("on the Projections tab", "in the signposts table below"), ""]
    L += ["## Scenarios for 2030", "", "| Scenario | Probability | What it looks like |", "|---|---|---|"]
    L += ["| **%s** | %s%% | %s |" % (cell(s["name"]), s["probability"], cell(s["tagline"])) for s in sc]
    L.append("")
    for s in sc:
        L += ["### %s (%s%%)" % (s["name"], s["probability"]), "", s["summary"], "",
              "- **Spectrum prices:** " + s["spectrum_prices"], "- **US carriers:** " + s["carriers"], "- **Satellite operators:** " + s["satellites"],
              "- **For an investor:** " + s["investors"], "- **Signposts:** " + s["signposts"], ""]
    L += ["## Forecasts", "", "Central estimate with an 80% range (10th to 90th percentile), from five independent forecasting lenses aggregated and reviewed by a chief forecaster.", ""]
    groups = []
    for f in fc:
        if f["group"] not in groups:
            groups.append(f["group"])
    for g in groups:
        L += ["### " + g, "", "| Question | Today | Central | 80% range | By |", "|---|---|---|---|---|"]
        for f in [x for x in fc if x["group"] == g]:
            L.append("| %s | %s | %s | %s to %s | %s |" % (cell(f["short"]), cell(f["current_label"]), money(f["p50"], f["fmt"]), money(f["p10"], f["fmt"]), money(f["p90"], f["fmt"]), f["horizon"]))
        L.append("")
        for f in [x for x in fc if x["group"] == g]:
            L += ["**%s.** %s" % (f["short"], f["rationale"]), ""]
    L += ["## Key events and their odds", "", "Ranges across lenses are narrow partly because the lenses shared research; they are not independent confirmations.", "", "| Event | By | Probability | Range across lenses |", "|---|---|---|---|"]
    L += ["| %s | %s | %s%% | %s-%s%% |" % (cell(p["question"]), p["horizon"], p["probability"], p["low"], p["high"]) for p in pr]
    L.append("")
    L += ["## Key findings", ""]
    for f in findings:
        L += ["### %s" % f["topic"], "", "*%s the thesis.* %s" % (f["tag"] if f["tag"] != "Mixed" else "Mixed for", f["summary"]), "", bullets(f["body"]), ""]
        ns = sorted([n for n in nums if n["finding"] == f["id"]], key=lambda n: n["order"])
        if ns:
            L += ["| Figure | Value |", "|---|---|"]
            L += ["| %s | %s |" % (cell(n["label"]), link(cell(n["value"]), n.get("source_url"))) for n in ns]
            L.append("")
    L += ["## Listed companies and funds with spectrum exposure", "", "Exposure is our judgment of how much the share price would move if US spectrum prices rose. It combines the spectrum share of value with whether the company can sell that spectrum. A map of the market, not a recommendation.", "",
          "| Name | Ticker | Category | Exposure | Market cap | Spectrum share of value | Holdings | How it fares in our four futures |", "|---|---|---|---|---|---|---|---|"]
    rank = {"High": 0, "Medium": 1, "Low": 2}
    for u in sorted(uni, key=lambda u: (rank.get(u["exposure_grade"], 3), u["category"], u["name"])):
        mc = cell(u.get("market_cap_label")) or ("" if u["category"] == "Funds and ETFs" else "Not confirmed")
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (link(cell(u["name"]), u.get("website")), cell(u["ticker"]), cell(u["category"]), u["exposure_grade"],
                                                               mc, cell(u.get("spectrum_pct_ev")), cell(u["holdings"]), cell(u.get("scenario_view"))))
    L += ["", "## Signposts and upcoming events", "", "| When | What | Why it matters |", "|---|---|---|"]
    L += ["| %s | %s | %s |" % (cell(w["when"]), cell(w["item"]), cell(w["why"])) for w in watch]
    L += ["", "## Method and caveats", ""]
    for p in [p for p in plan if p["kind"] == "method"]:
        L += ["**%s.** %s" % (p["heading"], p["body"].replace("is in the Appendix", "is in the Appendix of the interactive report")), ""]
    for p in [p for p in plan if p["kind"] == "caveat"]:
        L += [p["body"], ""]
    open(out, "w").write("\n".join(L))
    print("wrote", out, len(L), "lines")


if __name__ == "__main__":
    main(*sys.argv[1:3])
