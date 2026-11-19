// ---------- wireless spectrum report: renderers ----------
function fmtF(fmt, v) {
  if (v === null || v === undefined || Number.isNaN(v)) return '';
  if (fmt === 'usd2') return '$' + d3.format(',.2f')(v);
  if (fmt === 'usd') return '$' + d3.format(',.0f')(v);
  if (fmt === 'usd_t') return '$' + d3.format(',.1f')(v) + 'T';
  if (fmt === 'x') return d3.format(',.1f')(v) + 'x';
  if (fmt === 'mhz') return d3.format(',.0f')(v) + ' MHz';
  if (fmt === 'eb') return d3.format(',.0f')(v) + ' EB';
  if (fmt === 'm') return d3.format(',.0f')(v) + 'M';
  if (fmt === 'm1') return d3.format(',.1f')(v) + 'M';
  return fmtBy(fmt, v);
}
const wq = (id) => 'id=' + encodeURIComponent(id);
function detailsBox(summary) {
  const d = document.createElement('details');
  d.appendChild(mk('summary', null, summary));
  return d;
}
function labelled(parent, label, text, src, field, where) {
  if (!text) return;
  const p = mk('p', 'tx-card-note');
  p.appendChild(mk('b', null, label + ': '));
  p.appendChild(mk('span', null, text, src, field, where));
  parent.appendChild(p);
}

// ----- method box and caveats
function renderMethod() {
  const box = document.getElementById('method-box');
  if (!prep(box, ['plan'])) return;
  box.appendChild(mk('div', 'tx-bottom-label', 'Method'));
  const grid = mk('div', 'tx-verdict-grid');
  rows('plan').filter((r) => r.kind === 'method').sort(byOrder).forEach((r) => {
    const sec = mk('div', 'tx-verdict-sec');
    sec.appendChild(mk('h3', 'tx-verdict-h', r.heading, 'plan', 'heading', wq(r.id)));
    sec.appendChild(mk('p', 'tx-bottom-text tx-pre', r.body, 'plan', 'body', wq(r.id)));
    grid.appendChild(sec);
  });
  box.appendChild(grid);
}
function renderCaveats() {
  const el = document.getElementById('caveats-text');
  if (!prep(el, ['plan'])) return;
  rows('plan').filter((r) => r.kind === 'caveat').sort(byOrder).forEach((r) => el.appendChild(mk('span', null, r.body, 'plan', 'body', wq(r.id))));
}

