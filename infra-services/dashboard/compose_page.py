"""Compose the infra-services dashboard page from the transformer page's shared parts plus this report's own parts.

Usage: python3 -I compose_page.py <transformer index.html> <layer_titles.json> <out index.html>
Shared parts taken from the transformer page: all CSS, the Whitesail band, JS helpers, the table
system, the value-chain graph, glossary pop-ups, the watchlist timeline, and the tabs/collapsibles code.
This report's own parts: body.html, infra.css, infra.js, the tab map below, and VC_PATCHES, which adapt the
value-chain graph to show the prospective platform (kind "prospect") and Fulton's links to it (kind "fulton_synergy").
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

TABS = """const TABS = {
  overview: ['verdict-box', 'value-chain', 'key-findings', 'actions'],
  market: ['market-tiles', 'aging', 'why-now', 'watchlist'],
  competition: ['precedents', 'fragmentation'],
  economics: ['tam', 'synergies'],
  candidates: ['candidates'],
  fam: ['prospect', 'ranking', 'plan'],
  appendix: ['cand-appendix', 'sources', 'glossary', 'notes'],
};"""

FULTON = "/^fulton/.test(e.kind)"
VC_PATCHES = [
    ("const vcState = { sel: null };", "const vcState = { sel: 'prospect' };"),
    ("  if (n.kind === 'fulton') return 'var(--color-warn)';\n",
     "  if (n.kind === 'fulton') return 'var(--color-warn)';\n  if (n.kind === 'prospect') return 'var(--vc-prospect)';\n"),
    ("(showF || e.kind !== 'fulton_opportunity')", "(showF || !" + FULTON + ")"),
    ("[['Supplier chain of the selected company', c[0], false], ['Customer chain', c[1], false], ['Fulton opportunity: addressable market, not current sales', 'var(--color-warn)', true]]",
     "[['Selected company and its whole chain: darker lines', 'var(--color-fg-muted)', false], ['Dashed: estimated links of the New Platform' + (document.getElementById('vc-fulton').checked ? ' and Fulton\\'s companies' : ''), 'var(--cds-chart-muted)', true]]"),
    ("'Value chain of the North American transformer market: suppliers, builders and customers with annual flows'",
     "'Value chain of US utility infrastructure services: suppliers, service providers and customers with annual flows'"),
    (".attr('text-anchor', 'middle').text('Builders');", ".attr('text-anchor', 'middle').text('Service providers');"),
    ("const color = (e, r) => (e.kind === 'fulton_opportunity' ? 'var(--color-warn)' : r === 'up' ? c[0] : r === 'down' ? c[1] : 'var(--cds-chart-muted)');",
     "const color = () => 'var(--cds-chart-muted)';"),
    ("const op = r === 'none' ? (e.kind === 'fulton_opportunity' ? 0.75 : 0.4) : 0.9;", "const op = r === 'none' ? (e.kind !== 'flow' ? 0.8 : 0.4) : 0.9;"),
    (".attr('stroke-dasharray', e.kind === 'fulton_opportunity' ? '5 4' : null);", ".attr('stroke-dasharray', e.kind !== 'flow' ? '5 4' : null);"),
    ("e.kind === 'fulton_opportunity' ? 'Addressable market for a Fulton company, not current sales' : ''",
     "e.kind === 'prospect' ? 'Estimate for a platform of about $50M revenue, not a specific company' : " + FULTON + " ? 'Possible link with a Fulton company, not current sales' : ''"),
    ("n.kind === 'fulton' ? 'is-fulton' : '',", "n.kind === 'fulton' ? 'is-fulton' : '', n.kind === 'prospect' ? 'is-prospect' : '',"),
    ("model.edges.filter((e) => e.kind !== 'fulton_opportunity').forEach((e) => {", "model.edges.filter((e) => e.kind === 'flow').forEach((e) => {"),
    ("if (vcState.sel) labelled = model.edges.filter((e) => e.source === vcState.sel || e.target === vcState.sel);",
     "if (vcState.sel) labelled = model.edges.filter((e) => e.source === vcState.sel || e.target === vcState.sel).sort((a, b) => (vcMid(b) || 0) - (vcMid(a) || 0)).slice(0, 6);"),
    ("      if (e.kind === 'fulton_opportunity') { const ch = mk('span', 'tx-chip', 'Opportunity'); ch.setAttribute('data-kind', 'fulton'); top.appendChild(ch); }",
     "      if (" + FULTON + ") { const ch = mk('span', 'tx-chip', 'Fulton link'); ch.setAttribute('data-kind', 'fulton'); top.appendChild(ch); }\n"
     "      if (e.kind === 'prospect') { const ch = mk('span', 'tx-chip', 'Prospective'); ch.setAttribute('data-kind', 'prospect'); top.appendChild(ch); }"),
]


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
    for old, new in VC_PATCHES:
        assert vc.count(old) == 1, old[:70]
        vc = vc.replace(old, new)
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
