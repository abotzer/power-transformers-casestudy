// ---------- infra report: renderers ----------
const UNIT_LABEL = { gas: 'Natural gas', 'power-gen': 'Power generation', 'T&D': 'T&D and electrical', water: 'Water and wastewater' };
const TAG_ATTR = { Favorable: 'High', Mixed: 'Medium', Watch: 'Low' };
function byOrder(a, b) { return (num(a.order) || 0) - (num(b.order) || 0); }
function linkTo(url, text) {
  const u = safeUrl(url);
  if (!u) return mk('span', null, text);
  const a = document.createElement('a');
  a.href = u;
  a.target = '_blank';
  a.rel = 'noopener noreferrer';
  a.textContent = text;
  return a;
}
function sourceLinks(list) {
  const wrap = mk('div', 'tx-srcs');
  String(list || '').split(' | ').map((s) => s.trim()).filter((s) => safeUrl(s)).slice(0, 8).forEach((u, i) => {
    let host = '';
    try { host = new URL(u).hostname.replace(/^www\./, ''); } catch (e) { host = 'source'; }
    const a = linkTo(u, host + ' ↗');
    if (i) wrap.appendChild(document.createTextNode(' · '));
    wrap.appendChild(a);
  });
  return wrap;
}

function renderSummary() {
  const box = document.getElementById('fam-summary');
  if (!prep(box, ['plan'])) return;
  box.appendChild(mk('div', 'tx-bottom-label', 'Our verdict'));
  const grid = mk('div', 'tx-verdict-grid');
  rows('plan').filter((r) => r.kind === 'verdict').sort(byOrder).forEach((r) => {
    const w = 'id=' + encodeURIComponent(r.id);
    const sec = mk('div', 'tx-verdict-sec');
    sec.appendChild(mk('h3', 'tx-verdict-h', r.heading, 'plan', 'heading', w));
    sec.appendChild(mk('p', 'tx-bottom-text tx-pre', r.body, 'plan', 'body', w));
    grid.appendChild(sec);
  });
  box.appendChild(grid);
}

// structured text: blank lines split blocks; "•" and "1." lines become lists; short lines ending in ":" become subheads
function richText(text) {
  const wrap = mk('div', 'tx-rich');
  let list = null;
  String(text || '').split('\n').forEach((raw) => {
    const line = raw.trim();
    if (!line) { list = null; return; }
    const bullet = /^•\s*/.test(line), numbered = /^\d+\.\s/.test(line);
    if (bullet || numbered) {
      const tag = bullet ? 'ul' : 'ol';
      if (!list || list.tagName.toLowerCase() !== tag) { list = mk(tag, 'tx-bul'); wrap.appendChild(list); }
      list.appendChild(mk('li', null, line.replace(/^•\s*|^\d+\.\s/, '')));
      return;
    }
    list = null;
    if (line.length < 90 && /:$/.test(line)) wrap.appendChild(mk('h4', 'tx-rich-h', line.replace(/:$/, '')));
    else wrap.appendChild(mk('p', null, line));
  });
  return wrap;
}

const kfState = { sel: null };
function renderFindings() {
  const el = document.getElementById('findings-grid');
  if (!prep(el, ['key_findings', 'key_numbers'])) return;
  const list = rows('key_findings').slice().sort(byOrder);
  if (!list.length) return;
  if (!list.some((r) => r.id === kfState.sel)) kfState.sel = list[0].id;
  const nav = mk('div', 'tx-kf-nav');
  nav.setAttribute('role', 'tablist');
  list.forEach((r) => {
    const w = 'id=' + encodeURIComponent(r.id);
    const btn = mk('button', 'tx-kf-item');
    btn.type = 'button';
    btn.setAttribute('role', 'tab');
    btn.setAttribute('aria-selected', String(r.id === kfState.sel));
    const top = mk('div', 'tx-kf-item-top');
    top.appendChild(mk('span', 'tx-kf-topic', r.topic, 'key_findings', 'topic', w));
    const chip = mk('span', 'tx-chip', r.tag, 'key_findings', 'tag', w);
    chip.setAttribute('data-attr', TAG_ATTR[r.tag] || 'Medium');
    top.appendChild(chip);
    btn.appendChild(top);
    btn.appendChild(mk('span', 'tx-kf-head', r.headline, 'key_findings', 'headline', w));
    btn.addEventListener('click', () => { kfState.sel = r.id; el.textContent = ''; renderFindings(); scheduleGlossary(); });
    nav.appendChild(btn);
  });
  el.appendChild(nav);

  const r = list.find((x) => x.id === kfState.sel);
  const w = 'id=' + encodeURIComponent(r.id);
  const pane = mk('article', 'tx-kf-pane');
  pane.setAttribute('role', 'tabpanel');
  pane.appendChild(mk('div', 'tx-bottom-label', r.topic, 'key_findings', 'topic', w));
  pane.appendChild(mk('h3', 'tx-kf-title', r.headline, 'key_findings', 'headline', w));
  pane.appendChild(mk('p', 'tx-kf-summary', r.summary, 'key_findings', 'summary', w));
  const kn = rows('key_numbers').filter((n) => n.finding === r.id).sort(byOrder);
  if (kn.length) {
    const strip = mk('div', 'tx-kf-stats');
    kn.forEach((n) => {
      const nw = 'id=' + encodeURIComponent(n.id);
      const b = mk('div', 'tx-kf-stat');
      b.appendChild(mk('div', 'tx-ans-val', n.value, 'key_numbers', 'value', nw));
      b.appendChild(mk('div', 'tx-ans-lbl', n.label, 'key_numbers', 'label', nw));
      if (safeUrl(n.source_url)) {
        let host = 'source';
        try { host = new URL(n.source_url).hostname.replace(/^www\./, ''); } catch (e) { host = 'source'; }
        const src = mk('div', 'tx-srcs');
        src.appendChild(linkTo(n.source_url, host + ' ↗'));
        b.appendChild(src);
      }
      strip.appendChild(b);
    });
    pane.appendChild(strip);
  }
  const d = document.createElement('details');
  d.className = 'tx-kf-more';
  d.appendChild(mk('summary', null, 'Full evidence and sources'));
  const body = richText(r.body);
  body.setAttribute('data-source', 'key_findings');
  body.setAttribute('data-field', 'body');
  body.setAttribute('data-where', w);
  d.appendChild(body);
  d.appendChild(sourceLinks(r.sources));
  pane.appendChild(d);
  el.appendChild(pane);
}

