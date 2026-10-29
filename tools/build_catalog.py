"""Build the public site: a catalog home page plus one folder per report.

Usage: python3 -I tools/build_catalog.py [repo_root] [out_dir]
Reads reports.json, builds each report with tools/build_site.py into <out_dir>/<slug>/,
and writes <out_dir>/index.html (the catalog), favicon.svg and robots.txt.
A report whose page or data folder does not exist yet is listed as "In preparation".
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site  # noqa: E402

LOGO = "shared/brand/whitesail-logo.svg"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Reports · Whitesail Labs</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&display=swap" rel="stylesheet">
<style>
:root { --navy: #1A3263; --cream: #F3EEE8; --amber: #FAB95B; --bg: #faf9f5; --panel: #fff; --fg: #1f1e1d; --muted: #6b6a66; --line: #e4e1d8; }
@media (prefers-color-scheme: dark) { :root { --bg: #1c1b19; --panel: #262522; --fg: #ecebe6; --muted: #a6a39b; --line: #3a3833; } }
* { box-sizing: border-box; }
html, body { margin: 0; background: var(--bg); color: var(--fg); font-family: Inter, system-ui, sans-serif; font-size: 15px; }
main { max-width: 72rem; margin: 0 auto; padding: 24px clamp(16px, 3vw, 40px) 56px; display: flex; flex-direction: column; gap: 28px; }
.band { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 16px; background: var(--navy); color: var(--cream); border-radius: 12px; padding: 14px 22px; position: relative; overflow: hidden; }
.band::after { content: ""; position: absolute; right: -2rem; top: 0; bottom: 0; width: 9rem; background: repeating-linear-gradient(180deg, transparent 0 .9rem, rgba(250,185,91,.55) .9rem 1.15rem); opacity: .35; transform: skewX(-20deg); }
.band svg { width: 44px; height: 44px; border-radius: 50%; box-shadow: 0 0 0 2px var(--cream); }
.name { font-family: "Source Serif 4", Georgia, serif; font-size: 20px; }
.tag { font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--amber); }
h1 { font-family: "Source Serif 4", Georgia, serif; font-weight: 400; font-size: clamp(28px, 4vw, 40px); margin: 0; padding-left: 14px; border-left: 4px solid var(--amber); }
.lede { color: var(--muted); max-width: 64ch; line-height: 1.55; margin: 0; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 22rem), 1fr)); gap: 18px; }
a.card { display: flex; flex-direction: column; gap: 10px; background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 22px; color: inherit; text-decoration: none; transition: border-color .15s, transform .15s; }
a.card:hover { border-color: var(--amber); transform: translateY(-2px); }
a.card.off { pointer-events: none; opacity: .6; }
.status { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); }
.card h2 { font-family: "Source Serif 4", Georgia, serif; font-weight: 400; font-size: 24px; margin: 0; }
.card p { margin: 0; line-height: 1.55; color: var(--muted); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto; }
.chips span { font-size: 12px; border: 1px solid var(--line); border-radius: 999px; padding: 1px 9px; color: var(--muted); }
.open { color: var(--fg); font-weight: 500; }
footer { color: var(--muted); font-size: 12px; border-top: 1px solid var(--line); padding-top: 14px; }
</style>
</head>
<body>
<main>
  <div class="band">%LOGO%<div><div class="name">Whitesail Labs</div><div class="tag">Market intelligence</div></div></div>
  <h1>Reports</h1>
  <p class="lede">Source-linked market research built on public and government data: permits, filings, federal statistics and regulatory dockets. Each report has a market map, the evidence behind it and what it means for the investor it was prepared for.</p>
  <div class="grid">
%CARDS%
  </div>
  <footer>Whitesail Labs · Prepared for Fulton Asset Management</footer>
</main>
</body>
</html>
"""


def card(r, live):
    e = html.escape
    chips = "".join("<span>%s</span>" % e(t) for t in r.get("tags", []))
    status = r["status"] if live else "In preparation"
    return """    <a class="card%s" href="%s/">
      <div class="status">%s · %s</div>
      <h2>%s</h2>
      <p>%s</p>
      <div class="chips">%s</div>
      <div class="open">%s</div>
    </a>""" % ("" if live else " off", e(r["slug"]), e(status), e(r["updated"]), e(r["title"]), e(r["subtitle"]), chips,
               "Open report &rarr;" if live else "")


def main(root=".", out="site"):
    reports = json.load(open(os.path.join(root, "reports.json")))
    os.makedirs(out, exist_ok=True)
    cards = []
    for r in reports:
        page, data = os.path.join(root, r["page"]), os.path.join(root, r["data"])
        live = os.path.exists(page) and os.path.isdir(data)
        if live:
            build_site.main(page, data, os.path.join(out, r["slug"]), r.get("page_title", r["title"]))
        cards.append(card(r, live))
    logo = open(os.path.join(root, LOGO)).read()
    svg = logo[logo.index("<svg"):]
    open(os.path.join(out, "index.html"), "w").write(PAGE.replace("%LOGO%", svg).replace("%CARDS%", "\n".join(cards)))
    open(os.path.join(out, "favicon.svg"), "w").write(logo)
    open(os.path.join(out, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    print("catalog:", len(reports), "reports ->", out)


if __name__ == "__main__":
    main(*sys.argv[1:3])