// ----- scenarios
function scenColor(i) { return dash.colors[i % dash.colors.length]; }
function drawScenBar(elId) {
  const el = document.getElementById(elId);
  if (!prep(el, ['scenarios'])) return;
  const list = rows('scenarios').slice().sort(byOrder);
  const bar = mk('div', 'tx-scen-track');
  bar.setAttribute('role', 'img');
  bar.setAttribute('aria-label', list.map((s) => s.name + ' ' + s.probability + '%').join(', '));
  list.forEach((s, i) => {
    const seg = mk('div', 'tx-scen-seg');
    seg.style.flexGrow = String(num(s.probability) || 0);
    seg.style.background = scenColor(i);
    seg.appendChild(mk('span', 'tx-scen-pct', fmtVal(num(s.probability)) + '%'));
    bar.appendChild(seg);
  });
  el.appendChild(bar);
  const key = mk('div', 'tx-scen-key');
  list.forEach((s, i) => {
    const item = mk('div', 'tx-scen-keyitem');
    const sw = mk('i', 'tx-swatch');
    sw.style.background = scenColor(i);
    item.appendChild(sw);
    const t = mk('div');
    const top = mk('div', 'tx-strong');
    top.appendChild(mk('span', null, s.name, 'scenarios', 'name', wq(s.id)));
    top.appendChild(document.createTextNode(' · '));
    top.appendChild(mk('span', null, fmtVal(num(s.probability)), 'scenarios', 'probability', wq(s.id)));
    top.appendChild(document.createTextNode('%'));
    t.appendChild(top);
    t.appendChild(mk('div', 'tx-card-note', s.tagline, 'scenarios', 'tagline', wq(s.id)));
    item.appendChild(t);
    key.appendChild(item);
  });
  el.appendChild(key);
}
function renderScenarios() {
  const el = document.getElementById('scen-grid');
  if (!prep(el, ['scenarios'])) return;
  rows('scenarios').slice().sort(byOrder).forEach((s, i) => {
    const w = wq(s.id);
    const card = mk('article', 'tx-card tx-scen-card');
    card.style.borderTopColor = scenColor(i);
    const top = mk('div', 'tx-scen-top');
    top.appendChild(mk('h3', 'tx-card-title', s.name, 'scenarios', 'name', w));
    const pr = mk('div', 'tx-scen-prob');
    pr.appendChild(mk('span', null, fmtVal(num(s.probability)), 'scenarios', 'probability', w));
    pr.appendChild(document.createTextNode('%'));
    top.appendChild(pr);
    card.appendChild(top);
    card.appendChild(mk('p', 'tx-strong', s.tagline, 'scenarios', 'tagline', w));
    card.appendChild(mk('p', null, s.summary, 'scenarios', 'summary', w));
    const dl = mk('dl', 'tx-dl');
    [['Spectrum prices', 'spectrum_prices'], ['US carriers', 'carriers'], ['Satellite operators', 'satellites'], ['For an investor', 'investors']].forEach(([lbl, f]) => {
      if (!s[f]) return;
      dl.appendChild(mk('dt', null, lbl));
      dl.appendChild(mk('dd', null, s[f], 'scenarios', f, w));
    });
    card.appendChild(dl);
    if (s.signposts) {
      const d = detailsBox('What would tell us we are heading here');
      d.appendChild(mk('p', 'tx-pre', s.signposts, 'scenarios', 'signposts', w));
      card.appendChild(d);
    }
    el.appendChild(card);
  });
}