function renderProfile() {
  const el = document.getElementById('prospect-grid');
  if (!prep(el, ['plan'])) return;
  rows('plan').filter((r) => r.kind === 'profile').sort(byOrder).forEach((r) => {
    const w = 'id=' + encodeURIComponent(r.id);
    const card = mk('div', 'tx-card');
    card.appendChild(mk('h3', 'tx-card-title', r.heading, 'plan', 'heading', w));
    card.appendChild(mk('p', 'tx-profile-text', r.body, 'plan', 'body', w));
    el.appendChild(card);
  });
}

function renderSteps() {
  const el = document.getElementById('plan-steps');
  if (!prep(el, ['plan'])) return;
  rows('plan').filter((r) => r.kind === 'step').sort(byOrder).forEach((r) => {
    el.appendChild(mk('li', null, r.body, 'plan', 'body', 'id=' + encodeURIComponent(r.id)));
  });
}

function renderTiles(elId, tab) {
  const el = document.getElementById(elId);
  if (!prep(el, ['figures'])) return;
  rows('figures').filter((r) => r.tab === tab).sort(byOrder).forEach((r) => {
    const w = 'id=' + encodeURIComponent(r.id);
    const t = mk('div', 'tx-tile');
    t.appendChild(mk('div', 'tx-tile-label', r.label, 'figures', 'label', w));
    const big = mk('div', 'tx-big');
    if (r.prefix) big.appendChild(mk('span', null, r.prefix, 'figures', 'prefix', w));
    big.appendChild(mk('span', null, fmtVal(num(r.value) !== null ? num(r.value) : r.value), 'figures', 'value', w));
    if (r.unit) big.appendChild(mk('span', 'tx-unit tx-unit-word', r.unit, 'figures', 'unit', w));
    t.appendChild(big);
    if (r.note) t.appendChild(mk('div', 'tx-tile-note', r.note, 'figures', 'note', w));
    t.appendChild(srcLine(r.confidence, r.source_url, 'figures', w));
    el.appendChild(t);
  });
}

