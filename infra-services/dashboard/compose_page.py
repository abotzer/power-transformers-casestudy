"""Compose the infra-services dashboard page from the transformer page's shared parts plus this report's own parts.

Usage: python3 -I compose_page.py <transformer index.html> <layer_titles.json> <out index.html>
Shared parts taken from the transformer page: all CSS, the Whitesail band, JS helpers, the table
system, the value-chain graph, glossary pop-ups, the watchlist timeline, and the tabs/collapsibles code.
This report's own parts: body.html, infra.css, infra.js and the tab map below.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

TABS = """const TABS = {
  overview: ['verdict-box', 'questions', 'value-chain', 'actions'],
  market: ['market-tiles', 'aging', 'why-now', 'deck-claims', 'watchlist'],
  competition: ['precedents', 'fragmentation'],
  economics: ['tam', 'synergies'],
  candidates: ['candidates'],
  fam: ['ranking', 'plan'],
  appendix: ['cand-appendix', 'sources', 'glossary', 'notes'],
};"""


def cut(s, start, end):
    i = s.index(start)
    j = s.index(end, i)
    return s[i:j]


def main(src, titles_path, out):
    s = open(src).read()
    css = s[s.index("<style>") + 7:s.index("</style>")]
    band = cut(s, '<div class="ws-band">', '<h1 class="tx-title">').rstrip()
    mark = cut(s, '<svg class="ws-mark"', "<span>Whitesail Labs ·").rstrip()
    js = []
    js.append(cut(s, "const FAIL = [", "function statusColor("))
    js.append(cut(s, "const sortState = {};", "const CAP_TABLE = {"))
    vc = cut(s, "const VC_LAYERS = [", "function renderFulton() {")
    titles = json.load(open(titles_path))
    assert len(titles) == 7
    start = vc.index("const VC_TITLES = [")
    end = vc.index("\n", start)
    vc = vc[:start] + "const VC_TITLES = " + json.dumps(titles) + ";" + vc[end:]
    js.append(vc)
    js.append(cut(s, "function renderWatchTimeline() {", "function renderPortfolioBoard() {"))
    js.append(cut(s, "const GLOSS_TABLE = {", "// ---------- glossary"))
    js.append(cut(s, "// ---------- glossary", "document.getElementById('vc-select')"))
    js.append(open(os.path.join(HERE, "infra.js")).read())
    tabs = cut(s, "// ---------- tabs and collapsibles", "dash.onData(renderAll);")
    t0 = tabs.index("const TABS = {")
    t1 = tabs.index("};", t0) + 2
    tabs = tabs[:t0] + TABS + tabs[t1:]
    js.append(tabs)
    js.append("dash.onData(renderAll);\n")
    body = open(os.path.join(HERE, "body.html")).read().replace("%BAND%", band).replace("%MARK%", mark)
    page = ("<style>" + css + "\n" + open(os.path.join(HERE, "infra.css")).read() + "</style>\n\n<div class=\"tx\">\n"
            + body + "</div>\n\n<script>\n" + "\n".join(js) + "</script>\n")
    open(out, "w").write(page)
    print("wrote", out, len(page), "bytes")


if __name__ == "__main__":
    main(*sys.argv[1:4])