// ----- forecasts: one card per question with an 80% range strip
function niceDomain(vals, isLog) {
  let lo = d3.min(vals), hi = d3.max(vals);
  if (isLog) return [lo / 1.35, hi * 1.35];
  const pad = (hi - lo) * 0.12 || Math.abs(hi) * 0.2 || 1;
  lo = lo - pad;
  if (d3.min(vals) >= 0 && lo < 0) lo = 0;
  return [lo, hi + pad];
}
function drawStrip(el, f, panel) {
  const W = Math.max(el.clientWidth, 260), H = 92, padL = 10, padR = 10, axisY = 58;
  const isLog = f.log === 'Yes';
  const vals = [num(f.p10), num(f.p50), num(f.p90), num(f.current)].concat(panel.map((p) => num(p.p50))).filter((v) => v !== null && (!isLog || v > 0));
  if (!vals.length) return;
  const x = (isLog ? d3.scaleLog() : d3.scaleLinear()).domain(niceDomain(vals, isLog)).range([padL, W - padR]);
  const fmt = (v) => fmtF(f.fmt, v);
  const svg = newSvg(el, W, H).attr('aria-label', f.short + ': central ' + fmt(num(f.p50)) + ', 80% range ' + fmt(num(f.p10)) + ' to ' + fmt(num(f.p90)));
  svg.append('line').attr('x1', padL).attr('x2', W - padR).attr('y1', axisY).attr('y2', axisY).style('stroke', 'var(--cds-chart-grid)').attr('stroke-width', 2);
  const ticks = isLog ? x.ticks(4).filter((t, i, a) => a.length <= 5 || i % 2 === 0) : x.ticks(4);
  ticks.forEach((t) => {
    svg.append('line').attr('x1', x(t)).attr('x2', x(t)).attr('y1', axisY - 3).attr('y2', axisY + 3).style('stroke', 'var(--cds-chart-axis)');
    const lbl = svg.append('text').attr('x', x(t)).attr('y', H - 4).attr('text-anchor', 'middle').text(fmt(t).replace(/\.0(?=\D*$)/, ''));
    const lw = lbl.node().getComputedTextLength();
    if (x(t) - lw / 2 < 0) lbl.attr('text-anchor', 'start').attr('x', 0);
    else if (x(t) + lw / 2 > W) lbl.attr('text-anchor', 'end').attr('x', W);
  });
  const p10 = num(f.p10), p50 = num(f.p50), p90 = num(f.p90), cur = num(f.current);
  if (p10 !== null && p90 !== null) {
    svg.append('rect').attr('x', x(p10)).attr('y', axisY - 12).attr('width', Math.max(3, x(p90) - x(p10))).attr('height', 24).attr('rx', 5)
      .style('fill', dash.colors[0]).attr('fill-opacity', 0.22);
  }
  panel.forEach((p) => {
    const v = num(p.p50);
    if (v === null || (isLog && v <= 0)) return;
    svg.append('line').attr('x1', x(v)).attr('x2', x(v)).attr('y1', axisY - 22).attr('y2', axisY - 15).style('stroke', 'var(--color-fg-muted)').attr('stroke-width', 1.5)
      .on('mousemove', (ev) => { const [qx, qy] = d3.pointer(ev, svg.node()); showTip(el, p.lens, [fmt(v), p.note || ''], qx, qy); })
      .on('mouseleave', () => hideTip(el));
  });
  if (p50 !== null) {
    svg.append('line').attr('x1', x(p50)).attr('x2', x(p50)).attr('y1', axisY - 13).attr('y2', axisY + 13).style('stroke', dash.colors[0]).attr('stroke-width', 3);
    const t = svg.append('text').attr('class', 'tx-val').attr('x', x(p50)).attr('y', 14).attr('text-anchor', 'middle').style('font-weight', 600).text(fmt(p50));
    const tw = t.node().getComputedTextLength();
    if (x(p50) - tw / 2 < 0) t.attr('x', tw / 2);
    if (x(p50) + tw / 2 > W) t.attr('x', W - tw / 2);
  }
  if (cur !== null && (!isLog || cur > 0)) {
    svg.append('circle').attr('cx', x(cur)).attr('cy', axisY).attr('r', 5).style('fill', 'var(--color-panel)').style('stroke', 'var(--color-fg)').attr('stroke-width', 2);
  }
  svg.append('rect').attr('x', 0).attr('y', 0).attr('width', W).attr('height', H).style('fill', 'transparent')
    .on('mousemove', (ev) => {
      const [qx, qy] = d3.pointer(ev, svg.node());
      showTip(el, f.short, ['Central: ' + fmt(p50), '80% range: ' + fmt(p10) + ' to ' + fmt(p90), cur !== null ? 'Today: ' + (f.current_label || fmt(cur)) : ''], qx, qy);
    })
    .on('mouseleave', () => hideTip(el))
    .lower();
}
function forecastCard(f, panelRows, compact) {
  const w = wq(f.id);
  const card = mk('article', 'tx-card tx-fc');
  const head = mk('div', 'tx-fc-head');
  head.appendChild(mk('h3', 'tx-card-title', f.short, 'forecasts', 'short', w));
  const chips = mk('div', 'tx-chips');
  chips.appendChild(mk('span', 'tx-chip', f.horizon, 'forecasts', 'horizon', w));
  head.appendChild(chips);
  card.appendChild(head);
  card.appendChild(mk('p', 'tx-card-note', f.question, 'forecasts', 'question', w));
  const strip = mk('div', 'tx-chart tx-fc-strip');
  strip.setAttribute('data-source', 'forecasts forecast_panel');
  card.appendChild(strip);
  const nums = mk('div', 'tx-fc-nums');
  [['Low (10%)', 'p10'], ['Central', 'p50'], ['High (90%)', 'p90']].forEach(([lbl, fld]) => {
    const b = mk('div', 'tx-fc-num' + (fld === 'p50' ? ' is-mid' : ''));
    b.appendChild(mk('span', 'tx-ans-lbl', lbl));
    b.appendChild(mk('span', 'tx-ans-val', fmtF(f.fmt, num(f[fld])), 'forecasts', fld, w));
    nums.appendChild(b);
  });
  const today = mk('div', 'tx-fc-num');
  today.appendChild(mk('span', 'tx-ans-lbl', 'Today'));
  today.appendChild(mk('span', 'tx-ans-val tx-fc-today', f.current_label, 'forecasts', 'current_label', w));
  nums.appendChild(today);
  card.appendChild(nums);
  const d = detailsBox(compact ? 'Reasoning' : 'Reasoning, drivers and signposts');
  d.appendChild(mk('p', null, f.rationale, 'forecasts', 'rationale', w));
  if (!compact) {
    labelled(d, 'What would push it up', f.drivers_up, 'forecasts', 'drivers_up', w);
    labelled(d, 'What would hold it down', f.drivers_down, 'forecasts', 'drivers_down', w);
    labelled(d, 'Reference class', f.base_rate, 'forecasts', 'base_rate', w);
    labelled(d, 'Signposts', f.signposts, 'forecasts', 'signposts', w);
    if (panelRows.length) {
      const ul = mk('ul', 'tx-bul tx-card-note');
      panelRows.forEach((p) => {
        const li = mk('li');
        li.appendChild(mk('b', null, p.lens + ': '));
        li.appendChild(mk('span', null, fmtF(f.fmt, num(p.p50)) + ' (' + fmtF(f.fmt, num(p.p10)) + ' to ' + fmtF(f.fmt, num(p.p90)) + ')'));
        if (p.note) li.appendChild(mk('span', 'tx-muted', ' · ' + p.note));
        ul.appendChild(li);
      });
      const t = mk('p', 'tx-card-note');
      t.appendChild(mk('b', null, 'Each lens on its own:'));
      d.appendChild(t);
      d.appendChild(ul);
    }
  }
  d.appendChild(sourceLinks(f.sources));
  card.appendChild(d);
  return [card, strip];
}
function renderForecastGrid(elId, filter, compact) {
  const el = document.getElementById(elId);
  if (!prep(el, ['forecasts', 'forecast_panel'])) return;
  const panel = rows('forecast_panel');
  const list = rows('forecasts').filter(filter).sort((a, b) => String(a.group).localeCompare(String(b.group)) || byOrder(a, b));
  if (!list.length) { el.appendChild(mk('p', 'tx-card-note', 'No forecast in this topic.')); return; }
  const jobs = [];
  let lastGroup = null;
  list.forEach((f) => {
    if (!compact && f.group !== lastGroup) { el.appendChild(mk('h3', 'tx-fc-group', f.group, 'forecasts', 'group', wq(f.id))); lastGroup = f.group; }
    const pr = panel.filter((p) => p.forecast_id === f.id);
    const [card, strip] = forecastCard(f, pr, compact);
    el.appendChild(card);
    jobs.push([strip, f, pr]);
  });
  jobs.forEach(([strip, f, pr]) => { try { drawStrip(strip, f, pr); } catch (e) { console.error('forecast ' + f.id, e); } });
}
function renderForecasts() {
  const sel = document.getElementById('fc-group');
  if (statusOf(['forecasts']) === 'ok' && sel.options.length <= 1) {
    Array.from(new Set(rows('forecasts').map((f) => f.group))).sort().forEach((g) => { const o = document.createElement('option'); o.value = g; o.textContent = g; sel.appendChild(o); });
  }
  const g = sel.value;
  renderForecastGrid('fc-grid', (f) => !g || f.group === g, false);
}