// ----- generic chart engine: chart_meta (one row per chart) + charts (rows: chart_id, series, x, y, y2, label, order)
function fmtBy(fmt, v) {
  if (v === null || v === undefined || Number.isNaN(v)) return '';
  if (fmt === 'pct') return d3.format('.0f')(v) + '%';
  if (fmt === 'pct1') return d3.format('.1f')(v) + '%';
  if (fmt === 'usd_b') return '$' + d3.format(',.1f')(v) + 'B';
  if (fmt === 'usd_m') return '$' + d3.format(',.0f')(v) + 'M';
  if (fmt === 'k') return d3.format(',.0f')(v / 1000) + 'k';
  if (fmt === 'dec1') return d3.format(',.1f')(v);
  return d3.format(',')(Math.round(v * 100) / 100);
}
function renderChartCards(containerId, group) {
  const box = document.getElementById(containerId);
  if (!box) return;
  const ok = prep(box, ['chart_meta', 'charts']);
  if (!ok) { box.classList.add('dash-skeleton'); return; }
  const metas = rows('chart_meta').filter((m) => m.group === group).sort(byOrder);
  const data = rows('charts');
  const jobs = [];
  metas.forEach((m) => {
    const w = 'id=' + encodeURIComponent(m.id);
    const card = mk('div', 'tx-card' + (m.wide === 'Yes' ? ' tx-span' : ''));
    card.appendChild(mk('h3', 'tx-card-title', m.title, 'chart_meta', 'title', w));
    if (m.note) card.appendChild(mk('p', 'tx-card-note', m.note, 'chart_meta', 'note', w));
    const legend = mk('div', 'tx-legend');
    card.appendChild(legend);
    const el = mk('div', 'tx-chart tx-chart-gen');
    el.setAttribute('data-source', 'charts');
    el.style.minHeight = (num(m.height) || 240) + 'px';
    card.appendChild(el);
    card.appendChild(srcLine(m.confidence, m.source_url, 'chart_meta', w));
    box.appendChild(card);
    jobs.push([el, legend, m]);
  });
  // draw only after every card is in the grid, so each chart is sized to its final column width
  jobs.forEach(([el, legend, m]) => {
    try { drawGeneric(el, legend, m, data.filter((r) => r.chart_id === m.id)); el.style.minHeight = ''; } catch (e) { console.error('chart ' + m.id, e); }
  });
}
function axisTicks(x, isLog, span) {
  if (isLog) {
    const [a, b] = x.domain();
    const all = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000].filter((t) => t >= a && t <= b);
    return all.length > 6 ? all.filter((t, i) => i % 2 === 0) : all;
  }
  return x.ticks(Math.max(2, Math.min(6, Math.floor(span / 70))));
}
function seriesList(list) {
  const seen = [];
  list.slice().sort(byOrder).forEach((r) => { if (!seen.includes(r.series)) seen.push(r.series); });
  return seen;
}
function catList(list) {
  const seen = [];
  list.slice().sort(byOrder).forEach((r) => { if (!seen.includes(String(r.x))) seen.push(String(r.x)); });
  return seen;
}
function addLegend(legend, series, colorOf) {
  legend.textContent = '';
  if (series.length < 2) return;
  series.forEach((s) => {
    const item = document.createElement('span');
    const sw = document.createElement('i');
    sw.className = 'tx-swatch';
    sw.style.background = colorOf(s);
    item.append(sw, document.createTextNode(s));
    legend.appendChild(item);
  });
}
function drawGeneric(el, legend, m, list) {
  const kind = m.kind || 'bar';
  const W = Math.max(el.clientWidth, 300);
  const c = dash.colors;
  const series = seriesList(list);
  const colorOf = (s) => (/^Fail/.test(String(s)) ? 'var(--color-bad)' : m.highlight && s !== m.highlight ? 'var(--cds-chart-muted)' : c[Math.max(0, series.indexOf(s)) % c.length]);
  const fmt = (v) => fmtBy(m.fmt, v);
  const tickFmt = (v) => fmt(v).replace(/\.0(?=\D*$)/, '');
  if (kind === 'hbar' || kind === 'range') {
    const items = list.slice().sort(byOrder);
    const rowH = 30, top = 6;
    const svg0 = newSvg(el, W, 10);
    const left = Math.min(W * 0.42, measure(svg0, items.map((r) => String(r.x)), 'tx-lbl') + 14);
    const right = Math.min(W * 0.3, measure(svg0, items.map((r) => r.label || (kind === 'range' ? fmt(num(r.y)) + '–' + fmt(num(r.y2)) : fmt(num(r.y)))), 'tx-val') + 14);
    svg0.remove();
    const H = top + items.length * rowH + 24;
    const svg = newSvg(el, W, H).attr('aria-label', m.title);
    const vals = items.flatMap((r) => [num(r.y), num(r.y2)]).filter((v) => v !== null);
    const lo = m.log_x === 'Yes' ? Math.max(d3.min(vals) * 0.8, 0.01) : Math.min(0, d3.min(vals));
    const x = (m.log_x === 'Yes' ? d3.scaleLog() : d3.scaleLinear()).domain([lo, d3.max(vals) * 1.05]).range([left, W - right]).nice();
    axisTicks(x, m.log_x === 'Yes', W - left - right).forEach((t) => {
      svg.append('line').attr('x1', x(t)).attr('x2', x(t)).attr('y1', top).attr('y2', H - 22).style('stroke', 'var(--cds-chart-grid)');
      svg.append('text').attr('x', x(t)).attr('y', H - 6).attr('text-anchor', 'middle').text(tickFmt(t));
    });
    items.forEach((r, i) => {
      const cy = top + i * rowH + rowH / 2;
      const t = svg.append('text').attr('class', 'tx-lbl').attr('x', 0).attr('y', cy).attr('dy', '0.35em').text(String(r.x));
      fitText(t.node(), left - 12);
      const base = m.log_x === 'Yes' ? x.domain()[0] : 0;
      const a = kind === 'range' ? num(r.y) : base, b = kind === 'range' ? num(r.y2) : num(r.y);
      const col = m.highlight ? (String(r.x) === m.highlight ? c[0] : 'var(--cds-chart-muted)') : (b < a ? 'var(--color-bad)' : (r.series && series.length > 1 ? colorOf(r.series) : c[0]));
      const x0 = x(Math.min(a, b)), x1 = x(Math.max(a, b));
      svg.append('rect').attr('x', x0).attr('y', cy - 7).attr('width', Math.max(3, x1 - x0)).attr('height', 14).attr('rx', 4).style('fill', col);
      svg.append('text').attr('class', 'tx-val').attr('x', x1 + 6).attr('y', cy).attr('dy', '0.35em').text(r.label || (kind === 'range' ? fmt(a) + '–' + fmt(b) : fmt(b)));
      svg.append('rect').attr('x', 0).attr('y', cy - rowH / 2).attr('width', W).attr('height', rowH).style('fill', 'transparent')
        .on('mousemove', (ev) => { const [px, py] = d3.pointer(ev, svg.node()); showTip(el, String(r.x), [r.label || (kind === 'range' ? fmt(a) + '–' + fmt(b) : fmt(b)), r.note || ''], px, py); })
        .on('mouseleave', () => hideTip(el));
    });
    addLegend(legend, series.length > 1 ? series : [], colorOf);
    return;
  }
  if (kind === 'heat') {
    const xs = m.x_order ? m.x_order.split('|') : catList(list), ys = m.y_order ? m.y_order.split('|') : seriesList(list);
    const svg0 = newSvg(el, W, 10);
    const left = Math.min(W * 0.35, measure(svg0, ys, 'tx-lbl') + 14);
    svg0.remove();
    const cell = Math.min(m.wide === 'Yes' ? 170 : 64, (W - left) / xs.length);
    const ch = m.wide === 'Yes' ? 32 : cell * 0.62;
    const top = 34, H = top + ys.length * ch + 6;
    const svg = newSvg(el, W, H).attr('aria-label', m.title);
    const vmax = d3.max(list, (r) => num(r.y)) || 1;
    xs.forEach((xv, i) => {
      const t = svg.append('text').attr('class', 'tx-lbl').attr('x', left + i * cell + cell / 2).attr('y', top - 10).attr('text-anchor', 'middle').text(xv);
      fitText(t.node(), cell - 4);
    });
    ys.forEach((yv, j) => {
      const t = svg.append('text').attr('class', 'tx-lbl').attr('x', 0).attr('y', top + j * ch + ch / 2).attr('dy', '0.35em').text(yv);
      fitText(t.node(), left - 10);
      xs.forEach((xv, i) => {
        const r = list.find((d) => d.series === yv && String(d.x) === xv);
        const v = r ? num(r.y) : null;
        svg.append('rect').attr('x', left + i * cell + 1).attr('y', top + j * ch + 1).attr('width', cell - 2).attr('height', ch - 2).attr('rx', 3)
          .style('fill', v === null ? 'var(--color-panel)' : c[0]).attr('fill-opacity', v === null ? 1 : 0.12 + 0.88 * v / vmax)
          .on('mousemove', (ev) => { const [px, py] = d3.pointer(ev, svg.node()); showTip(el, yv + ' × ' + xv, [v === null ? 'n/a' : fmt(v), r && r.note ? r.note : ''], px, py); })
          .on('mouseleave', () => hideTip(el));
        if (v !== null) svg.append('text').attr('class', 'tx-val').attr('x', left + i * cell + cell / 2).attr('y', top + j * ch + ch / 2).attr('dy', '0.35em').attr('text-anchor', 'middle')
          .style('fill', v / vmax > 0.6 ? 'var(--color-panel)' : 'var(--color-fg)').style('pointer-events', 'none').text(r.label || fmt(v));
      });
    });
    return;
  }
  if (kind === 'scatter') {
    const H = Math.max(260, num(m.height) || 300), padL = 44, padB = 32, top = 10, right = 16;
    const svg = newSvg(el, W, H).attr('aria-label', m.title);
    const xv = list.map((r) => num(r.x)).filter((v) => v !== null && v > 0), yv = list.map((r) => num(r.y)).filter((v) => v !== null);
    const x = (m.log_x === 'Yes' ? d3.scaleLog() : d3.scaleLinear()).domain([d3.min(xv) * 0.7, d3.max(xv) * 1.4]).range([padL, W - right]);
    const y = d3.scaleLinear().domain([Math.min(0, d3.min(yv)), d3.max(yv) * 1.15]).nice().range([H - padB, top]);
    y.ticks(5).forEach((t) => {
      svg.append('line').attr('x1', padL).attr('x2', W - right).attr('y1', y(t)).attr('y2', y(t)).style('stroke', 'var(--cds-chart-grid)');
      svg.append('text').attr('x', padL - 6).attr('y', y(t)).attr('dy', '0.35em').attr('text-anchor', 'end').text(fmtBy(m.fmt, t));
    });
    axisTicks(x, m.log_x === 'Yes', W - padL - right).forEach((t) => {
      svg.append('text').attr('x', x(t)).attr('y', H - 12).attr('text-anchor', 'middle').text(fmtBy(m.x_fmt, t));
    });
    if (m.x_title) svg.append('text').attr('x', W - right).attr('y', H - 1).attr('text-anchor', 'end').text(m.x_title);
    list.forEach((r) => {
      const px = num(r.x), py = num(r.y);
      if (px === null || py === null || px <= 0) return;
      svg.append('circle').attr('cx', x(px)).attr('cy', y(py)).attr('r', 6).style('fill', colorOf(r.series)).attr('fill-opacity', 0.85).style('stroke', 'var(--color-panel)').attr('stroke-width', 1.5)
        .on('mousemove', (ev) => { const [qx, qy] = d3.pointer(ev, svg.node()); showTip(el, r.label || String(r.x), [r.series, fmtBy(m.x_fmt, px) + ' · ' + fmtBy(m.fmt, py), r.note || ''], qx, qy); })
        .on('mouseleave', () => hideTip(el));
      const t = svg.append('text').attr('class', 'tx-val').attr('x', x(px) + 9).attr('y', y(py)).attr('dy', '0.35em').style('pointer-events', 'none').text(clip(r.label, 18));
      if (x(px) + 120 > W) t.attr('x', x(px) - 9).attr('text-anchor', 'end');
    });
    addLegend(legend, series, colorOf);
    return;
  }
  // bar (grouped), stack, line
  const cats = catList(list);
  const H = num(m.height) || 240, padL = 48, padB = 34, top = 14, right = 12;
  const svg = newSvg(el, W, H).attr('aria-label', m.title);
  const stacked = kind === 'stack';
  let ymax;
  if (stacked) ymax = d3.max(cats, (cv) => d3.sum(list.filter((r) => String(r.x) === cv), (r) => num(r.y) || 0));
  else ymax = d3.max(list, (r) => num(r.y));
  const ymin = Math.min(0, d3.min(list, (r) => num(r.y)) || 0);
  const yTop = stacked && m.fmt === 'pct' && ymax <= 101 ? 100 : ymax * 1.1 || 1;
  const y = d3.scaleLinear().domain([ymin, yTop]).nice().range([H - padB, top]);
  y.ticks(5).forEach((t) => {
    svg.append('line').attr('x1', padL).attr('x2', W - right).attr('y1', y(t)).attr('y2', y(t)).style('stroke', 'var(--cds-chart-grid)');
    svg.append('text').attr('x', padL - 6).attr('y', y(t)).attr('dy', '0.35em').attr('text-anchor', 'end').text(tickFmt(t));
  });
  const x = d3.scaleBand().domain(cats).range([padL, W - right]).padding(kind === 'line' ? 0 : 0.22);
  const every = Math.ceil(cats.length / Math.max(1, Math.floor((W - padL) / 54)));
  const yearAxis = kind === 'line' && cats.length > 2 && cats.every((cv) => /^\d{4}$/.test(cv));
  const xYear = yearAxis ? d3.scaleLinear().domain(d3.extent(cats, (cv) => +cv)).range([x(cats[0]) + x.bandwidth() / 2, x(cats[cats.length - 1]) + x.bandwidth() / 2]) : null;
  let lastTick = -Infinity;
  cats.forEach((cv, i) => {
    if (yearAxis ? xYear(+cv) - lastTick < 40 : i % every) return;
    if (yearAxis) lastTick = xYear(+cv);
    const t = svg.append('text').attr('x', yearAxis ? xYear(+cv) : x(cv) + x.bandwidth() / 2).attr('y', H - 14).attr('text-anchor', 'middle').text(cv);
    fitText(t.node(), x.bandwidth() * every - 2);
  });
  if (kind === 'line') {
    const px = (cv) => (yearAxis ? xYear(+cv) : x(cv) + x.bandwidth() / 2);
    series.forEach((s) => {
      const pts = cats.map((cv) => { const r = list.find((d) => d.series === s && String(d.x) === cv); return r && num(r.y) !== null ? [px(cv), y(num(r.y)), r] : null; }).filter(Boolean);
      svg.append('path').attr('d', d3.line()(pts.map((p) => [p[0], p[1]]))).attr('fill', 'none').style('stroke', colorOf(s)).attr('stroke-width', 2.5);
      pts.forEach((p) => svg.append('circle').attr('cx', p[0]).attr('cy', p[1]).attr('r', 3.5).style('fill', colorOf(s))
        .on('mousemove', (ev) => { const [qx, qy] = d3.pointer(ev, svg.node()); showTip(el, s + ' · ' + p[2].x, [p[2].label || fmt(num(p[2].y)), p[2].note || ''], qx, qy); })
        .on('mouseleave', () => hideTip(el)));
      const last = pts[pts.length - 1];
      if (last && series.length <= 4) svg.append('text').attr('class', 'tx-val').attr('x', Math.min(last[0] + 4, W - 40)).attr('y', last[1] - 8).text(last[2].label || fmt(num(last[2].y)));
    });
  } else {
    const inner = d3.scaleBand().domain(series).range([0, x.bandwidth()]).padding(0.08);
    cats.forEach((cv) => {
      let acc = 0;
      series.forEach((s) => {
        const r = list.find((d) => d.series === s && String(d.x) === cv);
        if (!r || num(r.y) === null) return;
        const v = num(r.y);
        const bx = stacked ? x(cv) : x(cv) + inner(s);
        const bw = stacked ? x.bandwidth() : inner.bandwidth();
        const y0 = stacked ? y(acc + v) : y(Math.max(0, v));
        const h = stacked ? y(acc) - y(acc + v) : Math.abs(y(v) - y(0));
        acc += v;
        svg.append('rect').attr('x', bx).attr('y', y0).attr('width', bw).attr('height', Math.max(0, h - (stacked ? 1 : 0))).attr('rx', stacked ? 1 : 3)
          .style('fill', colorOf(s))
          .on('mousemove', (ev) => { const [qx, qy] = d3.pointer(ev, svg.node()); showTip(el, (series.length > 1 ? s + ' · ' : '') + cv, [r.label || fmt(v), r.note || ''], qx, qy); })
          .on('mouseleave', () => hideTip(el));
        if (!stacked && cats.length * series.length <= 14) svg.append('text').attr('class', 'tx-val').attr('x', bx + bw / 2).attr('y', y0 - 4).attr('text-anchor', 'middle').style('pointer-events', 'none').text(r.label || fmt(v));
      });
    });
  }
  addLegend(legend, series, colorOf);
}

