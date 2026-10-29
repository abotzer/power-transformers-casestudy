"""Build a standalone static copy of a dashboard report for self-hosting.

Usage: python3 -I tools/build_site.py <dashboard/index.html> <data_dir> <out_dir> [title]
Writes <out_dir>/index.html (page + embedded datasets + a small `dash` runtime shim),
<out_dir>/favicon.svg. The page gets a small link back to the report catalog (../).
"""
import json
import os
import sys

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>%TITLE%</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
<style>
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Source Serif 4", Georgia, serif;
  --color-bg: #faf9f5; --color-panel: #ffffff; --color-fg: #1f1e1d; --color-fg-muted: #6b6a66;
  --color-border-line: #e4e1d8; --color-ok: #2f7d4f; --color-warn: #c27c0e; --color-bad: #b4372f;
  --cds-border: #d9d5ca; --cds-surface-popover: #ffffff; --cds-shadow-popover: 0 8px 24px rgba(0,0,0,.12);
  --cds-text-secondary: #4a4945; --cds-chart-axis: #a3a09a; --cds-chart-grid: #ece9e1; --cds-chart-muted: #b9b5ab; --cds-chart-reference: #8a877f;
  --cds-font-size-caption: 12px; --cds-font-size-body: 14px; --cds-font-size-heading: 16px; --cds-font-size-title: 26px; --cds-font-weight-medium: 600;
  --cds-gap-xs: 4px; --cds-gap-sm: 8px; --cds-gap-md: 16px; --cds-gap-lg: 24px; --cds-gap-xl: 32px;
  --cds-pad-xs: 4px; --cds-pad-sm: 8px; --cds-pad-md: 12px; --cds-pad-lg: 20px; --cds-radius: 10px;
  --cds-dur-slow: 400ms; --cds-ease-out: cubic-bezier(.2,.8,.2,1);
  --s1: #2c6fbb; --s2: #d9822b; --s3: #3a9a6a; --s4: #8e5bb5; --s5: #c94f6d; --s6: #3fa3b5; --s7: #9a8a2e; --s8: #6b7a8f;
}
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #1c1b19; --color-panel: #262522; --color-fg: #ecebe6; --color-fg-muted: #a6a39b;
    --color-border-line: #3a3833; --color-ok: #5cbf86; --color-warn: #e6a23c; --color-bad: #e06a5f;
    --cds-border: #45423c; --cds-surface-popover: #2d2c28; --cds-shadow-popover: 0 8px 24px rgba(0,0,0,.5);
    --cds-text-secondary: #cfccc4; --cds-chart-axis: #77746c; --cds-chart-grid: #33312d; --cds-chart-muted: #6f6c64; --cds-chart-reference: #8f8c84;
    --s1: #6aa5e8; --s2: #f0a35a; --s3: #67c49a; --s4: #b58ad8; --s5: #e7849c; --s6: #6cc8d8; --s7: #c9b75a; --s8: #9aa7b8;
  }
}
html, body { margin: 0; background: var(--color-bg); color: var(--color-fg); font-family: var(--font-anthropic-sans); font-size: var(--cds-font-size-body); }
.ws-catalog { padding: 12px clamp(16px, 2.5vw, 40px) 0; font-size: 13px; }
.ws-catalog a { color: var(--color-fg-muted); text-decoration: none; }
.ws-catalog a:hover { color: var(--color-fg); text-decoration: underline; }
#dash-root { padding: 24px clamp(16px, 2.5vw, 40px) 48px; }
.dash-skeleton { position: relative; min-height: 2rem; border-radius: var(--cds-radius); background: linear-gradient(90deg, var(--color-border-line) 0%, var(--color-panel) 50%, var(--color-border-line) 100%); background-size: 200% 100%; animation: dash-sk 1.4s linear infinite; color: transparent; }
@keyframes dash-sk { from { background-position: 200% 0; } to { background-position: -200% 0; } }
</style>
</head>
<body>
<nav class="ws-catalog"><a href="../">&larr; All reports</a></nav>
<div id="dash-root">
"""

SHIM = """<script>
(function () {
  const DATA = %s;
  const calcs = [];
  const results = {};
  const listeners = [];
  function data(id) {
    if (Object.prototype.hasOwnProperty.call(DATA, id)) {
      const d = DATA[id];
      return { status: 'ok', data: d, rows: d, columns: Array.isArray(d) && d.length ? Object.keys(d[0]) : [], refreshing: false, meta: [] };
    }
    if (Object.prototype.hasOwnProperty.call(results, id)) return { status: 'ok', data: results[id], rows: results[id], columns: [], refreshing: false, meta: [] };
    return { status: 'missing', data: [], rows: [], columns: [], refreshing: false, meta: [] };
  }
  function runCalcs() {
    calcs.forEach((c) => {
      try { results[c.id] = c.fn.apply(null, c.inputs.map((i) => data(i).data)); } catch (e) { console.error('calc ' + c.id, e); }
    });
  }
  let queued = false;
  function fire() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => { queued = false; listeners.forEach((f) => { try { f(); } catch (e) { console.error(e); } }); });
  }
  window.dash = {
    data: data,
    calc: (id, spec) => { calcs.push({ id: id, inputs: spec.inputs || [], fn: spec.fn }); },
    loader: () => {},
    onData: (fn) => { listeners.push(fn); runCalcs(); try { fn(); } catch (e) { console.error(e); } },
    colors: ['var(--s1)', 'var(--s2)', 'var(--s3)', 'var(--s4)', 'var(--s5)', 'var(--s6)', 'var(--s7)', 'var(--s8)'],
    refresh: () => {},
    params: () => ({}), setParams: () => {}, resetParams: () => {},
    setLink: (name) => { try { history.replaceState(null, '', '#' + name); } catch (e) {} },
  };
  let w = window.innerWidth;
  window.addEventListener('resize', () => { if (window.innerWidth !== w) { w = window.innerWidth; fire(); } });
})();
</script>
"""


def scrub(obj):
    """Drop links to the working repository and local file paths from the published data."""
    if isinstance(obj, dict):
        return {k: scrub(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [scrub(v) for v in obj]
    if isinstance(obj, str):
        if "github.com/abotzer/" in obj:
            return ""
        if "/home/user/" in obj:
            return "Baseline market map (S)"
    return obj


def main(page_path, data_dir, out, title="Whitesail Labs report"):
    page = open(page_path).read()
    data = {}
    for f in sorted(os.listdir(data_dir)):
        if f.endswith(".json"):
            data[f[:-5]] = json.load(open(os.path.join(data_dir, f)))
    data = scrub(data)
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (HEAD.replace("%TITLE%", title) + SHIM % blob + page).replace("--font-anthropic-", "--font-") + "\n</div>\n</body>\n</html>\n"
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(html)
    logo = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "shared", "brand", "whitesail-logo.svg")
    if os.path.exists(logo):
        open(os.path.join(out, "favicon.svg"), "w").write(open(logo).read())
    print("wrote", os.path.join(out, "index.html"), len(html), "bytes;", len(data), "datasets")


if __name__ == "__main__":
    main(*sys.argv[1:5])
