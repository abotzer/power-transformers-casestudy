"""Compose the wireless-spectrum dashboard page from the shared report parts plus this report's own parts.

Usage: python3 -I compose_page.py <transformer index.html> <infra dashboard dir> <layer_titles.json> <out index.html>
Shared parts taken from the transformer page: all CSS, the Whitesail band, JS helpers, the table system, the
market-map graph, glossary pop-ups, the watchlist timeline and the tabs/collapsibles code.
Shared parts taken from the infra report (infra.js, infra.css): the verdict box, key-findings pane, figure tiles and the
generic chart engine (chart_meta + charts).
This report's own parts: body.html, spectrum.css, spectrum.js, the tab map below, and VC_PATCHES, which adapt the
market map: no portfolio overlay, dashed lines for spectrum-rights transactions (kind "spectrum") and a highlighted
"focus" company (SpaceX) that the page can trace with one click.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

TABS = """const TABS = {
  overview: ['verdict-box', 'outlook', 'value-chain', 'key-findings'],
  demand: ['demand-tiles', 'traffic', 'capacity'],
  supply: ['supply-tiles', 'holdings', 'pipeline'],
  prices: ['price-tiles', 'auctions', 'global', 'precedents'],
  satellite: ['sat-tiles', 'd2d', 'd2d-players'],
  projections: ['proj-method', 'scenarios', 'forecasts', 'events', 'watchlist'],
  invest: ['exposure', 'economics'],
  appendix: ['universe-appendix', 'players-appendix', 'sources', 'glossary', 'notes'],
};"""

VC_PATCHES = [
    ("const showF = document.getElementById('vc-fulton').checked;", "const showF = false;"),
    ("  if (n.kind === 'fulton') return 'var(--color-warn)';\n",
     "  if (n.kind === 'fulton') return 'var(--color-warn)';\n  if (n.kind === 'focus') return 'var(--vc-focus)';\n"),
    ("[['Supplier chain of the selected company', c[0], false], ['Customer chain', c[1], false], ['Fulton opportunity: addressable market, not current sales', 'var(--color-warn)', true]]",
     "[['Supplier chain of the selected company', c[0], false], ['Customer chain', c[1], false], ['Dashed: spectrum rights bought, sold or leased (deal or auction value, not a yearly flow)', 'var(--cds-chart-muted)', true]]"),
    ("'Value chain of the North American transformer market: suppliers, builders and customers with annual flows'",
     "'Market map of US wireless spectrum: where spectrum comes from, who holds it, the networks built on it and the demand they serve'"),
    (".attr('text-anchor', 'middle').text('Builders');", ".attr('text-anchor', 'middle').text('Spectrum holders');"),
    ("const color = (e, r) => (e.kind === 'fulton_opportunity' ? 'var(--color-warn)' : r === 'up' ? c[0] : r === 'down' ? c[1] : 'var(--cds-chart-muted)');",
     "const color = (e, r) => (r === 'up' ? c[0] : r === 'down' ? c[1] : 'var(--cds-chart-muted)');"),
    ("const op = r === 'none' ? (e.kind === 'fulton_opportunity' ? 0.75 : 0.4) : 0.9;", "const op = r === 'none' ? (e.kind === 'spectrum' ? 0.7 : 0.4) : 0.9;"),
    (".attr('stroke-dasharray', e.kind === 'fulton_opportunity' ? '5 4' : null);", ".attr('stroke-dasharray', e.kind === 'spectrum' ? '5 4' : null);"),
    ("e.kind === 'fulton_opportunity' ? 'Addressable market for a Fulton company, not current sales' : ''",
     "e.kind === 'spectrum' ? 'Spectrum rights: a deal or auction value, not a yearly flow' : ''"),
    ("n.kind === 'fulton' ? 'is-fulton' : '',", "n.kind === 'fulton' ? 'is-fulton' : '', n.kind === 'focus' ? 'is-focus' : '',"),
    ("model.edges.filter((e) => e.kind !== 'fulton_opportunity').forEach((e) => {", "model.edges.filter((e) => e.kind === 'flow').forEach((e) => {"),
    ("if (vcState.sel) labelled = model.edges.filter((e) => e.source === vcState.sel || e.target === vcState.sel);",
     "if (vcState.sel) labelled = model.edges.filter((e) => e.source === vcState.sel || e.target === vcState.sel).sort((a, b) => (vcMid(b) || 0) - (vcMid(a) || 0)).slice(0, 6);"),
    ("      if (e.kind === 'fulton_opportunity') { const ch = mk('span', 'tx-chip', 'Opportunity'); ch.setAttribute('data-kind', 'fulton'); top.appendChild(ch); }",
     "      if (e.kind === 'spectrum') { const ch = mk('span', 'tx-chip', 'Spectrum rights'); ch.setAttribute('data-kind', 'focus'); top.appendChild(ch); }"),
    ("'Click a company, or pick one from the list, to see who supplies it, who it sells to, what changes hands and how much it is worth each year.",
     "'Click a company, or pick one from the list, to see where its spectrum and equipment come from, who it sells to, what changes hands and how much it is worth."),
]


def cut(s, start, end):
    i = s.index(start)
    j = s.index(end, i)
    return s[i:j]


def main(src, infra_dir, titles_path, out):
    s = open(src).read()
    ij = open(os.path.join(infra_dir, "infra.js")).read()
    icss = open(os.path.join(infra_dir, "infra.css")).read()
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
    js.append(cut(ij, "const TAG_ATTR = {", "function renderPlatforms() {"))
    js.append(open(os.path.join(HERE, "spectrum.js")).read())
    tabs = cut(s, "// ---------- tabs and collapsibles", "dash.onData(renderAll);")
    t0 = tabs.index("const TABS = {")
    t1 = tabs.index("};", t0) + 2
    tabs = tabs[:t0] + TABS + tabs[t1:]
    js.append(tabs)
    js.append("dash.onData(renderAll);\n")
    body = open(os.path.join(HERE, "body.html")).read().replace("%BAND%", band).replace("%MARK%", mark)
    page = ("<style>" + css + "\n" + icss + "\n" + open(os.path.join(HERE, "spectrum.css")).read() + "</style>\n\n<div class=\"tx\">\n"
            + body + "</div>\n\n<script>\n" + "\n".join(js) + "</script>\n")
    open(out, "w").write(page)
    print("wrote", out, len(page), "bytes")


if __name__ == "__main__":
    main(*sys.argv[1:5])