function renderPlatforms() {
  const el = document.getElementById('prec-board');
  if (!prep(el, ['platforms'])) return;
  const outcomes = [['thriving', 'Thriving'], ['solid', 'Solid'], ['mixed', 'Mixed'], ['struggling', 'Struggling'], ['failed/restructured', 'Failed or restructured'], ['exited', 'Exited or merged']];
  const list = rows('platforms');
  outcomes.forEach(([o, label]) => {
    const items = list.filter((r) => r.outcome === o);
    if (!items.length) return;
    const col = mk('div', 'tx-board-col');
    col.setAttribute('data-outcome', o);
    col.appendChild(mk('div', 'tx-board-head', label));
    items.forEach((r) => {
      const w = 'id=' + encodeURIComponent(r.id);
      const it = mk('article', 'tx-board-item');
      const name = mk('div', 'tx-strong');
      const nm = mk('span', null, r.name, 'platforms', 'name', w);
      if (safeUrl(r.website)) { const a = linkTo(r.website, ''); a.appendChild(nm); name.appendChild(a); } else name.appendChild(nm);
      it.appendChild(name);
      const chips = mk('div', 'tx-chips');
      chips.appendChild(mk('span', 'tx-chip', r.type, 'platforms', 'type', w));
      chips.appendChild(mk('span', 'tx-chip', r.model, 'platforms', 'model', w));
      if (r.units) chips.appendChild(mk('span', 'tx-chip', r.units, 'platforms', 'units', w));
      it.appendChild(chips);
      const facts = mk('div', 'tx-card-note');
      [['revenue', r.revenue], ['margin', r.margin]].forEach(([f, v], i) => {
        if (!v) return;
        if (facts.childNodes.length) facts.appendChild(document.createTextNode(' · '));
        facts.appendChild(mk('span', null, v, 'platforms', f, w));
      });
      if (facts.childNodes.length) it.appendChild(facts);
      it.appendChild(mk('p', null, r.lesson, 'platforms', 'lesson', w));
      const d = document.createElement('details');
      d.appendChild(mk('summary', null, 'Evidence and deals'));
      d.appendChild(mk('p', null, r.evidence, 'platforms', 'evidence', w));
      if (r.acquisitions) d.appendChild(mk('p', null, r.acquisitions, 'platforms', 'acquisitions', w));
      d.appendChild(sourceLinks(r.sources));
      it.appendChild(d);
      col.appendChild(it);
    });
    el.appendChild(col);
  });
}