// ----- yes/no events
function renderProbabilities() {
  const el = document.getElementById('prob-list');
  if (!prep(el, ['probabilities'])) return;
  const panel = statusOf(['forecast_panel']) === 'ok' ? rows('forecast_panel') : [];
  rows('probabilities').slice().sort(byOrder).forEach((r) => {
    const w = wq(r.id);
    const it = mk('article', 'tx-prob');
    const top = mk('div', 'tx-prob-top');
    const q = mk('div', 'tx-prob-q');
    q.appendChild(mk('span', 'tx-strong', r.question, 'probabilities', 'question', w));
    const chips = mk('div', 'tx-chips');
    chips.appendChild(mk('span', 'tx-chip', r.horizon, 'probabilities', 'horizon', w));
    if (r.group) chips.appendChild(mk('span', 'tx-chip', r.group, 'probabilities', 'group', w));
    q.appendChild(chips);
    top.appendChild(q);
    const big = mk('div', 'tx-prob-val');
    big.appendChild(mk('span', null, fmtVal(num(r.probability)), 'probabilities', 'probability', w));
    big.appendChild(document.createTextNode('%'));
    top.appendChild(big);
    it.appendChild(top);
    const track = mk('div', 'tx-prob-track');
    track.setAttribute('role', 'img');
    track.setAttribute('aria-label', r.probability + '% (lenses from ' + r.low + '% to ' + r.high + '%)');
    const lo = num(r.low), hi = num(r.high), p = num(r.probability);
    if (lo !== null && hi !== null) { const rg = mk('i', 'tx-prob-range'); rg.style.left = lo + '%'; rg.style.width = Math.max(0.8, hi - lo) + '%'; track.appendChild(rg); }
    const fill = mk('i', 'tx-prob-fill');
    fill.style.width = (p || 0) + '%';
    track.appendChild(fill);
    panel.filter((x) => x.forecast_id === r.id).forEach((x) => { const v = num(x.p50); if (v === null) return; const t = mk('i', 'tx-prob-tick'); t.style.left = v + '%'; t.title = x.lens + ': ' + v + '%'; track.appendChild(t); });
    it.appendChild(track);
    const rng = mk('div', 'tx-card-note');
    rng.appendChild(document.createTextNode('Range across lenses: '));
    rng.appendChild(mk('span', null, fmtVal(lo), 'probabilities', 'low', w));
    rng.appendChild(document.createTextNode('% to '));
    rng.appendChild(mk('span', null, fmtVal(hi), 'probabilities', 'high', w));
    rng.appendChild(document.createTextNode('%'));
    it.appendChild(rng);
    const d = detailsBox('Reasoning and how it resolves');
    d.appendChild(mk('p', null, r.rationale, 'probabilities', 'rationale', w));
    labelled(d, 'Resolves yes if', r.resolution, 'probabilities', 'resolution', w);
    labelled(d, 'Signposts', r.signposts, 'probabilities', 'signposts', w);
    it.appendChild(d);
    el.appendChild(it);
  });
}

