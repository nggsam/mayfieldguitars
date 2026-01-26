## 2025-02-18 - CSS Import Blocking in Themes
**Learning:** The `bnw` theme used `@import` in LESS files to load Google Fonts. This compiles to `@import` in the CSS, causing blocking requests and chained latency, which is a significant bottleneck for First Contentful Paint (FCP).
**Action:** Always inspect LESS/SASS source files in Nikola themes for external `@import`s. Move them to `<link rel="stylesheet">` in the HTML template (e.g., `zzz_helper.tmpl`) with `preconnect` and `display: swap`.