const CRIT = [['c_recurring', 'Recurring maintenance'], ['c_customer', 'Large regional or national customer'], ['c_specialized', 'Specialized labor and equipment'], ['c_avoid', 'Avoids low-bid and fixed-price work'], ['c_independent', 'Independent (not sponsor-owned)']];
function critDot(v) {
  const s = mk('span', 'tx-dot');
  s.setAttribute('data-v', v || 'unknown');
  s.textContent = v === 'unknown' || !v ? '?' : '';
  return s;
}
function candFilter(r) {
  const u = document.getElementById('cand-unit').value;
  const q = (document.getElementById('cand-search').value || '').trim().toLowerCase();
  if (u && r.unit !== u) return false;
  if (document.getElementById('cand-platform').checked && r.grade !== 'Platform') return false;
  if (document.getElementById('cand-free').checked && r.c_independent === 'no') return false;
  if (q && !['name', 'hq', 'services', 'customers', 'ownership', 'size_hint'].some((k) => String(r[k] || '').toLowerCase().includes(q))) return false;
  return true;
}
function renderCandidates() {
  const el = document.getElementById('cand-board');
  const sel = document.getElementById('cand-unit');
  if (!prep(el, ['candidates'])) return;
  const all = rows('candidates');
  if (sel.options.length <= 1) Object.keys(UNIT_LABEL).forEach((u) => { if (all.some((r) => r.unit === u)) { const o = document.createElement('option'); o.value = u; o.textContent = UNIT_LABEL[u]; sel.appendChild(o); } });
  const list = all.filter(candFilter).sort((a, b) => num(b.fit_score) - num(a.fit_score) || String(a.name).localeCompare(String(b.name)));
  if (!list.length) { el.appendChild(mk('p', 'tx-card-note', 'No company matches these filters.')); return; }
  const legend = mk('div', 'tx-dot-legend');
  CRIT.forEach(([, label], i) => { const s = mk('span'); s.appendChild(mk('b', null, String.fromCharCode(65 + i))); s.appendChild(document.createTextNode(' ' + label)); legend.appendChild(s); });
  el.appendChild(legend);
  const grid = mk('div', 'tx-cand-grid');
  list.forEach((r) => {
    const w = 'id=' + encodeURIComponent(r.id);
    const it = mk('article', 'tx-cand');
    const head = mk('div', 'tx-cand-head');
    const nm = mk('span', 'tx-strong', r.name, 'candidates', 'name', w);
    if (safeUrl(r.website)) { const a = linkTo(r.website, ''); a.appendChild(nm); head.appendChild(a); } else head.appendChild(nm);
    const sc = mk('span', 'tx-cand-score', fmtVal(num(r.fit_score)), 'candidates', 'fit_score', w);
    sc.setAttribute('data-score', String(r.fit_score));
    head.appendChild(sc);
    it.appendChild(head);
    const chips = mk('div', 'tx-chips');
    chips.appendChild(mk('span', 'tx-chip', UNIT_LABEL[r.unit] || r.unit));
    const g = mk('span', 'tx-chip', r.grade, 'candidates', 'grade', w);
    g.setAttribute('data-attr', r.grade === 'Platform' ? 'High' : r.grade === 'Add-on' ? 'Medium' : 'Low');
    chips.appendChild(g);
    if (r.hq_short) chips.appendChild(mk('span', 'tx-chip', r.hq_short, 'candidates', 'hq_short', w));
    it.appendChild(chips);
    it.appendChild(mk('p', 'tx-cand-svc', r.services, 'candidates', 'services', w));
    const dots = mk('div', 'tx-dots');
    CRIT.forEach(([f], i) => { const d = mk('span', 'tx-dotwrap'); d.appendChild(mk('b', null, String.fromCharCode(65 + i))); d.appendChild(critDot(r[f])); dots.appendChild(d); });
    it.appendChild(dots);
    const d = document.createElement('details');
    d.appendChild(mk('summary', null, 'Ownership, size, customers and sources'));
    [['hq', 'Headquarters'], ['ownership', 'Ownership'], ['size_hint', 'Size'], ['customers', 'Customers'], ['recurring_evidence', 'Recurring work'], ['red_flags', 'Red flags']].forEach(([f, lbl]) => {
      if (!r[f]) return;
      const p = mk('p', 'tx-card-note');
      p.appendChild(mk('b', null, lbl + ': '));
      p.appendChild(mk('span', null, r[f], 'candidates', f, w));
      d.appendChild(p);
    });
    d.appendChild(sourceLinks(r.sources));
    it.appendChild(d);
    grid.appendChild(it);
  });
  el.appendChild(grid);
}