// ----- universe of listed exposure
const CAT_ORDER = ['US carriers', 'Spectrum holders', 'Satellite and direct-to-device', 'Cable', 'Towers', 'SpaceX access', 'Funds and ETFs', 'International'];
const GRADE_RANK = { High: 0, Medium: 1, Low: 2 };
function uniFilter(r) {
  const g = document.getElementById('uni-grade').value;
  const q = (document.getElementById('uni-search').value || '').trim().toLowerCase();
  if (g && r.exposure_grade !== g) return false;
  if (q && !['name', 'ticker', 'category', 'holdings', 'benefits_if', 'loses_if', 'risks'].some((k) => String(r[k] || '').toLowerCase().includes(q))) return false;
  return true;
}
function renderUniverse() {
  const el = document.getElementById('uni-board');
  if (!prep(el, ['universe'])) return;
  const list = rows('universe').filter(uniFilter);
  if (!list.length) { el.appendChild(mk('p', 'tx-card-note', 'Nothing matches these filters.')); return; }
  const cats = CAT_ORDER.filter((c) => list.some((r) => r.category === c)).concat(Array.from(new Set(list.map((r) => r.category))).filter((c) => !CAT_ORDER.includes(c)));
  cats.forEach((c) => {
    const sec = mk('section', 'tx-uni-cat');
    sec.appendChild(mk('h3', 'tx-fc-group', c));
    const grid = mk('div', 'tx-cand-grid');
    list.filter((r) => r.category === c).sort((a, b) => (GRADE_RANK[a.exposure_grade] ?? 3) - (GRADE_RANK[b.exposure_grade] ?? 3) || (num(b.market_cap_usd_b) || 0) - (num(a.market_cap_usd_b) || 0)).forEach((r) => {
      const w = wq(r.id);
      const it = mk('article', 'tx-cand');
      const head = mk('div', 'tx-cand-head');
      const nm = mk('span', 'tx-strong', r.name, 'universe', 'name', w);
      if (safeUrl(r.website)) { const a = linkTo(r.website, ''); a.appendChild(nm); head.appendChild(a); } else head.appendChild(nm);
      const g = mk('span', 'tx-chip', r.exposure_grade, 'universe', 'exposure_grade', w);
      g.setAttribute('data-attr', r.exposure_grade);
      head.appendChild(g);
      it.appendChild(head);
      const chips = mk('div', 'tx-chips');
      if (r.ticker) chips.appendChild(mk('span', 'tx-chip', r.ticker, 'universe', 'ticker', w));
      it.appendChild(chips);
      it.appendChild(mk('p', 'tx-cand-svc', r.holdings, 'universe', 'holdings', w));
      const facts = mk('div', 'tx-uni-facts');
      [['Market cap', 'market_cap_label'], ['Spectrum share of value', 'spectrum_pct_ev'], ['1-year return', 'return_1y']].forEach(([lbl, f]) => {
        if (!r[f]) return;
        const b = mk('div');
        b.appendChild(mk('span', 'tx-ans-lbl', lbl));
        b.appendChild(mk('span', 'tx-uni-v', r[f], 'universe', f, w));
        facts.appendChild(b);
      });
      it.appendChild(facts);
      const d = detailsBox('If spectrum gets scarcer, and if not');
      labelled(d, 'Gains if', r.benefits_if, 'universe', 'benefits_if', w);
      labelled(d, 'Loses if', r.loses_if, 'universe', 'loses_if', w);
      labelled(d, 'Risks', r.risks, 'universe', 'risks', w);
      labelled(d, 'Under our scenarios', r.scenario_view, 'universe', 'scenario_view', w);
      d.appendChild(sourceLinks(r.sources));
      it.appendChild(d);
      grid.appendChild(it);
    });
    sec.appendChild(grid);
    el.appendChild(sec);
  });
}

