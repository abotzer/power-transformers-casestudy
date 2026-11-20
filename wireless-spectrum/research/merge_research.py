"""Merge the research workflow runs into research/workflow_result.json and write research/brief.md (a digest for later stages).

Usage: python3 -I merge_research.py <out dir> <journal.jsonl> [<journal.jsonl> ...]
Each journal line of type "result" holds one domain researcher's return value.
"""
import json
import sys

ORDER = ["demand", "capacity", "supply", "prices", "satellite", "economics", "investables", "precedents", "global"]


def main(out, *journals):
    research = {}
    for j in journals:
        for line in open(j):
            try:
                e = json.loads(line)
            except ValueError:
                continue
            r = e.get("result")
            if e.get("type") == "result" and isinstance(r, dict) and r.get("domain"):
                research[r["domain"]] = r
    missing = [k for k in ORDER if k not in research]
    print("domains:", len(research), "missing:", missing)
    json.dump({"research": {k: research[k] for k in ORDER if k in research}}, open(out + "/workflow_result.json", "w"), ensure_ascii=False, indent=1)
    lines = ["# Wireless spectrum research digest (prepared 2026-11-19)", ""]
    for k in ORDER:
        r = research.get(k)
        if not r:
            continue
        lines += ["## " + k, "", r.get("answer", "").strip(), "", "### Key findings"]
        for f in r.get("findings", []):
            if f.get("key"):
                lines.append("- [%s] %s: %s (%s; %s, %s)" % (f.get("confidence"), f.get("claim"), f.get("value"), f.get("as_of"), f.get("source_name"), f.get("source_url")))
        lines += ["", "### Forecast seeds"]
        for s in r.get("forecast_seeds", []):
            lines.append("- %s [%s] now %s; history: %s; up: %s; down: %s; base rate: %s; suggested P10/P50/P90 %s / %s / %s (%s)" % (
                s.get("question"), s.get("unit"), s.get("current_value"), s.get("history"), s.get("drivers_up"), s.get("drivers_down"), s.get("base_rate"), s.get("p10"), s.get("p50"), s.get("p90"), s.get("horizon")))
        lines += ["", "### Gaps", r.get("gaps", ""), ""]
    open(out + "/brief.md", "w").write("\n".join(lines))
    print("brief chars", sum(len(x) + 1 for x in lines))


if __name__ == "__main__":
    main(*sys.argv[1:])
