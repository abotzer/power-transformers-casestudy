"""Write report.md: the verdict, key findings, recommended actions and the candidate list, from the site datasets.

Usage: python3 -I build_report_md.py site-data report.md
"""
import json
import os
import sys

UNITS = [("gas", "Natural gas distribution"), ("water", "Water / wastewater"), ("T&D", "T&D / electrical"), ("power-gen", "Power generation")]


def load(d, name):
    return json.load(open(os.path.join(d, name + ".json")))


def link(text, url):
    return "[%s](%s)" % (text.replace("[", "(").replace("]", ")"), url) if url else text


def main(d, out):
    findings = sorted(load(d, "key_findings"), key=lambda r: r["order"])
    nums = load(d, "key_numbers")
    plan = sorted(load(d, "plan"), key=lambda r: r["order"])
    cands = load(d, "candidates")
    head = next((p for p in plan if p["kind"] == "headline"), None)
    L = ["# Critical utility infrastructure services", ""]
    if head:
        L += ["**%s**" % head["body"], ""]
    L += ["Prepared for Fulton Asset Management by Whitesail Labs. The interactive report has the charts, market map and full source list; this file holds the text.", ""]
    L += ["## Our verdict", ""]
    for p in [p for p in plan if p["kind"] == "verdict"]:
        L += ["**%s**" % p["heading"], "", p["body"].replace("\u2022 ", "- "), ""]
    L += ["## Key findings", ""]
    for f in findings:
        L += ["### %s" % f["topic"], "", "*%s.* %s" % (f["tag"], f["summary"]), "", f["body"].replace("\u2022 ", "- "), ""]
        ns = sorted([n for n in nums if n["finding"] == f["id"]], key=lambda n: n["order"])
        if ns:
            L += ["| Figure | Value |", "|---|---|"]
            L += ["| %s | %s |" % (n["label"], link(n["value"], n.get("source_url"))) for n in ns]
            L.append("")
    L += ["## Recommended action items", ""]
    L += ["%d. %s" % (k + 1, p["body"]) for k, p in enumerate([p for p in plan if p["kind"] == "step"])]
    L += ["", "## Where a prospective platform would sit", ""]
    for p in [p for p in plan if p["kind"] == "profile"]:
        L += ["**%s.** %s" % (p["heading"], p["body"]), ""]
    L += ["## How Fulton's companies could work with the platform", ""]
    L += ["- **%s:** %s" % (p["heading"], p["body"]) for p in plan if p["kind"] == "vi"]
    L.append("")
    L += ["## Platform candidates by unit", "",
          "Grades: **Platform** = fits the platform criteria well enough to anchor a unit; **Add-on** = a tuck-in; **Watch** = weaker fit; **Lead** = website not yet verified.", ""]
    for key, name in UNITS:
        cs = sorted([c for c in cands if c["unit"] == key], key=lambda c: (["Platform", "Add-on", "Watch", "Lead"].index(c["grade"]) if c["grade"] in ["Platform", "Add-on", "Watch", "Lead"] else 9, -(c.get("fit_score") or 0), c["name"]))
        if not cs:
            continue
        L += ["### %s (%d)" % (name, len(cs)), "", "| Company | Grade | Fit | Ownership | HQ |", "|---|---|---|---|---|"]
        for c in cs:
            cell = lambda s: str(s or "").replace("|", "/").replace("\n", " ")
            L.append("| %s | %s | %s | %s | %s |" % (link(cell(c["name"]), c.get("website")), c["grade"], c.get("fit_score") or "", cell(c.get("ownership"))[:120], cell(c.get("hq"))[:60]))
        L.append("")
    open(out, "w").write("\n".join(L))
    print("wrote", out, len(L), "lines")


if __name__ == "__main__":
    main(*sys.argv[1:3])