// ----- direct-to-device players
function renderPlayers() {
  const el = document.getElementById('players-board');
  if (!prep(el, ['d2d_players'])) return;
  rows('d2d_players').slice().sort(byOrder).forEach((r) => {
    const w = wq(r.id);
    const it = mk('article', 'tx-cand');
    const head = mk('div', 'tx-cand-head');
    head.appendChild(mk('span', 'tx-strong', r.name, 'd2d_players', 'name', w));
    it.appendChild(head);
    const chips = mk('div', 'tx-chips');
    if (r.owner) chips.appendChild(mk('span', 'tx-chip', r.owner, 'd2d_players', 'owner', w));
    if (r.stage) { const s = mk('span', 'tx-chip', r.stage, 'd2d_players', 'stage', w); s.setAttribute('data-attr', r.stage === 'In service' ? 'High' : r.stage === 'Testing' ? 'Medium' : 'Low'); chips.appendChild(s); }
    it.appendChild(chips);
    labelled(it, 'Spectrum', r.spectrum, 'd2d_players', 'spectrum', w);
    labelled(it, 'Partners', r.partners, 'd2d_players', 'partners', w);
    const d = detailsBox('Satellites, capacity and status');
    labelled(d, 'Satellites', r.satellites, 'd2d_players', 'satellites', w);
    labelled(d, 'Status', r.status, 'd2d_players', 'status', w);
    labelled(d, 'Capacity', r.capacity, 'd2d_players', 'capacity', w);
    labelled(d, 'Value or funding', r.value, 'd2d_players', 'value', w);
    d.appendChild(sourceLinks(r.sources));
    it.appendChild(d);
    el.appendChild(it);
  });
}

