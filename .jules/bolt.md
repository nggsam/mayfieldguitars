## 2025-05-15 - Font Loading Optimization
**Learning:** Nikola themes often bundle CSS files, so optimizing source CSS files (like `bnw-generated.css`) is necessary but requires understanding the bundling process (`USE_BUNDLES` in `conf.py`). Moving from `@import` in CSS to `<link>` in templates is a high-impact, low-risk optimization for static sites.
**Action:** When working with Nikola, always check `conf.py` for bundle settings and `zzz_helper.tmpl` (or similar) for the `<head>` construction to optimize Critical Rendering Path.