function renderRanking() {
  const el = document.getElementById('rank-list');
  if (!prep(el, ['unit_ranking'])) return;
  rows('unit_ranking').slice().sort((a, b) => num(a.rank) - num(b.rank)).forEach((r) => {
    const w = 'id=' + encodeURIComponent(r.id);
    const card = mk('article', 'tx-play');
    const top = mk('div', 'tx-play-top');
    top.appendChild(mk('span', 'tx-play-rank', fmtVal(num(r.rank)), 'unit_ranking', 'rank', w));
    top.appendChild(mk('h4', 'tx-play-title', r.unit, 'unit_ranking', 'unit', w));
    card.appendChild(top);
    const chips = mk('div', 'tx-chips');
    const a = mk('span', 'tx-chip', r.attractiveness, 'unit_ranking', 'attractiveness', w);
    a.setAttribute('data-attr', r.attractiveness);
    chips.appendChild(a);
    card.appendChild(chips);
    const parts = String(r.why || '').split(/\s*•\s*/).filter(Boolean);
    card.appendChild(mk('p', null, parts[0], 'unit_ranking', 'why', w));
    if (parts.length > 1) {
      const ul = mk('ul', 'tx-bul');
      parts.slice(1).forEach((t) => ul.appendChild(mk('li', null, t)));
      card.appendChild(ul);
    }
    const dl = mk('dl', 'tx-dl');
    [['Market size', 'tam'], ['Maintenance share', 'mro_share'], ['Margins', 'margin_range'], ['Fragmentation', 'fragmentation'], ['Competition', 'competition'], ['Candidates', 'candidates']].forEach(([lbl, f]) => {
      if (!r[f]) return;
      dl.appendChild(mk('dt', null, lbl));
      dl.appendChild(mk('dd', null, r[f], 'unit_ranking', f, w));
    });
    const d = document.createElement('details');
    d.appendChild(mk('summary', null, 'Size, margins, competition and candidates'));
    d.appendChild(dl);
    card.appendChild(d);
    el.appendChild(card);
  });
}

