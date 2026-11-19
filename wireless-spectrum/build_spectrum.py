"""Build the wireless-spectrum dashboard datasets from the research, verification, forecasting and synthesis results.

Usage: python3 -I build_spectrum.py <research dir> <out dir>
Reads research/workflow_result.json (nine research domains), research/verification.json (independent checks of
key numbers), research/forecasts.json (forecasting panel and chief forecaster), research/map_glossary.json (market map
and glossary) and research/synthesis.json (key findings, universe curation, watchlist), plus editorial.py (report
wording: verdict, method, caveats, chart titles and notes).
Writes one JSON file per dataset into <out dir> and dashboard/layer_titles.json.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editorial as E  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def clean(t):
    t = str(t if t is not None else "").replace("**", "").replace("&amp;", "&")
    t = re.sub(r"(^|\n)\s*[-*]\s+", r"\1• ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def https(u):
    u = str(u or "").strip()
    return u if u.startswith("https://") or u.startswith("http://") else ""


def slug(s, n=40):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:n]


def numf(v):
    """First number in a string ('$23.0B' -> 23.0, '~0.94' -> 0.94); None if absent."""
    if v is None:
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
    print(name, len(rows))


def load(path, default=None):
    return json.load(open(path)) if os.path.exists(path) else default