// ----- precedents
function renderPrecedents() {
  const el = document.getElementById('prec-board');
  if (!prep(el, ['precedents'])) return;
  const list = rows('precedents');
  [['Won', 'Paid off', 'thriving'], ['Mixed', 'Mixed', 'mixed'], ['Lost', 'Lost money', 'struggling']].forEach(([o, label, cls]) => {
    const items = list.filter((r) => r.outcome === o).sort(byOrder);
    if (!items.length) return;
    const col = mk('div', 'tx-board-col');
    col.setAttribute('data-outcome', cls);
    col.appendChild(mk('div', 'tx-board-head', label));
    items.forEach((r) => {
      const w = wq(r.id);
      const it = mk('article', 'tx-board-item');
      it.appendChild(mk('div', 'tx-strong', r.name, 'precedents', 'name', w));
      const chips = mk('div', 'tx-chips');
      chips.appendChild(mk('span', 'tx-chip', r.period, 'precedents', 'period', w));
      if (r.multiple) chips.appendChild(mk('span', 'tx-chip', r.multiple, 'precedents', 'multiple', w));
      it.appendChild(chips);
      it.appendChild(mk('p', null, r.lesson, 'precedents', 'lesson', w));
      const d = detailsBox('Cost, outcome and sources');
      labelled(d, 'Holder', r.holder, 'precedents', 'holder', w);
      labelled(d, 'Spectrum', r.spectrum, 'precedents', 'spectrum', w);
      labelled(d, 'Cost', r.cost_basis, 'precedents', 'cost_basis', w);
      labelled(d, 'Outcome', r.outcome_value, 'precedents', 'outcome_value', w);
      d.appendChild(sourceLinks(r.sources));
      it.appendChild(d);
      col.appendChild(it);
    });
    el.appendChild(col);
  });
}

// ----- tables
const PIPE_TABLE = {
  id: 'pipe-table', src: 'pipeline', key: 'id',
  cols: [
    { field: 'band', label: 'Band or rule' },
    { field: 'kind', label: 'Type' },
    { field: 'mhz', label: 'MHz', sortable: false },
    { field: 'timing', label: 'Timing', sortBy: 'order' },
    { field: 'status', label: 'Status', sortable: false, cls: 'tx-pre' },
    { field: 'notes', label: 'What it means', sortable: false, cls: 'tx-hide-sm tx-pre' },
  ],
  defaultSort: byOrder,
};
const DEALS_TABLE = {
  id: 'deals-table', src: 'deals', key: 'id',
  cols: [
    { field: 'name', label: 'Auction or deal' },
    { field: 'date', label: 'Date', sortBy: 'sort_date' },
    { field: 'kind', label: 'Type', cls: 'tx-hide-sm' },
    { field: 'band', label: 'Band', sortable: false },
    { field: 'buyer', label: 'Buyer', cls: 'tx-hide-sm' },
    { field: 'seller', label: 'Seller', cls: 'tx-hide-sm' },
    { field: 'price_label', label: 'Price', sortBy: 'price_usd_b' },
    { field: 'usd_per_mhz_pop', label: '$/MHz-pop', num: true, cls: 'tx-num' },
  ],
  defaultSort: (a, b) => (a.sort_date < b.sort_date ? 1 : -1),
};
const UNI_TABLE = {
  id: 'uni-table', src: 'universe', key: 'id',
  cols: [
    { field: 'name', label: 'Company or fund' },
    { field: 'ticker', label: 'Ticker' },
    { field: 'category', label: 'Category', cls: 'tx-hide-sm' },
    { field: 'exposure_grade', label: 'Exposure', cellClass: (r) => 'i-' + (r.exposure_grade || 'Low') },
    { field: 'market_cap_label', label: 'Market cap', sortBy: 'market_cap_usd_b' },
    { field: 'spectrum_pct_ev', label: 'Spectrum share of value', sortable: false },
    { field: 'return_1y', label: '1-year return', sortable: false, cls: 'tx-hide-sm' },
    { field: 'holdings', label: 'Holdings', sortable: false, cls: 'tx-hide-sm' },
  ],
  defaultSort: (a, b) => (GRADE_RANK[a.exposure_grade] ?? 3) - (GRADE_RANK[b.exposure_grade] ?? 3) || (num(b.market_cap_usd_b) || 0) - (num(a.market_cap_usd_b) || 0),
};
const PLAYERS_TABLE = {
  id: 'players-table', src: 'd2d_players', key: 'id',
  cols: [
    { field: 'name', label: 'Player' },
    { field: 'owner', label: 'Owner or ticker' },
    { field: 'stage', label: 'Stage' },
    { field: 'spectrum', label: 'Spectrum', sortable: false },
    { field: 'partners', label: 'Partners', sortable: false, cls: 'tx-hide-sm' },
    { field: 'satellites', label: 'Satellites', sortable: false, cls: 'tx-hide-sm' },
  ],
  defaultSort: byOrder,
};
const WATCH_TABLE = {
  id: 'watch-table', src: 'watchlist', key: 'id',
  cols: [
    { field: 'when', label: 'When', sortBy: 'sort_date' },
    { field: 'item', label: 'What', sortable: false, cls: 'tx-pre' },
    { field: 'why', label: 'Why it matters', sortable: false, cls: 'tx-pre' },
  ],
  defaultSort: (a, b) => (a.sort_date < b.sort_date ? -1 : 1),
};
const SRC_TABLE = {
  id: 'src-table', src: 'findings', key: 'id',
  cols: [
    { field: 'claim', label: 'Finding', sortable: false },
    { field: 'value', label: 'Value', sortable: false },
    { field: 'domain', label: 'Topic' },
    { field: 'status', label: 'Check', cls: 'tx-hide-sm' },
    { field: 'confidence', label: 'Tag' },
    { field: 'source_url', label: 'Source', sortable: false, cls: 'tx-hide-sm' },
  ],
  filter: (r) => {
    const q = (document.getElementById('src-search').value || '').trim().toLowerCase();
    return !q || ['claim', 'value', 'domain', 'source_name', 'source_url'].some((k) => String(r[k] || '').toLowerCase().includes(q));
  },
};