function renderPlan() {
  const ids = ['plan-first', 'plan-vi', 'plan-risks', 'plan-signals', 'caveats-text'];
  const els = ids.map((i) => document.getElementById(i));
  const ok = els.map((e) => prep(e, ['plan']));
  if (!ok[0]) return;
  const [first, vi, risks, signals, cav] = els;
  rows('plan').sort(byOrder).forEach((r) => {
    const w = 'id=' + encodeURIComponent(r.id);
    if (r.kind === 'first_unit') {
      first.appendChild(mk('div', 'tx-bottom-label', r.heading, 'plan', 'heading', w));
      first.appendChild(mk('p', 'tx-bottom-text', r.body, 'plan', 'body', w));
    } else if (r.kind === 'rationale') first.appendChild(mk('p', 'tx-pre', r.body, 'plan', 'body', w));
    else if (r.kind === 'vi' || r.kind === 'risk' || r.kind === 'signal') {
      const li = mk('li');
      li.appendChild(mk('span', 'tx-strong', r.heading, 'plan', 'heading', w));
      li.appendChild(document.createTextNode(' — '));
      li.appendChild(mk('span', null, r.body, 'plan', 'body', w));
      ({ vi: vi, risk: risks, signal: signals })[r.kind].appendChild(li);
    } else if (r.kind === 'caveat') cav.appendChild(mk('span', null, r.body, 'plan', 'body', w));
  });
}

const WATCH_TABLE = {
  id: 'watch-table', src: 'watchlist', key: 'id',
  cols: [
    { field: 'when', label: 'When', sortBy: 'sort_date' },
    { field: 'item', label: 'What', sortable: false, cls: 'tx-pre' },
    { field: 'why', label: 'Why it matters', sortable: false, cls: 'tx-pre' },
  ],
  defaultSort: (a, b) => (a.sort_date < b.sort_date ? -1 : 1),
};
const SCALED_TABLE = {
  id: 'scaled-table', src: 'scaled', key: 'id',
  cols: [
    { field: 'company', label: 'Company' },
    { field: 'revenue_label', label: 'Utility-services revenue', sortBy: 'revenue_usd_b' },
    { field: 'units', label: 'Units' },
    { field: 'ownership', label: 'Ownership', cls: 'tx-hide-sm' },
    { field: 'website', label: 'Website', sortable: false },
    { field: 'note', label: 'Note', cls: 'tx-hide-sm', sortable: false },
  ],
  defaultSort: (a, b) => (num(b.revenue_usd_b) || 0) - (num(a.revenue_usd_b) || 0),
};
const PL_TABLE = {
  id: 'pl-table', src: 'pl', key: 'id',
  cols: [
    { field: 'line', label: 'Line', sortable: false },
    { field: 's50', label: 'Small', sortable: false },
    { field: 's150', label: 'Mid', sortable: false },
    { field: 's500', label: 'Large', sortable: false },
    { field: 'drivers', label: 'What drives it', sortable: false, cls: 'tx-hide-sm' },
  ],
  defaultSort: byOrder,
};
const SYN_TABLE = {
  id: 'syn-table', src: 'synergies', key: 'id',
  cols: [
    { field: 'lever', label: 'Synergy in the deck' },
    { field: 'verdict', label: 'Verdict', cellClass: (r) => 'i-' + ({ Real: 'High', Partial: 'Medium', Overstated: 'Low' }[r.verdict] || 'Low') },
    { field: 'quant', label: 'Size', sortable: false },
    { field: 'evidence', label: 'Evidence', sortable: false, cls: 'tx-hide-sm' },
  ],
  defaultSort: byOrder,
};
const CAND_TABLE = {
  id: 'cand-table', src: 'candidates', key: 'id',
  cols: [
    { field: 'name', label: 'Company' },
    { field: 'unit', label: 'Unit' },
    { field: 'grade', label: 'Grade' },
    { field: 'fit_score', label: 'Fit', num: true, cls: 'tx-num' },
    { field: 'hq', label: 'HQ', cls: 'tx-hide-sm' },
    { field: 'ownership', label: 'Ownership', cls: 'tx-hide-sm', sortable: false },
    { field: 'size_hint', label: 'Size', sortable: false, cls: 'tx-hide-sm' },
    { field: 'website', label: 'Website', sortable: false },
  ],
  defaultSort: (a, b) => String(a.unit).localeCompare(String(b.unit)) || num(b.fit_score) - num(a.fit_score),
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

document.getElementById('vc-select').addEventListener('change', (ev) => vcSelect(ev.target.value || null));
document.getElementById('vc-fulton').addEventListener('change', () => { drawValueChain(); scheduleGlossary(); });
document.getElementById('vc-clear').addEventListener('click', () => vcSelect(null));
document.getElementById('vc-prospect').addEventListener('click', () => vcSelect('prospect'));
document.getElementById('gloss-search').addEventListener('input', () => renderTable(GLOSS_TABLE));
document.getElementById('src-search').addEventListener('input', () => renderTable(SRC_TABLE));
['cand-unit', 'cand-platform', 'cand-free', 'cand-search'].forEach((id) => document.getElementById(id).addEventListener(id === 'cand-search' ? 'input' : 'change', () => { renderCandidates(); scheduleGlossary(); }));

let linked = false;
function renderAll() {
  [
    fillMarks, renderSummary, drawValueChain, renderFindings, renderSteps, renderProfile,
    () => renderTiles('tiles-market', 'market'),
    () => renderChartCards('charts-aging', 'aging'), () => renderChartCards('charts-demand', 'demand'),
    () => renderChartCards('charts-competition', 'competition'), () => renderChartCards('charts-economics', 'economics'),
    () => renderChartCards('charts-synergies', 'synergies'), () => renderChartCards('charts-candidates', 'candidates'),
    renderWatchTimeline, renderPlatforms, renderCandidates, renderRanking, renderPlan,
    () => renderTable(WATCH_TABLE), () => renderTable(SCALED_TABLE), () => renderTable(PL_TABLE), () => renderTable(SYN_TABLE),
    () => renderTable(CAND_TABLE), () => renderTable(SRC_TABLE), () => renderTable(GLOSS_TABLE),
  ].forEach((f) => {
    try { f(); } catch (e) { console.error(e); }
  });
  glHide(true);
  scheduleGlossary();
}