function vcFocusId() {
  const n = rows('value_chain_nodes').find((x) => x.kind === 'focus');
  return n ? n.id : null;
}
document.getElementById('vc-select').addEventListener('change', (ev) => vcSelect(ev.target.value || null));
document.getElementById('vc-clear').addEventListener('click', () => vcSelect(null));
document.getElementById('vc-focus').addEventListener('click', () => vcSelect(vcFocusId()));
document.getElementById('gloss-search').addEventListener('input', () => renderTable(GLOSS_TABLE));
document.getElementById('src-search').addEventListener('input', () => renderTable(SRC_TABLE));
document.getElementById('fc-group').addEventListener('change', () => { renderForecasts(); scheduleGlossary(); });
['uni-grade', 'uni-search'].forEach((id) => document.getElementById(id).addEventListener(id === 'uni-search' ? 'input' : 'change', () => { renderUniverse(); scheduleGlossary(); }));

let linked = false;
function renderAll() {
  [
    fillMarks, renderSummary, () => drawScenBar('outlook-scen'), () => renderForecastGrid('outlook-grid', (f) => f.headline === 'Yes', true),
    drawValueChain, renderFindings,
    () => renderTiles('tiles-demand', 'demand'), () => renderTiles('tiles-supply', 'supply'), () => renderTiles('tiles-prices', 'prices'), () => renderTiles('tiles-satellite', 'satellite'),
    () => renderChartCards('charts-demand', 'demand'), () => renderChartCards('charts-capacity', 'capacity'), () => renderChartCards('charts-supply', 'supply'),
    () => renderChartCards('charts-prices', 'prices'), () => renderChartCards('charts-global', 'global'), () => renderChartCards('charts-precedents', 'precedents'),
    () => renderChartCards('charts-satellite', 'satellite'), () => renderChartCards('charts-invest', 'invest'), () => renderChartCards('charts-economics', 'economics'),
    renderMethod, () => drawScenBar('scen-bar'), renderScenarios, renderForecasts, renderProbabilities, renderWatchTimeline,
    renderUniverse, renderPlayers, renderPrecedents, renderCaveats,
    () => renderTable(PIPE_TABLE), () => renderTable(DEALS_TABLE), () => renderTable(UNI_TABLE), () => renderTable(PLAYERS_TABLE),
    () => renderTable(WATCH_TABLE), () => renderTable(SRC_TABLE), () => renderTable(GLOSS_TABLE),
  ].forEach((f) => {
    try { f(); } catch (e) { console.error(e); }
  });
  glHide(true);
  scheduleGlossary();
}
